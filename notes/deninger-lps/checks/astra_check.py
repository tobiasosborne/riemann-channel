# Author: codex:gpt-6-astra
"""Independent finite checks; creates no output files or bytecode."""
import sys, re, itertools, collections
sys.dont_write_bytecode=True
import numpy as np
import sympy as sy
from scipy import sparse
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]/'scripts'))
from weil_lps import lps_quaternions, conj, weil_rep_table, split_matrices, build, parity_blocks, superop

def mul(a,b):
    w,x,y,z=a; W,X,Y,Z=b
    return (w*W-x*X-y*Y-z*Z,w*X+x*W+y*Z-z*Y,w*Y-x*Z+y*W+z*X,w*Z+x*Y-y*X+z*W)
def canon(a):
    for v in a:
        if v: return tuple(x if v>0 else -x for x in a)
def mc(a):
    for v in a:
        if v%5: return tuple((x*pow(v%5,-1,5))%5 for x in a)
def mm(a,b):
    A,B,C,D=a; E,F,G,H=b
    return mc((A*E+B*G,A*F+B*H,C*E+D*G,C*F+D*H))
def phi(a):
    w,x,y,z=a
    return mc((w+2*x,y+2*z,-y+2*z,w-2*x))
H=lps_quaternions(13); V=lps_quaternions(17)
G=sorted({mc(a) for a in itertools.product(range(5),repeat=4) if (a[0]*a[3]-a[1]*a[2])%5})
idx={g:i for i,g in enumerate(G)}; n=len(G)
step=lambda Q:np.array([[idx[mm(g,phi(a))] for a in Q] for g in G])
h,v=step(H),step(V)
for st in (h,v):
    seen={0}; todo=[0]
    for g in todo:
        for t in st[g]:
            if t not in seen:seen.add(t);todo.append(t)
    assert len(seen)==120
revh=np.array([H.index(conj(a)) for a in H])
revv=np.array([V.index(conj(a)) for a in V])
def edge_index(st,rev):
    ids={}; lookup={}
    for g in range(n):
        for a in range(len(rev)):
            pair=(g,a); back=(int(st[g,a]),int(rev[a])); key=min(pair,back)
            if key not in ids:ids[key]=len(ids)
            lookup[pair]=(ids[key],1 if pair==key else -1)
    return ids,lookup
he,hl=edge_index(h,revh); ve,vl=edge_index(v,revv)
right={canon(mul(b,a)):(j,i) for j,b in enumerate(V) for i,a in enumerate(H)}
assert len(right)==252
rules={(i,j):right[canon(mul(a,b))] for i,a in enumerate(H) for j,b in enumerate(V)}
T=np.zeros((840,840),dtype=np.int64); D=np.zeros((840,120),dtype=np.int64)
for (g,a),e in he.items():
    D[e,g]=-1;D[e,h[g,a]]=1
    for b in range(18):
        bp,ap=rules[a,b]; f,s=hl[int(v[g,bp]),ap];T[e,f]+=s
A=np.zeros((120,120),dtype=np.int64)
for g in range(120):
    for t in v[g]:A[g,t]+=1
assert np.array_equal(T,T.T) and np.array_equal(T@D,D@A)
# Directed transport, reversal, and sign multiplication.
rr=[];cc=[]
for g in range(120):
    for a in range(14):
        for b in range(18):
            bp,ap=rules[a,b];rr.append(g*14+a);cc.append(int(v[g,bp])*14+ap)
