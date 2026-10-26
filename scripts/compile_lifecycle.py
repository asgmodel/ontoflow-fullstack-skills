#!/usr/bin/env python3
"""Regenerate the lifecycle Turtle projection from canonical flat RDF/XML."""
from pathlib import Path
from rdflib import Graph
ROOT = Path(__file__).resolve().parents[1]
if __name__ == '__main__':
    owl = ROOT/'skills/ontolink-skills/assets/ontolink.owl'
    Graph().parse(owl, format='xml').serialize(owl.with_suffix('.ttl'), format='turtle')
    mirror = owl.with_suffix('.ttl')
    mirror.write_text(mirror.read_text().rstrip()+'\n')
    print('Lifecycle projection regenerated')
