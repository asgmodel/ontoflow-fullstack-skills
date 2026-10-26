#!/usr/bin/env python3
"""Behavioral routing checks: scope, safety, freshness, native stack and budget integrity."""
import copy, unittest
from unittest.mock import patch
from route import read_graph,route,closure
from rdflib import Graph,Namespace,RDF,Literal
from pyshacl import validate
from pathlib import Path
import tempfile
from owl_reader import load_ontology,parse_named_rdfxml

ROOT=Path(__file__).resolve().parents[1]/'skills/software-engineering'
N=Namespace('urn:software-engineering:')

def task(intent='feature',phase='build',profile='aspnet-single-host',layers=None,tags=None,**extra):
    return {'intent':intent,'phase':phase,'profile':profile,'layers':layers if layers is not None else ['backend'],'tags':tags or [],**extra}

def ids(result): return {s['id'] for s in result['skills']}

class RoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.graph=read_graph()
    def test_ui_does_not_load_backend(self):
        r=route(task('ui-fix',layers=['frontend']))
        self.assertIn('frontend-engineering',ids(r)); self.assertNotIn('backend-engineering',ids(r)); self.assertNotIn('sql-migration',r['required_gates'])
    def test_native_stack_not_forced_to_template(self):
        r=route(task('ui-fix',profile='existing-stack',layers=['frontend']))
        self.assertIn('frontend-ui-engineering',ids(r)); self.assertIn('frontend-engineering',ids(r)); self.assertNotIn('backend-engineering',ids(r)); self.assertEqual(r['profile'],'existing-stack')
    def test_owner_scoped_feature_keeps_security(self):
        r=route(task(layers=['frontend','backend','data'],tags=['auth','data','contract']))
        self.assertTrue({'frontend-engineering','backend-engineering','api-and-interface-design','security-and-hardening'}<=ids(r))
        self.assertTrue({'authorization','security','contract','behavior','browser'}<=set(r['required_gates']))
    def test_schema_keeps_migration_gate(self):
        r=route(task('migration',layers=['backend','data'],tags=['schema','data']))
        self.assertIn('deprecation-and-migration',ids(r)); self.assertIn('sql-migration',r['required_gates'])
    def test_native_database_gate_is_native(self):
        r=route(task('migration',profile='existing-stack',layers=['backend','data'],tags=['schema','data']))
        self.assertIn('native-database-migration',r['required_gates']); self.assertNotIn('sql-migration',r['required_gates'])
    def test_blank_has_no_invented_business(self):
        r=route(task('blank-scaffold','verify',layers=[]))
        self.assertEqual(ids(r),{'verification-engineering'}); self.assertNotIn('behavior',r['required_gates']); self.assertNotIn('authorization',r['required_gates'])
    def test_contract_invalidates_consumer_tests_and_bundle(self):
        r=route(task(changed_artifacts=['api-contract']))
        self.assertTrue({'ui','tests','backend','publish-bundle'}<=set(r['stale_artifacts']))
    def test_low_budget_never_silently_drops_security(self):
        small=route(task(tags=['auth'],budget_tokens=1)); large=route(task(tags=['auth'],budget_tokens=100000))
        self.assertEqual(ids(small),ids(large)); self.assertTrue(small['context_accounting']['overflow']); self.assertIn('security-and-hardening',ids(small))
    def test_failure_loads_debugging(self):
        r=route(task('feature','verify',tags=['failure']))
        self.assertIn('debugging-and-error-recovery',ids(r))
    def test_unknown_or_incomplete_inputs_are_blocked(self):
        for t in [{},task(intent='unknown'),task(tags=['unknown']),task(layers=['data']),task(budget_tokens=True),task(intent='ui-fix',layers=['frontend','backend'])]:
            with self.subTest(t=t),self.assertRaises(ValueError): route(t)
    def test_all_legal_intent_phases_route(self):
        for intent,phases in self.graph['recipes'].items():
            for phase in phases:
                layers=['frontend'] if intent=='ui-fix' else ['backend']
                tags=[]
                if intent=='migration': layers=['backend','data'];tags=['schema','data']
                if intent=='blank-scaffold':layers=[]
                r=route(task(intent,phase,layers=layers,tags=tags))
                self.assertTrue(r['skills'])
    def test_graph_cycles_do_not_loop_impact_traversal(self):
        self.assertEqual(closure(['a'],{'a':['b'],'b':['a']}),{'a','b'})
    def test_owl_reader_preserves_all_routing_triples(self):
        owl=ROOT/'assets/engineering.owl'
        expected={(str(s),str(p),'literal' if isinstance(o,Literal) else 'resource',str(o)) for s,p,o in Graph().parse(owl,format='xml')}
        self.assertEqual(parse_named_rdfxml(owl),expected)
    def test_reader_uses_live_owl_content(self):
        g=Graph().parse(ROOT/'assets/engineering.owl',format='xml')
        g.set((N['frontend-engineering'],N.summary,Literal('Changed OWL fixture summary')))
        with tempfile.TemporaryDirectory() as directory:
            owl=Path(directory)/'fixture.owl';g.serialize(owl,format='xml')
            derived=load_ontology(owl,ROOT)
            self.assertEqual(derived['skills']['frontend-engineering']['summary'],'Changed OWL fixture summary')
    def test_unsupported_owl_constructs_fail_explicitly(self):
        with tempfile.TemporaryDirectory() as directory:
            owl=Path(directory)/'fixture.owl'
            owl.write_text('<!DOCTYPE rdf [<!ENTITY x "payload">]><rdf/>')
            with self.assertRaises(ValueError):parse_named_rdfxml(owl)
    def test_stale_projection_is_blocked(self):
        with patch('route.digest',return_value='outdated'),self.assertRaises(ValueError): read_graph()
    def test_changed_workflow_is_blocked(self):
        from route import digest
        def altered(path):
            return digest(path) if path.name=='engineering.owl' else 'outdated-workflow'
        with patch('route.digest',side_effect=altered),self.assertRaises(ValueError): read_graph()
    def test_verified_evidence_without_proof_is_rejected(self):
        data=Graph(); data.add((N.fake,RDF.type,N.Evidence));data.add((N.fake,N.status,Literal('VERIFIED')))
        shapes=Graph().parse(ROOT/'assets/shapes.ttl')
        self.assertFalse(validate(data,shacl_graph=shapes)[0])
        data.add((N.fake,N.command,Literal('test command')));data.add((N.fake,N.result,Literal('exit 0')));data.add((N.fake,N.testedRevision,Literal('test fixture revision')))
        self.assertTrue(validate(data,shacl_graph=shapes)[0])

if __name__=='__main__': unittest.main(verbosity=2)
