import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np
from scipy.optimize import linprog

def atoms(N,m):
 n=np.arange(-N,N+1);t=np.log(np.arange(2,m+2))/np.log(13)
 b=np.sin(2*np.pi*t[:,None]*n[None,:])/np.pi
 diff=n[:,None]-n[None,:]; np.fill_diagonal(diff,1)
 T=(b[:,:,None]-b[:,None,:])/diff
 for j in range(m): np.fill_diagonal(T[j],-2*(1-t[j])*np.cos(2*np.pi*n*t[j]))
 return T

def solve(N,m):
 T=atoms(N,m);d=T.shape[1];A=T.reshape(m,-1)
 U,s,V=np.linalg.svd(A,full_matrices=False)
 if s[-1]<1e-11: return 'kernel',s[-1],0,None
 # cutting plane trace=1 outer approximation; actual minimum eigenvector separates
 tr=np.trace(T,axis1=1,axis2=2)
 cuts=[T[:,i,i] for i in range(d)]
 for it in range(1000):
  rr=linprog(np.zeros(m),A_ub=-np.array(cuts),b_ub=np.zeros(len(cuts)),A_eq=tr[None,:],b_eq=[1],bounds=[(None,None)]*m,method='highs')
  if rr.status==2:
   # PD annihilator by alternating projections; warm start LP Farkas not available.
   inv=np.linalg.inv(A@A.T);Z=np.eye(d);P=Z*0;Q=Z*0
   for j in range(30000):
    Y=Z+P;Y-= (A.T@(inv@(A@Y.ravel()))).reshape(d,d);P=Z+P-Y
    W=Y+Q;e,v=np.linalg.eigh(W);ZZ=(v*np.maximum(e,1))@v.T;Q=Y+Q-ZZ
    Z=ZZ
    if j%100==0:
     Y=Z-(A.T@(inv@(A@Z.ravel()))).reshape(d,d)
     emin=np.linalg.eigvalsh(Y)[0]
     if emin>1e-7:return 'zero',emin,it,Y
   return 'dual_failed',emin,it,None
  if not rr.success:return 'lp_failed',rr.status,it,None
  M=np.einsum('k,kij->ij',rr.x,T);e,v=np.linalg.eigh(M)
  if e[0]>-1e-8:return 'ray',e[0],it,rr.x
  for j in range(min(d,4)):
   if e[j]<-1e-9:cuts.append(np.einsum('i,kij,j->k',v[:,j],T,v[:,j]))
 return 'exceeded',e[0],it,None
for m in range(2,12):
 for N in range(0,15):
  kind,margin,it,obj=solve(N,m)
  print(m,N,kind,margin,it,flush=True)
  if kind=='zero':break
