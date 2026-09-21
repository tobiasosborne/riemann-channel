"""Exact sanity checks for counterexamples; the note contains independent proofs."""
import sympy as s

z = s.symbols("z")
I = s.I
X = s.Matrix([[0, 1], [1, 0]])
Y = s.Matrix([[0, -I], [I, 0]])
P = s.diag(1, -1)
rev = [1, 0, 3, 2]

def hashimoto(letters):
    n = letters[0].rows
    return s.BlockMatrix([
        [letters[i] if j != rev[i] else s.zeros(n) for i in range(4)]
        for j in range(4)
    ]).as_explicit()

# T1(b): ordinary nullities do not have the advertised index.
A = s.Matrix([[1, s.Rational(3, 2)], [s.Rational(3, 4), 1]])
xr = s.Rational(3, 4) * s.Matrix([[1, 2]]) * A.inv()
yc = s.Matrix([1, 1])
assert xr == s.Matrix([[3, -3]])
assert xr * yc == s.zeros(1)
assert (yc * xr).rank() == 1 and (yc * xr)**2 == s.zeros(2)

# T2(e): actual source-weighted twist traces are unequal.
U = s.diag(1, I)
assert abs(s.trace(U * U))**2 == 0
assert abs(s.trace(U.H * U))**2 == 4

# T3(c): exact Jordan obstruction at a retained band endpoint.
phase = (1 + I * s.sqrt(3)) / 2
E_theta = s.Matrix([[0, phase], [s.conjugate(phase), 0]])
H_odd = hashimoto([X, X, E_theta, E_theta])
K = s.simplify((H_odd**2).extract([0, 2, 4, 6], [0, 2, 4, 6]))
assert s.simplify(K.charpoly(z).as_expr() - (z - 1)**2 * (z - 3)**2) == 0
A3 = s.simplify(K - 3 * s.eye(4))
assert A3.rank() == 3
assert s.simplify(A3**2).rank() == 2

# T4(c): both the single-layer polynomial and the doubled norm.
h = hashimoto([X, X, Y, Y])
assert s.factor(h.charpoly(z).as_expr()) == (z - 1)**2 * (z + 1)**2 * (z**4 - 2*z**2 + 9)
letters_ad = [s.kronecker_product(U.conjugate(), U) for U in [X, X, Y, Y]]
H = hashimoto(letters_ad)
grading = s.kronecker_product(s.eye(4), s.kronecker_product(P, P))
assert s.trace(grading * H**2) == 32
print("Exact checks passed: kernel, twist, endpoint Jordan block, and single/doubled Pauli example.")
