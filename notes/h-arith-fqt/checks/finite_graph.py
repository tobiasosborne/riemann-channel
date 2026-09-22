# Author: codex:gpt-6-astra
"""Exact prime-field polynomial arithmetic and double-coset quotient of the tree."""
from collections import Counter
from itertools import product
import numpy as np

class Field:
    def __init__(self,q,N):
        self.q=q; self.N=N; self.d=len(N)-1; self.Q=q**self.d
        self.vec=[[(a//q**i)%q for i in range(self.d)] for a in range(self.Q)]
        self.add=[[sum(((x+y)%q)*q**i for i,(x,y) in enumerate(zip(self.vec[a],self.vec[b]))) for b in range(self.Q)] for a in range(self.Q)]
        self.mul=[[self.product(a,b) for b in range(self.Q)] for a in range(self.Q)]
        self.inv=[0]+[next(b for b in range(1,self.Q) if self.mul[a][b]==1) for a in range(1,self.Q)]
    def product(self,a,b):
        q=self.q; c=[0]*(2*self.d-1)
        for i,x in enumerate(self.vec[a]):
            for j,y in enumerate(self.vec[b]): c[i+j]=(c[i+j]+x*y)%q
        for k in range(len(c)-1,self.d-1,-1):
            for j in range(self.d): c[k-self.d+j]=(c[k-self.d+j]-c[k]*self.N[j])%q
        return sum(c[i]*q**i for i in range(self.d))
    def power(self,a,n):
        r=1
        for _ in range(n):r=self.mul[r][a]
        return r
    def primitive(self):
        return next(a for a in range(1,self.Q) if len({self.power(a,k) for k in range(self.Q-1)})==self.Q-1)

def quotient(q,N,kind=1):
    f=Field(q,N); Q=f.Q; d=f.d; cut=d-1
    def canon(v):
        a,b=v
        if kind==0:
            x=a or b; t=f.inv[x]
            return (f.mul[a][t],f.mul[b][t])
        return min((f.mul[a][t],f.mul[b][t]) for t in range(1,q))
    omega=sorted({canon((a,b)) for a in range(Q) for b in range(Q) if a or b}); pos={v:i for i,v in enumerate(omega)}
    def act(v,g):
        a,b=v; x,y,z,w=g
        return canon((f.add[f.mul[a][x]][f.mul[b][z]],f.add[f.mul[a][y]][f.mul[b][w]]))
    diag=[(a,0,0,1) for a in range(1,q)]
    def upper(n):return diag+[(1,q**i if i<d else 0,0,1) for i in range(min(n,d-1)+1)]
    def orbits(gens):
        parent=list(range(len(omega)))
        def root(i):
            while parent[i]!=i: parent[i]=parent[parent[i]];i=parent[i]
            return i
        for g in gens:
            for i,v in enumerate(omega):
                a,b=root(i),root(pos[act(v,g)])
                if a!=b:parent[max(a,b)]=min(a,b)
        groups={}
        for i in range(len(omega)):groups.setdefault(root(i),[]).append(i)
        parts=list(groups.values()); lookup={j:i for i,p in enumerate(parts) for j in p}
        return parts,lookup
    V=[]; maps=[]; st=[]
    for n in range(cut+2):
        parts,lookup=orbits(upper(0)+[(0,1,1,0)] if n==0 else upper(n))
        order=q*(q*q-1) if n==0 else (q-1)*q**(n+1)
        V.append(parts);maps.append(lookup);st.append([order//len(p) for p in parts])
    E=[]
    for n in range(cut+1):
        parts,_=orbits(upper(n)); order=(q-1)*q**(n+1)
        E.append([(maps[n][p[0]],maps[n+1][p[0]],order//len(p)) for p in parts])
    offsets=np.cumsum([0]+[len(v) for v in V[:-1]]); nv=offsets[-1]
    TX=np.zeros((nv,nv)); W=np.zeros((nv,len(V[-1]))); tails=[]
    for n,edges in enumerate(E):
        for a,b,se in edges:
            t=np.sqrt(st[n][a]*st[n+1][b]/q)/se
            if n<cut:
                i,j=offsets[n]+a,offsets[n+1]+b;TX[i,j]+=t;TX[j,i]+=t
            else:W[offsets[n]+a,b]+=t
    for p in V[-1]:
        a,b=omega[p[0]]; tails.append((int(a!=0),a or b))
    return dict(f=f,V=V,st=st,E=E,TX=TX,W=W,tails=tails,omega=omega)

def scattering(g,z):
    T,W=g['TX'],g['W'];G=W.T@np.linalg.solve((z+1/z)*np.eye(len(T))-T,W)
    return np.linalg.solve(z*G-np.eye(G.shape[0]),np.eye(G.shape[0])-G/z)

CASES=[(2,[0,1]),(2,[1,1,1]),(2,[1,1,0,1]),(3,[0,1]),(3,[1,0,1]),(3,[2,2,0,1])]
if __name__=='__main__':
    for q,N in CASES:
        for kind in (0,1):
            g=quotient(q,N,kind)
            from fractions import Fraction
            degrees=[[Fraction(0) for _ in layer] for layer in g['V']]
            for n,edges in enumerate(g['E']):
                for a,b,se in edges:
                    degrees[n][a]+=Fraction(g['st'][n][a],se)
                    degrees[n+1][b]+=Fraction(g['st'][n+1][b],se)
            assert all(v==q+1 for layer in degrees[:-1] for v in layer)
            assert all(v==q for v in degrees[-1])
            print(q,N,'Gamma',kind,'V',[len(v) for v in g['V'][:-1]],'E',[len(e) for e in g['E'][:-1]],'h',len(g['tails']))
            print('stabilisers',[dict(Counter(s)) for s in g['st'][:-1]])
            print('edges',g['E'])
