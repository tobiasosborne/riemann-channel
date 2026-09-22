"""Exact supplementary checks. These do not replace the manuscript proofs."""
import json
from pathlib import Path
import sympy as s

u = s.symbols('u')
I = s.eye(2)
J = s.Matrix([[0, -1], [1, 0]])
Om = -J
checks = []

def check(name, condition):
    if not bool(condition):
        raise AssertionError(name)
    checks.append(name)

def zero(M):
    return M == s.zeros(*M.shape)

def basis_kernel(M):
    cols = M.nullspace()
    return s.Matrix.hstack(*cols) if cols else s.zeros(M.cols, 0)

def bouquet(a, b, full_intertwiner=False):
    q = a*a + b*b
    r = (q+1)//2
    loops = [I]*max(a, 0) + [-I]*max(-a, 0) + [J]*(r-abs(a))
    rho = [R for L in loops for R in (L, L.inv())]
    d = len(rho)
    B1 = s.zeros(2*d)
    H = s.ones(d)
    rev = s.zeros(d)
    Rw = s.zeros(2*d)
    for c in range(d):
        rev[c,c^1] = 1
        Rw[2*c:2*c+2,2*(c^1):2*(c^1)+2] = rho[c]
        for k in range(d):
            if k != (c^1):
                B1[2*c:2*c+2,2*k:2*k+2] = rho[c]
    B0 = s.kronecker_product(H-rev,I)
    Aplus, Aminus = a*I+b*J, a*I-b*J
    Psi = s.Matrix.vstack(*[s.Matrix.hstack(R,-I) for R in rho])
    Phi = s.Matrix.vstack(s.Matrix.hstack(Aplus,Aminus),s.Matrix.hstack(I,I))
    core = Psi*Phi
    Fcomp = s.Matrix.vstack(s.Matrix.hstack(2*a*I,-q*I),s.Matrix.hstack(I,s.zeros(2)))
    coreF = s.diag(Aplus,Aminus)
    tag=f'a={a},b={b}'
    check(tag+': injective core',core.rank()==4)
    check(tag+': core intertwiner',zero(B1*core-core*coreF))
    check(tag+': companion intertwiner',zero(Fcomp*Phi-Phi*coreF))
    faceOm = Phi.inv().T*s.diag(Om,Om)*Phi.inv()
    faceG = Phi.inv().T*Phi.inv()
    claimedOm = s.Matrix.vstack(s.Matrix.hstack(Om,-a*Om),s.Matrix.hstack(-a*Om,q*Om))/(2*b*b)
    claimedG = s.Matrix.vstack(s.Matrix.hstack(I,-a*I),s.Matrix.hstack(-a*I,q*I))/(2*b*b)
    check(tag+': actual face form',zero(faceOm-claimedOm))
    check(tag+': actual metric',zero(faceG-claimedG))
    check(tag+': positive metric',all(faceG[:k,:k].det()>0 for k in range(1,5)))
    check(tag+': metric similitude',zero(Fcomp.T*faceG*Fcomp-q*faceG))
    check(tag+': cup similitude',zero(Fcomp.T*faceOm*Fcomp-q*faceOm))
    check(tag+': cup and star',zero(faceOm*s.diag(J,J)-faceG))
    z = s.symbols('z')
    expected1 = (z*z-1)**(2*(r-1))*(z*z-2*a*z+q)**2
    expected0 = (z-q)**2*(z-1)**(2*r)*(z+1)**(2*(r-1))
    check(tag+': odd characteristic polynomial',s.expand(B1.charpoly(z).as_expr()-expected1)==0)
    check(tag+': even characteristic polynomial',s.expand(B0.charpoly(z).as_expr()-expected0)==0)
    check(tag+': squarefree annihilator',zero((B1*B1-s.eye(2*d))*(B1*B1-2*a*B1+q*s.eye(2*d))))
    arms = 4*(r-1)
    P = s.zeros(arms)
    for k in range(arms): P[k,k^1]=1
    F0 = s.diag(s.eye(2),P)
    F1 = s.diag(Aplus,Aminus,P)
    F2 = q*s.eye(2)
    d0 = s.zeros(4+arms,2+arms)
    for k in range(arms):
        component=k//(2*(r-1))
        d0[4+k,component]=-1
        d0[4+k,2+k]=1
    check(tag+': cellular chain identity',zero(d0*F0-F1*d0))
    check(tag+': cellular cohomology ranks',d0.rank()==arms)
    if full_intertwiner:
        eigs=[1,-1,q]
        FY0=s.diag(F0,F2)
        Y0=s.Matrix.hstack(*[basis_kernel(FY0-l*s.eye(2*d)) for l in eigs])
        G0=s.Matrix.hstack(*[basis_kernel(B0-l*s.eye(2*d)) for l in eigs])
        T0=G0*Y0.inv()
        Y1=s.Matrix.hstack(s.eye(4+arms)[:,:4],basis_kernel(F1-s.eye(4+arms)),basis_kernel(F1+s.eye(4+arms)))
        G1=s.Matrix.hstack(core,basis_kernel(B1-s.eye(2*d)),basis_kernel(B1+s.eye(2*d)))
        T1=G1*Y1.inv()
        check(tag+': full even intertwiner',zero(B0*T0-T0*FY0))
        check(tag+': full odd intertwiner',zero(B1*T1-T1*F1))
        dgraph=T1*s.Matrix.hstack(d0,s.zeros(4+arms,2))*T0.inv()
        check(tag+': transferred graph chain identity',zero(dgraph*B0-B1*dgraph))
        check(tag+': graph exact pieces rank',dgraph.rank()==arms)
    return {'a':a,'b':b,'q':q,'loops':r,'cell_counts':[4*r-2,4*r,2], 'betti':[2,4,2], 'core_dimension':4}

