#!/usr/bin/env python3
"""Offline exact/numerical audit of physical fermion output selection and width robustness."""
import json
from pathlib import Path
import sympy as s
import numpy as np
OUT=Path(__file__).with_suffix('.json')
I=s.eye(2); X=s.Matrix([[0,1],[1,0]]); Y=s.Matrix([[0,-s.I],[s.I,0]]); Z=s.diag(1,-1)
k=s.kronecker_product
R=k(X,s.Matrix([[0,1],[0,0]])); P=k(Z,I)
W=[k(X,X),k(X,Y),k(Y,I),k(X,Z)]
z=s.symbols('z'); a,b,c,d=s.symbols('a b c d', real=True)
H=s.diag(a*X+b*Z,c*X+d*Z)
Q=-s.I*H-R.adjoint()*R/2
D=lambda O:Q.adjoint()*O+O*Q-R.adjoint()*O*R
M=s.Matrix(4,4,lambda i,j:s.simplify(s.trace(W[i]*D(W[j]))/4))
assert all(s.simplify(D(W[j])-sum((M[i,j]*W[i] for i in range(4)),s.zeros(4)))==s.zeros(4) for j in range(4))
assert all(W[i]*W[j]+W[j]*W[i]==(2*s.eye(4) if i==j else s.zeros(4)) for i in range(4) for j in range(4))
assert R*R==s.zeros(4) and R*R.adjoint()+R.adjoint()*R==s.eye(4)
poly=s.factor(M.charpoly(z).as_expr())
centered=s.Poly(s.expand(poly.subs(z,z-s.Rational(1,4))),z)
base={a:s.Rational(1,2),b:0,c:s.Rational(1,2),d:s.Rational(1,2)}
result={'majorana_drift':str(M),'characteristic':str(poly),'centered_characteristic':str(centered.as_expr()),'base_characteristic':str(s.factor(poly.subs(base))),'perturbations':[]}
# Numerical residues independently calculated from full signed transfer.
def evaluate(vals,quartic=0):
 h=np.array(H.subs(vals),complex)+quartic*np.array(P,complex)
 r=np.array(R,complex); q=-1j*h-r.conj().T@r/2
 ident=np.eye(4)
 L=np.kron(ident,q)+np.kron(q.conj(),ident)+np.kron(r.conj(),r)
 T=np.kron(ident,q)+np.kron(q.conj(),ident)-np.kron(r.conj(),r)
 ev,U=np.linalg.eig(L); v=U[:,np.argmin(abs(ev))]; rho=v.reshape((4,4),order='F'); rho=rho/np.trace(rho); rho=(rho+rho.conj().T)/2
 idx=[i+4*j for j in range(4) for i in range(4) if (i<2)!=(j<2)]
 A=T[np.ix_(idx,idx)]; poles,V=np.linalg.eig(A); Vinv=np.linalg.inv(V)
 src=(r@rho).reshape(16,order='F')[idx]; sink=r.reshape(16,order='F').conj()[idx]
 residue=(sink@V)*(Vinv@src)
 entries=sorted([{'real':float(lam.real),'imag':float(lam.imag),'residue_abs':float(abs(res))} for lam,res in zip(poles,residue)],key=lambda item:(round(item['real'],8),item['imag']))
 return {'values':{str(key):str(value) for key,value in vals.items()},'quartic_parity_coupling':quartic,'stationary_min_eigenvalue':float(np.linalg.eigvalsh(rho)[0]),'stationarity_error':float(np.linalg.norm(L@rho.reshape(16,order='F'))),'visible_poles':[item for item in entries if item['residue_abs']>1e-8],'all_odd_poles':entries}
for label,vals,quartic in [
 ('base',base,0),
 ('unequal_internal_drives',{**base,a:s.Rational(51,100)},0),
 ('positive_block_detuning',{**base,b:s.Rational(1,100)},0),
 ('negative_block_detuning',{**base,d:s.Rational(51,100)},0),
 ('quartic_parity_interaction',base,0.01),
 ('weak_drive_equal',{**base,a:s.Rational(1,20),c:s.Rational(1,20)},0),
 ('strong_equal_drive',{**base,a:s.Rational(3,5),c:s.Rational(3,5)},0),
]:
 result['perturbations'].append({'label':label,**evaluate(vals,quartic)})
 OUT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
