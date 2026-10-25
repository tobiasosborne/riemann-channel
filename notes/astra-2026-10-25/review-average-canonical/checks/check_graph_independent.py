#!/usr/bin/env python3
"""Hashimoto closed-walk counting and formal Schur functions over Q(sqrt(2))."""
from pathlib import Path
import sympy as s
H=Path(__file__).resolve().parent;lines=[]
def emit(*a):v=' '.join(map(str,a));lines.append(v);print(v,flush=True)
def graph(kind,m=0):
 if kind=='K4':return [[j for j in range(4) if i!=j] for i in range(4)]
 return [[(i-1)%m+m*b,(i+1)%m+m*b,i+m*(1-b)] for b in range(2) for i in range(m)]
def hashimoto(adj,K):
 edges=[(i,j) for i,ns in enumerate(adj) for j in ns];index={e:k for k,e in enumerate(edges)}
 nxt=[[index[v,w] for w in adj[v] if w!=u] for u,v in edges];tr=[len(edges)]+[0]*K
 for start in range(len(edges)):
  v=[0]*len(edges);v[start]=1
  for k in range(1,K+1):
   w=[0]*len(edges)
   for a,c in enumerate(v):
    for b in nxt[a]:w[b]+=c
   v=w;tr[k]+=v[start]
 return tr
Kfield=s.QQ.algebraic_field(s.sqrt(2));zero=Kfield.zero;one=Kfield.one
def divseries(a,b,n):
 r=[]
 for k in range(n):r.append(((a[k] if k<len(a) else zero)-sum((b[j]*r[k-j] for j in range(1,min(k+1,len(b)))),zero))/b[0])
 return r
def formal_schur(c):
 n=len(c)-1;F=[one]+[2*v/c[0] for v in c[1:]]
 f=divseries(F[1:],[2*one]+F[1:],n);out=[]
 while f:
  a=f[0];out.append(Kfield.to_sympy(a));r=one-a*a
  if r==zero:
   assert all(v==zero for v in f[1:]),'inconsistent terminal';return out,'terminal'
  if Kfield.to_sympy(r)<0:return out,'bad'
  f=divseries(f[1:],[r]+[-a*v for v in f[1:]],len(f)-1)
 return out,'unfinished'
for name,m in [('K4',0),('prism',16),('prism',17)]:
 adj=graph(name,m);n=len(adj);e=sum(map(len,adj))//2;tr=hashimoto(adj,16);bip=name=='prism' and m%2==0
 raw=[tr[k]-(e-n)*(1+(-1)**k)-(2**k+1)*(1+((-1)**k if bip else 0)) for k in range(17)]
 c=[Kfield.convert(v)/Kfield.convert(s.sqrt(2))**k for k,v in enumerate(raw)]
 aa,status=formal_schur(c)
 emit(name,m,'Hashimoto traces k0..4=',tr[:5],'retained unnormalized traces=',raw)
 emit('alpha=',aa,'status=',status,'last index=',len(aa)-1)
 if name=='K4':assert aa==[-s.sqrt(2)/4,-1]
 if m==16:assert len(aa)==14 and aa[-1]==s.Rational(43707967,3998190)
 if m==17:assert len(aa)==9 and aa[-1]==-s.Rational(413023893,312857602)*s.sqrt(2)
 if m:
  A=s.zeros(n)
  for i,ns in enumerate(adj):
   for j in ns:A[i,j]=1
  x=s.symbols('x');cp=A.charpoly(x).as_poly();cp=cp.exquo(s.Poly(x-3,x))
  if bip:cp=cp.exquo(s.Poly(x+3,x))
  intervals=cp.intervals(eps=s.Rational(1,10**12))
  assert all((max(a*a,b*b)<8) or (a*b>0 and min(a*a,b*b)>8) for (a,b),mult in intervals)
  outside=sum(mult for (a,b),mult in intervals if a*b>0 and min(a*a,b*b)>8)
  emit('exact out-of-band adjacency multiplicity=',outside);assert outside==4
# Fully symbolic identities, including both graph label orders.
lam,q=s.symbols('lambda q',real=True,nonzero=True);J=s.Matrix([[0,1],[-1,0]]);M=s.Matrix([[lam,-q],[1,0]]);C=s.Matrix([[0,-1],[1,0]])
Q=s.simplify(J*(M-q*M.inv())/2)
assert M.T*J*M==q*J
assert s.simplify(M.T*Q*M-q*Q)==s.zeros(2)
emit('conjugate label M=',C*M*C.inv(),'Q=',Q,'old-label Q=',C.inv().T*Q*C.inv())
z,a,b=s.symbols('z a b');T=s.Matrix([[z,-b],[-a*z,1]])
assert s.simplify(T.T*J*T-z*(1-a*b)*J)==s.zeros(2)
emit('universal alternating identity T^t J T=det(T) J; Szego det=',s.factor(T.det()))
(H/'output_graph_independent.txt').write_text('\n'.join(lines)+'\n')
