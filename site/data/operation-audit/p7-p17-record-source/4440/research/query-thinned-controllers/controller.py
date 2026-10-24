#!/usr/bin/env python3
"""Exact native/query controller construction. Apache-2.0; Codex assistance."""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def need(ok, message):
    if not ok:
        raise ValueError(message)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def engines():
    reference = ROOT/'research/kappa-0023-productive-jobs/dependencies/kappa-next-regime/bit-compression/carrier-reuse/reference/joint_pair_dag.py'
    load(reference, 'joint_pair_dag')
    base = ROOT/'research/kappa-rebuild/bit'
    bit = load(base/'mixed_productive_bit.py', 'mixed_productive_bit')
    complex_ = load(base/'complex_controller_factor.py', 'query_complex_factor')
    return bit, complex_


def keep_mask(p, a):
    b = p-1-a
    return sum(1 << i for i in list(range(1, 2*p-2, 2))+
               list(range(0, 2*a, 2))+list(range(3*(p-1)-b, 3*(p-1))))


def thick_stages(p):
    return {0, 2*p, *range(1, 2*p, 2)}


def specialize_complex(coefficients, thick):
    result = {}
    for term, matrix in coefficients.items():
        key = (term[0],)+tuple(x if s in thick else 0 for s, x in enumerate(term[1:]))
        out = result.setdefault(key, [[Q(0)]*len(matrix) for _ in matrix])
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                out[i][j] += value
    return {k: m for k, m in result.items() if any(any(row) for row in m)}


def specialize_bit(coefficients, thick):
    keep = 1+sum(1 << (s+1) for s in thick)
    out = {}
    for term, matrix in coefficients.items():
        key = term & keep
        old = out.setdefault(key, [0]*len(matrix))
        for i, row in enumerate(matrix):
            old[i] ^= row
    return {k: m for k, m in out.items() if any(m)}


def replay_events(events, p, kind):
    """Literal second replay of the emitted word, including query-only gates."""
    _, engine = engines()
    size, stages = 2*p, 2*p+1
    zero = (0,)*(stages+1)
    matrix = [[{zero: Q(i == j)} if i == j else {} for j in range(size)] for i in range(size)]
    for event in events:
        op = event[0]
        if op in ('LOCAL', 'QUERY_SHEAR'):
            _, stage, pair, backward = event
            x, y = 2*pair, 2*pair+1
            if backward: x, y = y, x
            term = (1 if backward else -1,)+(0,)*stages
            matrix[y] = [engine.plus(a, engine.monomial_times(b, term, -1 if backward else 1)) for a, b in zip(matrix[y], matrix[x])]
            if op == 'LOCAL':
                term = (0,)+tuple(int(s == stage) for s in range(stages))
                for role in (x, y): matrix[role] = [engine.monomial_times(a, term) for a in matrix[role]]
        elif op == 'IDLE':
            _, pair, selected = event
            term = (0,)+tuple(int(s in selected) for s in range(stages))
            for role in (2*pair, 2*pair+1): matrix[role] = [engine.monomial_times(a, term) for a in matrix[role]]
        elif op == 'ADD':
            _, dst, src, *coefficient = event
            c = coefficient[0] if coefficient else 1
            matrix[dst] = [engine.plus(a, b, c) for a, b in zip(matrix[dst], matrix[src])]
        elif op in ('SWAP', 'SIGNED_SWAP'):
            _, x, y = event
            matrix[x], matrix[y] = matrix[y], [engine.monomial_times(a, zero, -1 if op == 'SIGNED_SWAP' else 1) for a in matrix[x]]
        else:
            raise ValueError('Unknown emitted event: '+op)
    result = {}
    for i, row in enumerate(matrix):
        for j, poly in enumerate(row):
            for key, value in poly.items():
                if kind == 'complex':
                    result.setdefault(key, [[Q(0)]*size for _ in range(size)])[i][j] += value
                elif value.numerator % 2:
                    need(value.denominator == 1, 'Integral binary replay coefficient')
                    term = (key[0] % 2)+sum((exponent % 2) << (s+1) for s, exponent in enumerate(key[1:]))
                    result.setdefault(term, [0]*size)[i] ^= 1 << j
    return {k: m for k, m in result.items() if any(any(r) for r in m)} if kind == 'complex' else {k: m for k, m in result.items() if any(m)}


