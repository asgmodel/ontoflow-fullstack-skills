"""External dependency resolution, missing installs and live update behavior."""
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from dependency import resolve_coordinator
from route import project_route


class DependencyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.environment = patch.dict(os.environ, {}, clear=False)
        self.environment.start(); self.addCleanup(self.environment.stop)
        os.environ.pop('ONTOLINK_SKILL_ROOT', None)

    def fixture(self, name='ontolink-skills', revision=1):
        root = self.root/name
        (root/'scripts').mkdir(parents=True)
        (root/'assets').mkdir()
        (root/'SKILL.md').write_text('---\nname: ontolink-skills\ndescription: Synthetic external dependency fixture.\n---\n')
        (root/'assets/ontolink.owl').write_text('Synthetic fixture placeholder; the real mediator validates real ontology.')
        self.version(root, revision)
        return root

    def version(self, root, revision):
        packet = {'active_task':{'id':'task-discover','status':['READY'],'phase':['urn:ontolink:discover']},
                  'revision':revision,'workflow_skill':'ontolink-discovery','completion_gates':['missing-current-evidence:requirements']}
        (root/'scripts/mediator.py').write_text('import json\nprint(json.dumps('+repr(packet)+'))\n')

    def test_explicit_root_overrides_environment(self):
        first = self.fixture('first'); second = self.fixture('second')
        os.environ['ONTOLINK_SKILL_ROOT'] = str(first)
        self.assertEqual(resolve_coordinator(second), second)

    def test_host_generated_directory_is_resolved_by_identity(self):
        package = self.fixture('skill-host-generated-id')
        self.assertEqual(resolve_coordinator(search_roots=[self.root]), package)

    def test_frontmatter_order_and_quoted_name_are_supported(self):
        package = self.fixture()
        (package/'SKILL.md').write_text('---\ndescription: External fixture\nname: "ontolink-skills"\n---\n')
        self.assertEqual(resolve_coordinator(search_roots=[self.root]), package)

    def test_environment_path_is_used(self):
        package = self.fixture()
        os.environ['ONTOLINK_SKILL_ROOT'] = str(package)
        self.assertEqual(resolve_coordinator(), package)

    def test_missing_dependency_provides_official_external_install_command(self):
        with self.assertRaisesRegex(ValueError, 'npx skills add https://github.com/asgmodel/ontolink-skills'):
            resolve_coordinator(search_roots=[self.root])
        self.assertEqual(list(self.root.iterdir()), [])

    def test_loader_folder_is_not_mistaken_for_an_installed_skill(self):
        loader = self.root/'ontolink-skills'; loader.mkdir()
        (loader/'README.md').write_text('Instructions only')
        with self.assertRaisesRegex(ValueError, 'missing'):
            resolve_coordinator(search_roots=[self.root])
        self.assertFalse((loader/'SKILL.md').exists())

    def test_ambiguous_copies_require_an_explicit_choice(self):
        self.fixture('first'); self.fixture('second')
        with self.assertRaisesRegex(ValueError, 'Multiple external'):
            resolve_coordinator(search_roots=[self.root])

    def test_cli_style_symlink_is_deduplicated(self):
        package = self.fixture('real')
        (self.root/'alias').symlink_to(package, target_is_directory=True)
        self.assertEqual(resolve_coordinator(search_roots=[self.root]), package)

    def test_incomplete_explicit_install_does_not_fall_back(self):
        package = self.fixture()
        (package/'scripts/mediator.py').unlink()
        with self.assertRaisesRegex(ValueError, 'Incomplete'):
            resolve_coordinator(package)

    def test_updated_external_mediator_is_used_on_next_call(self):
        package = self.fixture(revision=1)
        state = self.root/'knowledge.owl'; state.write_text('Synthetic state for external CLI fixture')
        task = {'intent':'feature','profile':'existing-stack','layers':['backend'],'tags':[]}
        first = project_route(task, state, package)
        self.version(package, 2)
        second = project_route(task, state, package)
        self.assertEqual(first['lifecycle']['revision'], 1)
        self.assertEqual(second['lifecycle']['revision'], 2)
        self.assertFalse((self.root/'software-engineering').exists())

    def test_changed_external_context_shape_fails_explicitly(self):
        package = self.fixture()
        state = self.root/'knowledge.owl'; state.write_text('Synthetic state')
        for payload in [[], {'active_task':'changed-api'}]:
            with self.subTest(payload=payload):
                (package/'scripts/mediator.py').write_text('import json\nprint(json.dumps('+repr(payload)+'))\n')
                with self.assertRaisesRegex(ValueError, 'Incompatible external OntoLink'):
                    project_route({'intent':'feature','profile':'existing-stack','layers':['backend'],'tags':[]}, state, package)

    def test_incompatible_external_context_fails_explicitly(self):
        package = self.fixture()
        (package/'scripts/mediator.py').write_text('import json\nprint(json.dumps({"active_task":{"status":["READY"]}}))\n')
        state = self.root/'knowledge.owl'; state.write_text('Synthetic state')
        with self.assertRaisesRegex(ValueError, 'Incompatible external OntoLink'):
            project_route({'intent':'feature','profile':'existing-stack','layers':['backend'],'tags':[]}, state, package)


if __name__ == '__main__':
    unittest.main()