# Exact independent output resolvents, proving cancellation/visibility claims.
BAS=[]; IDX=[]
for col in range(4):
 for row in range(4):
  E=s.zeros(4); E[row,col]=1; BAS.append(E)
  if (row<2)!=(col<2): IDX.append(row+4*col)
def vec(A):return s.Matrix([A[row,col] for col in range(4) for row in range(4)])
rho=s.diag(s.Matrix([[s.Rational(1,5),s.I/10],[-s.I/10,s.Rational(1,10)]]),s.Matrix([[s.Rational(3,5),s.Rational(1,5)+s.I/10],[s.Rational(1,5)-s.I/10,s.Rational(1,10)]]))
source=vec(R*rho).extract(IDX,[0]); sink=s.Matrix([[s.trace(R.adjoint()*BAS[j]) for j in IDX]])
result['exact_resolvents']={}
for label,interaction in [('base',0),('quartic_interaction',s.Rational(1,100))]:
 h=H.subs(base)+interaction*P; q=-s.I*h-R.adjoint()*R/2
 assert s.simplify(q*rho+rho*q.adjoint()+R*rho*R.adjoint())==s.zeros(4)
 T=s.Matrix.hstack(*[vec(q*E+E*q.adjoint()-R*E*R.adjoint()) for E in BAS]).extract(IDX,IDX)
 response=s.factor((sink*(z*s.eye(8)-T).inv()*source)[0]); num,den=s.fraction(response)
 result['exact_resolvents'][label]={'response':str(response),'denominator_degree':s.degree(den,z),'coprime':s.gcd(num,den)==1}
 assert s.degree(den,z)==(4 if label=='base' else 8)
 OUT.write_text(json.dumps(result,indent=2,default=int)+'\n')
J=s.Matrix([[0,0,-1,0],[0,0,0,1],[-1,0,0,0],[0,1,0,0]])
N=M.subs(b,0)+s.eye(4)/4
assert J*J==s.eye(4) and s.simplify(J*N*J+N)==s.zeros(4)
U=s.Matrix([[1,0,1,0],[0,1,0,1],[-1,0,1,0],[0,1,0,-1]])/s.sqrt(2)
T=s.simplify(U.T*N*U); AB=s.simplify(T[:2,2:]*T[2:,:2]); G=s.diag(a+s.Rational(1,4),a-s.Rational(1,4))
assert s.simplify(G*AB-AB.T*G)==s.zeros(2)
result['exact_symmetry_and_quadratic_reduction']={'J':str(J),'quadratic_AB':str(AB),'metric':str(G),'verified':True}
OUT.write_text(json.dumps(result,indent=2,default=int)+'\n')
print('Exact base degree 4 / interacting degree 8; invariant Majorana space; involution; quadratic metric: PASS')
weak={a:s.Rational(1,20),b:0,c:s.Rational(1,20),d:s.Rational(1,2)}
weak_center=s.Poly(centered.as_expr().subs(weak),z)
weak_alpha=weak_center.coeff_monomial(z**2); weak_beta=weak_center.coeff_monomial(1)
weak_disc=s.factor(weak_alpha**2-4*weak_beta)
assert weak_alpha==s.Rational(77,200) and weak_beta==s.Rational(621,6400) and weak_disc==-s.Rational(2399,10000)
result['exact_weak_drive_failure']={'alpha':str(weak_alpha),'beta':str(weak_beta),'discriminant':str(weak_disc),'reflection_holds':True,'uniform_width_impossible':True}
# Single-copy signed and plus-sign transfers are similar by LEFT parity multiplication;
# physical CP meaning and observable insertions nevertheless differ.
q=Q.subs(base)
for E in BAS:
 assert s.simplify(P*(q*(P*E)+(P*E)*q.adjoint()+R*(P*E)*R.adjoint())-(q*E+E*q.adjoint()-R*E*R.adjoint()))==s.zeros(4)
result['signed_transfer_left_parity_similarity_verified']=True
OUT.write_text(json.dumps(result,indent=2,default=int)+'\n')
print('Exact weak-drive discriminant -2399/10000; signed-transfer parity similarity: PASS')
