"""REFUTE scratch core (ff-dirichlet.md), written from the page's STATEMENTS only.
F_p[t] arithmetic, power-residue characters, L-functions by brute force, exact Z[zeta_N] coefficients."""
import itertools, cmath, math
import mpmath as mp
mp.mp.dps = 40

def trim(a):
    a = list(a)
    while a and a[-1] == 0: a.pop()
    return a
def padd(a, b, p):
    n = max(len(a), len(b)); return trim([((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p for i in range(n)])
def pmul(a, b, p):
    if not a or not b: return []
    r = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b): r[i+j] = (r[i+j] + x*y) % p
    return trim(r)
def pdivmod(a, b, p):
    a = trim([x % p for x in a]); b = trim(b); inv = pow(b[-1], p-2, p); q = [0]*max(1, len(a)-len(b)+1)
    while len(a) >= len(b) and a:
        c = a[-1]*inv % p; k = len(a)-len(b); q[k] = c
        for i, y in enumerate(b): a[i+k] = (a[i+k] - c*y) % p
        a = trim(a)
    return trim(q), a
def pmod(a, b, p): return pdivmod(a, b, p)[1]
def ppowmod(a, e, m, p):
    r = [1]; a = pmod(a, m, p)
    while e:
        if e & 1: r = pmod(pmul(r, a, p), m, p)
        a = pmod(pmul(a, a, p), m, p); e >>= 1
    return r
def monics(k, p):
    for c in itertools.product(range(p), repeat=k): yield list(c) + [1]
def polys_below(k, p):  # all polys of degree < k (as lists of length k, may be zero)
    for c in itertools.product(range(p), repeat=k): yield list(c)
def is_irred(f, p):
    d = len(f)-1
    for k in range(1, d//2+1):
        for g in monics(k, p):
            if not pmod(f, g, p): return False
    return True
def irreducibles(k, p): return [f for f in monics(k, p) if is_irred(f, p)]
def primroot(p):
    for g in range(2, p):
        if all(pow(g, (p-1)//r, p) != 1 for r in range(2, p) if (p-1) % r == 0 and all(r % s for s in range(2, r))): return g
    return 1 if p == 2 else None
def dlog(c, g, p):
    x = 1
    for j in range(p-1):
        if x == c % p: return j
        x = x*g % p
    raise ValueError

class Char:
    """chi = prod_i (./P_i)_N, values as exponents k in Z/N (chi = zeta_N^k), None for 0."""
    def __init__(self, q, N, Ps, g=None):
        self.q, self.N, self.Ps = q, N, Ps
        self.g = g if g is not None else primroot(q)
        self.f = [1]
        for P in Ps: self.f = pmul(self.f, P, q)
        self.d = len(self.f)-1
    def sym(self, a, P):   # (a/P)_N as exponent k in Z/N, None if P | a
        q, N = self.q, self.N; Q = q**(len(P)-1)
        r = ppowmod(a, (Q-1)//N, P, q)
        if not r: return None
        assert len(r) == 1, r
        j = dlog(r[0], self.g, q); assert j % ((q-1)//N) == 0
        return (j//((q-1)//N)) % N
    def comp(self, a, i):  # chi_i(a)
        return self.sym(a, self.Ps[i])
    def __call__(self, a):
        k = 0
        for P in self.Ps:
            s = self.sym(a, P)
            if s is None: return None
            k += s
        return k % self.N
    def on_const(self, c):  # chi(c), c in F_q^x
        return self([c % self.q])

def zN(N): return cmath.exp(2j*math.pi/N)
def zval(vec, N):  # group-ring vector -> complex (mp)
    z = mp.exp(2j*mp.pi/N); return sum(mp.mpf(vec[k])*z**k for k in range(N))

def Lcoeffs(ch):
    """S_k = sum_{monic deg k} chi(m), k = 0..d, as group-ring vectors"""
    S = []
    for k in range(ch.d+1):
        v = [0]*ch.N
        for m in monics(k, ch.q):
            c = ch(m)
            if c is not None: v[c] += 1
        S.append(v)
    return S

def Lambda(ch):
    """returns (coeff list of complex mp values, parity, n)"""
    S = Lcoeffs(ch); N = ch.N
    assert all(zval(s, N) == 0 or abs(zval(s, N)) < 1e-20 for s in S[ch.d:]), "S_d != 0"
    L = [zval(s, N) for s in S[:ch.d]]
    while abs(L[-1]) < 1e-20: L.pop()
    even = all(ch.on_const(c) == 0 for c in range(1, ch.q))
    if even:
        # divide by (1-u): Lam_k = sum_{j<=k} L_j
        assert abs(sum(L)) < 1e-20
        Lam = [sum(L[:k+1]) for k in range(len(L)-1)]
    else:
        Lam = L
    return Lam, even, len(Lam)-1

def psi0(a, p): return mp.exp(2j*mp.pi*(a % p)/p)
