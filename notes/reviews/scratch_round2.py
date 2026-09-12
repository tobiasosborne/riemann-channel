"""Round-2 independent re-derivation, written from the STATEMENT of
notes/quantum-ihara-general.md (not from scripts/qihara_general.py).

Checks, in order:
 1. Theorem 1 in the *displayed* 1 + D(u) - A(u) form, symbolically, D = 2 and D = 4.
 2. Corollary 4's new D = 2 claim: T = E_1 (+) E_2 under T(v|i>) = sum_{j != ibar} E_i v |j>,
    sigma = (1 2), and det_W(1-uT) = det(1-uE_1) det(1-uE_2).
 3. Corollary 3 as an identity of POLYNOMIALS, including at u^2 = 1 (the new I3 sentence),
    D = 2, 4, 6.
 4. Corollary 4 exponent arithmetic ND/2 - N = N(D-2)/2 and totality at D = 2.
 5. The new Theorem 1 norm bound (max_i ||E_ibar E_i||)^{-1/2}: Neumann convergence.
 6. The section-5 Watanabe-Fukumizu specialisation: Ahat -> A by push-through,
    Dhat -> D by i <-> ibar relabelling, prefactor, and M = dB vs T = Bd (Sylvester).
"""
import itertools
import numpy as np
import sympy as sp

u = sp.symbols('u')

def hashimoto_sym(Es, inv, N, D):
    T = sp.zeros(N*D, N*D)
    for i in range(D):
        for j in range(D):
            if j != inv[i]:
                T[j*N:(j+1)*N, i*N:(i+1)*N] = Es[i]
    return T

def displayed_rhs(Es, inv, N, D):
    """prod_{pairs} det(1-u^2 E_ibar E_i) * det(1 + D(u) - A(u)), displayed form only."""
    pairs = {tuple(sorted((i, inv[i]))) for i in range(D)}
    pref = sp.prod([(sp.eye(N) - u**2*Es[b]*Es[a]).det() for a, b in pairs])
    A = sp.zeros(N, N); Dop = sp.zeros(N, N)
    for i in range(D):
        Rinv = (sp.eye(N) - u**2*Es[inv[i]]*Es[i]).inv()
        A += u*Es[i]*Rinv
        Dop += u**2*Es[inv[i]]*Es[i]*Rinv
    return pref*(sp.eye(N) + Dop - A).det()

print('--- 1. Theorem 1, displayed 1+D-A form, fully symbolic ---')
# includes the non-commuting D = 2, N = 2 case (the minimal instance that would expose a
# left/right or E_i <-> E_ibar transposition) and two different involution patterns at D = 4.
for N, D, inv in [(1, 2, [1, 0]), (2, 2, [1, 0]), (1, 4, [1, 0, 3, 2]), (1, 4, [2, 3, 0, 1])]:
    Es = [sp.Matrix(N, N, lambda a, b, i=i: sp.Symbol(f'e{i}_{a}{b}')) for i in range(D)]
    lhs = (sp.eye(N*D) - u*hashimoto_sym(Es, inv, N, D)).det()
    ok = sp.simplify(sp.cancel(sp.together(
        sp.expand(lhs) - sp.expand(displayed_rhs(Es, inv, N, D))))) == 0
    print(f'  N={N} D={D} inv={inv}: displayed form equals det_W(1-uT): {ok}')
    assert ok

# discrimination control: wrong order E_i E_ibar inside the resolvent must FAIL
N, D, inv = 2, 2, [1, 0]
Es = [sp.Matrix(N, N, lambda a, b, i=i: sp.Symbol(f'e{i}_{a}{b}')) for i in range(D)]
A = sp.zeros(N, N); Dop = sp.zeros(N, N)
for i in range(D):
    Rbad = (sp.eye(N) - u**2*Es[i]*Es[inv[i]]).inv()      # WRONG order
    A += u*Es[i]*Rbad
    Dop += u**2*Es[inv[i]]*Es[i]*Rbad
