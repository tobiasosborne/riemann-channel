#!/usr/bin/env python3
"""lps_square_complex.py -- blind numerics lane for `notes/deninger-lps/astra-brief.md`.

Author line: claude:fable-5.1 (blind numerics fork).  Protocol: BLIND to
`notes/deninger-lps/astra-proofs.md` (not read).  Inputs: the brief and
`notes/deninger-lps/src/lps-deninger-worked-example.md` only.  Deterministic, no
randomness, no timestamps.  Every claim is a `check(cond, msg)`; a failing check is
recorded and the run continues; no tolerance was loosened to make a claim pass.

CONSTRUCTION (re-derived from the worked example, Sections 1-8)
  Quaternions a = (a0,a1,a2,a3) = a0 + a1 i + a2 j + a3 k, Hamilton multiplication.
  S_p = {N(a) = p, a0 > 0 odd, a1,a2,a3 even}; |S_13| = 14, |S_17| = 18.
  Vertices: PGL_2(F_5), a matrix mod scalars normalised so that the first nonzero
  entry (row-major) is 1; sorted lexicographically.  Since 2^2 = -1 mod 5,
      phi(a) = [[a0 + 2 a1, a2 + 2 a3], [-a2 + 2 a3, a0 - 2 a1]]  mod 5,
  det phi(a) = a0^2 + a1^2 + a2^2 + a3^2 = N(a) mod 5 (because -4 = 1 mod 5).
  Directed horizontal edge (g, a): g -> g phi(a), a in S_13; vertical (g, b), b in S_17.
  (g, a)^{-1} = (g phi(a), conj a).  Undirected edge = the pair; canonical representative
  = the directed member with the smaller (vertex index, generator index).
  Squares: for (a, b) in S_13 x S_17 the unique (b', a') with a b = +- b' a'; the square
  at g has boundary  e_h(g,a) + e_v(g phi(a), b) - e_h(g phi(b'), a') - e_v(g, b').
  Horizontal differential (D f)(g,a) = f(g phi(a)) - f(g); K = ker D^t (721-dim).
  Transport (T_1 w)(g,a) = sum_b w(g phi(b'), a'), the opposite edge in each square.
"""
import sys, time
import numpy as np
from itertools import product
from scipy.linalg import null_space

T0 = time.time()
LEDGER = []
def check(cond, msg):
    tag = "D%02d" % (len(LEDGER) + 1)
    LEDGER.append((tag, bool(cond), msg))
    print("%s %s %s" % (tag, "PASS" if cond else "FAIL", msg))
    return bool(cond)

# ---------------------------------------------------------------- quaternions
def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
            a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0)
def qconj(a): return (a[0], -a[1], -a[2], -a[3])
def qnorm(a): return sum(x*x for x in a)
def qnormalise_sign(a):
    """central sign: first nonzero coefficient positive"""
    for x in a:
        if x != 0:
            return a if x > 0 else tuple(-y for y in a)
    return a
def gens(p):
    r = int(p**0.5) + 1
    out = []
    for a0 in range(1, r + 1, 2):
        for a1, a2, a3 in product(range(-r, r + 1), repeat=3):
            if a1 % 2 or a2 % 2 or a3 % 2: continue
            if a0*a0 + a1*a1 + a2*a2 + a3*a3 == p: out.append((a0, a1, a2, a3))
    return sorted(out)
S13, S17 = gens(13), gens(17)
check(len(S13) == 14 and len(S17) == 18, "|S_13| = 14, |S_17| = 18 (got %d, %d)" % (len(S13), len(S17)))

# ---------------------------------------------------------------- PGL_2(F_5)
P = 5
def mnorm(m):
    m = tuple(x % P for x in m)
    for x in m:
        if x:
            inv = pow(x, P - 2, P)
            return tuple((y * inv) % P for y in m)
    raise ValueError
def mmul(m, n):
    return mnorm((m[0]*n[0] + m[1]*n[2], m[0]*n[1] + m[1]*n[3], m[2]*n[0] + m[3]*n[2], m[2]*n[1] + m[3]*n[3]))
