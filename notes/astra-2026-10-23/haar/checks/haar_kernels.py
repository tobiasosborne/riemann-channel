#!/usr/bin/env python3
"""Exact small-group checks of the exterior kernels used for H4 reduction."""
import itertools
import sympy as s

I=s.I;half=s.Rational(1,2)

def matrix(q):
    a,b,c,d=q
    return s.Matrix([[a+I*b,c+I*d],[-c+I*d,a-I*b]])

def mul(a,b):
    w,x,y,z=a;v,X,Y,Z=b
    return tuple(s.expand(t) for t in (w*v-x*X-y*Y-z*Z,w*X+x*v+y*Z-z*Y,w*Y-x*Z+y*v+z*X,w*Z+x*Y-y*X+z*v))

def kernel(mats):
    # Entries of Lambda^0, Lambda^1 and Lambda^2 as a six-vector.
    out=s.zeros(6)
    for U in mats:
        v=s.Matrix([1,*list(U),s.simplify(U.det())])
        out+=v*v.conjugate().T
    return (out/len(mats)).applyfunc(s.simplify)

def main():
    axes=[]
    for i in range(4):
        for sign in [1,-1]:
            q=[s.Integer(0)]*4;q[i]=s.Integer(sign);axes.append(tuple(q))
    t=(-half,half,half,half);t2=mul(t,t)
    tetra=[(mul(q,p),j) for j,p in enumerate([(s.Integer(1),0,0,0),t,t2]) for q in axes]
    assert len({q for q,j in tetra})==24
    octa=[q for q,j in tetra]
    for i,j in itertools.combinations(range(4),2):
        for a,b in itertools.product([1,-1],repeat=2):
            q=[s.Integer(0)]*4;q[i]=a*s.sqrt(2)/2;q[j]=b*s.sqrt(2)/2;octa.append(tuple(q))
    assert len(set(octa))==48
    e=(-1+I*s.sqrt(3))/2
    target=s.diag(1,half,half,half,half,1)
    symplectic=target.copy();symplectic[0,5]=symplectic[5,0]=1
    cases=[('Q8',[matrix(q) for q in axes],symplectic),
           ('2T defining',[matrix(q) for q,j in tetra],symplectic),
           ('2T twist 1',[e**j*matrix(q) for q,j in tetra],target),
           ('2T twist 2',[e**(2*j)*matrix(q) for q,j in tetra],target),
           ('2O defining',[matrix(q) for q in octa],symplectic)]
    for name,mats,want in cases:
        actual=kernel(mats)
        assert actual==want
        print(name,'order',len(mats),'exterior kernel exactly',actual.tolist())
    # Check that eta(q*t^j)=zeta_3^j is a character, not merely a labeling.
    coset={q:j for q,j in tetra}
    for a,j in tetra:
        for b,k in tetra:assert coset[mul(a,b)]==(j+k)%3
    print('PASS: 2T quotient character checked on all 576 products; all exterior kernels exact.')

if __name__=='__main__':main()
