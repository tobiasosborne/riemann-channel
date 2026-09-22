# Author: codex:gpt-6-astra
"""Compare the independent finite quotient graph with closed-form Eisenstein blocks."""
import sys
sys.dont_write_bytecode = True
from finite_graph import *
import cmath

def characters(f):
    gen=f.primitive(); logs={f.power(gen,k):k for k in range(f.Q-1)}
    return [[0]+[cmath.exp(2j*np.pi*j*logs[a]/(f.Q-1)) for a in range(1,f.Q)] for j in range(f.Q-1)]

def completed(f,chi,even=True):
    co=[sum(chi[f.q**n+a] for a in range(f.q**n)) for n in range(f.d)]
    return np.cumsum(co)[:-1] if even else np.array(co)

def val(co,t):return sum(a*t**i for i,a in enumerate(co))

def phi(q,d,u,co=None,cobar=None):
    Q=q**d
    if co is None:
        base=q*(1-u*u)/(1-q*q*u*u)
        return base/(1-u**(2*d))*np.array([[(Q-1)*u**(2*d),u**d*(1-Q*u**(2*d))],[u**d*(1-Q*u**(2*d)),(Q-1)*u**(2*d)]],complex)
    A=lambda p:q*u**d*val(p,q*u*u)/val(p,u*u)
    return np.array([[0,A(co)],[A(cobar),0]],complex)

if __name__=='__main__':
    for q,N in CASES:
        g=quotient(q,N,1); f=g['f'];d=f.d;r=(f.Q-1)//(q-1); chars=characters(f)
        even=list(range(0,f.Q-1,q-1));U=np.zeros((2*r,2*r),complex)
        for k,j in enumerate(even):
            for t,(kind,label) in enumerate(g['tails']):U[t,2*k+kind]=chars[j][label]/np.sqrt(r)
        err=0; fe=0;le=0;ge=0
        for j,chi in enumerate(chars[1:],1):
            ev=j%(q-1)==0;co=completed(f,chi,ev);cobar=np.conj(co);m=d-2 if ev else d-1
            G=sum(chi[a]*cmath.exp(2j*np.pi*f.vec[a][-1]/q) for a in range(1,f.Q))
            tau=sum(chi[a]*cmath.exp(2j*np.pi*a/q) for a in range(1,q))
            eps=G/q**(d/2) if ev else G/(tau*q**((d-1)/2))
            ge=max(ge,abs(eps-co[-1]/q**(m/2)))
            for t in (.17,.31+.04j):le=max(le,abs(val(co,t)-eps*(q**.5*t)**m*val(cobar,1/(q*t))))
        for u in (.17,.29+.03j):
            z=1/(q**.5*u);actual=U.conj().T@scattering(g,z)@U;expected=np.zeros_like(actual)
            for k,j in enumerate(even):
                if j:co=completed(f,chars[j]);p=phi(q,d,u,co,np.conj(co));p1=phi(q,d,1/(q*u),co,np.conj(co))
                else:p=phi(q,d,u);p1=phi(q,d,1/(q*u))
                D=np.diag([z**(d-1),z**-1]);expected[2*k:2*k+2,2*k:2*k+2]=D@np.linalg.inv(p)@D
                fe=max(fe,np.max(abs(p@p1-np.eye(2))))
            err=max(err,np.max(abs(actual-expected)))
        assert err<1e-7 and fe<1e-10 and le<1e-10 and ge<1e-10
        print('q,d',q,d,'graph/block',err,'matrix FE',fe,'L FE',le,'Gauss',ge)
        if err>1e-6:
            print('ACTUAL block',actual[2:4,2:4]);print('EXPECTED block',expected[2:4,2:4])
    # A separate determinant/zero-count check in a numerically stable disk region.
    for q,N in CASES+[(5,[2,0,1]),(5,[1,1,0,1])]:
        g=quotient(q,N,1);f=g['f'];d=f.d;r=(f.Q-1)//(q-1);chars=characters(f);derr=0;zeros=0
        for j in range(q-1,f.Q-1,q-1):
            co=completed(f,chars[j]);roots=np.roots(list(co)[::-1])
            assert all(abs(abs(t)-q**-.5)<1e-10 for t in roots)
            zeros+=4*len(roots)
        for z in (.71+.16j,.57+.23j):
            u=1/(q**.5*z);detphi=np.linalg.det(phi(q,d,u))
            for j in range(q-1,f.Q-1,q-1):
                co=completed(f,chars[j]);R=val(co,q*u*u)/val(co,u*u)
                detphi*=(-q*q*u**(2*d))*R*R
            expected=z**(2*(d-2)*r)/detphi
            actual=np.linalg.det(scattering(g,z));derr=max(derr,abs(actual/expected-1))
        expected_modes=6*d-6+(r-1)*(8*d-12) if d>1 else 0
        assert zeros+(2*d-2)+4*(d-1)*r==expected_modes
        assert derr<1e-8
        print('determinant/Weil/model q,d',q,d,'relative error',derr,'arithmetic',zeros,'model',expected_modes)
