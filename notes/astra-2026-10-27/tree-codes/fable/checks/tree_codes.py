#!/usr/bin/env python3
"""T1 and T3 of notes/astra-2026-10-27/tree-codes/lane-brief.md  (claude:fable-5.1, 2026-10-27).

T1: L^perp = det(g)^{-1} L for L = g Z_p^2; colour = v_p(det g) mod 2; the phase convention for W~.
T3: hyperbolic/elliptic classification of random integer matrices; translation length ell(gamma) =
    max(v(det) - 2 v(tr), 0) against the tree distances d(v, gamma^k v); the axis vertices are the split lattices.

Exact arithmetic throughout (python integers / fractions); p-adic eigenvalues by Hensel lifting mod p^N.
Run: python3 checks/tree_codes.py
"""
from fractions import Fraction as Fr
import random, itertools, sys

random.seed(20261027)

# ---------------------------------------------------------------- p-adic helpers
def vp(x, p):
    """p-adic valuation of a Fraction/int; +inf for 0."""
    x = Fr(x)
    if x == 0:
        return 10**9
    n, d = x.numerator, x.denominator
    v = 0
    while n % p == 0:
        n //= p; v += 1
    while d % p == 0:
        d //= p; v -= 1
    return v

def det2(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]

def mul2(a, b):
    return [[a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]]

def inv2(m):
    d = Fr(det2(m))
    return [[Fr(m[1][1])/d, -Fr(m[0][1])/d], [-Fr(m[1][0])/d, Fr(m[0][0])/d]]

def tree_dist(B1, B2, p):
    """distance in T_p between the homothety classes of the lattices with basis matrices B1, B2 (columns):
    elementary divisors of B1^{-1} B2 are p^a, p^b; distance = |a - b| = v(det) - 2 min v(entries)."""
    m = mul2(inv2(B1), B2)
    vmin = min(vp(m[i][j], p) for i in range(2) for j in range(2))
    return vp(det2(m), p) - 2*vmin

def is_unit_matrix(m, p):
    """m in GL_2(Z_p)?"""
    return all(vp(m[i][j], p) >= 0 for i in range(2) for j in range(2)) and vp(det2(m), p) == 0

J = [[0, 1], [-1, 0]]          # omega(x, y) = x^T J y = x1 y2 - x2 y1
I2 = [[1, 0], [0, 1]]

def transpose(m):
    return [[m[0][0], m[1][0]], [m[0][1], m[1][1]]]

def hensel_root(t, d, p, N):
    """the two roots in Z_p of x^2 - t x + d, which exist with distinct valuations when v(t) < v(d)/2.
    Returns (lam1, lam2) as integers mod p^N with v(lam1) = v(t) < v(lam2) = v(d) - v(t)."""
    s = vp(t, p)
    assert 2*s < vp(d, p), "not hyperbolic"
    # mu = lambda / p^s solves mu^2 - (t/p^s) mu + d/p^{2s} = 0; mod p: mu (mu - t') = 0 with t' a unit.
    tp, dp = t // p**s, d // p**(2*s)
    M = p**N
    roots = []
    for mu in (tp % p, 0):            # simple roots mod p
        for _ in range(N + 2):        # Newton iteration mod p^N
            f = (mu*mu - tp*mu + dp) % M
            fp = (2*mu - tp) % M
            mu = (mu - f*pow(fp, -1, M)) % M
        roots.append((mu * p**s) % (M * p**s))
    return roots[0], roots[1]

