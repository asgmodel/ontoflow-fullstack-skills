#!/usr/bin/env python3
"""Generate/check a deterministic source inventory; never assert test outcomes."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIRECTORIES = {'skills', 'scripts', 'tests', 'docs', '.github'}
FILES = {'.gitignore', 'README.md', 'THIRD_PARTY_NOTICES.md', 'catalog.json'}
EXCLUDED = {'__pycache__', '.venv', 'node_modules', 'bin', 'obj'}


def source_files(root=ROOT):
    found = []
    for entry in root.iterdir():
        if entry.name in FILES and entry.is_file():
            found.append(entry)
        elif entry.name in DIRECTORIES and entry.is_dir():
            for path in entry.rglob('*'):
                if any(part in EXCLUDED for part in path.relative_to(root).parts):
                    continue
                if path.is_symlink():
                    raise ValueError('Source symlinks are unsupported: ' + str(path))
                if path.is_file():
                    found.append(path)
    return sorted(found, key=lambda path: path.relative_to(root).as_posix())


def payload(root=ROOT):
    paths = source_files(root)
    return {'schema_version': 2, 'distribution': 'ontology-mediated-software-engineering',
            'installable_packages': ['ontolink-skills', 'software-engineering'],
            'source_file_count': len(paths),
            'files': [{'path': p.relative_to(root).as_posix(),
                       'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths]}


def purpose(path):
    if '/upstream/' in path:
        return 'Attributed engineering workflow or supporting reference; selectively loaded.'
    if '/assets/templates/' in path:
        return 'Optional ASP.NET/React/Blazor scaffold source; copied only when selected.'
    if '/references/profiles/' in path:
        return 'Optional ASP.NET profile contract or retained source provenance.'
    if path.startswith('tests/'):
        return 'Executable behavioral regression or integration test.'
    if '/skills/ontolink-' in path:
        return 'Bundled lifecycle phase procedure, metadata or outcome contract.'
    if path.endswith('.owl'):
        return 'Authoritative ontology model or explicitly labelled example graph.'
    if path.endswith('.ttl') or path.endswith('engineering-index.json'):
        return 'Derived ontology projection or validation shape; no project state.'
    if '/scripts/' in path or path.startswith('scripts/'):
        return 'Runtime operation, maintenance validator or source inventory tool.'
    if '/references/' in path:
        return 'On-demand execution, engineering or evidence contract.'
    if '/agents/' in path or path.endswith('/SKILL.md'):
        return 'Skill identity, trigger metadata or operating entrypoint.'
    if path.startswith('.github/'):
        return 'Continuous validation workflow.'
    return 'Distribution documentation, catalog, provenance or configuration.'


def inventory(root=ROOT):
    paths = [p.relative_to(root).as_posix() for p in source_files(root)]
    paths.append('MANIFEST.json')
    lines = ['# Necessary file inventory', '',
             'The two installed packages contain runtime instructions, ontologies and selected resources. '
             'Repository tests, CI and documentation support maintenance. Project state, generated context, '
             'proof logs, virtual environments and temporary work are excluded from the distribution inventory.', '',
             '`MANIFEST.json` records the exact source paths and SHA-256 values; it excludes itself to avoid a hash cycle. '
             'Regenerate this list and the manifest with `python scripts/manifest.py --write`.', '',
             '| File | Purpose |', '| --- | --- |']
    for path in sorted(paths):
        lines.append(f'| `{path}` | {purpose(path)} |')
    return '\n'.join(lines)+'\n'


def write(root=ROOT):
    (root/'docs').mkdir(exist_ok=True)
    (root/'docs/file-inventory.md').touch(exist_ok=True)
    (root/'docs/file-inventory.md').write_text(inventory(root), encoding='utf-8')
    (root/'MANIFEST.json').write_text(json.dumps(payload(root), indent=2)+'\n', encoding='utf-8')


def check(root=ROOT):
    if (root/'docs/file-inventory.md').read_text(encoding='utf-8') != inventory(root):
        raise ValueError('Stale file inventory; run scripts/manifest.py --write')
    if json.loads((root/'MANIFEST.json').read_text(encoding='utf-8')) != payload(root):
        raise ValueError('Stale source manifest; run scripts/manifest.py --write')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    if args.write:
        write()
    else:
        check()
    print('Source inventory: PASS')