VERTS = sorted({mnorm(m) for m in product(range(P), repeat=4) if (m[0]*m[3] - m[1]*m[2]) % P})
VIDX = {v: i for i, v in enumerate(VERTS)}
NV = len(VERTS)
check(NV == 120, "|PGL_2(F_5)| = 120 (got %d)" % NV)
def phi(a):
    a0, a1, a2, a3 = a
    return mnorm((a0 + 2*a1, a2 + 2*a3, -a2 + 2*a3, a0 - 2*a1))
hom_ok = all(phi(qmul(a, b)) == mmul(phi(a), phi(b)) for a in S13 + S17 for b in S13 + S17)
det_ok = all((phi(a)[0]*phi(a)[3] - phi(a)[1]*phi(a)[2]) % P != 0 for a in S13 + S17)
check(hom_ok and det_ok, "phi is a projective homomorphism on the generators, images invertible")
IDM = mnorm((1, 0, 0, 1))

# ---------------------------------------------------------------- graphs
def build_colour(S):
    """directed edges (v, s) -> v phi(s); returns head array, undirected id, sign, canonical list"""
    n = len(S)
    head = np.zeros((NV, n), dtype=int)
    for v in range(NV):
        for si, s in enumerate(S):
            head[v, si] = VIDX[mmul(VERTS[v], phi(s))]
    conj_idx = [S.index(qconj(s)) for s in S]
    und = -np.ones((NV, n), dtype=int); sgn = np.zeros((NV, n), dtype=int); canon = []
    for v in range(NV):
        for si in range(n):
            if und[v, si] >= 0: continue
            w, ti = head[v, si], conj_idx[si]
            assert head[w, ti] == v
            k = len(canon); canon.append((v, si))
            und[v, si], sgn[v, si] = k, 1
            und[w, ti], sgn[w, ti] = k, -1
    return head, und, sgn, canon, conj_idx
H13, U13, G13, C13, CJ13 = build_colour(S13)
H17, U17, G17, C17, CJ17 = build_colour(S17)
NE_H, NE_V = len(C13), len(C17)
check(NE_H == 840 and NE_V == 1080, "840 horizontal, 1080 vertical undirected edges (got %d, %d)" % (NE_H, NE_V))
def adjacency(head):
    A = np.zeros((NV, NV), dtype=int)
    for v in range(NV):
        for w in head[v]: A[v, w] += 1
    return A
A13, A17 = adjacency(H13), adjacency(H17)
def simple_ok(A, d):
    return (np.diag(A) == 0).all() and (A.max() == 1) and (A.sum(1) == d).all() and (A == A.T).all()
check(simple_ok(A13, 14) and simple_ok(A17, 18), "no loops, no repeated edges within a colour, regular of degree 14 / 18, symmetric")
def connected(A):
    seen = {0}; stack = [0]
    while stack:
        v = stack.pop()
        for w in np.nonzero(A[v])[0]:
            if w not in seen: seen.add(int(w)); stack.append(int(w))
    return len(seen) == NV
def bipartite_sign(A):
    col = -np.ones(NV, dtype=int); col[0] = 0; stack = [0]
    while stack:
        v = stack.pop()
        for w in np.nonzero(A[v])[0]:
            if col[w] < 0: col[w] = 1 - col[v]; stack.append(int(w))
            elif col[w] == col[v]: return None
    return 1 - 2*col
EPS13, EPS17 = bipartite_sign(A13), bipartite_sign(A17)
check(connected(A13) and connected(A17) and EPS13 is not None and EPS17 is not None and (EPS13 == EPS17).all(),
      "both colour graphs connected and bipartite with the same bipartition")
def spectrum(M, tol=1e-6):
    ev = np.linalg.eigvalsh(M.astype(float)); out = {}
    for x in ev:
        r = round(x)
        key = r if abs(x - r) < tol else round(x, 6)
        out[key] = out.get(key, 0) + 1
    return out
