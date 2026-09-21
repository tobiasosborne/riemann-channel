#!/usr/bin/env python3
"""REFUTE lane, cusp-graph round: wave group, the 3/32 obstruction, the Hardy model,
the renewal channel (T1, T3-T6).   Author: claude:opus.
Nothing imported from scripts/cusp_graph.py; every object rebuilt from the definitions.
"""
import numpy as np, math, itertools
rng = np.random.default_rng(20260921)
OK = 0; FAIL = []
def chk(c, m):
    global OK
    if c: OK += 1
    else: FAIL.append(m); print("   !! FAIL:", m)

# ---------------------------------------------------------------- the graph
def build_T(TX, c, L):
    n = TX.shape[0]; N = n+L; T = np.zeros((N,N)); T[:n,:n] = TX
    for k in range(1, L): T[n+k-1, n+k] = T[n+k, n+k-1] = 1.0
    T[0, n] = T[n, 0] = c
    return T, n

def Emat(T):
    N = T.shape[0]
    return np.block([[np.eye(N), -T/2],[-T/2, np.eye(N)]])
def Wmat(T):
    N = T.shape[0]
    return np.block([[T, -np.eye(N)],[np.eye(N), np.zeros((N,N))]])

print("="*78); print("G.  T1(a): energy invariance, d'Alembert, the radiation spaces")
print("="*78)
for TXc in [ (np.array([[0.0]]), math.sqrt(3.0)),           # pure cusp q=2
             (np.array([[1.0]]), math.sqrt(0.5)),
             (np.array([[0.3,0.4],[0.4,-0.2]]), 1.3) ]:
    TX, c = TXc; L = 60; T, n = build_T(TX, c, L); E = Emat(T); W = Wmat(T); N = T.shape[0]
    chk(np.max(np.abs(W.T@E@W - E)) < 1e-10, "T1(a): W^T E W = E (energy invariance)")
    ray = lambda k: n+k-1
    def dplus(j):                       # (B, S*B) with B = e_{r_j}, j >= 2
        u = np.zeros(N); v = np.zeros(N); u[ray(j)] = 1.0; v[ray(j-1)] = 1.0
        return np.concatenate([u, v])
    def dminus(j):                      # (F, S F) with F = e_{r_j}, j >= 1
        u = np.zeros(N); v = np.zeros(N); u[ray(j)] = 1.0; v[ray(j+1)] = 1.0
        return np.concatenate([u, v])
    # forward / backward invariance (and the necessity of B_1 = 0)
    for j in range(2, 8):
        a = dplus(j); Wa = W@a
        chk(np.max(np.abs(Wa - dplus(j+1))) < 1e-12, f"T1(a): W (B,S*B) = (SB, B), j={j}")
    bad = np.zeros(2*N); bad[ray(1)] = 1.0                    # B = e_{r_1}, S*B = 0
    chk(abs((W@bad)[:N][0]) > 1e-9, "T1(a): B_1 != 0 leaks core data under W (so B_1 = 0 is forced)")
    Wi = np.linalg.inv(W)
    for j in range(1, 8):
        chk(np.max(np.abs(Wi@dminus(j) - dminus(j+1))) < 1e-12, f"T1(a): W^-1 (F,SF) = (SF, S^2 F), j={j}")
    # energy formulas (1.1) on random profiles
    for _ in range(40):
        B = np.zeros(N); F = np.zeros(N)
        Bc = rng.normal(size=12); Fc = rng.normal(size=12)
        for i, val in enumerate(Bc): B[ray(2+i)] = val
        for i, val in enumerate(Fc): F[ray(1+i)] = val
        u = np.concatenate([B, np.concatenate([np.zeros(n), B[n+1:], [0.0]])])   # (B, S*B)
        SB = np.zeros(N); SB[ray(1):ray(1)+L-1] = B[ray(2):ray(2)+L-1]
        up = np.concatenate([B, SB])
        SF = np.zeros(N); SF[ray(2):ray(2)+L-1] = F[ray(1):ray(1)+L-1]
        um = np.concatenate([F, SF])
        Bseq = np.concatenate([[0.0, 0.0], [B[ray(k)] for k in range(2, L+1)]])   # B_0,B_1,B_2,...
        Fseq = np.concatenate([[0.0, 0.0], [F[ray(k)] for k in range(1, L+1)]])   # F_{-1},F_0,F_1,...
        e_plus  = 0.5*sum((Bseq[k+2]-Bseq[k])**2 for k in range(0, L-1))
        e_minus = 0.5*sum((Fseq[k+2]-Fseq[k])**2 for k in range(0, L-1))
        chk(abs(up@E@up - e_plus) < 1e-9, "T1(a): E(B,S*B) = (1/2) sum |B_{k+2}-B_k|^2")
        chk(abs(um@E@um - e_minus) < 1e-9, "T1(a): E(F,SF) = (1/2) sum |F_k - F_{k-2}|^2")
        chk(abs(up@E@um) < 1e-9, "T1(a): D_+^0 perp_E D_-^0  (B on k>=2, F on k>=1)")
    # a datum with B_1 != 0 is NOT E-orthogonal to D_-  (numerics-lane D8, independently)
    b1 = np.zeros(2*N); b1[ray(1)] = 1.0; b1[N+0] = c       # (e_{r1}, c e_{v0})
    f1 = dminus(1)
    chk(abs(b1@E@f1 - (1-c*c)/2) < 1e-10,
        f"T1(a): <b_1, E f_1> = (1-c^2)/2 = {(1-c*c)/2:.6f}  [confirms numerics D8]")

