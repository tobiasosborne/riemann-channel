"""REFUTE lane scratch script (claude:opus).  Written from the STATEMENTS only.

Checks T5.5 <1>4 (pure gauge on the full Cayley complex), T5.5 <1>5 (the C_4
counterexample), T5.5 <1>3 (E_{(g,gs)}=rho(s) is not flat), and T5.6 (voltage
Artin decomposition det(I-uT) = prod_rho det(I-uT_rho)^{d_rho}).  EXACT sympy.
"""
import itertools, sys
import sympy as sp

u = sp.Symbol('u')

# ---------------------------------------------------------------- groups
def cyclic(n):
    els = list(range(n))
    return els, (lambda a, b: (a+b) % n), 0, (lambda a: (-a) % n)

def sym3():
    els = list(itertools.permutations(range(3)))
    mul = lambda a, b: tuple(a[b[i]] for i in range(3))   # (a*b)(i)=a(b(i))
    e = (0,1,2)
    def inv(a):
        r=[0]*3
        for i,x in enumerate(a): r[x]=i
        return tuple(r)
    return els, mul, e, inv

def quat8():
    # units {+-1,+-i,+-j,+-k} as (sign, letter)
    els = [(s,l) for l in '1ijk' for s in (1,-1)]
    tab = {('i','j'):(1,'k'),('j','k'):(1,'i'),('k','i'):(1,'j'),
           ('j','i'):(-1,'k'),('k','j'):(-1,'i'),('i','k'):(-1,'j'),
           ('i','i'):(-1,'1'),('j','j'):(-1,'1'),('k','k'):(-1,'1')}
    def mul(a,b):
        sa,la = a; sb,lb = b; s = sa*sb
        if la=='1': return (s,lb)
        if lb=='1': return (s,la)
        s2,l = tab[(la,lb)]
        return (s*s2, l)
    e = (1,'1')
    def inv(a):
        for b in els:
            if mul(a,b)==e: return b
    return els, mul, e, inv

# ------------------------------------------------------- Cayley complex
class Cay:
    def __init__(self, els, mul, e, inv, S):
        self.els, self.mul, self.e, self.inv, self.S = els, mul, e, inv, S
        adj = {g:set() for g in els}
        for g in els:
            for s in S: adj[g].add(mul(g,s))
        for g in els:                      # symmetrise (S should be symmetric)
            for h in adj[g]: adj[h].add(g)
        self.adj = adj
        # clique complex
        F = set(frozenset([g]) for g in els)
        for g in els:
            for h in adj[g]: F.add(frozenset([g,h]))
        cur = [frozenset([g,h]) for g in els for h in adj[g] if g!=h]
        cur = set(cur)
        k = 2
        while cur:
            nxt = set()
            for c in cur:
                cand = set.intersection(*[adj[v] for v in c]) - c
                for w in cand: nxt.add(c | {w})
            F |= nxt; cur = nxt; k += 1
            if k > 6: break
        self.F = F
        self.d = max(len(f) for f in F)-1
        self.Om = {}
        for kk in range(self.d+1):
            st=[]
            for f in F:
                if len(f)==kk+1: st.extend(itertools.permutations(sorted(f,key=lambda x:els.index(x))))
            self.Om[kk]=sorted(st, key=lambda t: tuple(els.index(x) for x in t))
        self.idx={kk:{s:i for i,s in enumerate(self.Om[kk])} for kk in self.Om}
    def f(self,k): return sum(1 for x in self.F if len(x)==k+1)
    def succ(self,k,s):
        out=[]
        for w in self.els:
            if w in s: continue
            if frozenset(s[1:]+(w,)) not in self.F: continue
            if frozenset(s+(w,)) in self.F: continue
            out.append(s[1:]+(w,))
        return out
    def T(self,k):
        n=len(self.Om[k]); M=sp.zeros(n,n)
        for s in self.Om[k]:
            for t in self.succ(k,s): M[self.idx[k][t], self.idx[k][s]] += 1
        return M
    def Ttwist(self,k,E):
        """E: dict (x,y)->sympy matrix; last-vertex anchor."""
        n=len(self.Om[k]); dV = E[next(iter(E))].rows
        M=sp.zeros(n*dV,n*dV)
        for s in self.Om[k]:
            i=self.idx[k][s]
            for t in self.succ(k,s):
                j=self.idx[k][t]; W=E[(s[-1],t[-1])]
                M[j*dV:(j+1)*dV, i*dV:(i+1)*dV] += W
        return M
    def Trho(self,k,rho,dr):
        """T5.6 voltage quotient block (free left action, anchor v_0)."""
        reps=[s for s in self.Om[k] if s[0]==self.e]
        ri={s:i for i,s in enumerate(reps)}
        M=sp.zeros(len(reps)*dr, len(reps)*dr)
        for a,sa in enumerate(reps):
            for t in self.succ(k,sa):
                h=t[0]                                  # voltage
                hi=self.inv(h)
                sb=tuple(self.mul(hi,x) for x in t)     # canonical rep
                b=ri[sb]
                M[b*dr:(b+1)*dr, a*dr:(a+1)*dr] += rho(hi)
        return M

