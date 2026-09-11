"""Transfer-matrix (MPS) formulation of the Weil bound for quadratic Artin–Schreier curves.

Curve C: y^q - y = g(x),  g(x) = sum_{j=0}^J a_j x^{1+q^j}  (a_j in F_q).
#C(F_{q^n}) = q^n + sum_{a in F_q^*} S_n(a g),  S_n(g) = sum_{x in F_{q^n}} psi(Tr g(x)).
In a self-dual normal basis (exists for n odd) Frobenius is the cyclic shift and
Tr(x * x^{q^j}) = sum_i x_i x_{i+j}, so S_n = Tr(E^n) for the transfer matrix E of a
translation-invariant quadratic spin model on a ring of n sites with alphabet F_q.
Weil's RH for C  <=>  the nonzero eigenvalues of E have modulus sqrt(q).
This script checks S_n (brute force in F_{q^n}) against Tr(E^n)."""
import itertools, numpy as np, sys
def irreducible(q,n):
    # monic irreducible of degree n over F_q (q prime), sympy irreducibility test
    from sympy.polys.galoistools import gf_irreducible_p
    from sympy.polys.domains import ZZ
    for coeffs in itertools.product(range(q),repeat=n):
        f=list(coeffs)+[1]   # low->high
        if gf_irreducible_p([ZZ(c) for c in reversed(f)],q,ZZ): return f
def polymulmod(a,b,f,q):
    n=len(f)-1; r=[0]*(2*n-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b): r[i+j]=(r[i+j]+x*y)%q
    for d in range(2*n-2,n-1,-1):
        c=r[d]
        if c:
            for k in range(n+1): r[d-n+k]=(r[d-n+k]-c*f[k])%q
    return r[:n]
def polypow(a,e,f,q):
    n=len(f)-1; r=[1]+[0]*(n-1)
    while e:
        if e&1: r=polymulmod(r,a,f,q)
        a=polymulmod(a,a,f,q); e>>=1
    return r
def has_root_free_irreducible(f,q,n):
    # irreducible iff x^{q^n} = x mod f and gcd conditions; use: x^{q^k} != x for k<n dividing... simple test:
    x=[0,1]+[0]*(n-2)
    if polypow(x,q**n,f,q)!=x: return False
    for k in range(1,n):
        if n%k==0 and polypow(x,q**k,f,q)==x: return False
    return True
def trace(z,f,q,n):
    t=[0]*n; w=z
    for _ in range(n):
        t=[(u+v)%q for u,v in zip(t,w)]; w=polypow(w,q,f,q)
    assert all(c==0 for c in t[1:]), 'trace not in F_q'
    return t[0]
def S_bruteforce(q,n,a):
    f=irreducible(q,n); J=len(a)-1; tot=0
    for coeffs in itertools.product(range(q),repeat=n):
        x=list(coeffs); g=[0]*n
        for j,aj in enumerate(a):
            if aj:
                xq=polypow(x,q**j,f,q); term=polymulmod(x,xq,f,q)
                g=[(u+aj*v)%q for u,v in zip(g,term)]
        tot+=np.exp(2j*np.pi*trace(g,f,q,n)/q)
    return tot
def transfer(q,a):
    J=len(a)-1; states=list(itertools.product(range(q),repeat=max(J,1))); idx={s:i for i,s in enumerate(states)}
    E=np.zeros((len(states),len(states)),complex)
    for s in states:
        for xn in range(q):
            s2=(s+(xn,))[-max(J,1):] if J>0 else (xn,)
            w=a[0]*xn*xn + sum(a[j]*s[-j]*xn for j in range(1,J+1))
            E[idx[s2],idx[s]]+=np.exp(2j*np.pi*(w%q)/q)
    return E
if __name__=='__main__':
    for q,a,ns in ((3,[0,1],[2,3,4,5,6,7]),(3,[1,1],[3,5,7]),(5,[0,1],[2,3,4,5]),(3,[0,1,1],[3,5,7]),(3,[0,0,1],[3,5,7])):
        E=transfer(q,a); ev=np.linalg.eigvals(E); mods=sorted(set(np.round(abs(ev),6)),reverse=True)
        print(f'\nq={q}, g(x)=sum a_j x^(1+q^j) with a={a}: transfer matrix {E.shape[0]}x{E.shape[0]}, |eigenvalues| = {mods}, sqrt(q)={np.sqrt(q):.6f}')
        for n in ns:
            s=S_bruteforce(q,n,a); t=np.trace(np.linalg.matrix_power(E,n))
            print(f'   n={n}: S_n brute force = {s.real:+9.3f}{s.imag:+8.3f}i   Tr(E^n) = {t.real:+9.3f}{t.imag:+8.3f}i   |S_n|/q^(n/2) = {abs(s)/q**(n/2):.4f}')
