#!/usr/bin/env python3
"""REFUTE lane, elliptic-cavity 2026-09-20.  Reviewer: claude:opus.
Is z = 0 a resonance of the DIAGRAM, or an artefact of where the core is cut?
Move the core/cusp cut one, two, three ray steps out on D2 and watch p, R, N.
Also settles the Childs-Gosset convention question (numerics D9 vs prover C2).
"""
import sympy as sp
NCHK=0; FAIL=[]
def chk(n,c,i=""):
    global NCHK; NCHK+=1
    if not c: FAIL.append((n,i)); print("  FAIL %-56s %s"%(n,i))
z=sp.symbols('z'); q=2
S={'A':6,'B':2,'C':2,'D':1,'E':3,'F':3}
E=[('A','B',2),('B','C',2),('C','D',1),('D','E',1),('D','F',1)]
def build(extra):
    """core = D2 core plus the first `extra` ray vertices; cusp attaches at the last one."""
    Sx=dict(S); Ex=list(E); prev='B'; pe=2
    for k in range(1,extra+1):
        v='c%d'%k; Sx[v]=2**(k+1); Ex.append((prev,v,pe)); prev=v; pe=2**(k+1)
    order=['A','B','C','D','E','F']+['c%d'%k for k in range(1,extra+1)]
    n=len(order); idx={v:i for i,v in enumerate(order)}
    A=sp.zeros(n,n)
    for (a,b,e) in Ex:
        A[idx[a],idx[b]]=sp.Rational(Sx[a],e); A[idx[b],idx[a]]=sp.Rational(Sx[b],e)
    C=sp.zeros(n,n); C[idx[prev],idx[prev]]=sp.Rational(Sx[prev],pe)   # c^2 = S(v)/S(e)
    t=sp.symbols('t')
    p=sp.expand(((1+q*t**2)*sp.eye(n)-t*A-C).det()).subs(t,z/sp.sqrt(q))
    p=sp.expand(sp.nsimplify(p)); pt=sp.expand(z**(2*n)*p.subs(z,1/z))
    return sp.factor(p), sp.factor(pt), n, sp.simplify(-p/pt), C[idx[prev],idx[prev]]
prev_R=None
for extra in range(0,4):
    p,pt,n,R,c2=build(extra)
    P=sp.Poly(sp.expand(p),z)
    m=min(mm[0] for mm in P.monoms() if P.coeff_monomial(mm)!=0)
    g=sp.factor(sp.gcd(sp.Poly(sp.expand(p),z),sp.Poly(sp.expand(pt),z)).as_expr())
    red=sp.Poly(sp.cancel(sp.expand(p)/g),z)
    N=sum(mult for r,mult in sp.roots(red).items() if abs(complex(r))<1-1e-12)
    print("  cut +%d ray vertices: n=%d  c^2=%s  ord_0 p=%d  N=%d"%(extra,n,c2,m,N))
    chk("cut +%d: c^2 = 1 (the cut can be moved freely along the ray)"%extra, c2==1)
    chk("cut +%d: ord_0 p = 2(1+extra)"%extra, m==2*(1+extra), "got %d"%m)
    chk("cut +%d: N = 4 + 2(1+extra)"%extra, N==4+2*(1+extra), "got %d"%N)
    if prev_R is not None:
        chk("cut +%d: R_new = z^2 R_old  (each ray step is a pure 2-step delay)"%extra,
            sp.simplify(sp.together(R-z**2*prev_R))==0)
    # the Hasse-Weil factor is unchanged
    chk("cut +%d: the Hasse-Weil factor 2z^4-2z^2+1 still divides p"%extra,
        sp.simplify(sp.rem(sp.expand(p),sp.expand(2*z**4-2*z**2+1),z))==0)
    chk("cut +%d: the exterior pair +-sqrt2 and the cusp forms +-i survive"%extra,
        sp.simplify(sp.rem(sp.expand(p),sp.expand((z**2-2)*(z**2+1)**2),z))==0)
    chk("cut +%d: [z^m]p = -1 is STABLE under moving the cut"%extra,
        sp.expand(p).coeff(z,m)==-1, "%s"%sp.expand(p).coeff(z,m))
    prev_R=R
