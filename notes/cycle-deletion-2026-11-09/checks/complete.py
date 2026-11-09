r"""Windows of real-rootedness of P_w(K_n) = sum_C w^{|C|} mu_{d,K_n\\V(C)} for complete graphs (the dense extreme)."""
import sys, math, itertools
from fractions import Fraction
from functools import lru_cache
from flint import fmpq_poly, fmpz_poly, fmpq
import sympy as sp

def mu_complete(m, d):
    """coefficients c[s] (Fractions) with mu_{d,K_m}(x) = sum_s (-1)^s c[s] x^{dm-2s}; symmetric DP over load-type counts."""
    FALL = [math.perm(d, s) for s in range(d + 1)]
    EDGE = [Fraction(1, math.factorial(k) * math.perm(d, k)) for k in range(d + 1)]
    states = {tuple([m] + [0] * d): {0: Fraction(1)}}
    for step in range(m):
        r = m - step
        new = {}
        for counts, poly in states.items():
            for j in range(d + 1):
                if counts[j] == 0: continue
                frac = Fraction(counts[j], r)
                rest = list(counts); rest[j] -= 1
                # distribute additional load a <= d-j over the remaining vertices: choose for class i a multiset of k's
                def rec(i, budget, cur, ways, wt, added):
                    if i > d:
                        s = j + added
                        f = frac * ways * wt * FALL[s]
                        key = tuple(cur)
                        dst = new.setdefault(key, {})
                        for e, c in poly.items():
                            dst[e + added] = dst.get(e + added, 0) + c * f
                        return
                    ni = rest[i]
                    # choose m_k vertices of class i to receive k (k=1..d-i), rest receive 0
                    def rec2(k, left, budget2, cur2, ways2, wt2, added2):
                        if k > d - i:
                            cur3 = list(cur2); cur3[i] += left
                            rec(i + 1, budget2, cur3, ways2, wt2, added2)
                            return
                        mk = 0
                        while mk <= left and mk * k <= budget2:
                            cur3 = list(cur2); cur3[i + k] += mk
                            rec2(k + 1, left - mk, budget2 - mk * k, cur3, ways2 * math.comb(left, mk), wt2 * EDGE[k] ** mk, added2 + mk * k)
                            mk += 1
                    rec2(1, ni, budget, cur, ways, wt, added)
                rec(0, d - j, [0] * (d + 1), 1, Fraction(1), 0)
        states = new
    (key, poly), = states.items()
    return [poly.get(s, Fraction(0)) for s in range(max(poly) + 1)]

def cycle_cover_counts(n):
    """a[m] = dict j -> number of ways to partition m labelled vertices into j cycles of length >= 3 (unoriented)."""
    a = [dict() for _ in range(n + 1)]
    a[0] = {0: 1}
    for m in range(1, n + 1):
        acc = {}
        for l in range(3, m + 1):      # cycle through the smallest vertex has length l
            ways = math.comb(m - 1, l - 1) * math.factorial(l - 1) // 2
            for j, c in a[m - l].items():
                acc[j + 1] = acc.get(j + 1, 0) + ways * c
        a[m] = acc
    return a

def T_complete(n, d):
    xs = {}
    a = cycle_cover_counts(n)
    T = {}
    for m in range(n + 1):
        if not a[m]: continue
        r = n - m
        c = mu_complete(r, d) if r else [Fraction(1)]
        co = [Fraction(0)] * (d * r + 1)
        for s, cs in enumerate(c): co[d * r - 2 * s] = (-1) ** s * cs
        p = fmpq_poly([fmpq(v.numerator, v.denominator) for v in co])
        for j, cnt in a[m].items():
            T[j] = T.get(j, fmpq_poly([0])) + p * (math.comb(n, m) * cnt)
    return [T.get(j, fmpq_poly([0])) for j in range(max(T) + 1)]

def real_rooted(p):
    q = p.numer() if hasattr(p, 'numer') else p
    co = [int(c) for c in q.coeffs()]
    k = 0
    while co[k] == 0: k += 1
    h = fmpz_poly(co[k:])
    if h.degree() <= 0: return True
    return sum(mult for r, mult in h.complex_roots() if r.imag == 0) == h.degree()

def Pw(T, w):
    p = fmpq_poly([0])
    for j, t in enumerate(T): p = p + t * fmpq(w.numerator, w.denominator) ** j
    return p

def thr(T, sign, big=4096, iters=40):
    a, b = Fraction(0), Fraction(sign * big)
    if real_rooted(Pw(T, b)): return float('inf') * sign
    for _ in range(iters):
        mid = (a + b) / 2
        if real_rooted(Pw(T, mid)): a = mid
        else: b = mid
    return float(a)

if __name__ == '__main__':
    d = int(sys.argv[1]); nmax = int(sys.argv[2])
    # check against the lane: mu_{4,K4} constant 87/4 - 3 = 75/4, mu_{3,K4}(0) = 97/9
    print('check mu_{4,K4}(0) =', mu_complete(4, 4)[8], ' mu_{3,K4}(0) =', mu_complete(4, 3)[6])
    for n in range(3, nmax + 1):
        T = T_complete(n, d)
        print('d=%d K_%d window [%.6f, %.6f]' % (d, n, thr(T, -1), thr(T, 1)), flush=True)
