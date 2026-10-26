#!/usr/bin/env python3
"""Validate engineering source and an instructions-only external dependency loader."""
from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote
from rdflib import Graph
from rdflib.compare import isomorphic
from pyshacl import validate as shacl
from manifest import check, source_files

ROOT = Path(__file__).resolve().parents[1]
ENGINEERING = ROOT/'skills/software-engineering'
sys.path.insert(0, str(ENGINEERING/'scripts'))
from route import read_graph


def main():
    check()
    loader = ROOT/'skills/ontolink-skills'
    if {p.relative_to(loader).as_posix() for p in loader.rglob('*') if p.is_file()} != {'README.md'}:
        raise ValueError('OntoLink folder must contain only loading instructions')
    if set(p.name for p in (ROOT/'skills').iterdir() if p.is_dir()) != {'software-engineering','ontolink-skills'}:
        raise ValueError('Unexpected top-level package/loader directory')
    catalog = json.loads((ROOT/'catalog.json').read_text())
    if [x['name'] for x in catalog['packages']] != ['software-engineering']:
        raise ValueError('Only the engineering skill is bundled')
    if catalog['external_dependencies'][0]['bundled'] is not False:
        raise ValueError('OntoLink must remain external')
    entries = list((ROOT/'skills').rglob('SKILL.md'))
    if entries != [ENGINEERING/'SKILL.md']:
        raise ValueError('Unexpected copied/duplicate skill entrypoint')
    text = entries[0].read_text()
    if not re.match(r'\A---\nname: software-engineering\ndescription: [^\n]+\n---\n', text):
        raise ValueError('Invalid engineering identity')
    graph = Graph().parse(ENGINEERING/'assets/engineering.owl', format='xml')
    mirror = Graph().parse(ENGINEERING/'assets/engineering.ttl', format='turtle')
    if not isomorphic(graph, mirror):
        raise ValueError('Stale engineering Turtle projection')
    conforms, _, report = shacl(graph, shacl_graph=Graph().parse(ENGINEERING/'assets/shapes.ttl'), inference='rdfs')
    if not conforms:
        raise ValueError(report)
    engineering = read_graph()
    if len(engineering['skills']) != 35 or set(engineering['lifecycle_mapping']) != {
            'urn:ontolink:'+phase for phase in ['discover','design','plan','build','verify','deliver','monitor']}:
        raise ValueError('Incomplete engineering coverage or external lifecycle bindings')
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
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
            target = target.split('#')[0]
            if not target or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                continue
            if not (path.parent/unquote(target)).exists():
                raise ValueError(f'Missing local link in {path.relative_to(ROOT)}: {target}')
            links += 1
    sources = json.loads((ENGINEERING/'references/sources.json').read_text())
    if len(sources['upstream']['files']) != 25 or not (ENGINEERING/sources['upstream']['license_file']).is_file():
        raise ValueError('Missing engineering attribution')
    print(json.dumps({'status':'PASS','bundled_packages':['software-engineering'],
                      'external_dependency':'ontolink-skills','loader_files':1,
                      'engineering_workflows':35,'local_links':links,
                      'source_files':len(source_files())}, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError) as error:
        raise SystemExit('Distribution validation failed: '+str(error))
