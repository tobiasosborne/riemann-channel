"""REFUTE lane, 2026-10-06: statements G1, G2, G3 of zeta-ingredients.md and S3 (data-ladder 4b), rebuilt from the statements.
numpy/scipy/mpmath; PARI/GP via subprocess for the genus-two Frobenius polynomial."""
import numpy as np, scipy.linalg as sl, mpmath as mp, subprocess
rng=np.random.default_rng(20261006)
ZE=np.load('/home/user/riemann-channel/data/zeros3000.npy')
ok=[]
def check(name,cond,info=""):
    ok.append(bool(cond)); print(("PASS " if cond else "FAIL ")+name+(" :: "+info if info else ""))

# ---------- G1: step, involution, similitude and adjunction for an arbitrary (non-RH) zero set ----------
mp.mp.dps=20
h=lambda u: mp.e**(-(u-0.3)**2)*(1+0.5j*u)
k=lambda u: mp.e**(-(u+0.2)**2/1.5)*(1-0.3j*u*u)
tilde=lambda f:(lambda u: mp.e**(-u)*mp.conj(f(-u)))          # x^{-1} conj f(1/x) in u=log x
step=lambda a,f:(lambda u: f(u-mp.log(a)))                      # delta_a * f
Vst=lambda a,f:(lambda u: a*f(u+mp.log(a)))                     # a delta_{1/a} * f
mell=lambda f,s: mp.quad(lambda u:f(u)*mp.e**(s*u),[-12,-3,0,3,12])   # int f(x) x^s d^x x
# delta transform check: tilde(delta_a) = a delta_{1/a} -- check on transforms of delta_a*h
a=mp.mpf(3); s0=mp.mpc(0.3,2.1)
check("G1 transform of delta_a*h is a^s hhat(s)",abs(mell(step(a,h),s0)-a**s0*mell(h,s0))<1e-12)
check("G1 transform of tilde h is conj(hhat(1-conj s))",abs(mell(tilde(h),s0)-mp.conj(mell(h,1-mp.conj(s0))))<1e-12)
# omega = sum over a synthetic zero set closed under rho->1-conj(rho), with an OFF-LINE quartet (no RH)
zs=[mp.mpc(0.5,g) for g in ZE[:6]]+[mp.mpc(0.5,-g) for g in ZE[:6]]+[mp.mpc(0.8,9),mp.mpc(0.2,9),mp.mpc(0.8,-9),mp.mpc(0.2,-9)]
def B(f1,f2):  # omega(f1 * tilde f2) = sum_rho f1hat(rho) * (tilde f2)hat(rho), transforms computed from the functions
    return sum(mell(f1,r)*mell(tilde(f2),r) for r in zs)
for a in [mp.mpf(2),mp.mpf('3.7')]:
    b0=B(h,k); b1=B(step(a,h),step(a,k)); b2=B(step(a,h),k); b3=B(h,Vst(a,k))
    check(f"G1 similitude B(M_a h,M_a k)=a B(h,k), a={a}, off-line zeros present",abs(b1-a*b0)<1e-9*abs(b0),f"{mp.nstr(b1/b0,12)}")
    check(f"G1 adjunction B(M_a h,k)=B(h,V_a k), a={a}",abs(b2-b3)<1e-9*abs(b2))

# ---------- G2: Proposition 1 ----------
def prop1(G,M,q,herm):
    V=q*np.linalg.inv(M); T=(lambda X:X.conj().T) if herm else (lambda X:X.T)
    Om=2*G@np.linalg.inv(M-V)
    return (np.abs(Om+T(Om)).max(), np.abs(T(M)@Om@M-q*Om).max(), np.abs(0.5*Om@(M-V)-G).max())
for herm in [False,True]:
    for sig in [(4,0),(2,2),(3,1)]:
        n=sum(sig); X=rng.normal(size=(n,n))+(1j*rng.normal(size=(n,n)) if herm else 0)
        G=X.conj().T@np.diag([1]*sig[0]+[-1]*sig[1])@X
        A=rng.normal(size=(n,n))+(1j*rng.normal(size=(n,n)) if herm else 0); A=A-(A.conj().T if herm else A.T)
        q=3.0; M=np.sqrt(q)*sl.expm(np.linalg.solve(G,A))
        e=prop1(G,M,q,herm)
        check(f"G2 Prop1 {'Hermitian' if herm else 'real'} G signature {sig}: alternating/compatible/(1/2)Om(M-V)=G",max(e)<1e-8,str(["%.1e"%v for v in e]))
