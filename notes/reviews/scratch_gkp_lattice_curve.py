"""REFUTE lane, 2026-10-06. Independent checks of curve-bridge.md from its STATEMENTS only.
No code from notes/adelic-gkp/checks/ is used.  sympy + PARI/GP (gp binary by subprocess)."""
import subprocess, itertools
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

def gp(cmd):
    return subprocess.run(['gp','-q','-f','-D','parisize=200000000'],input=cmd,capture_output=True,text=True).stdout.strip()

ok = []
def rep(name, cond, info=''):
    ok.append(bool(cond)); print(('PASS ' if cond else 'FAIL ')+name, info)

q,a = sp.symbols('q a', real=True)
Om = sp.Matrix([[0,1],[-1,0]])
M  = sp.Matrix([[0,-1],[q,a]])
V  = sp.simplify(q*M.inv())
rep('V = qM^-1 = a - M', sp.simplify(V-(a*sp.eye(2)-M))==sp.zeros(2))
rep('M^T Om M = q Om', sp.simplify(M.T*Om*M-q*Om)==sp.zeros(2))
G = sp.simplify(Om*(M-V)/2)
rep('Weil form G = [[q,a/2],[a/2,1]]', G==sp.Matrix([[q,a/2],[a/2,1]]), G)
rep('G symmetric and M^T G M = qG', G==G.T and sp.simplify(M.T*G*M-q*G)==sp.zeros(2))
d = sp.sqrt(4*q-a**2)
J = (2*M-a*sp.eye(2))/d
rep('J^2=-1', sp.simplify(J*J+sp.eye(2))==sp.zeros(2))
rep('J = (M-V)/d', sp.simplify(J-(M-V)/d)==sp.zeros(2))
rep('J symplectic, JM=MJ', sp.simplify(J.T*Om*J-Om)==sp.zeros(2) and sp.simplify(J*M-M*J)==sp.zeros(2))
vac = sp.simplify(Om*J)
rep('vacuum form Om(.,J.) = 2G/d', sp.simplify(vac-2*G/d)==sp.zeros(2))
# cokernel side: state s=(Y_j,Y_{j-1}); recurrence Y_j = a Y_{j-1} - q Y_{j-2}
W = sp.Matrix([[a,-q],[1,0]])
Y = sp.symbols('Y0:6')
Yn = [sp.Integer(3), sp.Integer(-2)]
for j in range(2,7): Yn.append(sp.expand(a*Yn[-1]-q*Yn[-2]))
s = lambda j: sp.Matrix([Yn[j],Yn[j-1]])
rep('W s_j = s_{j+1}', all(sp.simplify(W*s(j)-s(j+1))==sp.zeros(2,1) for j in range(1,6)))
Qm = sp.Matrix([[1,-a/2],[-a/2,q]])
rep('Casoratian similitude Q(s_{j+1}) = q Q(s_j)', all(sp.simplify((s(j+1).T*Qm*s(j+1))[0]-q*(s(j).T*Qm*s(j))[0])==0 for j in range(1,6)))
rep('discrete Wronskian = Om on states; W^T Om W = q Om', sp.simplify(W.T*Om*W-q*Om)==sp.zeros(2))
S = sp.Matrix([[0,-1],[1,0]])
rep('S W S^-1 = M', sp.simplify(S*W*S.inv()-M)==sp.zeros(2))
rep('S^T Om S = Om', S.T*Om*S==Om)
rep('S^T G S = Q', sp.simplify(S.T*G*S-Qm)==sp.zeros(2))
# Rosati form T(phi,psi)=Tr_{H^1}(phi(F)psi(V)) on R[F], basis (1,F): realise F by the 2x2 companion acting on H^1
F = M; Vh = V
def ev(c, X): return c[0]*sp.eye(2)+c[1]*X
def T(c1,c2): return sp.simplify((ev(c1,F)*ev(c2,Vh)).trace())
Tg = sp.Matrix(2,2,lambda i,k: T([1-i,i],[1-k,k]))
rep('Rosati Gram in (1,F) = [[2,a],[a,2q]]', sp.simplify(Tg-sp.Matrix([[2,a],[a,2*q]]))==sp.zeros(2), Tg)
# C: s -> Y_j - Y_{j-1} F  as coefficient vector in (1,F)
Cm = sp.Matrix([[1,0],[0,-1]])
# multiplication by V on R[F] in basis (1,F): V = a - F; F*F = aF - q
mulF = sp.Matrix([[0,-q],[1,a]])   # columns: F*1 = F, F*F = -q + aF
mulV = a*sp.eye(2)-mulF
rep('C W = (mult by V) C', sp.simplify(Cm*W-mulV*Cm)==sp.zeros(2))
rep('C^T (T/2) C = Q', sp.simplify(Cm.T*Tg/2*Cm-Qm)==sp.zeros(2))
# psi: phi -> phi(M) e2
e2 = sp.Matrix([0,1])
Psi = sp.Matrix.hstack(e2, M*e2)
rep('Psi unimodular (e2 cyclic, det 1)', sp.simplify(Psi.det())==1)
rep('Psi (mult F) = M Psi', sp.simplify(Psi*mulF-M*Psi)==sp.zeros(2))
rep('Psi^T G Psi = T/2', sp.simplify(Psi.T*G*Psi-Tg/2)==sp.zeros(2))
Ros = sp.Matrix([[1,a],[0,-1]])  # F -> V = a - F on coefficients (c0 + c1 F -> c0 + c1 (a - F))
rep('Rosati involution is a T-isometry', sp.simplify(Ros.T*Tg*Ros-Tg)==sp.zeros(2))
rep('S = Psi o Rosati o C', sp.simplify(Psi*Ros*Cm-S)==sp.zeros(2))
# bridge identity
x = sp.Matrix(sp.symbols('x1 x2'))
lhs = (S*x).T*Om*J*(S*x)
rep('bridge: Om(Ss,JSs) = 2Q(s)/d = T(Cs,Cs)/d', sp.simplify(lhs[0]-2*(x.T*Qm*x)[0]/d)==0 and sp.simplify(lhs[0]-((Cm*x).T*Tg*(Cm*x))[0]/d)==0)
for nm,qq,aa in [('E1',2,-1),('E2',5,-2),('E3',7,2)]:
    print('   ',nm,' sqrt(4q-a^2) =', sp.sqrt(4*qq-aa**2))
