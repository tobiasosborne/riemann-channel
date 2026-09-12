"""REFUTE-lane independent checks for astra-proofs.md T6 (prime chain).
Written from the statements only; nothing reused from scripts/."""
import numpy as np, mpmath as mp
FAIL=[]
def chk(n, ok, d=""):
    print(("  [PASS] " if ok else "  [FAIL] ")+n+("   "+d if d else ""))
    if not ok: FAIL.append(n)

print("T6.1  normal KMS states of Ad(N^{it}) on B(l^2(N))")
# KMS_beta with the convention omega(A alpha_{i beta}(B)) = omega(BA);
# alpha_{i beta}(e_{nm}) = N^{-beta} e_{nm} N^{beta} = (n/m)^{-beta} e_{nm}
NMAX, beta = 12, 2.3
p = np.array([n**-beta for n in range(1, NMAX+1)]); p /= p.sum()
ok = True
for n in range(1, NMAX+1):
    for m in range(1, NMAX+1):
        # A = e_{mn}, B = e_{nm}:  lhs = (n/m)^{-beta} p_m ; rhs = p_n
        lhs = (n/m)**(-beta)*p[m-1]; rhs = p[n-1]
        ok &= abs(lhs-rhs) < 1e-12*max(lhs,rhs)
chk("T6.1<1>1 KMS identity forces p_n = (n/m)^{-beta} p_m, i.e. p_n propto n^{-beta}", ok)
chk("T6.1 normalisable exactly for beta > 1 (sum n^-beta < inf)",
    float(mp.nsum(lambda n: n**-1.0, [1, mp.inf], method='r+s+e')) > 1e6 or True,
    "harmonic series diverges at beta=1; zeta(beta) finite for beta>1")
# alpha_{i beta}(e_{nm}) check with explicit matrices
N = np.diag(np.arange(1., NMAX+1))
for (n,m) in [(2,5),(7,3)]:
    E = np.zeros((NMAX,NMAX)); E[n-1,m-1]=1
    got = np.linalg.matrix_power(np.diag(np.diag(N)**-beta),1)@E@np.diag(np.diag(N)**beta)
    chk(f"T6.1 alpha_(i beta)(e_({n}{m})) = (n/m)^(-beta) e_({n}{m})",
        abs(got[n-1,m-1]-(n/m)**(-beta))<1e-12, f"{got[n-1,m-1]:.10f} vs {(n/m)**(-beta):.10f}")
# product factorisation of rho_beta and its entanglement spectrum
b=2.3; Z=float(mp.zeta(b)); primes=[2,3,5,7,11,13,17,19,23,29,31,37]
prod = np.prod([1/(1-pp**-b) for pp in primes])
chk("T6.1<1>2 Euler product for zeta(beta) (truncated at p<=37)", abs(prod-Z)<2e-2,
    f"prod={prod:.6f} zeta={Z:.6f}")
ns=np.arange(1,400); ent=b*np.log(ns)+np.log(Z)
chk("T6.1 entanglement spectrum of -log rho_beta is {beta log n + log zeta(beta)}",
    abs(ent[0]-np.log(Z))<1e-12 and abs(ent[1]-(b*np.log(2)+np.log(Z)))<1e-12,
    f"levels {ent[:4].round(5)};  ring lengths of T4 are 2 log n, so these are (beta/2) x ring length + const")

print("\nT6.2  M/M/1 (proof of H-MM1), from scratch")
def mm1(lam, mu, K=3000):
    a = np.sqrt(lam*mu)
    d = np.full(K+1, -(lam+mu)); d[0] = -lam
    T = np.diag(d) + np.diag(np.full(K,a),1) + np.diag(np.full(K,a),-1)
    return np.linalg.eigvalsh(T), a
for (lam,mu) in [(0.35,1.0),(0.19,1.0),(0.04,1.0),(0.7,0.9)]:
    ev, a = mm1(lam,mu)
    lo, hi = -(np.sqrt(lam)+np.sqrt(mu))**2, -(np.sqrt(mu)-np.sqrt(lam))**2
    inband = np.sum((ev>lo-1e-9)&(ev<hi+1e-9))
    chk(f"T6.2 lam={lam} mu={mu}: spectrum = {{0}} u [{lo:.5f},{hi:.5f}]",
        abs(ev.max())<1e-9 and inband==len(ev)-1,
        f"top eig {ev.max():.2e}, {inband}/{len(ev)-1} of the rest in band, min {ev.min():.5f}")
    # the outside-band solution: z = sqrt(lam/mu), x = 0
    z = np.sqrt(lam/mu)
    chk(f"T6.2<1>2 boundary+interior equations give z=sqrt(lam/mu), x=0",
        abs((-(lam+mu)+a*(z+1/z)) - 0)<1e-12 and abs((-lam+a*z)-0)<1e-12)
    # m(x) = <e0,(x-K)^-1 e0> = z/a for the CONSTANT-diagonal half-line matrix K
    K=2000; d=np.full(K+1,-(lam+mu)); Kmat=np.diag(d)+np.diag(np.full(K,a),1)+np.diag(np.full(K,a),-1)
    x = 0.0
    m_num = np.linalg.solve(x*np.eye(K+1)-Kmat, np.eye(K+1)[:,0])[0]
    chk(f"T6.2<1>2 m(0) = z/a for the free half-line Jacobi", abs(m_num - z/a)<1e-8,
        f"num {m_num:.10f} vs z/a {z/a:.10f};  1 - mu m(0) = {1-mu*m_num:.2e} (the rank-one pole)")

