#!/usr/bin/env python3
"""Reconstruct the primitive L-polynomial of nu*(./u)_6 via Gauss sums/FE.
All arithmetic exact. No root locations, RH, or numeric complex arithmetic.
Rows through degree 5 are primitive in our cubic-nu family. The q=7 extension
through degree 7 also restores the omitted Euler factors at sixth powers.
"""
from shortrow_exact import *
from flint import nmod_poly
import sympy as sp
from functools import lru_cache

@njit(cache=True)
def pmul(a,b):
    return np.array([a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]+a[1]*b[1]],np.int64)
@njit(cache=True)
def pconj(a):return np.array([a[0]+a[1],-a[1]],np.int64)

def poly_array(p):
    a=np.zeros(W,np.int64)
    for i,c in enumerate(p):a[i]=int(c)
    return a

class GaussBase:
    def __init__(self,q,ex):
        self.q=q;self.x=sp.Symbol('x');x=self.x
        self.mod=sp.Poly(sp.cyclotomic_poly(6*q,x),x,domain=sp.ZZ)
        self.T={}
        for j in range(1,6):
            self.T[j]=sp.Poly.from_dict({(e,):sum(1 for c in range(1,q) if (q*j*int(ex[c])+6*c)%(6*q)==e) for e in range(6*q)},x,domain=sp.ZZ).rem(self.mod)
        self.z=sp.Poly(x**q,x,domain=sp.ZZ).rem(self.mod)
    @lru_cache(None)
    def topbase(self,counts):
        q=self.q;x=self.x;J=sum(j*counts[j-1] for j in range(1,6))%6
        P=sp.Poly(1,x,domain=sp.ZZ)
        for j in range(1,6):
            for _ in range(counts[j-1]):P=(P*self.T[j]).rem(self.mod)
        if J:
            # 1/T_J = conjugate(T_J)/q; conjugate in Q(zeta_(6q)).
            T=self.T[J]
            C=sp.Poly.from_dict({((-int(k[0]))%(6*q),):int(v) for k,v in T.as_dict().items()},x,domain=sp.ZZ).rem(self.mod)
            P=(P*C).rem(self.mod)
        # In both parity cases divide by q. Even case G/q; odd case G/T_J.
        dic=P.as_dict();zd=self.z.as_dict()
        kk=next(k for k,v in zd.items() if k!=(0,) and v)
        b=sp.Rational(dic.get(kk,0),q*zd[kk]);a=sp.Rational(dic.get((0,),0),q)-b*zd.get((0,),0)
        assert P==sp.Poly(q*a,x,domain=sp.ZZ)+self.z*int(q*b),(counts,J,P,a,b)
        assert a.q==b.q==1,(counts,a,b)
        return np.array([int(a),int(b)],np.int64)


def row_metadata(F,h):
    q=F.q;base=GaussBase(q,F.ex);fp=nmod_poly(list(map(int,F.f[:4])),q)
    N=np.zeros(q**h,np.int64);top=np.zeros((q**h,2),np.int64)
    reduced=np.zeros((q**h,W),np.int64);rdegree=np.zeros(q**h,np.int64)
    masks=np.zeros((q**h,2),np.int64);maskdegree=np.zeros(q**h,np.int64)
    even=(h+9)%6==0
    for iu in range(q**h):
        u=decode(iu,q,h);p=nmod_poly(list(map(int,u[:h+1])),q)
        fac=[(a,int(e)%6) for a,e in p.factor()[1]] if h else []
        hasf=False;out=[];excluded=[];red=nmod_poly([1],q)
        for a,j in fac:
            if j:red*=a**j
            if a==fp:j=(j+3)%6;hasf=True
            if j:out.append((a,j))
            else:excluded.append(a)
        if not hasf:out.append((fp,3))
        reduced[iu]=poly_array(red);rdegree[iu]=red.degree()
        # Up to h=7 the only omitted factors are a single linear prime to exponent six.
        assert len(excluded)<=1 and all(a.degree()==1 for a in excluded)
        if excluded:
            a=excluded[0];r=int(red.resultant(a));v=int(F.eta[int(fp.resultant(a))])
            masks[iu]=v*PAIR[F.ex[r]];maskdegree[iu]=1
        counts=[0]*5;phase=0;M=sum(a.degree() for a,j in out)
        phase=3*((M-len(out))%2)
        for a,j in out:
            da=a.degree();counts[j-1]+=da
            R=int(a.resultant(a.derivative()))
            phase+=j*int(F.ex[R])
        for i,(a,j) in enumerate(out):
            for b,k in out[i+1:]:
                phase+=j*int(F.ex[int(a.resultant(b))])+k*int(F.ex[int(b.resultant(a))])
        t=pmul(base.topbase(tuple(counts)),PAIR[phase%6])
        N[iu]=M-1-int(even);top[iu]=t
        assert int(t[0])**2+int(t[0])*int(t[1])+int(t[1])**2==q**int(N[iu])
    return N,top,even,reduced,rdegree,masks,maskdegree