print("="*78); print("H.  T1(c): the 3/32 obstruction, and when it disappears")
print("="*78)
for q in [2, 3, 5]:
    TX = np.array([[0.0]]); c = math.sqrt(q+1.0); L = 400
    T, n = build_T(TX, c, L); E = Emat(T); N = T.shape[0]; ray = lambda k: n+k-1
    V = []
    for beta in [q**-0.5, -q**-0.5]:
        v = np.zeros(N); v[0] = 1.0
        for k in range(1, L+1): v[ray(k)] = c*beta**k
        V.append(v/np.linalg.norm(v))
    V = np.array(V)
    chk(np.max(np.abs(T@V[0] - (q+1)/math.sqrt(q)*V[0])) < 1e-9, f"q={q}: bound eigenvalue +(q+1)/sqrt q")
    chk(abs(abs(V[0][ray(1)])**2 - (q/( (q+1)+q ))*0 - (q+1)/( (q+1)+ (q+1)/(q-1)*0 +0)*0 - abs(V[0][ray(1)])**2) < 1,
        "placeholder")
    OK -= 1   # drop the placeholder
    P = np.eye(N) - V.T@V
    Pp = np.block([[P, np.zeros((N,N))],[np.zeros((N,N)), P]])
    a = np.zeros(2*N); a[ray(2)] = 1.0; a[N+ray(1)] = 1.0     # (r_2, r_1) in D_+^0
    b = np.zeros(2*N); b[ray(2)] = 1.0; b[N+ray(3)] = 1.0     # (r_2, r_3) in D_-^0
    chk(abs(a@E@b) < 1e-12, f"q={q}: the two local data ARE E-orthogonal before deletion")
    val = (Pp@a)@E@(Pp@b)
    f1sq = V[0][ray(1)]**2
    pred = 2*0.5*f1sq*(1-1/q)**2                               # 2 bound states, each -(1/2)f1^2(1-beta^2)^2
    chk(abs(val - pred) < 1e-7, f"q={q}: <Qa,Qb>_E = {val:.12f} = 2*(1/2)f_1^2(1-beta^2)^2")
    if q == 2:
        chk(abs(val - 3/32) < 1e-7, f"q=2: <Qa,Qb>_E = {val:.12f} = 3/32 EXACTLY (prover's number)")
        chk(abs(f1sq - 3/8) < 1e-10, "q=2: normalised |f_1|^2 = 3/8 (prover's number)")
# no bound states  =>  no obstruction (H-LOCAL)
for TX, c2 in [(np.array([[1.0]]), 0.5), (np.array([[0.0]]), 1.5)]:
    c = math.sqrt(c2); L = 400; T, n = build_T(TX, c, L); E = Emat(T); N = T.shape[0]; ray = lambda k: n+k-1
    ev, evec = np.linalg.eigh(T); tail = np.linalg.norm(evec[-40:,:], axis=0)
    nb = sum(1 for i in range(len(ev)) if tail[i] < 1e-3 and abs(ev[i]) > 2+1e-4)
    a = np.zeros(2*N); a[ray(2)] = 1.0; a[N+ray(1)] = 1.0
    b = np.zeros(2*N); b[ray(2)] = 1.0; b[N+ray(3)] = 1.0
    chk(nb == 0 and abs(a@E@b) < 1e-12, "H-LOCAL: no bound states => projection is the identity, no 3/32")
# the projected radiation spaces remain ISOMETRIC (prover's (a, a/beta) / (a, beta a) lemma)
q = 2; TX = np.array([[0.0]]); c = math.sqrt(q+1.0); L = 400
T, n = build_T(TX, c, L); E = Emat(T); N = T.shape[0]; ray = lambda k: n+k-1
V = []
for beta in [q**-0.5, -q**-0.5]:
    v = np.zeros(N); v[0] = 1.0
    for k in range(1, L+1): v[ray(k)] = c*beta**k
    V.append(v/np.linalg.norm(v))
V = np.array(V); P = np.eye(N) - V.T@V
Pp = np.block([[P, np.zeros((N,N))],[np.zeros((N,N)), P]])
def dplus(j):
    x = np.zeros(2*N); x[ray(j)] = 1.0; x[N+ray(j-1)] = 1.0; return x
def dminus(j):
    x = np.zeros(2*N); x[ray(j)] = 1.0; x[N+ray(j+1)] = 1.0; return x
for j in range(2, 10):
    for k in range(2, 10):
        chk(abs(dplus(j)@E@dplus(k) - (Pp@dplus(j))@E@(Pp@dplus(k))) < 1e-9,
            "T1(c): deletion preserves the E-inner product WITHIN D_+^0")