def detI(M, uu):
    n=M.rows
    if n==0: return sp.Integer(1)
    p=sp.Matrix(M).charpoly(sp.Symbol('x')); co=p.all_coeffs()
    return sp.expand(sum(c*uu**i for i,c in enumerate(co)))

# ---------------------------------------------------------------- irreps
def irreps_S3():
    els,mul,e,inv = sym3()
    def sgn(a):
        s=1
        for i in range(3):
            for j in range(i+1,3):
                if a[i]>a[j]: s=-s
        return s
    # standard 2-dim rep over Q: permutation on C^3 restricted to sum-zero
    B=sp.Matrix([[1,0],[0,1],[-1,-1]])
    Bp=(B.T*B).inv()*B.T
    def std(a):
        P=sp.zeros(3,3)
        for i in range(3): P[a[i],i]=1
        return sp.simplify(Bp*P*B)
    return [(lambda a: sp.Matrix([[1]]),1),
            (lambda a: sp.Matrix([[sgn(a)]]),1),
            (std,2)]

def irreps_Zn(n):
    w=sp.exp(2*sp.pi*sp.I/n)
    return [((lambda j: (lambda a: sp.Matrix([[sp.simplify(w**(j*a))]])))(j),1) for j in range(n)]

def irreps_Q8():
    els,mul,e,inv = quat8()
    one=sp.Matrix([[1]])
    def chi(si,sj):
        def f(a):
            s,l=a
            v={'1':1,'i':si,'j':sj,'k':si*sj}[l]
            return sp.Matrix([[v]])
        return f
    I2=sp.Matrix([[sp.I,0],[0,-sp.I]]); J2=sp.Matrix([[0,1],[-1,0]])
    K2=sp.simplify(I2*J2)
    def two(a):
        s,l=a
        M={'1':sp.eye(2),'i':I2,'j':J2,'k':K2}[l]
        return sp.simplify(s*M)
    return [(chi(1,1),1),(chi(1,-1),1),(chi(-1,1),1),(chi(-1,-1),1),(two,2)]

# ---------------------------------------------------------------- runs
def run(name, els, mul, e, inv, S, irrs):
    X=Cay(els,mul,e,inv,S)
    print(f"\n=== {name}: |G|={len(els)} f={[X.f(k) for k in range(X.d+1)]} d={X.d} "
          f"dimOm={[len(X.Om[k]) for k in range(X.d+1)]}")
    for k in range(1, X.d+1):
        if len(X.Om[k])==0: continue
        Tk=X.T(k); full=sp.expand(detI(Tk,u))
        # ---- T5.6 Artin decomposition
        prod=sp.Integer(1)
        for rho,dr in irrs:
            prod*= detI(X.Trho(k,rho,dr), u)**dr
        ok56 = sp.simplify(sp.expand(prod)-full)==0
        print(f"  k={k}: T5.6  prod_rho det(I-uT_rho)^d_rho == det(I-uT): {ok56}")
        # ---- T5.5 <1>4 pure gauge with covariant weights rho(s^{-1})
        for rho,dr in irrs:
            if dr==1: continue
            Ecov={}; Ewrong={}
            for g in els:
                for h in X.adj[g]:
                    s=mul(inv(g),h)
                    Ecov[(g,h)]=rho(inv(s)); Ewrong[(g,h)]=rho(s)
            dcov=detI(X.Ttwist(k,Ecov),u); dwr=detI(X.Ttwist(k,Ewrong),u)
            g1 = sp.simplify(sp.expand(dcov - full**dr))==0
            g2 = sp.simplify(sp.expand(dwr  - full**dr))==0
            print(f"        d_rho={dr}: covariant rho(s^-1) pure gauge: {g1};  "
                  f"chronological rho(s) also equals det^d: {g2}")
    return X

