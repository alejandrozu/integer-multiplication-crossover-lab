#!/usr/bin/env python3
"""Exact finite certificates for the adaptive-height, padding-free compiler.

Conditional on the raw native word and the integer-flow contracts in PROOF.md.
zxv, with substantial OpenAI Codex assistance. Apache-2.0.
"""
import argparse
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
import json
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import intervals as E

ONE = (Q(1), Q(1))


def hist(value):
    E.need(value and isinstance(value, dict), 'nonempty histogram')
    out = {}
    for k, n in value.items():
        r = int(k)
        E.need(str(r) == str(k) and r >= 1 and type(n) is int and n > 0,
               'canonical positive rank and multiplicity')
        out[r] = n
    return out


def mean(h, t):
    total = (Q(0), Q(0))
    for r, n in h.items():
        total = E.add(total, E.scale(E.mul(E.power(r, t), E.log_bounds(r)), n))
    return E.divide(total, E.moment(h, t))


def log_interval(x):
    E.need(x[0] > 0, 'positive logarithm interval')
    def at(q):
        return E.sub(E.log_bounds(q.numerator), E.log_bounds(q.denominator))
    return at(x[0])[0], at(x[1])[1]


def mirror_windows(T, P):
    """Exact (left,right] cells; positive histograms for the two mirror sides."""
    cuts = sorted({Q(0), *[Q(1, k) for k in T], *[Q(1, r) for r in P]})
    cells = []
    for left, right in zip(cuts, cuts[1:]):
        x = (left+right)/2
        exit_hist, source_hist = Counter(), Counter()
        for r, count in P.items():
            for k, weight in T.items():
                if r > k and Q(1, r) < x <= Q(1, k):
                    exit_hist[r*k] += count*weight
                if k > r and Q(1, k) < x <= Q(1, r):
                    source_hist[r*k] += count*weight
        if exit_hist:
            E.need(source_hist, 'boundary mirror window without source funding')
            cells.append((left, right, exit_hist, source_hist))
    return cells


def mirror_certificate(T, P, t0, thi, beta, slices):
    E.need(type(slices) is int and 1 <= slices <= 1000, 'bounded exponent cover')
    best, witness = Q(0), None
    cells = mirror_windows(T, P)
    for i in range(slices):
        lo, hi = t0+(thi-t0)*i/slices, t0+(thi-t0)*(i+1)/slices
        for left, right, exits, sources in cells:
            ratio = E.divide(E.moment(exits, hi), E.moment(sources, lo))
            E.need(ratio[1] < beta, 'uniform boundary mirror coefficient')
            if ratio[1] > best:
                best, witness = ratio[1], {'exponent_lower': str(lo),
                    'exponent_upper': str(hi), 'window': [str(left), str(right)]}
    return {'cells': len(cells), 'exponent_slices': slices,
            'maximum_upper': E.display((best, best)), 'maximizing_cell': witness}