for j in range(1, 10):
    for k in range(1, 10):
        chk(abs(dminus(j)@E@dminus(k) - (Pp@dminus(j))@E@(Pp@dminus(k))) < 1e-9,
            "T1(c): deletion preserves the E-inner product WITHIN D_-^0")

print("="*78); print("I.  T1(c)/(d): Blaschke factorisation, R H^2 cap H^2, the model space")
print("="*78)
def poly_p(TX, c2, tilde=False):
    n = TX.shape[0]; m = 2*n+1
    w = np.exp(2j*np.pi*np.arange(m)/m); vals = np.empty(m, complex)
    P0 = np.zeros((n,n)); P0[0,0] = 1.0
    for i, z in enumerate(w):
        vals[i] = np.linalg.det((1+z*z)*np.eye(n) - z*TX - (c2*z*z if tilde else c2)*P0)
    return (np.fft.fft(vals)/m)[::-1].real

MODELS = [("loop a=1 c2=0.5",  np.array([[1.0]]), 0.5),
          ("loop a=0 c2=0.5",  np.array([[0.0]]), 0.5),
          ("loop a=0.5 c2=1.2",np.array([[0.5]]), 1.2),
          ("2v prover T7a",    np.array([[0.4,np.sqrt(51)/5],[np.sqrt(51)/5,0.1]]), 2.5),
          ("2v t=1",           np.array([[0.0,1.0],[1.0,0.0]]), 0.5),
          ("random 3v",        np.array([[-0.3,0.15,-0.4],[0.15,-0.1,-0.1],[-0.4,-0.1,-0.4]]), 0.6)]
def split(TX, c2):
    n = TX.shape[0]
    p = poly_p(TX,c2); pt = poly_p(TX,c2,True)
    ev, evec = np.linalg.eigh(TX); seen=[]; cusp=[]
    for j in range(n):
        t = ev[j]
        if any(abs(t-s)<1e-8 for s in seen): continue
        seen.append(t); idx=[k for k in range(n) if abs(ev[k]-t)<1e-8]
        mc = len(idx) - (1 if np.linalg.norm(evec[0,idx])>1e-9 else 0)
        if mc: cusp.append((t,mc))
    Dc = np.array([1.0])
    for t,m in cusp:
        for _ in range(m): Dc = np.convolve(Dc,[1.0,-t,1.0])
    pb  = np.polydiv(p,Dc)[0] if len(Dc)>1 else p
    ptb = np.polydiv(pt,Dc)[0] if len(Dc)>1 else pt
    ptb = ptb[np.argmax(np.abs(ptb)>1e-10):]
    beta = [r.real for r in np.roots(ptb) if abs(r)<1-1e-7] if len(ptb)>1 else []
    res  = [r for r in (np.roots(pb) if len(pb)>1 else []) if abs(r)<1-1e-7]
    return res, beta

def blaschke(zs, w):
    out = np.ones_like(np.asarray(w, complex))
    for a in zs: out = out*(w-a)/(1-np.conj(a)*w)
    return out