# without the similitude hypothesis the alternating claim fails
G=np.eye(4); M=rng.normal(size=(4,4)); e=prop1(G,M,2.0,False)
check("G2 hypothesis needed: random M (not a similitude) gives a non-alternating Omega",e[0]>1e-2,"%.2f"%e[0])
# spectral model: B=I, M_p=diag(p^rho), V_p=diag(p^{1-rho})
g=ZE[:200]; rho=0.5+1j*g
for p in [2,3]:
    Mp=np.diag(p**rho); Vp=np.diag(p**(1-rho)); e=prop1(np.eye(200),Mp,float(p),True)
    w=np.diag(2*np.linalg.inv(Mp-Vp)); 
    check(f"G2 spectral model p={p}: Omega_p anti-Hermitian, weights -i/(sqrt p sin(g log p))",max(e)<1e-9 and np.allclose(w,-1j/(np.sqrt(p)*np.sin(g*np.log(p)))))

# ---------- G3: spectral-model numbers ----------
for p,f in [(2,0.502),(3,0.497),(5,0.498)]:
    fr=np.mean(np.sin(ZE*np.log(p))<0); check(f"G3 fraction of negative weights sqrt p sin(g log p), p={p}",abs(fr-f)<6e-4,f"{fr:.4f} (page {f})")
mn=np.min(np.abs(np.sin(ZE*np.log(2)))); check("G3 min|sin(g log2)| over 3000 zeros and weight 1/(sqrt2 min)",abs(mn-1.6e-4)<1e-5 and abs(1/(np.sqrt(2)*mn)-4393)<2,f"{mn:.4e}, {1/(np.sqrt(2)*mn):.1f}")
r=np.sqrt(2)*np.sin(ZE[:5]*np.log(2))/(np.sqrt(3)*np.sin(ZE[:5]*np.log(3)))
check("G3 ratios at first five zeros",np.allclose(np.round(r,2),[-1.67,-0.83,-1.14,0.71,0.61]),str(np.round(r,3)))
both=np.mean(np.sin(ZE*np.log(2))*np.sin(ZE*np.log(3))<0)
print(f"INFO  fraction of zeros where the steps 2 and 3 have opposite signs: {both:.3f}  -> no compatible Omega makes both Weil forms positive")
# generator D: Omega_FE weights -i sgn(g); Weil form of D = Omega_FE(.,D.) has weights |g|; Omega_D = B(.,D^{-1}.) weights 1/(conj(i g))
gg=np.concatenate([ZE[:50],-ZE[:50]]); wFE=-1j*np.sign(gg); dD=1j*gg
check("G3 generator: Omega_FE(.,D.) weights |gamma| > 0",np.allclose(np.conj(wFE)*0+wFE*dD,np.abs(gg)) or np.allclose(wFE*dD,np.abs(gg)) or np.allclose(np.conj(wFE)*dD,np.abs(gg)),"weights = sgn(g)*g")
wD=1/np.conj(dD); check("G3 Omega_D anti-Hermitian, B=Omega_D(.,D.), Williamson weights |g|",np.allclose(wD.real,0) and np.allclose(wD*np.conj(dD),1) and np.allclose(np.abs(1/wD),np.abs(gg)))
# Omega_D anti-Hermitian off RH: B(h,k)=sum_rho x_rho conj(y_{1-conj rho}); D acts by rho-1/2
zs2=np.array([0.5+14.13j,0.5-14.13j,0.8+9j,0.2+9j,0.8-9j,0.2-9j]); part=[np.argmin(abs(zs2-(1-np.conj(r)))) for r in zs2]
Bm=np.zeros((6,6),complex); 
for i,j in enumerate(part): Bm[i,j]=1      # B(x,y)=sum_i x_i conj(y_part(i)) -> y^H Bm^T x ; use form matrix F(x,y)=x^T Bm conj(y)
Dinv=np.diag(1/(zs2-0.5)); OmD=Bm@np.conj(Dinv)
check("G3 Omega_D anti-Hermitian with an off-line quartet (no RH)",np.allclose(OmD.T,-np.conj(OmD)))
# S2b attack: Omega_D is ONE form compatible with every step at once (form matrix F(x,y)=x^T F conj y)
for a_ in [2.0,3.0,5.0]:
    Ma=np.diag(a_**zs2)
    check(f"S2b Omega_D compatible with the step a={a_} (same Omega for every prime, off-line quartet present)",np.allclose(Ma.T@OmD@np.conj(Ma),a_*OmD) and np.allclose(Ma.T@Bm@np.conj(Ma),a_*Bm))
