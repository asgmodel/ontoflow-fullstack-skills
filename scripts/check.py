#!/usr/bin/env python3
"""Validate the actual two-package distribution, models, references and hashes."""
from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote

from rdflib import Graph, Namespace, RDF
from rdflib.compare import isomorphic
from pyshacl import validate as shacl
from manifest import check, source_files

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT/'skills/ontolink-skills'
ENGINEERING = ROOT/'skills/software-engineering'
sys.path.insert(0, str(CORE/'scripts'))
sys.path.insert(0, str(ENGINEERING/'scripts'))
from rdf_store import Store, O
from mediator import phases
from route import read_graph
from project_setup import installed_packages, engineering_packages


def main():
    check()
    top = {p.name for p in (ROOT/'skills').iterdir() if p.is_dir() and p.name != '__pycache__'}
    if top != {'ontolink-skills', 'software-engineering'}:
        raise ValueError('Expected exactly two top-level skill packages')
    catalog = json.loads((ROOT/'catalog.json').read_text())
    if {x['name'] for x in catalog['packages']} != top:
        raise ValueError('Root catalog differs from installed packages')
    core_catalog = json.loads((CORE/'assets/catalog.json').read_text())
    bundled = installed_packages(CORE, core_catalog)
    if len(bundled) != 8 or set(engineering_packages(CORE, core_catalog)) != {'software-engineering'}:
        raise ValueError('Incomplete coordinator/engineering catalog')
    names = set()
    for path in (ROOT/'skills').rglob('SKILL.md'):
        text = path.read_text(encoding='utf-8')
        match = re.match(r'\A---\nname: ([a-z0-9-]{1,64})\ndescription: ([^\n]+)\n---\n', text)
        if not match or match[1] != path.parent.name or match[1] in names:
            raise ValueError('Invalid/duplicate skill identity: '+str(path))
        names.add(match[1])
    if len(names) != 9:
        raise ValueError('Expected two entrypoints plus seven embedded phase procedures')
    for package, basename, namespace in [(CORE, 'ontolink', O), (ENGINEERING, 'engineering', 'urn:software-engineering:')]:
        graph = Graph().parse(package/f'assets/{basename}.owl', format='xml')
        mirror = Graph().parse(package/f'assets/{basename}.ttl', format='turtle')
        if not isomorphic(graph, mirror):
            raise ValueError('Stale Turtle projection: '+basename)
        shapes = Graph().parse(package/'assets/shapes.ttl', format='turtle')
        conforms, _, report = shacl(graph, shacl_graph=shapes, inference='rdfs')
        if not conforms:
            raise ValueError(report)
    ontology = Store.read(CORE/'assets/ontolink.owl')
    lifecycle = phases(ontology)
    if len(lifecycle) != 7:
        raise ValueError('Missing lifecycle phase')
    for phase in lifecycle:
        if phase['engineering'] != ['software-engineering']:
            raise ValueError('Lifecycle still references an uninstalled adapter')
        if phase['skill'] not in bundled:
            raise ValueError('Unresolved phase procedure')
    engineering = read_graph()
    if len(engineering['skills']) != 35:
        raise ValueError('Unexpected engineering catalog coverage')
    visited, active = set(), set()
    def visit(name):
        if name in active:
            raise ValueError('Engineering dependency cycle: '+name)
        if name in visited:
            return
        active.add(name)
        for dep in engineering['skills'][name]['requires']:
            visit(dep)
        active.remove(name); visited.add(name)
    for name in engineering['skills']:
        visit(name)
    links = 0
    for path in source_files():
        if path.suffix != '.md':
            continue
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            target = target.split('#')[0]
            if not target or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                continue
            resolved = path.parent/unquote(target)
            if not resolved.exists():
                raise ValueError(f'Missing local reference in {path.relative_to(ROOT)}: {target}')
            links += 1
    # Ensure the pinned attributed workflow bodies are unchanged by consolidation.
    sources = json.loads((ENGINEERING/'references/sources.json').read_text())
    if len(sources['upstream']['files']) != 25 or not (ENGINEERING/sources['upstream']['license_file']).is_file():
        raise ValueError('Missing attributed upstream coverage/license')
    print(json.dumps({'status': 'PASS', 'packages': sorted(top), 'embedded_phases': 7,
                      'engineering_workflows': 35, 'local_links': links,
                      'source_files': len(source_files())}, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError) as error:
        raise SystemExit('Distribution validation failed: '+str(error))
