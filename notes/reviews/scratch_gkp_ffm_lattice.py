"""REFUTE scratch (ff-dirichlet.md section 2, J3): the algebra E = Q(zeta_N)[x]/(P_chi), the order R = Z[zeta][F,V]
(my own closure + HNF), the involution sigma, index [R : Z[zeta][F]], the trace form Tr(x sigma y), its Weil form,
Omega_+ = Tr(x sigma(y)/(V-F)) with denominators and Smith invariants, charpoly_Z(F|R), ordinarity, det_Z F.
Exact rational arithmetic (sympy). Written from the statements only."""
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
from scratch_gkp_ffm_core import Char, Lcoeffs, monics
from scratch_gkp_ffm_phases import EX
from functools import reduce

def zeta_coeffs(vec, N):
    """group-ring vector over mu_N -> coefficients on 1..z^{phi-1} mod Phi_N"""
    z = sp.Symbol('z'); Phi = sp.Poly(sp.cyclotomic_poly(N, z), z)
    pol = sp.Poly(sum(int(vec[k])*z**k for k in range(N)), z).rem(Phi)
    phi = Phi.degree(); c = pol.all_coeffs()[::-1]
    return [sp.Integer(c[i]) if i < len(c) else sp.Integer(0) for i in range(phi)]

def exact_Lambda(ch):
    S = Lcoeffs(ch); N = ch.N
    L = [zeta_coeffs(s, N) for s in S[:ch.d]]
    even = all(ch.on_const(c) == 0 for c in range(1, ch.q))
    if even:
        Lam = []; acc = [0]*len(L[0])
        for k in range(len(L)-1):
            acc = [a+b for a, b in zip(acc, L[k])]; Lam.append(list(acc))
        assert all(x == 0 for x in [a+b for a, b in zip(acc, L[-1])])
    else: Lam = L
    while all(x == 0 for x in Lam[-1]): Lam.pop()
    return Lam, even

class Alg:
    def __init__(self, N, Pcoef, q):
        """Pcoef[k] in Z[z] (coeff lists), P_chi(x) = sum_k c_k x^{n-k}, c_0 = 1"""
        self.z, self.x = sp.symbols('z x'); z, x = self.z, self.x
        self.N, self.q = N, q
        self.Phi = sp.cyclotomic_poly(N, z) if N > 2 else (z+1 if N == 2 else z-1)
        self.phi = sp.degree(self.Phi, z)
        self.n = len(Pcoef)-1
        self.P = sp.expand(sum(sum(c[i]*z**i for i in range(len(c)))*x**(self.n-k) for k, c in enumerate(Pcoef)))
        self.D = self.phi*self.n
        self.basis = [(a, b) for b in range(self.n) for a in range(self.phi)]
    def red(self, e):
        z, x = self.z, self.x
        e = sp.rem(sp.expand(e), self.P, x) if self.n > 0 else e
        e = sp.expand(e); out = 0
        for b in range(self.n):
            cb = sp.expand(e).coeff(x, b)
            out += sp.rem(cb, self.Phi, z)*x**b
        return sp.expand(out)
    def vec(self, e):
        e = self.red(e); z, x = self.z, self.x
        return sp.Matrix([sp.expand(e.coeff(x, b)).coeff(z, a) for (a, b) in self.basis])
    def elt(self, v): return sum(v[i]*self.z**a*self.x**b for i, (a, b) in enumerate(self.basis))
    def mulmat(self, e):
        return sp.Matrix.hstack(*[self.vec(e*self.z**a*self.x**b) for (a, b) in self.basis])

def lattice_hnf(cols):
    """Z-span of rational column vectors -> basis matrix (columns)"""
    M = sp.Matrix.hstack(*cols); den = reduce(sp.ilcm, [sp.fraction(x)[1] for x in M], 1)
    Mi = (M*den).applyfunc(sp.Integer)
    H = hermite_normal_form(Mi)
    H = H[:, [j for j in range(H.cols) if any(H[i, j] != 0 for i in range(H.rows))]]
    return H/den

