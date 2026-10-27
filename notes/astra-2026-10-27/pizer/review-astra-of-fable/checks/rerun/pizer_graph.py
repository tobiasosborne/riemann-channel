#!/usr/bin/env python
"""P1: the Pizer graph G(p, l) built over F_{p^2} from the modular polynomial Phi_l; Brandt matrix B(l);
exact comparison of charpoly(B(l)) with (x - l - 1) * charpoly(T_l | S_2(Gamma_0(p))); Ramanujan bound;
explicit Hashimoto operator with the dual-isogeny reversal (p = 1 mod 12), half-loop count f, and the
corrected Ihara-Bass identity  det(1 - uB_H) = (1+u)^f (1-u^2)^{(N-f)/2 - n} det(1 - Au + l u^2);
point counts #X_0(p)(F_l) = l + 1 - Tr T_l, checked against hyperellcharpoly of the genus-2 model of X_0(37).
Run with the venv interpreter (cypari2 + python-flint):  python checks/pizer_graph.py
Author: claude:fable-5.1, 2026-10-27."""
import sys, itertools
import cypari2, flint
pari = cypari2.Pari(); pari.allocatemem(2 * 10**9)
x, y = pari('x'), pari('y')

def ss_j(p, t):
    """supersingular j-invariants in F_{p^2} via the Deuring polynomial H_p(lambda) = sum C(m,i)^2 lambda^i."""
    m = (p - 1) // 2
    H = pari('Mod(1,%d)' % p) * sum(pari.binomial(m, i)**2 * x**i for i in range(m + 1))
    lams = pari.polrootsmod(H, t)
    assert len(lams) == m, "H_p must split over F_{p^2}"
    js = []
    for lam in lams:
        j = 256 * (lam**2 - lam + 1)**3 / (lam**2 * (lam - 1)**2)
        if all(j != jj for jj in js):
            js.append(j)
    return js

def weight(j, p):
    # w = |Aut(E)|/2 : 1 generically, 2 for j = 1728, 3 for j = 0 (p > 3)
    if j == 0: return 3
    if j == 1728: return 2
    return 1

def model(j, t, p):
    """a model over F_{p^2} with Frobenius = -p (trace -2p), so every l-isogeny is F_{p^2}-rational."""
    if j == 0: E = pari.ellinit([0, 1], t)
    elif j == 1728: E = pari.ellinit([1, 0], t)
    else: E = pari.ellinit(pari.ellfromj(j), t)
    tr = p * p + 1 - pari.ellcard(E)
    if tr != -2 * p:
        # quadratic twist by a nonsquare d of F_{p^2}
        d = t
        while pari.issquare(d): d = d + 1
        a4, a6 = E[3], E[4]
        E = pari.ellinit([a4 * d**2, a6 * d**3], t)
        tr = p * p + 1 - pari.ellcard(E)
    assert tr == -2 * p, (j, tr)
    return E

def charpoly_Z(M):
    return flint.fmpz_mat([[int(v) for v in row] for row in M]).charpoly()

def rev(P, deg):
    """u^deg P(1/u) as fmpz_poly"""
    c = [int(P[i]) for i in range(deg + 1)]
    return flint.fmpz_poly(c[::-1])

def brandt(p, l, js, t):
    n = len(js)
    Phi = pari.polmodular(l)
    B = [[0] * n for _ in range(n)]
    for i, j in enumerate(js):
        P = pari.subst(Phi, x, j)          # Phi_l(j_i, y), degree l+1 in y
        for k, jk in enumerate(js):
            m = 0
            Q = P
            while pari.subst(Q, y, jk) == 0:
                Q = Q / (y - jk); m += 1
            B[i][k] = m
        assert sum(B[i]) == l + 1, "all roots of Phi_l(j_i, y) must be supersingular"
    return B