# ================================================================= T1
print("== T1  L^perp = det(g)^{-1} L, colour = v_p(det g) mod 2")
for p in (3, 5, 7):
    for trial in range(6):
        while True:
            g = [[Fr(random.randint(-30, 30)) * Fr(p)**random.randint(-2, 2) for _ in range(2)] for _ in range(2)]
            if det2(g) != 0:
                break
        # dual: x in L^perp iff g^T J^T x in Z_p^2  iff  x in (g^T J^T)^{-1} Z_p^2
        H = inv2(mul2(transpose(g), transpose(J)))              # basis of L^perp
        Hclaim = [[c / det2(g) for c in row] for row in g]       # basis of det(g)^{-1} L
        same = is_unit_matrix(mul2(inv2(Hclaim), H), p)          # same Z_p-lattice iff transition matrix in GL_2(Z_p)
        k = vp(det2(g), p)
        index = vp(det2(mul2(inv2(H), g)), p)                    # [L^perp : L] = p^index
        print(f"p={p} g=({g[0][0]},{g[0][1]};{g[1][0]},{g[1][1]})  v(det g)={k:3d}  L^perp == det^-1 L: {same}  "
              f"[L^perp:L] = p^{index} (claim p^{2*k}): {index == 2*k}")
        assert same and index == 2*k
    # the unique isotropic representative with k in {0,1} and its neighbours change colour
    for k in (0, 1):
        g = [[Fr(1), Fr(0)], [Fr(0), Fr(p**k)]]
        for t in range(p + 1):
            # neighbours of [g Z_p^2]: index-p sublattices  g (Z_p (1, t) + p Z_p^2)  and  g (Z_p (0,1) + p Z_p^2)
            if t < p:
                nb = mul2(g, [[Fr(1), Fr(0)], [Fr(t), Fr(p)]])
            else:
                nb = mul2(g, [[Fr(p), Fr(0)], [Fr(0), Fr(1)]])
            assert tree_dist(g, nb, p) == 1 and (vp(det2(nb), p) - k) % 2 == 1
    print(f"p={p}: all p+1 neighbours of the colour-k vertex (k=0,1) have v(det) of the other parity: True")

# ---------------------------------------------------------------- phase convention for W~ (finite model)
print("\n== T1'  phase convention: W~(u,v) = psi(s uv) W(u,v) is a representation on an isotropic lattice iff s = +1/2")
print("   model: functions on Z_p/p^2 Z_p (support condition dropped), W(u,v)f(x) = psi(vx) f(x+u), psi(x) = e^{2 pi i {x}_p}")
import numpy as np
for p in (3, 5):
    Mmod = p**2
    om = np.exp(2j*np.pi/Mmod)
    def W(u, v):            # u in Z/p^2, v in (1/p^2) Z / Z  represented by integer nu, v = nu / p^2
        m = np.zeros((Mmod, Mmod), complex)
        for x in range(Mmod):
            m[x, (x + u) % Mmod] = om**((v*x) % Mmod)
        return m
    for s_num, s_name in ((1, "+1/2"), (-1, "-1/2")):
        half = pow(2, -1, Mmod)
        def Wt(u, v):
            return om**((s_num*half*u*v) % Mmod) * W(u, v)
        # the isotropic lattice L_c = Z_p (1, c/p) + Z_p (0, 1), c = 1: generators lam = (1, p) [v = p/p^2 = 1/p], lam' = (0, p^2) [v = 1]
        # omega(lam, lam) = 0, so W~(lam)^2 must equal W~(2 lam)
        lam = (1, p)
        lhs = Wt(*lam) @ Wt(*lam)
        rhs = Wt(2*lam[0], 2*lam[1])
        ok = np.allclose(lhs, rhs)
        print(f"p={p} s={s_name}: W~(1,1/p)^2 == W~(2,2/p): {ok}")

# ================================================================= T3
print("\n== T3  classification of random integer matrices; translation length vs tree distances; axis = split lattices")
def vertices_within(R, p):
    """homothety classes at distance <= R from [Z_p^2], as basis matrices (columns), distance n:
    Z_p (x,y) + p^n Z_p^2 with (x:y) in P^1(Z/p^n)."""
    out = [(0, [[Fr(1), Fr(0)], [Fr(0), Fr(1)]])]
    for n in range(1, R + 1):
        pn = p**n
        for y in range(pn):                       # x = 1 (x a unit)
            out.append((n, [[Fr(1), Fr(0)], [Fr(y), Fr(pn)]]))
        for x in range(0, pn, p):                 # y = 1, x in pZ
            out.append((n, [[Fr(x), Fr(pn)], [Fr(1), Fr(0)]]))
    return out

def split_test(B, e1, e2, p):
    """L (basis B) is split by the lines Q_p e1, Q_p e2 iff L = (L cap l1) + (L cap l2)."""
    Binv = inv2(B)
    c1 = [Binv[0][0]*e1[0] + Binv[0][1]*e1[1], Binv[1][0]*e1[0] + Binv[1][1]*e1[1]]
    c2 = [Binv[0][0]*e2[0] + Binv[0][1]*e2[1], Binv[1][0]*e2[0] + Binv[1][1]*e2[1]]
    a = -min(vp(c1[0], p), vp(c1[1], p))         # p^a e1 is the generator of L cap l1
    b = -min(vp(c2[0], p), vp(c2[1], p))
    sub = [[c1[0]*Fr(p)**a, c2[0]*Fr(p)**b], [c1[1]*Fr(p)**a, c2[1]*Fr(p)**b]]   # coordinates of p^a e1, p^b e2 in the basis B
    return vp(det2(sub), p) == 0, a, b