def certify(profile, w):
    T, P = hist(profile['targets']), hist(profile['paid'])
    m = max(T)
    E.need(2 <= min(T) and max(P) < m and P.get(1, 0) > 0,
           'raw overlapping-flow contract and nonempty forest')
    E.need(sum(k*n for k, n in T.items()) > sum(k*n for k, n in P.items()),
           'raw positive rank-one surplus')
    t0, thi, p, c, s, lam = (Q(w[k]) for k in ('t0', 't_upper', 'p', 'c', 's', 'lambda'))
    a, b, M, ell = (w[k] for k in ('a', 'b', 'height_base', 'ell0'))
    E.need(all(type(x) is int and x >= 1 for x in (a, b, ell))
           and type(M) is int and M >= 2, 'integer adaptive-height geometry')
    E.need(0 < t0 < thi < 1 and p > 0 and s > 0 and lam > 0,
           'adaptive exponent domain')
    E.need(c >= p/(1-t0), 'concave funded majorant domain')
    guards = {k: Q(w['guards'][k]) for k in ('U', 'V', 'Q', 'd', 'beta', 'eta')}
    U, V, Qmax, d, beta, eta_min = (guards[k] for k in ('U', 'V', 'Q', 'd', 'beta', 'eta'))
    E.need(0 < U < 1 and 0 < V < 1 and Qmax > 1 and d > 0
           and 0 < beta < eta_min < 1, 'finite guard domains')
    logm, logM, log2 = E.log_bounds(m), E.log_bounds(M), E.log_bounds(2)
    logn0 = E.add(logm, E.scale(logM, ell))
    tau_max = E.add((t0, t0), E.divide((p, p), E.add((c, c), logn0)))
    E.need(tau_max[1] < thi, 'local exponent interval covers ordinary base cutoff')
    T0, P0 = E.moment(T, t0), E.moment(P, t0)
    E.need(T0[0] > P0[1], 'raw strict moment at base exponent')
    q_upper = E.divide(E.moment(T, thi), P0)
    E.need(q_upper[1] < Qmax, 'uniform moment ratio Q')
    derivative = E.sub(mean(T, t0), mean(P, thi))
    E.need(derivative[0] > d, 'uniform positive tilted log-mean gap')

    def ratio(h, t):
        return E.divide(E.moment(h, t+s), E.moment(h, t))
    target_low, paid_high = ratio(T, t0), ratio(P, thi)
    E.need(target_low[0] > paid_high[1], 'mixed layer endpoint dominates every lower layer')
    u = E.mul(E.power(M, -s), E.mul(E.ipow(ratio(T, thi), a), E.ipow(paid_high, b)))
    E.need(u[1] < U, 'mixed layer Chernoff U')
    v = E.mul(E.power(M, lam), E.ipow(E.divide(E.moment(T, thi-lam), P0), a+b))
    E.need(v[1] < V, 'root source Chernoff V')
    eta = E.scale(E.power(m, t0-1), t0)
    E.need(eta[0] > eta_min, 'source complement capacity')
    mirrors = mirror_certificate(T, P, t0, thi, beta, w.get('mirror_slices', 20))

    denominator = E.add((c, c), E.add(logm, E.add(E.scale(logM, ell+1), log2)))
    exponent = E.divide((d*p*(a*ell+1),)*2, denominator)
    gain = E.sub(E.exp_interval(exponent), ONE)
    lower_D = E.sub(E.scale(gain, 1-U**ell), E.scale(E.power(M, lam), Qmax*V**ell))
    required = (1-eta_min)/(eta_min-beta)
    E.need(lower_D[0] > required, 'sharp source and boundary cancellation for all heights')
    # With a>=1, the derivative of (a*l+1)/(constant+(l+1)logM)
    # has numerator a*(c+logm+log2)+(a-1)logM >0.
    monotone = E.add(E.scale(E.add((c, c), E.add(logm, log2)), a),
                     E.scale(logM, a-1))
    E.need(monotone[0] > 0, 'uniform height monotonicity')
    logA = E.sub(E.scale(logn0, 1-t0),
                  E.scale(log_interval(E.add((c, c), logn0)), p))
    saving, kappa = Q(w['uniform_saving']), Q(w['kappa'])
    gap = 1-saving-t0
    E.need(0 < kappa < saving < 1-t0 and gap > 0, 'funded uniform and consumer savings')

    def final_margin(H):
        x = E.scale(log2, H)
        lhs = E.add(logA, E.scale(log_interval(E.add((c, c), x)), p))
        return E.sub(E.scale(x, gap), lhs)

    H = w['H']
    E.need(type(H) is int and H > 0 and Q(H)*log2[0] > logn0[1],
           'uniform rank beyond ordinary base')
    margin = final_margin(H)
    E.need(margin[0] > 0, 'funded final uniform-rank inequality')
    E.need(gap*(c+H*log2[0]) > p, 'final comparison remains true at larger ranks')
    return {'status': 'PASS_ADAPTIVE_HEIGHT_DIRECT_COMPILER',
        'raw_ambient': m, 'raw_minimum_target': min(T), 'raw_maximum_paid': max(P),
        'raw_fields': sum(T.values()), 'tensor_power': 1,
        't0': str(t0), 't_upper': str(thi), 'p': str(p), 'c': str(c),
        'height_base': M, 'height_multiplier': a+b, 'ell0': ell,
        'ordinary_base': str(m)+'*'+str(M)+'^'+str(ell),
        'local_exponent_max': E.display(tau_max),
        'q_base': E.display(E.divide(T0, P0)), 'q_upper': E.display(q_upper),
        'tilted_log_mean_gap': E.display(derivative),
        'target_mgf_lower': E.display(target_low), 'paid_mgf_upper': E.display(paid_high),
        'mixed_chernoff': E.display(u), 'root_chernoff': E.display(v),
        'source_capacity': E.display(eta), 'mirror': mirrors,
        'uniform_D_lower': E.display(lower_D), 'required_D_upper': str(required),
        'log_majorant_normalization': E.display(logA),
        'H': H, 'N': '2^'+str(H), 'uniform_saving': str(saving),
        'kappa': str(kappa), 'uniform_gap': str(gap),
        'final_logarithmic_margin': E.display(margin),
        'word_materialized': False, 'native_and_outer_producers_replayed': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('profile', type=Path)
    parser.add_argument('witness', type=Path)
    args = parser.parse_args()
    print(json.dumps(certify(json.loads(args.profile.read_text()),
                             json.loads(args.witness.read_text())), indent=2, sort_keys=True))