def analyse(name, q, N, Ps):
    ch = Char(q, N, Ps); Lam, even = exact_Lambda(ch)
    A = Alg(N, Lam, q); D, n = A.D, A.n
    Mz = A.mulmat(A.z); MF = A.mulmat(A.x); MV = q*MF.inv()
    # sigma: z^a F^b -> z^{-a} V^b
    e0 = sp.Matrix([1]+[0]*(D-1))
    Mzi = Mz.inv()
    Sig = sp.Matrix.hstack(*[(Mzi**a)*(MV**b)*e0 for (a, b) in A.basis])
    hom = (Sig*MF == MV*Sig) and (Sig*Mz == Mzi*Sig) and (Sig*Sig == sp.eye(D))
    # R = Z[z][F,V]: closure of Z*1 under z, F, V
    B = lattice_hnf([e0])
    while True:
        B2 = lattice_hnf([B[:, j] for j in range(B.cols)] + [X*B[:, j] for X in (Mz, MF, MV) for j in range(B.cols)])
        if B2.cols == B.cols and abs(B2.det()) == abs(B.det()) if B2.cols == D and B.cols == D else False: break
        B = B2
    index = 1/abs(B.det())      # Z[z][F] = standard lattice
    def mult(v): return A.mulmat(A.elt(v))
    def Tr(v): return mult(v).trace()
    T = sp.Matrix(D, D, lambda i, j: Tr(mult(B[:, i])*Sig*B[:, j]))
    VmF_inv = (MV-MF).inv()
    Om = sp.Matrix(D, D, lambda i, j: Tr(mult(B[:, i])*VmF_inv*Sig*B[:, j]))
    den = reduce(sp.ilcm, [sp.fraction(x)[1] for x in Om], 1)
    Omi = (Om*den).applyfunc(sp.Integer); g = reduce(sp.igcd, list(Omi)); Omp = Omi/g
    snf = smith_normal_form(Omp)
    ed = sorted([abs(snf[i, i]) for i in range(D)])
    # checks on Omega_+: alternating, similitude in R-basis
    MFR = B.inv()*MF*B; MzR = B.inv()*Mz*B
    alt = (Om.T == -Om); sim = (MFR.T*Om*MFR == q*Om); zinv = (MzR.T*Om*MzR == Om)
    Wform = T/2
    minorsT = [T[:k, :k].det() for k in range(1, D+1)]
    I = sp.eye(D)
    Tc = sp.Matrix(D, D, lambda i, j: Tr(mult(I[:, i])*Sig*I[:, j]))
    print('   [companion basis Z[z][F]] Tr(x sigma y) leading minors', [Tc[:k, :k].det() for k in range(1, D+1)], ' R basis (cols):', B.T.tolist())
    import numpy as np
    evn = np.linalg.eigvalsh(np.array(Wform.evalf(), dtype=float))
    x = sp.Symbol('x'); cp = sp.Poly((x*sp.eye(D)-MF).det(), x)
    cpc = cp.all_coeffs()
    mid = cpc[D//2]
    print(f'{name}: P_chi coeffs (in Z[z]) {Lam}; D={D}, n={n}')
    print(f'   sigma ring involution: {hom};  R closed, [R:Z[z][F]] = {index};  companion V-integral: {all(v.q == 1 for v in MV)}')
    print(f'   trace form Tr(x sigma y): leading minors {minorsT}; det(Weil form = Tr/2) = {Wform.det()}; min eig Weil {evn.min():.4f}')
    print(f'   Omega_+: alternating {alt}, z-invariant {zinv}, q-similitude {sim}; denominator {den//sp.igcd(den, g) if True else den}, Smith of primitive multiple {ed}')
    print(f'   charpoly_Z(F|R) = {cp.as_expr()}; middle coeff {mid} mod p = {mid % q} -> ordinary {mid % q != 0}; det_Z F = {MF.det()} vs q^(D/2) = {sp.Integer(q)**sp.Rational(D, 2)}')
    return A, B, T

if __name__ == '__main__':
    for name, (q, N, Ps) in EX.items():
        analyse(name, q, N, Ps)
    # control C7: x^2 - 6x + 5, q = 5, N = 1
    A = Alg(1, [[1], [-6], [5]], 5)
    MF = A.mulmat(A.x); MV = 5*MF.inv(); e0 = sp.Matrix([1, 0])
    Sig = sp.Matrix.hstack(e0, MV*e0)
    T = sp.Matrix(2, 2, lambda i, j: A.mulmat(A.elt(A.mulmat(A.elt(sp.eye(2)[:, i]))*Sig*sp.eye(2)[:, j])).trace())
    print('C7 control: Tr(x sigma y) on Z[F]:', T.tolist(), 'minors', T[0, 0], T.det(), '; sigma hom', Sig*MF == MV*Sig)
