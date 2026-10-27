#!/usr/bin/env python
"""P2: the quaternion side for p = 37. B = (-2, -37)_Q (ramified at 37 and infinity), a maximal order O (basis from
PARI alginit; maximality verified by the reduced discriminant), the left ideal classes Cl(O) by BFS along the
l-neighbour tree (J subset I of index l^2), the ideal-class Brandt matrices for l = 2, 3, 5, 7, the unit groups, the
Eichler mass, and the half-loop count f_l = sum_i #{gamma in O_i : trd = 0, nrd = l}/2, all exact. The result is
compared with the Phi_l graphs of pizer_graph.py under ONE vertex relabelling for all four l.
Run with the venv interpreter:  python checks/pizer_quotient.py
Author: claude:fable-5.1, 2026-10-27."""
from fractions import Fraction as Fr
from math import gcd, isqrt
import itertools, sys
import cypari2, flint
pari = cypari2.Pari(); pari.allocatemem(10**9)

p = 37
A_, B_ = -2, -p                      # i^2 = A_, j^2 = B_, k = ij

def mul(x, y):
    a1, b1, c1, d1 = x; a2, b2, c2, d2 = y
    # (a + b i + c j + d k)(a' + b' i + c' j + d' k) in the algebra (A_, B_)
    return (a1*a2 + A_*b1*b2 + B_*c1*c2 - A_*B_*d1*d2,
            a1*b2 + b1*a2 - B_*c1*d2 + B_*d1*c2,
            a1*c2 + c1*a2 + A_*b1*d2 - A_*d1*b2,
            a1*d2 + d1*a2 + b1*c2 - c1*b2)
def conj(x): return (x[0], -x[1], -x[2], -x[3])
def nrd(x): return mul(x, conj(x))[0]
def trd(x): return 2 * x[0]

# sanity of the multiplication table
i_, j_, k_ = (0,1,0,0), (0,0,1,0), (0,0,0,1)
assert mul(i_, i_) == (A_,0,0,0) and mul(j_, j_) == (B_,0,0,0) and mul(i_, j_) == k_ and mul(j_, i_) == (0,0,0,-1)
assert mul(k_, k_) == (-A_*B_,0,0,0)