sp13, sp17 = spectrum(A13), spectrum(A17)
check(sp13 == {14: 1, -14: 1, 4: 34, -4: 34, 2: 25, -2: 25}, "spec A_13 = +-14 (1), +-4 (34), +-2 (25): %s" % sorted(sp13.items()))
check(sp17 == {18: 1, -18: 1, 6: 10, -6: 10, 5: 12, -5: 12, 3: 4, -3: 4, 2: 15, -2: 15, 0: 36},
      "spec A_17 = +-18 (1), +-6 (10), +-5 (12), +-3 (4), +-2 (15), 0 (36): %s" % sorted(sp17.items()))

# ---------------------------------------------------------------- reordering rules and squares
prod_ab = {}
for ai, a in enumerate(S13):
    for bi, b in enumerate(S17):
        prod_ab[(ai, bi)] = qnormalise_sign(qmul(a, b))
prod_ba = {}
for bi, b in enumerate(S17):
    for ai, a in enumerate(S13):
        prod_ba.setdefault(qnormalise_sign(qmul(b, a)), []).append((bi, ai))
RULE = {}
uniq = True
for key, val in prod_ab.items():
    lst = prod_ba.get(val, [])
    if len(lst) != 1: uniq = False
    else: RULE[key] = lst[0]          # (ai, bi) -> (b'i, a'i)
check(uniq and len(RULE) == 252 and len(set(prod_ab.values())) == 252,
      "252 reordering rules a b = +- b' a' exist and are unique; 252 distinct normalised products")
# check the rule is a bijection b -> b' for fixed a (used by T_1 D = D T_0)
check(all(len({RULE[(ai, bi)][0] for bi in range(18)}) == 18 for ai in range(14)), "for fixed a, b -> b' is a bijection of S_17")

def signed(und, sgn, v, si): return und[v, si], sgn[v, si]
sq_bd = {}   # frozenset of unsigned edge ids -> list of signed boundaries
sq_desc = []
for g in range(NV):
    for ai in range(14):
        for bi in range(18):
            bpi, api = RULE[(ai, bi)]
            ga, gb = H13[g, ai], H17[g, bpi]
            e1 = signed(U13, G13, g, ai)                       # e_h(g, a)
            e2 = (NE_H + U17[ga, bi], G17[ga, bi])            # e_v(g phi(a), b)
            e3 = signed(U13, G13, gb, api)                    # e_h(g phi(b'), a')
            e4 = (NE_H + U17[g, bpi], G17[g, bpi])           # e_v(g, b')
            # endpoint identity: head of e2 == head of e3
            assert H17[ga, bi] == H13[gb, api], "square does not close"
            bd = {e1[0]: e1[1], e2[0]: e2[1]}
            bd[e3[0]] = bd.get(e3[0], 0) - e3[1]
            bd[e4[0]] = bd.get(e4[0], 0) - e4[1]
            key = frozenset(bd.keys())
            sq_bd.setdefault(key, []).append(tuple(sorted(bd.items())))
            sq_desc.append((g, ai, bi))
four_ok = all(len(v) == 4 for v in sq_bd.values())
same_ok = True
for v in sq_bd.values():
    ref = dict(v[0])
    for other in v[1:]:
        o = dict(other)
        if not (all(o[k] == ref[k] for k in ref) or all(o[k] == -ref[k] for k in ref)): same_ok = False
check(len(sq_bd) == 7560 and four_ok and same_ok, "7560 squares, each with exactly 4 corner representatives agreeing up to sign (got %d)" % len(sq_bd))
SQUARES = [dict(v[0]) for v in sq_bd.values()]
NE = NE_H + NE_V
B1 = np.zeros((NV, NE), dtype=np.int64)
for k, (v, si) in enumerate(C13): B1[v, k] -= 1; B1[H13[v, si], k] += 1
for k, (v, si) in enumerate(C17): B1[v, NE_H + k] -= 1; B1[H17[v, si], NE_H + k] += 1
B2 = np.zeros((NE, len(SQUARES)), dtype=np.int64)
for c, bd in enumerate(SQUARES):
    for e, s in bd.items(): B2[e, c] = s