# Howe sign: replace (Om,J) by (-Om,-J)
rep('(-Om)(.,(-J).) = Om(.,J.)', sp.simplify((-Om)*(-J)-Om*J)==sp.zeros(2))

# ---- Latimer-MacDuffee dictionary, improper conjugation, counterexample to (i)=>(ii)
A_,B_,C_ = sp.symbols('A B C')
MABC = sp.Matrix([[(a-B_)/2,-C_],[A_,(a+B_)/2]])
VA = a*sp.eye(2)-MABC
rep('Weil form of M_(A,B,C) = [[A,B/2],[B/2,C]]', sp.simplify(Om*(MABC-VA)/2-sp.Matrix([[A_,B_/2],[B_/2,C_]]))==sp.zeros(2))
rep('det M_(A,B,C) = q when B^2-4AC = a^2-4q', sp.simplify(MABC.det().subs(C_,(B_**2-a**2+4*q)/(4*A_))-q)==0)
D = sp.diag(1,-1)
Mp = D*MABC*D
rep('improper conjugate of M_(A,B,C) has Weil form -(A,-B,C)-type (negative definite)', sp.simplify(Om*(Mp-(a*sp.eye(2)-Mp))/2-sp.Matrix([[-A_,B_/2],[B_/2,-C_]]))==sp.zeros(2))
Mpr = sp.Matrix([[0,1],[-5,-2]])
Wpr = Om*(Mpr-5*Mpr.inv())/2
rep("M'=[[0,1],[-5,-2]]: step, |mu|=sqrt5, Weil form negative definite", Mpr.T*Om*Mpr==5*Om and all(abs(sp.N(ev_))-sp.sqrt(5).evalf()<1e-12 for ev_ in Mpr.eigenvals()) and Wpr[0,0]<0 and Wpr.det()>0, Wpr)
# ---- B10: pulled-back vacuum = det(g) * vacuum, so 'times 2' <=> det g = 2
for nm,qq,aa,frm in [('E2',5,-2,(2,0,2)),('E3',7,2,(2,0,3))]:
    M1 = sp.Matrix([[0,-1],[qq,aa]]); A0,B0,C0 = frm
    M2 = sp.Matrix([[(aa-B0)//2,-C0],[A0,(aa+B0)//2]])
    g = sp.Matrix(2,2,sp.symbols('g0:4'))
    sol = sp.solve(list(g*M1-M2*g), list(g), dict=True)[0]
    gs = g.subs(sol)
    free = list(gs.free_symbols)
    dets = sorted(set(int(gs.subs(dict(zip(free,v))).det()) for v in itertools.product(range(-3,4),repeat=len(free))))
    dd = sp.sqrt(4*qq-aa**2); J1=(2*M1-aa*sp.eye(2))/dd; J2=(2*M2-aa*sp.eye(2))/dd
    gg = gs.subs(dict(zip(free,[1]+[0]*(len(free)-1))))
    rep(f'{nm} {frm}: g^T vac2 g = det(g) vac1 for an intertwiner g', sp.simplify(gg.T*Om*J2*gg-gg.det()*Om*J1)==sp.zeros(2), f'det g={gg.det()}; smallest |det| over integral intertwiners: {min(abs(x) for x in dets if x)}')

# ---- groups of points vs T/(1-F^k)T (PARI)
def snf(Mx): 
    s=smith_normal_form(sp.Matrix(Mx),domain=sp.ZZ); return sorted(abs(int(s[i,i])) for i in range(2) if abs(int(s[i,i]))!=1)
def grp(eq,p,k):
    r = gp(f'E=ellinit({eq},ffgen({p}^{k},\'t)); print(ellgroup(E))')
    return sorted(int(x) for x in r.strip('[]').split(',') if x.strip())
cases = [('E1',2,-1,'[1,0,0,0,1]',(1,1,2)),('E2 b=1',5,-2,'[4,1]',(1,0,4)),('E2 b=4',5,-2,'[4,4]',(1,0,4)),('E2 b=0',5,-2,'[4,0]',(2,0,2)),('E3 j=4',7,2,'[3,3]',None),('E3 j=5',7,2,'[1,3]',None)]
for nm,qq,aa,eq,frm in cases:
    print('   ',nm,'j =',gp(f'E=ellinit({eq},Mod(1,{qq})); print(lift(E.j))'), ' a =', gp(f'E=ellinit({eq},{qq}); print(ellap(E))'))
    forms = [frm] if frm else [(1,0,6),(2,0,3)]
    comp = sp.Matrix([[0,-1],[qq,aa]])
    allk = True; compk=True; rows=[]
    for k in range(1,7):
        g_ = grp(eq,qq,k); rows.append(g_)
        for (A0,B0,C0) in forms:
            Mf = sp.Matrix([[(aa-B0)//2,-C0],[A0,(aa+B0)//2]])
            if snf(sp.eye(2)-Mf**k)!=g_: allk=False
        if snf(sp.eye(2)-comp**k)!=g_: compk=False
    rep(f'{nm}: E(F_q^k) = Z^2/(1-M^k) for its form class {forms}, k=1..6', allk, rows[:4])
    print('       companion lattice matches at all k=1..6:', compk)
print(sum(ok),'of',len(ok),'pass')

# ---- Theorem 12 cokernel in genus one, from A(n) (Riemann-Roch), cutoff N=5; independent rebuild
def cokernel_check(qq,aa,hh,N=5):
    A=lambda n: 0 if n<0 else (sp.Rational(qq-1,hh) if n==0 else sp.Integer(qq)**n-1)
    js=list(range(-N,N+1)); ms=list(range(-N,N+1))
    # admissible c: sum c_j = 0, sum c_j q^j = 0
    C=sp.Matrix([[1]*len(js),[sp.Integer(qq)**j for j in js]]).nullspace()
    # Ef(m) = q^{m/2} sum_j c_j A(j-m); work with the q^{m/2}-free vector u(m)=sum_j c_j A(j-m) and Y(m)=y(m) q^{m/2}:
    # <y,Ef> = sum_m y(m) q^{m/2} u(m) = sum_m Y(m) u(m)
    # also check Ef vanishes outside [-N,N]
    outside_ok=all(sum(c[i]*A(js[i]-m) for i in range(len(js)))==0 for c in C for m in list(range(-3*N,-N))+list(range(N+1,3*N)))
    U=sp.Matrix([[sum(c[i]*A(js[i]-m) for i in range(len(js))) for m in ms] for c in C])
    Ysol=U.nullspace()
    rec=all(all(Y[k]-aa*Y[k-1]+qq*Y[k-2]==0 for k in range(2,len(ms))) for Y in Ysol)
    return outside_ok, len(Ysol), rec
for nm,qq,aa,hh in [('E1',2,-1,4),('E2',5,-2,8)]:
    o,dim,rec=cokernel_check(qq,aa,hh)
    rep(f'{nm}: Ef supported in [-5,5]; cokernel dim 2; Y_j - aY_(j-1) + qY_(j-2) = 0 on window', o and dim==2 and rec, (o,dim,rec))
print(sum(ok),'of',len(ok),'pass (final)')
