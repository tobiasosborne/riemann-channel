import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np
from scipy.optimize import linprog
exec(open('notes/rtp-round-2/lattice-box/checks/recession_probe.py').read().split('for m in range(2,12):')[0].split('def solve(N,m):')[0])
def solve(N,m):
 T=atoms(N,m);d=T.shape[1];A=T.reshape(m,-1)
 U,s,V=np.linalg.svd(A,full_matrices=False)
 if len(s)<m or s[-1]<1e-12:return 'kernel',0,0,None,None,None
 S=V.reshape(m,d,d);tr=np.trace(S,axis1=1,axis2=2)
 vv=list(np.eye(d));cuts=[S[:,i,i] for i in range(d)]
 for it in range(400):
  Aub=np.column_stack([-np.array(cuts),np.ones(len(cuts))])
  rr=linprog(np.r_[np.zeros(m),-1],A_ub=Aub,b_ub=np.zeros(len(cuts)),A_eq=np.r_[tr,0][None,:],b_eq=[1],bounds=[(None,None)]*(m+1),method='highs',options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
  if not rr.success:return 'fail',rr.status,it,None,None,None
  delta=U@(rr.x[:m]/s);M=np.einsum('k,kij->ij',delta,T);e,v=np.linalg.eigh(M)
  if e[0]>1e-9:return 'PD',e[0],it,delta,None,None
  if rr.x[-1]<-1e-9:
   alpha=-rr.ineqlin.marginals;Z=sum(a*np.outer(v,v) for a,v in zip(alpha,vv))-rr.x[-1]*np.eye(d)
   err=np.linalg.norm(T.reshape(m,-1)@Z.ravel())
   return 'ZERO',rr.x[-1],it,None,Z,err
  for j in range(min(d,4)):
   vv.append(v[:,j]);cuts.append(np.einsum('i,kij,j->k',v[:,j],S,v[:,j]))
 return 'unknown',(e[0],rr.x[-1]),it,None,None,None
for m in range(2,12):
 for N in range(1,12):
  r=solve(N,m)
  print(m,N,r[:3],r[-1],flush=True)
  if r[0]=='ZERO':break
