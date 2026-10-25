#!/usr/bin/env python3
"""Genus-eight plane sextics with exactly two ordinary geometric nodes.
Enumerates rational pairs and degree-two conjugate pairs, modulo moving
their locations by PGL3(F2), with ALL tangent quadratics. Node normalization
corrections are included before filtering against the cube targets.
"""
import itertools
import json
import subprocess
import sympy as S
from census_lookup import HERE,FLUX
from lowgenus import Field

MON=[(i,j,6-i-j) for i in range(7) for j in range(7-i)]
JETS=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]

def solve(rows,rhs):
    eq=[r|(v<<28) for r,v in zip(rows,rhs)]
    piv=[];rank=0
    for col in range(28):
        jj=next((j for j in range(rank,len(eq)) if eq[j]>>col&1),None)
        if jj is None:continue
        eq[rank],eq[jj]=eq[jj],eq[rank]
        for j in range(len(eq)):
            if j!=rank and eq[j]>>col&1:eq[j]^=eq[rank]
        piv.append(col);rank+=1
    assert all(r==0 for r in eq[rank:])
    offset=sum((eq[j]>>28)<<p for j,p in enumerate(piv))
    basis=[]
    for c in range(28):
        if c not in piv:
            basis.append((1<<c)|sum(((eq[j]>>c)&1)<<p for j,p in enumerate(piv)))
    assert len(basis)==16
    for r,v in zip(rows,rhs):
        assert (r&offset).bit_count()%2==v
        assert all((r&b).bit_count()%2==0 for b in basis)
    return offset,basis

def cases():
    out=[]
    # P=(1,0,0), Q=(0,1,0), tangent cross coefficient 1 at each.
    rows=[]
    for point in [0,1]:
        for r,s in JETS:
            rows.append(sum(1<<n for n,(i,j,k) in enumerate(MON) if (j if point==0 else i)==r and k==s))
    for a,c,d,f in itertools.product(range(2),repeat=4):
        offset,basis=solve(rows,[0,0,0,a,1,c,0,0,0,d,1,f])
        split=int(not(a and c))+int(not(d and f))
        delta=[2*split-2,2-split]+[0]*6
        out.append(dict(type='two rational nodes',tangents=[a,1,c,d,1,f],split=split,
                        offset=offset,basis=basis,delta_a=delta))
    # P=(1,alpha,0) and conjugate, alpha^2+alpha+1=0.
    F=Field(2);rows=[]
    for r,s in JETS:
        vals=[F.power(2,j-r) if k==s and j>=r and (r&j)==r else 0 for i,j,k in MON]
        for bit in range(2):rows.append(sum(1<<n for n,v in enumerate(vals) if v>>bit&1))
    for a,b,c in itertools.product(range(4),repeat=3):
        if not b:continue
        vals=[0,0,0,a,b,c]
        rhs=[(v>>bit)&1 for v in vals for bit in range(2)]
        offset,basis=solve(rows,rhs)
        split=(a==0 or sum((F.mul(a,F.mul(t,t))^F.mul(b,t)^c)==0 for t in range(4))==2)
        delta=[0,1 if split else -1,0,0 if split else 1]+[0]*4
        out.append(dict(type='conjugate degree-two nodes',tangents=[a,b,c],split=split,
                        offset=offset,basis=basis,delta_a=delta))
    return out

def expression(mask):
    X=S.symbols('X Y Z')
    return sum(S.prod(v**e for v,e in zip(X,m)) for i,m in enumerate(MON) if mask>>i&1),X

def exactly_nodes(mask,kind):
    f,X=expression(mask);x,y,z=X;cert=[]
    # Each ordinary node has reduced Jacobian ideal locally. Equality of the
    # chart singular ideals below rules out all other geometric singularities.
    for i in range(3):
        vs=[v for j,v in enumerate(X) if i!=j];ff=f.subs(X[i],1)
        actual=S.groebner([ff]+[S.diff(ff,v) for v in vs],*vs,modulus=2)
        if kind=='two rational nodes':
            expected=S.groebner(vs if i in [0,1] else [1],*vs,modulus=2)
        else:
            expected=S.groebner([vs[0]**2+vs[0]+1,vs[1]] if i in [0,1] else [1],*vs,modulus=2)
        cert.append(list(map(str,actual)))
        if list(actual)!=list(expected):return False,cert
    return True,cert

def main():
    cc=cases();assert len(cc)==64
    for k in range(1,9):Field(k) # check every C++ modulus for irreducibility
    binary=HERE/'plane_nodes'
    subprocess.run(['g++','-O3','-std=c++17',str(HERE/'plane_nodes.cpp'),'-o',str(binary)],check=True)
    flux=json.loads(FLUX.read_text());searches=[];hits=[]
    for target in [3,5]:
        r=next(r for r in flux if r['graph']=='cube' and r['mask']==target)
        data=[f'{len(cc)} 8']
        for i,c in enumerate(cc):
            a=[r['a'][str(k)]-c['delta_a'][k-1] for k in range(1,9)]
            data.append(' '.join(map(str,[i,len(c['basis']),c['offset']]+c['basis']+a)))
        path=HERE/'plane_nodes_input.txt';path.write_text('\n'.join(data)+'\n')
        proc=subprocess.run([str(binary),str(path)],check=True,capture_output=True,text=True)
        totals=[0]*8;raw=0;good=0
        for line in proc.stdout.splitlines():
            lhs,rhs=line.split(' MASKS');words=lhs.split();i=int(words[1]);nums=list(map(int,words[5:]))
            assert len(nums)==8
            totals=[a+b for a,b in zip(totals,nums)]
            masks=list(map(int,rhs.split()));raw+=len(masks)
            for eq in masks:
                ok,cert=exactly_nodes(eq,cc[i]['type'])
                if ok:
                    good+=1;f,_=expression(eq)
                    hit=dict(target=target,case=i,equation_mask=eq,equation=str(f),cert=cert)
                    hits.append(hit);print('WITNESS',hit,flush=True)
            searches.append(dict(target=target,case=i,log=line,raw_masks=masks))
        print('CUBE',target,'cases=64 equations=4194304 staged survivors=',totals,'raw=',raw,'exactly two nodes=',good,flush=True)
        (HERE/'output_plane_nodes.json.txt').write_text(json.dumps(dict(cases=cc,searches=searches,hits=hits),indent=2)+'\n')

if __name__=='__main__':main()