if __name__=="__main__":
    # --- T5.5 <1>5 : C_4
    els,mul,e,inv = cyclic(4)
    X=Cay(els,mul,e,inv,[1,3])
    T1=X.T(1)
    print("C_4: dim Omega_1 =",len(X.Om[1]),
          " det(I-uT_1) =", sp.factor(detI(T1,u)))
    triv=lambda a: sp.Matrix([[1]])
    print("     trivial-rep voltage block T_{1,triv} =", X.Trho(1,triv,1).tolist(),
          " det =", sp.factor(detI(X.Trho(1,triv,1),u)))
    prod=sp.Integer(1)
    for rho,dr in irreps_Zn(4): prod*=detI(X.Trho(1,rho,1),u)**dr
    print("     T5.6 product over Z/4 irreps =", sp.factor(sp.simplify(sp.expand(prod))))

    # --- S_3 with a 2-dimensional Cayley clique complex
    els,mul,e,inv = sym3()
    c=(1,2,0); c2=(2,0,1); t=(1,0,2)
    run("Cay(S_3,{c,c^2,(12)}) clique complex", els,mul,e,inv,[c,c2,t], irreps_S3())
    # --- Q_8 graph
    els,mul,e,inv = quat8()
    S=[(1,'i'),(-1,'i'),(1,'j'),(-1,'j')]
    run("Cay(Q_8,{+-i,+-j})", els,mul,e,inv,S, irreps_Q8())

# ---------------------------------------------------------------------------
# Addendum (REFUTE lane): a Cayley complex with genuinely NON-COMMUTING 2-cells,
# to separate T5.5 <1>3 (rho(s) not flat) from T5.5 <1>4 (rho(s^-1) pure gauge).
# Cay(Q_8, {+-i,+-j,+-k}); numerical (numpy) eigenvalue-multiset comparison.
# ---------------------------------------------------------------------------
def addendum():
    import numpy as np
    els,mul,e,inv = quat8()
    S=[(s,l) for l in 'ijk' for s in (1,-1)]
    X=Cay(els,mul,e,inv,S)
    print(f"\n=== ADDENDUM Cay(Q_8,{{+-i,+-j,+-k}}): f={[X.f(k) for k in range(X.d+1)]} d={X.d}")
    # non-flat count on 2-cells, chronological convention E_(g,gs)=rho(s)
    rho,dr = irreps_Q8()[-1]
    bad=0; tot=0
    for f in X.F:
        if len(f)!=3: continue
        for (a,b,c) in itertools.permutations(sorted(f,key=els.index)):
            s=mul(inv(a),b); t=mul(inv(b),c); st=mul(inv(a),c); tot+=1
            if not sp.simplify(rho(t)*rho(s)-rho(st)).is_zero_matrix: bad+=1
    print(f"   ordered 2-cells violating flatness for E=rho(s): {bad}/{tot}"
          f"  -> T5.5<1>3 confirmed: {bad>0}")
    k=1
    T1=np.array(X.T(k).tolist(),dtype=float)
    def twist(conv):
        Ed={}
        for g in els:
            for h in X.adj[g]:
                s=mul(inv(g),h)
                Ed[(g,h)]=rho(inv(s)) if conv=='cov' else rho(s)
        return np.array(X.Ttwist(k,Ed).tolist(),dtype=complex)
    ev=np.sort_complex(np.linalg.eigvals(T1))
    ev2=np.sort_complex(np.concatenate([ev,ev]))
    for conv in ('cov','chrono'):
        M=twist(conv); w=np.sort_complex(np.linalg.eigvals(M))
        d=np.max(np.abs(np.sort_complex(w)-ev2))
        print(f"   convention {conv:6s}: max |spec(T^E) - spec(T)x2| = {d:.3e} "
              f"-> det(I-uT^E)=det(I-uT)^2 : {d<1e-8}")
addendum()
