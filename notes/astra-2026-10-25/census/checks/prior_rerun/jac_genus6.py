#!/usr/bin/env python3
"""Exact targeted searches in three nonhyperelliptic genus-six families over F2.

All plane quintic equations and all bidegree (3,4) equations on P1 x P1
and Maroni-2 trigonal equations are searched by integer Walsh transforms;
these families DO NOT cover
all genus-six curves. Smooth hits are certified on every affine chart.
"""
import contextlib
import itertools
from pathlib import Path
import json
import numpy as np
import sympy as S
from jac_hyperelliptic import F2Field

HERE=Path(__file__).resolve().parent

def fwht(wt):
    step=1
    while step<len(wt):
        blocks=wt.reshape(-1,2*step)
        a=blocks[:,:step].copy();b=blocks[:,step:].copy()
        blocks[:,:step]=a+b;blocks[:,step:]=a-b;step*=2
    return wt

def points_plane(q):
    for i in range(3):
        for tail in itertools.product(range(q),repeat=2-i):yield (0,)*i+(1,)+tail

def points_bidegree(q):
    pts=[(1,a) for a in range(q)]+[(0,1)]
    for a,b in itertools.product(pts,repeat=2):yield a+b

def all_counts(monomials,pointgen,k):
    field=F2Field(k);wt=np.zeros(1<<len(monomials),dtype=np.int64)
    for pt in pointgen(field.q):
        powers=[[field.power(v,i) for i in range(8)] for v in pt]
        vals=[]
        for mon in monomials:
            v=1
            for i,e in enumerate(mon):v=field.mul(v,powers[i][e])
            vals.append(v)
        rows=[sum(1<<i for i,v in enumerate(vals) if v>>j&1) for j in range(k)]
        span={0}
        for r in rows:span|={v^r for v in tuple(span)}
        fac=(1<<k)//len(span)
        for v in span:wt[v]+=fac
    fwht(wt);assert np.all(wt%(1<<k)==0)
    return wt//(1<<k)

def smooth_plane(f,vars):
    for i in range(3):
        v=[x for j,x in enumerate(vars) if i!=j];g=f.subs(vars[i],1)
        gb=S.groebner([g]+[S.diff(g,x) for x in v],*v,modulus=2)
        if list(gb)!=[1]:return False
    return True

def smooth_bidegree(f,vars):
    for i,j in itertools.product((0,1),(2,3)):
        v=[x for a,x in enumerate(vars) if a not in (i,j)]
        g=f.subs({vars[i]:1,vars[j]:1})
        if list(S.groebner([g]+[S.diff(g,x) for x in v],*v,modulus=2))!=[1]:return False
    return True

def smooth_maroni2(f,vars):
    # The homogeneous monomials have base degree 7-2*j for fiber exponent j.
    # These trivializations, not ordinary bihomogeneity, define F_2 charts.
    return smooth_bidegree(f,vars)

def main():
    data=json.loads((HERE/'output_fluxes.json.txt').read_text())
    targets={r['mask']:[r['N'][str(k)] for k in range(1,7)] for r in data if r['graph']=='K33' and r['ramanujan']}
    hits={m:[] for m in targets}
    cases=[('plane quintic',[e for e in itertools.product(range(6),repeat=3) if sum(e)==5],points_plane,S.symbols('X Y Z'),smooth_plane),
           ('bidegree 3,4',[(i,3-i,j,4-j) for i in range(4) for j in range(5)],points_bidegree,S.symbols('X Y Z W'),smooth_bidegree),
           ('Maroni 2',[(i,7-2*j-i,j,3-j) for j in range(4) for i in range(8-2*j)],points_bidegree,S.symbols('X Y Z W'),smooth_maroni2)]
    for name,mons,pg,vs,sm in cases:
        keep={m:np.ones(1<<len(mons),dtype=bool) for m in targets}
        print(name+' coefficient dimension='+str(len(mons)),flush=True)
        for k in range(1,7):
            counts=all_counts(mons,pg,k)
            for m,N in targets.items():keep[m]&=counts==N[k-1]
            print(' k='+str(k)+' survivors='+str({m:int(v.sum()) for m,v in keep.items()}),flush=True)
        for m,v in keep.items():
            nsmooth=0
            for mask in np.nonzero(v)[0].tolist():
                f=sum(S.prod(x**e for x,e in zip(vs,mon)) for i,mon in enumerate(mons) if mask>>i&1)
                if sm(f,vs):
                    nsmooth+=1
                    if len(hits[m])<3:hits[m].append(dict(family=name,mask=mask,equation=str(f),counts=targets[m]))
            print(f' {name} K33:{m} smooth matching equations={nsmooth}',flush=True)
    for m,hh in hits.items():
        if hh:print('WITNESS K33:'+str(m)+' '+str(hh[0]))
        else:print('NO MATCH IN THESE THREE FAMILIES K33:'+str(m))
    (HERE/'output_genus6.json.txt').write_text(json.dumps(hits,indent=2)+'\n')

if __name__=='__main__':
    with (HERE/'output_genus6.txt').open('w') as f,contextlib.redirect_stdout(f):main()
    print((HERE/'output_genus6.txt').read_text())