Td=sparse.csr_matrix((np.ones(len(rr),dtype=np.int64),(rr,cc)),shape=(1680,1680))
r=np.array([int(h[g,a])*14+int(revh[a]) for g in range(120) for a in range(14)])
R=sparse.csr_matrix((np.ones(1680,dtype=np.int64),(np.arange(1680),r)),shape=(1680,1680))
eps=np.array([1 if (g[0]*g[3]-g[1]*g[2])%5 in (1,4) else -1 for g in G])
S=sparse.diags(np.repeat(eps,14),dtype=np.int64)
assert (R@Td-Td@R).nnz==0 and (S@Td+Td@S).nnz==0 and (S@R+R@S).nnz==0
# Exact polynomial assertions from the printed factorization.
x=sy.symbols('x')
rows=Path('notes/deninger-lps/src/lps-deninger-worked-example.md').read_text().split('**13.')[1]
factors=[]
for f,m in re.findall(r'\| \\\((.*?)\\\) \| (\d+) \|',rows):
    f=sy.sympify(re.sub(r'(\d)x',r'\1*x',f).replace('^','**'));m=int(m);factors.append((sy.Poly(f,x),m))
assert len(factors)==25
assert sum(f.degree()*m for f,m in factors)==721
assert all(f.count_roots(-8,8)==f.degree() for f,m in factors)
tr=sum(-f.nth(f.degree()-1)*m for f,m in factors)
assert tr==18
print('Exact: vertices 120; connected colours; edges',len(he),len(ve),'; rules 252')
print('Exact: T symmetric, T D = D A17; directed [T,R]=0, {T,S}=0, {R,S}=0')
print('Section 13: degree 721; trace',tr,'; all roots strictly in (-8,8) by rational root counts')
lin=[(-f.nth(0),m) for f,m in factors if f.degree()==1]
print('Linear factors (eigenvalue,multiplicity):',lin,'; linear dimension',sum(m for _,m in lin))
print('Dimension of real metric cone:',sum(f.degree()*m*m for f,m in factors))
# Unnormalized T17^2 convention: sphere radius 2 is degree 306, full Hecke T289 degree307.
Q2=lps_quaternions(289)
right2={canon(mul(b,a)):(j,i) for j,b in enumerate(Q2) for i,a in enumerate(H)}
assert len(Q2)==307 and len(right2)==14*307
v2=step(Q2);T2=np.zeros_like(T)
for (g,a),e in he.items():
    for b,c in enumerate(Q2):
        bp,ap=right2[canon(mul(H[a],c))];f,s=hl[int(v2[g,bp]),ap];T2[e,f]+=s
assert np.array_equal(T@T-17*np.eye(840,dtype=np.int64),T2)
print('Exact: norm-289 transport equals T1^2 - 17 I (including scalar quaternion 17)')
# Finite elliptic-curve trace examples only, not identification of global newforms.
for wanted in [-7,7]:
    done=False
    for a,b in itertools.product(range(17),repeat=2):
        if (4*a**3+27*b*b)%17==0:continue
        points=1+sum(sum((y*y-t*t*t-a*t-b)%17==0 for y in range(17)) for t in range(17))
        if 18-points==wanted:
            print('F17 curve y^2=x^3+%d*x+%d:'%(a,b),'points',points,'trace',wanted);done=True;break
    assert done
if '--weil' in sys.argv:
    table,X,Z=weil_rep_table(13);I,J=split_matrices(13)
    Q,gens,Ws,err=build(13,17,table,X,Z,I,J);B=parity_blocks(13)[1]
    E=superop([B.T@W@B for W in Ws])*18
    w=np.linalg.eigvalsh((E+E.conj().T)/2)
    print('Weil odd adjacency spectrum:',collections.Counter(np.round(w,8)))
    roots=np.concatenate([np.array([float(sy.re(t)) for t in sy.nroots(f.as_expr(),maxsteps=100)]) for f,m in factors])
    nontriv=w[w<17]
    print('Max distance of Weil nontrivial eigenvalues to worked-example roots:',max(min(abs(roots-t)) for t in nontriv))
