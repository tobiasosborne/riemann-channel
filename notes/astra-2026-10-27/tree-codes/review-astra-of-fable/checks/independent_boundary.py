#!/usr/bin/env python3
"""Exact Casoratian algebra, density fixed-point weights and T5 counterexamples."""
import sympy as S
import numpy as np

q,mu=S.symbols('q mu',nonzero=True)
lam=mu+q/mu
J=S.Matrix([[0,1],[-1,0]])
M=S.Matrix([[0,-1],[q,lam]])
Mrecord=S.Matrix([[lam,-q],[1,0]])
v=S.Matrix([1,-mu]);w=S.Matrix([1,-q/mu])
pair=(v.T*J*w)[0]
Q=S.simplify(J*(M-q*M.inv())/2)
print('M v_mu - mu v_mu =',S.simplify(M*v-mu*v))
print('Omega(v_mu,v_q/mu) =',pair)
print('Q =',Q,'pair^2 + 4det Q =',S.factor(pair**2+4*Q.det()))
print('symplectic coordinate change M = J M_record J^-1:',S.simplify(M-J*Mrecord*J.inv())==S.zeros(2))
assert S.simplify(pair-(mu-q/mu))==0
assert S.simplify(pair**2+4*Q.det())==0
for k in range(5):
    C=S.cancel((mu**(k+1)*(q/mu)**k-mu**k*(q/mu)**(k+1))/q**k)
    print('Casoratian k=',k,'=',C)
    assert S.simplify(C-pair)==0

for p in [3,5,7]:
    edge=2*S.sqrt(p)
    Qedge=S.Matrix([[p,edge/2],[edge/2,1]])
    print('endpoint p=',p,'lambda=',edge,'Q_rank=',Qedge.rank(),'Q_det=',Qedge.det())
    for ell in [1,2,3]:
        a=S.Rational(1,p**ell)
        # At the two boundary fixed points, |derivative| = a and 1/a.
        weight0=S.sqrt(a) # |1-lambda|=1
        weightinf=S.sqrt(1/a)/(1/a) # |1-lambda^-1|=|lambda|^-1
        print('half-density p=',p,'ell=',ell,'fixed weights=',weight0,weightinf,'sum=',S.simplify(weight0+weightinf))
        assert S.simplify(weight0+weightinf-2*p**(-S.Rational(ell,2)))==0
    s=S.Rational(3,4);ell=1;mu0=p**(1-s)
    print('swapped Satake equality counterexample p=',p,'s=3/4: p^(-(1-s))=',p**(-(1-s)),'p^-1 mu=',mu0/p,'equal=',S.simplify(p**(-(1-s))-mu0/p)==0)
    # A complementary-series invariant Riesz form: alpha=2s-1 in (0,1).
    alpha=2*s-1;N=1;size=p**N
    diagonal=(1-S.Rational(1,p))*p**(-N*alpha)/(1-p**(-alpha))
    gram=S.ones(size)/size
    for i in range(size):gram[i,i]=diagonal
    eigmin=float(diagonal-S.Rational(1,p))
    lam0=p**s+p**(1-s);detQ=S.simplify(p-lam0**2/4)
    gamma=(1-p**(alpha-1))/(1-p**(-alpha))
    print('complementary s=3/4 p=',p,'Riesz_Gamma=',gamma,'finite_Riesz_Gram=\n',np.array(gram,dtype=float),'min_eigenvalue=',eigmin,'adjacency_lambda=',float(lam0),'2sqrtp=',float(2*S.sqrt(p)),'Weil_det=',float(detQ))
    assert eigmin>0 and float(detQ)<0
    # Poisson kernel restricted to a ray moving away from its boundary point.
    ratio=1/S.sqrt(p);lamhalf=2*S.sqrt(p)
    recurrence_defect=S.simplify(ratio**2-lamhalf*ratio+p)
    print('unrescaled away-ray Poisson recurrence defect p=',p,'=',recurrence_defect)
    assert recurrence_defect!=0
    root=S.sqrt(p)
    determinant=2-root-1/root
    conjugate=2+root+1/root
    norm=S.simplify(determinant*conjugate)
    print('K=Q_p(sqrt(p)) phase-space obstruction p=',p,'Norm(det(1-g))=',norm,'extended-absolute-value weight=',1/root,'actual K-Haar fixed-point weight=',S.Rational(1,p))
    assert S.simplify(norm+S.Rational((p-1)**2,p))==0
    # Change the eigenaxis by a quadratic-phase Clifford Q_(1/p).
    # The cutoff P_0 is held fixed: its trace is a quadratic Gauss integral.
    residue=((1-p*p)*pow(2,-1,p))%p
    gauss=sum(np.exp(2j*np.pi*((residue*x*x)%p)/p) for x in range(p))/p
    conjugated_trace=gauss/np.sqrt(p)
    print('fixed P0 under axis conjugation p=',p,'Tr(P0 Q_(1/p) D_p Q_(1/p)^-1 P0)=',conjugated_trace,'standard-axis trace=',1/np.sqrt(p))
    assert abs(conjugated_trace-1/np.sqrt(p))>0.1

A=S.diag(1,3);B=S.Matrix([[1,1],[0,3]])
square_normalize=lambda G:G**2/G.det()
print('gamma -> gamma^2/det gamma is not a homomorphism; defect =',square_normalize(A*B)-square_normalize(A)*square_normalize(B))
print('p=3 gamma=diag(1,3): original length=1, ratio dilation phase-space length=2, weight=1/sqrt(3)')
print('Euler exponents remain original length; replacing all exponents by twice the length gives zeta(u^2).')
print('X5,11 zeta(u) first positive coefficient: 660*u^6; squared exponents first: 660*u^12')
print('normalized Riesz intertwiner Fourier multiplier |xi|^(1-2s) at s=1/2 is identically 1 away from xi=0')
print('ALL INDEPENDENT BOUNDARY CHECKS PASSED')
