#!/usr/bin/env python3
"""Create a blank Template project in a new directory, without external dependencies."""
import argparse
from pathlib import Path
import re
import shutil
import sys
import tempfile

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    parser.add_argument('--name', default='App', help='ASCII letter followed by ASCII letters or digits')
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z][A-Za-z0-9]{0,47}', args.name):
        parser.error('Name must be 1-48 ASCII letters/digits and begin with a letter.')
    reserved = set('abstract as base bool break byte case catch char checked class const continue decimal default delegate do double else enum event explicit extern false finally fixed float for foreach goto if implicit in int interface internal is lock long namespace new null object operator out override params private protected public readonly ref return sbyte sealed short sizeof stackalloc static string struct switch this throw true try typeof uint ulong unchecked unsafe ushort using virtual void volatile while'.split())
    if args.name in reserved:
        parser.error('Name must not be a C# reserved keyword.')
    out = Path(args.output).expanduser().absolute()
    if out.exists() or out.is_symlink():
        parser.error('Output must not already exist; existing projects are never overwritten.')
    source = Path(__file__).resolve().parents[1] / 'assets' / 'blank-project'
    if not (source / 'Template.slnx').is_file():
        parser.error('Bundled blank-project asset is missing.')
    out.parent.mkdir(parents=True, exist_ok=True)
    mappings = [('Template-App-Server', args.name+'-Server'), ('Template', args.name),
                ('TemplateDb', args.name+'Db'), ('template-client', args.name.lower()+'-client'),
                ('App.Server', args.name+'.Server')]
    def replace(text):
        for old, new in mappings:
            text = text.replace(old, new)
        return text
    temp = Path(tempfile.mkdtemp(prefix='.template-create-', dir=out.parent))
    try:
        for f in source.rglob('*'):
            if f.is_symlink():
                raise ValueError('Template symlinks are not supported')
            target = temp / replace(str(f.relative_to(source)))
            if f.is_dir(): target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(replace(f.read_text(encoding='utf-8')), encoding='utf-8')
        # Reserve the destination atomically; never merge into an existing tree.
        out.mkdir()
        try:
            for child in temp.iterdir(): shutil.move(str(child), str(out / child.name))
        except Exception:
            shutil.rmtree(out)
            raise
    finally:
        shutil.rmtree(temp, ignore_errors=True)
    print(f'Created blank project: {out}')
    print('Not yet built or runtime verified. Read AGENTS.md for setup and verification.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
