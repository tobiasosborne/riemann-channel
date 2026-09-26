#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane I (claude:opus, 2026-09-26): Gram matrices at NON-admissible widths, recomputed
from the definitions in real space, independent of scripts/rtp2_impure_bumps.py (no Chebyshev R_1, no 1D
finite-part integral over q): every archimedean entry is a nested 2D tanh-sinh integral over (x, y) or (x, w)
of the bump itself, split at every support edge;
  D > 2 delta :  W_R-part = int int phi(x) phi(w) rho(D + x - w) dx dw
  D <= 2 delta:  W_R-part = (log 4 pi + gamma) F(0) + int_x phi(x) int_0^Y [phi(x-y+D) + phi(x+y+D) - 2 e^{-y/2} phi(x+D)] rho(y) dy dx
                            + F(0) log tanh(Y/2),     Y = D + 2 delta,  F(y) = R_delta(y - D)
(CCM mc2arXiv.tex l.451: W_R(F) = (log 4pi+gamma)F(1) + int_1^oo (F(x)+F(1/x) - 2x^{-1/2}F(1)) x^{1/2}/(x-x^{-1}) d*x);
pole 2 cosh(D/2) c^2 (= Fhat(i/2)+Fhat(-i/2) exactly); prime term summed over ALL prime powers with
|log k -+ D| < 2 delta, each R_delta by direct quadrature, and SUBTRACTED (Psi = W02 - W_R - sum_p W_p, l.465-467).
Normalised by N = R_delta(0).  mpmath dps 30; eigenpairs by mp.eigsy.  Deterministic; 64 worker processes."""
import sys, os, math, itertools, bisect, json
from multiprocessing import Pool
import numpy as np
import mpmath as mp
mp.mp.dps = 30
NC = [0, 0]
def check(c, m):
    NC[0] += 1; NC[1] += (not c); print(('PASS ' if c else 'FAIL ') + m, flush=True)
X = 20000
sv = bytearray([1]) * (X + 1); sv[0] = sv[1] = 0
for p in range(2, int(X ** .5) + 1):
    if sv[p]: sv[p*p::p] = bytearray(len(sv[p*p::p]))
PP = {}
for p in range(2, X + 1):
    if sv[p]:
        k = p
        while k <= X: PP[k] = p; k *= p
KS = sorted(PP)
def phi(x, d):
    t = x / d
    return mp.exp(-1 / (1 - t * t)) if abs(t) < 1 else mp.mpf(0)
def rho(y): return mp.exp(y / 2) / (2 * mp.sinh(y))
def Rd(s, d):
    s = abs(s); lo, hi = s - d, d
    if lo >= hi: return mp.mpf(0)
    return mp.quad(lambda x: phi(x, d) * phi(x - s, d), [lo, (lo + hi) / 2, hi])
def cdel(d): return mp.quad(lambda x: phi(x, d) * mp.exp(x / 2), [-d, 0, d])
def arch(D, d):
    if D > 2 * d:
        return mp.quad(lambda x, w: phi(x, d) * phi(w, d) * rho(D + x - w), [-d, 0, d], [-d, 0, d])
    Y = D + 2 * d
    F0 = Rd(D, d)
    def inner(x):
        px = phi(x, d)
        if px == 0: return mp.mpf(0)
        pd = phi(x + D, d)
        br = sorted(set([mp.mpf(0), Y] + [b for b in (x + D - d, x + D + d, -x - D - d, -x - D + d) if 0 < b < Y]))
        f = lambda y: (phi(x - y + D, d) + phi(x + y + D, d) - 2 * mp.exp(-y / 2) * pd) * rho(y)
        return px * mp.quad(f, br)
    xb = sorted(set([-d, mp.mpf(0), d] + [b for b in (d - D, -D - d) if -d < b < d]))
    I = mp.quad(inner, xb)
    return (mp.log(4 * mp.pi) + mp.euler) * F0 + I + F0 * mp.log(mp.tanh(Y / 2))
def vp(k, p):
    m = 0
    while k % p == 0: k //= p; m += 1
    return m
def entry(args):
    """E/H/R tag here is relative to the (S, A) of the job; the assembly re-classifies per case."""
    num, den, dstr, S, A = args
    d = mp.mpf(dstr); D = mp.log(num) - mp.log(den)
    po = 2 * mp.cosh(D / 2) * cdel(d) ** 2
    ar = arch(D, d)
    prime = {}
    for k in KS[: bisect.bisect_right(KS, int(mp.exp(D + 2 * d)) + 1)]:
        lk = mp.log(k)
        if abs(lk - D) < 2 * d or abs(lk + D) < 2 * d:
            p = PP[k]; m = vp(k, p)
            cls = 'E' if p not in S else ('H' if m > A else 'R')
            prime[k] = (cls, p, mp.log(p) / mp.sqrt(k) * (Rd(lk - D, d) + Rd(lk + D, d)))
    return (num, den, dstr), (po, ar, prime)
def cls(k, p, S, A):
    return 'E' if p not in S else ('H' if vp(k, p) > A else 'R')
def geometry(S, A):
    pts = list(itertools.product(range(A + 1), repeat=len(S)))
    ns = [math.prod(p ** a for p, a in zip(S, t)) for t in pts]
    return pts, ns
def schmidt(v, S, A):
    t = np.array(v, dtype=float).reshape((A + 1,) * len(S)); w = 0.
    for j in range(len(S)):
        s = np.linalg.svd(np.moveaxis(t, j, 0).reshape(A + 1, -1), compute_uv=False)
        w = max(w, 1 - s[0] ** 2 / np.sum(s ** 2))
    return w
def eig(M):
    E, Q = mp.eigsy(M)
    i = min(range(len(E)), key=lambda j: E[j]); E2 = sorted(E)
    v = [Q[r, i] for r in range(M.rows)]
    if max(v, key=abs) < 0: v = [-x for x in v]
    return E2, v
CASES = [((2, 3), 2, '0.2'), ((2, 3), 3, '0.2'), ((2, 3, 5), 2, '0.2'),
         ((2, 3), 2, '0.05937104123213741'), ((2, 3), 3, '0.048514948002721076'),
         ((2, 3, 5), 2, '0.02542631156085117'), ((2, 3), 2, '0.345')]
REPORT = {  # lambda_min, Schmidt defect, lambda(K)  (report I4 tables, mp table, blind-lane numbers)
    ((2, 3), 2, '0.2'): ('0.00135372063318383512', 0.00319814799166319, None),
    ((2, 3), 3, '0.2'): ('0.000180074626644884947', 0.02941071123436459, None),
    ((2, 3, 5), 2, '0.2'): ('0.0000382190776467145010', 0.0015005925219149239, None),
    ((2, 3), 2, '0.05937104123213741'): ('0.06643745839', 0.0051970692, -0.36178461),
    ((2, 3), 3, '0.048514948002721076'): ('0.01883676831', 0.0210979, -0.592137121),
    ((2, 3, 5), 2, '0.02542631156085117'): ('0.05333277369', 0.017018849, -0.912982341),
    ((2, 3), 2, '0.345'): ('8.842738307e-05', 0.0026738833, -0.00847737417)}
if __name__ == '__main__':
    jobs = {}
    geo = {}
    for S, A, ds in CASES:
        pts, ns = geometry(S, A); geo[(S, A)] = (pts, ns)
        for x in ns:
            for y in ns:
                g = math.gcd(x, y); a, b = max(x, y) // g, min(x, y) // g
                jobs[(a, b, ds, S, A)] = None
    with Pool(64) as pool:
        res = dict(pool.map(entry, list(jobs), chunksize=1))
    N = {ds: Rd(0, mp.mpf(ds)) for _, _, ds in CASES}
    summary = {}
    for S, A, ds in CASES:
        pts, ns = geo[(S, A)]; n = len(pts); nn = N[ds]
        G = mp.matrix(n, n); K = mp.matrix(n, n)
        Mp = mp.matrix(n, n); Ma = mp.matrix(n, n); Mcls = {c: mp.matrix(n, n) for c in 'EHR'}
        for i in range(n):
            for j in range(n):
                x, y = ns[i], ns[j]; g = math.gcd(x, y); a, b = max(x, y) // g, min(x, y) // g
                po, ar, prime = res[(a, b, ds)]
                pr = mp.fsum(v for _, _, v in prime.values())
                G[i, j] = (po - ar - pr) / nn
                mixed = sum(u != w for u, w in zip(pts[i], pts[j])) >= 2
                if mixed:
                    Mp[i, j] = po / nn; Ma[i, j] = -ar / nn
                    for c in 'EHR': Mcls[c][i, j] = -mp.fsum(v for kk, (_, pp, v) in prime.items() if cls(kk, pp, S, A) == c) / nn
                else: K[i, j] = G[i, j]
        # minus-sign decomposition: G = K + M_pole + M_arch - sum_k w_k (X o P_k) with P_k >= 0
        rec = K + Mp + Ma + Mcls['E'] + Mcls['H'] + Mcls['R']
        dec = max(abs(rec[i, j] - G[i, j]) for i in range(n) for j in range(n))
        signs = all(Mcls[c][i, j] <= 0 for c in 'EHR' for i in range(n) for j in range(n))
        check(dec < mp.mpf(10) ** -25 and signs, f'{S} A={A} delta={ds}: G = K + Mpole + March - (mixed prime), every mixed prime entry <= 0 (sign as in Psi = W02 - W_R - sum W_p)')
        E, v = eig(G); EK, v0 = eig(K)
        dfct = schmidt([float(t) for t in v], S, A)
        lamR, dR, lkR = REPORT[(S, A, ds)]
        tol = mp.mpf('1e-14') if ds == '0.2' else mp.mpf(10) ** -(len(lamR.split('e')[0].replace('0.', '').lstrip('0')) + 1) * 5
        okK = lkR is None or abs(EK[0] - lkR) < 1e-8
        check(abs(E[0] - mp.mpf(lamR)) < max(tol, mp.mpf(lamR) * 1e-8) and abs(dfct - dR) < 1e-8 and okK and E[0] > 0,
              f'{S} A={A} delta={ds}: lambda_min(G) = {mp.nstr(E[0], 22)} (report {lamR}), diff {mp.nstr(abs(E[0]-mp.mpf(lamR)),3)}; gap {mp.nstr(E[1]-E[0],6)}; '
              f'Schmidt defect {dfct:.10g} (report {dR}); lambda(K) = {mp.nstr(EK[0], 10)} (report {lkR})')
        # Kronecker identity: K equals the Kronecker sum of independently assembled one-prime forms
        dd = float(G[0, 0]); Kn = np.array(K.tolist(), dtype=float)
        ks = np.zeros((n, n))
        for q, p in enumerate(S):
            Gp = np.array([[float(G[pts.index(tuple((a if r == q else 0) for r in range(len(S)))), pts.index(tuple((b if r == q else 0) for r in range(len(S))))])
                            for b in range(A + 1)] for a in range(A + 1)])
            term = np.array([[1.]])
            for r in range(len(S)): term = np.kron(term, Gp - dd * np.eye(A + 1) if r == q else np.eye(A + 1))
            ks += term
        ks += dd * np.eye(n)
        check(np.max(np.abs(ks - Kn)) < 1e-13, f'{S} A={A} delta={ds}: K (mixed zeroed) = Kronecker sum of the full one-prime forms, max diff {np.max(np.abs(ks-Kn)):.2e}')
        vv = np.array([float(t) for t in v]); v0n = np.array([float(t) for t in v0])
        parts = dict(pole=Mp, arch=Ma, E=Mcls['E'], H=Mcls['H'], R=Mcls['R'])
        along = {k: float(vv @ np.array(M.tolist(), dtype=float) @ vv) for k, M in parts.items()}
        first = {k: float(v0n @ np.array(M.tolist(), dtype=float) @ v0n) for k, M in parts.items()}
        ext = sorted({p for key in [(max(x, y) // math.gcd(x, y), min(x, y) // math.gcd(x, y), ds) for x in ns for y in ns]
                      for kk, (_, p, _) in res[key][2].items() if p not in S})
        print(f'    along v: {json.dumps({k: round(x, 10) for k, x in along.items()})}')
        print(f'    along v0: {json.dumps({k: round(x, 10) for k, x in first.items()})}; |<v,v0>| = {abs(vv @ v0n):.8f}; external primes {ext}')
        summary[(S, A, ds)] = dict(G=G, K=K, v=vv, v0=v0n, E=E, EK=EK, parts=parts, along=along)
        if (S, A, ds) == ((2, 3), 2, '0.2'):
            # report: E -1.517296509 / -1.390753653, H -0.04205917985 / -0.04066886719, R -0.1310258173 / -0.09275883215 (along v / v0)
            okc = (abs(along['E'] + 1.517296509) < 1e-8 and abs(along['H'] + 0.04205917985) < 1e-9 and abs(along['R'] + 0.1310258173) < 1e-9
                   and abs(first['E'] + 1.390753653) < 1e-8 and abs(first['R'] + 0.09275883215) < 1e-9)
            check(okc, 'E/H/R split of the mixed prime part at {2,3} A=2 delta=0.2 reproduced')
            # Schur bounds I2c (report 0.002147677857 <= defect <= 0.003201624504)
            C = vv.reshape(3, 3); C0 = v0n.reshape(3, 3)
            U, s, Vt = np.linalg.svd(C0)
            Cr = U.T @ C @ Vt.T
            if Cr[0, 0] < 0: Cr = -Cr
            a = Cr[0, 0]; x = Cr[1:, 0]; y = Cr[0, 1:]; T = Cr[1:, 1:] - np.outer(x, y) / a
            hF = np.linalg.norm(T); low = (hF / ((1 + np.linalg.norm(x) / a) * (1 + np.linalg.norm(y) / a))) ** 2
            check(a >= np.linalg.norm(T, 2) and abs(low - 0.002147677857) < 1e-9 and abs(hF ** 2 - 0.003201624504) < 1e-9 and low <= dfct <= hF ** 2,
                  f'I2c Schur bounds at delta=0.2: {low:.10f} <= {dfct:.10f} <= {hF**2:.10f}')
            # ablations (report: no_external -2.9496987345, no_mixed_pole -3.8055745265, no_mixed_arch -0.92987066659, no_mixed_prime -3.0178280392)
            Gn = np.array(G.tolist(), dtype=float)
            # no_external removes ALL entries of external primes, including axis/diagonal ones
            Eall = np.zeros((n, n))
            for i in range(n):
                for j in range(n):
                    x_, y_ = ns[i], ns[j]; g = math.gcd(x_, y_)
                    Eall[i, j] = float(mp.fsum(val for _, p_, val in res[(max(x_, y_) // g, min(x_, y_) // g, ds)][2].values() if p_ not in S) / nn)
            abl = {'no_external': Gn + Eall, 'no_mixed_pole': Gn - np.array(Mp.tolist(), dtype=float), 'no_mixed_arch': Gn - np.array(Ma.tolist(), dtype=float),
                   'no_mixed_prime': Gn - sum(np.array(Mcls[c].tolist(), dtype=float) for c in 'EHR')}
            refs = {'no_external': (-2.9496987345, 0.3810989831), 'no_mixed_pole': (-3.8055745265, 0.09151970754), 'no_mixed_arch': (-0.92987066659, 0.3323333617), 'no_mixed_prime': (-3.0178280392, 0.3678526529)}
            for k, M in abl.items():
                w, V = np.linalg.eigh(M)
                check(abs(w[0] - refs[k][0]) < 1e-8 and abs(schmidt(V[:, 0], S, A) - refs[k][1]) < 1e-7, f'ablation {k}: lambda {w[0]:.10f}, defect {schmidt(V[:,0],S,A):.10f} (report {refs[k]})')
            np.save(os.path.join(os.path.dirname(__file__), 'scratch_rtp2_impure_G23A2d02.npy'), Gn)
    print(f'# checks: {NC[0]} run, {NC[1]} failed')