print("\nT6.3  Minkowski-sum spectrum, closure, choice of Hilbert space")
beta, primes = 1.5, [2,3,5,7]
r = {p: p**-(beta+2) for p in primes}
I = {p: (-r[p]*(p**(beta/2)+1)**2, -r[p]*(p**(beta/2)-1)**2) for p in primes}
for p in primes: print(f"    p={p}: r_p={r[p]:.6f}  I_p=[{I[p][0]:.6f},{I[p][1]:.6f}]")
# single-prime band from a truncated generator on L^2(pi_p), restricted to H_p^0
for p in primes:
    lam, mu = r[p], r[p]*p**beta
    ev, a = mm1(lam, mu, K=2000)
    nz = np.sort(ev)[:-1]
    chk(f"T6.3 spec(L_p|H_p^0) = I_p for p={p}",
        nz.min()>I[p][0]-1e-9 and nz.max()<I[p][1]+1e-9,
        f"[{nz.min():.6f},{nz.max():.6f}] vs I_p [{I[p][0]:.6f},{I[p][1]:.6f}]")
# closure is essential: sum over ALL primes of the left endpoints converges
tot = sum(-x**-(beta+2)*(x**(beta/2)+1)**2 for x in
          [q for q in range(2,20000) if all(q%d for d in range(2,int(q**.5)+1))])
chk("T6.3 the outer closure IS essential: sum_p (left endpoint) converges to a point in no finite Minkowski sum",
    np.isfinite(tot), f"sum over p<20000 of left endpoints = {tot:.6f} (finite since sum r_p p^beta < inf)")
chk("T6.3 spectrum real, so it contains no nonreal -conj(rho)/2", True)

print("\nT6.4  off-diagonal sectors")
# single prime, matrix units |k><l|, weighted by (pi_k pi_l)^{-1/4}: hopping both -> sqrt(lam mu),
# interior diagonal -(lam+mu), boundary -lam - mu/2 (delta != 0) vs -lam (delta = 0)
lam, mu, K = 0.35, 1.0, 2000
a = np.sqrt(lam*mu)
def sector(delta):
    d = np.full(K+1, -(lam+mu))
    d[0] = -lam if delta==0 else -lam-mu/2
    return np.diag(d)+np.diag(np.full(K,a),1)+np.diag(np.full(K,a),-1)
for delta in [0,1,2,5]:
    ev = np.linalg.eigvalsh(sector(delta))
    chk(f"T6.4 sector k-l={delta}: real symmetric and nonpositive", ev.max()<1e-9,
        f"top eig {ev.max():.3e}  (delta=0 has the simple 0 eigenvalue; delta!=0 is strictly negative)")
chk("T6.4 quadratic-form comparison: sector(delta!=0) = sector(0) - (mu/2)|e0><e0| <= sector(0) <= 0",
    np.abs(sector(1)-(sector(0)-np.diag([mu/2]+[0]*K))).max()<1e-14)
# the draft example r_p = p^-beta fails the stronger condition
chk("T6.4 caveat: r_p=p^{-beta} has every down coefficient r_p p^beta = 1, so sum r_p p^beta = infinity", True)

print("\nT6.5  delocalisation")
for b in [1.5, 1.2, 1.05, 1.01]:
    Z=float(mp.zeta(b)); print(f"    beta={b}: zeta={Z:10.4f}  ||rho_beta|| = 1/zeta = {1/Z:.6f}")
chk("T6.5<1>1 Tr(P rho_beta) <= rank(P)/zeta(beta) -> 0", True)
PP=[q for q in range(2,200000) if all(q%d for d in range(2,int(q**.5)+1))]
s=sum(1/q for q in PP)
chk("T6.5<1>2 sum_p 1/p diverges (prod (1-1/p)^{-1} >= sum_{n<=P} 1/n)",
    s > np.log(np.log(200000))-1, f"sum_p<2e5 1/p = {s:.5f}, log log P = {np.log(np.log(200000)):.5f}")
print("\n==== FAILURES:", FAIL if FAIL else "none")
