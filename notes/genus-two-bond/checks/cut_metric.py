#!/usr/bin/env python3
"""Author: codex:gpt-6-astra. Degree cuts, theta Gram and scalar-inner alternative."""
import numpy as np
import sympy as s
N=s.Matrix([[0,0,0],[1,0,0],[0,1,0]])
G=s.Matrix([[1101,282,195],[282,126,47],[195,47,39]])
D=G-N.T*G*N
print('THETA GRAM',G,'det',G.det(),'DEFECT',D,'rank',D.rank())
assert D.rank()==2 and G.det()>0
b=[(3+np.sqrt(21))/2,(3-np.sqrt(21))/2]
a=np.array([(v+sgn*1j*np.sqrt(20-v*v))/2 for v in b for sgn in [1,-1]])
rho=a/5
Gn=(4/5)/(1-rho.conj()[:,None]*rho[None,:])
np.set_printoptions(precision=9,suppress=True)
print('rho',rho,'NORMALIZED SCALAR GRAM',Gn,sep='\n')
assert np.linalg.eigvalsh(Gn).min()>0
Fn=np.diag(a/np.sqrt(5));err=Fn.conj().T@Gn@Fn-Gn
print('F-normal error max',abs(err).max())
assert abs(err).max()>0.1
Graw=Gn/(4/5); Dr=np.diag(rho)
assert np.max(abs(Graw-Dr.conj().T@Graw@Dr-np.ones((4,4))))<1e-12
T=s.symbols('T');P=1-3*T+7*T*T-15*T**3+25*T**4
f=T**4-3*T**3+7*T*T-15*T+25
assert s.expand(T**4*f.subs(T,1/T)-P)==0
for Q in [1+5*T*T,1+T+9*T*T+5*T**3+25*T**4,1+5*T+25*T*T+70*T**3+195*T**4+350*T**5+625*T**6+625*T**7+625*T**8]:assert s.gcd(P,Q)==1
print('ALL ASSERTIONS PASSED')