N = 40
for p in (3, 5):
    print(f"\n-- p = {p}")
    count_h = 0
    trial = 0
    while trial < 10:
        g = [[random.randint(-12, 12) for _ in range(2)] for _ in range(2)]
        if det2(g) == 0:
            continue
        trial += 1
        t, d = g[0][0] + g[1][1], det2(g)
        vt, vd = vp(t, p), vp(d, p)
        ell = max(vd - 2*vt, 0)
        # tree distances d(v, gamma^k v) for the base vertex v = [Z_p^2]
        gk = I2
        dists = []
        for k in range(1, 6):
            gk = mul2(gk, g)
            dists.append(tree_dist(I2, [[Fr(x) for x in row] for row in gk], p))
        incs = [dists[i+1] - dists[i] for i in range(len(dists) - 1)]
        kind = "hyperbolic" if ell > 0 else "elliptic  "
        line = (f"g=({g[0][0]:3d},{g[0][1]:3d};{g[1][0]:3d},{g[1][1]:3d}) tr={t:4d} det={d:5d} v(tr)={vt} v(det)={vd} "
                f"{kind} ell={ell}  d(v,g^k v)={dists}  increments={incs}")
        if ell > 0:
            count_h += 1
            assert incs[-1] == ell and incs[-2] == ell
            lam1, lam2 = hensel_root(t, d, p, N)
            vl = (vp(lam1, p), vp(lam2, p))
            assert vl[1] - vl[0] == ell
            # eigenvectors (b, lam - a) or (lam - d, c)
            def eigvec(lam):
                a_, b_, c_, d_ = g[0][0], g[0][1], g[1][0], g[1][1]
                if vp(b_, p) < 10**8 and b_ != 0:
                    return [Fr(b_), Fr((lam - a_))]
                return [Fr(lam - d_), Fr(c_)]
            e1, e2 = eigvec(lam1), eigvec(lam2)
            # axis vertices within distance 3 of the base: displacement == ell; compare with the split test
            on_axis, split, both, n_in = 0, 0, 0, 0
            for (dist0, B) in vertices_within(3, p):
                n_in += 1
                gB = mul2([[Fr(x) for x in row] for row in g], B)
                disp = tree_dist(B, gB, p)
                sp, a_, b_ = split_test(B, e1, e2, p)
                on_axis += (disp == ell); split += sp; both += (disp == ell and sp)
                assert (disp == ell) == sp, (B, disp, sp)
            line += f" | v(eigs)={vl}; within radius 3: {n_in} vertices, {on_axis} with displacement ell, {split} split, equal: True"
        else:
            assert max(dists) <= dists[0] + 2  # bounded orbit (elliptic): distances do not grow
        print(line)
    print(f"p={p}: {count_h} hyperbolic of 10; every hyperbolic one: ell = v(det) - 2 v(tr) = v(lam2/lam1) = asymptotic increment of d(v, g^k v), "
          f"and axis vertices (radius 3) = split lattices exactly")

# squeeze diag(a^{-1}, a) translates the standard apartment by 2 v(a); diag(1, p) by one step
print("\n== T3'  squeeze diag(a^-1, a) with v(a) = m translates by 2m; diag(1,p) by one step and swaps colour")
for p in (3, 5):
    for m in (1, 2, 3):
        a = Fr(p**m)
        sq = [[1/a, Fr(0)], [Fr(0), a]]
        d_sq = tree_dist(I2, sq, p)
        half = [[Fr(1), Fr(0)], [Fr(0), Fr(p)]]
        print(f"p={p} m={m}: d([Z_p^2], diag(p^-m,p^m)[Z_p^2]) = {d_sq} (claim {2*m}); d(v, diag(1,p) v) = {tree_dist(I2, half, p)}, "
              f"colour change: {vp(det2(half), p) % 2 == 1}")
        assert d_sq == 2*m
print("\nALL ASSERTIONS PASSED")