check(not (B1 @ B2).any(), "B_1 B_2 = 0 exactly")
check((np.abs(B2).sum(0) == 4).all(), "every face column has exactly four nonzero entries +-1")

def rank_mod_p(A, p):
    A = (A % p).astype(np.int64).copy(); rows, cols = A.shape; r = 0
    for c in range(cols):
        nz = np.nonzero(A[r:, c])[0]
        if len(nz) == 0: continue
        piv = r + nz[0]
        if piv != r: A[[r, piv]] = A[[piv, r]]
        A[r] = (A[r] * pow(int(A[r, c]), p - 2, p)) % p
        below = r + 1 + np.nonzero(A[r + 1:, c])[0]
        if len(below): A[below] = (A[below] - np.outer(A[below, c], A[r])) % p
        r += 1
        if r == rows: break
    return r
rB1 = rank_mod_p(B1, 101)
gram = (B2 @ B2.T)   # 1920 x 1920; rank_p(B2 B2^t) <= rank_p(B2) <= rank_Q(B2) <= 1920 - 119
rGram = rank_mod_p(gram, 101)
check(rB1 == 119, "rank B_1 = 119 (mod 101, = rank over Q since rows sum to zero): %d" % rB1)
check(rGram == 1801, "rank B_2 = 1801: rank_101(B_2 B_2^t) = %d <= rank_101(B_2) <= rank_Q(B_2) <= 1920 - 119" % rGram)
b0, b1, b2 = NV - rB1, NE - rB1 - 1801, 7560 - 1801
check((b0, b1, b2) == (1, 0, 5759), "Betti numbers (1, 0, 5759): (%d, %d, %d)" % (b0, b1, b2))

# ---------------------------------------------------------------- horizontal differential, K, T_1
D = np.zeros((NE_H, NV), dtype=np.int64)     # (Df)(e) = f(head) - f(tail) on canonical directed reps
for k, (v, si) in enumerate(C13): D[k, v] -= 1; D[k, H13[v, si]] += 1
Vk = null_space(D.T.astype(float))            # 840 x dim K, orthonormal
check(Vk.shape[1] == 721, "dim K = dim ker D^t = 721 (got %d)" % Vk.shape[1])
# T_1 on antisymmetric fields (undirected coordinates, value at canonical orientation)
T1 = np.zeros((NE_H, NE_H), dtype=np.int64)
for k, (g, ai) in enumerate(C13):
    for bi in range(18):
        bpi, api = RULE[(ai, bi)]
        gb = H17[g, bpi]
        T1[k, U13[gb, api]] += G13[gb, api]
check((T1 == T1.T).all(), "T_1 is symmetric")
check(not (T1 @ D - D @ A17).any(), "T_1 D = D T_0 with T_0 = A_17, exactly")
check(np.abs(D.T @ (T1 @ Vk)).max() < 1e-9, "K = ker D^t is T_1-invariant (|D^t T_1 V| < 1e-9)")
M = Vk.T @ T1 @ Vk                            # T = T_1|_K in an orthonormal basis of K
M = (M + M.T) / 2
evK = np.linalg.eigvalsh(M)
check(np.abs(evK).max() < 8, "all eigenvalues of T lie in (-8, 8): max |lambda| = %.6f < 8 < 2 sqrt17 = %.6f" % (np.abs(evK).max(), 2*17**0.5))

# ---------------------------------------------------------------- directed-edge version, old/new, reversal
ND = NV * 14
def didx(v, si): return v * 14 + si
TD = np.zeros((ND, ND), dtype=np.int64)
for g in range(NV):
    for ai in range(14):
        for bi in range(18):
            bpi, api = RULE[(ai, bi)]
            TD[didx(g, ai), didx(H17[g, bpi], api)] += 1
R = np.zeros((ND, ND), dtype=np.int64)
for g in range(NV):
    for ai in range(14): R[didx(g, ai), didx(H13[g, ai], CJ13[ai])] = 1
