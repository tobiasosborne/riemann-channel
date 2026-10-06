"""REFUTE lane, 2026-10-06. Independent checks of cone-bridge.md from its STATEMENTS only
(no code from notes/adelic-gkp/checks/).  mpmath (50 digits) + sympy + PARI/GP via subprocess."""
import subprocess, itertools
import mpmath as mp, sympy as sp, numpy as np
mp.mp.dps = 50
def gp(cmd):
    return subprocess.run(['gp','-q','-f','-D','parisize=400000000'],input=cmd,capture_output=True,text=True).stdout.strip()
ok=[]
def rep(n,c,i=''):
    ok.append(bool(c)); print(('PASS ' if c else 'FAIL ')+n, i)

# ---------- genus two: chi = x^4-3x^3+7x^2-15x+25, q=5
q=5; chi=[1,-3,7,-15,25]
print('   PARI hyperellcharpoly:', gp('print(hyperellcharpoly(Mod(1,5)*(x^5+x^3+x^2-2)))'))
roots = mp.polyroots(chi, maxsteps=200, extraprec=200)
up = sorted([r for r in roots if mp.im(r)>0], key=lambda r:-mp.re(r+q/r))   # Phi_+ embeddings, ordered by lambda descending
emb = []
for r in up: emb += [r, mp.conj(r)]
lam = [mp.re(r+q/r) for r in up]
d = [mp.sqrt(4*q-l**2) for l in lam]
print('   lambda =', [mp.nstr(l,8) for l in lam], ' d_j =', [mp.nstr(x,8) for x in d])
# elements of K as functions of the embedding value a (root alpha): F -> a, V -> q/a, y=F+V
basis = [lambda a:1, lambda a:a+q/a, lambda a:a, lambda a:(a+q/a)*a]   # Z[F,V] = Z[y] + Z[y]F
def gram(f):  # f(a, xi, eta) summed over embeddings -> real matrix
    return mp.matrix([[mp.re(sum(f(a, basis[i](a), basis[k](a)) for a in emb)) for k in range(4)] for i in range(4)])
conj = lambda a: q/a          # complex conjugation sends alpha to q/alpha (=conj(alpha) on the circle)
hp = lambda y: 2*y-3          # h(y)=y^2-3y-3
dd = lambda a: (a-q/a)*hp(a+q/a)
Ocan = gram(lambda a,x,y: x*mp.conj(y)/dd(a))
Oplus = gram(lambda a,x,y: x*mp.conj(y)/(q/a-a))
Ttr = gram(lambda a,x,y: x*mp.conj(y))
R = lambda Mx: sp.Matrix(4,4,lambda i,k: int(mp.nint(Mx[i,k])))
isint = lambda Mx: max(abs(Mx[i,k]-mp.nint(Mx[i,k])) for i in range(4) for k in range(4))<mp.mpf(10)**-30
rep('Om_can integral, alternating', isint(Ocan) and R(Ocan).T==-R(Ocan), R(Ocan).tolist())
rep('det Om_can = 1 (unimodular)', R(Ocan).det()==1)
rep('Om_+ integral, alternating, det = disc(h)^2 = 441', isint(Oplus) and R(Oplus).T==-R(Oplus) and R(Oplus).det()==441)
rep('trace form Tr(x xbar) integral; disc Z[F,V] = det = 48069 = 21^2*109', isint(Ttr) and R(Ttr).det()==48069, R(Ttr).det())
print('   PARI disc of maximal order of Q(F):', gp('print(nfdisc(x^4-3*x^3+7*x^2-15*x+25))'), ' disc(Z[F]):', gp('print(poldisc(x^4-3*x^3+7*x^2-15*x+25))'), ' class number:', gp('print(bnfinit(x^4-3*x^3+7*x^2-15*x+25,1).no)'))
# M = multiplication by F in this basis
def mult(fun):
    # coordinates: solve sum_k c_k basis_k(a) = fun(a)*basis_i(a) for each i, using the 4 embeddings
    B = mp.matrix([[basis[k](a) for k in range(4)] for a in emb])
    cols=[]
    for i in range(4):
        rhs = mp.matrix([fun(a)*basis[i](a) for a in emb]); cols.append(mp.lu_solve(B,rhs))
    return mp.matrix([[mp.re(cols[i][k]) for i in range(4)] for k in range(4)])
