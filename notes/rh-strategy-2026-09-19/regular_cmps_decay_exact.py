#!/usr/bin/env python3
"""Exact algebra for the regular mixed-stationary cMPS decay toy."""
import sympy as s
X=s.Matrix([[0,1],[1,0]]); Z=s.diag(1,-1); r=s.Matrix([[0,1],[0,0]])
H=s.diag(X/2,(X+Z)/2); R=s.kronecker_product(X,r); P=s.diag(1,1,-1,-1)
Q=-s.I*H-R.adjoint()*R/2
basis=[]; odd=[]; even=[]
for j in range(4):
 for i in range(4):
  E=s.zeros(4); E[i,j]=1; basis.append(E)
  (odd if P[i,i]!=P[j,j] else even).append(len(basis)-1)
def vec(A): return s.Matrix([A[i,j] for j in range(4) for i in range(4)])
L=s.Matrix.hstack(*[vec(Q*E+E*Q.adjoint()+R*E*R.adjoint()) for E in basis])
z=s.symbols('z')
print('EXACT ODD CHARACTERISTIC POLYNOMIAL:'); print(s.factor(L.extract(odd,odd).charpoly(z).as_expr()))
print('EXACT EVEN CHARACTERISTIC POLYNOMIAL:'); print(s.factor(L.extract(even,even).charpoly(z).as_expr()))
ns=L.nullspace(); assert len(ns)==1
rho=s.Matrix(4,4,lambda i,j: ns[0][i+4*j]); rho=rho/s.trace(rho)
print('EXACT STATIONARY DENSITY:'); print(rho)
print('STATIONARY CHARACTERISTIC POLYNOMIAL:'); print(s.factor(rho.charpoly(z).as_expr()))
assert R*R==s.zeros(4)
assert s.simplify(L*vec(rho))==s.zeros(16,1)
assert rho==rho.adjoint()
print('JUMP SQUARED ZERO AND EXACT STATIONARITY: True')
slow=(z+s.Rational(1,4))**4+s.Rational(11,8)*(z+s.Rational(1,4))**2+s.Rational(9,256)
fast=(z+s.Rational(3,4))**4+s.Rational(11,8)*(z+s.Rational(3,4))**2+s.Rational(9,256)
assert s.expand(slow*fast-L.extract(odd,odd).charpoly(z).as_expr())==0
assert s.gcd(slow,fast)==1
print('SLOW POLYNOMIAL:',s.expand(slow))
print('FAST POLYNOMIAL:',s.expand(fast))
print('SLOW/FAST COPRIME: True')
print('PASS')
# One-fermion two-point function with creation at the left endpoint.
# Sign/insertion convention: refs/src/1211.3935/calculus.tex:388-403.
Leta=s.Matrix.hstack(*[vec(Q*E+E*Q.adjoint()-R*E*R.adjoint()) for E in basis])
source=vec(R*rho).extract(odd,[0])
sink=s.Matrix([[s.trace(R.adjoint()*basis[k]) for k in odd]])
resolvent=(z*s.eye(len(odd))-Leta.extract(odd,odd)).inv()*source
correlation=s.factor((sink*resolvent)[0])
print('PHYSICAL FERMION TWO-POINT RESOLVENT:'); print(correlation)
expected=8*z*(z**2+z+1)/(5*(8*z**4+8*z**3+14*z**2+6*z+1))
assert s.cancel(correlation-expected)==0
num,den=s.fraction(correlation)
assert s.degree(den,z)==4
assert s.degree(s.gcd(den,s.diff(den,z)),z)==0
print('EXACT FOUR-POLE CORRELATION IDENTITY AND SIMPLE POLES: True')
A=Leta.extract(odd,odd)
reach=s.Matrix.hstack(*[(A**k)*source for k in range(8)])
observe=s.Matrix.vstack(*[sink*(A**k) for k in range(8)])
print('SOURCE REACHABLE DIMENSION:',reach.rank())
print('SINK OBSERVABLE DIMENSION:',observe.rank())
assert s.gcd(s.fraction(correlation)[0],s.fraction(correlation)[1])==1
print('NUMERATOR/DENOMINATOR COPRIME: True')
K=A+s.eye(8)/4
V=s.Matrix.hstack(*[(K**k)*source for k in range(4)])
Kcomp=s.Matrix([[0,0,0,-s.Rational(9,256)],[1,0,0,0],[0,1,0,-s.Rational(11,8)],[0,0,1,0]])
assert V.rank()==4
assert s.simplify(K*V-V*Kcomp)==s.zeros(8,4)
G=s.Matrix([[s.Rational(10496,27),0,-s.Rational(32,3),0],[0,s.Rational(32,3),0,-1],[-s.Rational(32,3),0,1,0],[0,-1,0,1]])
assert Kcomp.T*G+G*Kcomp==s.zeros(4)
minors=[G[:k,:k].det() for k in range(1,5)]
assert all(g>0 for g in minors)
print('LETTER/INSERTION KRYLOV METRIC:'); print(G)
print('POSITIVE LEADING PRINCIPAL MINORS:',minors)
print('EXACT CENTERED SKEW-ADJOINT IDENTITY ON REACHABLE SUBSPACE: True')
