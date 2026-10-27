"""Exact modular-polynomial / modular-form comparison. Run with python3.

Reexecutes the preinstalled PARI interpreter; never downloads anything.
The actual isogeny-duality certificate is supplied by pizer_quotient.py.
"""
import os, sys
sys.dont_write_bytecode = True
PARI_PY = '/tmp/claude-1000/-home-tobias-Projects-riemann-channel/dcae8e10-414e-4cb4-8b95-d35e159cfb50/scratchpad/venv-astra/bin/python'
try:
    from cypari2 import Pari
except ImportError:
    os.execv(PARI_PY, [PARI_PY, '-u', __file__, *sys.argv[1:]])
import math
import sympy as s
import numpy as np
pari=Pari()
pari.allocatemem(512000000, silent=True)
x,u=s.symbols('x u')

def sp(poly):
    return s.Poly(str(poly).replace('^','**'),x).as_expr()

def supersingular(p):
    t=pari.ffgen(p*p,'t')
    X=pari('x')
    m=(p-1)//2
    H=sum(math.comb(m,k)**2*X**k for k in range(m+1))*t**0
    roots=pari.polrootsmod(H)
    js=[]
    for a in roots:
        j=256*(1-a+a*a)**3/(a*a*(1-a)**2)
        if not any(j==b for b in js): js.append(j)
    js.sort(key=str)
    assert all(pari.ellissupersingular(j)==1 for j in js)
    w=[3 if j==0 else 2 if j==1728 else 1 for j in js]
    expected=p//12+{1:0,5:1,7:1,11:2}[p%12]
    assert len(js)==expected
    return t,js,w

def brandt(p,ell,js=None):
    if js is None: _,js,_=supersingular(p)
    Phi=pari.polmodular(ell)
    B=s.zeros(len(js))
    for i,j in enumerate(js):
        f=pari.subst(Phi,'y',j)
        factors=pari.factor(f)
        for k in range(factors.nrows()):
            pol,mult=factors[k,0],int(factors[k,1])
            assert pari.poldegree(pol)==1
            root=-pari.polcoef(pol,0)/pari.polcoef(pol,1)
            target=next(a for a,b in enumerate(js) if b==root)
            B[i,target]+=mult
    assert all(sum(B.row(i))==ell+1 for i in range(B.rows))
    return B

def charpoly_pari(A):
    return sp(pari.charpoly(pari.matrix(A.rows,A.cols,list(A))))

def hecke_data(p,ells):
    mf=pari.mfinit([p,2],1)
    eig=pari.mfeigenbasis(mf)
    coefs=[pari.mfcoefs(f,max(ells)) for f in eig]
    result={}
    for ell in ells:
        cp=sp(pari.charpoly(pari.mfheckemat(mf,ell)))
        eigenvalues=[v[ell] for v in coefs]
        # Characteristic polynomial on each coefficient field, not just minpoly:
        ep=pari(1)
        for a in eigenvalues:
            ep*=pari.charpoly(a,'x') if a.type()=='t_POLMOD' else pari('x')-a
        assert s.expand(sp(ep)-cp)==0
        result[ell]=(cp,eigenvalues)
    return result

