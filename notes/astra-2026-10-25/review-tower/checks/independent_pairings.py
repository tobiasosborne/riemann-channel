#!/usr/bin/env python3
"""Actual torsion via division-polynomial roots, independent of lane T's sampler.
PARI curve bases + brute force ALL Frobenius intertwiners, common finite fields.
"""
from pathlib import Path
from math import gcd
from itertools import product
import os,subprocess,sys,json
HERE=Path(__file__).resolve().parent
PY='/tmp/claude-1000/-home-tobias-Projects-riemann-channel/venv-astra/bin/python'
if '--worker' not in sys.argv:
    raise SystemExit(subprocess.run([PY,str(Path(__file__).resolve()),'--worker'],env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')).returncode)
from cypari2 import Pari
pa=Pari();pa.allocatemem(256000000,silent=True)
pa('setrand(20261025)')

def mm(A,B,N):
    a,b,c,d=A;e,f,g,h=B
    return ((a*e+b*g)%N,(a*f+b*h)%N,(c*e+d*g)%N,(c*f+d*h)%N)
def inter(A,B,N):
    ans={}
    for g in product(range(N),repeat=4):
        d=(g[0]*g[3]-g[1]*g[2])%N
        if gcd(d,N)==1 and mm(g,A,N)==mm(B,g,N): ans.setdefault(d,[]).append(g)
    return ans

def dlog(z,w,N):
    return next(i for i in range(N) if w**i==z)
def torsion_data(p,k,ab,N,z,w):
    E=pa.ellinit(ab,z)
    tors=[pa([0])]
    pol=pa.elldivpol(E,N)
    for x in pa.polrootsmod(pol,z):
        for y in pa.ellordinate(E,x):
            P=pa([x,y])
            if len(pa.ellmul(E,P,N))==1: tors.append(P)
    assert len(tors)==N*N,(p,k,ab,N,len(tors),pol)
    primitive=lambda zz: all(zz**d!=1 for d in range(1,N))
    P,Q,wei=next((P,Q,v) for P in tors for Q in tors if primitive(v:=pa.ellweilpairing(E,P,Q,N)))
    coords={str(pa.elladd(E,pa.ellmul(E,P,i),pa.ellmul(E,Q,j))):(i,j) for i,j in product(range(N),repeat=2)}
    assert len(coords)==N*N
    F=[coords[str(pa([R[0]**p,R[1]**p]))] for R in (P,Q)]
    A=(F[0][0],F[1][0],F[0][1],F[1][1])
    e=dlog(wei,w,N)
    print(f'  E={ab} j={E.j()} N={N} torsion_count={len(tors)} basis=({P},{Q}) Frob={A} e={wei}=w^{e}')
    return A,e

def check_family(p,trace,D,curves,levels):
    print(f'PAIRING FAMILY p={p} trace={trace} End_D={D} j/models={curves}')
    pairs={ij:{} for ij in product(curves,repeat=2)}
    for N,k in levels:
        z=pa.ffgen(p**k,'z');w=pa.ffprimroot(z)**((p**k-1)//N)
        print(f' N={N} extension_k={k} field_minpoly={pa.minpoly(z)} common_w={w}')
        data={j:torsion_data(p,k,ab,N,z,w) for j,ab in curves.items()}
        for j1,j2 in pairs:
            A,e=data[j1];B,f=data[j2]
            ints=inter(A,B,N)
            S=sorted({f*d*pow(e,-1,N)%N for d in ints})
            pairs[j1,j2][N]=S
            if j1<j2: print(f'  PAIR j={j1}->{j2} N={N} isos={sum(map(len,ints.values()))} Weil_multiplier_set={S} strict={1 in S}')
    allsep=all(any(1 not in S for S in levels.values()) for (a,b),levels in pairs.items() if a!=b)
    print(f' ALL_DISTINCT_CURVES_STRICTLY_SEPARATED={allsep}')
    assert allsep
    return {f'{a}->{b}':row for (a,b),row in pairs.items()}

out={}
out['D-84']=check_family(37,8,-84,{7:[2,2],3:[2,11],2:[3,14],28:[5,17]},[(3,3),(4,4)])
# The two original h=2 examples, recomputed by division-polynomial roots.
out['D-24']=check_family(7,2,-24,{4:[3,3],5:[1,3]},[(3,3),(8,8)])
out['D-20']=check_family(41,12,-20,{40:[1,17],12:[3,11]},[(4,4),(8,4)])
# A class-separating norm obstruction which disappears at an isolated level.
rows=json.loads((HERE/'independent_curves.json').read_text())
f2={int(j):v['model'] for r in rows if r['p']==41 and r['t']==6 for j,v in r['curves'].items() if v['f']==2}
out['D-32']=check_family(41,6,-32,f2,[(4,4),(8,4),(16,8)])
# Independent scalar-Frobenius counterexample to unrestricted isolated-level S_N.
A=(3,-14,7,10); H={int((x*x+x*y+2*y*y)%7) for x,y in product(range(7),repeat=2) if (x*x+x*y+2*y*y)%7}
assert set(inter(A,A,7))==set(range(1,7)) and H=={1,2,4}
print('ISOLATED_LEVEL q=128 trace=13 N=7 determinants=',sorted(inter(A,A,7)),'extendable_norms=',sorted(H))
(HERE/'independent_pairings.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all independent division-polynomial pairing checks')
