#!/usr/bin/env python3
"""Read-only phase routing. This program never edits or deploys an application."""
import argparse, hashlib, json, math, sys, subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
from owl_reader import load_ontology

ROOT=Path(__file__).resolve().parents[1]
TAGS={'auth','data','external','contract','schema','performance','failure','framework','uncertain'}
LAYERS={'frontend','backend','data','infrastructure'}
PHASES={'define','plan','build','verify','review','ship','monitor'}

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def count_tokens(text):
    return math.ceil(len(text.encode('utf-8'))/3), 'heuristic: UTF-8 bytes/3, not exact tokens'

def read_graph():
    pinned=json.loads((ROOT/'assets/engineering-index.json').read_text())
    if pinned['ontology_sha256']!=digest(ROOT/'assets/engineering.owl'):
        raise ValueError('Stale graph projection; run scripts/compile_graph.py after ontology edits.')
    graph=load_ontology(ROOT/'assets/engineering.owl',ROOT)
    for id,s in pinned['skills'].items():
        p=(ROOT/s['workflow']).resolve()
        if not p.is_relative_to(ROOT.resolve()) or not p.is_file() or digest(p)!=s['workflow_sha256']:
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

def validate_task(task,graph,require_recipe=True):
    if not isinstance(task,dict): raise ValueError('Task must be a JSON object.')
    allowed={'intent','profile','phase','layers','tags','changed_artifacts','budget_tokens','project_reserve_tokens'}
    if set(task)-allowed: raise ValueError('Unknown task fields: '+', '.join(sorted(set(task)-allowed)))
    for k in ['intent','profile','phase','layers','tags']:
        if k not in task: raise ValueError(f'Missing {k}; inspect scope/layers/risks before routing.')
    if not isinstance(task['intent'],str) or task['intent'] not in graph['recipes']: raise ValueError('Unknown intent.')
    if task['profile'] not in ['aspnet-single-host','existing-stack']: raise ValueError('Unknown project profile.')
    if not (task['phase'] is None and not require_recipe) and (not isinstance(task['phase'],str) or task['phase'] not in PHASES): raise ValueError('Unknown phase.')
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
    if task['profile']=='existing-stack' and intent=='blank-scaffold': raise ValueError('Blank scaffold requires the ASP.NET profile.')
    if intent=='migration' and not {'schema','data'}<=tags: raise ValueError('Migration requires explicit schema and data risk tags.')
    if intent in ['feature','bug-fix','backend-fix','ui-fix','full-product','performance'] and task['phase'] in ['build','verify'] and not layers:
        raise ValueError('An implementation/verification task requires affected layers.')
    if require_recipe and task['phase'] not in graph['recipes'][intent]: raise ValueError(f'Phase {task["phase"]} is not part of intent {intent}.')

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
            if 'schema' in tags: gates.add('sql-migration' if task['profile']=='aspnet-single-host' else 'native-database-migration')
            if 'performance' in tags or intent=='performance': gates.add('performance')
        if phase=='ship': gates.update(['publish','release'])
    changed=task.get('changed_artifacts',[])
    stale=sorted(closure(changed,graph['invalidates'])-set(changed))
    packet={'version':graph['version'],'intent':intent,'phase':phase,'profile':task['profile'],'skills':[{'id':s,'summary':graph['skills'][s]['summary'],'role':graph['skills'][s]['role'],'path':graph['skills'][s]['workflow'],'why':reasons[s]} for s in selected],'required_gates':sorted(gates),'stale_artifacts':stale,'evidence_status':'NOT VERIFIED: selection is not execution evidence'}
    text=(ROOT/'SKILL.md').read_text()+'\n'+json.dumps(packet,sort_keys=True)+'\n'+'\n'.join((ROOT/graph['skills'][s]['workflow']).read_text() for s in selected)
    tokens,method=count_tokens(text); reserve=task.get('project_reserve_tokens',3000); target=task.get('budget_tokens',16000)
    packet['context_accounting']={'instruction_tokens':tokens,'method':method,'project_reserve_tokens':reserve,'planned_tokens':tokens+reserve,'soft_target_tokens':target,'overflow':tokens+reserve>target,'excluded':'linked references/checklists, conversation, tools and model outputs','action':'split at valid task boundary or load required context and report overflow' if tokens+reserve>target else 'load selected workflows and current required project context'}
    return packet