for tag, TX, c2 in MODELS:
    res, beta = split(TX, c2)
    N = len(res)
    def Rf(z):
        lam = z+1/z; G = np.linalg.solve(lam*np.eye(TX.shape[0])-TX, np.eye(TX.shape[0])[:,0])[0]
        return (1-c2*G/z)/(c2*G*z-1)
    # Theta = eta R B_bd with |eta| = 1  (prover (1.2))
    ws = 0.97*np.exp(1j*np.linspace(0.05, 6.2, 60))
    eta = np.array([blaschke(res, w)/(Rf(w)*blaschke(beta, w)) for w in ws])
    chk(np.max(np.abs(eta - eta[0])) < 1e-7 and abs(abs(eta[0])-1) < 1e-7,
        f"{tag}: Theta = eta R B_bd with eta constant of modulus 1 (eta = {eta[0]:.6f})")
    # R H^2 cap H^2 = Theta H^2:  R f analytic in the disc  <=>  f(beta) = 0 for every beta
    def neg_fourier(fun, M=32768):
        th = 2*np.pi*np.arange(M)/M
        v = np.array([fun(np.exp(1j*t)) for t in th])
        co = np.fft.fft(v)/M                    # co[k] = k-th Fourier coefficient
        return np.max(np.abs(co[M//2:]))        # negative-frequency mass
    if beta:
        f_bad = lambda w: 1.0+0*w
        chk(neg_fourier(lambda w: Rf(w)*f_bad(w)) > 1e-6,
            f"{tag}: R*1 is NOT in H^2 (poles at beta)")
        Bb = lambda w: blaschke(beta, w)
        chk(neg_fourier(lambda w: Rf(w)*Bb(w)) < 1e-8,
            f"{tag}: R * B_bd IS in H^2 -> R H^2 cap H^2 = R B_bd H^2 = Theta H^2")
        chk(neg_fourier(lambda w: Rf(w)*np.polyval(np.poly(beta)[::-1]*0 + np.poly(beta), w)) < 1e-8,
            f"{tag}: R * (any polynomial vanishing at every beta) is in H^2")
    else:
        chk(neg_fourier(lambda w: Rf(w)) < 1e-8, f"{tag}: no bound states => R itself is inner (H-LOCAL)")
    # the model space: dim K_Theta = N, spec Z = resonances
    if N >= 1 and len(set(np.round(res,10))) == N:
        zs = np.array(res, complex)
        G = 1.0/(1-np.conj(zs)[:,None]*zs[None,:])
        Gh = np.linalg.cholesky(G) if np.min(np.linalg.eigvalsh(G))>0 else None
        evG, UG = np.linalg.eigh(G); Gs = UG@np.diag(np.sqrt(evG))@UG.conj().T
        Gis = UG@np.diag(1/np.sqrt(evG))@UG.conj().T
        D = np.diag(zs)
        C = Gs@D@Gis                     # C = Z^* in an orthonormal basis of K_Theta
        j = Gis@np.ones(N)
        chk(np.max(np.abs(np.eye(N) - C.conj().T@C - np.outer(j, j.conj()))) < 1e-9,
            f"{tag}: I - C^*C = j j^*  (defect identity (1.3))")
        chk(np.max(np.abs(G - D.conj().T@G@D - np.ones((N,N)))) < 1e-9,
            f"{tag}: G - D^*GD = 1 1^*  (coordinate form of (1.3))")
        ec = np.linalg.eigvals(C)
        chk(max(min(abs(ec - z)) for z in zs) < 1e-8 and max(min(abs(zs - e_)) for e_ in ec) < 1e-8,
            f"{tag}: spec C = the resonances themselves (not 1/conj z)")
        chk(np.linalg.norm(np.linalg.matrix_power(C, 4000)) < 1e-9, f"{tag}: C^m -> 0")
        # direct Hardy-space cross-check of the Gram matrix by circle quadrature
        M = 65536; th = 2*np.pi*np.arange(M)/M; wc = np.exp(1j*th)
        ker = np.array([1.0/(1-z*wc) for z in zs])
        Gq = (ker.conj()@ker.T)/M
        chk(np.max(np.abs(Gq - G)) < 1e-8, f"{tag}: quadrature Gram = 1/(1 - conj(z_i) z_j)")
        Th = blaschke(zs, wc)
        chk(np.max(np.abs(np.abs(Th)-1)) < 1e-9, f"{tag}: Theta is inner on the circle")
        for i in range(N):
            chk(abs(abs(blaschke(zs, np.conj(zs[i]))) ) < 1e-9 or abs(blaschke(zs, np.conj(zs[i]))) < 1e-9,
                f"{tag}: Theta(conj z_i) = 0, so k_i(w)=1/(1-z_i w) lies in K_Theta")
        # <j,k_i> = 1 in the kernel basis
        coeff = np.linalg.solve(G, np.ones(N))
        chk(np.max(np.abs(G@coeff - np.ones(N))) < 1e-9, f"{tag}: j = V G^-1 1, <j,k_i> = 1")

print("="*78); print("J.  T1(c) (1.2a): the Abel-regularised radiation amplitude ratio")
print("="*78)
import sympy as sp
wS, tS, RS = sp.symbols('w t R')
aS = (wS**2-1)/(1-tS*wS**2)
bS = (1-wS**-2)*wS**-1/(RS*(1-tS*wS**-2))
chk(sp.simplify(sp.limit(aS/bS, tS, 1) + wS*RS) == 0,
    "T1(c): the prover's own Abel limit of his two pairings is exactly -w R")
# independent CLOSED-FORM derivation of the two radiation amplitudes.
# For a W-eigendatum X = (g, g/w) with T g = lam g, lam = w + 1/w real on |w| = 1,
#   <X, (u,v)>_E = ((1-w^2)/2) [ <g,u> - w^{-1} <g,v> ] .
# Outgoing (u,v) = (B, S*B):   <g,u> - w^-1<g,v> = (w^2-1) sum_j B_j w^{j-2}
# Incoming (u,v) = (F, S F):   <g,u> - w^-1<g,v> = conj(R)(w^2-1) sum_j F_j w^{-j-2}
q = 2; TX = np.array([[0.0]]); c = math.sqrt(q+1.0); L = 1400
T, n = build_T(TX, c, L); E = Emat(T); N = T.shape[0]; ray = lambda k: n+k-1
def Rpure(z): return (z*z-q)/(q*z*z-1)
for th in [0.6, 2.4, 4.1]:
    w = np.exp(1j*th); lam = w+1/w; R = Rpure(w)
    g = np.zeros(N, complex); g[0] = (1+R)/c
    for k in range(1, L+1): g[ray(k)] = w**(-k) + R*w**k
    chk(np.max(np.abs((T@g - lam*g)[:n+L-2])) < 1e-9, f"th={th:.2f}: g solves T g = lam g")
    data = np.concatenate([g, g/w])
    for tt in [0.95, 0.98]:
        B = np.zeros(N); F = np.zeros(N)
        for l in range(0, L//2-2):
            B[ray(2*l+2)] = math.sqrt(2)*tt**l
            F[ray(2*l+1)] = math.sqrt(2)*tt**l
        SsB = np.zeros(N); SsB[ray(1):ray(1)+L-1] = B[ray(2):ray(2)+L-1]
        SF  = np.zeros(N); SF[ray(2):ray(2)+L-1]  = F[ray(1):ray(1)+L-1]
        gp = np.concatenate([B, SsB]); gm = np.concatenate([F, SF])
        Ap = np.conj(data)@E@gp; Am = np.conj(data)@E@gm
        Ap_cf = ((1-w**2)/2)*(w**2-1)*math.sqrt(2)/(1-tt*w**2)
        Am_cf = ((1-w**2)/2)*np.conj(R)*(w**2-1)*math.sqrt(2)*w**(-3)/(1-tt*w**(-2))
        chk(abs(Ap-Ap_cf) < 1e-6*max(1,abs(Ap_cf)), f"th={th:.2f} t={tt}: outgoing amplitude closed form")
        chk(abs(Am-Am_cf) < 1e-6*max(1,abs(Am_cf)), f"th={th:.2f} t={tt}: incoming amplitude closed form")
    # Abel limit t -> 1 of the closed-form ratio
    lim = None
    for tt in [0.999, 0.99999, 0.9999999]:
        lim = (w**3*(1-tt*w**(-2)))/(np.conj(R)*(1-tt*w**2))
    chk(abs(lim + w*R) < 1e-5,
        f"T1(c) (1.2a): Abel limit of the amplitude ratio = -w R  (th={th:.2f}, dev {abs(lim+w*R):.2e})")
    chk(abs(abs(lim)-1) < 1e-8, f"T1(c): the ratio is unimodular (so U gamma_+ = -R once U gamma_- = w^-1)")
    # the untapered wandering profiles have E = 1 and orthonormal W-translates
    B = np.zeros(N); F = np.zeros(N)
    for l in range(0, L//2-2):
        B[ray(2*l+2)] = math.sqrt(2); F[ray(2*l+1)] = math.sqrt(2)
    SsB = np.zeros(N); SsB[ray(1):ray(1)+L-1] = B[ray(2):ray(2)+L-1]
    gp = np.concatenate([B, SsB])
    # the INFINITE profile has E = (1/2)|B_2-B_0|^2 = 1; a ray CUT adds exactly one seam
    # difference of the same size, so the truncated profile has E = 2.  This is precisely the
    # numerics lane's D10 warning that the energy completion is not computable on a finite cut.
    chk(abs(gp@E@gp - 2) < 1e-8, "T1(c): truncated wandering profile has E = 1 + 1 seam = 2")
    chk(np.linalg.norm(gp) > 20, "T1(c): ... and it is NOT in l^2 (norm grows with the cut)")

print("="*78); print("N.  T3-T6: the renewal channel on the model space")
print("="*78)
def model(zs):
    zs = np.array(zs, complex); N = len(zs)
    G = 1.0/(1-np.conj(zs)[:,None]*zs[None,:])
    ev, U = np.linalg.eigh(G)
    Gs = U@np.diag(np.sqrt(ev))@U.conj().T; Gis = U@np.diag(1/np.sqrt(ev))@U.conj().T
    D = np.diag(zs); C = Gs@D@Gis; j = Gis@np.ones(N)
    return C, j, zs, Gs, Gis, G
def vec(X): return X.reshape(-1, order='F')
def unvec(v, N): return v.reshape((N,N), order='F')

MODZ = [("loop a=1 c2=0.5", split(np.array([[1.0]]),0.5)[0]),
        ("2v t=1",          split(np.array([[0.0,1.0],[1.0,0.0]]),0.5)[0]),
        ("random 3v",       split(np.array([[-0.3,0.15,-0.4],[0.15,-0.1,-0.1],[-0.4,-0.1,-0.4]]),0.6)[0]),
        ("2v T7a",          split(np.array([[0.4,np.sqrt(51)/5],[np.sqrt(51)/5,0.1]]),2.5)[0])]
for tag, zs in MODZ:
    if len(zs) < 2: continue
    C, j, zsa, Gs, Gis, G = model(zs); N = len(zs)
    E0 = np.kron(np.conj(C), C)
    for trial in range(4):
        A = rng.normal(size=(N,N)) + 1j*rng.normal(size=(N,N)); Om = A@A.conj().T; Om /= np.trace(Om).real
        J = np.outer(j, j.conj())
        Ech = E0 + np.outer(vec(Om), vec(J).conj())
        # (T3a) CPTP: Choi positivity and trace preservation
        Kraus = [C] + [np.sqrt(max(p,0))*np.outer(v, j.conj())
                       for p, v in zip(*[np.linalg.eigh(Om)[0], np.linalg.eigh(Om)[1].T])]
        S = sum(K.conj().T@K for K in Kraus)
        chk(np.max(np.abs(S - np.eye(N))) < 1e-9, f"{tag}: Kraus sum = I (CPTP)")
        Choi = sum(np.outer(vec(K), vec(K).conj()) for K in Kraus)
        chk(np.min(np.linalg.eigvalsh(Choi)) > -1e-10, f"{tag}: Choi matrix is PSD")
        # (T3b) holding law telescopes, mean = sum s_m
        s = [np.trace(np.linalg.matrix_power(C,m)@Om@np.linalg.matrix_power(C,m).conj().T).real
             for m in range(0, 4000)]
        mm = [s[m-1]-s[m] for m in range(1, 4000)]
        chk(min(mm) > -1e-12 and abs(sum(mm)-1) < 1e-9, f"{tag}: holding law >= 0 and sums to 1")
        mu = sum(s)
        chk(abs(sum(m*mm[m-1] for m in range(1,4000)) - mu) < 1e-6, f"{tag}: mu = sum_m s_m")
        Sm = unvec(np.linalg.solve(np.eye(N*N)-E0, vec(Om)), N)
        chk(abs(np.trace(Sm).real - mu) < 1e-6, f"{tag}: (I-E0)^-1 Omega has trace mu")
        rho = Sm/np.trace(Sm)
        chk(np.max(np.abs(unvec(Ech@vec(rho), N) - rho)) < 1e-10, f"{tag}: rho_inf stationary")
        # uniqueness: dim ker(I - E) = 1
        sv = np.linalg.svd(np.eye(N*N)-Ech, compute_uv=False)
        chk(sum(1 for x in sv if x < 1e-9) == 1, f"{tag}: stationary density unique (dim ker = 1)")
        # attraction
        B0 = rng.normal(size=(N,N))+1j*rng.normal(size=(N,N)); r0 = B0@B0.conj().T; r0/=np.trace(r0).real
        v0 = vec(r0)
        for _ in range(40000): v0 = Ech@v0
        chk(np.max(np.abs(unvec(v0,N)-rho)) < 1e-8, f"{tag}: aperiodic => global attraction")
        # (T3e) secular determinant identity
        for u in [0.23+0.19j, -0.4+0.5j, 0.8]:
            mh = u*vec(J).conj()@np.linalg.solve(np.eye(N*N)-u*E0, vec(Om))
            chk(abs(np.linalg.det(np.eye(N*N)-u*Ech) - np.linalg.det(np.eye(N*N)-u*E0)*(1-mh)) < 1e-9,
                f"{tag}: det(I-uE) = det(I-uE0)(1-mhat(u))")
            chk(abs(mh - sum(mm[m-1]*u**m for m in range(1,3000))) < 1e-8, f"{tag}: mhat(u) = sum m(m) u^m")
    # (T4) modal rebound
    zsl = np.array(zs, complex)
    e = Gis@np.linalg.inv(Gis)   # identity; build normalised eigenvectors of C explicitly
    evals, evecs = np.linalg.eig(C)
    order = [int(np.argmin(np.abs(evals - z))) for z in zsl]
    Vv = evecs[:, order]; Vv = Vv/np.linalg.norm(Vv, axis=0)
    p = rng.random(N); p /= p.sum()
    Om = sum(p[i]*np.outer(Vv[:,i], Vv[:,i].conj()) for i in range(N))
    mu_pred = sum(p[i]/(1-abs(zsl[i])**2) for i in range(N))
    s = [np.trace(np.linalg.matrix_power(C,m)@Om@np.linalg.matrix_power(C,m).conj().T).real for m in range(20000)]
    chk(abs(sum(s)-mu_pred) < 1e-5, f"{tag}: (4.1) mu_Omega = sum p_i/(1-|z_i|^2)")
    Sm = unvec(np.linalg.solve(np.eye(N*N)-np.kron(np.conj(C),C), vec(Om)), N); rho = Sm/np.trace(Sm)
    pred = sum(p[i]/(1-abs(zsl[i])**2)*np.outer(Vv[:,i],Vv[:,i].conj()) for i in range(N))/mu_pred
    chk(np.max(np.abs(rho-pred)) < 1e-9, f"{tag}: (4.1) rho_inf modal formula")
    uni = (np.max(np.abs(np.abs(zsl)-abs(zsl[0]))) < 1e-9)
    chk((np.max(np.abs(rho-Om)) < 1e-9) == uni, f"{tag}: rho_inf = Omega iff all |z_i| equal ({uni})")
    if uni:
        chk(abs(mu_pred - 1/(1-abs(zsl[0])**2)) < 1e-9, f"{tag}: uniform modulus => mu = 1/(1-r^2)")
    # (T4c) Gram spectrum, not the weight list
    Oij = Vv.conj().T@Vv; wgt = np.array([p[i]/((1-abs(zsl[i])**2)*mu_pred) for i in range(N)])
    sp1 = np.sort(np.linalg.eigvalsh(rho))[-N:]
    sp2 = np.sort(np.linalg.eigvalsh(np.diag(np.sqrt(wgt))@Oij@np.diag(np.sqrt(wgt))).real)
    chk(np.max(np.abs(sp1-sp2)) < 1e-9, f"{tag}: density spectrum = Gram spectrum")
    chk(np.max(np.abs(np.sort(wgt)-sp1)) > 1e-6, f"{tag}: ... and NOT the weight list")
    # (T5) admissibility, flags, Schur form
    for _ in range(50):
        Bq = rng.normal(size=(N,N))+1j*rng.normal(size=(N,N)); sig = Bq@Bq.conj().T; sig/=np.trace(sig).real
        Q = sig - C@sig@C.conj().T
        chk(abs(np.trace(Q).real - (j.conj()@sig@j).real) < 1e-10, f"{tag}: Tr Q_sigma = <j,sigma j>")
    Qm = min(np.min(np.linalg.eigvalsh(sig - C@sig@C.conj().T)) for sig in
             [ (lambda M: M/np.trace(M).real)(Bq@Bq.conj().T) for Bq in
               [rng.normal(size=(N,N))+1j*rng.normal(size=(N,N)) for _ in range(30)] ])
    chk(Qm < 0, f"{tag}: a random density generally FAILS Q_sigma >= 0 (min eig {Qm:.4f})")
    # Schur triangularisation flag (works without a diagonalisable C)
    Tq, Zq = __import__('scipy.linalg', fromlist=['schur']).schur(C, output='complex')
    ps = np.sort(rng.random(N))[::-1]; ps /= ps.sum(); psx = np.append(ps, 0.0)
    sig = sum((psx[k]-psx[k+1])*(Zq[:, :k+1]@Zq[:, :k+1].conj().T) for k in range(N))
    Q = sig - C@sig@C.conj().T
    chk(np.min(np.linalg.eigvalsh(Q)) > -1e-10, f"{tag}: flag sigma is admissible (Q >= 0)")
    chk(np.max(np.abs(np.sort(np.linalg.eigvalsh(sig))[::-1] - ps)) < 1e-9,
        f"{tag}: flag sigma has EXACTLY the prescribed spectrum")
    Omf = Q/np.trace(Q).real
    Ef = np.kron(np.conj(C),C) + np.outer(vec(Omf), vec(np.outer(j,j.conj())).conj())
    chk(np.max(np.abs(unvec(Ef@vec(sig),N)-sig)) < 1e-9, f"{tag}: flag sigma is stationary for its own Omega")
    # (5.2) coefficient/Schur form in the resonance basis
    Vk = np.linalg.inv(Gis)                      # columns are the kernels in the orthonormal basis
    Am = rng.random((N,N)); Am = Am@Am.T
    sig2 = Vk@Am@Vk.conj().T
    Q2 = sig2 - C@sig2@C.conj().T
    coef = Am*(1-np.outer(zsl, np.conj(zsl)))
    chk(np.max(np.abs(Q2 - Vk@coef@Vk.conj().T)) < 1e-8, f"{tag}: (5.2) Q_sigma coefficient matrix A_ij(1-z_i conj z_j)")
    chk(abs(np.trace(sig2).real - np.trace(Am@G).real) < 1e-9, f"{tag}: Tr sigma = Tr(A G)")
    chk(abs(np.trace(Q2).real - np.real(np.ones(N)@Am@np.ones(N))) < 1e-8, f"{tag}: Tr Q = 1^* A 1")
    # (T6a) odd coherences
    Ct = np.block([[np.ones((1,1)), np.zeros((1,N))],[np.zeros((N,1)), C]])
    jt = np.concatenate([[0.0], j])
    Bq = rng.normal(size=(N+1,N+1))+1j*rng.normal(size=(N+1,N+1)); Omt = Bq@Bq.conj().T; Omt/=np.trace(Omt).real
    for i in range(N):
        X = np.zeros((N+1,N+1), complex); X[1:,0] = Vv[:,i]
        Y = Ct@X@Ct.conj().T + (jt.conj()@X@jt)*Omt
        chk(np.max(np.abs(Y - zsl[i]*X)) < 1e-9, f"{tag}: odd |k_i><vac| is an eigen-operator with eigenvalue z_i")

print("="*78); print("O.  T3(c): uniqueness under periodicity, and the +- i r example")
print("="*78)
for r in [0.7, 0.35]:
    C = np.array([[0,1],[-r*r,0]], complex); jv = np.array([math.sqrt(1-r**4), 0.0])
    chk(np.max(np.abs(np.eye(2)-C.conj().T@C-np.outer(jv,jv))) < 1e-12, f"r={r}: I - C^*C = jj^*")
    chk(np.max(np.abs(np.sort_complex(np.linalg.eigvals(C)) - np.sort_complex(np.array([1j*r,-1j*r])))) < 1e-12,
        f"r={r}: eigenvalues +- i r (NON-REAL resonances)")
    Om = np.diag([0.0,1.0]).astype(complex)
    mmv = [float(np.real(jv@np.linalg.matrix_power(C,m-1)@Om@np.linalg.matrix_power(C,m-1).conj().T@jv))
           for m in range(1, 9)]
    chk(all(abs(mmv[k]) < 1e-14 for k in range(0,8,2)), f"r={r}: m(odd) = 0 -> gcd = 2, PERIODIC")
    chk(abs(mmv[1]-(1-r**4)) < 1e-12 and abs(mmv[3]-(1-r**4)*r**4) < 1e-12, f"r={r}: m(2k) = (1-r^4) r^(4(k-1))")
    E0 = np.kron(np.conj(C),C); Ech = E0 + np.outer(vec(Om), vec(np.outer(jv,jv)).conj())
    sv = np.linalg.svd(np.eye(4)-Ech, compute_uv=False)
    chk(sum(1 for x in sv if x<1e-10) == 1, f"r={r}: stationary density STILL UNIQUE despite periodicity")
    Sm = unvec(np.linalg.solve(np.eye(4)-E0, vec(Om)),2); rho = Sm/np.trace(Sm)
    chk(np.max(np.abs(rho-np.eye(2)/2)) < 1e-12, f"r={r}: rho_inf = I/2")
    per = [x for x in np.linalg.eigvals(Ech) if abs(abs(x)-1) < 1e-9]
    chk(len(per) == 2 and abs(sorted(per, key=lambda t: t.real)[0]+1) < 1e-9,
        f"r={r}: peripheral spectrum = the 2nd roots of unity, each simple")
    v0 = vec(np.diag([0.9,0.1]).astype(complex))
    it = [unvec(v0,2).copy()]
    for _ in range(50): v0 = Ech@v0
    chk(np.max(np.abs(unvec(v0,2)-rho)) > 1e-3, f"r={r}: ... and attraction of every density FAILS")
    # the periodic example is REALISED by a graph core: a=0, c^2 = 1-r^2
    res, beta = split(np.array([[0.0]]), 1-r*r)
    chk(len(res)==2 and all(abs(abs(z)-r)<1e-12 for z in res) and all(abs(z.real)<1e-12 for z in res),
        f"r={r}: the core T_X=[0], c^2=1-r^2 has exactly the resonances +- i r")
    # modal rebound on the SAME contraction is aperiodic (numerics-lane D14 in its correct scope)
    ev, evec = np.linalg.eig(C); v = evec[:,0]/np.linalg.norm(evec[:,0]); Om2 = np.outer(v, v.conj())
    mm2 = [float(np.real(jv@np.linalg.matrix_power(C,m-1)@Om2@np.linalg.matrix_power(C,m-1).conj().T@jv))
           for m in range(1,9)]
    chk(all(x > 1e-12 for x in mm2), f"r={r}: a MODAL rebound on the same C is aperiodic (m(m)>0 for all m)")
# T3(d) purity
for tag, zs in MODZ:
    if len(zs) < 2: continue
    C, j, zsa, Gs, Gis, G = model(zs); N = len(zs)
    evals, evecs = np.linalg.eig(C)
    v = evecs[:,0]/np.linalg.norm(evecs[:,0]); Om = np.outer(v, v.conj())
    Sm = unvec(np.linalg.solve(np.eye(N*N)-np.kron(np.conj(C),C), vec(Om)), N); rho = Sm/np.trace(Sm)
    chk(abs(np.trace(rho@rho).real - 1) < 1e-9 and np.max(np.abs(rho-Om)) < 1e-9,
        f"{tag}: pure eigenvector rebound => rho_inf = Omega is PURE")
    u = rng.normal(size=N)+1j*rng.normal(size=N); u/=np.linalg.norm(u); Om2 = np.outer(u,u.conj())
    Sm2 = unvec(np.linalg.solve(np.eye(N*N)-np.kron(np.conj(C),C), vec(Om2)), N); rho2 = Sm2/np.trace(Sm2)
    chk(np.trace(rho2@rho2).real < 1-1e-6, f"{tag}: generic pure rebound => rho_inf MIXED")

print("="*78); print("P.  T6(b): the bound state is not a wave vacuum")
print("="*78)
q = 2; TX = np.array([[0.0]]); c = math.sqrt(q+1.0); L = 400
T, n = build_T(TX, c, L); E = Emat(T); W = Wmat(T); N = T.shape[0]; ray = lambda k: n+k-1
for beta in [q**-0.5, -q**-0.5]:
    f = np.zeros(N); f[0] = 1.0
    for k in range(1, L+1): f[ray(k)] = c*beta**k
    f /= np.linalg.norm(f); lam = beta+1/beta
    for t in [beta, 1/beta]:
        dat = np.concatenate([f, f/t])
        chk(np.max(np.abs((W@dat - t*dat)[:N-3])) < 1e-8, f"T6(b): wave data (f, f/t) has W-eigenvalue t={t:+.5f}")
        chk(abs(dat@E@dat) < 1e-8, f"T6(b): that eigen-datum is E-NULL")
    d1 = np.concatenate([f, f/beta]); d2 = np.concatenate([f, f*beta])
    blk = np.array([[d1@E@d1, d1@E@d2],[d2@E@d1, d2@E@d2]])
    chk(np.linalg.det(blk) < -1e-6, f"T6(b): the 2x2 bound-state energy block is HYPERBOLIC (det {np.linalg.det(blk):.4f})")
    chk(abs(abs(beta)-1) > 1e-6, "T6(b): |t| != 1 => no positive-definite W-invariant form on that block")

print("="*78)
print(f"CHECKS PASSED: {OK}   FAILURES: {len(FAIL)}")
for f_ in FAIL[:40]: print("  FAIL:", f_)
print("="*78)