check((TD == TD.T).all() and (R @ R == np.eye(ND, dtype=np.int64)).all(), "directed T_1 symmetric; reversal is an involution")
check(not (TD @ R - R @ TD).any(), "directed T_1 commutes with the edge reversal")
OLD = np.zeros((ND, 2 * NV), dtype=np.int64)
for g in range(NV):
    for ai in range(14):
        OLD[didx(g, ai), g] = 1                    # f(tail)
        OLD[didx(g, ai), NV + H13[g, ai]] = 1      # f(head)
rOld = np.linalg.matrix_rank(OLD.astype(float))
check(rOld == 238, "old space (tail and head pull-backs of vertex functions) has dimension 238 (got %d); new = %d" % (rOld, ND - rOld))
NEW = null_space(OLD.T.astype(float))
check(NEW.shape[1] == 1442 and np.abs(OLD.T @ (TD @ NEW)).max() < 1e-9, "new space is 1442-dimensional and T_1-invariant")
Rn = NEW.T @ R @ NEW
wR, VR = np.linalg.eigh((Rn + Rn.T) / 2)
plus, minus = VR[:, wR > 0], VR[:, wR < 0]
check(plus.shape[1] == 721 and minus.shape[1] == 721, "reversal splits new = 721 (+1) + 721 (-1) (got %d, %d)" % (plus.shape[1], minus.shape[1]))
Tn = NEW.T @ TD @ NEW
ev_plus = np.linalg.eigvalsh(plus.T @ Tn @ plus); ev_minus = np.linalg.eigvalsh(minus.T @ Tn @ minus)
dev_pm = np.abs(np.sort(ev_plus) - np.sort(ev_minus)).max(); dev_mK = np.abs(np.sort(ev_minus) - np.sort(evK)).max(); dev_pK = np.abs(np.sort(ev_plus) - np.sort(evK)).max()
check(dev_pm < 1e-8, "T_1 has the same spectrum on the two reversal sectors of new (max dev %.2e)" % dev_pm)
check(dev_mK < 1e-8, "the (-1) reversal sector of new has spectrum spec(T on K): dev %.2e (dev of the (+1) sector %.2e)" % (dev_mK, dev_pK))
dev_neg = np.abs(np.sort(ev_plus) - np.sort(-evK)).max()
check(dev_neg < 1e-8, "the (+1) sector has the NEGATED spectrum -spec(T on K) (bipartite twist: the transport crosses one 17-edge): dev %.2e" % dev_neg)
print("   first 5 eigenvalues: +1 sector %s ; -1 sector %s ; K %s" % (np.round(np.sort(ev_plus)[:5], 4), np.round(np.sort(ev_minus)[:5], 4), np.round(np.sort(evK)[:5], 4)))
print("   traces: +1 sector %.6f, -1 sector %.6f, K %.6f" % (ev_plus.sum(), ev_minus.sum(), evK.sum()))

# ---------------------------------------------------------------- Hecke relation at 17^2
def gens_norm(n):
    r = int(n**0.5) + 1; out = []
    for a0 in range(1, r + 1, 2):
        for a1, a2, a3 in product(range(-r, r + 1), repeat=3):
            if a1 % 2 or a2 % 2 or a3 % 2: continue
            if a0*a0 + a1*a1 + a2*a2 + a3*a3 == n: out.append((a0, a1, a2, a3))
    return sorted(out)
S289 = gens_norm(289)
check(len(S289) == 307, "307 = 17^2 + 17 + 1 normalised quaternions of norm 289 (a0 > 0 odd, others even), including 17*1: got %d" % len(S289))
check((17, 0, 0, 0) in S289 and phi((17, 0, 0, 0)) == IDM, "17*1 is among them and phi(17) = identity projectively")
A289 = np.zeros((NV, NV), dtype=np.int64)
for c in S289:
    for v in range(NV): A289[v, VIDX[mmul(VERTS[v], phi(c))]] += 1
