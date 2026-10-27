"""Rational quotient models and a good characteristic-two equation for X0(37)."""
import os,sys
sys.dont_write_bytecode=True
P='/tmp/claude-1000/-home-tobias-Projects-riemann-channel/dcae8e10-414e-4cb4-8b95-d35e159cfb50/scratchpad/venv-astra/bin/python'
try: import cypari2
except ImportError: os.execv(P,[P,'-u',__file__])
from pizer_graph import pari, brandt
import sympy as s
x,y=s.symbols('x y')
f=-x**6-9*x**4-11*x**2+37
F=s.expand((f.subs(x,2*x+1)-16)/64)
print('good-at-2 equation Y^2+Y=F(X), F=',F)
assert s.expand(f.subs(x,2*x+1)-(8*y+4)**2)==64*(F-y*y-y)
for ell in [2,3,5,7]:
    try:
        cp=pari.hyperellcharpoly([pari(str(F).replace('**','^'))*pari.Mod(1,ell),pari.Mod(1,ell)])
        print('good-at-2 model ell=',ell,'Frobenius polynomial=',cp)
        B=brandt(37,ell)
        T=s.cancel(B.charpoly(x).as_expr()/(x-ell-1))
        expected=s.expand(x**2*T.subs(x,x+ell/x))
        assert s.expand(s.sympify(str(cp).replace('^','**'))-expected)==0
        print('good model vs Brandt characteristic polynomial MATCH PASS')
        for k in [1,2]:
            z=pari.ffgen(ell**k,'z')
            elems=[a*z**0 for a in range(ell)] if k==1 else [a+b*z for a in range(ell) for b in range(ell)]
            count=0
            for xx in elems:
                rhs=-xx**6-3*xx**5-6*xx**4-7*xx**3-5*xx**2-2*xx
                count+=len(pari.polrootsmod(pari('y')**2+pari('y')-rhs))
            count+=len(pari.polrootsmod(pari('y')**2+z**0))
            C=s.Matrix([[0,0,0,-expected.coeff(x,0)],[1,0,0,-expected.coeff(x,1)],[0,1,0,-expected.coeff(x,2)],[0,0,1,-expected.coeff(x,3)]])
            pred=ell**k+1-s.trace(C**k)
            print('good model direct point count ell,k=',ell,k,'N=',count,'expected=',pred)
            assert count==pred
    except Exception as exc:
        print('hyperellcharpoly/model check failed at',ell,':',exc)
        raise
for label in ['37a1','37b1']:
    try: print('database',label,pari('ellinit("'+label+'")')[:5])
    except Exception as exc: print('database unavailable:',str(exc).splitlines()[0])
eqs=[[0,0,1,-1,0],[0,1,1,-23,-50],[0,-9,0,11,37],[0,-11,0,-333,-1369]]
for label,eq in zip(['brief 37a','brief 37b','quotient x^2','quotient 1/x^2'],eqs):
    E=pari.ellinit(eq)
    minimal=pari.ellminimalmodel(E)
    print(label,'equation=',eq,'minimal=',minimal[:5],'j=',E.j(),'disc=',minimal.disc(),'conductor=',pari.ellglobalred(E)[0])
    for ell in [2,3,5,7]:
        em=pari.ellinit(minimal[:5],ell)
        print('ell=',ell,'a=',pari.ellap(em),'group=',pari.ellgroup(em))

# Exact independent J(F_5) computation by reduced Mumford divisors.
# x_old=2+1/x, y_old=y/x^3 moves a rational branch point to infinity.
f5=s.Poly(s.cancel(x**6*f.subs(x,2+1/x)),x,modulus=5)
assert f5.degree()==5 and s.gcd(f5,f5.diff()).degree()==0
print('odd degree F5 Jacobian model f=',f5.as_expr())
one=s.Poly(1,x,modulus=5); zero=s.Poly(0,x,modulus=5)
identity=(one,zero)
def key(D): return (tuple(int(a)%5 for a in D[0].all_coeffs()),tuple(int(a)%5 for a in D[1].all_coeffs()))
def add(D1,D2):
    u1,v1=D1; u2,v2=D2
    e1,e2,d1=s.gcdex(u1,u2)
    c1,c2,d=s.gcdex(d1,v1+v2)
    h1,h2,h3=c1*e1,c1*e2,c2
    uu=(u1*u2).exquo(d*d)
    vv=(h1*u1*v2+h2*u2*v1+h3*(v1*v2+f5)).exquo(d).rem(uu)
    while uu.degree()>2:
        uu=(f5-vv*vv).exquo(uu).monic()
        vv=(-vv).rem(uu)
    uu=uu.monic(); vv=vv.rem(uu)
    assert (vv*vv-f5).rem(uu).is_zero
    return uu,vv
divisors=[identity]
for a in range(5):
    uu=s.Poly(x+a,x,modulus=5)
    for b in range(5):
        vv=s.Poly(b,x,modulus=5)
        if (vv*vv-f5).rem(uu).is_zero: divisors.append((uu,vv))
for a in range(5):
    for b in range(5):
        uu=s.Poly(x*x+a*x+b,x,modulus=5)
        for c in range(5):
            for d in range(5):
                vv=s.Poly(c*x+d,x,modulus=5)
                if (vv*vv-f5).rem(uu).is_zero: divisors.append((uu,vv))
keys=set(map(key,divisors))
assert len(keys)==len(divisors)==48
hist={}; generator=None
for D in divisors:
    assert key(add(D,(D[0],-D[1])))==key(identity)
    current=identity; seen=set()
    for k in range(1,49):
        current=add(current,D)
        assert key(current) in keys
        seen.add(key(current))
        if key(current)==key(identity): break
    else: raise AssertionError('order does not divide 48')
    assert 48%k==0 and len(seen)==k
    hist[k]=hist.get(k,0)+1
    if k==48: generator=D
print('J37(F5) exact reduced-divisor count=',len(divisors),'order distribution=',sorted(hist.items()))
assert generator is not None
print('J37(F5) cyclic generator (u,v)=',generator[0].as_expr(),generator[1].as_expr(),'GROUP=[48]')
