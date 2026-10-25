#!/usr/bin/env python3
"""Independent exact derivations: basis conventions, topology, Tate caveat."""
from itertools import product
from math import gcd
from fractions import Fraction
from sympy import Matrix, symbols, solve, expand
from independent_arithmetic import ideals

for q,t in [(7,2),(41,12),(37,8)]:
    u=t//2;m=q-u*u
    C=Matrix([[t,-q],[1,0]]);M=Matrix([[u,-m],[1,u]])
    U=Matrix([[1,-u],[0,1]])
    assert M*U==U*C and U.det()==1
    print(f'CONVENTIONS q={q}, trace={t}: M={M.tolist()}, companion={C.tolist()}, U={U.tolist()}, det(U)=1, M U=U companion')
M=Matrix([[0,-1],[2,-1]]);U=Matrix([[0,-1],[1,0]]);C=Matrix([[-1,-2],[1,0]])
assert M*U==U*C and U.det()==1
print('CONVENTIONS E1: U=',U.tolist(),'det=1, M U=U companion')

a,b,c,d=symbols('a b c d');G=Matrix([[a,b],[c,d]])
M0=Matrix([[1,-6],[1,2]]);M1=Matrix([[1,-3],[2,2]])
sol=solve(list(G*M0-M1*G),(b,d),dict=True)[0]
det=expand(G.subs(sol).det())
assert det==2*a*a+a*c+3*c*c
print('TOPOLOGY D=-23 q=8 trace=3: all integral intertwiners G=',G.subs(sol).tolist(),'det=',det)
print('  8 det = (4a+c)^2+23c^2; c=0 gives det=2a^2; |c|>=1 gives det>=23/8>1; so det cannot be +/-1')
assert expand(8*det-(4*a+c)**2-23*c*c)==0
# actual simultaneous local examples, whose existence at all levels is the genus theorem.
for N in (2,3,4,8,16,23):
    witness=next((aa,cc) for aa,cc in product(range(N),repeat=2) if (2*aa*aa+aa*cc+3*cc*cc)%N==1)
    print(f'  N={N} determinant-one local witness (a,c)={witness}')

M4a=Matrix([[0,-4],[1,1]]);M4b=Matrix([[0,-2],[2,1]])
D={int(H.det())%3 for tup in product(range(3),repeat=4) if gcd(int((H:=Matrix(2,2,tup)).det()),3)==1 and all(v%3==0 for v in H*M4a-M4b*H)}
assert D=={2}
print('MINIMAL_F4 D=-15 N=3 crossed determinants=',sorted(D))
for q in (2,3):
    traces=[t for t in range(-2*q,2*q+1) if t*t<4*q and gcd(t,q)==1]
    ds=sorted({t*t-4*q for t in traces})
    hs={D:len({f for _,_,f in ideals(D,32)}) for D in ds}
    assert set(hs.values())=={1}
    print(f'SMALLER_FIELD q={q} ordinary_traces={traces}, discriminants/class_numbers={hs}')

M=Matrix([[0,-1],[2,-1]]);A=M-Matrix.eye(2);h=abs(int(A.det()))
Gfix=[v for v in product(range(h),repeat=2) if all(x%h==0 for x in A*Matrix(v))]
N=3;PN=[v for v in Gfix if all(N*x%h==0 for x in v)]
assert len(Gfix)==4 and PN==[(0,0)] and (2-1)%N!=0
print(f'TATE_WELL_DEFINEDNESS q=2 k=1 N=3: Gfix vectors /{h}={Gfix}, G[N]={PN}, exp(G[N])=1, N does not divide q^k-1; zero pairing is well-defined')

C=Matrix([[1,1],[0,-1]])
for p,t in [(2,-1),(11,-4),(23,-8),(29,-2),(37,-6)]:
    v=next(v for v in range(1,20) if t*t+7*v*v==4*p);u=(t-v)//2
    M=Matrix([[u,-2*v],[v,u+v]]);Mb=Matrix([[u+v,2*v],[-v,u]])
    assert C*M==Mb*C and C.det()==-1
    print(f'CM_CONJUGATION p={p} trace={t} u={u} v={v} C M=Mbar C, det(C)=-1')
M=Matrix([[0,-1],[5,5]]);Om=Matrix([[0,1],[-1,0]])
assert M.T*Om*M==5*Om and all(x.is_Integer for x in 5*M.inv()) and M.trace()**2>4*M.det()
print('FORMAL_TOWER_WITHOUT_RH M=',M.tolist(),'q=5 trace=5 trace_squared=25>20; det(1-M^k), k=1..5:',[int((Matrix.eye(2)-M**k).det()) for k in range(1,6)])
print('PASS all independent linear derivations')
