"""Independent verification of Theorem 1 of notes/quantum-ihara-general.md.
Written from the STATEMENT only (T, pair product, A(u), D(u)); no reuse of scripts/qihara_general.py."""
import sympy as sp, itertools, random

u = sp.symbols('u')

def build_T(Es, bar, N, D):
    """T(v (x) |i>) = sum_{j != bar(i)} E_i v (x) |j>  ->  block (j,i) entry E_i."""
    T = sp.zeros(N*D, N*D)
    for i in range(D):
        for j in range(D):
            if j != bar[i]:
                T[j*N:(j+1)*N, i*N:(i+1)*N] = Es[i]
    return T

def lhs(Es, bar, N, D):
    return sp.expand((sp.eye(N*D) - u*build_T(Es, bar, N, D)).det())

def rhs(Es, bar, N, D):
    I = sp.eye(N)
    seen, pref = set(), sp.Integer(1)
    for i in range(D):
        p = frozenset((i, bar[i]))
        if p in seen: continue
        seen.add(p)
        pref *= (I - u**2*Es[bar[i]]*Es[i]).det()     # det_V(1 - u^2 E_ibar E_i)
    A = sp.zeros(N, N); Dop = sp.zeros(N, N)
    for i in range(D):
        P = (I - u**2*Es[bar[i]]*Es[i]).inv()
        A   += u   * Es[i]*P
        Dop += u**2 * Es[bar[i]]*Es[i]*P
    return sp.together(sp.expand(pref * (I + Dop - A).det()))

def report(tag, Es, bar, N, D, show=False):
    L, R = lhs(Es, bar, N, D), rhs(Es, bar, N, D)
    ok = sp.simplify(sp.together(L - R)) == 0
    print(f'{tag}: lhs == rhs ?  {ok}')
    if show:
        print('   lhs =', sp.factor(L))
        print('   rhs =', sp.factor(sp.simplify(R)))
    return ok

# ---------- instance 1: D=2 (single pair), N=1, fully symbolic ----------
e1, e2 = sp.symbols('e1 e2')
report('D=2, N=1 symbolic (single pair)', [sp.Matrix([[e1]]), sp.Matrix([[e2]])], [1,0], 1, 2, show=True)

# ---------- instance 2: D=2, N=2, fully symbolic (detects left/right ordering) ----------
a = sp.symbols('a1:5'); b = sp.symbols('b1:5')
E1 = sp.Matrix(2,2,a); E2 = sp.Matrix(2,2,b)
report('D=2, N=2 symbolic (single pair, noncommuting)', [E1,E2], [1,0], 2, 2)

# ---------- instance 3: D=4, N=1, fully symbolic ----------
f = sp.symbols('f1:5')
Es = [sp.Matrix([[x]]) for x in f]
report('D=4, N=1 symbolic, bar=(1 2)(3 4)', Es, [1,0,3,2], 1, 4, show=True)

# ---------- instance 4: D=4, N=1, the OTHER involution pairing to test pair-product ----------
report('D=4, N=1 symbolic, bar=(1 3)(2 4)', Es, [2,3,0,1], 1, 4)

# ---------- instance 5: D=4, N=2, random rationals (ordering-sensitive) ----------
random.seed(11)
def rmat(N): return sp.Matrix(N,N, lambda i,j: sp.Rational(random.randint(-4,4), random.randint(1,5)))
report('D=4, N=2 rational random, bar=(1 2)(3 4)', [rmat(2) for _ in range(4)], [1,0,3,2], 2, 4)

# ---------- instance 6: D=6, N=2 random rationals ----------
report('D=6, N=2 rational random', [rmat(2) for _ in range(6)], [1,0,3,2,5,4], 2, 6)
