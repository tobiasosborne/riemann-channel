"""Exact finite-field helpers, prime q only in computations; proofs allow prime powers.

Polynomial tuples are in ascending order. All persistent output stays in this lane.
"""
import sys
sys.dont_write_bytecode = True
from functools import lru_cache
from fractions import Fraction as F
import math
import numpy as np
import mpmath as mp
import sympy as sp
from flint import nmod_poly


def monics(q, d):
    for code in range(q**d):
        v = code
        a = []
        for _ in range(d):
            a.append(v % q)
            v //= q
        yield tuple(a + [1])


def matrix_monics(q, d):
    v = np.arange(q**d, dtype=np.int64)
    return np.column_stack([(v // q**i) % q for i in range(d)] + [np.ones(len(v), dtype=np.int64)])


@lru_cache(None)
def factors(q, a):
    return tuple((tuple(int(c) for c in p), int(e)) for p, e in nmod_poly(list(a), q).factor()[1])


@lru_cache(None)
def irreducibles(q, d):
    return tuple(a for a in monics(q, d) if len(factors(q, a)) == 1 and factors(q, a)[0][1] == 1)


def pmul(q, a, b):
    return tuple(int(c) for c in nmod_poly(list(a), q)*nmod_poly(list(b), q))


def squarefree_mask(q, d):
    mask = np.ones(q**d, dtype=bool)
    for r in range(1, d//2+1):
        bs = matrix_monics(q, d-2*r)
        for p in irreducibles(q, r):
            p2 = pmul(q, p, p)
            out = np.zeros((len(bs), d+1), dtype=np.int64)
            for j, c in enumerate(p2):
                out[:, j:j+bs.shape[1]] += c*bs
            codes = ((out[:, :d] % q) * np.array([q**i for i in range(d)])).sum(axis=1)
            mask[codes] = False
    assert int(mask.sum()) == (q if d == 1 else q**d-q**(d-1))
    return mask


@lru_cache(None)
def quadratic_table(q, p):
    r = len(p)-1
    mod = nmod_poly(list(p), q)
    table = []
    for k in range(q**r):
        a = [(k//q**j) % q for j in range(r)]
        v = nmod_poly(a, q).pow_mod((q**r-1)//2, mod)
        table.append(0 if not v else (1 if int(v[0]) == 1 else -1))
    return np.array(table, dtype=np.int64)


def residue_codes(q, polys, p):
    r = len(p)-1
    a = polys.copy()
    for i in range(a.shape[1]-1, r-1, -1):
        c = a[:, i].copy()
        for j in range(r):
            a[:, i-r+j] = (a[:, i-r+j]-c*p[j]) % q
    return (a[:, :r]*np.array([q**i for i in range(r)], dtype=np.int64)).sum(axis=1)


def jacobi(q, a, b):
    """Jacobi (a/b), including nonsquarefree b, using resultants over F_q."""
    if len(b) == 1:
        return 1
    v = int(nmod_poly(list(b), q).resultant(nmod_poly(list(a), q)))
    z = pow(v, (q-1)//2, q)
    return 0 if z == 0 else (1 if z == 1 else -1)


def series_factor(v, r, c, inverse=False):
    """Multiply by (1+c*t^r), or its inverse, truncated to len(v)."""
    out = list(v)
    if inverse:
        for k in range(r, len(v)):
            out[k] -= c*out[k-r]
    else:
        for k in range(r, len(v)):
            out[k] += c*v[k-r]
    return out


@lru_cache(None)
def quadratic_L(q, h):
    """Primitive coefficients: Jacobi sums to the middle, algebraic FE above it."""
    d=len(h)-1
    if d==0:
        return ()
    g=(d-1)//2
    low=[F(sum(jacobi(q, a, h) for a in monics(q, k))) for k in range(g+1)]
    if d%2==0:
        low=[sum(low[:k+1]) for k in range(g+1)]
    ell=complete_quadratic(q,g,low)
    if d%2==0:
        ell=[ell[0]]+[ell[i]-ell[i-1] for i in range(1,len(ell))]+[-ell[-1]]
    assert all(x.denominator==1 for x in ell)
    return tuple(int(x) for x in ell)


def a2_term(q, d, a, h):
    if len(h) == 1:
        v = [q**k for k in range(d+1)]
    else:
        ell = quadratic_L(q, h)
        v = list(ell) + [0]*max(0, d+1-len(ell))
        v = v[:d+1]
        for p, _ in factors(q, h):
            v = series_factor(v, 2*(len(p)-1), -1, True)
    v = series_factor(v, 2, -q)
    hp = {p for p, _ in factors(q, h)}
    for p, _ in factors(q, a):
        if p not in hp:
            v = series_factor(v, len(p)-1, jacobi(q, p, h), True)
    return (-1 if q % 4 == 3 and d*(len(h)-1) % 2 else 1)*v[d]


def a2_coefficient(q, d, n):
    square = nonsquare = 0
    for m in range(n//2+1):
        hdeg = n-2*m
        for h in monics(q, hdeg):
            if any(e != 1 for _, e in factors(q, h)):
                continue
            for a in monics(q, m):
                val = a2_term(q, d, a, h)
                if hdeg == 0:
                    square += val
                else:
                    nonsquare += val
    den = q**d-q**(d-1)
    return F(square, den), F(nonsquare, den)


def complete_quadratic(q, g, low):
    out = list(low)+[F(0)]*(2*g+1-len(low))
    for i in range(g):
        out[2*g-i] = q**(g-i)*out[i]
    return out


def expr(coeff, name='u'):
    u = sp.Symbol(name)
    return sp.Add(*[sp.Rational(c.numerator,c.denominator)*u**i for i,c in enumerate(map(F,coeff))])


def root_report(coeff, q, label='', out=print):
    """Numpy roots in z=sqrt(q)u; coefficientwise condition, 80-digit Newton check.

    Condition kappa=sum|a_k z^k|/|z p'(z)| bounds relative root response
    to componentwise relative coefficient perturbations to first order.
    High-precision refinement diagnoses floating error, not an interval proof.
    """
    coeff = list(map(F, coeff))
    while len(coeff)>1 and coeff[-1] == 0:
        coeff.pop()
    if len(coeff) == 1:
        out(f'{label} constant polynomial; degree=0; no roots (degree collapse if positive degree expected)')
        return 0.0
    mp.mp.dps = 80
    a = [mp.mpf(c.numerator)/c.denominator/mp.sqrt(q)**i for i,c in enumerate(coeff)]
    znp = np.roots(np.array([complex(x) for x in a[::-1]]))
    np_dev=float(max(abs(abs(z)-1) for z in znp))
    refined=[]
    max_kappa=0.0
    max_resid=0.0
    max_diff=0.0
    for z in sorted(znp, key=lambda t:(round(t.real,8),t.imag)):
        zz = mp.mpc(z)
        for _ in range(30):
            val = mp.polyval(a[::-1],zz)
            deriv = mp.polyval([i*a[i] for i in range(len(a)-1,0,-1)],zz)
            if not deriv:
                break
            step = val/deriv
            zz -= step
            if abs(step)<mp.mpf('1e-70'):
                break
        val = mp.polyval(a[::-1],zz)
        deriv = mp.polyval([i*a[i] for i in range(len(a)-1,0,-1)],zz)
        scale = mp.fsum(abs(c*zz**i) for i,c in enumerate(a))
        kap = scale/abs(zz*deriv) if deriv else mp.inf
        max_kappa=max(max_kappa,float(kap))
        max_resid=max(max_resid,float(abs(val)/scale))
        max_diff=max(max_diff,float(abs(zz-z)))
        refined.append(zz)
        u=zz/mp.sqrt(q)
        out(f'  u={float(u.real):+.12f}{float(u.imag):+.12f}i |u|sqrt(q)={float(abs(zz)):.12f}')
    dev=max(abs(abs(z)-1) for z in refined)
    distinct=min((abs(a-b) for i,a in enumerate(refined) for b in refined[:i]),default=mp.inf)
    assert distinct>mp.mpf('1e-30'), 'Repeated/merged roots require a separate treatment.'
    assert max_resid<1e-60, 'High precision refinement failed.'
    assert max_diff<1e-10*max(1,max_kappa), 'Numpy roots disagree with high precision beyond the condition diagnostic.'
    out(f'{label} max_radial_deviation={mp.nstr(dev,18)} numpy_radial_deviation={np_dev:.3e} max_kappa={max_kappa:.6g} max_np_to_80d={max_diff:.3e} max_relative_residual={max_resid:.3e}')
    return float(dev)


def sturm_curve_certificate(coeff,q):
    """Exact rational isolation of R where P(u)=u^g R(qu+1/u)."""
    coeff=list(map(F,coeff));g=(len(coeff)-1)//2
    assert len(coeff)==2*g+1
    assert coeff==complete_quadratic(q,g,coeff[:g+1])
    x=sp.Symbol('x')
    sk=[sp.Integer(2),x]
    for k in range(2,g+1):sk.append(sp.expand(x*sk[-1]-q*sk[-2]))
    r=sp.Poly(sp.Rational(coeff[g])+sum(sp.Rational(coeff[i])*sk[g-i] for i in range(g)),x)
    iv=r.intervals(eps=sp.Rational(1,10**25))
    assert sum(mult for _,mult in iv)==g
    assert all(max(a*a,b*b)<4*q for (a,b),_ in iv)
    return r.as_expr(),iv