def inventories(kind, p, a, diagonal, idles):
    thick = thick_stages(p)
    ports, block = (112, 8) if kind == 'complex' else (111, 7)
    if kind == 'complex':
        local = json.loads((ROOT/'research/kappa-rebuild/complex/full-identity-certificates/RESULT.json').read_text())['providers']['THREE-base']
        helpers = {int(k): v for k, v in local['helper_boundary']['widths'].items()}
        children = {int(k): v for k, v in local['unsplit_replays']['forward']['paid_profile'].items()}
        selected = [[s for s, x in enumerate(term[1:]) if x] for term in diagonal]
        need(all(term[0] in (-1, 1) for term in diagonal), 'Only legal central Gaussian normalizers')
    else:
        helpers = {8: 439}
        children = {1: 1323, 2: 1342, 3: 79, 4: 44, 5: 102, 6: 11, 7: 19}
        selected = [[s for s in range(2*p+1) if term >> (s+1) & 1] for term in diagonal]
        need(all(term & 1 for term in diagonal), 'Every binary main output retains its central rank-one factor')
    targets = Counter({r: len(thick)*n for r, n in helpers.items()})
    paid = Counter({r: len(thick)*n for r, n in children.items()})
    thin_calls = ports*(2*p+1-len(thick))
    paid[1] += thin_calls
    main = Counter()
    for stages in selected:
        need(set(stages) <= thick, 'No removed stage receives output credit')
        main[1+block*len(stages)] += ports
    targets.update(main)
    idle = Counter()
    for row in idles:
        if row['retained']:
            rank = block*len(thick.intersection(row['stages']))
            if rank:
                idle[rank] += 2*ports
    paid.update(idle)
    # A second derivation uses only the declared prefix/suffix intervals.
    expected_main = Counter({1+block*(p+2): 2*ports})
    expected_idle = Counter()
    for length in (a, p-1-a):
        for j in range(1, length+1):
            expected_main[1+block*(j+1)] += 2*ports
            expected_idle[block*(j+1)] += 2*ports
    need(main == expected_main and idle == expected_idle, 'Literal and interval-derived complete invoices agree')
    surplus = sum(r*n for r, n in targets.items())-sum(r*n for r, n in paid.items())
    need(surplus == (48*len(thick)-112 if kind == 'complex' else 48*len(thick)-111), 'Rank mass includes every query and lost helper')
    return {'targets': dict(sorted(targets.items())), 'paid': dict(sorted(paid.items())),
            'main': dict(sorted(main.items())), 'whole_idle': dict(sorted(idle.items())),
            'productive_fields': sum(targets.values()), 'paid_calls': sum(paid.values()),
            'rank_surplus': surplus, 'thin_queries': thin_calls,
            'thick_calls': len(thick), 'thick_stages': sorted(thick),
            'raw_scalar_record_bound': 10**9, 'owned_streams_reused_sequentially': 1}


def run(kind, p, a):
    bit, complex_ = engines()
    mask = keep_mask(p, a)
    thick = thick_stages(p)
    if kind == 'complex':
        coefficients, events, idles = complex_.controller(p, mask)
        coefficients = specialize_complex(coefficients, thick)
        factor = complex_.factor(coefficients)
        need(factor is not None, 'Exact rational Laurent simultaneous factorization')
        diagonal = factor['diagonal']
        boundaries = {'left': complex_.serialize_matrix(factor['left']),
                      'right': complex_.serialize_matrix(factor['right']),
                      'left_program': factor['left_program'], 'right_program': factor['right_program']}
        need(all(Q(row[-1]) in (1, -1) for program in (factor['left_program'], factor['right_program'])
                 for row in program if row[0] in ('ADD', 'SCALE')), 'Unit scalar boundary coefficients')
    else:
        coefficients, events, idles = bit.physical_controller(p, mask)
        coefficients = specialize_bit(coefficients, thick)
        factor = bit.simultaneous_monomial_factor(coefficients)
        need(factor is not None, 'Exact binary group-ring simultaneous factorization')
        diagonal = factor['diagonal_monomials']
        boundaries = factor
    invoice = inventories(kind, p, a, diagonal, idles)
    new_events = []
    for row in events:
        if row[0] == 'LOCAL' and row[1] not in thick:
            new_events.append(['QUERY_SHEAR', *row[1:]])
        elif row[0] == 'IDLE':
            selected = ([s for s in row[2] if s in thick] if kind == 'complex' else
                        [s for s in range(2*p+1) if row[2] >> (s+1) & 1 and s in thick])
            if selected:
                new_events.append(['IDLE', row[1], selected])
        else:
            new_events.append(row)
    need(sum(row[0] == 'LOCAL' for row in new_events) == p+2, 'Exactly p+2 full native calls')
    need(sum(row[0] == 'QUERY_SHEAR' for row in new_events) == p-1, 'Exactly p-1 copied-query shears')
    return {'kind': kind, 'pairs': p, 'prefix_pairs': a, 'keep_mask': mask,
            'ambient_rank': 1+(8 if kind == 'complex' else 7)*(p+2),
            'diagonal': diagonal, 'boundaries': boundaries,
            'physical_events': new_events, 'invoice': invoice}


if __name__ == '__main__':
    for kind, p, a in [('complex', 17, 8), ('bit', 16, 7)]:
        row = run(kind, p, a)
        path = HERE/(kind.upper()+'-CONTROLLER.json')
        path.write_text(json.dumps(row, indent=2, sort_keys=True)+'\n')
        print(kind, row['invoice'], flush=True)
