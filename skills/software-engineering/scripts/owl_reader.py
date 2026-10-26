#!/usr/bin/env python3
"""Read Software Engineering named RDF/XML nodes directly, with no RDF runtime dependency.

This constrained parser supports the generated ontology's named typed nodes,
resource properties, nested named nodes and literals. It rejects other RDF/XML
constructs explicitly. It is not a general RDF/XML parser or an OWL reasoner.
"""
import hashlib
from pathlib import Path
import xml.etree.ElementTree as ET

RDF='http://www.w3.org/1999/02/22-rdf-syntax-ns#'
OWL='http://www.w3.org/2002/07/owl#'
NX='urn:software-engineering:'

def uri(tag):
    if not tag.startswith('{'): raise ValueError('Unqualified RDF/XML element.')
    ns,name=tag[1:].split('}',1);return ns+name

def parse_named_rdfxml(path):
    raw=Path(path).read_bytes()
    if b'<!DOCTYPE' in raw.upper() or b'<!ENTITY' in raw.upper(): raise ValueError('DTD/entities are unsupported.')
    try: root=ET.fromstring(raw)
    except ET.ParseError as error: raise ValueError(f'Invalid OWL RDF/XML: {error}') from error
    if root.tag!='{'+RDF+'}RDF' or root.attrib: raise ValueError('Expected rdf:RDF with absolute named resources and no root attributes.')
    triples=set()
    def node(element):
        subject=element.get('{'+RDF+'}about')
        if not subject or ':' not in subject or set(element.attrib)!={'{'+RDF+'}about'}: raise ValueError('Use absolute rdf:about named resources; blank nodes/subject attributes are unsupported.')
        if element.tag!='{'+RDF+'}Description': triples.add((subject,RDF+'type','resource',uri(element.tag)))
        for prop in element:
            predicate=uri(prop.tag);resource=prop.get('{'+RDF+'}resource')
            if resource is not None:
                if len(prop) or set(prop.attrib)!={'{'+RDF+'}resource'} or (prop.text or '').strip() or ':' not in resource: raise ValueError('Malformed/unsupported resource property.')
                triples.add((subject,predicate,'resource',resource))
            elif len(prop):
                if prop.attrib or len(prop)!=1 or (prop.text or '').strip(): raise ValueError('Unsupported RDF/XML property structure.')
                triples.add((subject,predicate,'resource',node(prop[0])))
            else:
                if set(prop.attrib)-{'{'+RDF+'}datatype','{http://www.w3.org/XML/1998/namespace}lang'}: raise ValueError('Unsupported literal attributes.')
                triples.add((subject,predicate,'literal',prop.text or ''))
        return subject
    for element in root: node(element)
    return triples

def load_ontology(path,skill_root):
    path=Path(path);skill_root=Path(skill_root).resolve();triples=parse_named_rdfxml(path)
    def values(s,p,kind=None): return sorted({o for a,b,k,o in triples if a==s and b==p and (kind is None or kind==k)})
    def one(s,p,kind=None):
        found=values(s,p,kind)
        if len(found)!=1: raise ValueError(f'{s} requires exactly one {p}.')
        return found[0]
    def subjects(type): return sorted({s for s,p,k,o in triples if p==RDF+'type' and k=='resource' and o==type})
    def local(value):
        if not value.startswith(NX): raise ValueError('Routing references must use the Software Engineering namespace.')
        return value[len(NX):]
    if not subjects(OWL+'Ontology'): raise ValueError('Missing OWL ontology declaration.')
    skills={}
    for subject in subjects(NX+'Skill'):
        id=one(subject,NX+'id','literal');workflow=one(subject,NX+'workflowPath','literal');file=(skill_root/workflow).resolve()
        if not file.is_relative_to(skill_root) or not file.is_file(): raise ValueError('Missing/unsafe workflow '+workflow)
        if id in skills: raise ValueError('Duplicate skill id '+id)
        skills[id]={'id':id,'summary':one(subject,NX+'summary','literal'),'workflow':workflow,'workflow_sha256':hashlib.sha256(file.read_bytes()).hexdigest(),'role':local(one(subject,NX+'ownedBy','resource')).removeprefix('role-'),'requires':[local(x) for x in values(subject,NX+'requiresSkill','resource')],'phases':[local(x).removeprefix('phase-') for x in values(subject,NX+'appliesInPhase','resource')]}
    recipes={};rules=[]
    for subject in subjects(NX+'RoutingRule'):
        intent=one(subject,NX+'id','literal');phase=local(one(subject,NX+'forPhase','resource')).removeprefix('phase-');skill=local(one(subject,NX+'activatesSkill','resource'))
        if skill not in skills: raise ValueError('Unknown routing skill '+skill)
        tags=values(subject,NX+'requiredTag','literal');layers=values(subject,NX+'requiredLayer','literal')
        if len(tags)>1 or len(layers)>1: raise ValueError('Ambiguous routing condition.')
        if tags or layers: rules.append({'tag':tags[0] if tags else None,'layer':layers[0] if layers else None,'phase':phase,'skill':skill})
        else: recipes.setdefault(intent,{}).setdefault(phase,[]).append(skill)
    for stages in recipes.values():
        for phase in stages: stages[phase]=sorted(set(stages[phase]))
    invalidates={}
    for s,p,k,o in sorted(triples):
        if p==NX+'invalidates' and k=='resource': invalidates.setdefault(local(s),[]).append(local(o))
    lifecycle_mapping = {}
    for subject in subjects(NX+'LifecycleMapping'):
        phase = one(subject,NX+'lifecyclePhase','resource')
        if phase in lifecycle_mapping or not phase.startswith('urn:ontolink:'):
            raise ValueError('Duplicate/invalid external lifecycle mapping.')
        stages = [local(stage).removeprefix('phase-') for stage in values(subject,NX+'engineeringPhase','resource')]
        if not stages:
            raise ValueError('Lifecycle mapping needs an engineering phase.')
        lifecycle_mapping[phase] = stages
    return {'version':one(NX+'Ontology',OWL+'versionInfo','literal'),'ontology_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'skills':dict(sorted(skills.items())),'recipes':recipes,'conditional_rules':sorted(rules,key=lambda x:(x['phase'],x['skill'],x['tag'] or '',x['layer'] or '')),'invalidates':invalidates,'lifecycle_mapping':dict(sorted(lifecycle_mapping.items()))}
