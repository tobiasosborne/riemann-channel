#!/usr/bin/env python3
"""Targeted ordinary genus-eight double covers of a genus-two curve.

Base: y^2+(x^2+x+1)y=x^5+1, the only genus-two polynomial surviving
the cube:3 cover test. Necessary branching is D=P+Q, P rational and Q
degree four. For each of the 18 such divisors on this explicit base, test
every f in L(2D), represented as (a(x)+b(x)y)/d(x)^2. Completeness of this
family for conductor <=2D follows from H^1(O(D))=0 (deg D=5>2g-2).
lowgenus.py checks that this base is the only base isomorphism class.
Counts from linear trace evaluations are checked by direct z enumeration.
"""
import itertools
import json
from collections import Counter
from census_lookup import HERE,FLUX
from lowgenus import Field,pmul

def inv(F,a):
    assert a
    return F.power(a,F.q-2)

def trace(F,a):
    v=0
    for _ in range(F.k):v^=a;a=F.mul(a,a)
    assert v in [0,1]
    return v

def taylor(F,pol,x,j):
    v=0
    for i in range(j,pol.bit_length()):
        if pol>>i&1 and (i&j)==j:v^=F.power(x,i-j)
    return v

def base_points(F):
    out=[]
    for x in range(F.q):
        h=F.ev(7,x);f=F.ev(33,x)
        out += [(x,y) for y in range(F.q) if (F.mul(y,y)^F.mul(h,y))==f]
    return out

def local_numerator(F,a,b,x,y):
    h=F.ev(7,x);hi=inv(F,h)
    y1=F.mul(F.power(x,4)^y,hi)
    y2=F.mul(F.mul(y1,y1)^y1^y,hi)
    aa=[taylor(F,a,x,j) for j in range(3)]
    bb=[taylor(F,b,x,j) for j in range(3)]
    return [aa[0]^F.mul(bb[0],y),
            aa[1]^F.mul(bb[1],y)^F.mul(bb[0],y1),
            aa[2]^F.mul(bb[2],y)^F.mul(bb[1],y1)^F.mul(bb[0],y2)]

