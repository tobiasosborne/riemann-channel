#!/usr/bin/env python3
"""A regular one-species fermionic cMPS with internal reset and mixed bond.
All letters are rational matrices, selected without Riemann zero information.
"""
import json
import numpy as np
from scipy.linalg import block_diag, expm

sx=np.array([[0,1],[1,0]],complex)
sz=np.diag([1,-1]).astype(complex)
r=np.array([[0,1],[0,0]],complex)
p=block_diag(np.eye(2),-np.eye(2))
hp=sx/2
hm=(sx+sz)/2
h=block_diag(hp,hm)
rjump=np.block([[np.zeros((2,2)),r],[r,np.zeros((2,2))]])
q=-1j*h-rjump.conj().T@rjump/2

def L(a):
    return q@a+a@q.conj().T+rjump@a@rjump.conj().T

units=[]
parities=[]
for j in range(4):
    for i in range(4):
        a=np.zeros((4,4),complex); a[i,j]=1
        units.append(a)
        parities.append(p[i,i]*p[j,j])
superop=np.column_stack([L(a).reshape(-1,order='F') for a in units])
odd=np.where(np.array(parities)==-1)[0]
even=np.where(np.array(parities)==1)[0]
assert np.linalg.norm(rjump@rjump)<1e-12
assert np.linalg.norm(p@rjump@p+rjump)<1e-12
assert np.linalg.norm(p@h-h@p)<1e-12
assert np.linalg.norm(superop[np.ix_(odd,even)])<1e-12
assert np.linalg.norm(q+q.conj().T+rjump.conj().T@rjump)<1e-12
values,vectors=np.linalg.eig(superop)
zero=np.argmin(abs(values))
assert abs(values[zero])<1e-12
assert np.count_nonzero(abs(values)<1e-10)==1
rho=vectors[:,zero].reshape((4,4),order='F')
rho=rho/np.trace(rho)
rho=(rho+rho.conj().T)/2
weights=np.linalg.eigvalsh(rho)
assert min(weights)>1e-6
assert max(np.real(np.delete(values,zero))) < -1e-5
assert np.linalg.norm(L(rho))<1e-12
assert np.linalg.norm(p@rho@p-rho)<1e-12
odd_values=np.linalg.eigvals(superop[np.ix_(odd,odd)])
even_values=np.linalg.eigvals(superop[np.ix_(even,even)])
assert np.ptp(np.real(odd_values))>1e-3  # No false uniform-decay claim.
ring=[]
for t in [.1,.5,1,2,5,10]:
    e=expm(t*superop)
    val=(np.trace(e[np.ix_(even,even)])-np.trace(e[np.ix_(odd,odd)])).real
    assert val>-1e-10
    ring.append({"length":t,"supertrace":float(val)})

def complex_list(vals):
    return [[float(z.real),float(z.imag)] for z in sorted(vals,key=lambda z:(z.real,z.imag))]
print(json.dumps({"status":"PASS","construction":"P=Z tensor I; R=X tensor lowering; H=diag(X/2,(X+Z)/2)","kinetic_R_squared_norm":float(np.linalg.norm(rjump@rjump)),"stationary_weights":weights.tolist(),"stationary_entropy":float(-np.dot(weights,np.log(weights))),"stationary_residual":float(np.linalg.norm(L(rho))),"odd_modes_real_imag":complex_list(odd_values),"even_modes_real_imag":complex_list(even_values),"ring_norms":ring,"uniform_odd_decay":False},indent=2))
