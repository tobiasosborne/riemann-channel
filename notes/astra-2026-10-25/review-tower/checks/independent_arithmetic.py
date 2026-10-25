#!/usr/bin/env python3
"""Independent integer ideals + PARI curve census. No lane-T imports.
Run with python3; PARI work is a subprocess in the prescribed environment.
HNF ideals c*(A,B+w) are enumerated by actual index, not residue vectors.
"""
from pathlib import Path
from math import gcd, isqrt, prod
from itertools import product
import json, os, subprocess, sys
HERE=Path(__file__).resolve().parent
PY='/tmp/claude-1000/-home-tobias-Projects-riemann-channel/venv-astra/bin/python'

def red(a,b,c):
    while True:
        k=(a-b)//(2*a)
        b,c=b+2*k*a,a*k*k+b*k+c
        if a>c:
            a,b,c=c,-b,a
            continue
        if (abs(b)==a or a==c) and b<0: b=-b
        return (a,b,c)

def ideals(D,bound):
    s=D%2; n=(s*s-D)//4
    for z in range(1,isqrt(bound)+1):
        for a in range(1,bound//(z*z)+1):
            for b in range(a):
                c0,rem=divmod(b*b+s*b+n,a)
                if rem or gcd(gcd(a,2*b+s),c0)!=1: continue
                yield z*z*a, (z*a,z*b,z), red(a,2*b+s,c0)

def normsets(D,mods,bound=1024):
    rows=list(ideals(D,bound)); fs=sorted({f for _,_,f in rows})
    print(f'D={D} bound={bound} invertible_HNF_ideals={len(rows)} classes={fs}')
    for N in mods:
        sets=[]
        for f in fs:
            witness={}
            for n,H,g in rows:
                if f==g and gcd(n,N)==1 and (n%N not in witness or n<witness[n%N][0]):
                    witness[n%N]=[n,list(H)]
            S=sorted(witness)
            # Independent finite form calculation is an upper bound for the
            # bounded ideal search. Equality certifies that every residue occurs.
            a,b,c=f
            full={v for x,y in product(range(N),repeat=2) if gcd(v:=(a*x*x+b*x*y+c*y*y)%N,N)==1}
            assert set(S)==full,(D,N,f,S,full)
            sets.append(S)
            print(f'  N={N} class={f} S={S} minimal_norm/HNF_witnesses={dict(sorted(witness.items()))}')
        a,b,c=fs[0]
        H={v for x,y in product(range(N),repeat=2) if gcd(v:=(a*x*x+b*x*y+c*y*y)%N,N)==1}
        assert all(set(S)=={S[0]*h%N for h in H} for S in sets)
    return fs

def mm(A,B):
    a,b,c,d=A;e,f,g,h=B
    return (a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)
def mpow(A,k):
    R=(1,0,0,1)
    for _ in range(k): R=mm(R,A)
    return R
def group(A,k):
    a,b,c,d=mpow(A,k);a-=1;d-=1
    g=gcd(gcd(abs(a),abs(b)),gcd(abs(c),abs(d)))
    return [n for n in (abs(a*d-b*c)//g,g) if n>1]
def matrix(u,b,s,n,f):
    assert b%f==0
    return (u,-n*b*f,b//f,u+b*s)
def census(p,t):
    reps={}; models=0
    for A in range(p):
        for B in range(p):
            den=(4*A**3+27*B*B)%p
            if not den: continue
            card=1+sum(1 if (v:=(x**3+A*x+B)%p)==0 else 2 if pow(v,(p-1)//2,p)==1 else 0 for x in range(p))
            if card!=p+1-t: continue
            j=1728*4*A**3*pow(den,-1,p)%p
            reps.setdefault(j,[A,B]);models+=1
    return reps,models

def pari_main():
    from cypari2 import Pari
    pari=Pari();pari.allocatemem(256000000,silent=True)
    print('PARI version',pari('version()'))
    allrows=[]
    for p,t,D,u,b,s,n,fs in [(41,12,-20,6,1,0,5,[1]),(7,2,-24,1,1,0,6,[1]),(41,6,-8,3,4,0,2,[1,2,4]),(7,1,-3,-1,3,1,1,[1,3]),(37,8,-84,4,1,0,21,[1])]:
        reps,nmodels=census(p,t)
        assert t*t-4*p==D*b*b
        print(f'CENSUS p={p} trace={t} discZpi={t*t-4*p} DK={D} fpi={b} models={nmodels} j/models={reps}')
        predict={f:[group(matrix(u,b,s,n,f),k) for k in range(1,7)] for f in fs}
        for f in fs: print(f'  conductor={f} M={matrix(u,b,s,n,f)} groups_k1..6={predict[f]}')
        result={}
        for j,ab in reps.items():
            gs=[]
            for k in range(1,7):
                z=pari.ffgen(p**k,'z');E=pari.ellinit(ab,z)
                g=list(map(int,pari.ellgroup(E)));gs.append(g)
                assert int(pari.ellcard(E))==prod(g)
            cs=[f for f in fs if gs==predict[f]]
            assert len(cs)==1,(p,t,j,gs,cs)
            f=cs[0];result[j]={'model':ab,'f':f,'groups':gs}
            H=pari.polclass(D*f*f)
            assert int(pari.subst(H,'x',j))%p==0
            print(f'  j={j} E={ab} End_discriminant={D*f*f} conductor={f} PARI_groups={gs}; H_D(j)=0 mod p')
        for f in fs:
            assert sum(v['f']==f for v in result.values())==int(pari.qfbclassno(D*f*f))
        if len(fs)>1:
            for f in fs[1:]:
                sep=next(k+1 for k,(g,h) in enumerate(zip(predict[1],predict[f])) if g!=h)
                print(f'  SMALLEST_SEPARATING_k: conductors 1/{f} => {sep}')
        else: print('  SMALLEST_SEPARATING_k: none for any two listed curves; End common, Lenstra applies for every k')
        allrows.append({'p':p,'t':t,'DK':D,'fpi':b,'curves':result})
    for D in (-24,-20,-84,-32,-36,-23,-15):
        ff=sorted({f for _,_,f in ideals(D,64)})
        print(f'CLASS_GROUP D={D} h={int(pari.qfbclassno(D))} forms={ff} squares={[str(pari.qfbpow(pari.Qfb(*f),2)) for f in ff]}')
    # The smallest field T4 example, independent PARI + direct point enumeration.
    z=pari.ffgen(4,'z')
    for c in (z,z+1):
        E=pari.ellinit([1,0,0,0,c],z)
        pts=[(str(x),str(y)) for x in (z*0,z*0+1,z,z+1) for y in (z*0,z*0+1,z,z+1) if y*y+x*y==x**3+c]
        assert int(pari.ellcard(E))==len(pts)+1==4
        print(f'MINIMAL_F4 c={c} j={E.j()} points={pts} plus O, card=4, trace=1, disc=-15')
    (HERE/'independent_curves.json').write_text(json.dumps(allrows,indent=2)+'\n')
    print('PASS independent PARI census, every conductor, six extension groups, class squares, F4 minimal example')

if __name__=='__main__':
    if '--pari' in sys.argv: pari_main()
    else:
        for D,mods in [(-24,[2,3,4,8,9,16,24]),(-20,[2,3,4,5,8,9,16,20]),(-84,[2,3,4,7,8,12,21,84]),(-32,[4,8,16,32]),(-36,[3,4,9,12,36])]: normsets(D,mods)
        print('PASS bounded actual-ideal enumeration exhausts all predicted norm residues')
        sys.stdout.flush()
        subprocess.run([PY,str(Path(__file__).resolve()),'--pari'],check=True,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
