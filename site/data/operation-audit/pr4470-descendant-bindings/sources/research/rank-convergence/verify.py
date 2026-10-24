#!/usr/bin/env python3
"""Source-bound finite proof gates for the padding-free rank compiler.

Native and outer producer receipts are inherited, not replayed.
zxv with substantial OpenAI Codex assistance; Apache-2.0.
"""
import argparse
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha1, sha256
import io
import json
from pathlib import Path
import sys
import unittest
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import compiler
import intervals as E
import flow
import test_flow
import test_independent


def authenticate_bytes(raw, row):
    E.need(sha256(raw).hexdigest() == row['sha256'], 'source SHA256: '+row['path'])
    E.need(sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest() == row['git_blob'],
           'source Git blob: '+row['path'])


def authenticate():
    receipt = {}
    rows = json.loads((HERE/'SOURCES.json').read_text())['files']
    for row in rows:
        if row['usage'] == 'input':
            authenticate_bytes((ROOT/row['path']).read_bytes(), row)
            receipt[row['path']] = row['sha256']
    path = str(flow.SOURCE.relative_to(ROOT))
    E.need(path in receipt and receipt[path] == flow.SOURCE_SHA256,
           'executed predecessor is a declared authenticated input')
    first = next(row for row in rows if row['usage'] == 'input')
    try:
        authenticate_bytes((ROOT/first['path']).read_bytes()+b' ', first)
    except ValueError:
        pass
    else:
        raise ValueError('source corruption control accepted')
    return receipt


def at(value, keys):
    for key in keys:
        value = value[key]
    return value


def rejected(profile, witness, fragment, mutation):
    changed = deepcopy(witness)
    mutation(changed)
    try:
        compiler.certify(profile, changed)
    except ValueError as exc:
        E.need(fragment in str(exc), 'unexpected rejection: '+str(exc))
        return str(exc)
    raise ValueError('invalid witness accepted: '+fragment)


