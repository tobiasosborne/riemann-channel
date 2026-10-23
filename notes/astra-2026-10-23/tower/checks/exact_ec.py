"""Independent finite-field elliptic arithmetic for Lane T (python-flint).

General Weierstrass group law, Miller pairings with translated divisors,
and constructive group certificates. None of these calls PARI. Point counts
over extensions use the proved Frobenius recurrence after counting F_p.
"""
from math import isqrt
from random import Random
from flint import fq_default_ctx
from sympy import factorint

RNG = Random(20261023)


def key(P):
    return None if P is None else tuple(tuple(int(x) for x in z.to_list()) for z in P)


def cardinal(p, a, k):
    s0, s1 = 2, a
    for _ in range(2,k+1):
        s0,s1 = s1,a*s1-p*s0
    return p**k+1-(s1 if k else s0)


class Curve:
    def __init__(self,p,k,ai,trace=None):
        self.p,self.k,self.q = p,k,p**k
        self.F = fq_default_ctx(p,k,'t')
        if len(ai)==2:
            ai = [0,0,0,*ai]
        self.ai = list(ai)
        self.a1,self.a2,self.a3,self.a4,self.a6 = [self.F(x) for x in ai]
        self.trace = trace
        self.card = cardinal(p,trace,k) if trace is not None else None
        self._basis = None

    def field(self,n):
        cs=[]
        for _ in range(self.k):
            cs.append(n%self.p)
            n//=self.p
        return self.F(cs)

    def rhs(self,x):
        return x**3+self.a2*x*x+self.a4*x+self.a6

    def ys(self,x):
        b=self.a1*x+self.a3
        c=self.rhs(x)
        if self.p==2:
            if b.is_zero():
                return [c.sqrt()]
            return [y for i in range(self.q) if (y:=self.field(i))**2+b*y == c]
        disc=b*b+4*c
        if not disc.is_square():
            return []
        s=disc.sqrt()
        y=(-b+s)/2
        return [y] if s.is_zero() else [y,(-b-s)/2]

    def points(self):
        yield None
        for n in range(self.q):
            x=self.field(n)
            for y in self.ys(x):
                yield x,y

    def random(self):
        while True:
            x=self.field(RNG.randrange(self.q))
            ys=self.ys(x)
            if ys:
                return x,ys[RNG.randrange(len(ys))]

    def on(self,P):
        if P is None:
            return True
        x,y=P
        return y*y+self.a1*x*y+self.a3*y == self.rhs(x)

    def neg(self,P):
        if P is None:
            return None
        x,y=P
        return x,-y-self.a1*x-self.a3

    def slope(self,P,Q):
        x,y=P
        X,Y=Q
        if x==X:
            return (3*x*x+2*self.a2*x+self.a4-self.a1*y)/(2*y+self.a1*x+self.a3)
        return (Y-y)/(X-x)

    def add(self,P,Q):
        if P is None:
            return Q
        if Q is None:
            return P
        x,y=P
        X,Y=Q
        if x==X and Y == -y-self.a1*x-self.a3:
            return None
        lam=self.slope(P,Q)
        xx=lam*lam+self.a1*lam-self.a2-x-X
        yy=-(lam+self.a1)*xx-(y-lam*x)-self.a3
        return xx,yy

    def mul(self,n,P):
        if n<0:
            return self.mul(-n,self.neg(P))
        S=None
        while n:
            if n&1:
                S=self.add(S,P)
            P=self.add(P,P)
            n>>=1
        return S

    def frob(self,P):
        return None if P is None else tuple(z**self.p for z in P)

    def order(self,P,bound=None):
        n=self.card if bound is None else bound
        assert self.mul(n,P) is None
        for l in factorint(n):
            while n%l==0 and self.mul(n//l,P) is None:
                n//=l
        return n

    def log(self,R,P,n):
        m=isqrt(n)+1
        table={}
        S=None
        for j in range(m):
            table.setdefault(key(S),j)
            S=self.add(S,P)
        step=self.neg(self.mul(m,P))
        S=R
        for i in range(m+1):
            j=table.get(key(S))
            if j is not None and i*m+j<n:
                return i*m+j
            S=self.add(S,step)
        raise ValueError('discrete logarithm does not exist')

    def line(self,P,Q,R):
        if P is None or Q is None:
            return self.F.one()
        if R is None:
            raise ZeroDivisionError('evaluation at infinity')
        S=self.add(P,Q)
        if S is None:
            return R[0]-P[0]
        lam=self.slope(P,Q)
        return (R[1]-P[1]-lam*(R[0]-P[0]))/(R[0]-S[0])

    def miller(self,P,R,N):
        if P is None:
            return self.F.one()
        T=P
        f=self.F.one()
        for bit in bin(N)[3:]:
            f=f*f*self.line(T,T,R)
            T=self.add(T,T)
            if bit=='1':
                f=f*self.line(T,P,R)
                T=self.add(T,P)
        return f

    def weil(self,P,Q,N):
        if P is None or Q is None:
            return self.F.one()
        assert self.mul(N,P) is None and self.mul(N,Q) is None
        for _ in range(1000):
            S=self.random()
            try:
                z=(self.miller(P,self.add(Q,S),N)/self.miller(P,S,N)
                   *self.miller(Q,self.neg(S),N)/self.miller(Q,self.add(P,self.neg(S)),N))
                if not z.is_zero():
                    assert z**N == 1
                    return z
            except ZeroDivisionError:
                pass
        raise RuntimeError('no disjoint divisors for Weil evaluation')

    def tate(self,P,Q,N):
        assert (self.q-1)%N==0 and self.mul(N,P) is None
        if P is None or Q is None:
            return self.F.one()
        for _ in range(1000):
            S=self.random()
            try:
                z=self.miller(P,self.add(Q,S),N)/self.miller(P,S,N)
                if not z.is_zero():
                    z=z**((self.q-1)//N)
                    assert z**N == 1
                    return z
            except ZeroDivisionError:
                pass
        raise RuntimeError('no disjoint divisors for Tate evaluation')

    def primary_basis(self,l,exponents):
        """Certificate with a primitive Weil value on the smaller torsion.

        exponents=(e1,e2), e1>=e2; e2=0 permits a cyclic group.
        A small BSGS removes the high-order component of a second point.
        """
        e1,e2=exponents
        o1,o2=l**e1,l**e2
        co=self.card//(o1*o2)
        for _ in range(10000):
            P=self.mul(co,self.random())
            if self.order(P,o1)==o1:
                break
        else:
            raise RuntimeError('no point of predicted exponent')
        if o2==1:
            return [o1],[P]
        for _ in range(10000):
            R=self.mul(co,self.random())
            aa=self.log(self.mul(o2,R),self.mul(o2,P),o1//o2)
            Q=self.add(R,self.neg(self.mul(aa,P)))
            if self.order(Q,o2)!=o2:
                continue
            z=self.weil(self.mul(o1//o2,P),Q,o2)
            if z**(o2//l)!=1:
                return [o1,o2],[P,Q]
        raise RuntimeError('no independent second generator')

    def basis(self,invariants):
        if self._basis is not None:
            return self._basis
        os=sorted(invariants,reverse=True)
        if len(os)==1:
            os.append(1)
        assert os[0]*os[1]==self.card and os[0]%os[1]==0
        gs=[None,None]
        for l in factorint(self.card):
            es=[]
            for o in os:
                e=0
                while o%l==0:
                    o//=l
                    e+=1
                es.append(e)
            ls,ps=self.primary_basis(l,es)
            for i,P in enumerate(ps):
                gs[i]=self.add(gs[i],P)
        assert self.order(gs[0])==os[0] and self.order(gs[1])==os[1]
        if os[1]>1:
            z=self.weil(self.mul(os[0]//os[1],gs[0]),gs[1],os[1])
            assert all(z**(os[1]//l)!=1 for l in factorint(os[1]))
        self._basis=(os,gs)
        return os,gs


def dlog_mu(z,w,N):
    x=w**0
    for j in range(N):
        if x==z:
            return j
        x*=w
    raise ValueError('not in mu_N')


def root(E,N,normalise7=False):
    assert (E.q-1)%N==0
    for _ in range(1000):
        z=E.field(RNG.randrange(1,E.q))**((E.q-1)//N)
        if all(z**(N//l)!=1 for l in factorint(N)):
            if normalise7 and N in (4,8,16):
                m=8 if N==4 else N
                if N==4:
                    return root(E,8,True)**2
                for j in range(1,N,2):
                    w=z**j
                    w8=w if N==8 else w*w
                    if w8+w8**(-1)==3:
                        return w
            if normalise7 and N==3:
                return E.F(4)
            return z
    raise RuntimeError('no primitive root')


def velu_data(E,K):
    """Rational short-Weierstrass kernel points, giving the quotient."""
    assert E.ai[:3]==[0,0,0]
    A,B=E.ai[3:]
    ts=sum((3*x*x+A for x,y in K),E.F.zero())
    ws=sum((5*x*x*x+3*A*x+2*B for x,y in K),E.F.zero())
    return (int((E.F(A)-5*ts).to_list()[0]),int((E.F(B)-7*ws).to_list()[0]))


def velu_apply(E,K,P,u=1):
    if P is None or key(P) in {key(T) for T in K}:
        return None
    x,y=P
    X,Y=x,y
    for T in K:
        R=E.add(P,T)
        X+=R[0]-T[0]
        Y+=R[1]-T[1]
    return u*u*X,u*u*u*Y
