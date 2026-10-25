#!/usr/bin/env python3
"""Independent exact genus-two and targeted genus-three witness enumeration.
Also audits double-cover candidates for the cube/Petersen targets.
"""
import itertools
import json
from pathlib import Path
import sympy as S
from census_lookup import HERE,FLUX,coeff_from_counts,counts_from_coeff

def rem(a,b):
    while a and a.bit_length()>=b.bit_length():
        a^=b<<(a.bit_length()-b.bit_length())
    return a

def gcd(a,b):
    while b:a,b=b,rem(a,b)
    return a

def pmul(a,b):
    out=0
    while b:
        if b&1:out^=a
        a<<=1;b>>=1
    return out

def deriv(a):
    return sum(1<<(i-1) for i in range(1,a.bit_length(),2) if a>>i&1)

class Field:
    MOD={1:3,2:7,3:11,4:19,5:37,6:67,7:131,8:285,9:529,10:1033,11:2053,12:4179}
    def __init__(self,k):
        self.k=k;self.q=1<<k;self.mod=self.MOD[k]
        # Rabin irreducibility: x^(2^k)=x and gcd at prime divisors of k.
        z=rem(2,self.mod)
        seq=[z]
        for _ in range(k):
            z=rem(pmul(z,z),self.mod);seq.append(z)
        assert z==seq[0]
        for p in S.factorint(k):assert gcd(seq[k//int(p)]^seq[0],self.mod)==1
    def mul(self,a,b):return rem(pmul(a,b),self.mod)
    def power(self,a,n):
        r=1
        while n:
            if n&1:r=self.mul(r,a)
            a=self.mul(a,a);n>>=1
        return r
    def ev(self,pol,x):
        out=0
        for i in range(pol.bit_length()-1,-1,-1):out=self.mul(out,x)^((pol>>i)&1)
        return out

def smooth_hyp(h,f,g):
    hp=deriv(h);fp=deriv(f)
    finite=gcd(h,pmul(fp,fp)^pmul(pmul(hp,hp),f))==1
    infinity=((h>>(g+1))&1) or (((f>>(2*g+1))&1)^(((h>>g)&1)&((f>>(2*g+2))&1)))
    return finite and bool(infinity)

def hyp_count(h,f,g,F):
    # Direct y enumeration; both standard weighted-projective charts.
    n=0
    for x in range(F.q):
        a,b=F.ev(h,x),F.ev(f,x)
        n+=sum((F.mul(y,y)^F.mul(a,y)^b)==0 for y in range(F.q))
    a,b=(h>>(g+1))&1,(f>>(2*g+2))&1
    return n+sum((F.mul(y,y)^F.mul(a,y)^b)==0 for y in range(F.q))

def polstr(n,var='x'):
    return '+'.join(('1' if i==0 else var if i==1 else f'{var}^{i}') for i in range(n.bit_length()) if n>>i&1) or '0'

def transform(poly,degree,mat):
    a,b,c,d=mat;u=(a<<1)|b;v=(c<<1)|d
    up=[1];vp=[1]
    for _ in range(degree):up.append(pmul(up[-1],u));vp.append(pmul(vp[-1],v))
    out=0
    for i in range(degree+1):
        if poly>>i&1:out^=pmul(up[i],vp[degree-i])
    return out

def factors():
    x=S.Symbol('x');targets={}
    for r in json.loads(FLUX.read_text()):
        if not r['ramanujan'] or r['p']!=2:continue
        for f,e in S.factor_list(S.Poly.from_list(r['weil_coefficients'],x))[1]:
            if f.degree() in [4,6]:
                c=tuple(map(int,f.all_coeffs()))
                targets.setdefault(c,[]).append(f"{r['graph']}:{r['mask']}")
    return targets

def main():
    F=[Field(k) for k in range(1,5)];targets=factors()
    results={};all2={};elliptic=[]
    X,Y,Z=S.symbols('X Y Z')
    for trace,a1,a2,a3,a4,a6 in [(0,0,0,1,0,0),(-2,0,0,1,1,0),(2,0,0,1,1,1),(-1,1,0,0,0,1),(1,1,1,0,0,1)]:
        equation=Y*Y*Z+a1*X*Y*Z+a3*Y*Z*Z-X**3-a2*X*X*Z-a4*X*Z*Z-a6*Z**3
        for v in [X,Y,Z]:
            vs=[w for w in [X,Y,Z] if w!=v];ff=equation.subs(v,1)
            assert list(S.groebner([ff]+[S.diff(ff,w) for w in vs],*vs,modulus=2))==[1]
        NN=[]
        for field in F[:2]:
            nn=1
            for xx in range(field.q):
                for yy in range(field.q):
                    rhs=field.power(xx,3)^field.mul(a2,field.mul(xx,xx))^field.mul(a4,xx)^a6
                    lhs=field.mul(yy,yy)^field.mul(a1,field.mul(xx,yy))^field.mul(a3,yy)
                    nn+=int(lhs==rhs)
            NN.append(nn)
        assert NN==counts_from_coeff([1,-trace,2],2)
        ee=dict(trace=trace,coeff=[1,-trace,2],weierstrass=[a1,a2,a3,a4,a6],N=NN)
        elliptic.append(ee);print('ELLIPTIC',ee,'smoothness PASS',flush=True)
    for g in [2,3]:
        wanted={c for c in targets if len(c)==2*g+1}
        target_counts={tuple(counts_from_coeff(c,g)):c for c in wanted}
        smooth=0;hits={c:[] for c in wanted}
        for h in range(1,1<<(g+2)):
            for f in range(1<<(2*g+3)):
                if not smooth_hyp(h,f,g):continue
                smooth+=1;Ns=[]
                for k in range(1,g+1):
                    Ns.append(hyp_count(h,f,g,F[k-1]))
                    if g==3 and not any(tuple(Ns)==a[:k] for a in target_counts):break
                if len(Ns)<g:continue
                c=tuple(coeff_from_counts(Ns))
                if g==2:all2.setdefault(c,(h,f))
                if c in wanted:hits[c].append((h,f))
        print('HYPERELLIPTIC genus',g,'smooth equations',smooth,'genus2 polynomial count',len(all2),flush=True)
        for c,hh in sorted(hits.items()):
            result=dict(coeff=c,targets=targets[c],hyp_equations=len(hh))
            if hh:
                h,f=hh[0];counts=[hyp_count(h,f,g,Field(k)) for k in range(1,2*g+1)]
                assert counts==counts_from_coeff(c,2*g)
                result.update(h=h,f=f,equation=f'y^2+({polstr(h)})y={polstr(f)}',counts=counts)
            results[str(c)]=result
            print('FACTOR',result,flush=True)
            if c==(1,0,1,0,4):
                orbit=set()
                for mat in itertools.product(range(2),repeat=4):
                    a,b,cc,d=mat
                    if (a*d)^(b*cc):
                        H=transform(7,3,mat);G=transform(33,6,mat)
                        for rr in range(16):orbit.add((H,G^pmul(rr,rr)^pmul(H,rr)))
                assert orbit==set(hh)
                result['isomorphism_classes']=1
                print('GENUS2 1+T^2+4T^4: all',len(hh),'equations lie in one explicit PGL2/y-shift orbit: PASS',flush=True)
    (HERE/'output_lowgenus.json.txt').write_text(json.dumps(dict(factors=results,elliptic=elliptic,genus2_polynomials=[list(c) for c in all2]),indent=2)+'\n')

if __name__=='__main__':main()
