#!/usr/bin/env python3
"""T4 of notes/astra-2026-10-27/tree-codes/lane-brief.md  (claude:fable-5.1, 2026-10-27).

(c) Honest Gamma \\ T_5: the LPS graphs X^{5,q} (Lubotzky-Phillips-Sarnak 1988, from memory): Cayley graph of PSL_2(F_q)
    ((5/q) = 1, non-bipartite) or PGL_2(F_q) ((5/q) = -1, bipartite) on the six quaternions 1 +- 2i, 1 +- 2j, 1 +- 2k of
    norm 5, through a splitting H(F_q) = M_2(F_q).  It is Gamma \\ T_5 for the arithmetic lattice Gamma = Lambda(2q) of the
    Hamilton quaternions (LPS).  q = 11 (660 vertices), q = 13 (2184), q = 29 (12180, with --big).
    (i)   N_k = Tr B^k for k <= KMAX by enumerating cyclically reduced words in the generators with product 1 (the
          left-regular action is simply transitive on vertices, so every closed tailless NB walk is |G| x a word); for
          q = 11 also by dense powers of the Hashimoto matrix B as an independent route.
    (ii)  N_k from Ihara-Bass through the adjacency spectrum, and the primitive cycle counts pi(l) by Moebius inversion.
    (iii) the explicit formula: sum over non-trivial lines of w^k  =  q^{-k/2} sum_{l | k} l pi(l)  -  n(q-1) q^{-k/2} [k even]
          - (trivial pairs), to machine precision.
(a)/(b) the elements gamma in Gamma of the closed walks: the quaternion product of the word, as a 5-adic matrix; its
    translation length ell(gamma) = v_5(det) - 2 v_5(tr) equals the walk length for tailless walks and is smaller for walks
    with a tail; the eigenvalue ratio lambda(gamma) has v_5 = ell, so |lambda|^{1/2}/|1 - lambda| = 5^{-ell/2}.
(b) the cutoff trace Tr(P_n D_a P_n) on the GKP code C_n of the lattice p^n Z_p^2 (functions on p^{-n}Z_p / p^n Z_p),
    computed exactly, against the Lefschetz number |a|^{1/2} / |1 - a|.
Run: python3 checks/ihara_lefschetz.py [--big]
"""
import sys, itertools, time
import numpy as np
from fractions import Fraction as Fr

P = 5
KMAX = 8
BIG = "--big" in sys.argv

# ---------------------------------------------------------------- quaternions and the splitting
def qmul(x, y):
    a1, b1, c1, d1 = x; a2, b2, c2, d2 = y
    return (a1*a2 - b1*b2 - c1*c2 - d1*d2,
            a1*b2 + b1*a2 + c1*d2 - d1*c2,
            a1*c2 - b1*d2 + c1*a2 + d1*b2,
            a1*d2 + b1*c2 - c1*b2 + d1*a2)

GENS = [(1, 2, 0, 0), (1, -2, 0, 0), (1, 0, 2, 0), (1, 0, -2, 0), (1, 0, 0, 2), (1, 0, 0, -2)]
INV = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}          # conjugate = inverse in PGL_2

def splitting(q):
    """x, y with x^2 + y^2 = -1 mod q; I = [[0,1],[-1,0]], J = [[x,y],[y,-x]], K = IJ."""
    for x in range(q):
        for y in range(q):
            if (x*x + y*y + 1) % q == 0:
                return x, y
    raise ValueError

def to_mat(quat, q, xy):
    a, b, c, d = quat; x, y = xy
    I = ((0, 1), (-1, 0)); Jm = ((x, y), (y, -x))
    K = ((I[0][0]*Jm[0][0] + I[0][1]*Jm[1][0], I[0][0]*Jm[0][1] + I[0][1]*Jm[1][1]),
         (I[1][0]*Jm[0][0] + I[1][1]*Jm[1][0], I[1][0]*Jm[0][1] + I[1][1]*Jm[1][1]))
    m = [[a, 0], [0, a]]
    for coef, B in ((b, I), (c, Jm), (d, K)):
        for i in range(2):
            for j in range(2):
                m[i][j] += coef*B[i][j]
    return tuple(tuple(v % q for v in row) for row in m)

def canon(m, q):
    """representative of m in PGL_2(F_q): scale so the first nonzero entry is 1."""
    flat = [m[0][0], m[0][1], m[1][0], m[1][1]]
    for v in flat:
        if v % q:
            s = pow(v, -1, q)
            return tuple(tuple((e*s) % q for e in row) for row in m)
    raise ValueError

