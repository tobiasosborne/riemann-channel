#!/usr/bin/env python3
"""Independent Horner/direct audits for the new sixth-power Euler masks."""
from shortrow_reconstruct import *

@njit(cache=True)
def physical_mask_rows(q,D,mixed,ns,mu,nu,ex):
    result=np.zeros((q,2),np.int64)
    for c in range(q):
        for i in range(q**D):
            if not(mu[i] and nu[i]):continue
            a=0;b=0
            for j in range(D,-1,-1):
                a=(a*(-c)+ns[i,j])%q
                b=(b*(-c-2)+ns[i,j])%q
            if not a:continue
            if mixed:
                r=b*((-1)**D)%q
                if not r:continue
                e=ex[r]
            else:e=0
            result[c]+=mu[i]*nu[i]*PAIR[e]
    return result

checked=0
for q,Dmax in [(7,7),(13,5)]:
    F=Field(q,Dmax)
    for mixed in [False,True]:
        N,top,even,reduced,rdegree,_,_=row_metadata(F,1 if mixed else 0)
        order=np.array([(c+2)%q for c in range(q)],np.int64) if mixed else np.zeros(q,np.int64)
        N=N[order];top=top[order];reduced=reduced[order];rdegree=rdegree[order]
        masks=np.zeros((q,2),np.int64)
        for c in range(q):
            P=decode(c,q,1);v=int(F.eta[resultant(F.f,3,P,1,q,F.inv)])
            masks[c]=v*(PAIR[F.ex[(-2)%q]] if mixed else PAIR[0])
        maskdegree=np.ones(q,np.int64)
        norms,iv,raw,errors=reconstruct_degree(q,7 if mixed else 6,Dmax,N,top,even,reduced,rdegree,masks,maskdegree,F.flatns,F.flatnu,F.offset,F.inv,F.ex)
        assert not np.any(errors)
        for D in range(1,Dmax+1):
            direct=physical_mask_rows(q,D,mixed,F.ns[D],F.mu[D],F.nu[D],F.ex)
            sign=int(F.eta[q-1])**D if mixed else 1
            assert np.array_equal(direct,sign*iv[:,D]),(q,D,mixed,direct,iv[:,D])
            checked+=q
        print('LOCAL_MASK_AUDIT q=',q,'physical_rows=', 'P^6*(P+2)' if mixed else 'P^6','degrees=1..',Dmax,'complex_coefficients=',q*Dmax,'PASS',flush=True)
    del F
print('LOCAL_MASK_AUDIT_TOTAL',checked,'complex coefficients PASS')
