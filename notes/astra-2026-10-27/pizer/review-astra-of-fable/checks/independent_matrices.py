#!/usr/bin/env python3
"""Independent PARI Smith forms (author used FLINT), simple-root basis,
Hecke power-sum recurrence, and Hashimoto determinants by walk traces.
Author: codex:gpt-6-astra.
"""
import ast,itertools,json,math,re
from pathlib import Path
import os
os.environ["SYMPY_GROUND_TYPES"]="python"
import sympy as s
from cypari2 import Pari
P=Pari();P.allocatemem(300000000,silent=True)
x=s.symbols('x');here=Path(__file__).resolve().parent;source=here.parents[1]/'fable/checks'
matrices={};p=None;weights={};hash_expected={};poly_expected={}
for line in (source/'output_pizer_graph.txt').read_text().splitlines():
 m=re.search(r'==== p = (\d+).*weights w = (\[.*?\])',line)
 if m:p=int(m[1]);weights[p]=ast.literal_eval(m[2])
 m=re.search(r'-- l = (\d+): B\(l\) = (\[.*\])',line)
 if m:l=int(m[1]);matrices[p,l]=s.Matrix(ast.literal_eval(m[2]))
 m=re.search(r'Hashimoto: N = (\d+).* f = (\d+)',line)
 if m:hash_expected[p,l]=(int(m[1]),int(m[2]))
 m=re.search(r'det\(1 - u B_H\) = (.*)',line)
 if m:poly_expected[p,l]=s.Poly(s.sympify(m[1].replace('^','**')),x)
expected={};p=l=None
for line in (source/'output_label_lattice.txt').read_text().splitlines():
 m=re.search(r'==== p = (\d+)',line)
 if m:p=int(m[1])
 m=re.search(r'-- l = (\d+)',line)
 if m:l=int(m[1])
 m=re.search(r'k = (\d+): L0/\(1-M\^k\)L0 = (.*?)\, order (\d+)',line)
 if m:expected[p,l,int(m[1])]=([int(z) for z in re.findall(r'Z/(\d+)',m[2])],int(m[3]))
