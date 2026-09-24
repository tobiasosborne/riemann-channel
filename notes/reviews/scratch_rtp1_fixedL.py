#!/usr/bin/env python3
"""REFUTE lane R, RTP-1 (claude:opus, 2026-09-24).  Claim C3 and the "edge effect" reading (B2, C12).
Fixed window L = log 50: pole + arch fixed, prime powers k <= X added one at a time with full weight
(1 - log k/L) (a partial-information form, not the CCM form except at X = 49).  Reviewer's own (a,b) and
ball LDL^T.  (1) inertia (certified) and lambda_min (inverse iteration + certified inertia bracket) at every X,
N = 60; (2) Rayleigh decomposition of eps at X = 49, N = 60 over the prime-power terms;
(3) adversarial tests of "barely indefinite = edge effect": all-but-49 at N = 60..240; all-but-k for interior k;
49 removed from a wider window L = log 53 (49 no longer at the edge); operator norm of the removed term.
Deterministic.  Usage: python3 scratch_rtp1_fixedL.py"""
import sys, os, math
import numpy as np
from flint import arb, ctx
import mpmath as mp
sys.path.insert(0, os.path.dirname(__file__))
import scratch_rtp1_ab as AB, scratch_rtp1_linalg as LA
NCHK = [0, 0]
def check(c, m):
    NCHK[0] += 1; NCHK[1] += (not c); print(('PASS ' if c else 'FAIL ') + m, flush=True)
PREC = 3000
ctx.prec = PREC
mp.mp.dps = 40

def even_block_np(a, b):
    M = len(a) - 1
    af = [float(t.mid()) for t in a]; bf = [float(t.mid()) for t in b]
    E = np.zeros((M + 1, M + 1))
    E[0, 0] = af[0]
    for j in range(1, M + 1):
        E[0, j] = E[j, 0] = math.sqrt(2) * bf[j] / j
        E[j, j] = af[j] + bf[j] / j
    for i in range(1, M + 1):
        for j in range(1, M + 1):
            if i != j: E[i, j] = (bf[i] - bf[j]) / (i - j) + (bf[i] + bf[j]) / (i + j)
    return E

def lam_min(a, b):
    """certified lambda_min of the even block: double estimate -> shifted inverse iteration -> inertia bracket"""
    Ed = even_block_np(a, b)
    ld = np.linalg.eigvalsh(Ed)[0]
    if ld > -1e-10:
        sig = '0'   # (near-)PD: plain inverse iteration; certified bracket below decides
    else:
        sig = mp.nstr(mp.mpf(ld) - max(1e-3 * abs(ld), 1e-12), 20)
    lam, res, v = LA.eig_even(PREC, a, b, sig, 6, 40)
    mid = mp.mpf(lam.strip('[').split()[0])
    t = mp.mpf('1e-8')
    lo, hi = (mid * (1 - t), mid * (1 + t)) if mid > 0 else (mid * (1 + t), mid * (1 - t))
    br = LA.inertia(PREC, a, b, [mp.nstr(lo, 40), mp.nstr(hi, 40)])
    ok = br[0]['negE'] == 0 and br[0]['undE'] == 0 and br[1]['negE'] == 1 and br[1]['undE'] == 0
    return mid, ok

def form(L, N, keep):
    """(a,b) with pole + arch + the prime powers in keep (list of (k,p)), window L"""
    return AB.ab_total(L, N, keep, PREC)

L50 = arb(50).log()
pp = AB.von_mangoldt_table(49)
N = 60
lane = {1: (-1.373, 3), 2: (-1.693, 4), 5: (-1.149, 10), 9: (-1.122, 14), 13: (-1.074, 16), 19: (-0.923, 16),
        29: (-0.628, 14), 37: (-0.432, 10), 43: (-0.0699, 6), 47: (-5.66e-7, 3), 49: (1.75e-116, 0)}
print('# (1) fixed window L = log 50, N = 60: X, #pp, lambda_min (certified), neg even, neg odd')
negs = []
for idx in range(0, len(pp) + 1):
    keep = pp[:idx]
    Xc = keep[-1][0] if keep else 1
    a, b = form(L50, N, keep)
    inr = LA.inertia(PREC, a, b, ['0'])[0]
    lm, ok = lam_min(a, b)
    negs.append(inr['negE'])
    print(f'X={Xc:3d} #pp={idx:2d} lambda_min={mp.nstr(lm, 6):>14} certified={ok} negE={inr["negE"]} (undecided {inr["undE"]}) negO={inr["negO"]}', flush=True)
    if Xc in lane:
        lv, ln = lane[Xc]
        check(ok and inr['undE'] == 0 and inr['negE'] == ln and abs(lm - lv) <= 5e-3 * abs(lv), f'X={Xc}: lane A1 row (lambda_min {lv}, {ln} negative even) reproduced')