def hashimoto(p, l, js, t, B):
    """oriented edges (i, a): a-th subgroup C of order l of E_i (as kernel polynomial). Everything is done over
    F_big = F_{p^{2k}}, k = order of -p mod l, where E[l] is fully rational (Frobenius of the F_{p^2}-model is -p);
    subgroups are found by grouping torsion points, not from the factorisation of the division polynomial.
    Returns the Hashimoto matrix, the half-loop count f (fixed points of the dual-isogeny reversal), N."""
    n = len(js)
    k = 1
    while pow(-p, k, l) != 1 % l: k += 1
    T = pari("ffgen([%d,%d],'T)" % (p, 2 * k))
    emb = pari.ffembed(t, T)
    jsB = [pari.ffmap(emb, j) for j in js]
    Es = []
    for j in js:
        E = model(j, t, p)
        Es.append(pari.ellinit([pari.ffmap(emb, E[3]), pari.ffmap(emb, E[4])], T))
    kers = []
    for E in Es:
        xs = pari.polrootsmod(pari.elldivpol(E, l), T)
        nx = 3 if l == 2 else (l * l - 1) // 2
        assert len(xs) == nx, "E[l] must be rational over F_big"
        used = set(); hs = []
        for x0 in xs:
            if str(x0) in used: continue
            ys = pari.ellordinate(E, x0); P = [x0, ys[0]]
            xsC = [pari.ellmul(E, P, m)[0] for m in range(1, (l - 1) // 2 + 1)] if l > 2 else [x0]
            for xx in xsC: used.add(str(xx))
            h = pari('1')
            for xx in xsC: h = h * (x - xx)
            hs.append(h)
        assert len(hs) == l + 1 and len(used) == nx, (len(hs), len(used))
        kers.append(hs)
    edges = [(i, a) for i in range(n) for a in range(l + 1)]
    idx = {e: r for r, e in enumerate(edges)}
    target, reverse = {}, {}
    for (i, a) in edges:
        E = Es[i]; h = kers[i][a]
        iso = pari.ellisogeny(E, h)
        Ep = pari.ellinit(iso[0], T)
        jp = Ep[12]
        kk = [m for m in range(n) if jsB[m] == jp]
        assert len(kk) == 1; kk = kk[0]
        target[(i, a)] = kk
        # isomorphism Ep -> E_k on x: x -> s x, with s = (B_k/B')(A'/A_k) (j != 0, 1728 only)
        A1, B1 = Ep[3], Ep[4]; Ak, Bk = Es[kk][3], Es[kk][4]
        s = (Bk / B1) * (A1 / Ak)
        assert s**2 == Ak / A1 and s**3 == Bk / B1, "target is the twist: trace mismatch"
        f, g, hh = iso[1]
        b = (a + 1) % (l + 1)                      # another subgroup C'' != C ; its image is the dual's kernel
        h2 = kers[i][b]
        alpha = pari.Mod(f, h2) / pari.Mod(hh, h2)**2
        chi = pari.charpoly(alpha, y)              # roots: x-coordinates of phi(C''\0) on Ep
        hk = pari.subst(chi, y, y / s)             # transport to E_k
        hk = pari.subst(hk, y, x); hk = hk / pari.pollead(hk)
        c = [cc for cc in range(l + 1) if kers[kk][cc] == hk]
        assert len(c) == 1, ("image kernel not found", i, a, kk, hk)
        reverse[(i, a)] = (kk, c[0])
    for e in edges:
        assert reverse[reverse[e]] == e, "reversal must be an involution"
        assert target[reverse[e]] == e[0]
    fixed = sum(1 for e in edges if reverse[e] == e)
    N = len(edges)
    BH = [[0] * N for _ in range(N)]
    for e in edges:
        for e2 in edges:
            if e2[0] == target[e] and e2 != reverse[e]:
                BH[idx[e]][idx[e2]] = 1
    for i in range(n):
        for m in range(n):
            assert sum(1 for a in range(l + 1) if target[(i, a)] == m) == B[i][m]
    return BH, fixed, N

def main():
    out = []
    def pr(*a):
        s = ' '.join(str(v) for v in a); print(s); out.append(s)
    pr("P1 table: Pizer graphs G(p,l) from Phi_l over F_{p^2}; Brandt matrices; Hecke comparison; Ihara-Bass with half-loops")
    ps = [int(a) for a in sys.argv[1:]] or [11, 37, 73, 101, 109]
    for p in ps:
        t = pari("ffgen([%d,2],'t)" % p)
        js = ss_j(p, t)
        n = len(js)
        expected = p // 12 + {1: 0, 5: 1, 7: 1, 11: 2}[p % 12]
        ws = [weight(j, p) for j in js]
        for j in js:
            assert pari.ellissupersingular(model(j, t, p)) == 1
        pr("\n==== p = %d (p mod 12 = %d): #S_p = %d (formula %d), genus g(X_0(p)) = %d, weights w = %s, mass sum 1/w_i = %s (Eichler: sum 1/|O_i^x| = (p-1)/24, so sum 1/w_i = (p-1)/12 = %s)"
           % (p, p % 12, n, expected, n - 1, ws, pari('sum(i=1,%d,1/[%s][i])' % (n, ','.join(map(str, ws)))), pari('(%d-1)/12' % p)))
        assert n == expected
        pr("  j-invariants:", [str(j) for j in js])
        mf = pari('mfinit([%d,2],1)' % p)
        g = int(pari.mfdim(mf)); assert g == n - 1
        for l in [2, 3, 5, 7]:
            B = brandt(p, l, js, t)
            pr("  -- l = %d: B(l) =" % l, B)
            # weighted symmetry w_j B_ij = w_i B_ji
            for i in range(n):
                for k in range(n):
                    assert ws[k] * B[i][k] == ws[i] * B[k][i], "w_j B_ij = w_i B_ji fails"
            chiB = charpoly_Z(B)
            T = pari.mfheckemat(mf, l)
            chiT = pari.charpoly(T)
            chiT_Z = flint.fmpz_poly([int(pari.polcoef(chiT, i)) for i in range(g + 1)])
            prod = chiT_Z * flint.fmpz_poly([-(l + 1), 1])
            pr("     charpoly B(l) =", chiB)
            pr("     (x-l-1) * charpoly(T_l on S_2(Gamma_0(%d))) =" % p, prod, " EQUAL:", chiB == prod)
            assert chiB == prod
            # Ramanujan: all roots of chiT in [-2 sqrt l, 2 sqrt l]
            roots = pari.polroots(chiT)
            mx = max(abs(float(r.real())) for r in roots) if g > 0 else 0.0
            pr("     max |a_l(f)| = %.6f <= 2 sqrt(l) = %.6f : %s ; eigenvalues of B(l): %s" % (mx, 2 * l**0.5, mx <= 2 * l**0.5 + 1e-9, [str(r) for r in pari.polroots(pari.Pol(list(reversed([int(c) for c in chiB.coeffs()]))))]))
            assert all(abs(r.imag()) < 1e-9 for r in roots)
            # P_{p,l}(u) and the count
            trT = int(pari.trace(T))
            pr("     #X_0(%d)(F_%d) = l + 1 - Tr T_l = %d" % (p, l, l + 1 - trT))
            # det(1 - B u + l u^2) via the companion M = ((B,-l),(1,0))
            M = [[0] * (2 * n) for _ in range(2 * n)]
            for i in range(n):
                for k in range(n): M[i][k] = B[i][k]
                M[i][n + i] = -l; M[n + i][i] = 1
            chiM = charpoly_Z(M)
            detAu = rev(chiM, 2 * n)                   # det(1 - Bu + l u^2)
            Ppl = flint.fmpz_poly([1]);
            # P_{p,l}(u) = det(1 - Bu + lu^2) / ((1-u)(1-lu))
            q, r = divmod(detAu, flint.fmpz_poly([1, -1]) * flint.fmpz_poly([1, -l]))
            assert r == 0
            pr("     det(1 - B(l)u + l u^2) = (1-u)(1-lu) * P_{p,l}(u) with P_{p,l}(u) (variable x = u) =", q)
            if p % 12 == 1:
                BH, f, N = hashimoto(p, l, js, t, B)
                chiH = charpoly_Z(BH)
                detH = rev(chiH, N)                    # det(1 - u B_H)
                e = (N - f) // 2 - n
                lhs = detH; rhs = flint.fmpz_poly([1, 1])**f * detAu
                if e >= 0: rhs = rhs * flint.fmpz_poly([1, 0, -1])**e
                else: lhs = lhs * flint.fmpz_poly([1, 0, -1])**(-e)
                ok = (lhs == rhs)
                naive = (detH == flint.fmpz_poly([1, 0, -1])**(N // 2 - n) * detAu) if (N // 2 - n) >= 0 else None
                pr("     Hashimoto: N = %d oriented edges, half-loops (self-dual loops, phi^2 = -l) f = %d, Tr B(l) = %d;" % (N, f, sum(B[i][i] for i in range(n))),
                   "det(1-uB_H) = (1+u)^f (1-u^2)^{(N-f)/2-n} det(1-Bu+lu^2):", ok, "; naive (1-u^2)^{N/2-n} form:", naive)
                assert ok
                pr("     det(1 - u B_H) =", detH)
    # X_0(37) model check
    pr("\n==== X_0(37): y^2 = -x^6 - 9x^4 - 11x^2 + 37 (from memory), hyperellcharpoly over F_l versus Hecke")
    mf = pari('mfinit([37,2],1)')
    for l in [3, 5, 7, 11, 13, 17, 19, 23]:
        f = pari('Mod(1,%d)*(-x^6-9*x^4-11*x^2+37)' % l)
        chiF = pari.hyperellcharpoly(f)
        T = pari.mfheckemat(mf, l)
        chiT = pari.charpoly(T)
        # expected: prod_f (x^2 - a_l x + l) = resultant-type: compute from eigenvalues: chiT(a) -> prod (x^2 - a x + l)
        a = [r for r in pari.polroots(chiT)]
        exp = pari.polresultant(pari.subst(chiT, x, pari('z')), x**2 - pari('z') * x + l, pari('z'))
        npts = l + 1 - int(pari.trace(T))
        # direct point count of the model (affine points over F_l + 2 points at infinity since leading coeff -1: at infinity y^2 = -1 ...)
        cnt = 0
        for xx in range(l):
            v = int(pari.subst(pari('-x^6-9*x^4-11*x^2+37'), x, xx)) % l
            cnt += 1 + int(pari.kronecker(v, l)) if v % l else 1
        cnt += 1 + int(pari.kronecker(-1, l))   # points at infinity: y^2 = lead coeff = -1
        pr("  l = %2d: Frobenius charpoly of the model = %s ; from Hecke: %s ; equal: %s ; #X_0(37)(F_l): Hecke %d, direct count of model %d" % (l, chiF, exp, chiF == exp, npts, cnt))
        assert chiF == exp and npts == cnt
    if not sys.argv[1:]:
      with open(__file__.replace('pizer_graph.py', 'output_pizer_graph.txt'), 'w') as fh:
        fh.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()