Mm = mult(lambda a:a); Vm = mult(lambda a:q/a)
rep('F, V integral on Z[F,V]', isint(Mm) and isint(Vm))
Mi, Vi = R(Mm), R(Vm)
rep('M^T Om_can M = 5 Om_can; MV=5', Mi.T*R(Ocan)*Mi==5*R(Ocan) and Mi*Vi==5*sp.eye(4))
# mode projectors and Krein signs
def poly_in(Mx, coeffs): pass
y = Mm+Vm
pis=[]
for j in range(2):
    k=1-j; pis.append((y-lam[k]*mp.eye(4))/(lam[j]-lam[k]))
def krein(Om):
    out=[]
    for j in range(2):
        W = Om*(Mm-Vm)
        Wj = pis[j].T*W*pis[j]
        ev = mp.eig(mp.matrix([[ (Wj[i,k]+Wj[k,i])/2 for k in range(4)] for i in range(4)]))[0]
        ev = sorted([mp.re(e) for e in ev], key=abs)[-2:]
        out.append(int(mp.sign(ev[0])) if mp.sign(ev[0])==mp.sign(ev[1]) else 0)
    return out
kc, kp = krein(Ocan), krein(Oplus)
rep('Krein signs: Om_can = -sgn h\'(lambda_j) (mixed), Om_+ = (+,+)', kc==[-int(mp.sign(hp(l))) for l in lam] and kp==[1,1], (kc,kp))
def vacuum(Om, eps):
    Jm = sum((eps[j]*(Mm-Vm)*pis[j]/d[j] for j in range(2)), mp.zeros(4))
    return Om*Jm, Jm
Gc, Jc = vacuum(Ocan, kc); Gp, Jp = vacuum(Oplus, kp)
rep('J_can^2 = -1, G_can symmetric positive', mp.norm(Jc*Jc+mp.eye(4))<1e-30 and mp.norm(Gc-Gc.T)<1e-30 and min(mp.re(e) for e in mp.eig(Gc)[0])>0)
def weights(B, G):   # B = sum w_j G|_j : w_j = B(pi_j x, pi_j x)/G(pi_j x, pi_j x)
    out=[]
    for j in range(2):
        v = pis[j]*mp.matrix([1,2,-1,3])
        out.append((v.T*B*v)[0]/(v.T*G*v)[0])
    return out
wW = weights(Ocan*(Mm-Vm)/2, Gc); wT = weights(Ttr, Gc); wGp = weights(Gp, Gc); wTp = weights(Ttr, Gp)
rep('Weil form of Om_can = sum eps_j Im(alpha_j) G_can|_j', all(abs(wW[j]-kc[j]*d[j]/2)<1e-30 for j in range(2)), [mp.nstr(x,6) for x in wW])
rep('Rosati T_L (e=1) weights rel. G_can = |h\'| d_j = 10.870, 20.171', all(abs(wT[j]-abs(hp(lam[j]))*d[j])<1e-30 for j in range(2)), [mp.nstr(x,6) for x in wT])
rep('ratio 20.171/10.870 = R_0 = 1.8557', abs(wT[1]/wT[0]-mp.mpf('1.8557'))<5e-5, mp.nstr(wT[1]/wT[0],6))
rep('Weil form of Om_+ = T_L/2 exactly', mp.norm(Oplus*(Mm-Vm)/2 - Ttr/2)<1e-30)
rep('G_+ = sqrt21 G_can; T_L = sum d_j G_+|_j', all(abs(wGp[j]-mp.sqrt(21))<1e-30 for j in range(2)) and all(abs(wTp[j]-d[j])<1e-30 for j in range(2)))
# cone is 2-dim: similitude forms
Ms = sp.Matrix(Mi); syms = sp.symbols('b0:10'); Bs = sp.zeros(4); it=iter(syms)
for i in range(4):
    for k in range(i,4):
        s_=next(it); Bs[i,k]=s_; Bs[k,i]=s_
