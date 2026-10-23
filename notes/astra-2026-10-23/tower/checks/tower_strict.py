#!/usr/bin/env python3
"""Exact norm-residue and intertwiner audit. No PARI dependency or RH input.

Run: python3 notes/astra-2026-10-23/tower/checks/tower_strict.py
S_N is the norm set of integral invertible ideals in a fixed class, prime to N.
The proof in astra-proofs.md identifies it with unit values of its norm form.
"""
from itertools import product
from math import gcd, isqrt


def forms(D):
    ans = []
    for a in range(1, isqrt((-D)//3)+1):
        for b in range(-a, a+1):
            if (b*b-D) % (4*a):
                continue
            c = (b*b-D)//(4*a)
            if a > c or gcd(gcd(a, b), c) != 1:
                continue
            if (abs(b) == a or a == c) and b < 0:
                continue
            ans.append((a, b, c))
    return ans


def residues(f, N):
    a, b, c = f
    return {v for x, y in product(range(N), repeat=2)
            if gcd(v := (a*x*x+b*x*y+c*y*y) % N, N) == 1}


def step(f, trace):
    a, b, c = f
    return ((trace-b)//2, -c, a, (trace+b)//2)


def mul(A, B, N):
    a,b,c,d = A
    e,f,g,h = B
    return ((a*e+b*g)%N, (a*f+b*h)%N,
            (c*e+d*g)%N, (c*f+d*h)%N)


def intertwiners(A, B, N):
    ans = {}
    for g in product(range(N), repeat=4):
        d = (g[0]*g[3]-g[1]*g[2]) % N
        if gcd(d,N) == 1 and mul(g,A,N) == mul(B,g,N):
            ans.setdefault(d, g)
    return ans


def main():
    for D in (-7, -15, -20, -24, -23):
        fs = forms(D)
        print(f'D={D} h={len(fs)} reduced primitive forms={fs}')
        for N in (2,3,4,8,9,16,abs(D)):
            rows = [(f, sorted(residues(f,N))) for f in fs]
            print(f'  N={N}: {rows}')
            H = residues(fs[0],N)
            for f, row in rows:
                assert row
                assert set(row) == {(row[0]*h)%N for h in H}
        print()
    expected = {2:{1},3:{2},4:{1,3},8:{3,5},9:{2,5,8},16:{3,5,11,13}}
    for N,S in expected.items():
        assert residues((2,0,3),N) == S
        inter = intertwiners(step((1,0,6),2),step((2,0,3),2),N)
        assert set(inter) == S
        print(f'D=-24 N={N} norm coset=intertwiner determinants={sorted(S)} witnesses={inter}')
    for f in forms(-23)[1:]:
        for N in (2,3,4,8,16,23):
            inter = intertwiners(step((1,1,6),3),step(f,3),N)
            assert 1 in inter
            assert residues(f,N) == residues((1,1,6),N)
            print(f'D=-23 form={f} N={N} strict determinant-one witness={inter[1]}')
    # O=Z[(1+sqrt(-7))/2], pi=3+7*omega: q=128, trace=13, conductor(Z[pi])=7.
    # On E[7] pi is scalar. Many isolated-level maps do not extend up the tower.
    M = (3,-14,7,10)
    dets = set(intertwiners(M,M,7))
    H = residues((1,1,2),7)
    assert dets == {1,2,3,4,5,6} and H == {1,2,4}
    print('FINITE-LEVEL CAVEAT: q=128 a=13 O discriminant=-7 conductor(Z[pi])=7')
    print(f'  centralizer determinants on E[7]={sorted(dets)}; extendable tower multipliers={sorted(H)}')
    from sympy import Matrix
    C=Matrix([[1,1],[0,-1]])
    for u,v in ((0,1),(1,2),(3,2),(1,4),(5,1)):
        M=Matrix([[u,-2*v],[v,u+v]])
        Mc=Matrix([[u+v,2*v],[-v,u]])
        assert C*M==Mc*C and C.det()==-1
    print('CM scope: conjugation C=[[1,1],[0,-1]] intertwines every u+v*omega with its conjugate, determinant=-1.')
    print('Well-definedness caveat: q=2, E1, k=1, N=3: G=Z/4 has G[3]=0, so the Tate shadow is trivially well-defined although 3 does not divide 2-1.')
    from exact_ec import Curve
    E=Curve(2,2,[1,0,0,0,1])
    t=E.F.gen()
    for a6 in (t,t+1):
        E.a6=a6
        pts=list(E.points())
        assert len(pts)==4
        print(f'MINIMAL T4 counterexample over F4={E.F}: y^2+xy=x^3+({a6}), j={1/a6}, #E=4, trace=1, disc=-15, conductor=1; points={pts}')
    assert len(forms(-15))==2
    assert set(intertwiners(step((1,1,4),1),step((2,1,2),1),3))=={2}
    assert all(len(forms(D))==1 for D in (-7,-8,-11))
    print('  N=3 crossed determinant set={2}, hence strict separation; smaller q=2,3 ordinary discriminants -7,-8,-11 all have h=1.')
    print('PASS all assertions; D=-23 has three classes and one strict genus.')


if __name__ == '__main__':
    main()
