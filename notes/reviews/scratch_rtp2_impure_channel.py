#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane I (claude:opus, 2026-09-26): is the impure channel a "third-prime channel"?
Reviewer's real-space entries (scratch_rtp2_impure_gram.entry).  On {2,3}, A=2, at two non-admissible widths:
the per-prime amplitude matrices B_q (ALL entries, axes included) for q = 2, 3 and every external q; the exact
first-order responses d lambda/d theta_q = -v^T B_q v and d(defect)/d theta_q (centred differences, h = 1e-6),
the same for the mixed pole and mixed archimedean amplitudes, and the mixed-only restriction X o B_q.
Also I5: {2,3} -> {2,3,5} -> {2,3,5,7} at A = 1, delta = 0.2 (movement = 1 - overlap on the old sublattice)."""
import sys, os, math, itertools
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np, mpmath as mp
from multiprocessing import Pool
import scratch_rtp2_impure_gram as g
NC = [0, 0]
def check(c, m):
    NC[0] += 1; NC[1] += (not c); print(('PASS ' if c else 'FAIL ') + m, flush=True)
def key(x, y):
    gg = math.gcd(x, y); return max(x, y) // gg, min(x, y) // gg
def assemble(S, A, ds, res):
    pts, ns = g.geometry(S, A); n = len(pts); nn = g.Rd(0, mp.mpf(ds))
    po = np.zeros((n, n)); ar = po.copy(); mix = np.zeros((n, n), bool); Bq = {}
    for i in range(n):
        for j in range(n):
            a, b = key(ns[i], ns[j]); p_, a_, prime = res[(a, b, ds)]
            po[i, j] = float(p_ / nn); ar[i, j] = float(a_ / nn); mix[i, j] = sum(u != w for u, w in zip(pts[i], pts[j])) >= 2
            for k, (cl, p, val) in prime.items():
                Bq.setdefault(p, np.zeros((n, n)))[i, j] += float(val / nn)
    G = po - ar - sum(Bq.values())
    return G, po, ar, mix, Bq
def ground(M):
    w, V = np.linalg.eigh(M); v = V[:, 0]
    return w, (v if v[np.argmax(abs(v))] > 0 else -v)
if __name__ == '__main__':
    cases = [((2, 3), 2, '0.2'), ((2, 3), 2, '0.05937104123213741'), ((2, 3), 1, '0.2'), ((2, 3, 5), 1, '0.2'), ((2, 3, 5, 7), 1, '0.2')]
    jobs = set()
    for S, A, ds in cases:
        _, ns = g.geometry(S, A)
        for x in ns:
            for y in ns: jobs.add(key(x, y) + (ds, S, A))
    # entry() classifies E/H/R relative to (S, A); per-prime sums below do not use the class
    with Pool(64) as pool:
        out = pool.map(g.entry, sorted(jobs, key=lambda t: (t[2], t[0] / t[1])), chunksize=1)
    res = {}
    for k, v in out: res[k] = v
    for S, A, ds in cases[:2]:
        G, po, ar, mix, Bq = assemble(S, A, ds, res)
        w, v = ground(G); df0 = g.schmidt(v, S, A)
        print(f'{S} A={A} delta={ds}: lambda {w[0]:.12g}, gap {w[1]-w[0]:.4g}, defect {df0:.8g}')
        amps = {f'theta_{q}': B for q, B in sorted(Bq.items())}
        amps['mixed pole'] = -po * mix; amps['mixed arch'] = ar * mix   # dG/damp = -B convention: G(theta) = G - (theta-1) B
        for q, B in sorted(Bq.items()): amps[f'mixed part of theta_{q}'] = B * mix
        rows = []
        for name, B in amps.items():
            h = 1e-6
            dp = g.schmidt(ground(G - h * B)[1], S, A); dm = g.schmidt(ground(G + h * B)[1], S, A)
            dl = -float(v @ B @ v); dd = (dp - dm) / (2 * h)
            rows.append((name, dl, dd, float(np.linalg.norm(B * mix, 2)), float(np.linalg.norm(B * ~mix, 2))))
        for r in rows:
            print(f'   {r[0]:>24}: dlambda {r[1]:+.5f}  d(defect) {r[2]:+.5f}   ||mixed part|| {r[3]:.4f}  ||axis+diag part|| {r[4]:.4f}')
        ext = [r for r in rows if r[0].startswith('theta_') and int(r[0][6:]) not in S]
        loc = [r for r in rows if r[0].startswith('theta_') and int(r[0][6:]) in S]
        sE = sum(abs(r[2]) for r in ext); sL = sum(abs(r[2]) for r in loc)
        pa = [r for r in rows if r[0] in ('mixed pole', 'mixed arch')]
        print(f'   sum |d defect|: external primes {sE:.4f}, primes 2 and 3 {sL:.4f}, mixed pole {abs(pa[0][2]):.4f}, mixed arch {abs(pa[1][2]):.4f}')
        print(f'   sum |d lambda|: external primes {sum(abs(r[1]) for r in ext):.4f}, primes 2 and 3 {sum(abs(r[1]) for r in loc):.4f}')
        if ds == '0.2':
            check(abs(w[0] - 0.00135372063318383512) < 1e-13, 'baseline reproduces the report lambda at delta = 0.2')
            ref = {5: -0.441838446, 7: -0.3338406, 37: -0.0490887763}
            check(all(abs(-float(v @ Bq[q] @ v) - x) < 1e-8 for q, x in ref.items()), 'd lambda/d theta_q for q = 5, 7, 37 reproduce the report sensitivity table')
    # I5 at A = 1, delta = 0.2
    chain = [((2, 3), 1), ((2, 3, 5), 1), ((2, 3, 5, 7), 1)]
    vecs = {}
    for S, A in chain:
        G, *_ = assemble(S, A, '0.2', res); w, v = ground(G); vecs[S] = (w[0], v)
    rep = {((2, 3), (2, 3, 5)): (0.009617377905, 0.002228248928, 0.01341788669), ((2, 3, 5), (2, 3, 5, 7)): (0.002228248928, 0.0002422501422, 0.01852628918)}
    for (s, b), (ls, lb, mv) in rep.items():
        vb = vecs[b][1].reshape((2,) * len(b))[..., 0].flatten(); ov = abs(vb @ vecs[s][1]) / np.linalg.norm(vb)
        check(abs(vecs[s][0] - ls) < 1e-11 and abs(vecs[b][0] - lb) < 1e-11 and abs(1 - ov - mv) < 1e-9,
              f'I5 A=1 delta=0.2 {s} -> {b}: lambda {vecs[s][0]:.10g} -> {vecs[b][0]:.10g}, movement {1-ov:.10g} (report {ls}, {lb}, {mv})')
    print(f'# checks: {NC[0]} run, {NC[1]} failed')