sol = sp.solve(list(Ms.T*Bs*Ms-5*Bs), syms, dict=True)[0]
rep('similitude forms: dimension g = 2', len(Bs.subs(sol).free_symbols)==2)
# unit orbit: e -> eps e, eps = (5+sqrt21)/2 = 1+lambda_1 in Q(lambda)
epsu = [1+l for l in lam]
rep('eps = 1+y is a unit of norm 1; Rosati weights at e=eps: 0.4735, 463.04', abs(epsu[0]*epsu[1]-1)<1e-30, [mp.nstr(wT[j]/epsu[j]**2,6) for j in range(2)])
# 5-adic types over the Galois closure (PARI): count primes above 5 by type
gpres = gp(r'''
f=x^4-3*x^3+7*x^2-15*x+25; L=nfinit(subst(nfsplitting(f),x,y)); print("deg Galois closure ",poldegree(L.pol)," group ",polgalois(f)[1..3]);
r=nfroots(L,f); P=idealprimedec(L,5); print("primes above 5: ",#P);
z=vector(4,k,nfeltembed(L,r[k],1));
for(i=1,#P, s=vector(4,k, nfeltval(L,r[k],P[i])>0); print(apply(t->round(real(t)*1000)/1000.,z)," ",apply(t->round(imag(t)*1000)/1000.,z)," ",s));
''')
print(gpres)
# parse: each prime line gives vals in order of roots r; classify by (Im>0 at root with larger lambda, Im>0 at smaller)
lines=[l for l in gpres.splitlines() if l.startswith('[') ]
cnt={}
for l in lines:
    re_s, im_s, s = [t.strip(' []') for t in l.split('] [')]
    re_v=[float(x) for x in re_s.strip('[]').split(',')]; im_v=[float(x) for x in im_s.strip('[]').split(',')]
    sv=[int(x) for x in s.strip('[]').split(',')]
    typ=[]
    for k in range(4):
        if sv[k]:
            al = complex(re_v[k],im_v[k]); lm=(al+5/al).real
            typ.append(('l1' if lm>1.5 else 'l2')+('+' if al.imag>0 else '-'))
    t=tuple(sorted(typ)); cnt[t]=cnt.get(t,0)+1
print('   S_P types:', cnt)
rep('8 primes; 2 each of Phi_+, conj Phi_+, and the two mixed types', len(lines)==8 and sorted(cnt.values())==[2,2,2,2] and cnt.get(('l1+','l2+'),0)==2)
mixed_can = tuple(sorted([('l1+' if kc[0]>0 else 'l1-'),('l2+' if kc[1]>0 else 'l2-')]))
rep('type of Om_can occurs among the mixed S_P', cnt.get(mixed_can,0)==2, mixed_can)
# the given 4x4 M of the page in its "symplectic Z-basis"
Mp = sp.Matrix([[-2,17,101,32],[-1,4,29,5],[0,1,7,3],[0,-2,-19,-6]])
Om4 = sp.Matrix([[0,0,1,0],[0,0,0,1],[-1,0,0,0],[0,-1,0,0]])
x_=sp.symbols('x')
rep('page M: M^T Om M = 5 Om (Om=[[0,I],[-I,0]]), charpoly chi', Mp.T*Om4*Mp==5*Om4 and sp.expand(Mp.charpoly(x_).as_expr()-(x_**4-3*x_**3+7*x_**2-15*x_+25))==0)
# graph convention impossible: (a-c)^2+4b^2=21
rep('no integer (a-c)^2+4b^2 = 21', not any((u*u+4*v*v)==21 for u in range(-5,6) for v in range(-3,4)))
# |h'| constant across roots is impossible for g>=3 (ordered-root argument); numeric spot check
rnd=np.random.default_rng(1); bad=0
for _ in range(2000):
    g=rnd.integers(3,6); r=np.sort(rnd.uniform(-3,3,g)); hpv=[abs(np.prod([r[j]-r[k] for k in range(g) if k!=j])) for j in range(g)]
    if max(hpv)/min(hpv)<1+1e-9: bad+=1
