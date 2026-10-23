#!/usr/bin/env python3
"""Replay lane U's unchanged 22 assertions/42 comparisons with independent FLINT.

This is explicitly NOT a PARI rerun. Only the gp(body) boundary is replaced.
All lattice routines, case lists, and assertions are loaded from the old file.
The original file is read, never modified. No output outside this lane.
"""
import ast
import hashlib
import re
from pathlib import Path
from math import prod
from sympy import Matrix, factorint
from exact_ec import Curve,dlog_mu,root
from tower_audit import coords,snf

ROOT=Path(__file__).resolve().parents[4]
SOURCE=ROOT/'notes/adelic-gkp/checks/check_tower_pairing.py'


def matrix(p):
    return Matrix([[0,-1],[2,-1]]) if p==2 else Matrix([[1,-6],[1,1]])


def group(p,k,ai):
    M=matrix(p)
    inv=snf(M,k)
    E=Curve(p,k,ai,-1 if p==2 else 2)
    E.basis(inv)
    return inv


def cdata(ai,p,k,l,N,nm):
    E=Curve(p,k,ai,-1 if p==2 else 2)
    inv=snf(matrix(p),k)
    os=[]
    es=[]
    for o in inv:
        e=0
        while o%l==0:
            e+=1
            o//=l
        if e:
            es.append(e)
    if len(es)==1:
        es.append(0)
    os,gs=E.primary_basis(l,es)
    F=[coords(E,E.frob(P),gs,os) for P in gs]
    ps=[E.mul(o//min(o,N),P) for o,P in zip(os,gs)]
    w=root(E,N,nm==7)
    if nm==-7 and N==8:
        w=root(E,8,True)**3
        assert w+w**(-1)==4
    Tm=[[dlog_mu(E.tate(P,Q,N),w,N) for Q in gs] for P in ps] if (E.q-1)%N==0 else -1
    We=dlog_mu(E.weil(*ps,N),w,N) if len(os)==2 and min(os)>=N else -1
    return [os,F,Tm,We,inv,N]


def gp_boundary(body):
    lines=[]
    if 'print("EG|' in body:
        for k in range(1,9):
            lines.append(f'EG|{k}|{group(2,k,[1,0,0,0,1])}')
        for c,ai in [('E4',[3,3]),('E5',[1,3])]:
            for k in range(1,5):
                lines.append(f'E3G|{c}|{k}|{group(7,k,ai)}')
    else:
        pattern=r'print\("CD\|(\d+)\|",cdata\((\[[^]]+\]),(\d+),(\d+),(\d+),(\d+),(-?\d+)\)\);'
        rows=re.findall(pattern,body)
        assert rows,body
        for i,ai,p,k,l,N,nm in rows:
            lines.append(f'CD|{i}|{cdata(ast.literal_eval(ai),int(p),int(k),int(l),int(N),int(nm))}')
    return '\n'.join(lines)


def main():
    src=SOURCE.read_text()
    print('BACKEND: independent FLINT/Miller arithmetic, NOT PARI.')
    print('Legacy assertion labels below retain the word PARI; all curve values in THIS replay come from FLINT.')
    print('Legacy source:',SOURCE.relative_to(ROOT))
    print('SHA256:',hashlib.sha256(src.encode()).hexdigest())
    split=src.index('print("== S.')
    ns={'__file__':str(SOURCE),'__name__':'lane_u_replay'}
    exec(compile(src[:split],str(SOURCE),'exec'),ns)
    ns['gp']=gp_boundary
    exec(compile(src[split:],str(SOURCE),'exec'),ns)
    assert ns['nfail']==0
    simultaneous=0
    for tag,row in ns['RESULTS'].items():
        if row['weil'] is None or row['tate'] is None:
            continue
        N=int(tag.split('N=')[1].split()[0])
        # The old helper uses 1-M^k; the page's corrected convention uses M^k-1.
        for sw,st in zip(row['weil'][0],row['tate'][0]):
            assert sw & {(-s)%N for s in st}, (tag,sw,st)
        simultaneous+=1
    print(f'PASS common Weil/Tate multiplier for EACH equivariant map in all {simultaneous} cases having both pairings, after fixing the one global Tate sign.')


if __name__=='__main__':
    main()
