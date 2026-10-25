"""Finite obstructions and a high-precision check of the missing conjugation bars.

No number-field L-function zero is used. Floating Gauss-sum checks are numerical,
not interval certificates; the support, matrix and polynomial checks are exact.
"""
import sympy as s
import mpmath as mp

z = s.symbols('z')
M = s.Matrix([[5, -5], [1, 0]])
Omega = s.Matrix([[0, 1], [-1, 0]])
assert M.T*Omega*M == 5*Omega
print("Integral rank-two counterexample: M =", list(M))
print("M.T Omega M - 5 Omega =", list(M.T*Omega*M-5*Omega))
print("Eigenvalues = (5 +/- sqrt(5))/2; larger/sqrt(5) = (1+sqrt(5))/2 > 1")

# All-negative K4 flux, q=2; graph zeta reciprocal, not an L numerator.
P = s.Poly((1-z*z)**2*(1+3*z+2*z*z)*(1-z+2*z*z)**3, z)
assert P.degree() == 12 and P.eval(-s.Rational(1, 2)) == 0
assert P.nth(13) == 0
print("K4 all-negative reciprocal Ihara polynomial degree =", P.degree())
print("P(-1/2) =", P.eval(-s.Rational(1, 2)), "; coefficient z^13 =", P.nth(13))
print("Thus eventual coefficient cancellation does not exclude an off-circle pole at z=-1/2.")

mp.mp.dps = 80
omega = mp.exp(2j*mp.pi/3)
pi = -2-3*omega  # norm 7, primary; omega reduces to 4 modulo pi.
residues = {}
for sign in [1, -1]:
    for j in range(3):
        residues[(sign*pow(4, j, 7)) % 7] = sign*omega**j
assert len(residues) == 6
def chi(x):
    return residues[x % 7] if x % 7 else mp.mpc(0)
def gauss(j):
    return sum(chi(x)**j*mp.exp(2j*mp.pi*3*x/7) for x in range(1, 7))/mp.sqrt(7)
alpha = pi/mp.sqrt(7)
G = mp.conj(chi(4))*gauss(3)
lhs = -gauss(-1)
rhs = chi(-1)/G*mp.conj(alpha)*gauss(2)
wrong = chi(-1)/(chi(4)*gauss(3))*alpha*gauss(2)
err = abs(lhs-rhs)
assert err < mp.mpf('1e-75') and abs(lhs-wrong) > mp.mpf('0.1')
print("Gauss identity numerical precision = 80 decimal digits")
print("Correct conjugated identity residual =", mp.nstr(err, 10))
print("Unconjugated brief identity residual =", mp.nstr(abs(lhs-wrong), 30))
print("Cubic charge support over F7 = 6; prime-qudit stabilizer supports = {1,7}.")
exponents = [-1, 1]
haar_energy = sum(a == b for a in exponents for b in exponents)
print("F(z)=z+z^-1 Haar energy =", haar_energy)
for N in [2, 3, 6]:
    energy = sum((a-b) % N == 0 for a in exponents for b in exponents)
    print(f"F(z)=z+z^-1 torsion energy, N={N}: {energy}")
    assert energy == (4 if N == 2 else 2)
print("All structural checks passed.")