check(not (A17 @ A17 - 17 * np.eye(NV, dtype=np.int64) - A289).any(), "Hecke relation T_17^2 - 17 I = T_289 on vertex functions (all 307 elements)")
# products b1 b2 of generators: reduced words (b2 != conj b1) give the 306 primitive elements
prods = {}
for b1 in S17:
    for b2 in S17:
        if b2 == qconj(b1): continue
        prods.setdefault(qnormalise_sign(qmul(b1, b2)), []).append((b1, b2))
check(len(prods) == 306 and all(len(v) == 1 for v in prods.values()) and set(prods) | {(17, 0, 0, 0)} == set(S289),
      "the 306 reduced words b1 b2 are exactly the primitive norm-289 elements, each once")
# edge version: double transport over reduced words, plus identity
T289E = np.zeros((NE_H, NE_H), dtype=np.int64)
for k, (g, ai) in enumerate(C13):
    for b1i in range(18):
        bp1, ap1 = RULE[(ai, b1i)]; g1 = H17[g, bp1]
        for b2i in range(18):
            if b2i == CJ17[b1i]: continue
            bp2, ap2 = RULE[(ap1, b2i)]; g2 = H17[g1, bp2]
            T289E[k, U13[g2, ap2]] += G13[g2, ap2]
T289E += np.eye(NE_H, dtype=np.int64)
check(not (T1 @ T1 - 17 * np.eye(NE_H, dtype=np.int64) - T289E).any(),
      "edge version: T_1^2 - 17 I = (double transport over reduced words) + I, exactly, on all antisymmetric fields (hence on K)")

# ---------------------------------------------------------------- chi_T against the worked example
FACTORS = [([1, -7], 4), ([1, 7], 4), ([1, -4, -43, 188], 6), ([1, 1], 8), ([1, 3, -6], 8), ([1, 3], 6),
           ([1, -2, -36, -24], 10), ([1, 1, -18], 12), ([1, 2, -39], 12), ([1, -10, 20, 8], 12),
           ([1, -3, -31, 103, 2], 12), ([1, 4, -20], 15), ([1, 0, -12], 15), ([1, -8, 4], 15), ([1, -4, -4], 15),
           ([1, -4], 18), ([1, 1, -38], 18), ([1, 6, -4, -40], 18), ([1, 6, -15, -58, 140, -72], 18),
           ([1, 5], 12), ([1, -6], 15), ([1, 6], 17), ([1, -2], 20), ([1, -3], 44), ([1, 2], 77)]
claimed = []
for coeffs, m in FACTORS:
    for r in np.roots(coeffs): claimed += [r.real] * m
claimed = np.sort(np.array(claimed))
check(len(claimed) == 721, "Section 13 table: sum of m deg f = 721 (got %d)" % len(claimed))
check(np.abs(claimed - np.sort(evK)).max() < 1e-6, "spec(T on K) equals the roots of the Section 13 factor table with multiplicities (max dev %.2e)" % np.abs(claimed - np.sort(evK)).max())
def imult(ev, x, tol=1e-6): return int((np.abs(ev - x) < tol).sum())
table = {-2: 77, 3: 44, 2: 20, 7: 4, -7: 4, 4: 18, -6: 17, 6: 15, -5: 12, -1: 8, -3: 6}   # x+5 | 12 in the table: eigenvalue -5
got = {x: imult(evK, x) for x in table}
check(got == table, "integer eigenvalue multiplicities of T: %s" % sorted(got.items()))
allT1 = np.sort(np.linalg.eigvalsh(T1.astype(float)))
ev17 = np.sort(np.linalg.eigvalsh(A17.astype(float)))
ev17_no18 = ev17[np.abs(ev17 - 18) > 1e-6]
combined = np.sort(np.concatenate([evK, ev17_no18]))
check(len(ev17_no18) == 119 and np.abs(combined - allT1).max() < 1e-6,
      "chi_T = chi_{T_1} (x - 18) / chi_{A_17} as multisets of eigenvalues (max dev %.2e)" % np.abs(combined - allT1).max())
check(abs(np.trace(M) - 18) < 1e-9 and np.trace(T1) == 0, "Tr T = 18, Tr T_1 = 0")

