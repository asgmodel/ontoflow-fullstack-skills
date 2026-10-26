"""Exercise the real lifecycle/engineering boundary and executable entrypoints."""
import copy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from mediator import bootstrap, initialize, update_file, snapshot, sha, ONTOLOGY
from rdf_store import Store, O
from route import project_route, route, ROOT as ENGINEERING

REPO = Path(__file__).resolve().parents[1]
CORE = REPO / 'skills/ontolink-skills'


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.state = self.root / 'knowledge.owl'
        self.ontology = Store.read(ONTOLOGY)
        bootstrap(self.root, self.ontology)
        self.task = {'intent': 'feature', 'profile': 'existing-stack',
                     'layers': ['frontend', 'backend', 'data'],
                     'tags': ['auth', 'data', 'contract']}

    def packet(self):
        return snapshot(Store.read(self.state), self.ontology, self.state.parent)

    def record(self, payload):
        update_file(self.state, payload, self.packet()['revision'], self.ontology)

    def complete(self, phase, kind):
        artifact = self.state.parent / (kind + '.txt')
        proof = self.state.parent / (kind + '.log')
        artifact.write_text('Synthetic integration fixture outcome: ' + kind)
        proof.write_text('Synthetic provenance fixture; no application behavior asserted.')
        self.record({'id': kind, 'type': 'Artifact', 'kind': kind,
                     'path': artifact.name, 'contentHash': sha(artifact), 'status': 'CURRENT'})
        self.record({'id': kind+'-proof', 'type': 'Evidence', 'supports': kind,
                     'outcome': 'PASS', 'proofPath': proof.name,
                     'proofHash': sha(proof), 'targetHash': sha(artifact)})
        self.record({'id': 'task-'+phase, 'type': 'Task', 'usesArtifact': [kind], 'status': 'DONE'})

    def to_build(self):
        for phase, kind in [('discover', 'requirements'), ('design', 'contracts'), ('plan', 'plan')]:
            self.complete(phase, kind)

    def test_route_uses_fresh_lifecycle_and_preserves_state(self):
        before = self.state.read_bytes()
        packet = project_route(self.task, self.state, CORE)
        self.assertEqual(packet['lifecycle']['phase'], 'discover')
        self.assertEqual(packet['phase'], 'define')
        self.assertEqual(packet['lifecycle']['revision'], 0)
        self.assertEqual(self.state.read_bytes(), before)
        self.assertIn('requirements-engineering', {s['id'] for s in packet['skills']})

    def test_user_cannot_jump_to_build(self):
        with self.assertRaisesRegex(ValueError, 'does not match'):
            project_route({**self.task, 'phase': 'build'}, self.state, CORE)
        self.assertEqual(self.packet()['revision'], 0)

    def test_build_keeps_native_stack_and_protected_gates(self):
        self.to_build()
        packet = project_route(self.task, self.state, CORE)
        self.assertEqual(packet['phase'], 'build')
        self.assertTrue({'authorization', 'security', 'contract', 'behavior', 'browser'} <= set(packet['required_gates']))
        self.assertIn('security-engineering', {s['id'] for s in packet['skills']})
        self.assertIn('data-engineering', {s['id'] for s in packet['skills']})
        self.assertNotIn('sql-migration', packet['required_gates'])

    def test_blocked_focused_task_does_not_authorize_execution(self):
        self.to_build()
        self.record({'id': 'provider', 'type': 'Blocker', 'affects': 'task-build',
                     'summary': 'Synthetic unavailable prerequisite', 'status': 'OPEN'})
        with self.assertRaisesRegex(ValueError, 'No eligible'):
            project_route(self.task, self.state, CORE, 'task-build')

    def test_assigned_tasks_preserve_ownership_and_dependency_gates(self):
        self.to_build()
        for name, role in [('backend-owner', 'Planned backend engineering role'),
                           ('frontend-owner', 'Planned frontend engineering role')]:
            self.record({'id': name, 'type': 'Actor', 'title': name, 'role': role})
        self.record({'id': 'implement-api', 'type': 'Task', 'phase': 'build',
                     'title': 'Implement accepted API contract', 'owner': 'backend-owner',
                     'status': 'TODO', 'requiredKind': ['implementation'], 'dependsOn': ['task-plan']})
        self.record({'id': 'integrate-ui', 'type': 'Task', 'phase': 'build',
                     'title': 'Integrate accepted API consumer', 'owner': 'frontend-owner',
                     'status': 'TODO', 'requiredKind': ['implementation'], 'dependsOn': ['implement-api']})
        tasks = {task['id']: task for task in self.packet()['task_index']}
        self.assertEqual(tasks['implement-api']['owner'], 'backend-owner')
        self.assertEqual(tasks['implement-api']['status'], 'READY')
        self.assertEqual(tasks['integrate-ui']['owner'], 'frontend-owner')
        self.assertEqual(tasks['integrate-ui']['status'], 'TODO')
        with self.assertRaisesRegex(ValueError, 'No eligible'):
            project_route(self.task, self.state, CORE, 'integrate-ui')
        self.assertEqual(project_route(self.task, self.state, CORE, 'implement-api')['lifecycle']['task'], 'implement-api')
        self.complete('build', 'implementation')
        tasks = {task['id']: task for task in self.packet()['task_index']}
        self.assertEqual(tasks['task-verify']['status'], 'TODO')

    def test_future_focused_task_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'No eligible'):
            project_route(self.task, self.state, CORE, 'task-verify')

    def test_absent_recipe_does_not_skip_lifecycle_phase(self):
        task = {'intent': 'ui-fix', 'profile': 'existing-stack', 'layers': ['frontend'], 'tags': []}
        packet = project_route(task, self.state, CORE)
        self.assertEqual(packet['skills'], [])
        self.assertEqual(packet['lifecycle']['phase'], 'discover')
        self.assertIsNone(packet['phase'])
        self.assertEqual(self.packet()['progress']['percent'], 0)

    def test_invalid_scope_rejected_even_without_a_phase_recipe(self):
        for changes in [{'tags': ['invented']}, {'intent': []}, {'layers': 'frontend'}, {'phase': None}]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                project_route({**self.task, **changes}, self.state, CORE)

    def test_explicit_state_is_reused_without_new_graph(self):
        folder = self.root/'state'; folder.mkdir()
        self.state.rename(folder/'custom.owl'); self.state = folder/'custom.owl'
        packet = project_route(self.task, self.state, CORE)
        self.assertEqual(packet['lifecycle']['state'], str(self.state))
        self.assertFalse((self.root/'knowledge.owl').exists())

    def test_missing_or_invalid_state_is_not_replaced(self):
        self.state.unlink()
        with self.assertRaisesRegex(ValueError, 'missing'):
            project_route(self.task, self.state, CORE)
        self.assertFalse(self.state.exists())
        self.state.write_text('invalid original bytes')
        with self.assertRaisesRegex(ValueError, 'context failed'):
            project_route(self.task, self.state, CORE)
        self.assertEqual(self.state.read_text(), 'invalid original bytes')

    def test_stale_artifact_blocks_project_route(self):
        self.complete('discover', 'requirements')
        (self.root/'requirements.txt').write_text('Changed after proof')
        with self.assertRaisesRegex(ValueError, 'context failed'):
            project_route(self.task, self.state, CORE)

    def test_monitoring_routes_operational_knowledge_without_shipping(self):
        self.to_build()
        for phase, kind in [('build', 'implementation'), ('verify', 'verification'), ('deliver', 'handoff')]:
            self.complete(phase, kind)
        packet = project_route(self.task, self.state, CORE)
        self.assertEqual(packet['lifecycle']['phase'], 'monitor')
        self.assertEqual(packet['phase'], 'monitor')
        self.assertEqual({s['id'] for s in packet['skills']}, {'operations-engineering'})
        self.assertEqual(packet['required_gates'], [])
        self.complete('monitor', 'monitoring')
        self.assertEqual(self.packet()['progress']['percent'], 100)

    def test_review_only_selects_review_in_verification(self):
        self.to_build(); self.complete('build', 'implementation')
        packet = project_route({**self.task, 'intent': 'review-only'}, self.state, CORE)
        self.assertEqual(packet['phase'], 'review')
        self.assertIn('code-review-and-quality', {s['id'] for s in packet['skills']})

    def test_live_lifecycle_owl_controls_mapping(self):
        coordinator = self.root/'copy'
        shutil.copytree(CORE, coordinator, ignore=shutil.ignore_patterns('__pycache__'))
        from rdflib import Graph, Namespace, Literal
        ol = Namespace(O); path = coordinator/'assets/ontolink.owl'
        graph = Graph().parse(path); graph.set((ol.discover, ol.engineeringPhase, Literal('plan')))
        graph.serialize(path, format='xml')
        packet = project_route(self.task, self.state, coordinator)
        self.assertEqual(packet['phase'], 'plan')
        self.assertEqual(packet['lifecycle']['phase'], 'discover')

    def test_state_symlink_is_rejected(self):
        link = self.root/'alias.owl'; link.symlink_to(self.state)
        with self.assertRaisesRegex(ValueError, 'symlink'):
            project_route(self.task, link, CORE)

    def test_runtime_works_without_site_packages(self):
        task = self.root/'task.json'; task.write_text(json.dumps(self.task))
        command = [sys.executable, '-S', str(ENGINEERING/'scripts/route.py'),
                   '--task', str(task), '--state', str(self.state),
                   '--coordinator-root', str(CORE)]
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['lifecycle']['phase'], 'discover')

    def test_project_cli_requires_state(self):
        task = self.root/'task.json'; task.write_text(json.dumps(self.task))
        result = subprocess.run([sys.executable, str(ENGINEERING/'scripts/route.py'), '--task', str(task)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn('--state is required', result.stderr)

    def test_catalog_cli_is_explicitly_read_only(self):
        task = self.root/'task.json'; task.write_text(json.dumps({**self.task, 'phase': 'build'}))
        before = self.state.read_bytes()
        result = subprocess.run([sys.executable, str(ENGINEERING/'scripts/route.py'), '--task', str(task), '--catalog-only'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('CATALOG INSPECTION ONLY', json.loads(result.stdout)['authority'])
        self.assertEqual(before, self.state.read_bytes())


class ScaffoldTests(unittest.TestCase):
    def test_real_scaffold_generation_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)/'Sample'
            command = [sys.executable, str(ENGINEERING/'scripts/scaffold.py'), '--output', str(output), '--name', 'Sample']
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((output/'Sample.slnx').exists())
            self.assertTrue((output/'src/Sample.Server/ClientApp/package.json').exists())
            before = (output/'Sample.slnx').read_bytes()
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(before, (output/'Sample.slnx').read_bytes())
