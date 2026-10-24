"""Exact missing-span retiming. Apache-2.0; substantial Codex assistance.

Retains zxv's native words and the fresh-helper-boundary retiming lemma.
No source predicate is relaxed: every transport remains nested and positive.
"""
from collections import Counter
from copy import deepcopy
from pathlib import Path
import sys
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT/'research/fresh-helper-boundary'))
import native as F
need = F.need


def run():
    patch = F.read(HERE/'PATCH.json')
    c = F.read(F.BASE/'THREE-base-FULL-IDENTITY-CANONICAL.json.gz')
    original = F.read(F.BASE/'THREE-base-FULL-IDENTITY-NATIVE.json.gz')
    changes = F.read(F.HERE/'CHANGES.json')
    for key, field in [('entrances', 'start'), ('exits', 'final')]:
        for role, old, new in changes[key]:
            need(c[field][role] == old, 'Pinned helper boundary')
            c[field][role] = new
    for direction, program in original.items():
        keys = F.gates(program)
        for phase, ordinal, old, new in changes['gates']:
            event = program[keys[phase, ordinal]]
            need(event[2] == old, 'Pinned source scalar frame')
            event[2] = new
    basis = patch['new_basis']; space = F.span(basis)
    lower = F.span([x for f in patch['incoming_frames'] for x in c['frames'][f]])
    upper = set.intersection(*(set(F.span(c['frames'][f])) for f in patch['outgoing_frames']))
    need(space == lower and len(space) == 8 and space <= upper, 'Actual missing three-dimensional span')
    need(c['frames'][patch['old_frame']] == patch['old_basis'], 'Pinned old four-dimensional frame')
    need(space not in [F.span(b) for b in c['frames']], 'The span really is absent from the frozen catalog')
    new_frame = len(c['frames']); c['frames'].append(basis)
    before = {d: F.synthesize(c, p) for d, p in original.items()}
    for direction, program in original.items():
        index = F.gates(program)[patch['phase'], patch['ordinal']]
        need(program[index][2] == patch['old_frame'], 'Bound unique new scalar contact')
        program[index][2] = new_frame
    programs = {d: F.synthesize(c, p) for d, p in original.items()}
    V = F.load(ROOT/'research/kappa-causal-continuation/buffer-borrowing/verify_buffers.py', 'join_rows')
    X = F.load(ROOT/'research/kappa-rebuild/complex/native_extensions.py', 'join_literal')
    receipts, profiles = {}, {}
    for direction, program in programs.items():
        backward = direction == 'backward'
        rows, rec = X.literal_replay(V, c, program, backward)
        for r in range(632):
            need(rows['L', r] == V.expected(('L', r), [], backward, False), 'All 632 actual arbitrary-input endpoints')
        profiles[direction] = Counter({int(k): v for k, v in rec['paid_profile'].items()})
        rebound = deepcopy(c); rebound['local_profile'] = dict(profiles[direction])
        rec['second_literal'] = V.replay(program, rebound, [], backward, False)
        receipts[direction] = rec
    paid = Counter({1:2254, 2:514, 3:444, 4:103, 5:40, 8:8})
    need(profiles['forward'] == profiles['backward'] == paid, 'Both complete new physical rank bills')
    H = Counter()
    for r in range(224, 632):
        a, b = c['start'][r], c['final'][r]
        need(F.span(c['frames'][a]) < F.span(c['frames'][b]), 'Every helper remains independently productive')
        H[len(c['frames'][b])-len(c['frames'][a])] += 1
    need(H == {4:26, 5:2, 7:29, 8:42, 9:309}, 'All 408 helper jobs retained')
    edges = lambda p: {(e[3], e[4]) for e in p if e[0] == 'climb'}
    new_edges = edges(programs['forward'])-edges(before['forward'])
    need(new_edges == {(364,new_frame), (360,new_frame), (new_frame,736), (new_frame,692)}, 'Exactly the four announced new transports')
    ce = F.load(ROOT/'research/t74-native-fast/vendor/native/new/code/borrow/vendor/clifford/clifford_exact.py', 'join_clifford')
    P = F.load(ROOT/'research/kappa-function-composition/complex/prune_native.py', 'join_phase_decode')
    physical = []
    for a, b in sorted(new_edges):
        op = ce.canonical_frame(9,c['frames'][a]).adjoint().then(ce.canonical_frame(9,c['frames'][b]))
        rank = len(c['frames'][b])-len(c['frames'][a]); directions = {}
        for d in ('forward', 'backward'):
            actual = P.conjugate(ce,op) if d == 'backward' else op
            rec = X.N.lower_exact(P,ce,actual)
            need(rec['rank'] == rank, 'Exact new Fourier rank, tableau and absolute phase')
            directions[d] = rec
        physical.append({'old':a, 'new':b, 'rank':rank, 'recipes':directions})
    # Changing the emitted rank while keeping the physical contact must fail.
    bad = deepcopy(programs['forward'])
    next(e for e in bad if e[0] == 'climb' and e[4] == new_frame)[5] += 1
    rejected = False
    try:
        rebound = deepcopy(c); rebound['local_profile'] = dict(paid)
        V.replay(bad,rebound,[],False,False)
    except (ValueError, AssertionError):
        rejected = True
    need(rejected, 'An understated or overstated physical transport rank is rejected')
    return {'status':'PASS_MISSING_JOIN_BOTH_ORIENTATIONS_ALL_632_COLUMNS',
            'helpers':dict(sorted(H.items())), 'paid':dict(sorted(paid.items())),
            'new_basis':basis, 'native':receipts, 'new_physical_edges':physical,
            'wrong_emitted_rank_rejected':rejected}


if __name__ == '__main__':
    import json
    print(json.dumps(run(),sort_keys=True))
