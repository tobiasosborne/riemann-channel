#!/usr/bin/env python3
"""Author: codex:gpt-6-astra. Exact field, polarization and metric checks."""
import sympy as s
import numpy as np
x=s.symbols('x');f=x**4-3*x**3+7*x*x-15*x+25
def red(a):return s.rem(a,f,x)
def inv(a):return s.invert(a,f,x)
def tr(a):
    a=s.Poly(red(a),x)
    return sum(a.nth(i)*[4,3,-5,9][i] for i in range(4))
b=red(x+5*inv(x));delta=red(2*x-b);root21=2*b-3
assert red(b*b-3*b-3)==0
assert red(delta*delta-(3*b-17))==0
B=[s.Integer(1),b,x,red(b*x)]
M=s.Matrix([[tr(a*c) for c in B] for a in B]);print('BASIS',B,'TRACE GRAM',M,'DISC',M.det())
assert M.det()==48069
xi=inv(red(root21*delta));conj=lambda a:red(a.subs(x,5*inv(x)))
assert red(conj(xi)+xi)==0
E=s.Matrix([[tr(red(xi*a*conj(c))) for c in B] for a in B])
print('xi',s.factor(xi),'E',E,'DET',E.det())
assert E.det()==1 and E+E.T==s.zeros(4)
assert all(v.q==1 for v in E)
eta=(5+s.sqrt(21))/2
print('UNIT GAUGE multiplier',s.expand(eta**4))
d1=s.sqrt((25-3*s.sqrt(21))/2);d2=s.sqrt((25+3*s.sqrt(21))/2)
R=s.simplify(d2/d1)
print('REFERENCE c',s.N(1/(s.sqrt(21)*d1),15),s.N(1/(s.sqrt(21)*d2),15))
print('REFERENCE R',R,s.N(R,15),'R^2',s.radsimp(R**2))
print('inverse weights c and ratio',s.N(s.sqrt(21)*d1),s.N(s.sqrt(21)*d2),s.N(1/R))
print('IRREDUCIBLE MOD2',s.Poly(f,x,modulus=2).is_irreducible)
print('ALL ASSERTIONS PASSED')