pairs = {tuple(sorted((i, inv[i]))) for i in range(D)}
pref = sp.prod([(sp.eye(N) - u**2*Es[b]*Es[a]).det() for a, b in pairs])
lhs = (sp.eye(N*D) - u*hashimoto_sym(Es, inv, N, D)).det()
bad = sp.simplify(sp.cancel(sp.together(lhs - pref*(sp.eye(N) + Dop - A).det()))) == 0
print(f'  control (wrong resolvent order) agrees? {bad}   [must be False]')
assert not bad

print('--- 2. Corollary 4, D = 2: T = E_1 (+) E_2 ---')
for N in (1, 2, 3):
    Es = [sp.Matrix(N, N, lambda a, b, i=i: sp.Symbol(f'f{i}_{a}{b}')) for i in range(2)]
    T = hashimoto_sym(Es, [1, 0], N, 2)
    blockdiag = sp.zeros(N*2, N*2)
    blockdiag[0:N, 0:N] = Es[0]; blockdiag[N:2*N, N:2*N] = Es[1]
    same = sp.simplify(T - blockdiag) == sp.zeros(N*2, N*2)
    factors = sp.simplify((sp.eye(2*N) - u*T).det()
                          - (sp.eye(N) - u*Es[0]).det()*(sp.eye(N) - u*Es[1]).det()) == 0
    print(f'  N={N}: T == E_1 (+) E_2: {same}; det factorises: {factors}')
    assert same and factors

print('--- 3. Corollary 3 as polynomials, incl. u^2 = 1 ---')
for N, D in [(1, 2), (2, 2), (2, 4), (2, 6), (1, 6)]:
    inv = [i + 1 if i % 2 == 0 else i - 1 for i in range(D)]
    # E_ibar = E_i^{-1}: build invertible rational matrices
    rng = np.random.default_rng(1234 + 10*N + D)
    Es = [None]*D
    for k in range(0, D, 2):
        while True:
            X = sp.Matrix(N, N, lambda a, b: sp.Rational(int(rng.integers(-3, 4)), int(rng.integers(1, 4))))
            if X.det() != 0:
                break
        Es[k] = X; Es[k+1] = X.inv()
    T = hashimoto_sym(Es, inv, N, D)
    lhs = sp.expand((sp.eye(N*D) - u*T).det())
    Sigma = sum(Es, sp.zeros(N, N))
    rhs = sp.expand((1 - u**2)**sp.Rational(N*(D-2), 2)
                    * (sp.eye(N) - u*Sigma + (D-1)*u**2*sp.eye(N)).det())
    ok = sp.simplify(lhs - rhs) == 0
    # explicit evaluation at u = +-1, where Theorem 1's hypothesis fails
    at1 = sp.simplify(lhs.subs(u, 1) - rhs.subs(u, 1)) == 0
    atm1 = sp.simplify(lhs.subs(u, -1) - rhs.subs(u, -1)) == 0
    print(f'  N={N} D={D}: polynomial identity {ok}; at u=1 {at1}; at u=-1 {atm1}')
    assert ok and at1 and atm1

print('--- 4. Corollary 4 exponent arithmetic ---')
for D in (2, 4, 6, 8):
    for N in (1, 3, 9):
        assert sp.Rational(N*D, 2) - N == sp.Rational(N*(D-2), 2)
print('  ND/2 - N == N(D-2)/2 for all tested (N,D): True; D=2 gives 0 (total cancellation):',
      all(sp.Rational(N*(2-2), 2) == 0 for N in (1, 3, 9)))

print('--- 5. Neumann bound (max_i ||E_ibar E_i||)^{-1/2} ---')
rng = np.random.default_rng(5)
for trial in range(200):
    N, D = 3, 4
    inv = [1, 0, 3, 2]
    Es = [rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N)) for _ in range(D)]
    mx = max(np.linalg.norm(Es[inv[i]] @ Es[i], 2) for i in range(D))
    r = mx**-0.5
    uu = 0.999*r*np.exp(2j*np.pi*rng.random())
    ok = all(abs(np.linalg.det(np.eye(N) - uu**2*Es[inv[i]] @ Es[i])) > 1e-12 for i in range(D))
    assert ok, 'hypothesis failed inside the stated disc'