def mmul(a, b, q):
    return (((a[0][0]*b[0][0] + a[0][1]*b[1][0]) % q, (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % q),
            ((a[1][0]*b[0][0] + a[1][1]*b[1][0]) % q, (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % q))

def lps_graph(q):
    xy = splitting(q)
    gens = [canon(to_mat(g, q, xy), q) for g in GENS]
    assert len(set(gens)) == 6, "generators not distinct mod scalars"
    one = canon(((1, 0), (0, 1)), q)
    assert one not in gens
    # BFS
    index = {one: 0}; order = [one]; adj = []
    i = 0
    while i < len(order):
        g = order[i]; row = []
        for s in gens:
            h = canon(mmul(g, s, q), q)
            if h not in index:
                index[h] = len(order); order.append(h)
            row.append(index[h])
        adj.append(row); i += 1
    n = len(order)
    A = np.zeros((n, n))
    for g, row in enumerate(adj):
        for h in row:
            A[g, h] += 1
    assert np.allclose(A, A.T) and np.allclose(A.sum(1), 6) and A.max() == 1
    return n, A, adj, gens

def legendre(a, q):
    return pow(a % q, (q - 1)//2, q)

# ---------------------------------------------------------------- closed walks by words
def closed_word_counts(adj, kmax):
    """number of cyclically reduced words s_1..s_k (s_{i+1} != s_i^{-1}, s_1 != s_k^{-1}) with product = 1 at vertex 0,
    and the words themselves; also the count of reduced-but-tailed closed words."""
    counts = {}; tailed = {}; words = {}
    for k in range(1, kmax + 1):
        c = 0; ct = 0; ws = []
        # DFS over reduced words from vertex 0
        stack = [(0, [], None)]
        while stack:
            v, w, last = stack.pop()
            if len(w) == k:
                if v == 0:
                    if INV[w[0]] != w[-1]:
                        c += 1; ws.append(tuple(w))
                    else:
                        ct += 1
                continue
            for s in range(6):
                if last is not None and s == INV[last]:
                    continue
                stack.append((adj[v][s], w + [s], s))
        counts[k] = c; tailed[k] = ct; words[k] = ws
    return counts, tailed, words

def moebius(n):
    r, m = 1, n; d = 2
    while d*d <= m:
        if m % d == 0:
            m //= d
            if m % d == 0:
                return 0
            r = -r
        d += 1
    if m > 1:
        r = -r
    return r

# ---------------------------------------------------------------- 5-adic data of gamma
def vp_int(x, p):
    if x == 0:
        return 10**9
    v = 0
    while x % p == 0:
        x //= p; v += 1
    return v

def word_quaternion(w):
    qt = (1, 0, 0, 0)
    for s in w:
        qt = qmul(qt, GENS[s])
    return qt

def hensel_sqrt_minus1(p, N):
    x = 2 if p == 5 else None
    M = p**N
    for _ in range(N + 2):
        x = (x - (x*x + 1)*pow(2*x, -1, M)) % M
    assert (x*x + 1) % M == 0
    return x

# ---------------------------------------------------------------- cutoff trace of D_a on the code of p^n Z_p^2
def cutoff_trace(a_num, a_den, p, n):
    """Tr(P_n D_a P_n), a = a_num/a_den in Q_p^x, P_n = projector on functions supported in p^{-n}Z_p constant mod p^n Z_p.
    <e_c, D_a e_c> = p^n |a|^{1/2} vol((c + p^n Z_p) cap a^{-1}(c + p^n Z_p)); exact, with cosets c = C/p^n, C mod p^{2n}."""
    va = vp_int(a_num, p) - vp_int(a_den, p)          # a = p^va u
    u_num = a_num // p**vp_int(a_num, p); u_den = a_den // p**vp_int(a_den, p)
    Nprec = 6*n + 2*abs(va) + 10
    M = p**Nprec
    uinv = (u_den * pow(u_num, -1, M)) % M            # u^{-1} mod p^Nprec
    total = Fr(0)
    for C in range(p**(2*n)):                          # c = C p^{-n}
        # a^{-1} c = p^{-va} u^{-1} C p^{-n};  the ball a^{-1}(c + p^n Z_p) = a^{-1}c + p^{n - va} Z_p
        # intersect with c + p^n Z_p: compare c - a^{-1}c = C p^{-n} (1 - p^{-va} u^{-1}) at valuation >= min(n, n - va)
        # write everything times p^{n + max(va,0)} to make it integral
        sh = n + max(va, 0)
        diff = (C * p**(sh - n) * (p**max(va, 0) - p**(max(va, 0) - va) * uinv)) % (M)   # = p^{sh} (c - a^{-1} c) mod p^Nprec, as integer
        # need v(c - a^{-1}c) >= n - min(va, 0)  (the smaller ball's radius): i.e. v(diff) - sh >= n - min(va,0)
        vdiff = vp_int(diff, p) if diff else 10**9
        if vdiff - sh >= n - min(va, 0):
            vol = Fr(1, p**(n - min(va, 0)))           # volume of the smaller ball
            total += p**n * vol
        # |a|^{1/2} factor
    return total * Fr(1, 1), va

if __name__ == "__main__":
    t0 = time.time()
    print("== T4(c)  LPS graphs X^{5,q}: walk counts, Ihara-Bass, explicit formula")
    qs = [11, 13] + ([29] if BIG else [])
    for q in qs:
        n, A, adj, gens = lps_graph(q)
        bip = legendre(P, q) != 1
        print(f"\n-- q = {q}: (5/q) = {'-1' if bip else '+1'} -> {'PGL' if bip else 'PSL'}_2(F_{q}), n = {n} vertices, "
              f"6-regular simple graph: True, bipartite expected: {bip}")
        ev = np.linalg.eigvalsh(A)
        ev_sorted = np.sort(ev)[::-1]
        nontriv = ev_sorted[1:-1] if bip else ev_sorted[1:]
        print(f"   eigenvalues: max = {ev_sorted[0]:.6f}, min = {ev_sorted[-1]:.6f}, largest nontrivial |lambda| = {np.abs(nontriv).max():.6f}, "
              f"2 sqrt(5) = {2*np.sqrt(5):.6f}, Ramanujan: {np.abs(nontriv).max() <= 2*np.sqrt(5) + 1e-9}")
        counts, tailed, words = closed_word_counts(adj, KMAX)
        Nk_words = {k: n*counts[k] for k in counts}
        # (ii) Ihara-Bass: N_k = n (q-1)[k even] + sum_lambda (mu^k + mubar^k), mu + mubar = lambda, mu mubar = p
        Nk_IB = {}
        for k in range(1, KMAX + 1):
            s = 0
            for lam in ev:
                disc = lam*lam - 4*P
                sq = np.sqrt(complex(disc))
                mu1, mu2 = (lam + sq)/2, (lam - sq)/2
                s += (mu1**k + mu2**k).real
            Nk_IB[k] = s + n*(P - 1)*(1 if k % 2 == 0 else 0)
        print("   k   N_k (words)   N_k (Ihara-Bass)   diff      tailed closed reduced words   pi(k) primitive classes")
        pi = {}
        for k in range(1, KMAX + 1):
            pi[k] = sum(moebius(k//d) * Nk_words[d] for d in range(1, k + 1) if k % d == 0) // k
            print(f"   {k}   {Nk_words[k]:10d}   {Nk_IB[k]:16.6f}   {Nk_words[k]-Nk_IB[k]:+.2e}   {n*tailed[k]:8d}   {pi[k]:8d}")
        # (iii) explicit formula with orbit weights
        maxdiff = 0
        for k in range(1, KMAX + 1):
            lhs = 0
            for lam in nontriv:
                w = np.roots([1, -lam/np.sqrt(P), 1])
                lhs += (w[0]**k + w[1]**k).real
            orbit = sum(l*pi[l] for l in range(1, k + 1) if k % l == 0) * P**(-k/2)
            tree = n*(P - 1)*P**(-k/2)*(1 if k % 2 == 0 else 0)
            trivial = P**(k/2) + P**(-k/2)
            if bip:
                trivial += (-1)**k * (P**(k/2) + P**(-k/2))
            rhs = orbit - tree - trivial
            maxdiff = max(maxdiff, abs(lhs - rhs))
        print(f"   explicit formula  sum_nontrivial w^k = q^(-k/2) sum_(l|k) l pi(l) - n(q-1)q^(-k/2)[k even] - trivial pair(s): "
              f"max |lhs - rhs| over k<=8 = {maxdiff:.2e}")
        # (a)/(b): the elements gamma of the closed walks
        if q == 11:
            N5 = 60
            i5 = hensel_sqrt_minus1(P, N5)
            M5 = P**N5
            print("   elements gamma of Gamma (quaternion products of the words), 5-adic translation length ell = v(det) - 2 v(tr):")
            okall = True
            for k in range(1, KMAX + 1):
                ells = []
                for w in words[k][:2000]:
                    qt = word_quaternion(w)
                    a, b, c, d = qt
                    nrm = a*a + b*b + c*c + d*d
                    assert nrm == P**k
                    ell = vp_int(nrm, P) - 2*vp_int(2*a, P)
                    ells.append(ell)
                okk = all(e == k for e in ells)
                okall &= okk
                ex = ""
                if words[k]:
                    w = words[k][0]; a, b, c, d = word_quaternion(w)
                    # eigenvalue ratio lambda = lam2/lam1 of gamma = [[a+bi, c+di],[-c+di, a-bi]]: v(lam) = ell
                    ex = f"   example word {w}: quaternion {(a,b,c,d)}, tr = {2*a}, det = 5^{k}, v_5(tr) = {vp_int(2*a,P)}, ell = {k - 2*vp_int(2*a,P)}, weight 5^(-ell/2) = {P**(-(k - 2*vp_int(2*a,P))/2):.6f}"
                print(f"   k={k}: {len(words[k])} tailless closed words, all with ell(gamma) = k: {okk}{ex}")
            # tailed words have ell < k
            k = 8
            stack = [(0, [], None)]; tailed_ells = []
            while stack:
                v, w, last = stack.pop()
                if len(w) == k:
                    if v == 0 and INV[w[0]] == w[-1]:
                        a, b, c, d = word_quaternion(w)
                        tailed_ells.append(k - 2*vp_int(2*a, P))
                    continue
                for s in range(6):
                    if last is not None and s == INV[last]:
                        continue
                    stack.append((adj[v][s], w + [s], s))
            print(f"   k=8 closed reduced words WITH a tail: {len(tailed_ells)}, their ell(gamma) values: {sorted(set(tailed_ells))} (all < 8: {max(tailed_ells) < 8})")
            print(f"   all tailless closed words have ell(gamma) = walk length: {okall}")
            # independent route for N_k: dense Hashimoto powers
            E = [(u, v) for u in range(n) for v in adj[u]]
            eidx = {e: i for i, e in enumerate(E)}
            m = len(E)
            B = np.zeros((m, m))
            for (u, v), i in eidx.items():
                for w_ in adj[v]:
                    if w_ != u:
                        B[i, eidx[(v, w_)]] = 1
            Bk = np.eye(m); diffs = []
            for k in range(1, KMAX + 1):
                Bk = Bk @ B
                diffs.append(int(round(np.trace(Bk))) - Nk_words[k])
            print(f"   dense Hashimoto route (|E_dir| = {m}): Tr B^k - N_k(words) for k=1..8 = {diffs}")
        print(f"   [{time.time()-t0:.1f} s]")

    # ---------------------------------------------------------------- (b) cutoff traces
    print("\n== T4(b)  Tr(P_n D_a P_n) on the code C_n of p^n Z_p^2 (dimension p^{2n}) against |a|^{1/2}/|1-a|, p = 5")
    p = P
    cases = [(5, 1), (25, 1), (125, 1), (1, 5), (1, 25), (2, 1), (6, 1), (26, 1), (126, 1), (-4, 1), (10, 1), (7, 5), (1, 1)]
    print("   a          n=0        n=1        n=2        n=3     Lefschetz |a|^(1/2)/|1-a|")
    for (an, ad) in cases:
        row = []
        for n_ in range(4):
            tr, va = cutoff_trace(an, ad, p, n_)
            row.append(tr * Fr(1) )   # times |a|^{1/2} below
        va = vp_int(an, p) - vp_int(ad, p)
        sa = p**(-va/2)
        if (an, ad) == (1, 1):
            lef = "infinite (a = 1: p^{2n}, the volume term)"
        else:
            one_minus = Fr(ad - an, ad)
            v1 = vp_int(one_minus.numerator, p) - vp_int(one_minus.denominator, p)
            lef = f"{sa * p**v1:.6f}  (v(1-a) = {v1})"
        vals = "  ".join(f"{float(r)*sa:9.5f}" for r in row)
        print(f"   {Fr(an,ad)!s:8s} {vals}   {lef}")
    print("DONE")