rep('g>=3: |h\'(lambda_j)| never constant (2000 random real-rooted h)', bad==0)

# ---------- K4 with one negative edge, q=2
As = np.array([[0,-1,1,1],[-1,0,1,1],[1,1,0,1],[1,1,1,0]],float)   # negative edge (1,2): the one P commutes with
ev,U = np.linalg.eigh(As)
rep('K4 one negative edge: spectrum {-sqrt5,-1,1,sqrt5}', np.allclose(ev,[-5**.5,-1,1,5**.5]), ev)
P = np.array([[-1,-2,1,1],[-2,-1,1,1],[1,1,-1,0],[1,1,0,-1]],float)
phi=(1+5**.5)/2
pv = [U[:,j]@P@U[:,j] for j in range(4)]
rep('P commutes with A_s, det 1, p(lambda)=(-phi^3,-1,1,phi^-3) = (1+2l-l^2)/2', np.allclose(P@As,As@P) and abs(np.linalg.det(P)-1)<1e-9 and np.allclose(pv,[-phi**3,-1,1,phi**-3]) and np.allclose(pv,[(1+2*l-l*l)/2 for l in ev]), np.round(pv,4))
n=4; I=np.eye(n); Z=np.zeros((n,n))
M8 = np.block([[Z,-I],[2*I,As]]); V8 = 2*np.linalg.inv(M8); Om8=np.block([[Z,I],[-I,Z]])
OmP = Om8@np.block([[P,Z],[Z,P]])
WP = OmP@(M8-V8)/2
sig = np.linalg.eigvalsh((WP+WP.T)/2)
rep('Weil form of Om_P has signature (4,4)', (sig>0).sum()==4 and (sig<0).sum()==4)
hpK=[abs(np.prod([l-m for m in ev if m!=l])) for l in ev]
rep('|p||h\'| = (75.8,8,8,4.22)', np.allclose(np.abs(pv)*hpK,[75.78,8,8,4.22],atol=0.01), np.round(np.abs(pv)*hpK,2))
# integral endomorphisms of Z^4 commuting with A_s that would make |p||h'| constant: impossible since p(+-1) rational, needs 5^(1/4)
print('   (|p(1)| would have to be 5^(1/4) for |p||h\'| constant with |N(p)|=1; p(1) is rational: impossible)')

# ---------- the 'general form' of lattice-tower §5 fails at a real eigenvalue +-sqrt(q)
B = sp.Matrix([[0,2],[1,0]]); qB = 2*B.inv().T
Mr = sp.diag(B, qB); Om = sp.Matrix([[0,0,1,0],[0,0,0,1],[-1,0,0,0],[0,-1,0,0]])
Vr = 2*Mr.inv()
rep('M_r = B (+) 2B^{-T}, B=[[0,2],[1,0]]: integral step, M^T Om M = 2 Om', all(x==int(x) for x in Mr) and Mr.T*Om*Mr==2*Om)
rep('M_r semisimple, all |mu| = sqrt2 (condition (i)), M_r^2 = 2', Mr*Mr==2*sp.eye(4))
rep('V = M, so (M-V)=0: every compatible Weil form vanishes (no positive one)', Vr==Mr)
# vacuum exists: eigenspaces of M/sqrt2 are Om-orthogonal symplectic planes; build J
S_ = (Mr/sp.sqrt(2))
Ep = (sp.eye(4)+S_)/2; Em=(sp.eye(4)-S_)/2
vp = Ep.columnspace(); vm = Em.columnspace()
rep('E+ and E- are Om-orthogonal and each symplectic (so an invariant vacuum exists: (iii))', all(sp.simplify((u.T*Om*w)[0])==0 for u in vp for w in vm) and sp.simplify((vp[0].T*Om*vp[1])[0])!=0 and sp.simplify((vm[0].T*Om*vm[1])[0])!=0)
print(sum(ok),'of',len(ok),'pass')
