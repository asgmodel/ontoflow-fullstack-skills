#!/usr/bin/env python3
"""Build integrity metadata and a Turtle mirror from the authoritative OWL file."""
from pathlib import Path
import json
from rdflib import Graph
from owl_reader import load_ontology

ROOT=Path(__file__).resolve().parents[1]

def compile_graph():
    path=ROOT/'assets/nexus.owl'
    result=load_ontology(path,ROOT)
    graph=Graph().parse(path,format='xml')
    graph.serialize(ROOT/'assets/nexus.ttl',format='turtle')
    mirror=ROOT/'assets/nexus.ttl'
    mirror.write_text(mirror.read_text().rstrip()+'\n')
    (ROOT/'assets/graph.json').write_text(json.dumps(result,indent=2)+'\n')
    return result

if __name__=='__main__':
    result=compile_graph();print(f"Compiled {len(result['skills'])} skills from assets/nexus.owl.")
