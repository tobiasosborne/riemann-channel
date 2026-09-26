#!/usr/bin/env python3
"""Independent exact convention check for Choi contraction and Heisenberg scale."""
import sympy as s
q=d=2
# Product channel E(A tensor X)=Tr(sigma A) X; complex offdiagonal entries
# test the conjugation/index convention, not just real diagonal data.
sigma=s.Matrix([[s.Rational(1,2),s.I/2],[-s.I/2,s.Rational(1,2)]])
rho=s.eye(d)/d
index=lambda i,a,b:(i*d+a)*d+b
J=s.zeros(q*d*d)
for i in range(q):
 for j in range(q):
  for a in range(d):
   for c in range(d):
    for b in range(d):
     for z in range(d):
      J[index(i,a,b),index(j,c,z)]=sigma[j,i]*int(a==b)*int(c==z)
assert J==J.conjugate().T
assert set(J.eigenvals()).issubset({s.Integer(0),s.Integer(2)})
assert s.trace(J)==d

def E(A,X):
 return s.Matrix(d,d,lambda b,z:sum(A[i,j]*X[a,c]*J[index(i,a,b),index(j,c,z)]
           for i in range(q) for j in range(q) for a in range(d) for c in range(d)))
assert E(s.eye(q),s.eye(d))==s.eye(d)
for a in range(d):
 for c in range(d):
  X=s.zeros(d); X[a,c]=1
  assert s.trace(rho*E(s.eye(q),X))==s.trace(rho*X)
h=s.Matrix([[1,0,0,0],[0,-1,2,0],[0,2,-1,0],[0,0,0,1]])/4
energy=0
for i in range(q):
 for j in range(q):
  for k in range(q):
   for l in range(q):
    energy += h[i*q+k,j*q+l]*sum(rho[z,b]*J[index(i,a,b),index(j,c,z)]*J[index(k,t,a),index(l,t,c)]
       for a in range(d) for b in range(d) for c in range(d) for z in range(d) for t in range(d))
assert s.simplify(energy-s.trace(s.kronecker_product(sigma,sigma)*h))==0
assert energy==s.Rational(1,4)
assert h.eigenvals()=={s.Rational(1,4):3,s.Rational(-3,4):1}
print('PASS: exact Choi Hermiticity/positivity, trace, unitality and stationary functional.')
print('PASS: exact cubic energy contraction equals product-state energy 1/4, including complex offdiagonal signs.')
print('PASS: Heisenberg local spectrum {-3/4, 1/4, 1/4, 1/4}.')
