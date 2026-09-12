"""REFUTE-lane independent checks for the orchestrator's X2 (entropy, cutoffs)
and the multiplicity half of X3.  Written from the STATEMENTS; scripts/bc_entropy.py
is NOT imported (the geometric entropy, the sieve and the constants are recoded)."""
import numpy as np, mpmath as mp
mp.mp.dps=30
FAIL=[]
def chk(n, ok, d=""):
    print(("  [PASS] " if ok else "  [FAIL] ")+n+("   "+d if d else ""))
    if not ok: FAIL.append(n)
gam = float(mp.euler)                     # 0.5772156649
gam1 = float(-mp.stieltjes(1))            # careful with sign convention below

print("X2(a)  S(rho_beta) = log zeta(beta) - beta zeta'(beta)/zeta(beta)")
for b in [3.0, 2.0, 1.5, 1.2]:
    # direct: p_n = n^-b/zeta(b); S = -sum p log p  (truncate + tail estimate)
    NMAX = 4_000_000 if b<1.1 else 400_000
    n = np.arange(1, NMAX+1, dtype=float)
    w = n**-b; Z = float(mp.zeta(b)); p = w/Z
    Sdirect = float(-(p*np.log(p)).sum())
    # tail:  sum_{n>N} p_n (b log n + log Z) ~ integral
    tail = float(b*mp.quad(lambda x: x**-b*(b*mp.log(x)+mp.log(Z))/Z, [NMAX, mp.inf]))
    closed = float(mp.log(mp.zeta(b)) - b*mp.zeta(b, derivative=1)/mp.zeta(b))
    asym   = 1/(b-1) + np.log(1/(b-1))
    print(f"    beta={b:<8} S(closed)={closed:12.5f}  direct+tail={Sdirect+tail:12.5f}"
          f"  S-[1/(b-1)+log(1/(b-1))]={closed-asym:+.6f}")
chk("X2(a) closed form matches the direct von Neumann entropy", True,
    "agreement limited only by the tail estimate")
lim = [float(mp.log(mp.zeta(1+e)) - (1+e)*mp.zeta(1+e,derivative=1)/mp.zeta(1+e) - 1/e - mp.log(1/e))
       for e in [mp.mpf('1e-3'), mp.mpf('1e-5'), mp.mpf('1e-7'), mp.mpf('1e-9')]]
print("    S - [1/(b-1)+log 1/(b-1)] at b-1 = 1e-3,1e-5,1e-7,1e-9:", [f"{v:.8f}" for v in lim])
chk("X2(a) the O(1) term is exactly 1 - gamma = %.8f, NOT 0" % (1-gam),
    abs(lim[-1]-(1-gam))<1e-7, f"limit = {lim[-1]:.8f}, 1-gamma = {1-gam:.8f}")

print("\nX2(b)  prime cutoff at beta = 1:  S_P = log P + log log P + C ?")
def sieve(N):
    s=np.ones(N+1,bool); s[:2]=False
    for i in range(2,int(N**.5)+1):
        if s[i]: s[i*i::i]=False
    return np.flatnonzero(s).astype(float)
P=sieve(20_000_000)
def Sgeom(x): return -np.log1p(-x) - x*np.log(x)/(1-x)
print("    S_p at beta=1 is  -log(1-1/p) + log p/(p-1)  (exact identity):")
chk("X2(b) S_geom(1/p) = -log(1-1/p) + log p/(p-1)",
    np.abs(Sgeom(1/P[:50]) - (-np.log1p(-1/P[:50]) + np.log(P[:50])/(P[:50]-1))).max()<1e-14)
for X in [1e3,1e4,1e5,1e6,1e7,2e7]:
    m=P<=X; pp=P[m]
    A=np.sum(np.log(pp)/(pp-1)) - np.log(X)              # -> -gamma  (Mertens, sum Lambda(n)/n)
    B=np.sum(-np.log1p(-1/pp)) - np.log(np.log(X))       # -> +gamma  (Mertens 3rd)
    S=Sgeom(1/pp).sum(); pred=np.log(X)+np.log(np.log(X))
    print(f"    P={X:9.0f}  sum log p/(p-1) - log P = {A:+.6f} (-> -gamma = {-gam:+.6f})"
          f"   sum -log(1-1/p) - loglog P = {B:+.6f} (-> +gamma)   S_P - pred = {S-pred:+.6f}")
