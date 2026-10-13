#!/usr/bin/env python3
"""Read-only phase routing. This program never edits or deploys an application."""
import argparse, hashlib, json, math, sys
from pathlib import Path
from owl_reader import load_ontology

ROOT=Path(__file__).resolve().parents[1]
PERSONAL={'full-stack','template-architecture','template-backend','template-frontend','template-verification'}
TAGS={'auth','data','external','contract','schema','performance','failure','framework','uncertain'}
LAYERS={'frontend','backend','data','infrastructure'}
PHASES={'define','plan','build','verify','review','ship'}

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def count_tokens(text):
    try:
        import tiktoken
        return len(tiktoken.get_encoding('cl100k_base').encode(text)), 'cl100k_base static instruction tokens'
    except (ImportError,OSError,ValueError):
        return math.ceil(len(text.encode('utf-8'))/3), 'heuristic: UTF-8 bytes/3, not exact tokens'

def read_graph():
    pinned=json.loads((ROOT/'assets/graph.json').read_text())
    if pinned['ontology_sha256']!=digest(ROOT/'assets/nexus.owl'):
        raise ValueError('Stale graph projection; run scripts/compile_graph.py after ontology edits.')
    graph=load_ontology(ROOT/'assets/nexus.owl',ROOT)
    for id,s in pinned['skills'].items():
        p=(ROOT/s['workflow']).resolve()
        if not p.is_relative_to(ROOT) or not p.is_file() or digest(p)!=s['workflow_sha256']:
            raise ValueError(f'Changed or missing workflow {id}; review changes and compile the graph.')
    if graph!=pinned:
        raise ValueError('OWL-derived routing differs from its integrity index; review and compile the ontology.')
    return graph

def closure(seeds,edges):
    found=set(); queue=list(seeds)
    while queue:
        node=queue.pop()
        if node not in found:
            found.add(node); queue.extend(edges.get(node,[]))
    return found

def validate_task(task,graph):
    if not isinstance(task,dict): raise ValueError('Task must be a JSON object.')
    allowed={'intent','profile','phase','layers','tags','changed_artifacts','budget_tokens','project_reserve_tokens'}
    if set(task)-allowed: raise ValueError('Unknown task fields: '+', '.join(sorted(set(task)-allowed)))
    for k in ['intent','profile','phase','layers','tags']:
        if k not in task: raise ValueError(f'Missing {k}; inspect scope/layers/risks before routing.')
    if task['intent'] not in graph['recipes']: raise ValueError('Unknown intent.')
    if task['profile'] not in ['template-single-host','existing-stack']: raise ValueError('Unknown project profile.')
    if task['phase'] not in PHASES: raise ValueError('Unknown phase.')
    for field,values in [('layers',LAYERS),('tags',TAGS),('changed_artifacts',set(json.loads((ROOT/'assets/task.schema.json').read_text())['properties']['changed_artifacts']['items']['enum']))]:
        supplied=task.get(field,[])
        if not isinstance(supplied,list) or any(not isinstance(x,str) for x in supplied): raise ValueError(f'{field} must be an array of strings.')
        if len(set(supplied))!=len(supplied) or set(supplied)-values: raise ValueError(f'Invalid or duplicate {field}.')
    for field,minimum,default in [('budget_tokens',1,16000),('project_reserve_tokens',0,3000)]:
        n=task.get(field,default)
        if type(n) is not int or n<minimum: raise ValueError(f'{field} must be an integer >= {minimum}.')
    tags=set(task['tags']); layers=set(task['layers']); intent=task['intent']
    if 'schema' in tags and 'data' not in layers: raise ValueError('Schema risk requires the data layer.')
    if 'data' in layers and intent!='blank-scaffold' and not ({'data','schema'} & tags): raise ValueError('Inspect and declare data/schema risk for a data-layer task.')
    if intent=='ui-fix' and (layers-{'frontend'} or 'schema' in tags): raise ValueError('UI-only scope crosses layers; classify it as feature or bug-fix.')
    if intent=='blank-scaffold' and (tags or task.get('changed_artifacts')): raise ValueError('A blank scaffold cannot inherit business/risk or change-impact claims; choose an implementation intent.')
    if task['profile']=='existing-stack' and intent=='blank-scaffold': raise ValueError('Blank Template scaffolding requires the Template profile.')
    if intent=='migration' and not {'schema','data'}<=tags: raise ValueError('Migration requires explicit schema and data risk tags.')
    if intent in ['feature','bug-fix','backend-fix','ui-fix','full-product','performance'] and task['phase'] in ['build','verify'] and not layers:
        raise ValueError('An implementation/verification task requires affected layers.')
    if task['phase'] not in graph['recipes'][intent]: raise ValueError(f'Phase {task["phase"]} is not part of intent {intent}.')

