#!/usr/bin/env python3
"""Exact SU(2) and U(2) integration on K4, with independent checks.

Run: python3 checks/haar_weingarten.py. Rational exterior-power Schur integrals
are a determinant-adapted Weingarten calculation. Also sums all 216 S3 fluxes
in an integral basis and all 512 Q8 fluxes by Gaussian-integer restriction.
"""
import itertools
import sympy as sp
import flint
from haar_common import graph, matching, matching_d, su2_average, root_report, x, tree_edges

def exact_finite_average(G, mats):
    n=len(G); d=mats[0].rows; tree,cot=tree_edges(G)
    total=[0]*(n*d+1)
    for indices in itertools.product(range(len(mats)), repeat=len(cot)):
        A=sp.zeros(n*d)
        for u,v in tree:
            A[u*d:(u+1)*d,v*d:(v+1)*d]=sp.eye(d)
            A[v*d:(v+1)*d,u*d:(u+1)*d]=sp.eye(d)
        for (u,v),j in zip(cot,indices):
            A[u*d:(u+1)*d,v*d:(v+1)*d]=mats[j]
            A[v*d:(v+1)*d,u*d:(u+1)*d]=mats[j].inv()
        coeff=flint.fmpz_mat([[int(a) for a in row] for row in A.tolist()]).charpoly().coeffs()
        for k,c in enumerate(coeff): total[k]+=int(c)
    size=len(mats)**len(cot)
    return sp.Poly(sum(sp.Rational(c,size)*x**k for k,c in enumerate(total)),x)

def s3_standard():
    # Basis e0-e2,e1-e2 in the sum-zero subspace, integral but not orthonormal.
    mats=[]
    for perm in itertools.permutations(range(3)):
        cols=[]
        for j in range(2):
            v=[0]*3;v[perm[j]]+=1;v[perm[2]]-=1
            cols.append(v[:2])
        mats.append(sp.Matrix.hstack(*[sp.Matrix(c) for c in cols]))
    return mats

def q8_exact_k4():
    # Complex 8x8 represented on R^16; charpoly_real=charpoly_complex^2.
    I=sp.eye(2); qi=sp.diag(sp.I,-sp.I);qj=sp.Matrix([[0,1],[-1,0]])
    mats=[sgn*M for M in [I,qi,qj,qi*qj] for sgn in [1,-1]]
    real=[]
    for M in mats:
        R=M.applyfunc(sp.re);J=M.applyfunc(sp.im)
        real.append(R.row_join(-J).col_join(J.row_join(R)))
    G=graph('K4'); tree,cot=tree_edges(G);total=sp.Poly(0,x)
    for ids in itertools.product(range(8),repeat=3):
        A=sp.zeros(16)
        for (u,v),M in [(e,sp.eye(4)) for e in tree]+[(e,real[j]) for e,j in zip(cot,ids)]:
            A[4*u:4*u+4,4*v:4*v+4]=M;A[4*v:4*v+4,4*u:4*u+4]=M.T
        cp=flint.fmpz_mat([[int(v) for v in row] for row in A.tolist()]).charpoly()
        # Exact formal monic square root, then square back as certificate.
        high=list(map(int,cp.coeffs()))[::-1];root=[sp.Integer(1)]
        for k in range(1,9):
            root.append(sp.Rational(high[k]-sum(root[j]*root[k-j] for j in range(1,k)),2))
        p=sp.Poly.from_list(root,x)
        assert (p*p-sp.Poly(sum(int(c)*x**i for i,c in enumerate(cp.coeffs())),x)).is_zero
        total+=p
    return total.set_domain(sp.QQ).mul_ground(sp.Rational(1,512))

def main():
    print('Exact exterior-moment Weingarten integration; Python/SymPy/FLINT; no random input.')
    print('U(2): E minor_r(U) conjugate(minor_s(U)) = delta_rs delta_indices / binomial(2,r).')
    print('SU(2): same for r=s; plus the 0<->2 determinant-one contractions.')
    print('Raw U(2) fourth moments: Wg(id)=1/3, Wg(transposition)=-1/6.')
    G=graph('K4');mu=matching(G);su,stats=su2_average(G);u=matching_d(G,2)
    print('mu_K4 =',mu.as_expr());print('mu_K4^2 =',(mu*mu).as_expr());print('cycle census:',stats)
    assert su == mu*mu+sp.Poly(4*x*x+3,x)
    root_report(su,2,'SU(2) K4')
    print('K4 certified complex isolating rectangles:',sp.polys.polytools.intervals(su,all=True,eps=sp.Rational(1,10**7))[1])
    root_report(u,2,'U(2) K4 = HPS 2-matching = S3 standard')
    s=exact_finite_average(G,s3_standard()); print('independent exact S3 sum:',s.as_expr())
    assert (s-u).is_zero
    q=q8_exact_k4();print('independent exact Q8 sum:',q.as_expr());assert (q-su).is_zero
    c=sp.Poly((x**3-3*x)**2+1,x);root_report(c,1,'C3 SU(2) = Q8')
    print('positivity certificates: C3 = (x^3-3x)^2+1 >= 1; K4 = (x^4-6x^2+3)^2+4x^2+3 >= 3')
    y=sp.Symbol('y');f=y**3+3*y-1
    print('C3 imaginary-root certificate y^3+3y-1: f(8/25)=',f.subs(y,sp.Rational(8,25)),'f(33/100)=',f.subs(y,sp.Rational(33,100)),'f-prime=3y^2+3>0')
    print('If loops allowed: one vertex and one loop, q=1, SU2/Q8: x^2+1, roots +-i.')
    print('If parallel edges allowed: two vertices, three edges, q=2, SU2/Q8: (x^2-3)^2+3, no real roots.')
    print('degenerate q=0: K2, sign representation of Z2: x^2-1, roots -1,1, band {0}')
    print('PASS all exact identities')

if __name__=='__main__':main()