# Weil form is not normalisation-free: any positive diagonal weights c_g are the vacuum form of Omega with weights -i sgn(g) c_g
c=rng.uniform(0.2,5,100); OmC=-1j*np.sign(gg)*c; J=-1j*np.sign(gg)
check("G3 attack: every positive diagonal form c is the vacuum form of a compatible Omega (so 'B = G_J' fixes a normalisation)",np.allclose(np.conj(OmC)*J*0+ (OmC*np.conj(J)).real, c) or np.allclose((np.conj(OmC)*J).real,c))
# genus two: lambda_j and the F^2 Weil form for the Omega whose F-Weil form is positive
cp=subprocess.run(["gp","-q","-f"],input="print(Vec(hyperellcharpoly(Mod(1,5)*(x^5+x^3+x^2-2))))\n",capture_output=True,text=True).stdout.strip()
co=[int(t) for t in cp.strip("[]").split(",")]; F=np.zeros((4,4)); F[1:,:3]=np.eye(3); F[:,3]=-np.array(co[::-1][:4])
q=5; V=q*np.linalg.inv(F); lam=np.sort(np.roots([1,-3,-3]))
ev,X=np.linalg.eig(F); Xi=np.linalg.inv(X); G=np.real(Xi.conj().T@Xi)
check("genus two: real Frobenius roots lambda_j",np.allclose(np.sort(np.linalg.eigvals(F+V).real)[::2],lam,atol=1e-9) or np.allclose(np.unique(np.round(np.linalg.eigvals(F+V).real,6)),np.round(lam,6)),f"P={cp}, lambda={np.round(lam,3)}")
Om=2*G@np.linalg.inv(F-V); W2=0.5*Om@(F@F-V@V); W2=(W2+W2.T)/2
e2=np.linalg.eigvalsh(W2); check("genus two: Weil form of F^2 for Omega_+ (F-Weil form positive) is indefinite, inertia (2,2)",sum(e2>0)==2 and sum(e2<0)==2,str(np.round(e2,3)))

# ---------- S3: one mode, CM family over K=Q(sqrt-7) ----------
Om2=np.array([[0,1],[-1,0]]); J=np.array([[0,-1],[1,0]])
for th in [0.4,2.0,4.0]:
    qq=7.0; S=np.cos(th)*np.eye(2)+np.sin(th)*J; M=np.sqrt(qq)*S; V=qq*np.linalg.inv(M)
    W=0.5*Om2@(M-V); check(f"S3 one mode theta={th}: Weil form = sqrt q sin(theta) G_J",np.allclose(W,np.sqrt(qq)*np.sin(th)*Om2@J))
    check(f"S3 one mode theta={th}: reversing Omega reverses the sign",np.allclose(0.5*(-Om2)@(M-V),-np.sqrt(qq)*np.sin(th)*Om2@J))
# O_K basis {1,w}, w=(1+sqrt-7)/2, w^2=w-2; multiplication by a+bw
mul=lambda a,b: np.array([[a,-2*b],[b,a+b]],float)
sq7=mul(-1,2)/np.sqrt(7)   # sqrt(-7)=2w-1, J_K = mult by sqrt(-7)/sqrt7 = i
GJ=Om2@sq7; GJ=(GJ+GJ.T)/2; posJ=np.all(np.linalg.eigvalsh(GJ)>0)
check("S3 CM: J_K^2=-1, G_JK=Omega J_K positive for this orientation",np.allclose(sq7@sq7,-np.eye(2)) and posJ)
TR=np.array([[2,1],[1,4]],float)   # Tr(x conj y) in basis {1,w}
check("S3 CM: trace form Tr(x conj y) is a positive multiple of G_JK",np.allclose(TR/TR[0,0],GJ/GJ[0,0]),f"ratio {TR[0,0]/GJ[0,0]:.4f} = 2*sqrt7/... ")
signs=[]; allpos=True
for p in [2,11,23,29,37,43,53,67,71,79]:
    sols=[(a,b) for a in range(-40,41) for b in range(-40,41) if a*a+a*b+2*b*b==p]
    (a,b)=sols[0]; M=mul(a,b); V=p*np.linalg.inv(M); W=0.5*Om2@(M-V); W=(W+W.T)/2
    im=b*np.sqrt(7)/2
    check(f"S3 CM p={p}: Weil form = Im psi(P) G_JK, definite; conjugate prime opposite sign",np.allclose(W,im*GJ) and np.allclose(0.5*Om2@(mul(a+b,-b)-p*np.linalg.inv(mul(a+b,-b))),-im*(Om2@sq7)) and np.linalg.det(W)>0)
    # choose the prime above p with Im>0
    ap,bp=(a,b) if b>0 else (a+b,-b); Mp=mul(ap,bp); Wp=0.5*Om2@(Mp-p*np.linalg.inv(Mp)); allpos&=np.all(np.linalg.eigvalsh((Wp+Wp.T)/2)>0)
check("S3 attack: one step per split rational prime (Im psi>0) -> every Weil form positive for ONE Omega",allpos)
print(f"\n{sum(ok)} of {len(ok)} pass")