print('  200 random instances: 1 - u^2 E_ibar E_i invertible for all |u| < (max||E_ibar E_i||)^{-1/2}: True')
# and that min_i ||.||^{-1/2} == (max_i ||.||)^{-1/2}
vals = [0.5, 2.0, 7.0]
print('  min_i ||.||^{-1/2} == (max_i ||.||)^{-1/2}:',
      abs(min(v**-0.5 for v in vals) - max(vals)**-0.5) < 1e-15)

print('--- 6. Watanabe-Fukumizu specialisation on the bouquet ---')
rng = np.random.default_rng(11)
N, D = 3, 6
inv = [1, 0, 3, 2, 5, 4]
E = [rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N)) for _ in range(D)]
uu = 0.11 + 0.03j
I = np.eye(N)
# WF Ahat, Dhat on a one-vertex graph, u_e = u E_e   (their form, resolvent on the LEFT)
Ahat = sum(np.linalg.inv(I - uu**2*E[e] @ E[inv[e]]) @ (uu*E[e]) for e in range(D))
Dhat = sum(np.linalg.inv(I - uu**2*E[e] @ E[inv[e]]) @ (uu**2*E[e] @ E[inv[e]]) for e in range(D))
# the note's A(u), D(u)
Anote = uu*sum(E[i] @ np.linalg.inv(I - uu**2*E[inv[i]] @ E[i]) for i in range(D))
Dnote = uu**2*sum(E[inv[i]] @ E[i] @ np.linalg.inv(I - uu**2*E[inv[i]] @ E[i]) for i in range(D))
print(f'  push-through  Ahat vs A(u): {np.abs(Ahat-Anote).max():.2e}')
print(f'  relabelling   Dhat vs D(u): {np.abs(Dhat-Dnote).max():.2e}')
pairs = {tuple(sorted((i, inv[i]))) for i in range(D)}
prefWF = np.prod([np.linalg.det(I - uu**2*E[a] @ E[b]) for a, b in pairs])
prefnote = np.prod([np.linalg.det(I - uu**2*E[b] @ E[a]) for a, b in pairs])
print(f'  prefactor  prod det(I-u_e u_ebar) vs prod det(1-u^2 E_ibar E_i): '
      f'{abs(prefWF/prefnote - 1):.2e}')
T = np.zeros((N*D, N*D), complex)
for i in range(D):
    for j in range(D):
        if j != inv[i]:
            T[j*N:(j+1)*N, i*N:(i+1)*N] = E[i]
wf = prefWF*np.linalg.det(I + Dhat - Ahat)
print(f'  WF corollary RHS vs det_W(1-uT): {abs(wf/np.linalg.det(np.eye(N*D)-uu*T) - 1):.2e}')
# M = dB (target-weighted, WF) vs T = Bd (source-weighted, note); Sylvester
d = np.zeros((N*D, N*D), complex)
for i in range(D):
    d[i*N:(i+1)*N, i*N:(i+1)*N] = uu*E[i]
B = np.zeros((N*D, N*D), complex)
for i in range(D):
    for j in range(D):
        if j != inv[i]:
            B[j*N:(j+1)*N, i*N:(i+1)*N] = I
Mwf = d @ B
print(f'  det(1 - dB) [WF, target-weighted] vs det(1 - u T) [note, source-weighted]: '
      f'{abs(np.linalg.det(np.eye(N*D)-Mwf)/np.linalg.det(np.eye(N*D)-uu*T) - 1):.2e}')
# reversal of words is a bijection of cyclically non-backtracking sequences
for ell in (2, 3, 4, 5):
    S = {w for w in itertools.product(range(D), repeat=ell)
         if all(w[(k+1) % ell] != inv[w[k]] for k in range(ell))}
    print(f'  reversal bijection at ell={ell}: {set(tuple(reversed(w)) for w in S) == S}')

print('ALL ROUND-2 CHECKS PASS')
