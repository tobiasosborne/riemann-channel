#!/usr/bin/env python3
"""Independent numpy check of the orchestrator's stations (demos-core.js): the permutation network, the
golden-mean and cyclic-rule shifts, the Gram/metric identity, and the lattice-bump Gram matrix of the Weil
functional against the zero side. Run from the repo root: python3 notes/weil-tn-tutorial/lanes/check_core.py"""
import numpy as np, itertools, math
np.set_printoptions(precision=6, suppress=True)
# --- permutation (1 2 3)(4 5 6) with point letters: E on the doubled bond, Tr E^k = #Fix(sigma^k)
sig = [1,2,0,4,5,3]; n = len(sig)
E = np.zeros((n*n, n*n))
for a in range(n):
    E[sig[a]*n+sig[a], a*n+a] = 1
fix = lambda k: sum(1 for x in range(n) if (lambda j: [j := sig[j] for _ in range(k)][-1] if k else x)(x) == x)
tr = [round(np.trace(np.linalg.matrix_power(E, k))) for k in range(1, 13)]
fx = [fix(k) for k in range(1, 13)]
assert tr == fx, (tr, fx)
T = np.array([[fx[abs(i-j)-1] if i != j else n for j in range(8)] for i in range(8)])
ev = np.linalg.eigvalsh(T)
print('perm: Tr E^k = #Fix:', fx, '| Toeplitz(8) eig:', np.round(ev, 6), '| kernel dim', int((abs(ev) < 1e-9).sum()), '(expect 5: 3 distinct eigenvalues)')
# --- shifts
def shift(M, K=10):
    M = np.array(M, float); ev = np.linalg.eigvals(M); lmax = max(z.real for z in ev if abs(z.imag) < 1e-9)
    tr = [np.trace(np.linalg.matrix_power(M, l)).real for l in range(0, 15)]
    nu = [(tr[l] - lmax**l)/lmax**(l/2) for l in range(15)]; nu[0] = len(M) - 1
    mins = [np.linalg.eigvalsh(np.array([[nu[abs(i-j)] for j in range(k)] for i in range(k)])).min() for k in range(1, 15)]
    ret = [z for z in ev if abs(z - lmax) > 1e-9 and abs(z) > 1e-9]
    return lmax, nu, mins, ret
for name, M in [('golden', [[1,1],[1,0]]), ('cyc4', [[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]])]:
    lmax, nu, mins, ret = shift(M)
    print(f'{name}: lmax={lmax:.6f} r={math.sqrt(lmax):.4f} nu_0..8={np.round(nu[:9],3)} lambda_min(K=10)={mins[9]:.4f} retained |mu|={[round(abs(z),4) for z in ret]}')
# --- Gram/metric identity: E = V Lam V^{-1}, G = (V^{-1})^* V^{-1}, Tr(G^{-1} (E^j)^* G E^k) = t_{k-j}
kappa = 1.0; Nm = np.array([[0,1,0.4],[0,0,1],[0,0,0]]); V = np.eye(3) + kappa*Nm; Vi = np.linalg.inv(V)
Lam = np.diag(np.exp(1j*np.array([0.6, 2.1, -1.4]))); Em = V @ Lam @ Vi; G = Vi.conj().T @ Vi; Gi = np.linalg.inv(G)
K = 6; pw = [np.linalg.matrix_power(Em, j) for j in range(K)]; t = [np.trace(p) for p in pw]
Tm = np.array([[t[k-j] if k >= j else np.conj(t[j-k]) for k in range(K)] for j in range(K)])
met = np.array([[np.trace(Gi @ pw[j].conj().T @ G @ pw[k]) for k in range(K)] for j in range(K)])
naive = np.array([[np.trace(pw[j].conj().T @ pw[k]) for k in range(K)] for j in range(K)])
print('gram: traces', np.round(t[:4], 3), '| max|metric-T| =', f'{abs(met-Tm).max():.2e}', '| max|naive-T| =', f'{abs(naive-Tm).max():.3f}', '| eig T', np.round(np.linalg.eigvalsh(Tm), 4), '| E^*GE-G', f'{np.linalg.norm(Em.conj().T@G@Em-G)/np.linalg.norm(G):.1e}')
# --- lattice Gram of the Weil functional: bumps at log n, n in {1,2,3,4,6}, s = 0.08 (conventions of "The Weil Functional")
from math import log, sqrt, pi, exp, cosh
def primes_upto(N):
    s = bytearray([1])*(N+1); s[0:2] = b'\0\0'
    for i in range(2, int(N**.5)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(N+1) if s[i]]
PP = []
for p in primes_upto(200000):
    q = p
    while q <= 200000: PP.append((q, log(p)/sqrt(q), log(q))); q *= p
PP.sort()
def simpson(f, a, b, m):
    h = (b-a)/m; acc = f(a)+f(b)
    for i in range(1, m): acc += f(a+i*h)*(4 if i % 2 else 2)
    return acc*h/3
def W(D, s, A):
    g = lambda x: A*exp(-(x-D)**2/(2*s*s))
    pole = simpson(lambda x: g(x)*2*cosh(x/2), D-9*s, D+9*s, 1600)
    xmax = abs(D)+8*s; pr = sum(w*(g(ln)+g(-ln)) for (nn, w, ln) in PP if ln <= xmax)
    g0 = g(0); rho = lambda y: exp(y/2)/(exp(y)-exp(-y))
    integ = lambda y: 2.5*g0 if y < 1e-7 else (g(y)+g(-y))*rho(y) - g0*exp(-2*y)/y
    Y = max(abs(D)+9*s, 30); arch = g0*log(pi) + simpson(integ, 0, 1, max(400, 2*math.ceil(25/s))) + simpson(integ, 1, Y, min(60000, max(4000, 2*math.ceil(25*(Y-1)/s))))
    return pole - pr - arch
ns = [1,2,3,4,6]; s = 0.08; cs = [log(x) for x in ns]
Gm = np.array([[W(cs[i]-cs[j], s*sqrt(2), s*sqrt(pi)) for j in range(5)] for i in range(5)])
import re
zeros = [float(z) for z in re.search(r'ZEROS100 = \[([^\]]*)\]', open('notes/weil-tn-tutorial/data-riemann.js').read()).group(1).split(',')]
Z = np.array([[sum(2*2*pi*s*s*exp(-s*s*gm*gm)*math.cos(gm*(cs[i]-cs[j])) for gm in zeros) for j in range(5)] for i in range(5)])
print('riemann lattice Gram eig (primes):', ['%.5g' % v for v in np.linalg.eigvalsh(Gm)])
print('riemann lattice Gram eig (zeros): ', ['%.5g' % v for v in np.linalg.eigvalsh(Z)], '| max|G-Z| =', f'{abs(Gm-Z).max():.2e}')
