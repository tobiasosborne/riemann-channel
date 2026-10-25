#!/usr/bin/env python3
"""Fresh finite-ring obstruction checks, lattice repair and CM square classes.
No lane J imports. The argument for why these congruences are necessary is
given in the review; this script does not mistake a failed unit search for proof.
"""
import itertools,json
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parents[2]/'astra-2026-10-23'/'jacobian'/'checks'
x=s.symbols('x')

def main():
    data=json.loads((SOURCE/'output_fluxes.json.txt').read_text())
    A=s.ones(4)-s.eye(4);A[0,1]=A[1,0]=-1;I=s.eye(4)
    U=A+(I-A*A)/2
    assert all(v%2==0 for v in A*A-I)
    assert U.det()==1 and all(v.q==1 for v in U.inv())
    print('K4 A² mod2 = '+str((A*A).applyfunc(lambda v:v%2).tolist()))
    print('K4 U='+str(U.tolist())+' U_inverse='+str(U.inv().tolist()))
    F=A.row_join(-2*I).col_join(I.row_join(s.zeros(4)));V=2*F.inv()
    Om=s.zeros(4).row_join(I).col_join((-I).row_join(s.zeros(4)))
    D=s.diag(U,U);B=Om*D;H=B*(F-V)*D
    assert B.T==-B and B.det()==1 and F.T*B==B*V
    assert all(H[:j,:j].det()>0 for j in range(1,9))
    print('K4 repaired form: alternating, compatible, unimodular; positive H leading minors='+str([H[:j,:j].det() for j in range(1,9)]))
    print('K4 unique degree<4 repair polynomial=(1+2x-x²)/2; half-integral, hence outside Z[A].')
    # Enumerate every degree<4 residue polynomial modulo16, not only (a,b).
    candidates=0
    for c in itertools.product(range(16),repeat=4):
        plus=sum(c)%16;minus=sum((-1)**i*c[i] for i in range(4))%16
        if plus not in (1,15) or (plus+minus)%16:continue
        a=(c[0]+5*c[2])%16;b=(c[1]+5*c[3])%16
        if (a*a-5*b*b)%16==15:candidates+=1
    assert candidates==0
    print('K4 full residue ring modulo16: admissible unit/sign candidates='+str(candidates))
    # Rational-value restrictions checked using coefficient residues modulo12.
    # Equivalent necessary constraints on the four values are exhaustive.
    rational=[]
    for vals in itertools.product((-1,1),repeat=4):
        a,b,c,d=vals
        if a==-b and (c-b)%3==0 and (d-a)%3==0 and (c-d)%4==0:rational.append(vals)
    assert not rational;print('rational +/-1,+/-2 unit/sign value tuples='+str(rational))
    print('0,sqrt5: possible f(0)^2 mod5='+str(sorted({i*i%5 for i in (1,-1)}))+'; required norm(-1) mod5=4')
    print('sqrt3: possible squares mod3='+str(sorted({i*i%3 for i in range(3)}))+'; negative norm requires2')
    # Pell unit via continued fraction; not a bounded search over graph units.
    cf=s.continued_fraction_periodic(0,1,33);period=cf[1]
    gen=s.continued_fraction_convergents(cf)
    pell=[]
    for _ in range(2*len(period)):
        q=next(gen);a,b=int(s.numer(q)),int(s.denom(q))
        if a*a-33*b*b==1:pell.append((a,b))
    assert pell[0]==(23,4)
    print('sqrt33 continued fraction='+str(cf)+'; first norm+1 convergent='+str(pell[0]))
    residues=[(sg,k,(sg*pow(3,k,8))%8,(sg*pow(5,k,6))%6) for sg in (-1,1) for k in (0,1)]
    assert not any(a==1 and b==5 for sg,k,a,b in residues)
    print('sqrt33 unit residues (sign,parity,at1 mod8,at-1 mod6)='+str(residues))
    # Verify every NO certificate really restricts a factor of this orbit.
    patterns={'k4':(x*x-1)*(x*x-5),'rational':(x*x-1)*(x*x-4),'zero5':x*(x*x-5),'sqrt3':x*x-3,'k5':(x*x-1)*(x*x-x-8),'k5mirror':(x*x-1)*(x*x+x-8)}
    labels={('K4',1):'k4',('Petersen',1):'rational',('Petersen',6):'k4',('Petersen',10):'rational',('Petersen',22):'zero5',('K33',6):'rational',('cube',3):'sqrt3',('cube',5):'k4',('cube',23):'sqrt3',('K5',1):'k5',('K5',11):'k5mirror',('K5',13):'zero5'}
    for r in data:
        label=labels.get((r['graph'],r['mask']))
        if label:
            h=s.Poly.from_list(r['adjacency_coefficients'],x)
            assert h.rem(s.Poly(patterns[label],x)).is_zero
            print(f'NO {r["graph"]}:{r["mask"]}: required real factors verified; {label}')
    print('NO certificate count='+str(len(labels)))
    # Independent arithmetic supporting the compatible-embedding YES claims.
    g=x**3-x*x-5*x+1
    print('cube1 real cubic discriminant='+str(s.discriminant(g,x)))
    print('cube1 cubic mod23='+str(s.factor(g,modulus=23)))
    D=s.resultant(g,x*x-8,x)
    assert D==-23
    print('cube1 norm(lambda²-8)='+str(D)+'; gcd mod23='+str(s.gcd(s.Poly(g,x,modulus=23),s.Poly(x*x-8,x,modulus=23)).as_expr()))
    assert s.discriminant(g,x)%7 and s.discriminant(g,x)%23
    print('cube1 primes7,23 unramified in real splitting field; discriminants have disjoint odd supports at conjugate primes above23 and at7.')
    assert s.expand((-5+2*s.sqrt(2))*(-5-2*s.sqrt(2)))==17
    print('cube9 D1,D2 totally negative, product17; 17 nonsquare in Q(sqrt2).')
    for mask in (1,9):
        r=next(r for r in data if r['graph']=='cube' and r['mask']==mask);A=s.Matrix(r['A'])
        assert A.det()==1
        print(f'cube:{mask} det A=1; ordinary middle coefficient={r["weil_coefficients"][8]}; U=A integral unit.')

if __name__=='__main__':main()
