#!/usr/bin/env python3
"""Independent quaternion theta-series computation, no PARI ideal or short-vector routines.
Enumerates stable 2-planes of O/2O, uses SymPy HNF, a small exact Gram-LLL,
and exhaustive ellipsoid bounding boxes. Author: codex:gpt-6-astra.
"""
import itertools, math, json
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form
D=s.diag(1,2,37,74)

def mul(x,y):
 a,b,c,d=x; A,B,C,F=y
 return s.Matrix([a*A-2*b*B-37*c*C-74*d*F,
                  a*B+b*A+37*c*F-37*d*C,
                  a*C+c*A-2*b*F+2*d*B,
                  a*F+d*A+b*C-c*B])
def conj(x): return s.diag(1,-1,-1,-1)*x

def span(cols):
 M=s.Matrix.hstack(*cols); den=s.ilcm(*[x.q for x in M]); H=hermite_normal_form(s.Matrix([[int(x*den) for x in M.row(i)] for i in range(M.rows)]))
 return H/den

def product(I,J): return span([mul(I[:,i],J[:,j]) for i in range(4) for j in range(4)])
def conjugate(I): return s.diag(1,-1,-1,-1)*I

def gs(B):
 U=[]; mu=[[s.Rational(0)]*4 for _ in range(4)]; norms=[]
 for i in range(4):
  v=B[:,i]
  for j in range(i):
   mu[i][j]=(B[:,i].T*D*U[j])[0]/norms[j]; v=v-mu[i][j]*U[j]
  U.append(v);norms.append((v.T*D*v)[0])
 return mu,norms

def lll(B):
 B=B.copy();k=1
 while k<4:
  mu,ns=gs(B)
  for j in range(k-1,-1,-1):
   r=s.floor(mu[k][j]+s.Rational(1,2))
   if r: B[:,k]=B[:,k]-r*B[:,j];mu,ns=gs(B)
  if ns[k]>=(s.Rational(3,4)-mu[k][k-1]**2)*ns[k-1]: k+=1
  else:
   c=B[:,k];B[:,k]=B[:,k-1];B[:,k-1]=c;k=max(k-1,1)
 return B

def theta(I, scale=1, bound=139):
 B=lll(I); Q=B.T*D*B/scale; den=int(s.ilcm(*[x.q for x in Q])); H=Q*den; inv=Q.inv()
 bounds=[math.isqrt(int(s.floor(bound*inv[i,i]))) for i in range(4)]
 h=[[int(H[i,j]) for j in range(4)] for i in range(4)]
 ct=[0]*(bound+1);tz=[0]*(bound+1)
 trden=int(s.ilcm(*[x.q for x in B[0,:]])); tr=[int(x*trden) for x in B[0,:]]
 for a,b,c,d in itertools.product(*(range(-z,z+1) for z in bounds)):
  v=(a,b,c,d)
  val=h[0][0]*a*a+h[1][1]*b*b+h[2][2]*c*c+h[3][3]*d*d+2*(h[0][1]*a*b+h[0][2]*a*c+h[0][3]*a*d+h[1][2]*b*c+h[1][3]*b*d+h[2][3]*c*d)
  if val<=bound*den and val%den==0:
   m=val//den;ct[m]+=1
   if sum(tr[i]*v[i] for i in range(4))==0:tz[m]+=1
 return ct,tz

# A supplied maximal order is only initial algebraic data: all order operations are independently checked.
O=s.Matrix([[s.Rational(1,2),0,s.Rational(1,2),s.Rational(1,2)],
            [0,s.Rational(1,4),s.Rational(1,2),s.Rational(3,4)],
            [0,0,1,0],[0,0,0,1]]).T
assert product(O,O)==span([O[:,j] for j in range(4)])
assert all(v.q==1 for v in O.inv()*s.Matrix([1,0,0,0]))
tracegram=s.Matrix(4,4,lambda i,j:2*mul(O[:,i],O[:,j])[0])
print('Order reduced discriminant',math.isqrt(abs(int(tracegram.det()))))
# Stable subspaces of dimension 2 over F_2, enumerated as bit sets, not cyclic O-generators.
vec=lambda a:s.Matrix([(a>>i)&1 for i in range(4)])
encode=lambda v:sum((int(v[i])%2)<<i for i in range(4))
left=[O.inv()*s.Matrix.hstack(*[mul(O[:,i],O[:,j]) for j in range(4)]) for i in range(4)]
planes={frozenset((0,a,b,a^b)) for a in range(1,16) for b in range(a+1,16) if a!=b}
stable=[U for U in planes if all(encode(L*vec(a)) in U for L in left for a in U)]
assert len(planes)==35 and len(stable)==3
ideals=[span([2*O[:,i] for i in range(4)]+[O*vec(a) for a in sorted(U)]) for U in sorted(stable,key=lambda U:tuple(sorted(U)))]
reps=[O]; norms=[1]
for I in ideals:
 assert product(O,I)==I and abs(I.det()/O.det())==4
 if theta(I,1,2)[0][2]==0:
  reps.append(I); norms.append(2)
assert len(reps)==3
print('Stable 2-planes:',[sorted(U) for U in stable]);print('Ideal bases:',[[str(v) for v in I] for I in reps])
ells=[2,3,5,7,11,139]; matrices={l:[[0]*3 for _ in range(3)] for l in ells}
for i in range(3):
 for j in range(i,3):
  H=product(conjugate(reps[i]),reps[j]); counts,_=theta(H,norms[i]*norms[j])
  assert counts[1]==(2 if i==j else 0)
  for l in ells:
   assert counts[l]%2==0
   matrices[l][i][j]=matrices[l][j][i]=counts[l]//2
print('Unit counts / class distinction checked by norm-one Hom theta coefficients')
orders=[product(conjugate(I),I)/n for I,n in zip(reps,norms)]
fs={l:0 for l in ells}
for R in orders:
 assert product(R,R)==R
 count,zero=theta(R)
 assert count[1]==2
 for l in ells:fs[l]+=zero[l]//2
for l,A in matrices.items():
 assert all(sum(row)==l+1 for row in A)
 print('ell',l,'B_theta',A,'half_loops',fs[l],flush=True)
# Compare with the supplied modular-polynomial data without importing author's code.
import ast,re
src=Path(__file__).resolve().parents[2]/'fable/checks/output_pizer_graph.txt'
p=None;saved={}
for line in src.read_text().splitlines():
 m=re.search(r'==== p = (\d+)',line)
 if m:p=int(m[1])
 m=re.search(r'-- l = (\d+): B\(l\) = (\[.*\])',line)
 if m and p==37:saved[int(m[1])]=ast.literal_eval(m[2])
perms=[v for v in itertools.permutations(range(3)) if all(matrices[l][v[i]][v[j]]==A[i][j] for l,A in saved.items() for i in range(3) for j in range(3))]
assert perms; perm=perms[0]
print('One permutation to all four saved Phi matrices:',perm)
matrices={l:[[A[perm[i]][perm[j]] for j in range(3)] for i in range(3)] for l,A in matrices.items()}
Path(__file__).with_name('theta_data.json').write_text(json.dumps({'matrices':matrices,'half_loops':fs},indent=2)+'\n')
