"""Deterministic checks and evidence, row-major Kronecker convention of 02g.

All arithmetic input is a finite field, a graph, or displayed letter parameters.
No table of zeta zeros is read. No random sampling is used.
"""
from pathlib import Path
import itertools
import json
import numpy as np
import sympy as s

HERE = Path(__file__).resolve().parent
u, z = s.symbols('u z')

class Checks:
    def __init__(self, name):
        self.name, self.total, self.failed = name, 0, []
    def check(self, condition, message):
        self.total += 1
        if not bool(condition):
            self.failed.append(message)
        print(('PASS ' if condition else 'FAIL ') + message)
    def equal(self, a, b, message):
        self.check(s.simplify(a-b) == 0, message)
    def close(self, a, b, message, tol=2e-8):
        self.check(np.allclose(a, b, atol=tol, rtol=tol), message)
    def finish(self, matrices, sequences, formulas, facts=None):
        result = dict(name=self.name, checks=self.total, failed=self.failed,
                      matrices={k: [[str(s.simplify(v)) for v in row] for row in s.Matrix(m).tolist()]
                                for k,m in matrices.items()},
                      sequences={k: [str(v) for v in vs] for k,vs in sequences.items()},
                      formulas={k: str(v) for k,v in formulas.items()}, facts=facts or [])
        (HERE/'results').mkdir(exist_ok=True)
        (HERE/'results'/f'{self.name}.json').write_text(json.dumps(result, indent=2)+'\n')
        for name, m in result['matrices'].items():
            print(name)
            for row in m: print('['+', '.join(row)+']')
        for name, seq in result['sequences'].items(): print(name, seq)
        for name, f in result['formulas'].items(): print(name, '=', f)
        print(f'TALLY {self.name}: {self.total-len(self.failed)}/{self.total} PASS; {len(self.failed)} FAIL')
        if self.failed: raise AssertionError(self.failed)
        return result

def transfer(letters):
    D=letters[0].rows
    return sum((s.kronecker_product(a,s.conjugate(a)) for a in letters),s.zeros(D*D))

def norm_counts(letters, parity, nmax=6):
    E=transfer(letters); G=s.kronecker_product(parity, parity.conjugate())
    return [s.simplify(s.trace(G*E**n)) for n in range(1,nmax+1)]

def primes(counts):
    return [s.simplify(sum(s.mobius(n//d)*counts[d-1] for d in s.divisors(n))/n)
            for n in range(1,len(counts)+1)]

def ring_zeta(E, parity):
    plus=[i for i in range(E.rows) if parity[i,i]==1]
    minus=[i for i in range(E.rows) if parity[i,i]==-1]
    return s.factor((s.eye(len(minus))-u*E.extract(minus,minus)).det()/
                    (s.eye(len(plus))-u*E.extract(plus,plus)).det())

def words_norm(letters, parity, n):
    total=0
    for word in itertools.product(letters,repeat=n):
        a=s.eye(parity.rows)
        for b in word: a=b*a
        t=s.trace(parity*a)
        total += t*s.conjugate(t)
    return s.simplify(total)

def verify_tensor(c, letters, P, target, word_n=3, channel_q=None):
    E=transfer(letters); G=s.kronecker_product(P,P.conjugate())
    c.check(E*G==G*E,'transfer preserves doubled grading')
    for i,a in enumerate(letters):
        c.check(P*a*P==a or P*a*P==-a,f'letter {i} homogeneous')
    counts=norm_counts(letters,P,len(target))
    for n,(a,b) in enumerate(zip(counts,target),1):
        c.equal(a,b,f'count n={n}')
    for n in range(1,word_n+1):
        c.equal(words_norm(letters,P,n),counts[n-1],f'orthonormal word contraction n={n}')
    if channel_q is not None:
        c.check(s.simplify(sum((a.conjugate().T*a for a in letters),s.zeros(P.rows)))==channel_q*s.eye(P.rows),
                'Kraus completeness on the entire bond')
    return E,counts

def powers(a,q,nmax=6):
    v=[s.Integer(2),s.sympify(a)]
    for n in range(2,nmax+1): v.append(s.expand(a*v[-1]-q*v[-2]))
    return v[1:]

class Field:
    """Small finite fields; integer digits in ascending powers, deterministic modulus."""
    def __init__(self,p,n,modulus=None):
        self.p,self.n,self.order=p,n,p**n
        if modulus is None:
            if n==1: modulus=[0,1]
            else:
                x=s.symbols('x')
                for a in itertools.product(range(p),repeat=n):
                    if a[0] and s.Poly(x**n+sum(a[i]*x**i for i in range(n)),x,modulus=p).is_irreducible:
                        modulus=list(a)+[1]; break
        self.modulus=modulus
    def digits(self,a): return [(a//self.p**i)%self.p for i in range(self.n)]
    def encode(self,a): return sum((v%self.p)*self.p**i for i,v in enumerate(a))
    def add(self,a,b): return self.encode([x+y for x,y in zip(self.digits(a),self.digits(b))])
    def neg(self,a): return self.encode([-x for x in self.digits(a)])
    def mul(self,a,b):
        aa,bb=self.digits(a),self.digits(b); v=[0]*(2*self.n-1)
        for i,x in enumerate(aa):
            for j,y in enumerate(bb): v[i+j]+=x*y
        for i in range(len(v)-1,self.n-1,-1):
            for j in range(self.n): v[i-self.n+j]-=v[i]*self.modulus[j]
        return self.encode(v[:self.n])
    def power(self,a,n):
        v=1
        while n:
            if n&1: v=self.mul(v,a)
            a=self.mul(a,a); n//=2
        return v
    def trace(self,a):
        v=0
        for _ in range(self.n): v=self.add(v,a); a=self.power(a,self.p)
        assert v<self.p
        return v
    def primitive(self):
        for a in range(1,self.order):
            if all(self.power(a,(self.order-1)//r)!=1 for r in s.factorint(self.order-1)):
                return a

def elliptic5(n):
    F=Field(5,n); total=1
    for x in range(F.order):
        f=F.add(F.add(F.power(x,3),x),1)
        total+=1+(0 if f==0 else (1 if F.power(f,(F.order-1)//2)==1 else -1))
    return total

def elliptic_tensor(q,a,affine=False):
    """Four-letter CPTP (after /sqrt(q)) realization; a comes from a curve count."""
    pi=(a+s.I*s.sqrt(4*q-a*a))/2
    t=s.Rational(q+(0 if affine else 1),2)
    h=s.Rational(q-(0 if affine else 1),2)
    letters=[s.diag(s.sqrt(t),pi/s.sqrt(t)),s.diag(0,s.sqrt(t-q/t)),
             s.Matrix([[0,s.sqrt(h)],[0,0]]),s.Matrix([[0,0],[s.sqrt(h),0]])]
    return letters,s.diag(1,-1),pi
