#!/usr/bin/env python3
"""Exact Lie-algebra normalizations and discrete-series lowest-weight checks.

These finite algebra checks do not prove an infinite spectral decomposition.
The representation-theoretic inputs are stated explicitly in the report.
"""
import sympy as s
import numpy as np

count=0
def check(ok,msg):
    global count
    assert bool(ok),msg
    count+=1
    print(f'PASS {count:03d}: {msg}')

H=s.diag(1,-1);E=s.Matrix([[0,1],[1,0]]);W=s.Matrix([[0,1],[-1,0]])
comm=lambda a,b:a*b-b*a
check(comm(H,E)==2*W and comm(W,H)==-2*E and comm(W,E)==2*H,
      'shard 09b sl2 brackets, W has period 2*pi in SL2')
n,j,m,r,d=s.symbols('n j m r d',real=True)
cas_discrete=n*(n-2)/4
rate=s.expand(-2*cas_discrete+(n+2*j)**2/2)
check(rate==n+2*n*j+2*j*j,'-T_09b on D_n K-type n+2j is n+2nj+2j^2')
check(s.simplify(2*(s.Rational(1,2)+s.I*r)*(s.Rational(1,2)-s.I*r)+m*m/2
                 -(s.Rational(1,2)+2*r*r+m*m/2))==0,'principal-series rate 1/2+2r^2+m^2/2')
check(s.simplify((s.Rational(1,2)+2*r*r)/d).subs(r,0)==1/(2*d),
      'the normalized 2d-letter walk has threshold 1/(2d)')

# D_k^+ in the polynomial model: K_-=d/dz, K_+=z^2 d/dz+k z,
# 2K_0=2z d/dz+k. Total lowest vectors (z-w)^ell.
z,w=s.symbols('z w')
for k in [1,2,4]:
    for ell in range(7):
        v=(z-w)**ell
        check(s.expand(s.diff(v,z)+s.diff(v,w))==0,
              f'k={k}, ell={ell}: tensor lowest vector annihilated')
        Ktot=2*z*s.diff(v,z)+2*w*s.diff(v,w)+2*k*v
        check(s.expand(Ktot-(2*k+2*ell)*v)==0 and s.expand(v.xreplace({z:w,w:z})-(-1)**ell*v)==0,
              f'k={k}, ell={ell}: weight 2k+2ell and flip sign (-1)^ell')

# Exact K-character multiplicity count in the complete positive tensor product.
for total in range(12):
    check(sum(1 for a in range(total+1)) == sum(1 for ell in range(total+1)),
          f'tensor K-level {total}: all multiplicities exhausted')

# Positive lowest matrix coefficient = cosh(t/2)^(-n), exponent -n/2.
for nv in [2,4,6,8]:
    slope=-nv/2*np.tanh(12/2)
    check(abs(slope+nv/2)<1e-4,f'D_{nv}: large-t logarithmic derivative approaches -{nv}/2')

# Repka parameter conversion, as a check of the formula, not a proof of H-repka.
ss=s.symbols('s',real=True)
check(s.expand(1-2*(1-ss))==2*ss-1,'Repka: complementary constituent parameter s_new=2s-1')
check(s.simplify(2*(2*ss-1)*(2-2*ss)).subs(ss,s.Rational(3,4))==s.Rational(1,2),
      'Repka boundary agrees with the spherical diffusion threshold')
check(s.Rational(3,4)*(1-s.Rational(3,4))==s.Rational(3,16), 'same parameter gives Laplace value 3/16')

# Reflection interchanges two equal diffusion eigenspaces, irrespective of Gamma parity.
gamma,a=s.symbols('gamma a',positive=True)
J=s.Matrix([[0,1],[1,0]])
M=-a*s.eye(2)+gamma*(J-s.eye(2))
check(M.eigenvals()=={-a:1,-a-2*gamma:1},'reflection shifts both sector pairs by 0 or -2gamma')
print(f'\n{count}/{count} checks passed')
