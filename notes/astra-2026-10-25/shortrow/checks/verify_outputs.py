#!/usr/bin/env python3
"""Independent FLINT audit, old-output comparison and high-precision log audit."""
from shortrow_exact import *
from flint import nmod_poly
import random,mpmath as mp,re
rng=random.Random(20261025)
for q in (7,13):
    ex,eta,inv,f=tables(q);count=0
    for _ in range(1200):
        da=rng.randrange(8);db=rng.randrange(8)
        a=np.zeros(W,np.int64);b=np.zeros(W,np.int64)
        for j in range(da):a[j]=rng.randrange(q)
        for j in range(db):b[j]=rng.randrange(q)
        a[da]=rng.randrange(1,q);b[db]=rng.randrange(1,q)
        pa=nmod_poly(list(map(int,a[:da+1])),q);pb=nmod_poly(list(map(int,b[:db+1])),q)
        assert int(resultant(a,da,b,db,q,inv))==int(pa.resultant(pb)),(q,a,b)
        if da:
            a[da]=1;pa=nmod_poly(list(map(int,a[:da+1])),q)
            R=int(pa.resultant(pa.derivative()));mu=(-1)**da*int(eta[R*(-1)**(da*(da-1)//2)%q])
            fac=pa.factor()[1];independent=0 if any(e>1 for _,e in fac) else (-1)**len(fac)
            assert mu==independent
        count+=1
    print('FLINT_RESULTANT_AND_PELLET q=',q,'samples=',count,'PASS')
old=(HERE.parents[2]/'astra-2026-10-23/qrh-transpose/checks/output_ff.txt').read_bytes()
new=(HERE/'output_q2_rerun.txt').read_bytes()
assert old==new
print('Q2_RERUN_BYTE_IDENTICAL PASS')
def integer_mobius(n):
    sign=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;sign=-sign
            if n%p==0:return 0
        p+=1
    return -sign if n>1 else sign
def euler_weight(q,D):
    a=[1]+[0]*D
    for d in range(1,D+1):
        number=sum(integer_mobius(k)*q**(d//k) for k in range(1,d+1) if d%k==0)//d-(d==3)
        b=[0]*(D+1)
        for k in range(min(number,D//d)+1):
            w=comb(number,k)*(q**d-1)**k
            for j in range(D-k*d+1):b[j+k*d]+=a[j]*w
        a=b
    return a[D]
data=json.loads((HERE/'cells_all.json').read_text())
for q,Dmax in [(7,7),(13,5)]:
    F=Field(q,Dmax)
    for D in range(1,Dmax+1):assert F.diagonal_weight(D)==euler_weight(q,D)
    print('DIVISOR_MASK_VS_EULER_PRODUCT q=',q,'max_degree=',Dmax,'PASS')
    del F
for q,D in [(7,d) for d in range(1,7)]+[(13,d) for d in range(1,6)]:
    W=euler_weight(q,D)
    assert data[f'{q},{D},{2*D-1}']==q**D*W
    print('EULER_DIAGONAL q=',q,'D=',D,'W=',W,'PASS')
extra=HERE/'cells_7_7_poisson.json'
if extra.exists():
    W=euler_weight(7,7);values=json.loads(extra.read_text())
    assert values['13']==7**7*W
    print('EULER_DIAGONAL q=7 D=7 W=',W,'PASS')
count=0
for fn in ['table_all.md','table_growth.md','table_extension.md']:
    p=HERE/fn
    if not p.exists():continue
    for line in p.read_text().splitlines()[2:]:
        parts=[s.strip() for s in line.strip('|').split('|')]
        if not parts[0].isdigit():continue
        q=int(parts[0]);D=int(parts[1])
        if D==0:continue
        R=Fraction(parts[-2]);printed=mp.mpf(parts[-1])
        with mp.workdps(80):a=mp.log(mp.mpf(R.numerator)/R.denominator)/mp.log(q)/D
        with mp.workdps(100):
            b=mp.log(mp.mpf(R.numerator)/R.denominator)/mp.log(q)/D
            assert abs(a-b)<mp.mpf('1e-75')
            assert abs(b-mp.mpf(parts[-1]))<=mp.mpf('0.50001e-12')
        count+=1
print('LOGARITHMS 80_vs_100_decimal_digits rounded_to_12_places cells=',count,'PASS')
for q,D in [(7,7),(13,5)]:
    bound=3*q**(2*D)*sum(q**i for i in range(D+1))
    assert bound<2**63
    print('INNER_INT64_CONSERVATIVE_BOUND q=',q,'D=',D,'bound=',bound,'limit=',2**63,'PASS')
for q in (7,13):
    bound=3*q**16
    assert bound<2**63
    print('RECONSTRUCTION_NORM_INT64_BOUND q=',q,'Dmax=8 bound=',bound,'PASS')
print('VERIFICATION PASS')
