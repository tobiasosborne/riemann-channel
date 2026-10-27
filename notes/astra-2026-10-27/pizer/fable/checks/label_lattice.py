#!/usr/bin/env python
"""P3: the label phase space Z^{2n} of the Pizer graph, M = ((B(l), -l), (1, 0)), the nontrivial sublattice
L0 = {(f, g): sum f = sum g = 0} (the Omega-orthogonal of the trivial plane Z(v,0) + Z(0,v), v = (1,...,1)), the
characteristic polynomial of M on L0 against P_{p,l}, the Smith normal forms of 1 - M^k on L0 (k = 1..4) against the
Hecke count #J_0(p)(F_{l^k}) = Res(chi, 1 - x^k), the group structure for p = 37 against E1(F_{l^k}) x E2(F_{l^k})
(37a1: y^2 + y = x^3 - x, 37b1: y^2 + y = x^3 + x^2 - 23x - 50), and det(Omega|L0) = n^2.
Run with the venv interpreter:  python checks/label_lattice.py
Author: claude:fable-5.1, 2026-10-27."""
import sys, itertools
from math import gcd
import cypari2, flint
pari = cypari2.Pari(); pari.allocatemem(10**9)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from pizer_graph import ss_j, brandt
x = pari('x')

def snf_invariants(Mat):
    S = flint.fmpz_mat(Mat).snf()
    d = [abs(int(S[i, i])) for i in range(S.nrows())]
    return [v for v in d if v != 1]

def group_snf(inv_list):
    """SNF invariants of a product of cyclic groups"""
    if not inv_list: return []
    n = len(inv_list)
    D = [[0] * n for _ in range(n)]
    for i, v in enumerate(inv_list): D[i][i] = v
    return snf_invariants(D)

def matpow(A, k):
    n = len(A); R = [[int(i == j) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = [[sum(R[i][t] * A[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
    return R

out = []
def pr(*a):
    s = ' '.join(str(v) for v in a); print(s); out.append(s)

E1 = pari.ellinit([0, 0, 1, -1, 0]); E2 = pari.ellinit([0, 1, 1, -23, -50])
pr("Cremona 37a1: y^2 + y = x^3 - x, conductor %s, a_2 = %s, a_3 = %s, a_5 = %s; 37b1: y^2 + y = x^3 + x^2 - 23x - 50, conductor %s, a_2 = %s, a_3 = %s, a_5 = %s"
   % (pari.ellglobalred(E1)[0], pari.ellap(E1, 2), pari.ellap(E1, 3), pari.ellap(E1, 5), pari.ellglobalred(E2)[0], pari.ellap(E2, 2), pari.ellap(E2, 3), pari.ellap(E2, 5)))
pr("rank 37a1 (analytic, ellanalyticrank) = %s ; rank 37b1 = %s" % (pari.ellanalyticrank(E1)[0], pari.ellanalyticrank(E2)[0]))

for p in [37, 73, 109]:
    t = pari("ffgen([%d,2],'t)" % p)
    js = ss_j(p, t); n = len(js); g = n - 1
    mf = pari('mfinit([%d,2],1)' % p)
    pr("\n==== p = %d, n = %d, g = %d" % (p, n, g))
    for l in [2, 3, 5, 7]:
        B = brandt(p, l, js, t)
        # M on Z^{2n}
        M = [[0] * (2 * n) for _ in range(2 * n)]
        for i in range(n):
            for k in range(n): M[i][k] = B[i][k]
            M[i][n + i] = -l; M[n + i][i] = 1
        # Omega and the similitude identity
        Om = [[0] * (2 * n) for _ in range(2 * n)]
        for i in range(n): Om[i][n + i] = 1; Om[n + i][i] = -1
        MT = [[M[j][i] for j in range(2 * n)] for i in range(2 * n)]
        prod = [[sum(MT[i][a] * Om[a][b] * M[b][j] for a in range(2 * n) for b in range(2 * n)) for j in range(2 * n)] for i in range(2 * n)]
        assert prod == [[l * Om[i][j] for j in range(2 * n)] for i in range(2 * n)]
        # M on L0 in the basis (e_i - e_{n-1}, 0), (0, e_i - e_{n-1}), i < n-1 : coordinates are the first n-1 entries
        m = n - 1
        M0 = [[0] * (2 * m) for _ in range(2 * m)]
        for i in range(m):
            # image of (e_i - e_{n-1}, 0): f = B e_i - B e_{n-1}, g = e_i - e_{n-1}
            for r in range(m): M0[r][i] = B[r][i] - B[r][n - 1]
            M0[m + i][i] = 1
            # image of (0, e_i - e_{n-1}): f = -l (e_i - e_{n-1}), g = 0
            M0[i][m + i] = -l
        chi0 = flint.fmpz_mat(M0).charpoly()
        T = pari.mfheckemat(mf, l); chiT = pari.charpoly(T)
        chiH = pari.polresultant(pari.subst(chiT, x, pari('z')), x**2 - pari('z') * x + l, pari('z'))   # prod_f (x^2 - a_l x + l)
        chiH_Z = flint.fmpz_poly([int(pari.polcoef(chiH, i)) for i in range(2 * g + 1)])
        pr("  -- l = %d: charpoly(M | L0) = %s ; prod_f (x^2 - a_l(f) x + l) from Hecke: equal %s" % (l, chi0, chi0 == chiH_Z))
        assert chi0 == chiH_Z
        # Omega restricted to L0: Gram C of A_{n-1} (C_ij = 1 + delta_ij) in both blocks, det = n^2
        C = [[1 + int(i == j) for j in range(m)] for i in range(m)]
        detC = int(flint.fmpz_mat(C).det())
        pr("     Omega|L0 = ((0, C), (-C, 0)) with C the A_{n-1} Gram matrix, det C = %d = n, det Omega|L0 = %d = n^2; index [Z^{2n} : L0 + L_triv] = n^2 = %d" % (detC, detC**2, n * n))
        assert detC == n
        for k in [1, 2, 3, 4]:
            Mk = matpow(M0, k)
            A = [[int(i == j) - Mk[i][j] for j in range(2 * m)] for i in range(2 * m)]
            inv = snf_invariants(A)
            order = 1
            for v in inv: order *= v
            det = abs(int(flint.fmpz_mat(A).det()))
            hecke = int(pari.polresultant(chiH, 1 - x**k))
            line = "     k = %d: L0/(1-M^k)L0 = Z/%s, order %d ; #J_0(%d)(F_{%d^%d}) from Hecke = %d ; equal %s" % (k, ' x Z/'.join(map(str, inv)) if inv else '1', order, p, l, k, hecke, order == hecke)
            assert order == det == hecke
            if p == 37:
                F = pari("ffgen([%d,%d],'u)" % (l, k))
                g1 = [int(v) for v in pari.ellgroup(pari.ellinit(E1, F))]
                g2 = [int(v) for v in pari.ellgroup(pari.ellinit(E2, F))]
                prodg = group_snf(g1 + g2)
                line += " ; E1(F) = %s, E2(F) = %s, E1 x E2 as SNF = %s ; graph lattice = product group: %s" % (g1, g2, prodg, prodg == inv)
            pr(line)

with open(__file__.replace('label_lattice.py', 'output_label_lattice.txt'), 'w') as fh:
    fh.write('\n'.join(out) + '\n')
