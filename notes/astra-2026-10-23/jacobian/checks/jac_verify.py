#!/usr/bin/env python3
"""Independent witness counts, integral gluing, and cycle-sign certificates."""
import contextlib
import itertools
import json
from pathlib import Path
import numpy as np
import sympy as S
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from jac_fluxes import step
from jac_hyperelliptic import F2Field,lpoly_from_counts
from jac_hyperelliptic_f3 import F3Field
from jac_trigonal import smooth,X

HERE=Path(__file__).resolve().parent

def integer_kernel(M):
    d,s,t=smith_normal_decomp(DomainMatrix.from_Matrix(M).convert_to(S.ZZ))
    D=d.to_Matrix();T=t.to_Matrix()
    assert abs(T.det())==1
    idx=[i for i in range(M.cols) if all(D[j,i]==0 for j in range(M.rows))]
    B=T[:,idx];assert M*B==S.zeros(M.rows,len(idx))
    return B

def cycle_data(A,length):
    n=A.rows;found=set()
    def dfs(path):
        if len(path)==length:
            if A[path[-1],path[0]]:
                found.add(min(tuple(path),(path[0],)+tuple(reversed(path[1:]))))
            return
        for j in range(path[0]+1,n):
            if A[path[-1],j] and j not in path:dfs(path+[j])
    for i in range(n):dfs([i])
    signs=[int(S.prod(A[c[i],c[(i+1)%length]] for i in range(length))) for c in found]
    return len(signs),signs.count(-1),sum(signs)

def main():
    data=json.loads((HERE/'output_fluxes.json.txt').read_text())
    r=next(r for r in data if r['graph']=='K4' and r['ramanujan'])
    # Cone parametrization X=a^2,Y=b^2,Z=ab, with free T;
    # a=1,b=t gives T^3+(1+t)T^2+(1+t^3)T+t^6.
    counts=[]
    for k in range(1,9):
        f=F2Field(k);q=f.q
        mul=np.array([[f.mul(a,b) for b in range(q)] for a in range(q)],dtype=np.int64)
        v=np.arange(q,dtype=np.int64);v2=mul[v,v];v3=mul[v2,v];v6=mul[v3,v3]
        vals=v3[None,:]^mul[(1^v)[:,None],v2[None,:]]^mul[(1^v3)[:,None],v[None,:]]^v6[:,None]
        # Base (a,b)=(0,1) has cubic T^3+1. The cone vertex is not on C.
        N=int((vals==0).sum()+(v3==1).sum());counts.append(N)
        assert N==r['N'][str(k)]
    print('K4 independent cone-parametrization counts k1..8='+str(counts))
    XX,YY,ZZ,TT=X
    Q=XX*YY+ZZ**2;C=TT**3+TT**2*XX+TT**2*ZZ+TT*XX**2+TT*YY*ZZ+YY**3
    assert smooth(Q,C)
    print('K4 witness smooth over algebraic closure on all four charts: PASS')
    # Count the five ternary witnesses by direct enumeration of y, not chi.
    f3data=json.loads((HERE/'output_hyperelliptic_f3.json.txt').read_text())
    for mask,polys in f3data['hits'].items():
        c=polys[0];N=[]
        for k in range(1,6):
            field=F3Field(k);cnt=0
            squares=[field.mul[y,y] for y in range(field.q)]
            for a in range(field.q):
                z=0
                for b in reversed(c):z=int(field.add[field.mul[z,a],b])
                cnt+=squares.count(z)
            cnt+=squares.count(c[-1]);N.append(cnt)
        tar=f3data['targets'][mask];assert N==tar
        row=next(r for r in data if r['graph']=='K5' and r['mask']==int(mask))
        assert lpoly_from_counts(N,3,5)==row['weil_coefficients']
        print(f'K5:{mask} direct (x,y) point counts={N}; Newton L-polynomial matches: PASS')
    for name,mask in [('K4',1),('Petersen',22),('K5',13)]:
        row=next(r for r in data if r['graph']==name and r['mask']==mask)
        A=S.Matrix(row['A']);p=row['p'];F=step(A,p);n=A.rows;I=S.eye(2*n)
        Om=S.zeros(n).row_join(S.eye(n)).col_join((-S.eye(n)).row_join(S.zeros(n)))
        if name=='K4':
            polys=[F*F-F+2*I,F*F+F+2*I,F**4-F*F+4*I]
            expected=16
        else:
            polys=[F*F+p*I,F**4+(2*p-5)*F*F+p*p*I]
            expected=5**(6 if name=='Petersen' else 2)
        bases=[integer_kernel(poly) for poly in polys]
        B=S.Matrix.hstack(*bases);index=abs(int(B.det()))
        assert index==expected
        print(f'{name}:{mask} rank blocks={[b.cols for b in bases]}; integral splitting index={index}; restricted Omega determinants={[int((b.T*Om*b).det()) for b in bases]}')
    for row in data:
        if not row['ramanujan']:continue
        A=S.Matrix(row['A']);p=row['p'];cy={l:cycle_data(A,l) for l in (3,4,5)}
        assert row['a']['4']==(p**4-p*p)//4-2*cy[4][2]
        if row['graph']=='Petersen':assert row['a']['5']==6-2*cy[5][2]
        if row['graph']=='cube' and row['mask']==23:assert A*A==3*S.eye(A.rows)
        print(f'{row["graph"]}:{row["mask"]} cycles(length:total,negative,signedsum)={cy}')

if __name__=='__main__':
    with (HERE/'output_verify.txt').open('w') as f,contextlib.redirect_stdout(f):main()
    print((HERE/'output_verify.txt').read_text())
