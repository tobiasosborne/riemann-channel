#!/usr/bin/env python3
"""Exact local lattice checks; run with python3. No network or external data."""
from fractions import Fraction
import random
import sympy as sp


def vp(x, p):
    x = Fraction(x)
    if not x:
        return float('inf')
    n, d = x.numerator, x.denominator
    a = b = 0
    while n % p == 0:
        n //= p
        a += 1
    while d % p == 0:
        d //= p
        b += 1
    return a - b


def ppow(p, k):
    return sp.Rational(p) ** k


def integral(A, p):
    return all(vp(x, p) >= 0 for x in A)


def same_lattice(A, B, p):
    return integral(A.inv() * B, p) and integral(B.inv() * A, p)


def lattice_distance(A, B, p):
    C = A.inv() * B
    s = min(vp(x, p) for x in C)
    return int(vp(C.det(), p) - 2 * s)


def t1():
    print('T1 exact rational arithmetic; equality means equality of Z_p modules')
    J = sp.Matrix([[0, 1], [-1, 0]])
    rng = random.Random(20261027)
    for p in (3, 5, 7):
        count = 0
        for _ in range(30):
            while True:
                g = sp.Matrix(2, 2, [rng.randint(-8, 8) for _ in range(4)])
                if g.det():
                    break
            g = g * sp.diag(ppow(p, rng.randrange(-3, 4)), ppow(p, rng.randrange(-3, 4)))
            # x^T J g integral, hence a dual basis is J g^{-T} (sign immaterial).
            dual = J * g.inv().T
            assert same_lattice(dual, g / g.det(), p)
            d = int(vp(g.det(), p))
            k = d % 2
            hat = ppow(p, (k-d)//2) * g
            assert vp(hat.det(), p) == k
            assert integral((hat / hat.det()).inv() * hat, p)
            assert vp(((hat / hat.det()).inv() * hat).det(), p) == 2*k
            assert same_lattice(hat, (1+p)*hat, p)
            count += 1
        print(f'p={p}: {count} dual/normalisation/unique-unit-representative checks passed')
    p = 3
    print('Homothety counterexample p=3: dim C_(Z_3^2)=1; dim C_(3 Z_3^2)=9')
    print('D_3 sends Z_3^2 to diag(1/3,3) Z_3^2; determinant valuation=0, not 2')
    # The phase of W_c(lambda)^2 / W_c(2 lambda), c=-uv/2, is +2uv.
    lam = (sp.Rational(1, 3), sp.Rational(1, 3))
    bad = 2 * lam[0] * lam[1]
    u,v,r,s,c=sp.symbols('u v r s c')
    cocycle=sp.expand(c*u*v+c*r*s+u*s-c*(u+r)*(v+s))
    assert sp.expand(cocycle.subs(c,sp.Rational(1,2))-(u*s-v*r)/2)==0
    assert sp.expand(cocycle.subs(c,-sp.Rational(1,2)).subs({r:u,s:v})-2*u*v)==0
    print('Wrong-sign Weyl counterexample p=3, self-dual g=[[1/3,0],[1/3,3]], lambda=(1/3,1/3)')
    print('W_minus(lambda)^2/W_minus(2lambda) exponent=', bad, '; v_3=', vp(bad,p), '; nontrivial character')
    print('Correct plus-sign Weyl cocycle: omega(lambda,mu)/2; on (lambda,lambda) exponent=0')


def local_hnf(A, p):
    """Canonical upper triangular Z_p Hermite representative up to homothety.

    Return exponents a,b and h for [[p^a,h],[0,p^b]], after removing the
    common scalar p^s. Only exact rational arithmetic and unit inverses used.
    """
    s = min(vp(x,p) for x in A)
    C = ppow(p,-s)*A
    b = int(min(vp(C[1,0],p),vp(C[1,1],p)))
    a = int(vp(C.det(),p))-b
    j = 0 if vp(C[1,0],p)==b else 1
    h = Fraction(C[0,j]*ppow(p,b)/C[1,j])
    modulus = p**a
    h = (h.numerator * pow(h.denominator,-1,modulus)) % modulus if a else 0
    H = sp.Matrix([[p**a,h],[0,p**b]])
    assert same_lattice(C,H,p)
    return (a,b,h)


def unit_root(T,D,p,precision):
    """Hensel lift of the nonzero root of y^2-Ty+D; T unit, D divisible by p."""
    r = T % p
    modulus = p
    for _ in range(1,precision):
        f = r*r-T*r+D
        assert f % modulus == 0
        digit = (-(f//modulus)*pow(2*r-T,-1,p)) % p
        r += digit*modulus
        modulus *= p
    assert (r*r-T*r+D) % modulus == 0
    return r


def classify_and_check(g,p,label):
    t, d = vp(g.trace(),p), int(vp(g.det(),p))
    if 2*t < d:
        t = int(t)
        ell = d-2*t
        precision = 40
        T, D = int(g.trace())//p**t, int(g.det())//p**(2*t)
        root = unit_root(T,D,p,precision)
        alpha = sp.Integer(p**t*root)
        beta = g.det()/alpha  # Vieta, more accurate for the small root.
        assert vp(beta/alpha,p)==ell
        # Exact rational approximants to the two p-adic eigenlines.
        if g[0,1]:
            S=sp.Matrix([[g[0,1],g[0,1]],[alpha-g[0,0],beta-g[0,0]]])
        elif g[1,0]:
            S=sp.Matrix([[alpha-g[1,1],beta-g[1,1]],[g[1,0],g[1,0]]])
        else:
            S=sp.eye(2) if vp(g[0,0],p)<vp(g[1,1],p) else sp.Matrix([[0,1],[1,0]])
        assert S.det()
        hs=[]
        for k in range(-3,4):
            L=S*sp.diag(1,ppow(p,k))
            nxt=S*sp.diag(1,ppow(p,k+ell))
            assert lattice_distance(L,g*L,p)==ell
            assert local_hnf(g*L,p)==local_hnf(nxt,p)
            assert lattice_distance(L,S*sp.diag(1,ppow(p,k+1)),p)==1
            hs.append(local_hnf(L,p))
        # A neighbour not in the apartment must move ell+2 steps.
        off=S*sp.Matrix([[1,0],[1,p]])
        assert lattice_distance(off,g*off,p)==ell+2
        print(f'{label}: g={list(g)}; v(tr)={t}, v(det)={d}; HYPERBOLIC length={ell}; eigenvalue valuations=({vp(alpha,p)},{vp(beta,p)}); v(beta/alpha)={vp(beta/alpha,p)}')
        print(f'  Hensel precision={precision} digits; split-axis HNF classes k=-3..3: {hs}')
        print(f'  seven exact HNF translation checks passed; off-axis neighbour displacement={ell+2}')
        return 'hyperbolic'
    slope=sp.Rational(d,2)
    # Construct a cyclic basis; its stable lattice or edge witnesses ellipticity.
    S=None
    for v in (sp.Matrix([1,0]),sp.Matrix([0,1]),sp.Matrix([1,1])):
        trial=sp.Matrix.hstack(v,g*v)
        if trial.det():
            S=trial
            break
    if d%2==0:
        h=ppow(p,-d//2)*g
        if S is None:
            L=sp.eye(2)
        else:
            v=S[:,0]
            L=sp.Matrix.hstack(v,h*v)
        assert local_hnf(h*L,p)==local_hnf(L,p)
        witness=f'fixed vertex HNF={local_hnf(L,p)}'
    else:
        h=ppow(p,-(d-1)//2)*g
        assert S is not None
        v=S[:,0]
        L=sp.Matrix.hstack(v,h*v)
        assert lattice_distance(L,h*L,p)==1
        assert local_hnf(h*h*L,p)==local_hnf(L,p)
        witness=f'inverted edge HNF={local_hnf(L,p)} <-> {local_hnf(h*L,p)}'
    print(f'{label}: g={list(g)}; v(tr)={t}, v(det)={d}; ELLIPTIC eigenvalue valuations=({slope},{slope}); v(ratio)=0; metric-tree translation length=0; {witness}')
    return 'elliptic'


def t3():
    print('\nT3: Newton slopes, Hensel eigenlines, and exact local Hermite reduction')
    print('Matrices are printed in row-major order. Inverted edges have vertex minimum 1, but metric-tree translation length 0.')
    for p in (3,5):
        rng=random.Random(20261027+p)
        counts={'elliptic':0,'hyperbolic':0}
        for j in range(10):
            while True:
                g=sp.Matrix(2,2,[rng.randint(-p*p,p*p) for _ in range(4)])
                if g.det():
                    break
            kind=classify_and_check(g,p,f'p={p}, random {j+1}')
            counts[kind]+=1
        print(f'p={p}, random classification totals={counts}')
        for label,g in (
            ('one-step non-Clifford',sp.diag(1,p)),
            ('two-step square',sp.diag(1,p*p)),
            ('quadratic irrational eigenlines',sp.Matrix([[1,1],[p,0]])),
            ('edge inversion',sp.Matrix([[0,1],[p,0]])),
            ('unit squeeze a=1',sp.eye(2)),
        ):
            classify_and_check(g,p,f'p={p}, {label}')
    print('Counterexample to no fixed vertex at m=0: a=1 gives D_1=identity, length=0.')
    print('Square-class obstruction at p=3: diag(1,3) has odd determinant valuation; diag(1,18) has even valuation 2 but nonsquare unit 2 mod 3.')
    print('For p=3, gamma=diag(1,9) has length=2; its SL2 lift diag(1/3,3) is implemented by D_3, not D_9.')


if __name__ == '__main__':
    t1()
    t3()
