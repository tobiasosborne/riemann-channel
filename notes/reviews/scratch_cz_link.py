"""REFUTE lane scratch script (claude:opus).  Written from the STATEMENTS only.

T0.3: the A~_2 link arithmetic.  The vertex link of a type-preserving quotient of
the PGL_3 building over F_q is the point-line incidence graph of PG(2,q); the
outdegree of the UNRESTRICTED ordered rule T0.1 at a directed edge, and of the
opposition (Kang-Li L_E) rule, are local facts about that link.  Constructed here
from PG(2,q) directly (q = 2,3,4,5), exactly.

Also T0.3 statement 5 (two cyclic-orientation blocks of T_2 with equal
determinant) tested on a 3-colourable 2-complex (the octahedron).
"""
import itertools
import sympy as sp
u=sp.Symbol('u')

def PG2(q):
    """points and lines of PG(2,q) as 1- and 2-dim subspaces of F_q^3 (q prime)."""
    V=[v for v in itertools.product(range(q),repeat=3) if any(v)]
    def norm(v):
        for c in v:
            if c: inv=pow(c,q-2,q) if q>2 else c
            else: continue
            return tuple((x*inv)%q for x in v)
    pts=sorted(set(norm(v) for v in V))
    lines=[]
    for a in pts:                     # a line = kernel of a nonzero functional
        L=frozenset(p for p in pts if sum(a[i]*p[i] for i in range(3))%q==0)
        lines.append((a,L))
    lines=sorted(set((a,L) for a,L in lines))
    return pts, lines

def check(q):
    pts,lines=PG2(q); N=q*q+q+1
    assert len(pts)==N and len(lines)==N, (len(pts),len(lines))
    # incidence graph
    P=[('P',p) for p in pts]; Lv=[('L',a) for a,_ in lines]
    Lset={('L',a):L for a,L in lines}
    def inc(x,y):
        if x[0]==y[0]: return False
        (p,l)=(x,y) if x[0]=='P' else (y,x)
        return p[1] in Lset[l]
    nodes=P+Lv
    deg=set(sum(1 for y in nodes if inc(x,y)) for x in nodes)
    # any two points on exactly one line
    uniq=all(sum(1 for l in Lv if inc(('P',a),l) and inc(('P',b),l))==1
             for a,b in itertools.combinations(pts,2))
    # T0.1 unrestricted outdegree at a directed edge (x,y):
    #   w in Lk(y), w != x, w NOT adjacent to x in Lk(y)
    x=P[0]
    same=sum(1 for w in nodes if w[0]==x[0] and w!=x)
    opp =sum(1 for w in nodes if w[0]!=x[0] and not inc(x,w))
    oppinc=sum(1 for w in nodes if w[0]!=x[0] and inc(x,w))
    print(f"  q={q}: N={N} link |V|={len(nodes)} degrees={sorted(deg)} "
          f"unique-line-thru-2-points={uniq}")
    print(f"         same part (excl. x): {same} (= N-1 = {N-1})   "
          f"opposite part non-incident: {opp} (= q^2 = {q*q})   incident: {oppinc} (= q+1)")
    print(f"         T0.1 unrestricted outdegree = {same+opp}  (claim 2q^2+q = {2*q*q+q}) "
          f"{'OK' if same+opp==2*q*q+q else '*** MISMATCH ***'}")
    print(f"         opposition (L_E) outdegree = {opp}  (claim q^2 = {q*q}) "
          f"{'OK' if opp==q*q else '*** MISMATCH ***'}")
    print(f"         of the {same+opp} unrestricted successors, {opp} keep the directed-edge "
          f"colour (= L_E) and {same} flip it -> colour classes NOT invariant: "
          f"{'confirmed' if same>0 else 'FALSE'}")

print("== T0.3 <1>1-<1>3 : link of a vertex = incidence graph of PG(2,q) (exact)")
for q in (2,3,4,5):
    if q==4: continue          # 4 is not prime; skip
    check(q)

# ---------------------------------------------------------------- T0.3 <1>4/5
print("\n== T0.3 <1>4/<1>5 : cyclic-orientation blocks of the unrestricted T_2")
print("   test bed: the octahedron (clique complex of K_{2,2,2}), which is")
print("   3-colourable with rainbow triangles, like a type-preserving A~_2 quotient.")
pairs=[(0,1),(2,3),(4,5)]; col={0:0,1:0,2:1,3:1,4:2,5:2}
tri=[t for t in itertools.combinations(range(6),3) if all(not set(p)<=set(t) for p in pairs)]
F=set()
for t in tri:
    for r in range(1,4):
        for s in itertools.combinations(t,r): F.add(frozenset(s))
Om2=sorted([p for t in tri for p in itertools.permutations(t)])
idx={s:i for i,s in enumerate(Om2)}
print(f"   |Omega_2| = {len(Om2)} = 6 f_2 with f_2 = {len(tri)}")
def inccyc(s):  # increasing cyclic colour order?
    return (col[s[1]]-col[s[0]])%3==1 and (col[s[2]]-col[s[1]])%3==1
inc=[s for s in Om2 if inccyc(s)]; dec=[s for s in Om2 if not inccyc(s)]
print(f"   increasing-orientation block: {len(inc)} states, decreasing: {len(dec)} "
      f"(claim 3 f_2 = {3*len(tri)} each) {'OK' if len(inc)==3*len(tri) else '***'}")
def succ(s):
    out=[]
    for w in range(6):
        if w in s: continue
        if frozenset(s[1:]+(w,)) not in F: continue
        if frozenset(s+(w,)) in F: continue
        out.append(s[1:]+(w,))
    return out
splits=all(all(inccyc(t)==inccyc(s) for t in succ(s)) for s in Om2)
outdeg=set(len(succ(s)) for s in Om2)
print(f"   T_2 preserves the cyclic orientation: {splits};  outdegrees {sorted(outdeg)}")
def det_block(states):
    ii={s:i for i,s in enumerate(states)}; n=len(states)
    M=sp.zeros(n,n)
    for s in states:
        for t in succ(s): M[ii[t],ii[s]]+=1
    return sp.factor(sp.expand((sp.eye(n)+u*M).det()))
dI=det_block(inc); dD=det_block(dec)
print(f"   det(I+uT_2|inc) = {dI}\n   det(I+uT_2|dec) = {dD}\n   equal: {sp.simplify(dI-dD)==0}")
print(f"   => det_{{H_2}}(I+uT_2) = (block)^2 : {sp.factor(dI*dD)}")

# ---- colour behaviour of the unrestricted T_1 on the same 3-coloured complex
Om1=sorted([p for e in F if len(e)==2 for p in itertools.permutations(sorted(e))])
def succ1(s):
    out=[]
    for w in range(6):
        if w in s: continue
        if frozenset(s[1:]+(w,)) not in F: continue
        if frozenset(s+(w,)) in F: continue
        out.append(s[1:]+(w,))
    return out
flip=0; keep=0
for s in Om1:
    c=(col[s[1]]-col[s[0]])%3
    for t in succ1(s):
        if (col[t[1]]-col[t[0]])%3==c: keep+=1
        else: flip+=1
print(f"\n   unrestricted T_1 transitions: colour-preserving {keep}, colour-flipping {flip}"
      f"  -> colour classes invariant? {flip==0}")