def dart_hashimoto(B,halfloops):
    """halfloops[i] are reversal-fixed darts; remaining loops form pairs."""
    darts=[]; rev=[]
    def pair(a,b):
        k=len(darts); darts.extend([a,b]); rev.extend([k+1,k])
    for i in range(B.rows):
        h=halfloops[i]
        assert h<=B[i,i] and (int(B[i,i])-h)%2==0
        for _ in range(h):
            rev.append(len(darts)); darts.append((i,i))
        for _ in range((int(B[i,i])-h)//2): pair((i,i),(i,i))
        for j in range(i+1,B.rows):
            assert B[i,j]==B[j,i]
            for _ in range(int(B[i,j])): pair((i,j),(j,i))
    H=s.zeros(len(darts))
    for e,(_,target) in enumerate(darts):
        for f,(source,_) in enumerate(darts):
            H[e,f]=int(target==source and f!=rev[e])
    return H,darts,rev

def bass_check(B,ell,halfloops):
    H,darts,rev=dart_hashimoto(B,halfloops)
    cp=charpoly_pari(H)
    detH=s.expand(u**H.rows*cp.subs(x,1/u))
    detV=s.expand(B.charpoly(x).as_expr().subs(x,(1+ell*u*u)/u)*u**B.rows)
    h=sum(halfloops); m=(len(darts)-h)//2
    rhs=s.cancel((1-u*u)**(m-B.rows)*(1+u)**h*detV)
    assert s.expand(detH-rhs)==0
    return m,h,s.factor(detH)

def curve37_check(ell,P):
    # The brief's affine equation is a Q-model; its written reduction is bad at 2.
    if ell==2:
        f=pari('(-x^6-3*x^5-6*x^4-7*x^3-5*x^2-2*x)')*pari.Mod(1,2)
        cp=sp(pari.hyperellcharpoly([f,pari.Mod(1,2)]))
        got=s.expand(u**4*cp.subs(x,1/u))
        assert s.expand(got-P)==0
        print('X0(37) good characteristic-two model hyperellcharpoly=',cp,'P match=True')
        return
    f=pari('(-x^6-9*x^4-11*x^2+37)')*pari.Mod(1,ell)
    if pari.poldegree(pari.gcd(f,pari.deriv(f)))>0:
        print('X0(37) displayed sextic singular at',ell,'; skipped')
        return
    cp=sp(pari.hyperellcharpoly(f))
    got=s.expand(u**4*cp.subs(x,1/u))
    print('X0(37) sextic hyperellcharpoly=',cp,'P match=',s.expand(got-P)==0)
    # Also independently count points, including infinity, over F_ell and F_ell^2.
    for k in [1,2]:
        g=pari.ffgen(ell**k,'t')
        elems=[a*g**0 for a in range(ell)] if k==1 else [a+b*g for a in range(ell) for b in range(ell)]
        N=0
        for a in elems:
            v=-a**6-9*a**4-11*a*a+37
            N+=1 if v==0 else 2 if v**((ell**k-1)//2)==1 else 0
        lead=-g**0
        N+=2 if lead**((ell**k-1)//2)==1 else 0
        F=s.Matrix([[0,0,0,-cp.coeff(x,0)],[1,0,0,-cp.coeff(x,1)],[0,1,0,-cp.coeff(x,2)],[0,0,1,-cp.coeff(x,3)]])
        expected=ell**k+1-s.trace(F**k)
        print('sextic direct N',k,'=',N,'charpoly N=',expected)
        assert N==expected
    assert s.expand(got-P)==0

def main():
    print('PARI',pari('version()'))
    ells=[2,3,5,7]
    for p in [37,73,109,101,11,13]:
        t,js,w=supersingular(p)
        print('\np=',p,'field generator=',t,'j=',[str(j) for j in js],'weights=',w,'h=',len(js))
        hecke=hecke_data(p,ells) if len(js)>1 else {ell:(s.Integer(1),[]) for ell in ells}
        genus=s.Rational(p+1,12)-s.Rational(1+s.kronecker_symbol(-1,p),4)-s.Rational(1+s.kronecker_symbol(-3,p),3)
        assert genus==len(js)-1
        mass=sum(s.Rational(1,a) for a in w)
        assert mass==s.Rational(p-1,12)
        print('genus=',len(js)-1,'genus formula=',genus,'mass=',mass,'expected=',s.Rational(p-1,12))
        for ell in ells:
            B=brandt(p,ell,js)
            cp,eig=hecke[ell]
            assert s.expand(B.charpoly(x).as_expr()-(x-ell-1)*cp)==0
            W=s.diag(*w); D=W.inv()
            assert D*B==B.T*D
            print('\nell=',ell,'B=',B.tolist())
            print('cusp charpoly=',s.factor(cp),'newform coefficients=',[str(a) for a in eig])
            S=np.diag([1/math.sqrt(a) for a in w])@np.array(B.tolist(),dtype=float)@np.diag([math.sqrt(a) for a in w])
            vals=np.linalg.eigvalsh(S)
            print('eigenvalues (double display only)=',vals.tolist(),'bound=',2*math.sqrt(ell))
            # Exact positive-definiteness of 4 ell I - A_cusp^2, in weighted metric.
            # Use rational kernel of stationary row (1/w_i).
            K=s.Matrix.hstack(*s.Matrix([[s.Rational(1,a) for a in w]]).nullspace()) if B.rows>1 else s.zeros(1,0)
            G=K.T*D*(4*ell*s.eye(B.rows)-B*B)*K
            minors=[G[:k,:k].det() for k in range(1,G.rows+1)]
            assert all(a>0 for a in minors)
            P=s.cancel(u**(len(js)-1)*cp.subs(x,(1+ell*u*u)/u))
            print('P=',s.expand(P),'#X0(p)(F_ell)=',ell+1+cp.coeff(x,len(js)-2) if len(js)>1 else ell+1)
            print('exact strict Ramanujan leading minors=',minors,'DETERMINANT MATCH PASS')
            if all(a==1 for a in w):
                from pizer_quotient import natural_halfloops
                actualB,half=natural_halfloops(p,ell)
                assert actualB==B
                m,h,detH=bass_check(B,ell,half)
                print('ACTUAL ISOGENY DUALITY halfloops=',half,'paired edges=',m,'fixed darts=',h,'BASS PASS; det(I-uH)=',detH)
                if h: print('ACTUAL REVERSAL HAS FIXED DARTS: ordinary Bass needs correction')
            else:
                print('WEIGHTED EDGE-INDEXED QUOTIENT; no ordinary-graph Bass assertion')
            if p==37: curve37_check(ell,P)
    print('\nALL P1 MATRIX / HECKE / POSITIVITY CHECKS PASS')

if __name__=='__main__': main()