def pari_matrix(A):return P.matrix(A.rows,A.cols,[int(z) for z in A])
def snf(A):return sorted(abs(int(v)) for v in P.matsnf(pari_matrix(A)) if abs(int(v))!=1)
def classno(D):
 forms=[]
 for a in range(1,math.isqrt(abs(D)//3)+2):
  for b in range(-a,a+1):
   if (b*b-D)%(4*a):continue
   c=(b*b-D)//(4*a)
   if a>c or (abs(b)==a or a==c) and b<0 or math.gcd(math.gcd(a,b),c)>1:continue
   forms.append((a,b,c))
 return len(forms)
def cm_fixed(p,l):
 discs=[-4*l]+([-l] if l%4==3 else [])
 return sum(classno(D)*(1-int(s.kronecker_symbol(D,p)))//2 for D in discs)
def make_arcs(A):
 arcs=[];rev=[];n=A.rows
 def pair(i,j):
  e=len(arcs);arcs.extend([(i,j),(j,i)]);rev.extend([e+1,e])
 for i in range(n):
  for j in range(i+1,n):
   for _ in range(int(A[i,j])):pair(i,j)
  for _ in range(int(A[i,i])//2):pair(i,i)
  if A[i,i]%2:rev.append(len(arcs));arcs.append((i,i))
 successors=[[j for j,b in enumerate(arcs) if a[1]==b[0] and rev[i]!=j] for i,a in enumerate(arcs)]
 return arcs,rev,successors
def walk_determinant(successors):
 N=len(successors);power=[[int(i==j) for j in range(N)] for i in range(N)];traces=[];coeff=[1]
 for k in range(1,N+1):
  nxt=[]
  for neigh in successors:
   row=[0]*N
   for j in neigh:
    prev=power[j]
    for h in range(N):row[h]+=prev[h]
   nxt.append(row)
  power=nxt;traces.append(sum(power[i][i] for i in range(N)))
  num=-sum(traces[j-1]*coeff[k-j] for j in range(1,k+1));assert num%k==0;coeff.append(num//k)
 return s.Poly.from_list(list(reversed(coeff)),x)

for (p,l),A in matrices.items():
 n=A.rows;W=s.diag(*weights[p]);Winv=W.inv();ones=s.ones(n,1)
 assert A*W==W*A.T and A*ones==(l+1)*ones
 assert (ones.T*Winv)*A==(l+1)*(ones.T*Winv)
 H=P.mfheckemat(P.mfinit([p,2],1),l); cp=s.Poly(str(P.charpoly(H)).replace('^','**'),x)
 assert s.Poly(A.charpoly(x).as_expr(),x)==s.Poly((x-l-1)*cp.as_expr(),x)
 # Exact exclusion of the band endpoints, and rational root isolation for strict bounds.
 assert s.gcd(cp,s.Poly(x*x-4*l,x)).degree()==0
 intervals=cp.intervals(eps=s.Rational(1,10**8))
 assert all(max(abs(a),abs(b))**2<4*l for (a,b),mult in intervals)
 print('P1 p,ell',p,l,'weighted symmetry and full Hecke polynomial match; endpoint gcd=1; exact strict bound; #X',l+1-int(P.trace(H)))
 if p%12!=1:continue
 Z=s.zeros(n,n-1)
 for i in range(n-1):Z[i,i]=1;Z[i+1,i]=-1
 C=Z.T*Z;R=s.Matrix(n-1,n-1,lambda i,j:sum((A*Z)[r,j] for r in range(i+1)))
 assert A*Z==Z*R and R.T*C==C*R
 g=n-1;M=R.row_join(-l*s.eye(g)).col_join(s.eye(g).row_join(s.zeros(g)))
 O=s.zeros(g).row_join(C).col_join((-C).row_join(s.zeros(g)))
 assert O.det()==n*n and M.T*O*M==l*O
 Weil=O*(M-l*M.inv())/2
 correct=C.row_join(-C*R/2).col_join((-C*R/2).row_join(l*C))
 assert Weil==correct and M.T*Weil*M==l*Weil
 Hs=s.Matrix([[s.Rational(str(H[i,j])) for j in range(g)] for i in range(g)])
 S0,S1=2*s.eye(g),Hs
 for k in range(1,5):
  Sk=S1 if k==1 else Hs*S1-l*S0
  if k>1:S0,S1=S1,Sk
  # Product over 2-dimensional Frobenius pairs, no resultant or companion determinant.
  count=int(((1+l**k)*s.eye(g)-Sk).det())
  inv=snf(s.eye(2*g)-M**k);assert (inv,count)==expected[p,l,k] and math.prod(inv)==count
  print('SNF p,ell,k',p,l,k,inv,'Hecke recurrence count',count,'saved match True')
 N,f=hash_expected[p,l];assert cm_fixed(p,l)==f
 arcs,rev,succ=make_arcs(A);assert len(arcs)==N and sum(i==j for i,j in enumerate(rev))==f
 actual=walk_determinant(succ);exponent=(N-f)//2-n
 rhs=s.Poly((1+x)**f*(1-x*x)**exponent,x)*s.Poly(((1+l*x*x)*s.eye(n)-x*A).det(),x)
 assert actual==rhs==poly_expected[p,l]
 print('Hashimoto p,ell',p,l,'N,f,exponent',N,f,exponent,'walk-trace determinant = saved = corrected Bass; CM half-loops',cm_fixed(p,l))

# The degenerate test forces the exponent and checks its negative values.
for loops,pairs in [(1,0),(0,1),(3,0)]:
 A=s.Matrix([[loops+2*pairs]]);arcs=[];rev=[]
 for _ in range(pairs):e=len(arcs);arcs.extend([(0,0)]*2);rev.extend([e+1,e])
 for _ in range(loops):rev.append(len(arcs));arcs.append((0,0))
 N=len(arcs);succ=[[j for j in range(N) if j!=rev[i]] for i in range(N)]
 det=walk_determinant(succ).as_expr();q=N-1;e=pairs-1
 rhs=(1+x)**loops*(1-x*x)**e*(1-N*x+q*x*x)
 assert s.cancel(det-rhs)==0
 print('one vertex test fixed,pairs',loops,pairs,'exponent',e,'det',det)

new=json.loads((here/'theta_data.json').read_text())
for l in [11,139]:
 A=s.Matrix(new['matrices'][str(l)]);R=s.Matrix(2,2,lambda i,j:A[i,j]-A[i,2]);M=R.row_join(-l*s.eye(2)).col_join(s.eye(2).row_join(s.zeros(2)))
 inv=snf(s.eye(4)-M)
 print('NEW p,ell',37,l,'B',A.tolist(),'restriction',R.tolist(),'SNF k1',inv,'order',math.prod(inv),'2-primary rank',sum(v%2==0 for v in inv))
# Elementary convention correction, independent of a graph example.
a,q=s.symbols('a q');M=s.Matrix([[a,-q],[1,0]]);O=s.Matrix([[0,1],[-1,0]])
print('Exact Weil form for the stated companion convention:',s.simplify(O*(M-q*M.inv())/2).tolist())