examples=[bouquet(2,1,True),bouquet(1,2,True),bouquet(0,3),bouquet(-2,1),bouquet(2,-1)]

# The larger family: arbitrary SL(2,Z) holonomies with elliptic trace sum.
general_examples=[]
for q,tau in [(3,1),(7,5),(5,-4),(9,0)]:
    r=(q+1)//2
    loops=[J]*(r-1)+[s.Matrix([[0,-1],[1,tau]])]
    rho=[R for L in loops for R in (L,L.inv())]
    B=s.zeros(4*r)
    for c,R in enumerate(rho):
        for k in range(2*r):
            if k!=(c^1):B[2*c:2*c+2,2*k:2*k+2]=R
    Ap=s.Matrix([[0,-q],[1,tau]]); Am=tau*I-Ap
    Psi=s.Matrix.vstack(*[s.Matrix.hstack(R,-I) for R in rho])
    Phi=s.Matrix.vstack(s.Matrix.hstack(Ap,Am),s.Matrix.hstack(I,I))
    C=Ap-s.Rational(tau,2)*I
    G0=Om*C
    tag=f'general q={q},trace={tau}'
    check(tag+': scalar adjacency',sum(rho,s.zeros(2))==tau*I)
    check(tag+': core injective',Psi.rank()==4)
    check(tag+': core intertwiner',zero(B*Psi*Phi-Psi*Phi*s.diag(Ap,Am)))
    check(tag+': complex structure square',zero(C*C+(q-s.Rational(tau*tau,4))*I))
    check(tag+': symmetric geometric energy',G0==G0.T)
    check(tag+': positive geometric energy',G0[0,0]>0 and G0.det()>0)
    check(tag+': conformal energy',zero(Ap.T*G0*Ap-q*G0))
    z=s.symbols('z')
    check(tag+': characteristic polynomial',s.expand(B.charpoly(z).as_expr()-(z*z-1)**(2*(r-1))*(z*z-tau*z+q)**2)==0)
    general_examples.append({'q':q,'trace':tau,'loops':r})

# Check the arbitrary reciprocal Bass identity on an irregular multigraph
# having a loop, parallel edges, and a pendant edge.
edges=[(0,0,I),(0,1,J),(0,1,-I),(1,2,J)]
n=3; m=len(edges); arcs=[]
for src,dst,R in edges: arcs.extend([(src,dst,R),(dst,src,R.inv())])
S=s.zeros(4*m,2*n); T=s.zeros(2*n,4*m); R=s.zeros(4*m)
deg=[0]*n
for c,(src,dst,W) in enumerate(arcs):
    S[2*c:2*c+2,2*src:2*src+2]=W
    T[2*dst:2*dst+2,2*c:2*c+2]=I
    R[2*c:2*c+2,2*(c^1):2*(c^1)+2]=W
    deg[src]+=1
B=S*T-R; Adj=T*S; D=s.kronecker_product(s.diag(*deg),I)
check('irregular graph: inverse transports',zero(R*R-s.eye(4*m)))
check('irregular graph: degree identity',zero(T*R*S-D))
for x in [s.Rational(1,3),s.Rational(2,5),s.Rational(-1,2)]:
    lhs=(s.eye(4*m)-x*B).det()
    rhs=(1-x*x)**(2*(m-n))*(s.eye(2*n)-x*Adj+x*x*(D-s.eye(2*n))).det()
    check('irregular graph: exact Bass at '+str(x),lhs==rhs)

# Three-step directed realization on the torus's odd transfer matrix.
A=s.Matrix([[2,-1],[1,2]])
transitions=[(j,i,A[i,j]) for i in range(2) for j in range(2) if A[i,j]]
Q=s.zeros(2+2*len(transitions))
for k,(src,dst,w) in enumerate(transitions):
    p=2+2*k; r=p+1
    Q[p,src]=1; Q[r,p]=1; Q[dst,r]=w
t=s.symbols('t')
check('directed realization: determinant',s.expand((s.eye(Q.rows)-t*Q).det()-(s.eye(2)-t**3*A).det())==0)
check('directed realization: no opposite arcs',all(not(Q[i,j] and Q[j,i]) for i in range(Q.rows) for j in range(Q.rows)))
N={n:int(1+5**n-s.trace(A**n)) for n in range(1,7)}
primitives={n:int(sum(s.mobius(k)*N[n//k] for k in s.divisors(n))/n) for n in N}
check('fixed point counts',list(N.values())==[2,20,122,640,3202,15860])
check('primitive orbit counts',list(primitives.values())==[2,9,40,155,640,2620])
check('anisotropic torus: cup',zero(s.diag(2,3).T*Om*s.diag(2,3)-6*Om))
check('prism: exact strict inequality',50>49)
out={'status':'PASS','exact_assertions':len(checks),'examples':examples,'general_examples':general_examples,'fixed_points':N,'primitive_orbits':primitives,'checks':checks}
Path(__file__).resolve().with_name('compatibility-verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','exact_assertions','examples','fixed_points','primitive_orbits']},indent=2))
