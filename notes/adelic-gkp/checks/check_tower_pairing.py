#!/usr/bin/env python3
"""Checks for 'The logical commutator of the tower's codes is a pairing on the points' (notes/adelic-gkp/tower-pairing.md), lane U.

Setting (lattice-tower.md). L = Z^{2n}, Omega standard, step M with M^T Omega M = q Omega, V = q M^{-1}. Level-k code C_k: stabiliser lattice
Lam_k = (1 - V^k) L, logical group A_k = Lam_k^perp / Lam_k with commutator c(a, b) = exp(2 pi i Omega(a, b)).
Shifts: Fix(M^k) = Lam_k^perp / L (the periodic syndromes, = the points); phases: L / Lam_k.

Curve side: PARI/GP 2.15.4 through the gp binary. E1: y^2 + xy = x^3 + 1 over F_2 (Deligne module: companion of x^2 + x + 2).
E3 pair over F_7 (trace 2): E4: y^2 = x^3 + 3x + 3 (j = 4), E5: y^2 = x^3 + x + 3 (j = 5); lattices (1,0,6) and (2,0,3) with
M_(A,B,C) = [[(a-B)/2, -C], [A, (a+B)/2]] (curve-bridge.md section 1).

Root-of-unity normalisation iota (q = 7 only): the 8th root w in F_{7^k} with w + 1/w = 3 is sent to exp(2 pi i / 8), and 4 in F_7 to
exp(2 pi i / 3). This is the identification induced by a Deligne embedding eps with eps(s) = +sqrt 2 for the 7-adic s = sqrt 2 = 3 mod 7 (the
convention of overlap-data.md section 1, under which j = 5 is the principal curve) and eps(sqrt -6) = +i sqrt 6 for the 7-adic sqrt -6 = 6 mod 7.

Pairings compared (P, Q points; P~, Q~ lifts to Lam_k^perp; N a prime power):
  Weil:  e_N(P, Q)  versus  c(N P~, Q~) = exp(2 pi i N Omega(P~, Q~))           on E[N] inside Fix(M^k)
  Tate:  t_N(P, Q)  versus  c(P~, (1 - M^k) Q~) = exp(2 pi i Omega(P~, (1 - M^k) Q~))  on Fix[N] x Fix/N, N | q^k - 1
For every Frobenius-equivariant isomorphism phi: E(F_{q^k})_l -> Fix(M^k)_l the script finds the units s with
(curve exponent) = s * (lattice exponent) mod N on generators, and reports the set of such s ("scale set").
Run:  python3 check_tower_pairing.py > output_tower_pairing.txt   (about 10 s)
"""
import itertools
import subprocess
import time
from fractions import Fraction
from math import gcd
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

T0 = time.time()
npass = nfail = 0


def check(name, ok, detail=""):
    global npass, nfail
    npass += bool(ok)
    nfail += (not ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))