def route(task,graph=None):
    graph=graph or read_graph(); validate_task(task,graph)
    intent=task['intent']; phase=task['phase']; tags=set(task['tags']); layers=set(task['layers'])
    selected=set(graph['recipes'][intent][phase]); reasons={s:[f'intent:{intent}/{phase}'] for s in selected}
    def add(skill,reason): selected.add(skill); reasons.setdefault(skill,[]).append(reason)
    if intent!='blank-scaffold':
        for rule in graph['conditional_rules']:
            if rule['phase']==phase and (not rule['tag'] or rule['tag'] in tags) and (not rule['layer'] or rule['layer'] in layers):
                add(rule['skill'],f"boundary:{rule['tag'] or rule['layer']}")
        if phase=='build' and intent!='review-only' and ('backend' in layers or 'data' in layers): add('test-driven-development','behavior/persistence boundary')
    # Do not force Template adapters onto existing non-Template applications.
    if task['profile']=='existing-stack':
        replacements={'template-backend':'api-and-interface-design','template-frontend':'frontend-ui-engineering','template-verification':'test-driven-development','template-architecture':'planning-and-task-breakdown','full-stack':'incremental-implementation'}
        for old,new in replacements.items():
            if old in selected:
                selected.remove(old); reasons.pop(old,None); add(new,'existing stack: native implementation and commands')
    edges={id:s['requires'] for id,s in graph['skills'].items()}
    all_selected=closure(selected,edges)
    for s in all_selected-selected: reasons[s]=['required workflow dependency']
    selected=sorted(all_selected)
    gates=set()
    if phase in {'build','verify','review','ship'}:
        gates.add('build')
        if intent!='blank-scaffold':
            if layers & {'backend','data'} or intent in {'bug-fix','feature','full-product','migration'}: gates.add('behavior')
            if 'frontend' in layers: gates.add('browser')
            if tags & {'auth','data','external'} or intent=='security-audit': gates.add('security')
            if 'auth' in tags: gates.add('authorization')
            if 'contract' in tags or intent in {'feature','full-product'}: gates.add('contract')
            if 'schema' in tags: gates.add('sql-migration' if task['profile']=='template-single-host' else 'native-database-migration')
            if 'performance' in tags or intent=='performance': gates.add('performance')
        if phase=='ship': gates.update(['publish','release'])
    changed=task.get('changed_artifacts',[])
    stale=sorted(closure(changed,graph['invalidates'])-set(changed))
    packet={'version':graph['version'],'intent':intent,'phase':phase,'profile':task['profile'],'skills':[{'id':s,'summary':graph['skills'][s]['summary'],'path':graph['skills'][s]['workflow'],'why':reasons[s]} for s in selected],'required_gates':sorted(gates),'stale_artifacts':stale,'original_personal_skills_to_resolve':[s for s in selected if s in PERSONAL],'evidence_status':'NOT VERIFIED: selection is not execution evidence'}
    text=(ROOT/'SKILL.md').read_text()+'\n'+json.dumps(packet,sort_keys=True)+'\n'+'\n'.join((ROOT/graph['skills'][s]['workflow']).read_text() for s in selected)
    tokens,method=count_tokens(text); reserve=task.get('project_reserve_tokens',3000); target=task.get('budget_tokens',16000)
    packet['context_accounting']={'instruction_tokens':tokens,'method':method,'project_reserve_tokens':reserve,'planned_tokens':tokens+reserve,'soft_target_tokens':target,'overflow':tokens+reserve>target,'excluded':'original personal skill bodies/references, linked checklists, conversation, tools and model outputs','action':'split at valid task boundary or load required context and report overflow' if tokens+reserve>target else 'load selected workflows and current required project context'}
    return packet

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--task',type=Path,required=True); p.add_argument('--phase',choices=sorted(PHASES)); p.add_argument('--packet',action='store_true'); args=p.parse_args()
    try:
        task=json.loads(args.task.read_text())
        if args.phase: task['phase']=args.phase
        result=route(task)
        if args.packet:
            print(f"NEXUS | {result['intent']} | {result['phase']} | {result['profile']}")
            for s in result['skills']: print(f"- {s['id']}: {s['summary']} Read: {s['path']}")
            print('Required gates: '+', '.join(result['required_gates']))
            print('Stale dependents: '+', '.join(result['stale_artifacts']))
            print(json.dumps(result['context_accounting']))
            print(result['evidence_status'])
        else: print(json.dumps(result,indent=2))
    except (OSError,ValueError,TypeError,KeyError,json.JSONDecodeError) as error:
        print(f'Routing blocked: {error}',file=sys.stderr); return 2
    return 0

if __name__=='__main__': sys.exit(main())