def residue(F,a,b,d,x,y):
    n0,n1,n2=local_numerator(F,a,b,x,y)
    di=inv(F,taylor(F,d,x,1));di2=F.mul(di,di)
    c2=F.mul(n0,di2);c1=F.mul(n1,di2)
    return c1^F.power(c2,F.q//2)

def regular_at_denominator(F,a,b,d,x,y):
    n0,n1,n2=local_numerator(F,a,b,x,y)
    assert n0==n1==0
    di=inv(F,taylor(F,d,x,1))
    return F.mul(n2,F.mul(di,di))

def direct_count(F,pts,a,b,d,P):
    count=0
    for x,y in pts:
        dv=F.ev(d,x)
        if not dv:
            if residue(F,a,b,d,x,y):count+=1;continue
            value=regular_at_denominator(F,a,b,d,x,y)
        else:
            dd=F.mul(dv,dv)
            value=F.mul(F.ev(a,x)^F.mul(F.ev(b,x),y),inv(F,dd))
        count+=sum((F.mul(z,z)^z)==value for z in range(F.q))
    if P is None:count+=1
    else:
        value=(a>>10)&1
        count+=sum((F.mul(z,z)^z)==value for z in range(F.q))
    return count

def nullbasis(rows,n):
    rows=list(rows);piv=[];r=0
    for c in range(n):
        j=next((j for j in range(r,len(rows)) if rows[j]>>c&1),None)
        if j is None:continue
        rows[r],rows[j]=rows[j],rows[r]
        for j in range(len(rows)):
            if j!=r and rows[j]>>c&1:rows[j]^=rows[r]
        piv.append(c);r+=1
    out=[]
    for c in range(n):
        if c not in piv:out.append((1<<c)|sum(((rows[j]>>c)&1)<<p for j,p in enumerate(piv)))
    assert all(all((v&r).bit_count()%2==0 for r in rows) for v in out)
    return out

def minimal_x(F,x):
    roots=[];z=x
    while z not in roots:roots.append(z);z=F.mul(z,z)
    assert len(roots)==4
    c=[1]
    for r in roots:
        out=[0]*(len(c)+1)
        for j,v in enumerate(c):out[j]^=F.mul(v,r);out[j+1]^=v
        c=out
    assert all(v in [0,1] for v in c)
    return sum(v<<i for i,v in enumerate(c))

def main():
    FF={k:Field(k) for k in range(1,9)}
    pts={k:base_points(F) for k,F in FF.items()}
    F=FF[4];seen=set();places=[]
    for x,y in pts[4]:
        if (x,y) in seen:continue
        orb=[];xx,yy=x,y
        while (xx,yy) not in orb:
            orb.append((xx,yy));xx=F.mul(xx,xx);yy=F.mul(yy,yy)
        seen.update(orb)
        if len(orb)==4:places.append((x,y,minimal_x(F,x)))
    assert len(places)==6 and len(pts[1])==2
    r=next(r for r in json.loads(FLUX.read_text()) if r['graph']=='cube' and r['mask']==3)
    hits=[];logs=[]
    for P in [None]+pts[1]:
        for qx,qy,qpol in places:
            d=qpol if P is None else pmul(qpol,3)
            na,nb=(10,7) if P is None else (11,8)
            n=na+nb
            def unpack(v):return v&((1<<na)-1),v>>na
            # Vanish to order >=2 at the conjugate point above the same x.
            reject=[(F,qx,qy^F.ev(7,qx))]
            if P is not None:reject.append((FF[1],P[0],P[1]^FF[1].ev(7,P[0])))
            rows=[]
            for field,xx,yy in reject:
                vals=[local_numerator(field,*unpack(1<<i),xx,yy)[:2] for i in range(n)]
                for j in range(2):
                    for bit in range(field.k):rows.append(sum(1<<i for i,v in enumerate(vals) if v[j]>>bit&1))
            basis=nullbasis(rows,n);assert len(basis)==9
            candidates=[]
            for mask in range(1<<9):
                v=0
                for i,b in enumerate(basis):
                    if mask>>i&1:v^=b
                a,b=unpack(v)
                rp=(b>>6)&1 if P is None else residue(FF[1],a,b,d,*P)
                rq=residue(F,a,b,d,qx,qy)
                if rp and rq:candidates.append((mask,a,b))
            survivors=[len(candidates)]
            # On the chosen ramified points the cover has exactly one point.
            # For each other base point the fiber has 1+(-1)^Tr(f) points.
            for k,field in FF.items():
                rowmasks=[]
                for xx,yy in pts[k]:
                    dv=field.ev(d,xx)
                    vals=[]
                    if not dv:
                        # Decide whether this is a prescribed ramified point
                        # using one candidate (all candidates have the same D).
                        if not candidates:break
                        _,a0,b0=candidates[0]
                        if residue(field,a0,b0,d,xx,yy):continue
                    for v in basis:
                        a,b=unpack(v)
                        if dv:
                            z=field.ev(a,xx)^field.mul(field.ev(b,xx),yy)
                            z=field.mul(z,field.mul(inv(field,dv),inv(field,dv)))
                        else:z=regular_at_denominator(field,a,b,d,xx,yy)
                        vals.append(trace(field,z))
                    rowmasks.append(sum(v<<i for i,v in enumerate(vals)))
                if P is not None:
                    # Infinity is unramified and f(infinity)=a_10.
                    rowmasks.append(sum((((unpack(v)[0]>>10)&1)*(k%2))<<i for i,v in enumerate(basis)))
                baseN=len(pts[k])+1
                keep=[]
                for mask,a,b in candidates:
                    count=baseN+sum(1-2*((mask&v).bit_count()%2) for v in rowmasks)
                    assert count==direct_count(field,pts[k],a,b,d,P)
                    if count==r['N'][str(k)]:keep.append((mask,a,b))
                candidates=keep
                survivors.append(len(candidates))
                if not candidates:break
            log=dict(P=P,Q=[qx,qy],qpol=qpol,dimension=9,survivors=survivors)
            print('DIVISOR',log,flush=True);logs.append(log)
            for mask,a,b in candidates:
                hit=dict(a=a,b=b,d=d,P=P,Q=[qx,qy],base='y^2+(x^2+x+1)y=x^5+1',cover='z^2+z=(a(x)+b(x)y)/d(x)^2')
                hits.append(hit);print('WITNESS',hit,flush=True)
    print('TOTAL divisors',len(logs),'raw functions',len(logs)*512,'matches',len(hits),flush=True)
    (HERE/'output_double_covers.json.txt').write_text(json.dumps(dict(logs=logs,hits=hits),indent=2)+'\n')

if __name__=='__main__':main()
