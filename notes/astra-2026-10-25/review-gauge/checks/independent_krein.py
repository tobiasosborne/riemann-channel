#!/usr/bin/env python3
"""Direct rational/algebraic matrix checks, without importing lane K.
Family polynomial is computed by a direct determinant, not half traces.
"""
import random
from math import comb
import numpy as np
import networkx as nx
import sympy as s
from sympy.polys.matrices import DomainMatrix
x=s.Symbol('x');I=s.eye(2);eta=s.diag(1,-1)
g=s.Matrix([[s.Rational(5,4),s.Rational(3,4)],[s.Rational(3,4),s.Rational(5,4)]])
h=s.diag((-3+4*s.I)/5,(-3-4*s.I)/5)

def adjacency(n,edges,labels):
    A=s.zeros(2*n)
    for j,(u,v) in enumerate(edges):
        U=labels.get(j,I)
        assert s.simplify(U.det())==1
        assert (U.conjugate().T*eta*U-eta).applyfunc(s.simplify)==s.zeros(2)
        A[2*u:2*u+2,2*v:2*v+2]+=U
        A[2*v:2*v+2,2*u:2*u+2]+=U.inv()
    return A.applyfunc(s.cancel)

def k4(G=g,H=h):
    return adjacency(4,[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)],{3:-I,4:G,5:H})

def cp(A):
    # DomainMatrix charpoly uses exact field arithmetic, not spectral traces.
    D=DomainMatrix.from_Matrix(A).to_field()
    coeff=D.charpoly()
    return s.Poly.from_list([D.domain.to_sympy(c) for c in coeff],x)

def evaluate(p,A):
    B=s.zeros(A.rows)
    for c in s.Poly(p,x).all_coeffs():B=B*A+c*s.eye(A.rows)
    return B.applyfunc(s.simplify)

