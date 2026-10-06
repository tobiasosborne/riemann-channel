"""REFUTE scratch (scope of ff-dirichlet.md 2.3-2.6): q=5, N=4, f = t^4+1 = (t^2+2)(t^2+3) (the Fermat quartic
y^4 = t^4 + 1). P_chi has a repeated root although RH holds: E is not reduced, Tr(x sigma y) is degenerate,
F is not semisimple on R, so no vacuum; while on H_1 of the curve Frobenius is semisimple."""
import sympy as sp
from scratch_gkp_ffm_lattice import exact_Lambda, Alg, analyse
from scratch_gkp_ffm_core import Char
from scratch_gkp_ffm_curves import count
from scratch_gkp_ffm_phases import global_W
import mpmath as mp
q, N, Ps = 5, 4, [[2, 0, 1], [3, 0, 1]]
ch = Char(q, N, Ps); Lam, even = exact_Lambda(ch)
print('exact Lambda coefficients in Z[i] (c_k = a + b i):', Lam, ' even:', even)
i = sp.I; c = [a + b*i for a, b in Lam]; x = sp.Symbol('x')
P = sp.expand(sum(ck*x**(len(c)-1-k) for k, ck in enumerate(c)))
print('P_chi(x) =', P, ' = ', sp.factor(P, extension=sp.I), ' discriminant', sp.simplify(sp.discriminant(P, x)), ' |root|^2 =', sp.simplify(abs(sp.solve(P, x)[0])**2))
A, B, T = analyse('Fermat', q, N, Ps)
print('det of Tr(x sigma y) on R:', T.det(), '; rank', T.rank(), 'of', T.shape[0])
MF = A.mulmat(A.x); alpha = sp.solve(P, x)[0]
# semisimplicity of F on E over Q: minimal polynomial of the 4x4 integer matrix
cp = sp.factor((x*sp.eye(4)-MF).det()); print('charpoly_Q(F|E) =', cp)
m2 = (MF**2 + 2*MF + 5*sp.eye(4))   # x^2+2x+5 is the Q-minimal polynomial of -(1+2i)
print('F semisimple on E?  (F^2+2F+5) == 0 :', m2 == sp.zeros(4))
# the curve: y^4 = c f with c^{(q-1)/N} = (-1)^{(q-1)d/N} = 1 -> c = 1
f = [1, 0, 0, 0, 1]
print('point counts of y^4 = t^4+1 over F_5^r, r=1..3:', [count(5, 4, f, 1, r) for r in (1, 2, 3)])