if '--weil-exact' in sys.argv:
    from weil_lps import psl2_elements, psl2_canon, quat_to_gl2, sqrt_mod, inv_mod, mat_mod
    els=psl2_elements(13); ei={g:i for i,g in enumerate(els)};ident=ei[(1,0,0,1)]
    I,J=split_matrices(13);scale=inv_mod(sqrt_mod(17,13),13)
    gens=[mat_mod(scale*quat_to_gl2(a,13,I,J),13) for a in lps_quaternions(17)]
    dest=[[ei[psl2_canon(mat_mod(np.array(g).reshape(2,2)@s,13),13)] for s in gens] for g in els]
    def leg(a):
        t=pow(int(a)%13,6,13);return 0 if t==0 else (1 if t==1 else -1)
    # 2*chi_End(W_odd) = A + B*sqrt(13). Follows from the quadratic Gauss sum.
    def character(g):
        a,b,c,d=g;tr=(a+d)%13
        if b==c==0 and a==d:return (72,0)
        if tr in (2,11):return (7,leg(b if b else c))
        # regular split elements: 0; regular nonsplit elements: 1.
        return (0,0) if leg(tr*tr-4)==1 else (2,0)
    ch=[character(g) for g in els]
    counts=[0]*1092;counts[ident]=1;mom=[36]
    for k in range(1,37):
        nxt=[0]*1092
        for i,c in enumerate(counts):
            for j in dest[i]:nxt[j]+=c
        counts=nxt
        a=sum(c*h[0] for c,h in zip(counts,ch));b=sum(c*h[1] for c,h in zip(counts,ch))
        assert b==0 and a%2==0;mom.append(a//2)
    coeff=[sy.Integer(1)]
    for k in range(1,37):coeff.append(-sum(coeff[k-j]*mom[j] for j in range(1,k+1))/k)
    cp=sy.Poly.from_list(coeff,x)
    expected=(x-18)*(x-3)**8*(x+5)**6*(x+3)**3*(x**4-34*x*x+97)**3*(x*x-3*x-2)**3
    assert cp==sy.Poly(expected,x)
    print('Exact Weil odd characteristic polynomial:',sy.factor(cp.as_expr()))
    ft=sy.prod(f.as_expr()**m for f,m in factors)
    print('gcd with worked-example characteristic polynomial:',sy.factor(sy.gcd(cp.as_expr(),ft)))
if '--rank' in sys.argv:
    # Canonicalize signed square boundaries, then rank their Gram matrix mod101.
    faces=set()
    for g in range(120):
        for a in range(14):
            for b in range(18):
                bp,ap=rules[a,b]
                terms=[hl[g,a],(vl[int(h[g,a]),b][0]+840,vl[int(h[g,a]),b][1]),(hl[int(v[g,bp]),ap][0],-hl[int(v[g,bp]),ap][1]),(vl[g,bp][0]+840,-vl[g,bp][1])]
                terms=sorted(terms)
                if terms[0][1]<0:terms=[(i,-s) for i,s in terms]
                faces.add(tuple(terms))
    assert len(faces)==7560
    rr=[];cc=[];vv=[]
    for j,f in enumerate(sorted(faces)):
        for i,s in f:rr.append(i);cc.append(j);vv.append(s)
    bd=sparse.csr_matrix((np.array(vv,dtype=np.int16),(rr,cc)),shape=(1920,7560))
    lap=(bd@bd.T).toarray()%101
    k=0
    for col in range(1920):
        candidates=np.flatnonzero(lap[k:,col])
        if not len(candidates):continue
        pivot=k+int(candidates[0]);lap[[k,pivot]]=lap[[pivot,k]]
        lap[k,col:]=(lap[k,col:]*pow(int(lap[k,col]),-1,101))%101
        rows=np.flatnonzero(lap[k+1:,col])+k+1
        if len(rows):lap[rows,col:] = (lap[rows,col:] - lap[rows,col,None]*lap[k,None,col:])%101
        k+=1
    assert k==1801
    print('Exact: 7560 squares; rank(B2 B2^t mod101)=1801, hence rank(B2)=1801 and Betti=(1,0,5759)',flush=True)
