#!/usr/bin/env python3
"""Independent Z_p lattice HNF reduction, BFS balls and projector axis test.

Author route: valuations of entries/determinant, intersections with eigenlines.
Review route: HNF of an augmented integer module modulo p^precision; split test
by the eigenprojector preserving the lattice. No imports from the Fable lane.
"""
import random
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form

INF=10**6
def vp(x,p):
    x=s.Rational(x)
    if not x:return INF
    a,b=abs(int(x.p)),int(x.q);v=0
    while a%p==0:a//=p;v+=1
    while b%p==0:b//=p;v-=1
    return v

def module_hnf(B,p,N=24,primitive=True):
    """Recover a Q_p homothety class as canonical integer column HNF.
    Add p^N Z^2 to replace prime-to-p divisibility by invertibility in Z_p.
    """
    low=min(vp(x,p) for x in B)
    C=B*s.Rational(p)**(-low)
    modulus=p**N
    R=C.applyfunc(lambda x:int(x.p)*pow(int(x.q),-1,modulus)%modulus)
    H=hermite_normal_form(R.row_join(modulus*s.eye(2)))
    assert vp(H.det(),p)<N
    if primitive:
        common=min(vp(x,p) for x in H)
        H=H/(p**common)
    return H

def key(B,p):return tuple(module_hnf(B,p))
def distance(B,C,p):
    H=module_hnf(B.inv()*C,p)
    # Primitive HNF quotient is cyclic of order p^distance.
    return vp(H.det(),p)

def ball(p,R):
    I=s.eye(2);out={key(I,p):(I,0)};front=[I]
    moves=[s.Matrix([[1,0],[t,p]]) for t in range(p)]+[s.diag(p,1)]
    for d in range(1,R+1):
        new=[]
        for B in front:
            for M in moves:
                H=module_hnf(B*M,p);k=tuple(H)
                if k not in out:out[k]=(H,d);new.append(H)
        front=new
    return list(out.values())

def roots_digitwise(t,d,p,N=22):
    v=vp(t,p);t0=int(t/p**v);d0=int(d/p**(2*v))
    roots=[0,t0%p];mod=p
    for j in range(1,N):
        new=[]
        for r in roots:
            candidates=[r+a*mod for a in range(p) if ((r+a*mod)**2-t0*(r+a*mod)+d0)%(mod*p)==0]
            assert len(candidates)==1
            new.append(candidates[0])
        roots=new;mod*=p
    return sorted([r*p**v for r in roots],key=lambda x:vp(x,p))

def inspect(G,p,vertices):
    t,d=G.trace(),G.det();ell=max(vp(d,p)-2*vp(t,p),0)
    ds=[distance(s.eye(2),G**k,p) for k in range(1,6)]
    if ell:
        a,b=roots_digitwise(t,d,p)
        E=(G-b*s.eye(2))/(a-b)
        on=split=0
        for B,_ in vertices:
            disp=distance(B,G*B,p)
            # Integral idempotent gives direct-sum decomposition of the lattice.
            preserves=all(vp(x,p)>=0 for x in B.inv()*E*B)
            on+=disp==ell;split+=preserves
            assert preserves==(disp==ell),(G,B,disp,preserves)
        assert vp(b,p)-vp(a,p)==ell
        extra=f'eigenvaluations={(vp(a,p),vp(b,p))} axis={on} projector_split={split}'
    else:extra='elliptic geometric/stable length zero'
    print('p=',p,'G=',list(G),'tr=',t,'det=',d,'ell=',ell,'base_distances=',ds,extra)

def main():
    J=s.Matrix([[0,1],[-1,0]])
    rng=random.Random(727104)
    for p in [3,5,7]:
        for trial in range(12):
            while True:
                G=s.Matrix(2,2,lambda i,j:s.Rational(rng.randint(-20,20))*s.Rational(p)**rng.randint(-2,2))
                if G.det():break
            dual=(G.T*J.T).inv();claimed=G/G.det()
            transition=claimed.inv()*dual
            assert all(vp(x,p)>=0 for x in transition) and vp(transition.det(),p)==0
            k=vp(G.det(),p);L0=G*s.Rational(p)**(-(k//2))
            assert vp(L0.det(),p)==k%2
            print('dual/parity p=',p,'trial=',trial,'vdet=',k,'canonical_k=',vp(L0.det(),p),'correct=True')
    examples={3:[s.Matrix([[8,5],[9,0]]),s.Matrix([[-1,12],[10,-6]]),s.Matrix([[6,-11],[12,4]])],5:[s.Matrix([[-2,-8],[4,-4]])]}
    for p in [3,5]:
        vertices=ball(p,3)
        print('BFS HNF ball p=',p,'radius=3 vertices=',len(vertices))
        for G in examples[p]:inspect(G,p,vertices)
        for j in range(10):
            while True:
                G=s.Matrix(2,2,lambda i,k:rng.randint(-12,12))
                if G.det():break
            inspect(G,p,vertices)
        # An exact conjugate whose axis does not contain the base vertex.
        H=s.Matrix([[1,s.Rational(1,p)],[0,1]])
        inspect(H*s.diag(1,p)*H.inv(),p,vertices)
        # Counterexample to the lane's "g^2 x=x implies d(x,gx)=1" step.
        G=s.Matrix([[0,1],[p,0]])
        L=s.diag(1,p**2)
        print('inversion p=',p,'G^2=',list(G**2),'off-axis vertex=',list(L),'d(L,GL)=',distance(L,G*L,p),'d(L,G^2 L)=',distance(L,G**2*L,p))
        assert distance(L,G*L,p)==3 and distance(L,G**2*L,p)==0
    # Even translation length does not suffice for a Q_p symplectic lift.
    G=s.diag(1,18)
    print('square-class counterexample p=3 gamma=diag(1,18), ell=',distance(s.eye(2),G,3),'unit determinant mod 3=',(18//9)%3,'unit squares mod 3=',sorted({x*x%3 for x in [1,2]}))
    print('code towers p=3 qunaught dims=',[3**(2*m) for m in range(4)],'qudit dims=',[3**(1+2*m) for m in range(4)])
    print('ALL INDEPENDENT LATTICE CHECKS PASSED')

if __name__=='__main__':main()
