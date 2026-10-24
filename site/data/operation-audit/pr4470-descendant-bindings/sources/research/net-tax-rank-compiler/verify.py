#!/usr/bin/env python3
"""Source-bound replay of the scoped rank certificates.

Native and outer producer receipts are inherited, not recomputed here.
zxv with substantial OpenAI Codex assistance. Apache-2.0.
"""
import argparse
from collections import Counter
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha1, sha256
import io
import json
from pathlib import Path
import sys
import unittest
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import compiler
import intervals as E
import test_math

ROOT = HERE.parents[1]
FLOW = ('research/kappa-rebuild/architecture/sources/Sussman-563b4e6/'
        'research/record-track/programs/theorem-1g/tree_flow.py')


def authenticate_bytes(raw, row):
    E.need(sha256(raw).hexdigest() == row['sha256'], 'source SHA256: '+row['path'])
    E.need(sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
           == row['git_blob'], 'source Git blob: '+row['path'])


def authenticate():
    manifest = json.loads((HERE/'SOURCES.json').read_text())
    receipts = {}
    for row in manifest['files']:
        if row['usage'] == 'input':
            raw = (ROOT/row['path']).read_bytes()
            authenticate_bytes(raw, row)
            receipts[row['path']] = row['sha256']
    first = next(row for row in manifest['files'] if row['usage'] == 'input')
    try:
        authenticate_bytes((ROOT/first['path']).read_bytes()+b' ', first)
    except ValueError:
        pass
    else:
        raise ValueError('source mutation control accepted')
    return receipts


def literal_flow_checks():
    # Execute authenticated source bytes directly, bypassing bytecode caches.
    path = ROOT/FLOW
    env = {'__file__': str(path), '__name__': 'pinned_tree_flow_oracle'}
    exec(compile(path.read_bytes(), str(path), 'exec'), env)
    receipt = []
    for n in (5, 14, 15, 44, 45, 135):
        paid = [1, 1, 1, 1, 2]
        actual, tree = env['lockstep_literal']({3: 2, 5: 1}, paid, n)
        expected = Counter({1: 1})
        for _ in range(tree.G+1):
            changed = Counter()
            for rank, count in expected.items():
                for r in paid:
                    changed[rank*r] += count
            expected = changed
        E.need(actual['issued_before_start'] and actual['exits'] == dict(expected),
               'literal chronological exit law')
        receipt.append({'top_rank': n, 'G': tree.G,
                        'exits': dict(sorted(expected.items())),
                        'literal_classes': actual['classes']})
    return receipt


def inherited_consumer(source, result, kind):
    if kind == 'native':
        outer, original = source['outer'], source['compiler']
        legacy = source['legacy_outer']['checks']
    else:
        outer, original = source['outer']['ledger'], source['uniform_rank']
        legacy = source['outer']['legacy_63_checks']
    point = outer['parameters']
    E.need(Q(result['uniform']['kappa']) == Q(source['kappa']) == Q(point['kappa']),
           'unchanged inherited kappa point')
    required = Q(point['complex_uniform_saving'])
    available = Q(result['uniform']['uniform_saving'])
    E.need(available >= required, 'new uniform bound supplies retained outer point')
    E.need(Q(original['uniform_saving']) == required, 'source compiler/consumer binding')
    for name in ('strict_checks', 'functional_checks'):
        E.need(outer[name] and all(Q(x) > 0 for x in outer[name].values()),
               'positive inherited consumer receipt: '+name)
    E.need(len(outer['margins']) == 9
           and all(Q(x) > Q(source['kappa']) for x in outer['margins'].values()),
           'nine inherited outer margins')
    E.need(len(legacy) == 63 and all(Q(x) > 0 for x in legacy.values()),
           'legacy inherited receipt')
    return {'status': 'INHERITED_RECEIPT_AND_MONOTONE_BOUND_BINDING',
            'producer_replayed': False, 'source_H': original['H'],
            'retained_kappa': str(Q(source['kappa'])),
            'required_uniform_saving': str(required),
            'available_uniform_saving': str(available),
            'strict_checks_in_receipt': len(outer['strict_checks']),
            'functional_checks_in_receipt': len(outer['functional_checks']),
            'legacy_checks_in_receipt': len(legacy),
            'rank_exponent_reduction': str(Q(original['H'], result['uniform']['H']))}


def expect_rejected(profile, witness, fragment, mutate):
    changed = deepcopy(witness)
    mutate(changed)
    try:
        compiler.certify(profile, changed)
    except ValueError as exc:
        E.need(fragment in str(exc), 'unexpected rejection: '+str(exc))
        return str(exc)
    raise ValueError('invalid certificate accepted: '+fragment)


