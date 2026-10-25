#!/usr/bin/env python3
"""Exhaustive targeted genus-5 hyperelliptic comparison over F3.

All genus-5 hyperelliptics have y^2=f(x), squarefree degree 11 or12.
Every K5 target has N2=20, the hyperelliptic maximum over F9. Odd degree
has just one infinity point and at most18 affine points, hence is excluded.
Enumerate ALL 2*3^12 degree12 equations, with no quotient or random sample.
Filter exact counts over F_{3^k}, k<=5; test squarefreeness on matches.
"""
import contextlib
from pathlib import Path
import itertools
import json
import numpy as np
import sympy as S

HERE=Path(__file__).resolve().parent
x=S.Symbol('x')

def digits(n,k):
    a=[]
    for _ in range(k): a.append(n%3);n//=3
    return a

class F3Field:
    def __init__(self,k):
        self.k=k;self.q=3**k
        if k==1: self.mod=[0,1]
        else:
            for code in range(1,3**k):
                a=digits(code,k)+[1]
                if S.Poly(sum(v*x**i for i,v in enumerate(a)),x,modulus=3).is_irreducible:
                    self.mod=a;break
        vals=[digits(a,k) for a in range(self.q)]
        self.add=np.array([[sum(((a+b)%3)*3**i for i,(a,b) in enumerate(zip(A,B))) for B in vals] for A in vals],dtype=np.int64)
        self.mul=np.array([[self.mult(A,B) for B in vals] for A in vals],dtype=np.int64)
        self.chi=np.zeros(self.q,dtype=np.int64)
        for a in range(1,self.q):
            b=self.power(a,(self.q-1)//2)
            assert b in (1,2)
            self.chi[a]=1 if b==1 else -1
    def mult(self,A,B):
        c=[0]*(2*self.k-1)
        for i,a in enumerate(A):
            for j,b in enumerate(B): c[i+j]=(c[i+j]+a*b)%3
        for d in range(len(c)-1,self.k-1,-1):
            a=c[d]
            for j,b in enumerate(self.mod): c[d-self.k+j]=(c[d-self.k+j]-a*b)%3
        return sum(a*3**i for i,a in enumerate(c[:self.k]))
    def power(self,a,n):
        r=1
        while n:
            if n&1:r=int(self.mul[r,a])
            a=int(self.mul[a,a]);n>>=1
        return r
    def counts(self,coeff):
        X=np.arange(self.q,dtype=np.int64)[None,:]
        Y=np.zeros((len(coeff),self.q),dtype=np.int64)
        for j in range(coeff.shape[1]-1,-1,-1):
            Y=self.add[self.mul[Y,X],coeff[:,j,None]]
        return self.q+1+self.chi[Y].sum(axis=1)+self.chi[coeff[:,-1]]

def main():
    flux=json.loads((HERE/'output_fluxes.json.txt').read_text())
    targets={r['mask']:[r['N'][str(k)] for k in range(1,6)] for r in flux if r['graph']=='K5' and r['ramanujan']}
    fields=[F3Field(k) for k in range(1,6)]
    for field in fields: print('FIELD degree='+str(field.k)+' modulus='+str(field.mod),flush=True)
    survivors=[0]*5; hits={m:[] for m in targets}; singular={m:0 for m in targets}
    for start in range(0,2*3**12,8192):
        ids=np.arange(start,min(start+8192,2*3**12),dtype=np.int64)
        coeff=np.stack([(ids//3**i)%3 for i in range(12)]+[ids//3**12+1],axis=1)
        seq=np.empty((len(ids),0),dtype=np.int64)
        for k,field in enumerate(fields):
            if len(coeff)==0:break
            counts=field.counts(coeff)
            seq=np.column_stack((seq,counts))
            keep=np.zeros(len(coeff),dtype=bool)
            for tar in targets.values(): keep|=np.all(seq==np.array(tar[:k+1]),axis=1)
            coeff=coeff[keep];seq=seq[keep];survivors[k]+=len(coeff)
        for C,N in zip(coeff,seq):
            f=S.Poly(sum(int(c)*x**i for i,c in enumerate(C)),x,modulus=3)
            squarefree=S.gcd(f,f.diff()).degree()==0
            for m,tar in targets.items():
                if N.tolist()!=tar:continue
                if not squarefree:singular[m]+=1
                else:hits[m].append(C.tolist())
    print('degree12 equations considered='+str(2*3**12))
    print('successive point-count prefix survivors='+str(survivors))
    for m,tar in targets.items():
        print(f'K5:{m} target={tar}; smooth matching equations={len(hits[m])}; singular matches={singular[m]}')
        if hits[m]:print('  witness coefficients low-to-high='+str(hits[m][0]))
    (HERE/'output_hyperelliptic_f3.json.txt').write_text(json.dumps(dict(targets=targets,survivors=survivors,hits=hits,singular=singular),indent=2)+'\n')

if __name__=='__main__':
    with (HERE/'output_hyperelliptic_f3.txt').open('w') as f,contextlib.redirect_stdout(f):main()
    print((HERE/'output_hyperelliptic_f3.txt').read_text())
