#!/usr/bin/env python3
"""Fable's scratch checks for the partial review of lanes R, S, U (written from the statements, not from the lane scripts)."""
import itertools, sympy as sp
# S1: counts of y^4 = t^4 + 1 over F_5, F_25, F_125 (affine + 4 rational places at infinity, lane S's claim)
p=5
def field(deg):
    # F_{5^deg} as polynomials mod an irreducible: deg 1: x; 2: x^2-2; 3: x^3+x+1
    mods={1:[0,1],2:[3,0,1],3:[1,1,0,1]}[deg]  # coefficients low->high of the modulus
    n=deg
    def mul(a,b):
        r=[0]*(2*n-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): r[i+j]=(r[i+j]+x*y)%p
        for k in range(2*n-2,n-1,-1):   # reduce x^k using modulus (monic)
            c=r[k]
            if c:
                for i in range(n+1): r[k-n+i]=(r[k-n+i]-c*mods[i])%p
        return tuple(r[:n])
    elts=[tuple(v) for v in itertools.product(range(p),repeat=n)]
    return elts,mul
def count(deg):
    elts,mul=field(deg)
    def pw(a,k):
        r=tuple([1]+[0]*(deg-1))
        for _ in range(k): r=mul(r,a)
        return r
    one=tuple([1]+[0]*(deg-1))
    fourth={}
    for y in elts:
        fourth.setdefault(pw(y,4),0); fourth[pw(y,4)]+=1
    aff=0
    for t in elts:
        rhs=tuple((a+b)%p for a,b in zip(pw(t,4),one))
        aff+=fourth.get(rhs,0)
    return aff+4
u=sp.symbols('u'); L=sp.expand((1+2*u+5*u**2)**2*(1-2*u+5*u**2))
roots=sp.Poly(sp.expand(u**6*L.subs(u,1/u)),u).nroots()
for k in (1,2,3):
    predicted=5**k+1-round(sum(complex(r)**k for r in roots).real)
    print(f"S1 k={k}: brute-force #C = {count(k)}, from L_C = {predicted}")
# U-K3: intertwiners g mod 8 between the companion steps of (1,0,6) and (2,0,3) at q = 7 (M = [[(a-B)/2, -C],[A,(a+B)/2]], a = 2)
def step(A,B,C,a): return sp.Matrix([[(a-B)//2,-C],[A,(a+B)//2]])
M1,M2=step(1,0,6,2),step(2,0,3,2)
dets=set()
for a,b,c,d in itertools.product(range(8),repeat=4):
    g=sp.Matrix([[a,b],[c,d]])
    if all(x%8==0 for x in (g*M1-M2*g)) and sp.gcd(int(g.det())%8,8)==1: dets.add(int(g.det())%8)
print("U-K3: determinants mod 8 of invertible intertwiners g M_(1,0,6) = M_(2,0,3) g:", sorted(dets), "(lane U: {3,5}, never +-1)")
# U-S2: (1 - M^k)(1 - V^k) = h_k for one mode; Lambda^perp = (1-M^k)^{-1} L
Om=sp.Matrix([[0,1],[-1,0]])
for name,M,q in (("E1",sp.Matrix([[0,-1],[2,-1]]),2),("(1,0,6)",M1,7),("(2,0,3)",M2,7)):
    V=q*M.inv(); ok=True
    for k in range(1,7):
        h=(sp.eye(2)-M**k).det(); ok&=((sp.eye(2)-M**k)*(sp.eye(2)-V**k)==h*sp.eye(2))
        B=sp.eye(2)-V**k; Z=((B.T*Om).inv()).inv()*(sp.eye(2)-M**k).inv(); ok&=(all(x.is_integer for x in Z) and abs(Z.det())==1)
    print(f"U-S1/S2 {name}: (1-M^k)(1-V^k) = h_k and Lambda_k^perp = (1-M^k)^{{-1}}L for k<=6:", ok)
# R-A2: translation invariance of the zero-sum form: |hhat(gamma) e^{i gamma t}|^2 = |hhat(gamma)|^2, trivially; checked numerically on one packet
import numpy as np
g=np.load('data/zeros3000.npy')[:50]
def Z(h,t):  # h: Gaussian packet in u = log x, translated by t
    u=np.linspace(-3,3,120001); hu=np.exp(-(u-t)**2/(2*0.03**2))
    hh=np.array([np.trapezoid(hu*np.exp(1j*gam*u),u) for gam in g]); return np.sum(np.abs(hh)**2)
z0,z1=Z(None,0.0),Z(None,np.log(2))
print(f"R-A2: zero-sum form of a Gaussian packet, t=0: {z0:.10f}, t=log 2: {z1:.10f}, relative difference {abs(z0-z1)/z0:.1e}")