check(min(negs[:-1]) == 3 and max(negs[:-1]) == 16 and negs[-1] == 0, f'negative even counts before 49 enters range over [{min(negs[:-1])}, {max(negs[:-1])}]; 0 after')
# (2) Rayleigh decomposition at X = 49, N = 60 (= CCM x = 50, N = 60)
a, b = form(L50, N, pp)
lam, res, v = LA.eig_even(PREC, a, b, '0', 6, 400)
eps = mp.mpf(lam.strip('[').split()[0])
mp.mp.dps = 420
vv = [mp.mpf(t) for t in v]
def rq(a_, b_):
    M = len(a_) - 1
    A = [mp.mpf(t.mid().str(420, radius=False)) for t in a_]; B = [mp.mpf(t.mid().str(420, radius=False)) for t in b_]
    s = A[0] * vv[0] ** 2
    for j in range(1, M + 1):
        s += 2 * vv[0] * vv[j] * mp.sqrt(2) * B[j] / j + (A[j] + B[j] / j) * vv[j] ** 2
    for i in range(1, M + 1):
        for j in range(i + 1, M + 1):
            s += 2 * vv[i] * vv[j] * ((B[i] - B[j]) / (i - j) + (B[i] + B[j]) / (i + j))
    return s
P = AB.ab_parts(L50, N, [], PREC)
parts = {'pole': rq(*P['pole']), 'arch': rq(*P['arch'])}
contrib = {}
for (k, p) in pp:
    Pk = AB.ab_parts(L50, N, [(k, p)], PREC)
    contrib[k] = rq(*Pk['prime'])
tot = parts['pole'] + parts['arch'] + sum(contrib.values())
print(f'# (2) Rayleigh decomposition, L = log 50, N = 60: eps = {mp.nstr(eps, 6)}; pole {mp.nstr(parts["pole"], 6)}, arch {mp.nstr(parts["arch"], 6)}; sum of parts {mp.nstr(tot, 6)}')
print('   ' + ', '.join(f'{k}: {mp.nstr(contrib[k], 3)}' for k in contrib))
mn = min(abs(contrib[k]) for k in contrib)
print(f'   min_k |R_k| / eps = {mp.nstr(mn / eps, 4)} (k = {min(contrib, key=lambda k: abs(contrib[k]))})')
check(abs(tot - eps) < 1e-6 * eps, 'parts sum to eps (relative 1e-6)')
check(all(contrib[k] < 0 for k in contrib), 'every prime-power contribution negative at N = 60')
mp.mp.dps = 40
# (3) edge-effect tests
print('# (3a) all prime powers <= 47 (49 missing), L = log 50, as N grows')
allbut49 = pp[:-1]
for NN in (60, 90, 120, 160, 200, 240):
    a, b = form(L50, NN, allbut49)
    lm, ok = lam_min(a, b)
    inr = LA.inertia(PREC, a, b, ['0'])[0]
    print(f'   N={NN}: lambda_min = {mp.nstr(lm, 5)} certified={ok} negE={inr["negE"]}', flush=True)
print('# (3b) one prime power k removed (all others kept), L = log 50, N = 60')
for k in (2, 7, 23, 31, 43, 47, 49):
    keep = [t for t in pp if t[0] != k]
    a, b = form(L50, 60, keep)
    lm, ok = lam_min(a, b)
    wk = 1 - math.log(k) / math.log(50)
    print(f'   without k={k:2d} (a-weight 1 - log k/L = {wk:.4f}): lambda_min = {mp.nstr(lm, 5)} certified={ok}', flush=True)
print('# (3c) window L = log 53 (CCM form at x = 53, 53 enters with weight 0); remove 49 (a-weight 1 - log49/log53 = %.4f)' % (1 - math.log(49) / math.log(53)))
L53 = arb(53).log()
pp53 = AB.von_mangoldt_table(53)
for NN in (60, 120):
    a, b = form(L53, NN, pp53)
    lm_full, ok1 = lam_min(a, b)
    a, b = form(L53, NN, [t for t in pp53 if t[0] != 49])
    lm, ok = lam_min(a, b)
    print(f'   N={NN}: full lambda_min = {mp.nstr(lm_full, 4)} ({ok1}); without 49: {mp.nstr(lm, 5)} ({ok})', flush=True)
print('# (3d) operator norm (even block) of the single term W_49 at L = log 50, as N grows')
for NN in (60, 120, 240):
    Pk = AB.ab_parts(L50, NN, [(49, 7)], PREC)
    Ek = even_block_np(*Pk['prime'])
    print(f'   N={NN}: ||W_49||_even = {np.abs(np.linalg.eigvalsh(Ek)).max():.4g}')
print(f'# checks: {NCHK[0]} run, {NCHK[1]} failed')
