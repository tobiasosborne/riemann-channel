#!/usr/bin/env python3
"""Exact kinematic P1 and discrete prime-remainder P2 checks; no zeta zeros."""
import sympy as s
b=s.symbols('b', real=True)
E=s.Matrix([[1,0,b/2],[0,s.Rational(1,2),2*b/3],[b/2,2*b/3,s.Rational(1,2)+b/4]])
O=s.Matrix([[1,2*b/3],[2*b/3,1-b/2]])
se=1+b/2-s.Rational(41,18)*b*b
so=1-b/2-s.Rational(4,9)*b*b
assert s.expand(E.det()-se/4)==0
assert s.expand(O.det()-so)==0
ce=s.Matrix([b/s.sqrt(2),4*b/3])
assert s.expand(1+b/2-(ce.T*ce)[0]-se)==0
assert s.diff(se*so,b).subs(b,0)==0
left=(9-3*s.sqrt(337))/82
right=(9+3*s.sqrt(337))/82
for endpoint in (left,right):
    assert s.simplify(se.subs(b,endpoint))==0
    assert s.simplify(so.subs(b,endpoint)-(s.Rational(33,41)-s.Rational(49,82)*endpoint))==0
    assert so.subs(b,endpoint)>0
mid=s.simplify((left+right)/2)
halfwidth=s.simplify((right-left)/2)
assert mid==s.Rational(9,82)
assert s.simplify(-mid/halfwidth+3/s.sqrt(337))==0
print('P1 se =',se,'; so =',so)
print('P1 Ie =',left,right)
print('P1 midpoint =',mid,'; unique max = 0; exact offset =',-mid)
print('P1 normalised offset =',s.simplify(-mid/halfwidth))
print('P1 decimals:',s.N(left,35),s.N(right,35),s.N(-mid,35),s.N(-mid/halfwidth,35))
# Exact assembly of the 5x5 Loewner matrix verifies parity formulas.
idx=list(range(-2,3))
bs={-2:-b,-1:0,0:0,1:0,2:b}
T=s.Matrix([[1 if i==j else (bs[i]-bs[j])/s.Integer(i-j) for j in idx] for i in idx])
vec=lambda n: s.eye(5)[:,idx.index(n)]
Q=s.Matrix.hstack(vec(0),(vec(1)+vec(-1))/s.sqrt(2),(vec(2)+vec(-2))/s.sqrt(2),(vec(1)-vec(-1))/s.sqrt(2),(vec(2)-vec(-2))/s.sqrt(2))
blocked=s.simplify(Q.T*T*Q)
S=s.diag(1,1/s.sqrt(2),1/s.sqrt(2),1,1)
assert s.simplify(S*blocked*S-s.diag(E,O))==s.zeros(5)
# Three distinct atom centres are used only for the finite-place remainder.
ns=[1,2,6]; coeff=[s.Integer(1),s.Integer(2),s.Integer(-1)]
Ap={}
for i,m in enumerate(ns):
    for j,n in enumerate(ns):
        if n>m and n % m==0:
            fac=s.factorint(n//m)
            if len(fac)==1:
                p,k=next(iter(fac.items()))
                Ap[p]=Ap.get(p,0)+(s.conjugate(coeff[i])*coeff[j]+coeff[i]*s.conjugate(coeff[j]))/s.sqrt(p**k)
assert s.simplify(Ap[2]-2*s.sqrt(2))==0
assert s.simplify(Ap[3]+4/s.sqrt(3))==0
assert set(Ap)=={2,3}
remainder=-sum(v*s.log(p) for p,v in Ap.items())
print('P2 atom centres:',ns,'; coefficients:',coeff)
print('P2 local coefficients A_p:',Ap)
print('P2 Baker coordinates of remainder:',{p:s.simplify(-v) for p,v in Ap.items()})
print('P2 remainder =',remainder,'=',s.N(remainder,35))
for r in (s.Integer(2),s.Integer(3),s.Integer(6)):
    print('P2 r =',r,'; pole =',s.sqrt(r)+1/s.sqrt(r),'; rho =',s.simplify(s.sqrt(r)/(r-1/r)))
print('PASS: exact symbolic identities and interval inequalities; decimals only for display.')