def run():
    sources = authenticate()
    E.need(FLOW in sources, 'literal oracle must be an authenticated live input')
    tests = unittest.defaultTestLoader.loadTestsFromModule(test_math)
    stream = io.StringIO()
    tested = unittest.TextTestRunner(stream=stream, verbosity=1).run(tests)
    E.need(tested.wasSuccessful(), stream.getvalue())
    examples, profiles, witnesses = {}, {}, {}
    for case in json.loads((HERE/'BENCHMARKS.json').read_text())['cases']:
        E.need(case['source'] in sources, 'benchmark source must be an authenticated live input')
        source = json.loads((ROOT/case['source']).read_text())
        kind = 'p7' if case['profile_key'] else 'native'
        if kind == 'native':
            E.need(source['status'] == 'PASS_CONDITIONAL_NEW_NATIVE_PROFILE_KAPPA',
                   'native source receipt status')
        else:
            E.need(source['status'] == 'PASS_HIGHER_MOMENT_STRICTIFICATION',
                   'p7 source receipt status')
        profile = source if case['profile_key'] is None else source[case['profile_key']]
        result = compiler.certify(profile, case['witness'])
        result['consumer_binding'] = inherited_consumer(source, result, kind)
        examples[case['name']] = result
        profiles[case['name']], witnesses[case['name']] = profile, case['witness']
    baseline = examples['native-source-parameters']['uniform']['H']
    native = json.loads((ROOT/'research/native-lattice-retiming/RESULT.json').read_text())
    E.need(baseline == native['compiler']['H'], 'source rank reproduced by old parameters')
    final_name = 'native-concentrated-balanced'
    profile, witness = profiles[final_name], witnesses[final_name]
    negatives = {}
    for name, fragment, mutation in (
        ('too_small_tensor', 'strict net moment', lambda w: w.update(v=20)),
        ('invalid_tail_exponent', 'net tax exponent', lambda w: w.update(u='1/100000')),
        ('closed_uniform_saving', 'uniform exponent', lambda w: w.update(kappa=w['saving'])),
        ('degree23', 'polynomial coefficients', lambda w: w.update(p=23)),
        ('understated_raw_mean', 'raw paid log mean',
         lambda w: w['weighted'].update(raw_mean_upper='4/5')),
        ('understated_log_support', 'raw paid log support',
         lambda w: w['weighted'].update(raw_log_bound='1')),
        ('understated_full_paid_excess', 'full paid mass perturbation',
         lambda w: w['weighted'].update(paid_excess_upper='1/100000000')),
        ('wrong_log_shift_enclosure', 'normalized log shift',
         lambda w: w['weighted'].update(A_upper='347/100')),
        ('drop_tensor_concentration', 'polynomial coefficients',
         lambda w: (w.update(uniform_method='weighted'),
                    w['weighted'].update(mean_upper=w['weighted']['raw_mean_upper']))),
    ):
        negatives[name] = expect_rejected(profile, witness, fragment, mutation)
    # The earlier full-charge proof fails on the new small tensor, so the
    # improvement cannot be obtained merely by retaining its estimate.
    old = examples[final_name]['net_tax']['predecessor_full_charge_bound']
    E.need(Q(old['lower']) > 1, 'old full-charge comparison fails')
    return {'schema_version': 1, 'status': 'PASS_NET_TAX_AND_LOG_MOMENT_RANK_COMPILER',
            'scope': 'Conditional finite rank/leaf bounds; inherited native and outer producer receipts; no new kappa, selected frontier, materialized word or physical runtime claim.',
            'source_sha256': sources, 'examples': examples,
            'literal_pinned_flow_checks': literal_flow_checks(),
            'exact_math_tests': tested.testsRun,
            'rejected_mutations': negatives,
            'source_mutation_rejected': True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='replace the local exact receipt')
    args = parser.parse_args()
    result = run()
    payload = json.dumps(result, indent=2, sort_keys=True)+'\n'
    target = HERE/'RESULT.json'
    if args.write:
        target.write_text(payload)
    else:
        E.need(target.read_text() == payload, 'receipt differs; inspect then run --write')
    print(json.dumps({'status': result['status'], 'examples': {
        name: {'H': item['uniform']['H'], 'v': item['net_tax']['v'],
               'method': item['uniform']['method']}
        for name, item in result['examples'].items()},
        'exact_math_tests': result['exact_math_tests'],
        'rejected_mutations': len(result['rejected_mutations'])}, sort_keys=True))


if __name__ == '__main__':
    main()
