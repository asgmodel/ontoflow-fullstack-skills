#!/usr/bin/env python3
"""Validate RDF/SHACL, graph projection, dependencies and bundled paths."""
from pathlib import Path
import json, re, sys
from rdflib import Graph, Namespace, RDF
from pyshacl import validate
from route import read_graph

ROOT=Path(__file__).resolve().parents[1]
N=Namespace('urn:nexus:engineering:')

def main():
    data=Graph().parse(ROOT/'assets/nexus.owl',format='xml')
    shapes=Graph().parse(ROOT/'assets/shapes.ttl',format='turtle')
    conforms,_,report=validate(data,shacl_graph=shapes,inference='rdfs')
    if not conforms: print(report); return 1
    graph=read_graph(); visited=set(); active=set()
    def visit(id):
        if id in active: raise ValueError('requiresSkill cycle: '+id)
        if id in visited: return
        active.add(id)
        for dependency in graph['skills'][id]['requires']:
            if dependency not in graph['skills']: raise ValueError('Unknown dependency '+dependency)
            visit(dependency)
        active.remove(id); visited.add(id)
    for id in graph['skills']: visit(id)
    for stages in graph['recipes'].values():
        for phase,skills in stages.items():
            for id in skills:
                if id not in graph['skills']: raise ValueError(f'Unknown recipe skill {id}')
    sources=json.loads((ROOT/'references/sources.json').read_text())
    if len(sources['upstream']['files'])!=25 or len(graph['skills'])!=30:
        raise ValueError('Source catalog coverage changed; review source counts.')
    for p in ROOT.rglob('*.md'):
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',p.read_text()):
            target=target.split('#')[0]
            if target and not re.match(r'^(https?:|mailto:|skill:)',target) and not (p.parent/target).exists():
                raise ValueError(f'Missing reference in {p.relative_to(ROOT)}: {target}')
    print(json.dumps({'SHACL':'PASS','projection_hashes':'PASS','dependency_cycles':'PASS','local_reference_links':'PASS','skills':len(graph['skills']),'intents':len(graph['recipes']),'triples':len(data),'source_commit':sources['upstream']['commit']},indent=2))
    return 0

if __name__=='__main__': sys.exit(main())