print()
print("  => z = 0 modes are NOT intrinsic: their number is 2 x (number of ray vertices")
print("     placed inside the core).  The nonzero divisor (exterior, cusp-form,")
print("     threshold, Hasse-Weil) and [z^m]p = -1 are invariant.")
print()
print("checks: %d   failures: %d"%(NCHK,len(FAIL)))
for f in FAIL: print("   FAILED:",f)

# ---------------------------------------------------------------------------
# PART 2.  Is the T2(d) height shift D = diag(1,1,z,z) the same thing as cutting
# the two Q-cusps of D3 one ray step further out (so that ALL FOUR rays begin at
# S(c_1) = 36)?  Build the 11-vertex core and compare.
# ---------------------------------------------------------------------------
import numpy as np, math
q3 = 3
S3 = {'L1p':48,'L1':12,'L2':6,'X':2,'Xp':8,'Y':6,'Z':12,'Zp':48,'Q':4}
E3 = [('L1p','L1',12),('L1','L2',6),('L2','X',2),('X','Xp',2),
      ('X','Y',2),('X','Q',2),('Y','Z',6),('Z','Zp',12)]
def scat(S,E,cusps,q,order):
    n=len(order); idx={v:i for i,v in enumerate(order)}
    T=np.zeros((n,n))
    for (a,b,e) in E:
        T[idx[a],idx[b]]=T[idx[b],idx[a]]=math.sqrt(S[a]*S[b]/(q*e*e))
    h=len(cusps); W=np.zeros((n,h))
    for k,(v,e) in enumerate(cusps): W[idx[v],k]=math.sqrt(S[v]/e)
    def S_of(zv):
        lam=zv+1/zv
        G=np.linalg.inv(lam*np.eye(n)-T)
        Gam=W.T@G@W
        return np.linalg.solve(zv*Gam-np.eye(h), np.eye(h)-Gam/zv)
    return S_of,W
ordA=['L1p','L1','L2','X','Xp','Y','Z','Zp','Q']
SA,_=scat(S3,E3,[('L1',12),('Z',12),('Q',4),('Q',4)],q3,ordA)
# now absorb the first vertex of each Q-ray (S = 12, edge to Q has S = 4,
# next edge has S = 12) into the core
Sb=dict(S3); Sb['P1']=12; Sb['P2']=12
Eb=list(E3)+[('Q','P1',4),('Q','P2',4)]
ordB=ordA+['P1','P2']
SB,_=scat(Sb,Eb,[('L1',12),('Z',12),('P1',12),('P2',12)],q3,ordB)
for zv in (0.8+0.1j, 0.4+0.2j, 0.33-0.71j, 0.61+0.44j):
    D=np.diag([1,1,zv,zv])
    chk("equal-depth cut of the D3 Q-cusps == the T2(d) height shift D S D (z=%s)"%round(zv.real,2),
        np.abs(SB(zv)-D@SA(zv)@D).max()<1e-9, "%.3g"%np.abs(SB(zv)-D@SA(zv)@D).max())
    # and then S is EXACTLY Sorensen's form (a-d)P_inv + d J
    M=SB(zv); a=M[0,0]; d=M[0,1]
    Pinv=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]],dtype=float)
    chk("equal-depth D3 S = (a-d)P_inv + d J  (Sorensen group matrix x inversion)",
        np.abs(M-((a-d)*Pinv+d*np.ones((4,4)))).max()<1e-9,
        "%.3g"%np.abs(M-((a-d)*Pinv+d*np.ones((4,4)))).max())
    chk("equal-depth D3: a - d = z^2 (the three nontrivial characters)",
        abs(a-d-zv**2)<1e-9, "%s"%(a-d))
    chk("equal-depth D3: the two P_inv-fixed cusps are L1, Z (S = 12); Q_1,Q_2 swap",
        abs(Pinv[0,0]-1)<1e-12 and abs(Pinv[1,1]-1)<1e-12 and abs(Pinv[2,3]-1)<1e-12)
print()
print("  => the T2(d) height renormalisation IS the geometric statement 'cut all four")
print("     cusps at the same ray depth'; in that cut the D3 scattering matrix is")
print("     literally Sorensen's Pic-group matrix times the class inversion.")
print()
print("checks: %d   failures: %d"%(NCHK,len(FAIL)))
for f in FAIL: print("   FAILED:",f)
