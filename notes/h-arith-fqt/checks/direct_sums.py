# Author: codex:gpt-6-astra
"""Primitive-row constant terms: enumerate residues, truncate degree and infinity shells."""
import sys
sys.dont_write_bytecode = True
from finite_graph import Field
from verify_scattering import characters,completed,val,phi
import numpy as np

def poly(n,q):
    a=[]
    while n:a.append(n%q);n//=q
    return a

def rem(a,b,q):
    a=a[:]
    while a and a[-1]==0:a.pop()
    while len(a)>=len(b):
        t=a[-1]*pow(b[-1],-1,q)%q;k=len(a)-len(b)
        for j,c in enumerate(b):a[k+j]=(a[k+j]-t*c)%q
        while a and a[-1]==0:a.pop()
    return a

def coprime(a,b,q):
    while b:a,b=b,rem(a,b,q)
    return len(a)==1

def fieldres(a,f):return sum(x*f.q**j for j,x in enumerate(rem(a,f.N,f.q)))

if __name__=='__main__':
    for q,N in [(2,[0,1]),(2,[1,1,1]),(2,[1,1,0,1]),(3,[0,1]),(3,[1,0,1]),(3,[2,2,0,1])]:
        f=Field(q,N);chi=characters(f)[q-1] if f.d>1 else [0]+[1]*(q-1);co=completed(f,chi) if f.d>1 else None;M=5;J=6;rows=[]
        for n in range(M+1):
            for k in range(q**n):
                a=poly(q**n+k,q);res=fieldres(a,f)
                units=[b for b in range(q**n) if coprime(a,poly(b,q),q)]
                # Each b represents one primitive row modulo unipotent translates.
                count=len(units);diag=sum(np.conj(chi[fieldres(poly(b,q),f)]) for b in units) if res==0 else 0
                assert f.d==1 or abs(diag)<1e-10
                rows.append((n,res,count))
        for u in (.17,.23):
            integral=q+(q-1)*sum((q*u*u)**j for j in range(1,J+1))
            approx=u**f.d*integral*sum(chi[a]*count*u**(2*n) for n,a,count in rows)
            exact=q*u**f.d*val(co,q*u*u)/val(co,u*u) if f.d>1 else phi(q,f.d,u)[0,1]
            rho=q*q*u*u;I=q*(1-u*u)/(1-q*u*u)
            bound=u**f.d*(I*rho**(M+1)/(1-rho)+(q-1)*(q*u*u)**(J+1)/(1-q*u*u)/(1-rho))
            diagapprox=integral*sum(count*u**(2*n) for n,a,count in rows if a==0)
            diagexact=phi(q,f.d,u)[0,0]
            diagbound=I*rho**(M+1)/(1-rho)+(q-1)*(q*u*u)**(J+1)/(1-q*u*u)/(1-rho)
            assert abs(approx-exact)<=bound+1e-12
            assert abs(diagapprox-diagexact)<=diagbound+1e-12
            print('q,d,u',q,f.d,u,'primitive residue rows',sum(x[2] for x in rows),'offdiag error/bound',abs(approx-exact),bound,'diagonal error/bound',abs(diagapprox-diagexact),diagbound)