def weil(A,q):
    H=s.diag(*([1,-1]*(A.rows//2)))
    return H.row_join(-H*A/2).col_join((-H*A/2).row_join(q*H))

def exact_rank(A):
    return DomainMatrix.from_Matrix(A.applyfunc(s.simplify),extension=True).rank()

def signature(A):
    vals=np.linalg.eigvalsh(np.array(A.evalf(30),complex))
    return tuple(int(v) for v in (np.sum(vals>1e-9),np.sum(vals < -1e-9),np.sum(abs(vals)<=1e-9)))

def examples():
    T=adjacency(2,[(0,1)]*3,{1:g,2:h});A=k4()
    print('theta degree sequence [3,3], q=2; edges are three parallel length-one edges')
    print('theta A over Q(i):',T.tolist())
    print('theta charpoly:',s.factor(cp(T).as_expr()))
    assert (T*T-s.Rational(14,5)*s.eye(4)).applyfunc(s.simplify)==s.zeros(4)
    print('theta A^2=(14/5)I; semisimple; eigenvalues +/-',s.N(s.sqrt(s.Rational(14,5)),60),'each twice')
    print('K4 A over Q(i):',A.tolist())
    p=(x-1)*(x**3+x**2-5*x-s.Rational(29,5))
    characteristic=cp(A)
    assert s.expand(characteristic.as_expr()-p*p)==0
    print('K4 charpoly factored:',s.factor(characteristic.as_expr()))
    print('K4 charpoly expanded:',characteristic.as_expr())
    assert evaluate(p,A)==s.zeros(8)
    print('K4 p(A)=0 exactly; gcd(p,p-prime)=',s.gcd(p,s.diff(p,x)))
    print('K4 eigenvalues, each twice:',s.nroots(p,n=60,maxsteps=500))
    intervals=s.polys.polytools.intervals(p,eps=s.Rational(1,10**30))
    assert len(intervals)==4 and all(m==1 and max(a*a,b*b)<8 for (a,b),m in intervals)
    print('K4 exact real-root intervals:',intervals)
    print('g eigenvalues:',g.eigenvals(),'g*h-h*g:',(g*h-h*g).tolist())
    print('h action on g boundary fixed pair is z ->',s.expand(h[0,0]**2),'*z, hence does not preserve {+1,-1}')
    C=s.kronecker_product(s.eye(4),s.Matrix([[0,1],[1,0]]))
    E=s.kronecker_product(s.eye(4),s.Matrix([[0,1],[-1,0]]))
    H=s.kronecker_product(s.eye(4),eta)
    assert C*C==s.eye(8) and C*A.conjugate()==A*C
    assert C.T*H*C==-H and A.T*E==E*A and A.conjugate().T*H==H*A
    Q=weil(A,2);assert exact_rank(Q)==16
    print('K4 C^2=+1; C anti-isometric; A^T E=E A; rank Q=16; inertia by anti-isometry (8,8,0)')
    J=s.zeros(8).row_join(H).col_join((-H).row_join(s.zeros(8)))
    M=A.row_join(-2*s.eye(8)).col_join(s.eye(8).row_join(s.zeros(8)))
    R=s.zeros(8).row_join(s.eye(8)).col_join((-s.eye(8)).row_join(s.zeros(8)))
    assert (M.conjugate().T*J*M-2*J).applyfunc(s.simplify)==s.zeros(16)
    assert (J*(M-2*M.inv())/2-Q).applyfunc(s.simplify)==s.zeros(16)
    assert R.T*J*R==J
    assert (R*M*R.inv()-s.zeros(8).row_join(-s.eye(8)).col_join((2*s.eye(8)).row_join(A)))==s.zeros(16)
    print('Companion/Weil similitude and symplectic label change checked EXACT')

def family():
    r=s.Symbol('r',real=True)
    c=(1+r*r)/(1-r*r);b=2*r/(1-r*r)
    # Transform to real coordinates before the determinant to avoid costly
    # symbolic complex coefficients. This is an exact constant similarity.
    S=s.Matrix([[1,s.I],[1,-s.I]]);P=s.kronecker_product(s.eye(4),S)
    Ar=(P.inv()*k4(s.Matrix([[c,b],[b,c]]))*P).applyfunc(s.cancel)
    assert all(s.im(z).simplify()==0 for z in Ar)
    expected=(x-1)*(x**3+x**2-5*x-(9+16*c)/5)
    characteristic=cp(Ar)
    assert s.cancel(characteristic.as_expr()-expected**2)==0
    print('K4 family direct determinant in rational Cayley coordinate r=tanh(t/2):',s.factor(characteristic.as_expr()))
    C=s.Symbol('c',real=True);cubic=x**3+x**2-5*x-(9+16*C)/5
    print('family reduced polynomial in c=cosh(t):',(x-1)*cubic)
    print('family cubic discriminant:',s.factor(s.discriminant(cubic,x)))
    cc=s.Rational(79,54);bb=5*s.sqrt(133)/54
    A=k4(s.Matrix([[cc,bb],[bb,cc]]));B=A+s.Rational(5,3)*s.eye(8)
    r1,r2=exact_rank(B),exact_rank(B*B)
    print('collision t*:',s.N(s.acosh(cc),70))
    print('collision reduced polynomial:',s.factor(((x-1)*cubic).subs(C,cc)))
    print('collision ranks:',r1,r2);assert (r1,r2)==(6,4)
    # Independent exact nullspace and radical certificate, not eig clustering.
    U=s.Matrix.hstack(*B.nullspace());H=s.diag(*([1,-1]*4))
    assert U.cols==2 and (U.conjugate().T*H*U).applyfunc(s.simplify)==s.zeros(2)
    print('collision eigenspace Gram matrix:',(U.conjugate().T*H*U).applyfunc(s.simplify).tolist())
    # Nullities 2 then 4 exhaust algebraic multiplicity 4: two size-two chains.
    assert exact_rank(weil(A,2))==16
    print('collision q=2: d0=0, rank Q=16, exact inertia (8,8,0); numerical',signature(weil(A,2)))
    # Stress test the defective-edge formula with an explicitly external cutoff.
    q=s.Rational(25,36);Q=weil(A,q)
    assert exact_rank(Q)==14
    assert exact_rank(A-s.Rational(5,3)*s.eye(8))==8
    print('same defective A with external q=25/36: geometric d0=2 (algebraic 4), rank Q=14; inertia (7,7,2); numerical',signature(Q))
    ce=(31+30*s.sqrt(2))/16;be=s.sqrt(ce*ce-1)
    Ae=k4(s.Matrix([[ce,be],[be,ce]]));Qe=weil(Ae,2)
    assert exact_rank(Qe)==14
    print('later true K4 band edge cosh(t)=',(31+30*s.sqrt(2))/16,'rank Q=14; inertia (7,7,2)')
    # Isospectral family: direct characteristic polynomial again.
    Aiso=(P.inv()*k4(s.Matrix([[c,b],[b,c]]),I)*P).applyfunc(s.cancel)
    assert s.cancel(cp(Aiso).as_expr()-((x*x-1)*(x*x-5))**2)==0
    assert evaluate((x*x-1)*(x*x-5),Aiso)==s.zeros(8)
    print('K4 unbounded isospectral family direct charpoly and annihilator PASS')

def rational_su11(r,u,v):
    rot=lambda a:s.diag((1+s.I*a)/(1-s.I*a),(1-s.I*a)/(1+s.I*a))
    boost=s.Matrix([[(1+r*r)/(1-r*r),2*r/(1-r*r)],[2*r/(1-r*r),(1+r*r)/(1-r*r)]])
    return (rot(u)*boost*rot(v)).applyfunc(s.cancel)

def unicyclic():
    rng=random.Random(20261025)
    for case,m in enumerate([3,4,5]):
        n=m+3;G=nx.cycle_graph(m)
        for v in range(m,n):G.add_edge(v,rng.randrange(v))
        E=sorted(tuple(sorted(e)) for e in G.edges())
        r=s.Rational(rng.randrange(1,5),7);u=s.Rational(rng.randrange(-5,6),7);v=s.Rational(rng.randrange(-5,6),11)
        U=rational_su11(r,u,v);A=adjacency(n,E,{E.index((0,m-1)):U})
        F=G.subgraph(range(m,n));chi=s.Matrix(nx.to_numpy_array(G,dtype=int)).charpoly(x).as_expr()
        chif=s.Matrix(nx.to_numpy_array(F,dtype=int)).charpoly(x).as_expr()
        predicted=s.expand(chi+(2-s.trace(U))*chif)
        actual=cp(A).as_expr();assert s.expand(actual-predicted**2)==0
        print('unicyclic case',case,'cycle',m,'edges',E,'Cayley r,u,v',r,u,v)
        print('holonomy=',U.tolist(),'trace=',s.trace(U))
        print('chi_Y=',chi,'chi_F=',chif,'reduced polynomial=',s.factor(predicted))
        print('direct 2n-by-2n characteristic determinant equals predicted square EXACT')
    # Explicit parabolic cases exercise the Jordan compression statement.
    par=s.Matrix([[1+s.I,1],[1,1-s.I]])
    for label,G in [('C3',nx.cycle_graph(3)),('C4',nx.cycle_graph(4)),('triangle-leaf',nx.Graph([(0,1),(1,2),(2,0),(0,3)]))]:
        E=sorted(tuple(sorted(e)) for e in G.edges());A=adjacency(len(G),E,{E.index((0,2)) if (0,2) in E else E.index((0,3)):par})
        B=s.Matrix(nx.to_numpy_array(G,nodelist=range(len(G)),dtype=int));p=B.charpoly(x).as_expr()
        squarefree=s.Poly(p,x).sqf_part()
        defect=evaluate(squarefree,A)!=s.zeros(A.rows)
        print('parabolic',label,'scalar charpoly',p,'defective',defect)
        if label=='triangle-leaf':assert not defect
        else:assert defect

def semicontinuity():
    Rb=s.diag((4+3*s.I)/5,(4-3*s.I)/5)
    Tb=adjacency(2,[(0,1)]*3,{2:Rb})
    assert (Tb*Tb-s.Rational(41,5)*s.eye(4)).applyfunc(s.simplify)==s.zeros(4)
    print('bounded theta nontrivial compact flux: delta=41/5 >8, kappa=0')
    Tnil=adjacency(2,[(0,1)]*3,{1:-g,2:-g})
    assert Tnil*Tnil==s.zeros(4) and exact_rank(Tnil)==2
    print('nilpotent theta S !=0, delta=0, rank A=2: two size-two blocks')
    for c in [s.Rational(31,4),s.Rational(8)]:
        G=s.Matrix([[c,s.sqrt(c*c-1)],[s.sqrt(c*c-1),c]])
        T=adjacency(2,[(0,1)]*3,{1:G,2:h});delta=s.simplify((T*T)[0,0])
        assert (T*T-delta*s.eye(4)).applyfunc(s.simplify)==s.zeros(4)
        print('theta crossing cosh(t)=',c,'delta=',delta,'closed-band kappa=',2 if delta<=8 else 0)
    omega=(-1+s.sqrt(3)*s.I)/2;R=s.diag(omega,s.conjugate(omega))
    T0=adjacency(2,[(0,1)]*3,{1:R,2:R.inv()})
    T1=adjacency(2,[(0,1)]*3,{1:g*R,2:R.inv()})
    assert T0==s.zeros(4) and (T1*T1).applyfunc(s.simplify)==-s.eye(4)/2
    print('interior theta: A0=0 semisimple kappa=2; at t=log(2), A^2=-I/2 kappa=0')

if __name__=='__main__':
    examples();family();unicyclic();semicontinuity();print('PASS independent Krein checks')
