#!/usr/bin/env python3
"""Exact character sums, small counterexamples, and aggregate-prime ambiguity."""
from check_ff_all import *


def quadratic(f,q,a,primes):
    val=1
    for P,e in factor(f,q,primes):
        assert e==1
        v=power(mod(a,P,q),(q**(len(P)-1)-1)//2,P,q)
        if not v: return 0
        assert v in [(1,),(q-1,)]
        val*=1 if v==(1,) else -1
    return val


def main():
    # X1 independently via the fourth-power residue symbol, no imported L data.
    q=5; f=(1,1,0,1); vals=[]
    for k in range(3):
        v=0
        for a in monics(q,k):
            z=power(a,(q**3-1)//4,f,q)
            v+=0 if not z else {1:1,2:sy.I,4:-1,3:-sy.I}[z[0]]
        vals.append(sy.expand(v))
    print('X1 exact Lambda=',vals)
    print('X1 exact alpha=',[sy.conjugate(-vals[1])/ (2*sy.sqrt(5)),-sy.conjugate(vals[2])/5])
    print('X1 exact |alpha0|^2=',sy.simplify(vals[1]*sy.conjugate(vals[1])/20))
    # Find smallest-degree repeated-root example in the exhaustive table.
    found=None
    for line in (HERE/'output_ff_all.txt').read_text().splitlines():
        if line.startswith('#') or ' | ' not in line: continue
        parts=line.split(' | ')
        if len(parts)!=6: continue
        if len(parts[4].split(','))==3 and len(parts[5].split(','))==1:
            found=parts; print('DEGREE TWO REPEATED',line); break
    assert found
    import ast
    q=int(found[0]); f=ast.literal_eval(found[1]); params=np.array(ast.literal_eval(found[2]))
    primes=[]
    for d in range(1,5):
        for P in monics(q,d):
            if not any(not mod(P,Q,q) for Q in primes if 2*(len(Q)-1)<=d): primes.append(P)
    loc=[local(q,P,e) for P,e in factor(f,q,primes)]
    orders=sum((list(l[2]) for l in loc),[]); D=lcm(*orders)
    print('REPEATED local generators/orders',[(l[0],l[1],l[2]) for l in loc])
    co=[]; Z=sy.Symbol('Z'); cycl=sy.Poly(sy.cyclotomic_poly(D,Z),Z)
    for k in range(4):
        counts=[0]*D
        for a in monics(q,k):
            coord=[]
            for m,g,oo,tab,pp in loc:
                c=tab.get(mod(a,m,q))
                if c is None: break
                coord.extend(c)
            else:
                exponent=sum(int(x)*y*(D//o) for x,y,o in zip(params,coord,orders))%D
                counts[exponent]+=1
        pol=sy.rem(sum(v*Z**j for j,v in enumerate(counts)),cycl.as_expr(),Z)
        co.append(pol)
    if found[3]=='even': co=list(it.accumulate(co))[:-1]
    print('REPEATED exact completed coefficients in Q[Z]/Phi_D; D=',D,'coeff=',[sy.expand(v) for v in co])
    print('REPEATED discriminant reduced=',sy.rem(sy.expand(co[1]**2-4*co[2]),cycl.as_expr(),Z))
    # Degree 5 quadratic characters: same root number W=1, completed degree 4.
    # Compare unweighted sums, as opposed to individual prime-character data.
    for q in [3,5]:
        primes=[]
        for d in range(1,6):
            for P in monics(q,d):
                if not any(not mod(P,Q,q) for Q in primes if 2*(len(Q)-1)<=d): primes.append(P)
        prime_seen={}; square_seen={}; pc=sc=None
        for f in monics(q,5):
            ff=factor(f,q,primes)
            if any(e>1 for P,e in ff): continue
            def chi(a):
                v=1
                for P,e in ff:
                    z=power(a,(q**(len(P)-1)-1)//2,P,q)
                    if not z: return 0
                    v*=1 if z==(1,) else -1
                return v
            S1=sum(chi(a) for a in monics(q,1)); S2=sum(chi(a) for a in monics(q,2))
            P2=sum(chi(a) for a in primes if len(a)==3)
            powers=sum(chi(a)**2 for a in monics(q,1)); SF2=S2-powers
            a0=-sy.Rational(S1,4)/sy.sqrt(q)
            a1=sy.simplify(((sy.Rational(S1*S1-2*S2,q))-4*a0*a0)/(4*(1-a0*a0)))
            row=(f,S1,S2,P2,powers,SF2,a0,a1)
            key=(S1,P2)
            if key in prime_seen and prime_seen[key][-1]!=a1 and pc is None: pc=(prime_seen[key],row)
            prime_seen[key]=row
            key=(S1,SF2)
            if key in square_seen and square_seen[key][-1]!=a1 and sc is None: sc=(square_seen[key],row)
            square_seen[key]=row
            if pc and sc: break
        print('AGGREGATE q=',q,'fields=(f,S1,S2,prime2,linear_squares,squarefree2,alpha0,alpha1)')
        print('PRIME',pc); print('SQUAREFREE',sc)
        if pc and sc: break
    assert pc and sc
    print('PASS exact X1, repeated-root discriminant, and two same-root-number ambiguity counterexamples')


if __name__=='__main__': main()
