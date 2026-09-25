#!/usr/bin/env python3
# Author: codex:gpt-6-astra
"""Deterministic checks for astra-proofs.md; output only, no generated files."""
from pathlib import Path
import numpy as np
import mpmath as mp
from scipy.linalg import expm
from sympy import primerange

mp.mp.dps = 50
root = Path(__file__).resolve().parents[3]
gammas = np.load(root / 'data/zeros3000.npy')
print('DATA', len(gammas), 'positive ordinates; last =', gammas[-1])
print('MODE FACTORS, t=1')
for j in range(1, 4):
    gamma = mp.im(mp.zetazero(j))
    factor = mp.exp(-mp.mpf(1)/4 - 1j*gamma/2)
    print(j, 'gamma', mp.nstr(gamma, 28), 'factor', mp.nstr(factor, 28))

# Ordered physical modes m_{+gamma_1}, m_{-gamma_1}, ... .
gs = np.array([sg*g for g in gammas[:3] for sg in (1, -1)])
D = np.diag(np.exp(-.25 - .5j*gs))
Omega = np.kron(np.eye(3), np.array([[0, -1j], [1j, 0]]))
J = np.diag([-1j, 1j]*3)
Rc = np.kron(np.eye(3), np.array([[0, 1], [1, 0]]))
G = np.eye(6)
q = np.exp(-.5)
print('pairing error', np.max(abs(D.T @ Omega @ D-q*Omega)))
# First-slot-linear convention: form matrix x^T G conjugate(y).
print('metric error', np.max(abs(D.T @ G @ D.conj()-q*G)))
print('compatibility error', np.max(abs(Omega @ J @ Rc-G)))
assert np.allclose(D.T @ Omega @ D, q*Omega)
assert np.allclose(D.T @ G @ D.conj(), q*G)
assert np.allclose(Omega @ J @ Rc, G)

# Full jets, arbitrary block length, synthetic off-line partners.
for m in (1,2,3,4):
    N = np.diag(np.ones(m-1), 1)
    B = np.zeros((m,m), complex)
    for j in range(m):
        B[j,m-1-j] = (-1j)**m * (-1)**j
    Om = np.block([[np.zeros((m,m)), B], [-B.T, np.zeros((m,m))]])
    lam = (.3-1-14j)/2
    lam2 = -.5-lam
    A = np.block([[lam*np.eye(m)+N, np.zeros((m,m))],
                  [np.zeros((m,m)), lam2*np.eye(m)+N]])
    T = expm(A)
    err = np.max(abs(T.T@Om@T-q*Om))
    print('synthetic paired jet length', m, 'error', err)
    assert err < 1e-12

# Gaussian f(t)=(4*pi*a)^(-1/2) exp(-t^2/(4a)), a=1/50.
a = mp.mpf(1)/50
h0 = 1/mp.sqrt(8*mp.pi*a)
def h(t): return h0*mp.exp(-t*t/(8*a))
W = 2*mp.fsum(mp.exp(-a*mp.mpf(float(g))**2/2) for g in gammas)
ends = 2*mp.exp(a/8)
contact = -2*mp.log(mp.pi)*h0
arch = mp.quad(lambda r: mp.exp(-a*r*r/2)*mp.re(mp.digamma(mp.mpf(1)/4+1j*r/2)), [0,1,4,10,25,50,100, mp.inf])/mp.pi
prime = mp.mpf(0)
for p in primerange(2,1001):
    n=p
    while n<=1000:
        prime -= 4*mp.log(p)/mp.sqrt(n)*h(2*mp.log(n))
        n*=p
geom = ends+contact+arch+prime
print('GAUSSIAN a=1/50')
for name,value in [('W first 3000 positive and negative',W),('endpoints',ends),('contact',contact),('gamma',arch),('prime powers <=1000',prime),('geometric total',geom),('difference float-zero-data',W-geom)]:
    print(name,mp.nstr(value,35))
assert abs(W-geom)<mp.mpf('1e-14')
L = mp.log(1000)
kappa = L/a - mp.mpf(1)/2
prime_tail_bound = 4*h0*mp.exp(L/2-L*L/(2*a))*(a+a/(2*kappa))
print('analytic prime tail bound <=', mp.nstr(prime_tail_bound,15))
assert prime_tail_bound < mp.mpf('2.962e-518')

print('CM E:y^2=x^3-x')
for p in (5,13,17):
    count=1+sum(1 for x in range(p) for y in range(p) if (y*y-x*x*x+x)%p==0)
    primary=[]
    for aa in range(-int(np.sqrt(p)),int(np.sqrt(p))+1):
        for bb in range(1,int(np.sqrt(p))+1):
            if aa*aa+bb*bb==p and aa%2==1 and bb%2==0 and (aa+bb)%4==1:
                primary.append((aa,bb))
    aa,bb=primary[0]
    assert count==p+1-2*aa==(aa-1)**2+bb**2
    print(p,'alpha =',aa,'+',bb,'i; trace =',2*aa,'count =',count,'P coefficients =',[1,-2*aa,p])
    A=np.array([[aa,-bb],[bb,aa]])
    Om=np.array([[0,1],[-1,0]])
    assert np.array_equal(A.T@A,p*np.eye(2))
    assert np.array_equal(A.T@Om@A,p*Om)

print('ALL ASSERTIONS PASSED')