@njit(cache=True,parallel=True)
def reconstruct_degree(q,h,Dmax,N,top,even,reduced,rdegree,masks,maskdegree,flatns,flatnu,offset,inv,ex):
    norms=np.zeros((len(N),Dmax+1),np.int64)
    inverse=np.zeros((len(N),Dmax+1,2),np.int64)
    raw_polys=np.zeros((len(N),h+3,2),np.int64)
    errors=np.zeros(len(N),np.int64)
    for iu in prange(len(N)):
        u=reduced[iu];uh=rdegree[iu];n=N[iu]
        low=np.zeros((n+1,2),np.int64);low[0,0]=1
        rawlow=np.zeros((n//2+1,2),np.int64);rawlow[0,0]=1
        for j in range(1,n//2+1):
            a=0;b=0
            for ix in range(offset[j],offset[j+1]):
                if not flatnu[ix]:continue
                r=resultant(u,uh,flatns[ix],j,q,inv)
                if r:
                    e=ex[r];a+=flatnu[ix]*PAIR[e,0];b+=flatnu[ix]*PAIR[e,1]
            rawlow[j,0]=a;rawlow[j,1]=b
            low[j]=rawlow[j]+low[j-1] if even else rawlow[j]
        for j in range((n-1)//2+1):
            x=pmul(top[iu],pconj(low[j]));den=q**j
            if x[0]%den!=0 or x[1]%den!=0:errors[iu]+=1
            low[n-j]=x//den
        if n%2==0:
            x=pmul(top[iu],pconj(low[n//2]));den=q**(n//2)
            if not np.all(x==den*low[n//2]):errors[iu]+=1
        raw=np.zeros((n+1+int(even)+maskdegree[iu],2),np.int64)
        for j in range(n+1):
            raw[j]+=low[j]
            if even:raw[j+1]-=low[j]
        if maskdegree[iu]:
            for j in range(len(raw)-2,-1,-1):raw[j+1]-=pmul(masks[iu],raw[j])
        raw_polys[iu,:len(raw)]=raw
        inverse[iu,0,0]=1;norms[iu,0]=1
        for D in range(1,Dmax+1):
            value=np.zeros(2,np.int64)
            for j in range(1,min(D,len(raw)-1)+1):value-=pmul(raw[j],inverse[iu,D-j])
            inverse[iu,D]=value
            a=value[0];b=value[1];norms[iu,D]=a*a+a*b+b*b
    return norms,inverse,raw_polys,errors


def run(q,Dmax,hmax,audit=False):
    assert q in (7,13) and 1<=Dmax<=8 and 0<=hmax<=(7 if q==7 else 5), 'proven int64 and local-mask implementation range'
    F=Field(q,max(3,Dmax if audit else (hmax+2)//2))
    totals=[0]*(Dmax+1);cells={};t=time.monotonic()
    for h in range(hmax+1):
        N,top,even,reduced,rdegree,masks,maskdegree=row_metadata(F,h)
        norms,iv,polys,errors=reconstruct_degree(q,h,Dmax,N,top,even,reduced,rdegree,masks,maskdegree,F.flatns,F.flatnu,F.offset,F.inv,F.ex)
        assert not np.any(errors), (q,h,'functional equation divisibility/central coefficient error')
        for D in range(1,Dmax+1):
            totals[D]+=(q-1)*sum(map(int,norms[:,D]));cells[f'{D},{h}']=totals[D]
            print(f'RECON q={q} D={D} h={h} S={totals[D]}',flush=True)
            if audit:
                dv=direct_degree(q,D,h,F.ns[D],F.mu[D],F.nu[D],F.inv,F.ex)
                assert np.array_equal(norms[:,D],dv),(q,D,h)
                for iu in range(q**h):
                    value=direct_value(q,D,decode(iu,q,h),h,F.ns[D],F.mu[D],F.nu[D],F.inv,F.ex)
                    sign=int(F.eta[q-1])**(h*D)  # kappa(-1)=eta(-1) for q=7,13
                    assert np.array_equal(value,sign*iv[iu,D]),(q,D,h,iu,value,iv[iu,D])
        # Independent full-L enumeration on selected rows, including repeated factors.
        for iu in sorted(set([0,min(1,q**h-1),q**h//2,q**h-1])):
            p=polys[iu];u=decode(iu,q,h)
            for j in range(len(p)):
                # Avoid expensive full L checks beyond degree 4; FE identity audited elsewhere.
                if j>4:break
                val=np.zeros(2,np.int64)
                for ix in range(q**j):
                    n=decode(ix,q,j);r=int(resultant(u,h,n,j,q,F.inv));nu=int(F.eta[resultant(F.f,3,n,j,q,F.inv)])
                    if r:val+=nu*PAIR[F.ex[r]]
                assert np.array_equal(val,p[j]),(q,h,iu,j,val,p[j])
        print(f'RECON_STAGE q={q} h={h} rows={q**h} parity_even={even} omitted_Euler_rows={np.count_nonzero(maskdegree)} metadata_and_FE_and_samples=PASS elapsed={time.monotonic()-t:.3f}',flush=True)
    suffix='_audit' if audit else ''
    (HERE/f'cells_{q}_reconstruct{suffix}.json').write_text(json.dumps(cells,indent=2)+'\n')
    if not audit:(HERE/f'cells_{q}_reconstruct_D{Dmax}_h{hmax}.json').write_text(json.dumps(cells,indent=2)+'\n')
    print('RECONSTRUCTION PASS',q,'seconds',time.monotonic()-t,flush=True)
    return cells

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--audit',action='store_true');ap.add_argument('--run',nargs=3,type=int);args=ap.parse_args()
    if args.audit:
        run(7,3,3,True);run(13,3,2,True)
    elif args.run:run(*args.run)
    else:run(7,6,5);run(13,5,4)
