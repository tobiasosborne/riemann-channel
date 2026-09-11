import numpy as np, mpmath as mp
from sympy import primerange
mp.mp.dps=20
def primes(P): return list(primerange(2,P))
def transfer(p,b,beta,K=60):
    # bond = residues mod b; local occupation k with Gibbs weight (1-p^-beta) p^{-beta k}; bond map r -> p^k r mod b
    E=np.zeros((b,b))
    for k in range(K):
        w=(1-p**-beta)*p**(-beta*k)
        for r in range(b): E[(pow(p,k,b)*r)%b, r]+=w
    return E
def phi_mpo(a,b,beta,P):
    v=np.zeros(b); v[1%b]=1.0            # boundary vector: residue 1
    for p in primes(P): v=transfer(p,b,beta)@v
    return sum(np.exp(2j*np.pi*a*r/b)*v[r] for r in range(b))
def phi_exact(a,b,beta):
    z=mp.zeta(beta)
    s=sum(mp.exp(2j*mp.pi*a*r/b)*b**(-beta)*mp.zeta(beta, mp.mpf(r)/b if r else 1) for r in range(1,b+1))
    return complex(s/z)
for (a,b,beta) in [(1,3,2.0),(1,4,2.0),(2,5,1.5),(1,6,1.7)]:
    m=phi_mpo(a,b,beta,200000); e=phi_exact(a,b,beta)
    print(f'a/b={a}/{b} beta={beta}: MPO={m:.6f}  exact={e:.6f}  |diff|={abs(m-e):.1e}')
# character sectors: eigenvalues of total transfer on units mod 5 vs L(beta,chi)/zeta(beta)
b,beta=5,1.5
Etot=np.eye(b)
for p in primes(200000): Etot=transfer(p,b,beta)@Etot
# restrict to units {1,2,3,4}: generator 2; characters chi_j(2^t)=i^{jt}
units=[1,2,3,4]; 
for j in range(4):
    chi={pow(2,t,5):1j**(j*t) for t in range(4)}
    vec=np.array([chi[r] for r in units]); sub=Etot[np.ix_(units,units)]
    lam=(sub@vec)/vec
    chivals=[chi[r%5] if r%5 else 0 for r in range(5)]
    L=mp.dirichlet(beta, chivals)   # mpmath: dirichlet(s, chi) with chi periodic values
    print(f'chi_{j}: transfer eigenvalue={lam[0]:.6f} (spread {np.ptp(abs(lam)):.1e}),  L(beta,chi)/zeta(beta)={complex(L/mp.zeta(beta)):.6f}')
