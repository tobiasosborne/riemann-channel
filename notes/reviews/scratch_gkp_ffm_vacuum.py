"""REFUTE scratch (ff-dirichlet.md 2.4 C5 and 3.2 B5): the vacuum J = (F-V)(4q-(F+V)^2)^{-1/2} on R with Omega_+,
and the CRT factorisation G = chi_1(P_2) chi_2(P_1) G_1 G_2 of the global Gauss sum for X2."""
import numpy as np, sympy as sp
from scipy.linalg import sqrtm
from scratch_gkp_ffm_lattice import exact_Lambda, Alg, lattice_hnf
from scratch_gkp_ffm_phases import EX, C, psi0
from scratch_gkp_ffm_core import *
for name, (q, N, Ps) in EX.items():
    ch = Char(q, N, Ps); Lam, even = exact_Lambda(ch); A = Alg(N, Lam, q); D = A.D
    Mz = A.mulmat(A.z); MF = A.mulmat(A.x); MV = q*MF.inv(); e0 = sp.Matrix([1]+[0]*(D-1)); Mzi = Mz.inv()
    Sig = sp.Matrix.hstack(*[(Mzi**a)*(MV**b)*e0 for (a, b) in A.basis])
    B = lattice_hnf([e0])
    for _ in range(6): B = lattice_hnf([B[:, j] for j in range(B.cols)] + [X*B[:, j] for X in (Mz, MF, MV) for j in range(B.cols)])
    mult = lambda v: A.mulmat(A.elt(v)); VmFi = (MV-MF).inv()
    Om = np.array(sp.Matrix(D, D, lambda i, j: mult(mult(B[:, i])*VmFi*Sig*B[:, j]).trace()), dtype=float)
    Fr = np.array(B.inv()*MF*B, dtype=float); Vr = np.array(B.inv()*MV*B, dtype=float); Zr = np.array(B.inv()*Mz*B, dtype=float)
    S = Fr+Vr; J = (Fr-Vr)@np.real(np.linalg.inv(sqrtm(4*q*np.eye(D)-S@S)))
    G = Om@J
    print(f'{name}: spec(F+V) real in (-2sqrt q, 2sqrt q): {np.all(np.abs(np.linalg.eigvals(S).imag) < 1e-9) and np.max(np.abs(np.linalg.eigvals(S))) < 2*np.sqrt(q)};'
          f' J^2=-1 {np.allclose(J@J, -np.eye(D))}, JF=FJ {np.allclose(J@Fr, Fr@J)}, Jz=zJ {np.allclose(J@Zr, Zr@J)}, Om J sym {np.allclose(G, G.T, atol=1e-10)}, min eig {np.linalg.eigvalsh(0.5*(G+G.T)).min():.3f}')
# B5 for X2
q, N, Ps = EX['X2']; ch = Char(q, N, Ps)
def G_P(i):
    P = Ps[i]; s = 0
    for a in polys_below(len(P)-1, q):
        k = ch.comp(trim(a), i)
        if k is not None: s += C(ch, k)*psi0(a[-1], q)
    return s
Gg = 0
for a in polys_below(ch.d, q):
    k = ch(trim(a))
    if k is not None: Gg += C(ch, k)*psi0(a[-1], q)
fac = C(ch, ch.comp(Ps[1], 0))*C(ch, ch.comp(Ps[0], 1))*G_P(0)*G_P(1)
print('X2: G =', mp.nstr(Gg, 8), ' chi1(P2)chi2(P1)G1G2 =', mp.nstr(fac, 8), ' diff', mp.nstr(abs(Gg-fac), 3))