def project_route(task, state, coordinator, focus_task=None):
    """Join live lifecycle eligibility to the engineering catalog without writes."""
    if not isinstance(task, dict):
        raise ValueError('Task must be a JSON object.')
    state = Path(state).absolute()
    if state.is_symlink() or any(p.is_symlink() for p in state.parents):
        raise ValueError('Canonical state and its parents cannot be symlinks.')
    if not state.is_file():
        raise ValueError('Canonical state missing; run the coordinator start command first.')
    coordinator = Path(coordinator).resolve(strict=True)
    mediator = coordinator / 'scripts/mediator.py'
    if not mediator.is_file() or '\nname: ontolink-skills\n' not in (coordinator / 'SKILL.md').read_text():
        raise ValueError('Resolve the actual ontolink-skills coordinator directory.')
    command = [sys.executable, str(mediator), 'context', '--state', str(state)]
    if focus_task:
        command.extend(['--task', focus_task])
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
    if result.returncode:
        raise ValueError('OntoLink context failed: ' + result.stderr.strip())
    context = json.loads(result.stdout)
    active = context.get('active_task')
    if not active or active.get('status') not in [['READY'], ['RUNNING']]:
        raise ValueError('No eligible OntoLink task; inspect current dependencies/blockers.')
    phase = active['phase'][0]
    raw = (coordinator / 'assets/ontolink.owl').read_bytes()
    if b'<!DOCTYPE' in raw.upper() or b'<!ENTITY' in raw.upper():
        raise ValueError('Unsupported lifecycle ontology declarations.')
    ontology = ET.fromstring(raw)
    rdf = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
    ol = 'urn:ontolink:'
    mapping = [node for node in ontology if node.get('{'+rdf+'}about') == phase]
    if len(mapping) != 1:
        raise ValueError('Lifecycle phase must have exactly one ontology definition.')
    stages = sorted({node.text for node in mapping[0] if node.tag == '{'+ol+'}engineeringPhase'})
    if any(stage not in PHASES for stage in stages):
        raise ValueError('Unknown engineering phase in lifecycle ontology.')
    graph = read_graph()
    supplied = task.get('phase')
    if 'phase' in task and (not isinstance(supplied, str) or supplied not in stages):
        raise ValueError('Requested engineering phase does not match the eligible lifecycle phase.')
    candidate = {**task, 'phase': supplied or (stages[0] if stages else None)}
    validate_task(candidate, graph, require_recipe=False)
    matching = [stage for stage in stages if stage in graph['recipes'][task['intent']]]
    if supplied and supplied not in matching:
        raise ValueError('Requested phase has no recipe for this intent.')
    if len(matching) > 1 and not supplied:
        # Prefer actual verification when both verification and review are valid.
        selected = 'verify' if 'verify' in matching else matching[0]
    else:
        selected = supplied or (matching[0] if matching else None)
    if selected:
        packet = route({**task, 'phase': selected}, graph)
    else:
        packet = {'version': graph['version'], 'intent': task['intent'], 'profile': task['profile'],
                  'phase': None, 'skills': [], 'required_gates': [],
                  'stale_artifacts': sorted(closure(task.get('changed_artifacts', []), graph['invalidates']) - set(task.get('changed_artifacts', []))),
                  'evidence_status': 'NOT VERIFIED: selection is not execution evidence',
                  'reason': 'No engineering recipe for this lifecycle phase/intent; complete the OntoLink phase outcome normally.'}
    packet['lifecycle'] = {'state': str(state), 'revision': context['revision'],
                           'task': active['id'], 'phase': phase.removeprefix(ol),
                           'workflow_skill': context['workflow_skill'],
                           'completion_gates': context['completion_gates']}
    packet['authority'] = 'OntoLink owns eligibility, state writes and completion; this packet is read-only.'
    return packet


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--task', type=Path, required=True)
    parser.add_argument('--state', type=Path)
    parser.add_argument('--coordinator-root', type=Path, default=ROOT.parent/'ontolink-skills')
    parser.add_argument('--focus-task')
    parser.add_argument('--catalog-only', action='store_true', help='Inspect routing without project eligibility; never an execution authorization.')
    args = parser.parse_args()
    try:
        task = json.loads(args.task.read_text(encoding='utf-8'))
        if args.catalog_only:
            if args.state or args.focus_task:
                raise ValueError('Catalog inspection cannot use project state or a focused task.')
            result = route(task)
            result['authority'] = 'CATALOG INSPECTION ONLY: no project eligibility or execution authorization.'
        else:
            if args.state is None:
                raise ValueError('--state is required for project routing; run start first.')
            result = project_route(task, args.state, args.coordinator_root, args.focus_task)
        print(json.dumps(result, indent=2))
    except (OSError, ValueError, TypeError, KeyError, ET.ParseError) as error:
        print(f'Routing blocked: {error}', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
