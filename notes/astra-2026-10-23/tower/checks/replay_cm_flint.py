#!/usr/bin/env python3
"""Replay the original 27 CM consistency assertions using exact FLINT.
PARI is not used or claimed. Also test the conjugate step, which the legacy
first-match loop never excluded. Cross-prime epsilon normalisation stays open.
"""
import hashlib
import re
import sys
from pathlib import Path
from sympy import Matrix, factorint
from exact_ec import Curve,dlog_mu,root
from tower_audit import coords,snf

ROOT=Path(__file__).resolve().parents[4]
AI=[1,-1,1,-20,46]
APS={}
for p in (2,11,23,29,37):
    APS[p]=p+1-sum(1 for _ in Curve(p,1,AI).points())


def step(p):
    a=APS[p]
    v=next(v for v in range(1,20) if a*a+7*v*v==4*p)
    u=(a-v)//2
    return Matrix([[u,-2*v],[v,u+v]])


def cdata(p,k,l,N):
    E=Curve(p,k,AI,APS[p])
    inv=snf(step(p),k)
    es=[factorint(o).get(l,0) for o in inv]
    if len(es)==1:
        es.append(0)
    os,gs=E.primary_basis(l,es)
    F=[coords(E,E.frob(P),gs,os) for P in gs]
    ps=[E.mul(o//min(o,N),P) for o,P in zip(os,gs)]
    w=root(E,N)
    T=[[dlog_mu(E.tate(P,Q,N),w,N) for Q in gs] for P in ps]
    W=dlog_mu(E.weil(*ps,N),w,N) if len(os)==2 and min(os)>=N else -1
    return [os,F,T,W,inv,N]


def gp_boundary(body):
    if 'forprime(' in body:
        return 'ai|'+str(AI)+'\n'+'\n'.join(f'ap|{p} {a}' for p,a in APS.items())
    if 'print("grp|' in body:
        p,k=map(int,re.search(r'ffgen\((\d+)\^(\d+)',body).groups())
        E=Curve(p,k,AI,APS[p])
        inv=snf(step(p),k)
        E.basis(inv)
        return f'grp|{inv}\ncard|{E.card}'
    p,k,l,N=map(int,re.search(r'r=cdata\(vector\(5,i,E\[i\]\),(\d+),(\d+),(\d+),(\d+),0\)',body).groups())
    return 'c|'+str(cdata(p,k,l,N))


def main():
    srcpath=ROOT/'notes/adelic-gkp/checks/check_cm_tower.py'
    twpath=ROOT/'notes/adelic-gkp/checks/check_tower_pairing.py'
    src,tw=srcpath.read_text(),twpath.read_text()
    print('BACKEND: independent FLINT/Miller, NOT PARI. Original assertion labels are retained.')
    print('Legacy CM source SHA256:',hashlib.sha256(src.encode()).hexdigest())
    ns={'__file__':str(srcpath),'__name__':'cm_replay','re':re,'sys':sys}
    exec(compile(tw[:tw.index('print("== S.')],str(twpath),'exec'),ns)
    ns['gp']=gp_boundary
    exec(compile(src[src.index('from math import gcd'):],str(srcpath),'exec'),ns)
    assert ns['nfail']==0
    C=Matrix([[1,1],[0,-1]])
    for p,(M,Mc) in ns['steps'].items():
        assert C*M==Mc*C and C.det()==-1
    print('PASS conjugation C=[[1,1],[0,-1]] intertwines psi and psi-bar at every checked prime, determinant=-1.')
    print('The legacy first-match loop proves existence for psi; it does NOT exclude psi-bar. Under arbitrary root automorphisms both work.')


if __name__=='__main__':
    main()