# ------------------------------------------------------------------------------------------------ gp
GP_LIB = r"""
setrand(20261006);
\\ l-primary part of E(F_{p^k}): invariants o1 >= o2 and a basis (random points; independence by the Weil pairing)
lpart(E,l)={my(cyc=ellgroup(E),Nn=ellcard(E),co,os,g1,x,P,z);
  os=select(o->o>1, apply(d->l^valuation(d,l), cyc)); co=Nn/l^valuation(Nn,l);
  until(ellorder(E,g1)==os[1], g1=ellmul(E,random(E),co));
  if(#os==1, return([os,[g1]]));
  P=ellmul(E,g1,os[1]/os[2]);
  while(1, x=ellmul(E,random(E),co); if(ellorder(E,x)!=os[2], next); z=ellweilpairing(E,P,x,os[2]); if(fforder(z)==os[2], break));
  [os,[g1,x]]};
frob(P,q)=if(#P<2,P,[P[1]^q,P[2]^q]);
\\ coordinates of R in the basis gs (orders os), brute force
coords(E,R,os,gs)={my(S,T);
  if(#os==1, T=[0]; for(a=0,os[1]-1, if(T==R, return([a])); T=elladd(E,T,gs[1])); error("nc1"));
  S=[0]; for(a=0,os[1]-1, T=S; for(b=0,os[2]-1, if(T==R, return([a,b])); T=elladd(E,T,gs[2])); S=elladd(E,S,gs[1])); error("nc2")};
dlogmu(z,w,N)={for(j=0,N-1, if(w^j==z, return(j))); error("dlog")};
\\ omega_N.  nm = 7: w8 + 1/w8 = 3, w4 = w8^2, w2 = -1, w3 = 4.  nm = -7: w8 + 1/w8 = 4.  else: a power of ffprimroot
omg(t,N,nm)={my(Q=t.p^t.f,g=ffprimroot(t),w,z);
  if(N==2, return(-1*t^0));
  if(nm==7 && (N==8 || N==4), z=g^((Q-1)/8); w=0;
     forstep(j=1,7,2, if(z^j+z^(-j)==3, w=z^j; break)); return(w^(8/N)));
  if(nm==-7 && N==8, z=g^((Q-1)/8); forstep(j=1,7,2, if(z^j+z^(-j)==4, return(z^j))));
  if(nm==7 && N==3, return(4*t^0));
  if(nm==7 && N==16, w=omg(t,8,7); z=g^((Q-1)/16); for(j=1,15, if((z^j)^2==w, return(z^j))));
  g^((Q-1)/N)};
\\ [invariants, Frobenius columns, Tate exponents m[i][j] = log t_N(p_i, g_j) (reduced), Weil exponent log e_N(p_1, p_2) or -1, ellgroup, check w+1/w]
cdata(ai,p,k,l,N,nm)={my(t=ffgen(p^k,'t),E=ellinit(ai,t),LP=lpart(E,l),os=LP[1],gs=LP[2],r=#os,F,ps,w,Tm,We=-1,Q=p^k);
  F=vector(r,j,coords(E,frob(gs[j],p),os,gs));
  ps=vector(r,i,ellmul(E,gs[i],os[i]/min(os[i],N)));
  w=omg(t,N,nm);
  Tm=if((Q-1)%N==0, vector(r,i,vector(r,j, dlogmu(elltatepairing(E,ps[i],gs[j],N)^((Q-1)/N),w,N))), -1);
  if(r==2 && os[1]>=N && os[2]>=N, We=dlogmu(ellweilpairing(E,ps[1],ps[2],N),w,N));
  [os,F,Tm,We,ellgroup(E),fforder(w)]};
"""


def gp(body):
    r = subprocess.run(["gp", "-q", "-f", "-s", "1000000000"], input=GP_LIB + body, capture_output=True, text=True, timeout=600)
    if r.returncode != 0 or "***" in r.stderr + r.stdout:
        raise RuntimeError(r.stderr + r.stdout)
    return r.stdout


def gp_lines(out):
    d = {}
    for ln in out.splitlines():
        if "|" in ln:
            tag, val = ln.split("|", 1)
            d.setdefault(tag.strip(), []).append(val.strip())
    return d


# ------------------------------------------------------------------------------------------------ lattice helpers
def omega_mat(n):
    return sp.Matrix(sp.BlockMatrix([[sp.zeros(n), sp.eye(n)], [-sp.eye(n), sp.zeros(n)]]))


def invariants(A):
    S = smith_normal_form(sp.Matrix(A), domain=sp.ZZ)
    return sorted(abs(int(S[i, i])) for i in range(min(S.shape)) if abs(int(S[i, i])) != 1)


def quotient_invariants(sub, sup):
    """invariants of (sup Z^m)/(sub Z^m) for full-rank lattices given by basis matrices (rational), sub inside sup"""
    X = sup.inv() * sub
    assert all(x.is_integer for x in X), "not a sublattice"
    return invariants(X)