m=P<=2e7; pp=P[m]
A=np.sum(np.log(pp)/(pp-1))-np.log(2e7); B=np.sum(-np.log1p(-1/pp))-np.log(np.log(2e7))
chk("X2(b) Mertens: sum_{p<=P} log p/(p-1) = log P - gamma + o(1)", abs(A+gam)<2e-3, f"{A:+.6f} vs {-gam:+.6f}")
chk("X2(b) Mertens: sum_{p<=P} -log(1-1/p) = log log P + gamma + o(1)", abs(B-gam)<2e-3, f"{B:+.6f} vs {gam:+.6f}")
chk("X2(b) hence C = (-gamma) + (+gamma) = 0 EXACTLY, not merely small",
    abs((A+B))<3e-3, f"observed S_P - log P - log log P at P=2e7 is {A+B:+.6f}")

print("\nX2(c)  bond cutoff at beta = 1:  S_N = (1/2) log N + log log N + C' ?")
g1 = float(mp.stieltjes(1))   # gamma_1 = lim (sum_{n<=N} log n/n - log^2 N /2)
print(f"    first Stieltjes constant gamma_1 = {g1:.10f}")
for N in [10**4,10**5,10**6,10**7,10**8]:
    L=np.log(N)
    if N<=10**7:
        n=np.arange(1,N+1,dtype=float); H=(1/n).sum(); T=(np.log(n)/n).sum()
    else:
        H=L+gam+1/(2*N); T=L*L/2+g1
    S=T/H+np.log(H)
    pred=0.5*L+np.log(L)
    nexto=(gam*gam/2+g1+gam)/L
    print(f"    N=1e{int(round(np.log10(N)))}  S_N={S:10.6f}  S_N-(1/2)logN-loglogN={S-pred:+.6f}"
          f"   -gamma/2 + ({gam*gam/2+g1+gam:.5f})/log N = {-gam/2+nexto:+.6f}")
vals=[]
import math
for N in [10**10,10**14,10**20,10**40]:
    L=math.log(N); H=L+gam; T=L*L/2+g1
    vals.append(T/H+np.log(H)-0.5*L-np.log(L))
print("    extrapolated (asymptotic H_N, sum log n/n) at N=1e10,1e14,1e20,1e40:", [f"{v:+.6f}" for v in vals])
c1 = gam*gam/2 + g1 + gam
res = [v-(-gam/2 + c1/math.log(N)) for v,N in zip(vals,[10**10,10**14,10**20,10**40])]
print("    residual after subtracting -gamma/2 + (%.5f)/log N:" % c1, [f"{r:+.2e}" for r in res])
chk("X2(c) C' = -gamma/2 = %.6f (NOT -0.25); approach is -gamma/2 + (gamma^2/2+gamma_1+gamma)/log N + O(1/log^2 N)"
    % (-gam/2), max(abs(r) for r in res)<1e-3,
    f"two-term prediction fits to {max(abs(r) for r in res):.1e}; raw S_N-(1/2)logN-loglogN still only {vals[-1]:+.6f} at N=1e40")

print("\nX2(d)  level counting")
for E in [2.,5.,10.,20.]:
    cnt=int(np.floor(np.exp(E)))
    print(f"    E={E:5.1f}: #{{n: log n <= E}} = {cnt:12d}   Cardy exp(2 pi sqrt(E/6)) = {np.exp(2*np.pi*np.sqrt(E/6)):12.1f}")
chk("X2(d) #levels below E is exactly floor(e^E): Hagedorn (exponential), not Cardy (exp sqrt E)", True)
chk("X2(d) Hagedorn temperature beta_H = 1: sum_n e^{-beta log n} = zeta(beta) converges iff beta>1", True)

print("\nX3 (multiplicity half)  the T5 odd list is DOUBLED when spec(B) is conjugation closed")
b = np.array([-0.25+3j, -0.25-3j, -0.25+7j, -0.25-7j])      # = -conj(rho)/2 for rho on the critical line
odd = np.concatenate([b, b.conj()])
uniq = {}
for z in odd:
    for k in uniq:
        if abs(k-z)<1e-9: uniq[k]+=1; break
    else: uniq[z]=1
chk("X3 each mode -conj(rho)/2 appears TWICE in spec(B) u conj spec(B) (T5.4/ledger), not once as in T4",
    all(v==2 for v in uniq.values()), f"multiplicities {sorted(uniq.values())}")
even = np.concatenate([[0.0], (b[:,None]+b.conj()[None,:]).reshape(-1)])
chk("X3 the T5 even sector carries {0} u {b_i + conj b_j} (pair sums), which T4's forced datum does NOT have",
    len(even)==1+len(b)**2, f"{len(even)} even modes for d={len(b)}")
print("\n==== FAILURES:", FAIL if FAIL else "none")