# ---------------------------------------------------------------- Bass doubling
n = M.shape[0]; I = np.eye(n)
F1 = np.block([[M, -17 * I], [I, np.zeros((n, n))]])
Om = np.block([[np.zeros((n, n)), I], [-I, np.zeros((n, n))]])
G = np.block([[I, -M / 2], [-M / 2, 17 * I]])
check(np.abs(F1.T @ Om @ F1 - 17 * Om).max() < 1e-9, "F_1^t Omega F_1 = 17 Omega")
check(np.abs(F1.T @ G @ F1 - 17 * G).max() < 1e-9, "F_1^t G F_1 = 17 G")
gmin = np.linalg.eigvalsh(G).min()
check(gmin > 0, "G > 0: smallest eigenvalue %.6f (Schur complement 17 - lambda^2/4 >= %.6f)" % (gmin, 17 - np.abs(evK).max()**2 / 4))
evF = np.linalg.eigvals(F1)
check(np.abs(np.abs(evF) - 17**0.5).max() < 1e-8, "all eigenvalues of F_1 have modulus sqrt(17): max deviation %.2e" % np.abs(np.abs(evF) - 17**0.5).max())
# N_n = 1 + 17^n - Tr F_1^n via the Chebyshev-type recurrence on the eigenvalues of T
p_prev, p_cur = 2 * np.ones(n), evK.copy(); Ns = []
for k in range(1, 7):
    trF = p_cur.sum() if k >= 1 else None
    Ns.append(int(round(1 + 17**k - trF)))
    p_prev, p_cur = p_cur, evK * p_cur - 17 * p_prev
check(Ns == [0, 11520, 10080, 126720, 1209600, 23886720], "N_n = 1 + 17^n - Tr F_1^n, n = 1..6: %s" % Ns)

# ---------------------------------------------------------------- representation decomposition
# left action of PGL_2(F_5): (L_h f)(g) = f(h^{-1} g); permutation matrices on vertices and (signed) on edges
def inv2(m):
    a, b, c, d = m
    return mnorm((d, -b, -c, a))
def left_perm_vertices(h):
    hinv = inv2(h)
    return np.array([VIDX[mmul(hinv, VERTS[g])] for g in range(NV)])   # perm[g] = h^{-1} g
def left_edges(h):
    """signed permutation on canonical horizontal edges: (L_h w)(g,a) = w(h^{-1} g, a)"""
    hinv = inv2(h); L = np.zeros((NE_H, NE_H))
    for k, (g, ai) in enumerate(C13):
        g2 = VIDX[mmul(hinv, VERTS[g])]
        L[k, U13[g2, ai]] = G13[g2, ai]
    return L
# conjugacy classes
def conj_classes():
    seen, classes = set(), []
    for g in VERTS:
        if g in seen: continue
        cl = {mmul(mmul(h, g), inv2(h)) for h in VERTS}
        seen |= cl; classes.append(sorted(cl))
    return classes
CLS = conj_classes()
NC = len(CLS)
check(NC == 7, "PGL_2(F_5) has 7 conjugacy classes (got %d): sizes %s" % (NC, [len(c) for c in CLS]))
# Burnside--Dixon: class multiplication constants, simultaneous eigenvectors -> irreducible characters
cls_of = {}
for i, c in enumerate(CLS):
    for g in c: cls_of[g] = i
Mc = np.zeros((NC, NC, NC))
for i in range(NC):
    for j in range(NC):
        cnt = np.zeros(NC)
        for x in CLS[i]:
            for y in CLS[j]: cnt[cls_of[mmul(x, y)]] += 1
        Mc[i, j, :] = cnt
# c_{ijk} = coefficient of K_k in K_i K_j ; M_i[j,k] = c_{ijk}; the class sums K_j -> omega_chi(K_j) give a common eigenvector
Cm = np.zeros((NC, NC, NC))
for i in range(NC):
    for j in range(NC):
        for k in range(NC): Cm[i, j, k] = Mc[i, j, k] / len(CLS[k])
