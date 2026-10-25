#!/usr/bin/env python3
"""Recheck only lane J's three restricted families, NOT the genus-six census.
Direct Boolean evaluation of surviving coefficient vectors, no Walsh transform.
Fresh fields and explicit singular-point witnesses for all final matches.
"""
import itertools,json
from pathlib import Path
import numpy as np
from review_k4 import field

HERE=Path(__file__).resolve().parent
parity=np.array([i.bit_count()%2 for i in range(256)],dtype=np.uint8)

def projective(q,d):
    for i in range(d):
        for tail in itertools.product(range(q),repeat=d-i-1):yield (0,)*i+(1,)+tail

def surface(q,plane):
    if plane:yield from projective(q,3)
    else:
        for a,b in itertools.product(projective(q,2),repeat=2):yield a+b

def powers(m):
    q=len(m);pw=np.ones((q,8),dtype=np.int64);pw[:,1]=np.arange(q)
    for j in range(2,8):pw[:,j]=m[pw[:,j-1],pw[:,1]]
    return pw

def evaluations(pt,mons,m,pw):
    vals=[]
    for mon in mons:
        val=1
        for v,e in zip(pt,mon):val=int(m[val,pw[v,e]])
        vals.append(val)
    return vals

def count(masks,mons,k,plane):
    m=field(k)[1];pw=powers(m);N=np.zeros(len(masks),dtype=np.int32)
    for pt in surface(len(m),plane):
        vals=evaluations(pt,mons,m,pw)
        rows={sum(1<<i for i,v in enumerate(vals) if v>>j&1) for j in range(k)}-{0}
        ok=np.ones(len(masks),dtype=bool)
        for row in rows:
            v=masks&row;v=v^(v>>16);v=v^(v>>8)
            ok &= parity[v&255]==0
        N+=ok
    return N

def singular_witness(mask,mons,k):
    # Only called for bidegree(3,4), the only family with final candidates.
    m=field(k)[1];pw=powers(m)
    for pt in surface(len(m),False):
        vals=evaluations(pt,mons,m,pw)
        C=0
        for i,v in enumerate(vals):
            if mask>>i&1:C^=v
        if C:continue
        # In each projective pair, first nonzero coordinate is the fixed 1.
        free=[1 if pt[0] else 0,3 if pt[2] else 2]
        deriv=[]
        for j in free:
            ds=[tuple(e-(a==j) for a,e in enumerate(mon)) for i,mon in enumerate(mons) if mask>>i&1 and mon[j]%2]
            val=0
            for v in evaluations(pt,ds,m,pw):val^=v
            deriv.append(val)
        if not any(deriv):return list(map(int,pt))
    return None

def main():
    data=json.loads((HERE.parents[2]/'astra-2026-10-23/jacobian/checks/output_fluxes.json.txt').read_text())
    targets={r['mask']:[r['N'][str(k)] for k in range(1,7)] for r in data if r['graph']=='K33' and r['ramanujan']}
    cases=[('plane quintic',[e for e in itertools.product(range(6),repeat=3) if sum(e)==5],True),('bidegree 3,4',[(i,3-i,j,4-j) for i in range(4) for j in range(5)],False),('Maroni 2',[(i,7-2*j-i,j,3-j) for j in range(4) for i in range(8-2*j)],False)]
    out=[]
    for name,mons,plane in cases:
        masks=np.arange(1<<len(mons),dtype=np.uint32);flags=np.full(len(masks),3,dtype=np.uint8);prefix=[]
        for k in range(1,7):
            N=count(masks,mons,k,plane)
            flags &= (N==targets[1][k-1]).astype(np.uint8)+2*(N==targets[6][k-1]).astype(np.uint8)
            keep=flags!=0;masks=masks[keep];flags=flags[keep]
            totals=[int(np.count_nonzero(flags&bit)) for bit in (1,2)];prefix.append(totals)
            print(f'{name} k={k} prefix survivors (mask1,mask6)={totals}',flush=True)
        witnesses=[]
        for mask in masks:
            assert name=='bidegree 3,4'
            found=None
            for k in range(1,7):
                pt=singular_witness(int(mask),mons,k)
                if pt is not None:found=dict(mask=int(mask),degree=k,point=pt);break
            assert found is not None
            witnesses.append(found)
        print(f'{name}: final raw matches={len(masks)}, singular witnesses={len(witnesses)}, smooth matches=0',flush=True)
        if witnesses:print('Singularity witness degree histogram='+str({k:sum(w['degree']==k for w in witnesses) for k in range(1,7)}),flush=True)
        out.append(dict(family=name,prefix=prefix,singular_witnesses=witnesses))
    (HERE/'output_independent_genus6.json.txt').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