def run():
    sources = authenticate()
    suite = unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromModule(module)
                               for module in (test_flow, test_independent))
    output = io.StringIO()
    tests = unittest.TextTestRunner(stream=output, verbosity=1).run(suite)
    E.need(tests.wasSuccessful(), output.getvalue())
    results, profiles, witnesses = {}, {}, {}
    for row in json.loads((HERE/'BENCHMARKS.json').read_text())['cases']:
        E.need(row['source'] in sources and row['baseline']['source'] in sources,
               'every profile, consumer and comparison source authenticated')
        source = json.loads((ROOT/row['source']).read_text())
        profile = source[row['profile_key']] if row['profile_key'] else source
        result = compiler.certify(profile, row['witness'])
        outer = at(source, row['consumer_key'])
        required = Q(outer['parameters']['complex_uniform_saving'])
        E.need(Q(result['kappa']) == Q(source['kappa']) == Q(outer['parameters']['kappa']),
               'retained consumer kappa identity')
        E.need(Q(result['uniform_saving']) >= required, 'supplied uniform bound funds retained consumer')
        E.need(len(outer['margins']) == 9
               and all(Q(x) > Q(result['kappa']) for x in outer['margins'].values()),
               'nine inherited consumer margins')
        for name in ('strict_checks', 'functional_checks'):
            E.need(outer[name] and all(Q(x) > 0 for x in outer[name].values()),
                   'positive inherited '+name+' receipt')
        legacy_outer = source.get('legacy_outer', {})
        legacy = legacy_outer.get('checks', legacy_outer.get('strict_checks',
                     source['outer'].get('legacy_63_checks', {})))
        E.need(len(legacy) == 63 and all(Q(x) > 0 for x in legacy.values()),
               'positive inherited legacy receipt')
        baseline_source = json.loads((ROOT/row['baseline']['source']).read_text())
        baseline = at(baseline_source, row['baseline']['path'])
        baseline_kappa = baseline.get('kappa', baseline_source.get('kappa'))
        E.need(baseline_kappa is not None and Q(baseline_kappa) == Q(result['kappa']),
               'comparison retains the same kappa')
        if row['baseline']['source'] != row['source']:
            E.need(baseline_source['source_sha256'][row['source']] == sources[row['source']],
                   'comparison receipt uses the same exact raw profile source')
        if 'uniform_saving' in baseline:
            baseline_saving = Q(baseline['uniform_saving'])
        else:
            baseline_saving = Q(baseline_source['outer']['parameters']['complex_uniform_saving'])
        result['comparison'] = {'source': row['baseline']['source'],
            'source_path': row['baseline']['path'], 'baseline_H': baseline['H'],
            'baseline_uniform_saving': str(baseline_saving),
            'same_uniform_saving': Q(result['uniform_saving']) == baseline_saving,
            'rank_exponent_reduction': str(Q(baseline['H'], result['H']))}
        result['consumer_binding'] = {'status': 'INHERITED_RECEIPT_AND_MONOTONE_BOUND',
            'producer_replayed': False, 'required_uniform_saving': str(required),
            'available_uniform_saving': result['uniform_saving'],
            'current_strict_checks': len(outer['strict_checks']),
            'functional_guards': len(outer['functional_checks']),
            'legacy_checks': len(legacy)}
        results[row['name']], profiles[row['name']], witnesses[row['name']] = result, profile, row['witness']
    # Bind the new p16 data to the actual published joint-helper profile as
    # well as its compact consumer receipt; no invoice is inferred from labels.
    joint_path = 'research/joint-helper-lattice/RESULT.json'
    E.need(joint_path in sources, 'joint native profile authenticated')
    joint = json.loads((ROOT/joint_path).read_text())
    E.need(all(joint[key] == profiles['p16'][key] for key in ('targets', 'paid')),
           'p16 compact/native profile equality')
    name = 'p7'
    profile, witness = profiles[name], witnesses[name]
    controls = {}
    for label, fragment, mutate in (
        ('old_incomplete_tau_interval', 'local exponent interval', lambda w: w.update(t_upper='.9974808')),
        ('below_root_moment', 'raw strict moment', lambda w: w.update(t0='.99731252')),
        ('nonconcave_majorant', 'concave funded majorant', lambda w: w.update(c='1')),
        ('unfunded_root_tail', 'root source Chernoff', lambda w: w['guards'].update(V='.8')),
        ('understated_boundary_share', 'boundary mirror coefficient', lambda w: w['guards'].update(beta='.2')),
        ('insufficient_tilted_gap', 'sharp source and boundary', lambda w: w['guards'].update(d='.1')),
        ('unfunded_uniform_gap', 'funded uniform and consumer', lambda w: w.update(uniform_saving=str(1-Q(w['t0'])))),
        ('too_small_final_rank', 'final uniform-rank inequality', lambda w: w.update(H=100000000)),
    ):
        controls[label] = rejected(profile, witness, fragment, mutate)
    E.need(results['native4453-matched-uniform']['comparison']['same_uniform_saving'],
           'controlled native comparison preserves uniform saving')
    E.need(results['p7']['comparison']['same_uniform_saving']
           and results['p16']['comparison']['same_uniform_saving'],
           'p7 and newest p16 comparisons preserve uniform saving')
    return {'schema_version': 1, 'status': 'PASS_PADDING_FREE_ADAPTIVE_COMPILER',
            'scope': 'Conditional direct overlapping-rank compiler under explicit finite gates; exact rank and inherited consumer binding, not a native/physical/analytic theorem audit.',
            'source_sha256': sources, 'examples': results,
            'finite_tests': tests.testsRun, 'rejected_witnesses': controls,
            'source_mutation_rejected': True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    receipt = run()
    raw = json.dumps(receipt, sort_keys=True, indent=2)+'\n'
    path = HERE/'RESULT.json'
    if args.write:
        path.write_text(raw)
    else:
        E.need(path.read_text() == raw, 'changed exact receipt; inspect then use --write')
    print(json.dumps({'status': receipt['status'], 'finite_tests': receipt['finite_tests'],
        'rejected_witnesses': len(receipt['rejected_witnesses']),
        'examples': {name: {'H': r['H'], 'kappa': r['kappa'], 'tensor_power': 1,
                          'reduction': r['comparison']['rank_exponent_reduction']}
                     for name, r in receipt['examples'].items()}}, sort_keys=True))


if __name__ == '__main__':
    main()
