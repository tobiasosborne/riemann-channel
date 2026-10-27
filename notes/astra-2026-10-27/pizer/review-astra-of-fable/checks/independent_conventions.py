#!/usr/bin/env python3
"""Small exact convention certificates, including the sign of the quaternion trace determinant."""
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
O=s.Matrix([[s.Rational(1,2),0,s.Rational(1,2),s.Rational(1,2)],
            [0,s.Rational(1,4),s.Rational(1,2),s.Rational(3,4)],
            [0,0,1,0],[0,0,0,1]]).T
G=2*O.T*s.diag(1,-2,-37,-74)*O
assert G.det()==-37**2
print('Quaternion reduced-trace Gram determinant:',G.det(),'; absolute value:',abs(G.det()))
for p,ws in [(11,[2,3]),(37,[1]*3),(73,[1]*6),(101,[3]+[1]*8),(109,[1]*9)]:
 n=len(ws);Z=s.Matrix.vstack(s.eye(n-1),-s.ones(1,n-1));C=Z.T*s.diag(*ws)*Z
 mass=sum(s.Rational(1,w) for w in ws)
 assert C.det()==s.prod(ws)*mass
 print('p',p,'weights',ws,'weighted cycle determinant',C.det(),'Gram Smith',list(smith_normal_form(C,domain=s.ZZ).diagonal()),'doubled alternating determinant',C.det()**2)
l=2;M=s.Matrix([[l+1,-l],[1,0]])
print('Trivial-plane companion at ell=2:',M.tolist(),'M(1,-1)=',list(M*s.Matrix([1,-1])),'M(1,1)=',list(M*s.Matrix([1,1])))
assert M*s.Matrix([1,1])==s.Matrix([1,1])
