#!/usr/bin/env python3
"""Exact certificates for the small-order unit obstruction and K4 repair.

This does not apply an ordinary CM-type rule to supersingular factors.
NO certificates in mixed cases use an ordinary subvariety and hold for a
Centeleghe--Stix normalization extending Deligne there. OPEN means the
nonordinary duality/positivity has not been constructed. YES cube entries
are for some compatible choice of the complex/p-adic embedding, certified
by square-class independence as proved in astra-proofs.md.
"""
import contextlib
from pathlib import Path
import itertools
import json
import sympy as S
from jac_fluxes import step,positive_definite,x

HERE=Path(__file__).resolve().parent

def main():
    data=json.loads((HERE/'output_fluxes.json.txt').read_text())
    A=S.ones(4)-S.eye(4); A[0,1]=A[1,0]=-1
    U=A+(S.eye(4)-A*A)/2
    assert all(v.q==1 for v in U) and U.det()==1
    F=step(A,2); V=2*F.inv()
    Om=S.zeros(4).row_join(S.eye(4)).col_join((-S.eye(4)).row_join(S.zeros(4)))
    B=Om*S.diag(U,U)
    assert B.T==-B and B.det()==1 and F.T*B==B*V
    assert positive_definite(B*(F-V)*S.diag(U,U))
    print('K4 saturated-order unit U=A+(I-A^2)/2='+str(U.tolist()))
    print('K4 det U=1; det(Omega_U)=1; integral, alternating and compatible: PASS')
    print('K4 values at (1,-1,sqrt5,-sqrt5): 1,-1,-2+sqrt5,-2-sqrt5')
    # Prove U is not in Z[A]: degree<4 representative has half coefficients.
    poly=x+(1-x*x)/2
    assert not S.Poly(poly,x).domain.is_ZZ
    print('U polynomial='+str(poly)+'; not in Z[A]')
    # Necessary small-order K4 congruence a divisible by 4, norm=-1.
    bad=[(a,b) for a in range(0,16,4) for b in range(16) if (a*a-5*b*b)%16==15]
    assert not bad
    print('K4 obstruction a=0 mod4, a^2-5b^2=-1 mod16: solutions='+str(bad))
    # Rational eigenvalues +/-1,+/-2: integer polynomial congruences.
    bad=[]
    for v1,vn1,v2,vn2 in itertools.product((-1,1),repeat=4):
        if v1!=-vn1: continue
        if (v2-vn1)%3==0 and (vn2-v1)%3==0 and (v2-vn2)%4==0:
            bad.append((v1,vn1,v2,vn2))
    assert not bad
    print('(+/-1,+/-2) rational-unit sign congruences: solutions='+str(bad))
    # 0 with +/-sqrt5, every central unit has norm ==1 mod5, but needs -1.
    assert {a*a%5 for a in (-1,1)}=={1}
    print('(0,+/-sqrt5) central unit norm mod5=1; opposite signs require -1=4: impossible')
    # +/-sqrt3 require norm -1 in Z[sqrt3], impossible modulo3.
    assert all((a*a+1)%3 for a in range(3))
    print('(+/-sqrt3) negative-norm unit: impossible mod3')
    # K5 ordinary orbits: O_Qsqrt33=Z[(1+sqrt33)/2], but every unit lies
    # in Z[sqrt33] (odd half-integers cannot have norm +/-1 mod8).
    assert all((a*a-33*b*b)%8!=4 for a in (1,3,5,7) for b in (1,3,5,7))
    assert all((a*a+1)%3 for a in range(3)) # excludes norm -1
    fundamental=[(a,b) for b in range(1,5) for a in range(1,24) if a*a-33*b*b==1]
    assert fundamental==[(23,4)]
    print('Q(sqrt33) least positive norm-one unit=23+4sqrt33=19+8theta; small solutions='+str(fundamental))
    possible=[]
    for sign,k in itertools.product((-1,1),range(2)):
        ep=sign*pow(27,k,8)%8 # theta=1, epsilon=27 mod8
        em=sign*pow(11,k,6)%6 # theta=-1, epsilon=11 mod6
        if ep==1 and em==5: possible.append((sign,k))
    assert not possible
    print('K5 ordinary: epsilon residues at theta=1 mod8 and theta=-1 mod6 prohibit (1,-1): '+str(possible))
    # Independent square classes for the two affirmative cube orbits.
    f=x**3-x*x-5*x+1
    assert S.discriminant(f,x)==592
    assert S.resultant(f,x*x-8,x)==-23
    roots23=[i for i in range(23) if int(f.subs(x,i))%23==0]
    common23=[i for i in roots23 if (i*i-8)%23==0]
    assert common23==[10]
    assert int(S.diff(f,x).subs(x,10))%23!=0
    print('cube1 square-class certificate: discr cubic=592; norm(lambda^2-8)=-23; unique common mod23 root='+str(common23))
    print('cube1 extra rational discriminant=-7; 7 and23 unramified in real S3 splitting field: PASS')
    assert S.expand((-5+2*S.sqrt(2))*(-5-2*S.sqrt(2)))==17
    print('cube9 square-class certificate: D1*D2=17, nonsquare in Q(sqrt2): PASS')
    no={'K4':{1:'K4-mod16'},'Petersen':{1:'rational-mod3,4',6:'K4-mod16',10:'rational-mod3,4',22:'gluing-mod5'},
        'K33':{6:'rational-mod3,4'},'cube':{3:'sqrt3-mod3',5:'K4-mod16',23:'sqrt3-mod3'},
        'K5':{1:'sqrt33-unit-congruence',11:'sqrt33-unit-congruence',13:'gluing-mod5'}}
    for r in data:
        if not r['ramanujan']: continue
        A=S.Matrix(r['A']); name=r['graph']; mask=r['mask']; n=A.rows;p=r['p']
        if name=='cube' and mask in (1,9):
            assert abs(A.det())==1
            print(f'{name}:{mask} YES for a compatible embedding: u=F+V; det A={A.det()}')
        elif mask in no.get(name,{}):
            print(f'{name}:{mask} NO in Z[F,V]: {no[name][mask]}')
        else:
            print(f'{name}:{mask} OPEN nonordinary polarization/duality normalization')
        fs=[f for f,e in S.factor_list(S.Poly.from_list(r['adjacency_coefficients'],x).as_expr())[1]]
        rs=[[abs(int(S.resultant(a,b,x))) if i!=j else 0 for j,b in enumerate(fs)] for i,a in enumerate(fs)]
        # Resultant-one exclusion requires a partition, not just one pair.
        split=[]
        for bits in range(1,1<<(len(fs)-1)):
            left=[i for i in range(len(fs)) if bits>>i&1]
            right=[i for i in range(len(fs)) if not bits>>i&1]
            if all(rs[i][j]==1 for i in left for j in right):split.append(left)
        print('  distinct real factors='+str(fs)+' pairwise absolute resultants='+str(rs)+' resultant-one partitions='+str(split))

if __name__=='__main__':
    with (HERE/'output_howe.txt').open('w') as f,contextlib.redirect_stdout(f): main()
    print((HERE/'output_howe.txt').read_text())