WTS = [1.0, 3**0.5, 5**0.5, 7**0.5, 11**0.5, 13**0.5, 17**0.5]   # generic weights: no eigenvalue collisions
comb = sum(WTS[i] * Cm[i] for i in range(NC))      # M_i omega = omega(K_i) omega: eigenvectors are the omega_chi
w, U = np.linalg.eig(comb)
IRR = []
sizes = np.array([len(c) for c in CLS])
for col in range(NC):
    vec = U[:, col]; vec = vec / vec[cls_of[IDM]]       # omega(identity class) = 1
    om = vec.real if np.abs(vec.imag).max() < 1e-8 else vec
    d2 = 120.0 / np.sum(np.abs(om)**2 / sizes)
    d = round(d2**0.5)
    chi = d * om / sizes
    IRR.append((d, chi))
IRR.sort(key=lambda t: (t[0], tuple(np.round(t[1].real, 6))))
dims = sorted(d for d, _ in IRR)
check(dims == [1, 1, 4, 4, 5, 5, 6] and sum(d*d for d in dims) == 120, "irreducible dimensions of PGL_2(F_5) = [1, 1, 4, 4, 5, 5, 6] (sum of squares 120): %s" % dims)
# character orthonormality check
ortho_ok = all(abs(np.sum(sizes * IRR[a][1] * np.conj(IRR[b][1])) / 120 - (1 if a == b else 0)) < 1e-8 for a in range(NC) for b in range(NC))
check(ortho_ok, "computed irreducible characters are orthonormal")
REPS = [c[0] for c in CLS]
LV = [left_perm_vertices(h) for h in REPS]
LE = [left_edges(h) for h in REPS]
def decompose(charV):
    out = []
    for d, chi in IRR:
        m = np.sum(sizes * charV * np.conj(chi)) / 120
        mr = int(round(m.real))
        if abs(m - mr) > 1e-6: DEC_OK[0] = False; out.append((d, float(np.round(m.real, 4))))
        elif mr: out.append((d, mr))
    return out
DEC_OK = [True]
print("\nRepresentation content of the A_17 eigenspaces on vertex functions (irrep dim, multiplicity):")
wV, UV = np.linalg.eigh(A17.astype(float))
vertex_dec = {}
for lam in sorted(set(np.round(wV, 6))):
    cols = UV[:, np.abs(wV - lam) < 1e-6]
    charV = np.array([np.trace(cols.T @ cols[LV[i], :]) for i in range(NC)])   # Tr(P L_h): (L_h f)(g) = f(h^-1 g)
    vertex_dec[lam] = decompose(charV)
    print("  lambda = %6.2f  mult %3d  ->  %s" % (lam, cols.shape[1], vertex_dec[lam]))
print("\nRepresentation content of the T eigenspaces on K (irrep dim, multiplicity):")
wK, UK = np.linalg.eigh(M)
K_dec = {}
for lam in sorted(set(np.round(wK, 6))):
    colsK = UK[:, np.abs(wK - lam) < 1e-6]
    cols = Vk @ colsK                        # 840 x m, orthonormal in edge coordinates
    charV = np.array([np.trace(cols.T @ (LE[i] @ cols)) for i in range(NC)])
    K_dec[lam] = decompose(charV)
    print("  lambda = %10.6f  mult %3d  ->  %s" % (lam, cols.shape[1], K_dec[lam]))
check(DEC_OK[0], "all multiplicities in the decompositions are integers")
iso_ok = all(all(isinstance(m, int) and m % d == 0 for d, m in dec) for dec in list(vertex_dec.values()) + list(K_dec.values()))
check(iso_ok, "every irreducible appears in every Hecke eigenspace with multiplicity a multiple of its dimension (isotypic blocks)")
check(all(sum(d * m for d, m in dec) == imult(wK, lam) for lam, dec in K_dec.items()), "K-eigenspace dimensions equal sum of (dim x multiplicity)")

# ---------------------------------------------------------------- summary
npass = sum(1 for _, ok, _ in LEDGER if ok)
print("\n%d checks, %d pass, %d fail; runtime %.1f s" % (len(LEDGER), npass, len(LEDGER) - npass, time.time() - T0))
