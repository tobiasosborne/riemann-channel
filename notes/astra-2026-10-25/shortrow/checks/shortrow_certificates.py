#!/usr/bin/env python3
"""Exact small corrections and exponent certificates; no RH input."""
from shortrow_exact import *
from flint import nmod_poly
q=7;D=2
eta=tables(q)[1];diag=0;Wphi=0
for i in range(q**D):
    p=nmod_poly(list(map(int,decode(i,q,D)[:D+1])),q)
    factors=p.factor()[1]
    if any(e>1 for a,e in factors) or not eta[int(p[0])]:continue
    phi=1
    for a,e in factors:phi*=q**a.degree()-1
    Wphi+=phi;diag+=q-1
print('DIAGONAL_COUNTEREXAMPLE q=7 nu=(./t)_2 D=2 h=0 actual=',diag,'claimed=',Fraction(Wphi,q),'weighted_phi=',Wphi)
assert diag==216 and Fraction(Wphi,q)==Fraction(1548,7)
F=Field(7,2);v=np.zeros(2,np.int64)
for i in range(49):
    if F.mu[2][i] and F.nu[2][i]:v+=F.nu[2][i]*PAIR[F.phase[2][i]]
Bnorm=int(v[0])**2+int(v[0])*int(v[1])+int(v[1])**2
print('NAIVE_POISSON_COUNTEREXAMPLE q=7 D=2 h=2 B1=',v.tolist(),'norm=',Bnorm,'suggested_S=',7**2*6*Bnorm,'actual_S=',11844)
print('EXPONENT alpha theta')
for a in [Fraction(3,4),Fraction(6,7),Fraction(1),Fraction(6,5),Fraction(3,2),Fraction(2)]:
    print(a,max(Fraction(1,2)+5*a/12,1-a/6))
for q,D in [(7,3),(7,6),(13,5)]:
    data=json.loads((HERE/'cells_all.json').read_text())
    print('BLIND_S',q,D,[(h,data[f'{q},{D},{h}']) for h in range(2*D+1)])
print('REPRODUCTION_COUNTS 83 positive-degree cells; two D=0 cells; growth grid 66 cells')
print('WORD: finite numerical values cannot refute a bound with an unspecified implied constant.')
