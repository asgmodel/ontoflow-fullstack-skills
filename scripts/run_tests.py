#!/usr/bin/env python3
"""Run distribution behavioral tests with the installed runtime import paths."""
from pathlib import Path
import sys
import unittest
import tempfile

ROOT = Path(__file__).resolve().parents[1]
for folder in ['skills/ontolink-skills/scripts', 'skills/software-engineering/scripts']:
    sys.path.insert(0, str(ROOT / folder))
if __name__ == '__main__':
    temporary = ROOT/'.ontolink/test-tmp'
    temporary.mkdir(parents=True, exist_ok=True)
    tempfile.tempdir = str(temporary)
    suite = unittest.defaultTestLoader.discover(str(ROOT / 'tests'))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(not result.wasSuccessful())
