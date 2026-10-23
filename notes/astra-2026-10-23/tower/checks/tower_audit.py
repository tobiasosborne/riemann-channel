#!/usr/bin/env python3
"""Constructive Lane T audit, PARI/cypari2 when available, exact FLINT always.

python3 notes/astra-2026-10-23/tower/checks/tower_audit.py

PARI is never silently emulated: output explicitly says which backend ran.
The independent arithmetic certifies group structures by generators; counts
at k>1 use the Frobenius recurrence, not an RH assumption. With cypari2, every
reported group and pairing is also compared with ellcard/ellgroup and
ellweilpairing/elltatepairing, in an explicitly identical finite field.
"""
import sys
from math import gcd
from pathlib import Path
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
from exact_ec import Curve, cardinal, dlog_mu, key, root, velu_apply, velu_data
from tower_strict import forms, intertwiners, residues

try:
    from cypari2 import Pari
    PARI = Pari()
    PARI.allocatemem(256_000_000, 1_000_000_000)
except ImportError:
    PARI = None


def snf(M,k):
    S=smith_normal_form(Matrix.eye(2)-M**k,domain=ZZ)
    return sorted([abs(int(S[i,i])) for i in range(2) if abs(S[i,i])!=1],reverse=True)


def models(p,a):
    ans={}
    nmodels=0
    for A in range(p):
        for B in range(p):
            den=(4*A**3+27*B*B)%p
            if not den:
                continue
            n=1
            for x in range(p):
                v=(x**3+A*x+B)%p
                n+=1 if v==0 else 2 if pow(v,(p-1)//2,p)==1 else 0
            if n==p+1-a:
                j=1728*4*A**3*pow(den,-1,p)%p
                ans.setdefault(j,(A,B))
                nmodels+=1
    return ans,nmodels


def coords(E,R,gs,os):
    table={}
    P=None
    if len(gs)==1:
        for a in range(os[0]):
            table[key(P)]=[a]
            P=E.add(P,gs[0])
    else:
        for a in range(os[0]):
            Q=P
            for b in range(os[1]):
                table[key(Q)]=[a,b]
                Q=E.add(Q,gs[1])
            P=E.add(P,gs[0])
    assert len(table)==__import__('math').prod(os)
    return table[key(R)]


def frob_matrix(E,ps,N):
    cols=[coords(E,E.frob(P),ps,[N,N]) for P in ps]
    return (cols[0][0],cols[1][0],cols[0][1],cols[1][1])


def pari_curve(E):
    # Same defining polynomial and same t-generator, not merely isomorphic fields.
    coeff=list(E.F.modulus())
    poly='+'.join(f'{int(c)}*x^{i}' for i,c in enumerate(coeff))
    t=PARI(f"ffgen(Mod(1,{E.p})*({poly}),'t)")
    return PARI.ellinit(E.ai,t),t


def pari_point(P,t):
    if P is None:
        return PARI('[0]')
    return PARI([sum((int(c)*t**i for i,c in enumerate(z.to_list())),t*0) for z in P])


def pari_value(z,t):
    return sum((int(c)*t**i for i,c in enumerate(z.to_list())),t*0)


def pari_validate(E,inv,ps=None,N=None,weis=None,tates=None,gs=None):
    if PARI is None:
        return
    ep,t=pari_curve(E)
    assert int(PARI.ellcard(ep))==E.card
    assert sorted(map(int,PARI.ellgroup(ep)),reverse=True)==inv
    if ps is not None:
        pp=[pari_point(P,t) for P in ps]
        wp=PARI.ellweilpairing(ep,*pp,N)
        # Both implementations use f_P(D_Q)/f_Q(D_P); do not permit a
        # separate arbitrary sign for each value or each torsion level.
        wz=pari_value(weis,t)
        assert wp==wz
        print(f'    PARI Weil agreement: exact; value={wp}')
        for i,P in enumerate(ps):
            for j,Q in enumerate(gs):
                tt=PARI.elltatepairing(ep,pari_point(P,t),pari_point(Q,t),N)**((E.q-1)//N)
                assert tt==pari_value(tates[i][j],t)
        print('    PARI ellcard, ellgroup, and all reduced Tate entries agree.')


def isogenies(p,a,src,dst):
    E=Curve(p,1,src,a)
    allpts=list(E.points())
    ans={}
    for d in (2,3):
        P=next(P for P in allpts if E.order(P)==d)
        K=[E.mul(i,P) for i in range(1,d)]
        raw=velu_data(E,K)
        u=next(u for u in range(1,p)
               if (pow(u,4,p)*raw[0])%p==dst[0] and (pow(u,6,p)*raw[1])%p==dst[1])
        ints=[tuple(int(z.to_list()[0]) for z in P) for P in K]
        ans[d]=(ints,u)
        print(f'  phi_{d}: kernel={ints}; Velu quotient y^2=x^3+{raw[0]}x+{raw[1]}; target scale (u^2 x,u^3 y), u={u}, scalars={(u*u%p,u**3%p)}')
        if PARI is not None:
            ep=PARI.ellinit(list(src),p)
            iso=PARI.ellisogeny(ep,PARI(list(ints[0])))
            print(f'    PARI ellisogeny: {iso}')
    return ans


def iso_map(E,datum,P):
    ints,u=datum
    K=[tuple(E.F(z) for z in P) for P in ints]
    return velu_apply(E,K,P,u)


def audit_pair(p,a,D,src,dst):
    M=Matrix([[a//2,-(-D//4)],[1,a//2]])
    ms,nmodels=models(p,a)
    fs=forms(D)
    print(f'\nISOGENY CLASS p={p} a={a} discriminant(Z[pi])={a*a-4*p} fundamental={D}; h(O_K)={len(fs)}')
    print(f'  all j -> representative short models: {ms}; short models with this trace={nmodels}')
    assert len(ms)==len(fs)==2 and a*a-4*p==D
    assert set(ms.values())=={tuple(src),tuple(dst)}
    print('  End(E)=O_K on every listed curve: conductor=1, forced by the fundamental Frobenius discriminant.')
    print('  forms=',fs)
    if PARI is not None:
        assert int(PARI.qfbclassno(D))==2
        print('  PARI class polynomial:',PARI.polclass(D))
    for ai in (src,dst):
        for k in range(1,7):
            E=Curve(p,k,ai,a)
            inv=snf(M,k)
            os,gs=E.basis(inv)
            if k<=2:
                assert sum(1 for _ in E.points())==E.card
            print(f'  E={ai} k={k} card={E.card} group={inv}; generator certificate={[(o,key(g)) for o,g in zip(os,gs) if o>1]}')
            pari_validate(E,inv)
    phis=isogenies(p,a,src,dst)
    print('  Compatible T1 map: phi_3 on the entire 2-primary tower; phi_2 on every odd-primary tower (including p).')
    for N in (2,3,4,8):
        k=next(k for k in range(1,97) if len(iv:=snf(M,k))==2 and iv[-1]%N==0)
        E=Curve(p,k,src,a)
        Ep=Curve(p,k,dst,a)
        inv=snf(M,k)
        os,gs=E.basis(inv)
        ops,gps=Ep.basis(inv)
        ps=[E.mul(o//N,g) for o,g in zip(os,gs)]
        qs=[Ep.mul(o//N,g) for o,g in zip(ops,gps)]
        w=root(E,N,p==7)
        z=E.weil(*ps,N)
        zp=Ep.weil(*qs,N)
        ez,ezp=dlog_mu(z,w,N),dlog_mu(zp,w,N)
        assert gcd(ez,N)==gcd(ezp,N)==1
        A,B=frob_matrix(E,ps,N),frob_matrix(Ep,qs,N)
        dets=intertwiners(A,B,N)
        scales=sorted({ezp*d*pow(ez,-1,N)%N for d in dets})
        assert set(scales)==residues(fs[1],N)
        d=3 if N%2==0 else 2
        images=[iso_map(E,phis[d],P) for P in ps]
        igs=[iso_map(E,phis[d],P) for P in gs]
        assert all(Ep.on(P) for P in images+igs)
        assert Ep.weil(*images,N)==z**d
        for P,im in zip(ps,images):
            assert iso_map(E,phis[d],E.frob(P))==Ep.frob(im)
        cols=[coords(Ep,P,qs,[N,N]) for P in images]
        T=[[E.tate(P,Q,N) for Q in gs] for P in ps]
        Tp=[[Ep.tate(P,Q,N) for Q in gps] for P in qs]
        Ti=[[Ep.tate(P,Q,N) for Q in igs] for P in images]
        assert all(Ti[i][j]==T[i][j]**d for i in range(2) for j in range(2))
        print(f'  N={N} full torsion field F_{p}^{k}, modulus={E.F.modulus()}, primitive root w={w}')
        print(f'    source basis={list(map(key,ps))}; Frob row matrix={A}; Weil e(P,Q)={z}=w^{ez}')
        print(f'    target basis={list(map(key,qs))}; Frob row matrix={B}; Weil e(P,Q)={zp}=w^{ezp}')
        print(f'    all equivariant Weil multiplier residues={scales}; phi_{d} matrix columns={cols}')
        print(f'    transported Weil value = ({z})^{d} = {z**d}')
        print(f'    reduced Tate exponents on E[N] x E(F)/N: source={[[dlog_mu(v,w,N) for v in row] for row in T]}; target={[[dlog_mu(v,w,N) for v in row] for row in Tp]}')
        print(f'    transported Tate exponents={[[dlog_mu(v,w,N) for v in row] for row in Ti]}; degree-{d} functoriality VERIFIED')
        pari_validate(E,inv,ps,N,z,T,gs)
        pari_validate(Ep,inv,qs,N,zp,Tp,gps)
    # A genuinely pointwise test, using the mixed-primary global map.
    k=4 if p==7 else 2
    E,Ep=Curve(p,k,src,a),Curve(p,k,dst,a)
    two=1
    while E.card%(two*2)==0:
        two*=2
    odd=E.card//two
    e2=(odd*pow(odd,-1,two))%E.card
    eo=(1-e2)%E.card
    def Phi(P):
        return Ep.add(iso_map(E,phis[3],E.mul(e2,P)),iso_map(E,phis[2],E.mul(eo,P)))
    points=list(E.points())
    imgs=[Phi(P) for P in points]
    assert len({key(P) for P in imgs})==E.card==len(points)
    assert all(Ep.on(Q) and Phi(E.frob(P))==Ep.frob(Q) for P,Q in zip(points,imgs))
    # Additivity is also structural (sum of homomorphisms); test a deterministic sample.
    assert all(Phi(E.add(P,Q))==Ep.add(Phi(P),Phi(Q)) for P,Q in zip(points[:100],points[-100:]))
    print(f'  Pointwise mixed-primary Phi: {len(points)} distinct images, all on target, all commute with Frobenius; additivity sample PASS.')


def q5_orders():
    print('\nPAULI PAIR p=5 a=-2 discriminant(Z[pi])=-16; maximal discriminant=-4, possible conductors 1,2')
    for ab,f,grp in (([4,0],1,[4,2]),([4,1],2,[8])):
        E=Curve(5,1,ab,-2)
        pts=list(E.points())
        n2=sum(E.mul(2,P) is None for P in pts)
        assert len(pts)==8 and n2==(4 if f==1 else 2)
        E.basis(grp)
        print(f'  model={ab} group={grp}, rational 2-torsion size={n2}, End discriminant={-4*f*f}, conductor={f}')
        pari_validate(E,grp)
    print('  Criterion: full E[2] rational iff (pi-1)/2 is integral; here this generates Z[i].')


def main():
    print('PARI/cypari2 backend:', 'AVAILABLE '+str(PARI('version()')) if PARI is not None else 'UNAVAILABLE; no PARI result claimed')
    print('Independent backend: python-flint exact finite fields, group certificates, translated-divisor Miller pairings.')
    audit_pair(7,2,-24,[3,3],[1,3])
    audit_pair(41,12,-20,[1,17],[3,11])
    q5_orders()
    print('\nPASS all constructive exact-arithmetic assertions.')
    if PARI is None:
        print('PENDING: rerun with cypari2 for the requested independent PARI audit; current results are FLINT, not PARI.')


if __name__=='__main__':
    main()