def step_form(A, B, C, a):
    return sp.Matrix([[(a - B) // 2, -C], [A, (a + B) // 2]])


def vtimes(M, v, D):
    return tuple(int(sum(M[i, j] * v[j] for j in range(len(v)))) % D for i in range(len(v)))


def Om2(v, w):
    return v[0] * w[1] - v[1] * w[0]


class LatGroup:
    """the l-primary part of Fix(M^k) = (1 - M^k)^{-1} L / L for one mode, as integer vectors v mod D (the point v / D)"""

    def __init__(self, M, k, ell):
        self.M, self.k, self.ell = M, k, ell
        self.A = sp.eye(2) - M ** k
        self.h = int(self.A.det())
        e = sp.multiplicity(ell, self.h)
        self.D = D = ell ** e
        A = [[int(self.A[i, j]) for j in range(2)] for i in range(2)]
        self.elts = [(a, b) for a in range(D) for b in range(D)
                     if (A[0][0] * a + A[0][1] * b) % D == 0 and (A[1][0] * a + A[1][1] * b) % D == 0]

    def order(self, v):
        m = 1
        while any((m * x) % self.D for x in v):
            m += 1
        return m

    def act(self, v):
        return vtimes(self.M, v, self.D)

    def add(self, *terms):
        return tuple(sum(c * v[i] for c, v in terms) % self.D for i in range(2))

    def weil_exp(self, v, w, N):
        """e_N exponent: N^2 Omega(v/D, w/D) mod N, for v, w in Fix[N]"""
        x = Fraction(N * N * Om2(v, w), self.D ** 2)
        assert x.denominator == 1
        return int(x) % N

    def tate_exp(self, v, w, N):
        """t_N exponent: N Omega(v/D, (1 - M^k) w / D) mod N, for v in Fix[N], w in Fix"""
        Aw = tuple(int(sum(self.A[i, j] * w[j] for j in range(2))) for i in range(2))
        x = Fraction(N * Om2(v, Aw), self.D ** 2)
        return x

    def basis(self):
        """a basis u_1, u_2 (orders o_1 >= o_2) and the Frobenius columns, as a 'model' like the curve side"""
        n = len(self.elts)
        o1 = max(self.order(v) for v in self.elts)
        u1 = next(v for v in self.elts if self.order(v) == o1)
        o2 = n // o1
        if o2 == 1:
            os, us = [o1], [u1]
        else:
            span1 = {self.add((a, u1)) for a in range(o1)}
            u2 = next(v for v in self.elts if self.order(v) == o2 and
                      all(self.add((b, v)) not in span1 for b in range(1, o2)))
            os, us = [o1, o2], [u1, u2]
        F = [self.coords(self.act(u), os, us) for u in us]
        return os, us, F

    def coords(self, v, os, us):
        for c in itertools.product(*[range(o) for o in os]):
            if self.add(*zip(c, us)) == v:
                return list(c)
        raise ValueError


def equivariant_isos(os, F, G):
    """all phi: (Z/o_1 x Z/o_2 with Frobenius columns F) -> G (a LatGroup) with phi(pi g) = M phi(g), bijective"""
    cands = [[v for v in G.elts if all((o * x) % G.D == 0 for x in v)] for o in os]
    out = []
    for us in itertools.product(*cands):
        ok = True
        for j in range(len(os)):
            if G.act(us[j]) != G.add(*zip(F[j], us)):
                ok = False
                break
        if not ok:
            continue
        # injective (hence bijective, equal orders): no nontrivial combination vanishes
        size = 1
        for o in os:
            size *= o
        if size != len(G.elts):
            continue
        zero = (0, 0)
        inj = all(G.add(*zip(c, us)) != zero for c in itertools.product(*[range(o) for o in os]) if any(c))
        if inj:
            out.append(us)
    return out


def units(N):
    return [s for s in range(1, N) if gcd(s, N) == 1] if N > 1 else [0]


def scales_for(os, Tm, We, G, phis, N, which):
    """for each equivariant iso, the set of units s with curve exponent = s * lattice exponent (mod N); returns (per-phi sets, union)"""
    per = []
    for us in phis:
        ps = [G.add(((o // min(o, N)), u)) for o, u in zip(os, us)]
        S = set()
        for s in units(N):
            if which == "weil":
                r = G.weil_exp(ps[0], ps[1], N)
                good = (We - s * r) % N == 0
            else:
                good = True
                for i in range(len(os)):
                    for j in range(len(os)):
                        x = G.tate_exp(ps[i], us[j], N)
                        if x.denominator != 1:
                            raise ValueError("lattice Tate value not in (1/N)Z")
                        if (Tm[i][j] - s * int(x)) % N:
                            good = False
            if good:
                S.add(s)
        per.append(S)
    union = set().union(*per) if per else set()
    return per, union


# ================================================================================================
print("== S. Structure of the logical group of the level-k code")
Om = omega_mat(1)
E1M = sp.Matrix([[0, -1], [2, -1]])
LAT = {"(1,0,6)": step_form(1, 0, 6, 2), "(2,0,3)": step_form(2, 0, 3, 2)}


def tower_data(M, q, k):
    n = M.shape[0] // 2
    Omn = omega_mat(n)
    I = sp.eye(2 * n)
    V = (q * M.inv()).applyfunc(sp.nsimplify)
    Mk, Vk = M ** k, V ** k
    B = I - Vk                                   # Lam_k basis (columns)
    Pperp = (B.T * Omn).inv()                    # Lam_k^perp basis: Omega(b_j, x) in Z
    def same_lattice(X, Y):
        Z = X.inv() * Y
        return all(x.is_integer for x in Z) and abs(Z.det()) == 1
    same = same_lattice(Pperp, (I - Mk).inv())
    Lin = all(x.is_integer for x in Pperp.inv())  # L inside Lam^perp
    h = int((I - Mk).det())
    return dict(V=V, B=B, Pperp=Pperp, same=same, Lin=Lin, h=h,
                A_inv=quotient_invariants(B, Pperp), phase_inv=quotient_invariants(B, I),
                shift_inv=quotient_invariants(I, Pperp), G_inv=invariants(I - Mk),
                dual_back=same_lattice(B, (Pperp.T * Omn).inv()))


out = gp("".join(f'print("EG|{k}|",ellgroup(ellinit([1,0,0,0,1],ffgen(2^{k},\'t))));\n' for k in range(1, 9))
         + "".join(f'print("E3G|{c}|{k}|",ellgroup(ellinit({ai},ffgen(7^{k},\'t))));\n' for c, ai in (("E4", "[3,3]"), ("E5", "[1,3]")) for k in range(1, 5)))
d = gp_lines(out)
eg = {int(s.split("|")[0]): sorted(eval(s.split("|")[1])) for s in d["EG"]}
e3g = {(s.split("|")[0], int(s.split("|")[1])): sorted(eval(s.split("|")[2])) for s in d["E3G"]}

print("      E1 (q = 2, M = companion of x^2 + x + 2): Lam_k = (1 - V^k)L, Lam_k^perp, Smith invariants")
print("      k  h_k  Lam_k basis (cols)        Lam_k^perp basis (cols)          A_k=Lam^perp/Lam  L/Lam_k  Lam^perp/L  L/(1-M^k)L  PARI E(F_2^k)")
rows = {}
okS1 = okS2 = okS3 = True
for k in range(1, 9):
    T = tower_data(E1M, 2, k)
    rows[k] = T
    okS1 &= T["same"] and T["Lin"] and T["dual_back"]
    okS2 &= T["A_inv"] == [T["h"], T["h"]] and T["phase_inv"] == T["G_inv"] == T["shift_inv"] == [x for x in eg[k] if x != 1]
    okS3 &= ((sp.eye(2) - E1M ** k) * (sp.eye(2) - T["V"] ** k)) == T["h"] * sp.eye(2)
    print(f"      {k}  {T['h']:3d}  {str(T['B'].tolist()):25s} {str(T['Pperp'].tolist()):32s} {str(T['A_inv']):17s} {str(T['phase_inv']):8s} "
          f"{str(T['shift_inv']):11s} {str(T['G_inv']):11s} {eg[k]}")
check("S1 E1, k = 1..8: the Omega-dual of Lam_k = (1 - V^k)L is (1 - M^k)^{-1} L; L lies in it; and (Lam_k^perp)^perp = Lam_k (the commutator form is "
      "non-degenerate on A_k)", okS1)
check("S2 E1, k = 1..8: L/Lam_k (phases), Lam_k^perp/L (shifts = periodic syndromes), L/(1 - M^k)L and PARI's E(F_{2^k}) have the same invariants; "
      "A_k = Lam_k^perp/Lam_k has invariants [h_k, h_k]", okS2)
check("S3 one mode: (1 - M^k)(1 - V^k) = h_k * 1, so A_k = (1 - M^k)^{-1}L/(1 - V^k)L ~ L/h_k L = (Z/h_k)^2 with commutator Omega/h_k: "
      "the logical group of C_k is the Pauli group of one qudit of dimension h_k", okS3)
okE3 = True
for nm_, M in LAT.items():
    for k in range(1, 5):
        T = tower_data(M, 7, k)
        okE3 &= T["same"] and T["Lin"] and T["A_inv"] == [T["h"], T["h"]]
        okE3 &= T["phase_inv"] == T["G_inv"] == [x for x in e3g[("E4", k)] if x != 1] == [x for x in e3g[("E5", k)] if x != 1]
check("S4 E3 lattices (1,0,6), (2,0,3), k = 1..4: same statements; phases, shifts and PARI's E4(F_{7^k}), E5(F_{7^k}) all have invariants "
      "[6], [2,30], [3,126], [20,120]", okE3)
# Lagrangian
okL = True
for k in range(1, 9):
    T = rows[k]
    okL &= len(T["phase_inv"]) <= 2 and sp.prod(T["phase_inv"]) ** 2 == sp.prod(T["A_inv"])
check("S5 L/Lam_k is isotropic (Omega is integral on L) and |L/Lam_k|^2 = |A_k|: the phase group is a Lagrangian subgroup, and the commutator "
      "pairs phases perfectly with shifts (phases = characters of the points)", okL)
# split / non-split
split = {k: sorted(rows[k]["A_inv"]) == sorted(rows[k]["G_inv"] * 2) or (len(rows[k]["G_inv"]) == 1 and rows[k]["A_inv"] == rows[k]["G_inv"] * 2)
         for k in range(1, 9)}
# direct test at k = 8: no lift of an order-3 shift has order 3 in A_8
T8 = rows[8]
a3 = sp.Matrix([0, sp.Rational(1, 3)])          # a shift of order 3: (1 - M^8) a3 is in L, a3 is not
assert all(x.is_integer for x in (sp.eye(2) - E1M ** 8) * a3)
# 3 (a3 + l) in Lam_8 for some l in L  <=>  3 a3 in Lam_8 + 3 L  <=>  B y = 3 a3 mod 3 for some y in (Z/3)^2
B8 = T8["B"]
nolift = a3 is not None and all(x.is_integer for x in 3 * a3) and not any(
    all(((B8 * sp.Matrix([y1, y2]) - 3 * a3)[i]) % 3 == 0 for i in range(2)) for y1 in range(3) for y2 in range(3))
check("S6 A_k = G_k x G_k^dual (a split Heisenberg group of the points) iff G_k is cyclic: true for E1, k = 1..7; false at k = 8, where "
      "G_8 = Z3 x Z96 but A_8 = (Z/288)^2, and no lift of an order-3 shift has order 3 in A_8 (its cube is a non-trivial logical phase)",
      all(split[k] for k in range(1, 8)) and not split[8] and nolift, f"A_8 invariants {T8['A_inv']}, G_8 {T8['G_inv']}")
# K4 with one negative edge, n = 4, k = 1
A4 = sp.ones(4, 4) - sp.eye(4)
A4[0, 1] = A4[1, 0] = -1
MK = sp.Matrix(sp.BlockMatrix([[sp.zeros(4), -sp.eye(4)], [2 * sp.eye(4), A4]]))
TK = tower_data(MK, 2, 1)
check("S7 K4 with one negative edge (n = 4), k = 1: Lam^perp = (1 - M)^{-1} L, L inside it; A_1 = (1-M)^{-1}L/(1-V)L",
      TK["same"] and TK["Lin"] and sp.prod(TK["A_inv"]) == TK["h"] ** 2,
      f"G_1 = {TK['G_inv']}, A_1 = {TK['A_inv']}, split: {sorted(TK['A_inv']) == sorted(TK['G_inv'] * 2)}")

# ================================================================================================
print("\n== L. The two pairings on the lattice side (no curve)")
# Tate on the lattice is well defined on Fix[N] x Fix/N iff N | q^k - 1
def tate_well_defined(M, q, k, N):
    G = LatGroup(M, k, sp.factorint(N).popitem()[0])
    PN = [v for v in G.elts if all((N * x) % G.D == 0 for x in v)]
    # shifting Q by a lattice vector l (Q~ -> Q~ + l): change is N Omega(P~, (1-M^k) l), must be 0 mod N
    for v in PN:
        for l in ((1, 0), (0, 1)):
            Al = tuple(int(sum(G.A[i, j] * l[j] for j in range(2))) for i in range(2))
            x = Fraction(N * Om2(v, Al), G.D)
            if x.denominator != 1 or int(x) % N:
                return False
    return True


cases_wd = [(E1M, 2, 1, 2), (E1M, 2, 2, 2), (E1M, 2, 4, 4), (E1M, 2, 6, 7), (E1M, 2, 8, 3), (LAT["(1,0,6)"], 7, 2, 4), (LAT["(2,0,3)"], 7, 4, 8)]
res = [(k, N, (q ** k - 1) % N == 0, tate_well_defined(M, q, k, N)) for M, q, k, N in cases_wd]
check("L1 the lattice Tate form Omega(P~, (1 - M^k) Q~) is well defined on Fix[N] x Fix/N exactly when N | q^k - 1 (the lattice shadow of mu_N in F_{q^k}): "
      "ill-defined for E1 at (k,N) = (1,2), (2,2), (4,4), well-defined at (6,7), (8,3) and for E3 at (2,4), (4,8)",
      all(a == b for _, _, a, b in res), str(res))
# Weil: E[N] inside Fix(M^k) forces q^k = 1 mod N, and the pairing is Galois-equivariant with factor q
okW = True
for M, q, k, N in ((LAT["(1,0,6)"], 7, 8, 8), (LAT["(2,0,3)"], 7, 4, 4), (E1M, 2, 8, 3)):
    G = LatGroup(M, k, sp.factorint(N).popitem()[0])
    EN = [v for v in G.elts if all((N * x) % G.D == 0 for x in v)]
    okW &= len(EN) == N * N and (q ** k - 1) % N == 0
    okW &= all(G.weil_exp(G.act(v), G.act(w), N) == (q * G.weil_exp(v, w, N)) % N for v in EN[:20] for w in EN[:20])
check("L2 E[N] inside Fix(M^k) (E3 at (k,N) = (8,8), (4,4); E1 at (8,3)) and q^k = 1 mod N; the code-side Weil form c(N P~, Q~) = exp(2 pi i N Omega(P~,Q~)) "
      "is well defined on E[N] (independent of the lifts) and scales by q under the step", okW)

# ================================================================================================
print("\n== C. Curve against code: Frobenius-equivariant isomorphisms E(F_{q^k})_l -> Fix(M^k)_l and the two pairings")
CASES = []  # (tag, curve ai, p, k, ell, N, nm, lattice name, M)
for k, ell, N in ((6, 7, 7), (8, 3, 3)):
    CASES.append((f"E1 k={k} N={N}", "[1,0,0,0,1]", 2, k, ell, N, 0, "companion", E1M))
E3C = {"E4": "[3,3]", "E5": "[1,3]"}
E3K = [(1, 2, 2), (1, 3, 3), (2, 2, 2), (2, 2, 4), (3, 3, 3), (4, 2, 4), (4, 2, 8), (8, 2, 8), (16, 2, 16)]
for cname, ai in E3C.items():
    for k, ell, N in E3K:
        for lname, M in LAT.items():
            CASES.append((f"{cname} k={k} N={N} vs {lname}", ai, 7, k, ell, N, 7, lname, M))
# the other root-of-unity normalisation at N = 8
for cname, ai in E3C.items():
    for lname, M in LAT.items():
        CASES.append((f"{cname} k=8 N=8 vs {lname} [iota']", ai, 7, 8, 2, 8, -7, lname, M))

need = sorted({(ai, p, k, ell, N, nm) for _, ai, p, k, ell, N, nm, _, _ in CASES})
out = gp("".join(f'print("CD|{i}|",cdata({ai},{p},{k},{ell},{N},{nm}));\n' for i, (ai, p, k, ell, N, nm) in enumerate(need)))
cd = {}
for s in gp_lines(out)["CD"]:
    i, v = s.split("|", 1)
    cd[need[int(i)]] = eval(v)

LG = {}
RESULTS = {}
for tag, ai, p, k, ell, N, nm, lname, M in CASES:
    os, F, Tm, We, grp, wo = cd[(ai, p, k, ell, N, nm)]
    key = (lname, k, ell)
    if key not in LG:
        LG[key] = LatGroup(M, k, ell)
    G = LG[key]
    phis = equivariant_isos(os, F, G)
    rw = scales_for(os, Tm, We, G, phis, N, "weil") if We != -1 else None
    rt = scales_for(os, Tm, We, G, phis, N, "tate") if Tm != -1 else None
    RESULTS[tag] = dict(os=os, F=F, nphi=len(phis), weil=rw, tate=rt, wo=wo, grp=grp)
    fmt = lambda r: "-" if r is None else (str(sorted(r[1])) + ("" if all(r[0]) else " (some phi match no s)"))
    print(f"      {tag:34s} E_l = {str(os):9s} Frob cols {str(F):22s} #equivariant isos {len(phis):4d}   Weil scales {fmt(rw):10s}  Tate scales {fmt(rt)}")

allmatch = all(r["nphi"] > 0 and (r["weil"] is None or all(r["weil"][0])) and (r["tate"] is None or all(r["tate"][0])) for r in RESULTS.values())
check("C1 in every case there are Frobenius-equivariant isomorphisms E(F_{q^k})_l -> Fix(M^k)_l, and for EACH of them the PARI Weil and Tate pairings equal the "
      "code-side forms c(N P~, Q~) and c(P~, (1-M^k) Q~) up to a unit s (an automorphism of mu_N): the commutator form is the pairing, up to Aut(mu_N)",
      allmatch, f"{len(RESULTS)} cases")
check("C2 roots of unity: the chosen w has exact order N in every case", all(r["wo"] == int(t.split("N=")[1].split()[0]) for t, r in RESULTS.items()))

def S(tag, which):
    r = RESULTS[tag][which]
    return sorted(r[1])

print("\n      decisive table, N = 8 (iota: w + 1/w = 3 -> exp(2 pi i/8)); entries are scale sets s (curve exponent = s * code exponent)")
print("                        Weil, k = 8        Tate, k = 8        Tate, k = 4")
for c in ("E4", "E5"):
    for l in ("(1,0,6)", "(2,0,3)"):
        print(f"      {c} vs {l}:     {str(S(f'{c} k=8 N=8 vs {l}', 'weil')):18s} {str(S(f'{c} k=8 N=8 vs {l}', 'tate')):18s} {S(f'{c} k=4 N=8 vs {l}', 'tate')}")
diag = all(S(f"{c} k={k} N=8 vs {l}", w) in ([1, 7], [3, 5]) for c in ("E4", "E5") for l in LAT for k, w in ((8, "weil"), (8, "tate"), (4, "tate")))
match = {(c, l): all(set(S(f"{c} k={k} N=8 vs {l}", w)) & {1, 7} for k, w in ((8, "weil"), (8, "tate"), (4, "tate"))) for c in ("E4", "E5") for l in LAT}
check("C3 (decisive) N = 8: with iota fixed, E5 matches (1,0,6) and E4 matches (2,0,3) with scale +-1 (scale set {1,7}); the crossed pairs need scale 3 or 5. "
      "Same for the Weil pairing on E[8] (k = 8) and the Tate pairing at k = 8 and already at k = 4, where E[8] is not rational",
      diag and match == {("E5", "(1,0,6)"): True, ("E4", "(2,0,3)"): True, ("E5", "(2,0,3)"): False, ("E4", "(1,0,6)"): False})
check("C4 this agrees with overlap-data.md criterion 2 (j-invariant route): eps(sqrt 2) = +sqrt 2 for the 7-adic sqrt 2 = 3 makes j = 5 the principal curve; "
      "here the same eps, entering only through iota, makes E5 the curve whose Weil/Tate pairing is the commutator form of the (1,0,6) code",
      match[("E5", "(1,0,6)")] and not match[("E5", "(2,0,3)")])
swap = all(S(f"{c} k=8 N=8 vs {l} [iota']", "weil") == ([3, 5] if S(f"{c} k=8 N=8 vs {l}", "weil") == [1, 7] else [1, 7]) for c in E3C for l in LAT)
check("C5 with the other normalisation iota' (w + 1/w = 4 -> exp(2 pi i/8), i.e. eps(sqrt 2) = -sqrt 2) the assignment swaps: E4 <-> (1,0,6), E5 <-> (2,0,3)", swap)
lowN = all(set(S(f"{c} k={k} N={N} vs {l}", w)) & {1, N - 1} for c in E3C for l in LAT for k, N, w in
           ((1, 2, "tate"), (2, 2, "tate"), (2, 2, "weil"), (2, 4, "tate"), (4, 4, "weil"), (4, 4, "tate")))
check("C6 at N = 2, 4 every curve matches every lattice with scale +-1 (Aut(mu_4) = {+-1}): these levels cannot separate the classes", lowN)
n3 = {(c, l): (S(f"{c} k=3 N=3 vs {l}", "weil"), S(f"{c} k=3 N=3 vs {l}", "tate"), S(f"{c} k=1 N=3 vs {l}", "tate")) for c in E3C for l in LAT}
check("C7 N = 3: every scale set is a single sign; E5-(1,0,6) and E4-(2,0,3) carry the same sign, the crossed pairs the opposite one "
      "(separation only once the orientation of Omega is fixed, as overlap-data.md section 4 found)",
      n3[("E5", "(1,0,6)")] == n3[("E4", "(2,0,3)")] and all(len(x) == 1 for v in n3.values() for x in v)
      and all({n3[("E5", "(1,0,6)")][i][0], n3[("E5", "(2,0,3)")][i][0]} == {1, 2} for i in range(3)), str(n3))
n16 = {(c, l): S(f"{c} k=16 N=16 vs {l}", "weil") for c in E3C for l in LAT}
check("C8 N = 16 (Weil, k = 16): matched pairs have scales {1,7,9,15}, crossed pairs {3,5,11,13}", 
      n16[("E5", "(1,0,6)")] == n16[("E4", "(2,0,3)")] == [1, 7, 9, 15] and n16[("E4", "(1,0,6)")] == n16[("E5", "(2,0,3)")] == [3, 5, 11, 13], str(n16))
e1 = (RESULTS["E1 k=6 N=7"], RESULTS["E1 k=8 N=3"])
sq7 = {1, 2, 4}
t7 = set(e1[0]["tate"][1])
check("C9 E1: the first levels with a non-trivial Tate pairing are k = 6 (N = 7, E(F_64) = Z56, E(F_64)[7] cyclic) and k = 8 (N = 3, E[3] rational). "
      "Both match the code forms up to Aut(mu_N). At N = 7 the 6 equivariant isomorphisms realise one coset of the squares (with the unnormalised root used here: "
      "the non-squares {3, 5, 6}); at N = 3 both signs occur. E1 has class number 1, so there is no class to separate",
      e1[0]["nphi"] == 6 and (t7 == sq7 or t7 == {3, 5, 6}) and sorted(e1[1]["tate"][1]) == [1, 2] and sorted(e1[1]["weil"][1]) == [1, 2]
      and [k for k in range(1, 9) if gcd(int((sp.eye(2) - E1M ** k).det()), 2 ** k - 1) > 1] == [6, 8], f"N = 7 scales {sorted(t7)}")
print(f"      N = 3 signs (Weil k=3, Tate k=3, Tate k=1): {n3}")
check("C10 Weil and Tate give the same scale sets at N = 8 and N = 16; at N = 3 the Weil sign is +1 and the Tate sign -1 for the matched pairs "
      "(t_N = c(P~, (M^k - 1) Q~) when e_N = c(N P~, Q~); a convention constant, the same for both curves)",
      all(S(f"{c} k={k} N={k} vs {l}", "weil") == S(f"{c} k={k} N={k} vs {l}", "tate") for c in E3C for l in LAT for k in (8, 16))
      and n3[("E5", "(1,0,6)")] == ([1], [2], [2]))

# ================================================================================================
print("\n== K. Code against code: the two steps on the same (L, Omega)")
def lat_model(M, k, ell, N):
    G = LatGroup(M, k, ell)
    os, us, F = G.basis()
    ps = [G.add(((o // min(o, N)), u)) for o, u in zip(os, us)]
    We = G.weil_exp(ps[0], ps[1], N) if len(os) == 2 and min(os) >= N else -1
    Tm = [[int(G.tate_exp(ps[i], us[j], N)) % N for j in range(len(os))] for i in range(len(os))]
    return os, F, Tm, We


kk = {}
for k, N in ((8, 8), (4, 8), (16, 16)):
    for a in LAT:
        os, F, Tm, We = lat_model(LAT[a], k, 2, N)
        for b in LAT:
            key = (LAT[b] is LAT[b], b, k)
            G = LG.get((b, k, 2)) or LatGroup(LAT[b], k, 2)
            phis = equivariant_isos(os, F, G)
            rw = scales_for(os, Tm, We, G, phis, N, "weil") if We != -1 else None
            rt = scales_for(os, Tm, We, G, phis, N, "tate")
            kk[(a, b, k, N)] = (len(phis), None if rw is None else sorted(rw[1]), sorted(rt[1]))
            print(f"      k = {k:2d}, N = {N:2d}: code {a} -> code {b}: {len(phis):4d} step-equivariant isomorphisms of the shift groups; "
                  f"Weil-form scales {kk[(a, b, k, N)][1]}, Tate-form scales {kk[(a, b, k, N)][2]}")
check("K1 step-equivariant isomorphisms between the shift groups of the (1,0,6) and (2,0,3) codes exist at every level, but scale the code's "
      "commutator-derived forms by 3 or 5 mod 8 (never +-1); from a code to itself the scales are {1, 7}",
      all(kk[(a, b, k, 8)][2] == ([1, 7] if a == b else [3, 5]) for a in LAT for b in LAT for k in (8, 4))
      and all(kk[(a, b, 8, 8)][1] == ([1, 7] if a == b else [3, 5]) for a in LAT for b in LAT)
      and all(kk[(a, b, 16, 16)][1] == ([1, 7, 9, 15] if a == b else [3, 5, 11, 13]) for a in LAT for b in LAT))
# arbitrary (non-equivariant) group isomorphisms: every scale occurs
dets8 = {int(sp.Matrix([[a, b], [c, e]]).det()) % 8 for a, b, c, e in itertools.product(range(8), repeat=4)
         if gcd(int(sp.Matrix([[a, b], [c, e]]).det()), 8) == 1}
check("K2 without equivariance every unit scale is realised by some group isomorphism (det over GL2(Z/8) = all units): the separation needs the step",
      dets8 == {1, 3, 5, 7})
# intertwiners mod 8 (as in overlap-data.md T2)
idets = {int((g.det()) % 8) for g in (sp.Matrix([[a, b], [c, e]]) for a, b, c, e in itertools.product(range(8), repeat=4))
         if gcd(int(g.det()), 8) == 1 and all(x % 8 == 0 for x in (g * LAT["(1,0,6)"] - LAT["(2,0,3)"] * g))}
check("K3 consistency with overlap-data.md T2: det of intertwiners g M_(1,0,6) = M_(2,0,3) g mod 8 is {3, 5}", idets == {3, 5})

print(f"\n{npass} of {npass + nfail} pass   ({time.time() - T0:.1f} s)")
