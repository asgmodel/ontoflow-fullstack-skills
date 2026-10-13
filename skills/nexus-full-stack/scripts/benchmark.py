#!/usr/bin/env python3
"""Measure selected static payload against all-skills loading; not end-to-end savings."""
import json
from pathlib import Path
from route import ROOT,read_graph,route,count_tokens

def main():
    graph=read_graph(); entry=(ROOT/'SKILL.md').read_text()
    baseline=entry+'\n'+'\n'.join((ROOT/s['workflow']).read_text() for s in graph['skills'].values())
    all_tokens,method=count_tokens(baseline)
    cases=[('CSS-only native UI',{'intent':'ui-fix','profile':'existing-stack','phase':'build','layers':['frontend'],'tags':[]}),('Owner-scoped Template feature',{'intent':'feature','profile':'template-single-host','phase':'build','layers':['frontend','backend','data'],'tags':['auth','data','contract']}),('Template schema migration',{'intent':'migration','profile':'template-single-host','phase':'build','layers':['backend','data'],'tags':['schema','data']}),('Blank scaffold verification',{'intent':'blank-scaffold','profile':'template-single-host','phase':'verify','layers':[],'tags':[]})]
    results=[]
    for label,task in cases:
        result=route(task,graph); selected=result['context_accounting']['instruction_tokens']
        results.append({'case':label,'selected_workflows':len(result['skills']),'selected_instruction_tokens':selected,'all_workflows_instruction_tokens':all_tokens,'static_payload_reduction_percent':round(100*(1-selected/all_tokens),2),'overflow':result['context_accounting']['overflow']})
    print(json.dumps({'method':method,'baseline':'Entry plus all 30 catalog workflow bodies, loaded once. This is an intentionally broad all-skills baseline, not a claim about the users existing workflow.','limitations':'Excluded original personal skill bodies, linked references, project source, tool calls, history, generated output and retries; no end-to-end cost or task success claim. Selected payload also includes its routing packet.','cases':results},indent=2))

if __name__=='__main__': main()
