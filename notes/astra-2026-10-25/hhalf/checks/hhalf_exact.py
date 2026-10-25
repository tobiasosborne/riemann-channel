#!/usr/bin/env python3
"""Exact averaged coefficients, unhalved H-half, and independent Sturm tests.
Run: python3 checks/hhalf_exact.py --grid 3:25,5:10,7:8,9:8,11:6,13:6
Optional --even checks the completed even-conductor family with the stated genera.
Caches are integer coefficient series, not approximate or sampled L-polynomials.
"""
import sys
sys.dont_write_bytecode=True
import argparse,json,time
from pathlib import Path
from fractions import Fraction as F
import sympy as sp
from exact_core import raw_series
from common import complete_quadratic,sturm_curve_certificate
HERE=Path(__file__).parent

def circle_test(b):
    w=sp.Symbol('w');x=sp.Symbol('x');p=sp.Poly(sum(sp.Rational(c)*w**i for i,c in enumerate(b)),w)
    assert b==b[::-1] and b[0]==1
    forced=0
    if p.degree()%2:
        p,rem=sp.div(p,sp.Poly(w+1,w));assert rem.is_zero;forced=1
    k=p.degree()//2;sk=[sp.Integer(2),x]
    for j in range(2,k+1):sk.append(sp.expand(x*sk[-1]-sk[-2]))
    r=sp.Poly(p.nth(k)+sum(p.nth(j)*sk[k-j] for j in range(k)),x)
    iv=r.intervals(eps=sp.Rational(1,10**12)) if k else []
    good=sum(mult for _,mult in iv)==k and all(-2<=a<=bb<=2 for (a,bb),_ in iv)
    return good,r,iv,forced

def get_series(q,n,D,emit):
    cache=HERE/f'series_q{q}_m{n//2}.json' if n%2==0 else HERE/f'series_q{q}_n{n}.json'
    if cache.exists():
        c=json.loads(cache.read_text())
        if len(c)>D:return c[:D+1]
    t=time.monotonic();p,jobs=raw_series(q,n,D)
    c=[int(p[k]) for k in range(D+1)]
    cache.write_text(json.dumps(c))
    emit(f'computed q={q} raw_n={n} through_d={D} grouped_jobs={jobs} seconds={time.monotonic()-t:.3f}')
    return c

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--grid',default='3:25,5:10,7:8,9:8,11:6,13:6');ap.add_argument('--even',action='store_true');args=ap.parse_args()
    outfile=HERE/('output_hhalf_even.txt' if args.even else 'output_hhalf_exact.txt')
    with outfile.open('w') as log:
        def emit(s):print(s,flush=True);print(s,file=log,flush=True)
        total=0
        for q,G in [tuple(map(int,z.split(':'))) for z in args.grid.split(',')]:
            D=2*G+1+int(args.even)
            ns=range(1,G+1) if args.even else range(2,G+1,2)
            raw={n:get_series(q,n,D,emit) for n in ns}
            for g in range(1,G+1):
                d=2*g+1+int(args.even);H=(q-1)*q**(d-1)
                if args.even:
                    low=[F(1)]+[F(raw[n][d],H) for n in range(1,g+1)]
                    low=[sum(low[:k+1]) for k in range(g+1)]
                    p=complete_quadratic(q,g,low)
                    r,iv=sturm_curve_certificate(p,q)
                    emit(f'even q={q} g={g} coefficients={list(map(str,p))}; exact_circle=True R(x)={r}; intervals={iv}')
                else:
                    b=[F(1)]+[F(raw[2*m][d],H*q**m) for m in range(1,g//2+1)]
                    b=b+list(reversed(b[:-1] if g%2==0 else b))
                    h=all(b[m-1]>=b[m]>0 for m in range(1,g//2+1))
                    circle,r,iv,forced=circle_test(b)
                    emit(f'q={q} g={g} B_coefficients={list(map(str,b))}')
                    emit(f'  monotone_unhalved={h} exact_circle={circle} forced_minus_one={forced} R(x)={r.as_expr()}; intervals={iv}')
                    if g>=2:emit(f'  minimum_first_half_gap={min(b[m-1]-b[m] for m in range(1,g//2+1))}')
                    assert h and circle,(q,g)
                total+=1
            emit(f'CERTIFIED q={q} g=1..{G} even={args.even}')
        emit(f'ALL {total} EXACT CERTIFICATES PASS. No universal extrapolation.')
if __name__=='__main__':main()
