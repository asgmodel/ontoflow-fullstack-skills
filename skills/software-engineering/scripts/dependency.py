#!/usr/bin/env python3
"""Locate the external OntoLink installation without copying or changing it."""
import argparse
import json
import os
from pathlib import Path
import re

SOURCE = 'https://github.com/asgmodel/ontolink-skills'
INSTALL = 'npx skills add '+SOURCE+' --skill ontolink-skills --global --yes'


def is_coordinator(text):
    header = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
    if not header:
        return False
    name = re.search(r'^name:\s*(.*?)\s*$', header[1], re.M)
    return bool(name and name[1].strip("\"'") == 'ontolink-skills')


def verify(root):
    root = Path(root).expanduser().resolve(strict=True)
    skill = root/'SKILL.md'
    if not skill.is_file() or not is_coordinator(skill.read_text(encoding='utf-8')):
        raise ValueError('Expected the real external ontolink-skills package: '+str(root))
    for relative in ['scripts/mediator.py', 'assets/ontolink.owl']:
        if not (root/relative).is_file():
            raise ValueError('Incomplete external OntoLink installation: '+str(root))
    return root


def resolve_coordinator(explicit=None, search_roots=None):
    selected = explicit or os.environ.get('ONTOLINK_SKILL_ROOT')
    if selected:
        return verify(selected)
    home = Path.home()
    roots = search_roots if search_roots is not None else [
        home/'.agents/skills', home/'.codex/skills',
        home/'.codex/skills/remote-skills', home/'.claude/skills']
    matches = set()
    for parent in roots:
        parent = Path(parent).expanduser()
        if not parent.is_dir():
            continue
        for folder in parent.iterdir():
            identity = folder/'SKILL.md'
            if not folder.is_dir() or not identity.is_file():
                continue
            try:
                text = identity.read_text(encoding='utf-8')
            except (OSError, UnicodeError):
                continue
            if is_coordinator(text):
                matches.add(verify(folder))
    if len(matches) > 1:
        raise ValueError('Multiple external OntoLink installations; select --coordinator-root or ONTOLINK_SKILL_ROOT.')
    if not matches:
        raise ValueError('External OntoLink is missing. Install/update it outside this project: '+INSTALL)
    return matches.pop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--coordinator-root', type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps({'skill':'ontolink-skills','root':str(resolve_coordinator(args.coordinator_root)),
                          'source':SOURCE,'freshness':'Resolve only; follow loader instructions to refresh before each project session.'}, indent=2))
    except (OSError, ValueError) as error:
        parser.exit(2, str(error)+'\n')