class Lat:
    """full-rank Z-lattice in B, stored as (D, H): rows of H/D are a Z-basis, H in Hermite normal form."""
    def __init__(self, gens):
        D = 1
        for g in gens:
            for c in g: D = D * c.denominator // gcd(D, c.denominator)
        rows = [[int(c * D) for c in g] for g in gens]
        H = flint.fmpz_mat(rows).hnf()
        rows = [[int(H[r, c]) for c in range(4)] for r in range(H.nrows()) if any(int(H[r, c]) for c in range(4))]
        assert len(rows) == 4
        g0 = D
        for r in rows:
            for c in r: g0 = gcd(g0, c)
        self.D = D // g0; self.H = tuple(tuple(c // g0 for c in r) for r in rows)
    def basis(self): return [tuple(Fr(c, self.D) for c in r) for r in self.H]
    def key(self): return (self.D, self.H)
    def __eq__(self, o): return self.key() == o.key()
    def __hash__(self): return hash(self.key())
    def det(self):      # |det| of a basis, as a Fraction
        return abs(Fr(int(flint.fmpz_mat([list(r) for r in self.H]).det()), self.D**4))
    def gram(self):     # integer Gram G'_ab = trd(w_a conj(w_b)) for the integer rows w; nrd(sum x_a w_a/D) = x^T G' x / (2 D^2)
        W = [tuple(Fr(c) for c in r) for r in self.H]
        return [[int(trd(mul(W[a], conj(W[b])))) for b in range(4)] for a in range(4)]
    def norm(self):     # reduced norm of the lattice = gcd of nrd of elements (via the Gram matrix: gcd of G'/2 diag and G' off-diag... use elements)
        W = self.basis(); vals = [nrd(w) for w in W] + [nrd(tuple(W[a][t] + W[b][t] for t in range(4))) for a in range(4) for b in range(a+1, 4)]
        g = Fr(0)
        for v in vals:
            g = Fr(gcd(g.numerator * v.denominator, v.numerator * g.denominator), g.denominator * v.denominator) if g else v
        return g
    def elements_of_norm(self, m):
        """all x in the lattice with nrd(x) = m (m a positive rational), via qfminim on the integer Gram"""
        G = self.gram(); bound = 2 * m * self.D**2
        assert bound.denominator == 1; bound = int(bound)
        res = pari.qfminim(pari.matrix(4, 4, [c for r in G for c in r]), bound, 10**6, 2)
        vecs = []
        W = self.basis()
        for c in range(int(res[0]) // 2):
            v = [int(res[2][r, c]) for r in range(4)]
            q = sum(v[a] * G[a][b] * v[b] for a in range(4) for b in range(4))
            if q == bound:
                el = tuple(sum(v[a] * W[a][t] for a in range(4)) for t in range(4))
                vecs.append(el); vecs.append(tuple(-c for c in el))
        return vecs

def lat_mul(L1, L2):
    return Lat([mul(a, b) for a in L1.basis() for b in L2.basis()])
def lat_conj(L): return Lat([conj(a) for a in L.basis()])
def lat_scale(L, s): return Lat([tuple(s * c for c in a) for a in L.basis()])
def lat_add(L1, L2): return Lat(L1.basis() + L2.basis())

al = pari('alginit(nfinit(y), [%d,%d])' % (A_, B_))
print("algebra (%d,%d): ramified places %s" % (A_, B_, pari.algramifiedplaces(al)))
Bas = pari.algbasis(al)
O = Lat([tuple(Fr(str(Bas[r, c])) for r in range(4)) for c in range(4)])
print("maximal order O basis (rows, in 1,i,j,k):", [[str(c) for c in r] for r in O.basis()])
# reduced discriminant: sqrt|det trd(e_a e_b)|
W = O.basis()
T = [[int(trd(mul(W[a], W[b]))) for b in range(4)] for a in range(4)]
d = abs(int(flint.fmpz_mat(T).det()))
print("det(trd(e_a e_b)) = %d = p^2 ? %s  -> O is maximal (reduced discriminant %d)" % (d, d == p * p, isqrt(d)))
assert d == p * p
assert lat_mul(O, O) == O

def right_order(I):          # O_R(I) = I^{-1} I = conj(I) I / nrd(I)
    return lat_scale(lat_mul(lat_conj(I), I), 1 / I.norm())
def is_equiv(I, J):          # left O-ideals: J = I beta  <=>  conj(I) J has an element of norm nrd(I) nrd(J)
    L = lat_mul(lat_conj(I), J)
    return len(L.elements_of_norm(I.norm() * J.norm())) > 0
def neighbours(I, l):        # the l+1 left O-ideals J subset I with [I:J] = l^2 :  J = O x + l I, x in I
    out = {}
    Ib = I.basis()
    lI = lat_scale(I, l)
    for coeffs in itertools.product(range(l), repeat=4):
        if not any(coeffs): continue
        xv = tuple(sum(coeffs[a] * Ib[a][t] for a in range(4)) for t in range(4))
        J = Lat([mul(o, xv) for o in O.basis()] + lI.basis())
        if J.det() == I.det() * l**2:
            out[J.key()] = J
    assert len(out) == l + 1, len(out)
    return list(out.values())

# class set by BFS with l = 2 neighbours, then verified with every l
reps = [O]
queue = [O]
while queue:
    I = queue.pop()
    for J in neighbours(I, 2):
        if not any(is_equiv(J, R) for R in reps):
            reps.append(J); queue.append(J)
h = len(reps)
print("class number h(O) = %d (BFS at l = 2); norms of representatives: %s" % (h, [str(R.norm()) for R in reps]))
orders = [right_order(R) for R in reps]
units = [len(Oi.elements_of_norm(Fr(1))) for Oi in orders]
mass = sum(Fr(1, u) for u in units)
print("unit group orders |O_i^x| = %s ; Eichler mass sum 1/|O_i^x| = %s = (p-1)/24 ? %s" % (units, mass, mass == Fr(p - 1, 24)))
assert mass == Fr(p - 1, 24)

Bq = {}
fq = {}
for l in [2, 3, 5, 7]:
    Bl = [[0] * h for _ in range(h)]
    for a, I in enumerate(reps):
        for J in neighbours(I, l):
            cls = [b for b in range(h) if is_equiv(J, reps[b])]
            assert len(cls) == 1
            Bl[a][cls[0]] += 1
    Bq[l] = Bl
    # half-loops: elements of trace 0 and norm l in O_i, up to sign
    f = 0
    for Oi in orders:
        els = Oi.elements_of_norm(Fr(l))
        f += sum(1 for e in els if trd(e) == 0) // 2
    fq[l] = f
    print("l = %d: ideal-class Brandt matrix B(l) = %s ; half-loops f_l = %d ; #elements of norm l in the orders: %s" % (l, Bl, f, [len(Oi.elements_of_norm(Fr(l))) for Oi in orders]))

# compare with the Phi_l graphs of pizer_graph.py (p = 37) under one permutation
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from pizer_graph import ss_j, brandt
t = pari("ffgen([37,2],'t)")
js = ss_j(37, t)
Bphi = {l: brandt(37, l, js, t) for l in [2, 3, 5, 7]}
found = None
for perm in itertools.permutations(range(h)):
    if all(Bq[l][perm[a]][perm[b]] == Bphi[l][a][b] for l in Bq for a in range(h) for b in range(h)):
        found = perm; break
print("Phi_l graphs (vertices = j-invariants %s):" % [str(j) for j in js])
for l in Bphi: print("  l = %d: B_Phi(l) = %s" % (l, Bphi[l]))
print("one vertex relabelling j_a -> ideal class %s matches all four Brandt matrices: %s" % (found, found is not None))
assert found is not None
print("half-loop counts from the quaternion side: %s (isogeny side, pizer_graph.py p = 37: l=2:1, l=3:0, l=5:2, l=7:0)" % fq)
assert fq == {2: 1, 3: 0, 5: 2, 7: 0}
print("Gamma = O[1/l]^x / Z[1/l]^x contains an element of odd norm valuation at l (an element of norm l in some O_i):",
      {l: any(len(Oi.elements_of_norm(Fr(l))) > 0 for Oi in orders) for l in [2, 3, 5, 7]})
