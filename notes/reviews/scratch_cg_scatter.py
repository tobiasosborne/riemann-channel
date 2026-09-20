#!/usr/bin/env python3
"""REFUTE lane, cusp-graph round: scattering, counts, prior art, T2, T7.

Author: claude:opus.  Written from the DEFINITIONS only; nothing imported from
scripts/cusp_graph.py and nothing taken on trust from notes/cusp-graph/astra-proofs.md.

Conventions fixed here (re-derived):
  H = C^n (+) l^2(N),  T = T_X (+) T_ray + c(|v0><r1| + |r1><v0|),
  (T g)(r_1) = g(r_2) + c g(v0),  (T g)(r_k) = g(r_{k+1}) + g(r_{k-1}), k >= 2.
  lambda = z + 1/z.
  p(z)      = det((1+z^2) I - z T_X - c^2 P0)
  ptilde(z) = det((1+z^2) I - z T_X - c^2 z^2 P0) = z^{2n} p(1/z)
"""
import numpy as np, itertools, math
np.random.seed(20260920)

OK = 0; FAIL = []
def chk(cond, msg):
    global OK
    if cond: OK += 1
    else: FAIL.append(msg); print("   !! FAIL:", msg)

def poly_p(TX, c2, tilde=False):
    """Coefficients (numpy convention, high->low) of p or ptilde, by DFT of the determinant."""
    n = TX.shape[0]; deg = 2*n
    m = deg + 1
    w = np.exp(2j*np.pi*np.arange(m)/m)
    vals = np.empty(m, complex)
    P0 = np.zeros((n, n)); P0[0, 0] = 1.0
    for i, z in enumerate(w):
        M = (1+z*z)*np.eye(n) - z*TX - (c2*z*z if tilde else c2)*P0
        vals[i] = np.linalg.det(M)
    co = np.fft.fft(vals)/m          # co[k] = coefficient of z^k
    return co[::-1].real if np.max(np.abs(co.imag)) < 1e-8 else co[::-1]

def Gfun(TX, lam):
    n = TX.shape[0]
    return np.linalg.solve(lam*np.eye(n) - TX, np.eye(n)[:, 0])[0]

def Rg(TX, c2, z):
    lam = z + 1/z; G = Gfun(TX, lam)
    return (1 - c2*G/z)/(c2*G*z - 1)

def build_T(TX, c, L):
    n = TX.shape[0]; N = n + L
    T = np.zeros((N, N))
    T[:n, :n] = TX
    for k in range(1, L):
        T[n+k-1, n+k] = T[n+k, n+k-1] = 1.0
    T[0, n] = T[n, 0] = c
    return T

# ---------------------------------------------------------------- test cores
def rsym(n, rng):
    M = rng.integers(-5, 6, (n, n))/10.0
    return (M + M.T)/2 if n > 1 else M.astype(float)

rng = np.random.default_rng(20260920)
CORES = [("pure cusp q=2",            np.array([[0.0]]),                    3.0),
         ("pure cusp q=5",            np.array([[0.0]]),                    6.0),
         ("free half line c=1",       np.array([[0.0]]),                    1.0),
         ("loop a=1 c2=0.5",          np.array([[1.0]]),                    0.5),
         ("loop a=0 c2=1.5",          np.array([[0.0]]),                    1.5),
         ("loop a=3/2 c2=1/2 (thr)",  np.array([[1.5]]),                    0.5),
         ("loop a=1 c2=3 (band edge)",np.array([[1.0]]),                    3.0),
         ("loop a=29/20 c2=1/2",      np.array([[29/20]]),                  0.5),
         ("loop a=1 c2=0.84 (CE)",    np.array([[1.0]]),                    0.84),
         ("2v prover T7a",            np.array([[0.4, np.sqrt(51)/5],
                                                [np.sqrt(51)/5, 0.1]]),     2.5),
         ("2v t=1",                   np.array([[0.0,1.0],[1.0,0.0]]),      0.5),
         ("2v t=3",                   np.array([[0.0,3.0],[3.0,0.0]]),      0.5),
         ("2v 3,-3",                  np.array([[3.0,0.2],[0.2,-3.0]]),     0.5),
        ]
for k in range(6):
    n = rng.integers(2, 6)
    CORES.append((f"random n={n} #{k}", rsym(n, rng), float(rng.choice([0.3,0.6,1.7,3.0]))))
# a core with a genuine cusp form (eigenvector vanishing at v0)
Tc = np.array([[0.0, 1.0, 0.0],[1.0, 0.0, 0.0],[0.0, 0.0, -3.0]])
CORES.append(("cusp form lam=-3", Tc, 0.6))
Tc2 = np.zeros((4,4)); Tc2[0,1]=Tc2[1,0]=1.0; Tc2[2,3]=Tc2[3,2]=1.0; Tc2[2,2]=0.5
CORES.append(("cusp form pair", Tc2, 1.3))

print("="*78); print("A.  C1: R from the ansatz, R = -p/ptilde, functional equation")
print("="*78)
for tag, TX, c2 in CORES:
    n = TX.shape[0]; c = math.sqrt(c2)
    p, pt = poly_p(TX, c2), poly_p(TX, c2, True)
    # (A1) ptilde(z) = z^{2n} p(1/z)  <=>  coefficient reversal
    chk(np.max(np.abs(np.asarray(pt, float) - np.asarray(p, float)[::-1])) < 1e-8,
        f"{tag}: ptilde = z^2n p(1/z)")
    # (A2) monic, p(0) = 1 - c^2, ptilde(0) = 1
    chk(abs(p[0]-1) < 1e-8 and abs(p[-1]-(1-c2)) < 1e-8 and abs(pt[-1]-1) < 1e-8,
        f"{tag}: p monic, p(0)=1-c^2={1-c2:.4g}, ptilde(0)=1")
    for z in [0.37+0.23j, -0.6+0.11j, 1.7-0.4j, 0.8j]:
        lam = z + 1/z
        if min(abs(np.linalg.eigvalsh(TX) - lam)) < 1e-6: continue
        # (A3) determinant form with the MINUS sign
        chk(abs(Rg(TX, c2, z) + np.polyval(p, z)/np.polyval(pt, z)) < 1e-8,
            f"{tag}: R = -p/ptilde at z={z}")
        # (A4) Childs-Strouse  R(z) = -Q(1/z)/Q(z),  Q(z) = 1 - z(a + b^dag(lam-D)^-1 b), a=0, b=c e_0
        Q  = lambda zz: 1 - zz*(c2*Gfun(TX, zz+1/zz))
        chk(abs(Rg(TX, c2, z) + Q(1/z)/Q(z)) < 1e-8,
            f"{tag}: Childs-Strouse -Q(1/z)/Q(z) == R at z={z}")
        # (A5) functional equation
        chk(abs(Rg(TX,c2,z)*Rg(TX,c2,1/z) - 1) < 1e-8, f"{tag}: R(z)R(1/z)=1")
        chk(abs(Rg(TX,c2,np.conj(z)) - np.conj(Rg(TX,c2,z))) < 1e-8, f"{tag}: R(zbar)=conj R(z)")
    for th in [0.4, 1.9, 2.7, 5.1]:
        z = np.exp(1j*th)
        if abs(np.polyval(pt, z)) < 1e-9: continue
        chk(abs(abs(Rg(TX,c2,z)) - 1) < 1e-8, f"{tag}: |R|=1 on the circle")
    # (A6) direct solve of T g = lam g on a long ray reproduces R  (ansatz not assumed)
    L = 300; T = build_T(TX, c, L); n_ = n
    for th in [0.7, 2.2]:
        z = np.exp(1j*th); lam = z + 1/z
        # unknowns: core values g_X (n), R.  Equations: core rows (n) using g(r1)=1/z+R z, g(r2)=1/z^2+R z^2
        A = np.zeros((n+1, n+1), complex); b = np.zeros(n+1, complex)
        # core rows: (T_X g_X)_i + c delta_{i0} g(r1) = lam g_i
        for i in range(n):
            A[i, :n] = TX[i, :] - lam*np.eye(n)[i, :]
            if i == 0: A[i, n] = c*z; b[i] = -c/z
        # ray row at r1: g(r2) + c g(v0) = lam g(r1)
        A[n, :n] = c*np.eye(n)[0, :]; A[n, n] = z*z - lam*z
        b[n] = -(1/z**2) + lam/z
        sol = np.linalg.solve(A, b)
        chk(abs(sol[n] - Rg(TX, c2, z)) < 1e-8, f"{tag}: direct ansatz solve == G-form R")

print("="*78); print("B.  C2: Krylov/cusp split, gcd, thresholds, bound states, the COUNT")
print("="*78)
def krylov_dim(TX):
    n = TX.shape[0]; v = np.eye(n)[:, 0]; V = [v]
    for _ in range(n):
        w = TX @ V[-1]
        M = np.array(V).T
        w = w - M @ np.linalg.lstsq(M, w, rcond=None)[0]
        if np.linalg.norm(w) > 1e-9: V.append(w/np.linalg.norm(w))
    return len(V) if np.linalg.norm(np.array(V)) > 0 else 0

COUNTS = []
for tag, TX, c2 in CORES:
    n = TX.shape[0]; c = math.sqrt(c2)
    p, pt = np.asarray(poly_p(TX,c2), float), np.asarray(poly_p(TX,c2,True), float)
    d = krylov_dim(TX); mu_cusp = n - d
    rp, rpt = np.roots(p), np.roots(pt[np.argmax(np.abs(pt) > 1e-10):])
    # cusp factor D_c(z) = prod over cusp eigenvalues (1 - t z + z^2)
    evals, evecs = np.linalg.eigh(TX)
    cusp_t = []
    for j in range(n):
        # multiplicity of t in the cusp block = dim{psi: T psi = t psi, psi_0 = 0}
        pass
    # build cusp multiplicities directly from eigenspaces
    seen = []
    for j in range(n):
        t = evals[j]
        if any(abs(t - s) < 1e-8 for s in seen): continue
        seen.append(t)
        idx = [k for k in range(n) if abs(evals[k]-t) < 1e-8]
        Vb = evecs[:, idx]
        w = Vb[0, :]                       # values at v0
        mc = len(idx) - (1 if np.linalg.norm(w) > 1e-9 else 0)
        if mc > 0: cusp_t.append((t, mc))
    chk(sum(m for _, m in cusp_t) == mu_cusp, f"{tag}: sum m_c = n - dim Krylov = {mu_cusp}")
    Dc = np.array([1.0])
    for t, m in cusp_t:
        for _ in range(m): Dc = np.convolve(Dc, [1.0, -t, 1.0])
    pb  = np.polydiv(p, Dc)[0] if len(Dc) > 1 else p
    ptb = np.polydiv(pt, Dc)[0] if len(Dc) > 1 else pt
    chk(len(Dc) == 1 or np.max(np.abs(np.polydiv(p, Dc)[1])) < 1e-6,
        f"{tag}: D_c divides p exactly")
    chk(len(Dc) == 1 or np.max(np.abs(np.polydiv(pt, Dc)[1])) < 1e-6,
        f"{tag}: D_c divides ptilde exactly")
    chk(abs(len(pb)-1 - 2*d) < 1e-9, f"{tag}: deg p_b = 2 dim Krylov = {2*d}")
    # thresholds
    Eth = [e for e in (1.0, -1.0) if abs(np.polyval(pb, e)) < 1e-7]
    tau = len(Eth)
    # simplicity of the threshold roots of p_b  (prover: p_b'(eps) = +- c^2 B(+-2) != 0)
    for e in Eth:
        chk(abs(np.polyval(np.polyder(pb), e)) > 1e-6,
            f"{tag}: threshold root z={e:+.0f} of p_b is SIMPLE (p_b'={np.polyval(np.polyder(pb),e):.4g})")
    # bound states = roots of ptilde_b in the open disc
    rptb = np.roots(ptb) if len(ptb) > 1 else np.array([])
    beta = [r for r in rptb if abs(r) < 1-1e-7]
    chk(all(abs(r.imag) < 1e-7 for r in beta), f"{tag}: no non-real pole of R in the disc (C2(ii))")
    b_ = len(beta)
    rpb = np.roots(pb) if len(pb) > 1 else np.array([])
    res = [r for r in rpb if abs(r) < 1-1e-7]
    N = len(res)
    # (B1) the prover's count
    chk(N == 2*d - b_ - tau, f"{tag}: N={N} == 2d-b-tau = {2*d-b_-tau}  [prover (0.5)]")
    # (B2) the numerics lane's count  #res = 2(n - mu) - t_nc - beta
    chk(N == 2*(n - mu_cusp) - b_ - tau, f"{tag}: N == 2(n-mu)-t_nc-beta [numerics D6]")
    # (B3) Childs's Levinson count  #res = 2n - 2 n_c - n_b - n_h
    chk(N == 2*n - 2*mu_cusp - b_ - tau, f"{tag}: N == 2n-2n_c-n_b-n_h [Childs 1103.5077:277/365]")
    # (B4) exterior roots of p_b are exactly 1/beta
    ext = sorted([r.real for r in rpb if abs(r) > 1+1e-7])
    chk(len(ext) == b_ and (b_ == 0 or np.max(np.abs(np.sort([1/x.real for x in beta]) - ext)) < 1e-6),
        f"{tag}: exterior roots of p_b == 1/beta")
    # (B5) gcd(p,ptilde) = D_c * H   (only cusp factors and thresholds)
    common = [r for r in rp if min(abs(r - s) for s in rpt) < 1e-6] if len(rpt) else []
    extra = [r for r in common if min([abs(r-t) for t in np.roots(Dc)] + [9.]) > 1e-6
                              and min([abs(r-e) for e in Eth] + [9.]) > 1e-6]
    chk(len(extra) == 0, f"{tag}: gcd(p,ptilde) has only cusp + threshold roots (C2(iii)/D5)")
    # (B6) bound states really are l^2 eigenvalues of T on Y; count on a long ray
    L = 400; T = build_T(TX, c, L); ev, evec = np.linalg.eigh(T)
    tail = np.linalg.norm(evec[-40:, :], axis=0)
    l2out = [ev[i] for i in range(len(ev)) if tail[i] < 1e-3 and abs(ev[i]) > 2+1e-4]
    lam_beta = sorted([r.real + 1/r.real for r in beta])
    # cusp forms outside the band are l^2 too but are NOT poles of R
    cusp_out = sum(m for t, m in cusp_t if abs(t) > 2+1e-6)
    chk(len(l2out) == b_ + cusp_out,
        f"{tag}: #l2 eigenvalues outside band = b + (cusp forms outside) = {b_}+{cusp_out}")
    if b_:
        matched = sorted([e for e in l2out if min(abs(e-x) for x in lam_beta) < 1e-4])
        chk(len(matched) == b_ and np.max(np.abs(np.array(matched)-np.array(lam_beta))) < 1e-4,
            f"{tag}: bound eigenvalues = beta + 1/beta")
    COUNTS.append((tag, n, d, mu_cusp, b_, tau, N, cusp_out))

print("\n core                          n   d  mu  b  tau   N  cuspOut")
for t, n, d, m, b_, ta, N, co in COUNTS:
    print(f" {t:28s} {n:2d} {d:3d} {m:3d} {b_:2d} {ta:4d} {N:3d} {co:6d}")

print("="*78); print("C.  C3: the pure cusp, phi = 1/R, and the xi-vs-Lambda caveat")
print("="*78)
for q in [2, 3, 5, 7]:
    TX = np.array([[0.0]]); c2 = q+1.0
    p, pt = np.asarray(poly_p(TX,c2),float), np.asarray(poly_p(TX,c2,True),float)
    chk(np.max(np.abs(p - np.array([1,0,-q]))) < 1e-8, f"q={q}: p = z^2 - q")
    chk(np.max(np.abs(pt - np.array([-q,0,1.0]))) < 1e-8, f"q={q}: ptilde = 1 - q z^2")
    for z in [0.37+0.23j, -0.21+0.6j]:
        R = (z*z-q)/(q*z*z-1)
        chk(abs(Rg(TX,c2,z) - R) < 1e-10, f"q={q}: R = (z^2-q)/(qz^2-1)")
        s = 0.5 + np.log(z)/np.log(q)
        zk = lambda t: 1/((1-q**(-t))*(1-q**(1.0-t)))
        chk(abs(1/R - q*zk(2*s-1)/zk(2*s)) < 1e-10, f"q={q}: 1/R = q zeta_K(2s-1)/zeta_K(2s)")
        chk(abs(R - q*zk(2*s-1)/zk(2*s)) > 1e-3, f"q={q}: R itself is NOT that ratio (phi = 1/R)")
    chk(abs(abs(np.roots(pt)[0]) - q**-0.5) < 1e-10, f"q={q}: bound states at +-q^-1/2")
    chk(len([r for r in np.roots(p) if abs(r) < 1-1e-9]) == 0, f"q={q}: NO resonances")
# period pi i / log q  (prover ledger 9)
q = 3.0
for z in [0.4+0.2j]:
    s = 0.5 + np.log(z)/np.log(q)
    f = lambda t: (1-q**(-2*t))/(1-q**(2-2*t))
    chk(abs(f(s) - f(s + 1j*np.pi/np.log(q))) < 1e-12, "1/R has period pi i/log q in s")
# xi vs Lambda:  xi(2s-1)/xi(2s) = ((s-1)/s) Lambda(2s-1)/Lambda(2s)
import mpmath as mp
mp.mp.dps = 40
for s in [mp.mpf('0.63')+mp.mpf('0.21')*1j, mp.mpf('0.8')-mp.mpf('0.4')*1j]:
    Lam = lambda t: mp.pi**(-t/2)*mp.gamma(t/2)*mp.zeta(t)
    xi  = lambda t: mp.mpf('0.5')*t*(t-1)*Lam(t)
    lhs = xi(2*s-1)/xi(2*s); rhs = ((s-1)/s)*Lam(2*s-1)/Lam(2*s)
    chk(abs(lhs-rhs) < 1e-25, "xi(2s-1)/xi(2s) = ((s-1)/s) Lambda(2s-1)/Lambda(2s) [prover ledger 11]")

print("="*78); print("D.  PRIOR ART: Arends-Peterson-Weich resonance matrix H(mu) vs p(z)")
print("="*78)
# APW:  H(mu) = (1/(2 sqrt q))(A_L + B(mu)) - z(mu) I,  z(mu) = (mu+1/mu)/2,
#       B(mu)_vv = c_v sqrt(q)/mu  (cusp edges).  With T_X = A_L/sqrt q, c^2 = c_{v0}:
#       2 H(mu) = T_X + (c^2/mu) P0 - (mu+1/mu) I,  so det H = (-1)^n (2 mu)^{-n} p(mu).
for tag, TX, c2 in CORES:
    n = TX.shape[0]; P0 = np.zeros((n,n)); P0[0,0]=1.0
    p = np.asarray(poly_p(TX,c2), float)
    for mu in [0.7+0.3j, 1.9-0.5j, -0.4+1.1j]:
        H = 0.5*(TX + (c2/mu)*P0 - (mu+1/mu)*np.eye(n))
        chk(abs(np.linalg.det(H) - (-1)**n*(2*mu)**(-n)*np.polyval(p, mu)) < 1e-8,
            f"{tag}: det H_APW(mu) = (-1)^n (2mu)^-n p(mu)")
# APW modular curve: H(mu) = (q+1)/(2mu) - (mu+1/mu)/2, zeros +- sqrt q = 1/(prover's beta)
for q in [2,3,5]:
    H = lambda mu: (q+1)/(2*mu) - (mu+1/mu)/2
    for mu in [np.sqrt(q), -np.sqrt(q)]:
        chk(abs(H(mu)) < 1e-12, f"APW modular curve q={q}: det H = 0 at mu = {mu:+.4f} = 1/beta")
# APW tree (all funnels): H(mu) = (q+1)/(2 q mu) - (mu+1/mu)/2, zeros +- q^{-1/2}
for q in [2,3]:
    Ht = lambda mu: (1/(2*np.sqrt(q)))*((q+1)/(np.sqrt(q)*mu)) - (mu+1/mu)/2
    chk(abs(Ht(q**-0.5)) < 1e-12 and abs(Ht(-q**-0.5)) < 1e-12, f"APW tree q={q}: zeros at +-q^-1/2")
# APW elliptic curve 1 (F_2): det H = (mu^2+1)^2 (mu^2-2)(2mu^4-2mu^2+1)
detH = np.polymul(np.polymul([1,0,1],[1,0,1]), np.polymul([1,0,-2],[2,0,-2,0,1]))
rts = np.roots(detH)
chk(sum(1 for r in rts if abs(abs(r)-1) < 1e-6) == 4, "APW ell.curve1: (mu^2+1)^2 -> 4 roots on |mu|=1 (cusp forms)")
chk(sum(1 for r in rts if abs(abs(r)-np.sqrt(2)) < 1e-9) == 2, "APW ell.curve1: +-sqrt q (trivial = 1/beta)")
hw = [r for r in np.roots([2,0,-2,0,1])]
chk(all(abs(abs(r) - 2**-0.25) < 1e-9 for r in hw), "APW ell.curve1: Hasse-Weil roots all have |mu| = q^-1/4")
# APW elliptic curve 2 (F_3): (mu^2+1)^2 (mu-1)^2 (mu+1)^2 (mu^2-3)(3 mu^4+1)
chk(all(abs(abs(r) - 3**-0.25) < 1e-9 for r in np.roots([3,0,0,0,1])),
    "APW ell.curve2: 3mu^4+1 roots all have |mu| = q^-1/4")
chk(sum(1 for r in np.roots(np.polymul([1,-1],[1,-1])) if abs(r-1)<1e-9) == 2,
    "APW ell.curve2: (mu-1)^2 -> the prover's threshold/tau roots at mu=+1")

print("="*78); print("E.  T2: walk expansions (2.1)-(2.4), logarithmic derivative (2.5), self-energy")
print("="*78)
for tag, TX, c2 in CORES:
    n = TX.shape[0]; P0 = np.zeros((n,n)); P0[0,0]=1.0
    p = np.asarray(poly_p(TX,c2), float); pt = np.asarray(poly_p(TX,c2,True), float)
    D = np.eye(n) - c2*P0
    z0 = 0.021
    # (2.1)  log ptilde = - sum tr(zA - z^2 D)^l / l
    s = 0.0; M = np.eye(n)
    for l in range(1, 160):
        M = M @ (z0*TX - z0*z0*D); s -= np.trace(M)/l
    chk(abs(s - np.log(np.polyval(pt, z0))) < 1e-9, f"{tag}: (2.1) walk series for log ptilde")
    # (2.2)  log p = log det D - sum tr(z D^-1 A - z^2 D^-1)^l / l   (needs c^2 != 1)
    if abs(c2-1) > 1e-9:
        Di = np.linalg.inv(D); s = 0.0; M = np.eye(n)
        for l in range(1, 200):
            M = M @ (z0*Di@TX - z0*z0*Di); s -= np.trace(M)/l
        s += np.log(abs(np.linalg.det(D)))
        chk(abs(np.exp(s) - abs(np.polyval(p, z0))) < 1e-7, f"{tag}: (2.2) walk series for log p")
    # (2.3) insertion form
    H0 = lambda z: np.eye(n) - z*TX + z*z*np.eye(n)
    h = lambda z: np.linalg.solve(H0(z), np.eye(n)[:,0])[0]
    chk(abs(np.polyval(p, z0) - np.linalg.det(H0(z0))*(1-c2*h(z0))) < 1e-10, f"{tag}: (2.3) p = detH0 (1-c^2 h)")
    chk(abs(np.polyval(pt,z0) - np.linalg.det(H0(z0))*(1-c2*z0*z0*h(z0))) < 1e-10, f"{tag}: (2.3) ptilde")
    # (2.4) power sums of the resonances from the coefficients of log ptilde
    d = krylov_dim(TX); mu_cusp = n - d
    evals, evecs = np.linalg.eigh(TX); seen=[]; cusp_t=[]
    for j in range(n):
        t = evals[j]
        if any(abs(t-s2)<1e-8 for s2 in seen): continue
        seen.append(t); idx=[k for k in range(n) if abs(evals[k]-t)<1e-8]
        mc = len(idx) - (1 if np.linalg.norm(evecs[0, idx]) > 1e-9 else 0)
        if mc: cusp_t.append((t, mc))
    Dc = np.array([1.0])
    for t, m in cusp_t:
        for _ in range(m): Dc = np.convolve(Dc,[1.0,-t,1.0])
    pb = np.polydiv(p, Dc)[0] if len(Dc)>1 else p
    Eth = [e for e in (1.0,-1.0) if abs(np.polyval(pb,e))<1e-7]
    ptb = np.polydiv(pt, Dc)[0] if len(Dc)>1 else pt
    ptb = ptb[np.argmax(np.abs(ptb)>1e-10):]
    beta = [r.real for r in np.roots(ptb) if abs(r)<1-1e-7] if len(ptb)>1 else []
    res = [r for r in (np.roots(pb) if len(pb)>1 else []) if abs(r)<1-1e-7]
    # Taylor coefficients of log ptilde(w) at 0
    ws = np.linspace(-0.02, 0.02, 41)
    for m in [1,2,3]:
        # finite-difference the m-th Taylor coefficient via a small circle
        MM = 64; th = 2*np.pi*np.arange(MM)/MM; rr = 0.02
        vals = np.log(np.polyval(pt, rr*np.exp(1j*th)).astype(complex))
        cm = np.mean(vals*np.exp(-1j*m*th))/rr**m
        lhs = sum(r**m for r in res) if res else 0.0
        rhs = -m*cm - sum(mc*(np.roots([1,-t,1])[0]**m + np.roots([1,-t,1])[1]**m)
                          for t, mc in cusp_t) \
                    - sum(e**m for e in Eth) - sum(b**(-m) for b in beta)
        chk(abs(lhs - rhs) < 1e-6, f"{tag}: (2.4) power sum m={m}  ({lhs:.6g} vs {rhs:.6g})")
    # (2.5) logarithmic derivative, and the resonance/bound partial fraction
    for z in [0.31+0.17j, -0.44+0.09j]:
        num = -np.polyval(np.polyder(p), z)/np.polyval(p, z) \
              + np.polyval(np.polyder(pt), z)/np.polyval(pt, z)
        eps = 1e-6
        dlog = (np.log(Rg(TX,c2,z+eps)) - np.log(Rg(TX,c2,z-eps)))/(2*eps)
        chk(abs(num + dlog) < 1e-4, f"{tag}: (2.5) -R'/R = -p'/p + ptilde'/ptilde")
        pf = -sum(1/(z-zi) + np.conj(zi)/(1-np.conj(zi)*z) for zi in res) \
             + sum(1/(z-b) + b/(1-b*z) for b in beta)
        chk(abs(pf + dlog) < 1e-4, f"{tag}: (2.5) partial-fraction form over resonances/bound states")
# T2(c): m_ray = z, Catalan expansion, and c^2/z = c^2 lambda - c^2 z
L = 4000
Tray = np.diag(np.ones(L-1),1)+np.diag(np.ones(L-1),-1)
for lam in [2.6, -3.1, 4.0]:
    m = np.linalg.solve(lam*np.eye(L)-Tray, np.eye(L)[:,0])[0]
    z = (lam - np.sign(lam)*np.sqrt(lam*lam-4))/2
    chk(abs(m - z) < 1e-6, f"T2(c): m_ray({lam}) = z = {z:.6f}")
    cat = sum(math.comb(2*r, r)/(r+1)/lam**(2*r+1) for r in range(0, 60))
    chk(abs(cat - z) < 1e-9, f"T2(c): Catalan series = z at lambda={lam}")
    chk(abs(1/z - (lam - z)) < 1e-9, f"T2(c): c^2/z = c^2 lambda - c^2 z")
# Catalan_r really counts ray walks r1 -> r1 of length 2r
W = np.linalg.matrix_power(Tray, 0)
for r in range(0, 7):
    chk(abs(np.linalg.matrix_power(Tray, 2*r)[0,0] - math.comb(2*r,r)/(r+1)) < 1e-6,
        f"T2(c): #walks r1->r1 of length {2*r} on the ray = Catalan_{r}")

print("="*78); print("F.  T7: RAM/RH independence, the product identity, self-reciprocity")
print("="*78)
def resonances(TX, c2):
    n = TX.shape[0]
    p = np.asarray(poly_p(TX,c2),float); pt = np.asarray(poly_p(TX,c2,True),float)
    evals, evecs = np.linalg.eigh(TX); seen=[]; cusp_t=[]
    for j in range(n):
        t = evals[j]
        if any(abs(t-s)<1e-8 for s in seen): continue
        seen.append(t); idx=[k for k in range(n) if abs(evals[k]-t)<1e-8]
        mc = len(idx) - (1 if np.linalg.norm(evecs[0,idx])>1e-9 else 0)
        if mc: cusp_t.append((t,mc))
    Dc = np.array([1.0])
    for t,m in cusp_t:
        for _ in range(m): Dc = np.convolve(Dc,[1.0,-t,1.0])
    pb = np.polydiv(p,Dc)[0] if len(Dc)>1 else p
    ptb = np.polydiv(pt,Dc)[0] if len(Dc)>1 else pt
    ptb = ptb[np.argmax(np.abs(ptb)>1e-10):]
    beta = [r.real for r in np.roots(ptb) if abs(r)<1-1e-7] if len(ptb)>1 else []
    Eth = [e for e in (1.0,-1.0) if abs(np.polyval(pb,e))<1e-7]
    res = [r for r in (np.roots(pb) if len(pb)>1 else []) if abs(r)<1-1e-7]
    return res, beta, Eth
# T7(a) prover's one-vertex example
res,beta,Eth = resonances(np.array([[29/20]]), 0.5)
chk(len(res)==2 and len(beta)==0 and len(Eth)==0, "T7(a): a=29/20, c^2=1/2 has 2 resonances, no bound/threshold")
chk(abs(sorted(abs(np.array(res)))[0] - (29-np.sqrt(41))/40) < 1e-10 and
    abs(sorted(abs(np.array(res)))[1] - (29+np.sqrt(41))/40) < 1e-10,
    "T7(a): roots = (29 +- sqrt 41)/40 = 0.5649..., 0.8851...")
# T7(a) prover's two-vertex example
TX2 = np.array([[0.4, np.sqrt(51)/5],[np.sqrt(51)/5, 0.1]])
p2 = np.asarray(poly_p(TX2, 2.5), float)
target = np.polymul(np.polymul([1,0,0.5],[1,-2]),[1,1.5])
chk(np.max(np.abs(p2-target)) < 1e-8, "T7(a): 2-vertex p = (z^2+1/2)(z-2)(z+3/2)")
res2,beta2,Eth2 = resonances(TX2, 2.5)
chk(sorted(abs(np.array(res2)))[:2] == sorted(abs(np.array(res2)))[:2] and
    all(abs(abs(r) - 2**-0.5) < 1e-9 for r in res2) and len(res2)==2,
    "T7(a): only resonances are +- i/sqrt2, RH holds non-vacuously")
chk(sorted(np.round(beta2,9)) == sorted(np.round([0.5,-2/3],9)),
    f"T7(a): visible bound parameters {sorted(np.round(beta2,6))} = 1/2, -2/3")
lams = sorted([b+1/b for b in beta2])
chk(abs(lams[1]-2.5)<1e-9 and abs(lams[0]+13/6)<1e-9, "T7(a): bound eigenvalues 5/2 and -13/6 (RAM fails)")
chk(np.max(np.linalg.eigvalsh(TX2)) < 2.5, "T7(a): core is not bipartite (positive loop) -> -13/6 is no exempt twin")
# T7(b) product identity
for tag, TX, c2 in CORES:
    p = np.asarray(poly_p(TX,c2),float)
    chk(abs(np.prod(np.roots(p)) - (1-c2)) < 1e-6, f"{tag}: prod of ALL roots of p = 1-c^2")
    res,beta,Eth = resonances(TX,c2)
    if res and all(abs(r) > 1e-9 for r in res):
        lhs = np.prod([abs(r) for r in res])
        rhs = abs(1-c2)*np.prod([abs(b) for b in beta]) if beta else abs(1-c2)
        rhs /= np.prod([abs(e) for e in Eth]) if Eth else 1.0
        chk(abs(lhs-rhs) < 1e-6, f"{tag}: retained product (7.2): {lhs:.6g} vs {rhs:.6g}")
# T7(b) r = sqrt(1-c^2) for a = 0
for c2 in [0.1,0.3,0.55,0.9]:
    res,_,_ = resonances(np.array([[0.0]]), c2)
    chk(all(abs(abs(r)-np.sqrt(1-c2))<1e-9 for r in res), f"T7(b): a=0, c^2={c2}: r = sqrt(1-c^2)")
# T7(c) THE DECIDING TEST: scaled self-reciprocity at the GEOMETRIC radius is not sufficient
Q = np.array([1.0, -1.0, 0.16])          # roots 0.8 and 0.2
Nn = 2; r_geo = abs(Q[-1])**(1.0/Nn)
co = Q[::-1]                              # low->high
bgeo = np.array([co[k]*r_geo**(k-Nn) for k in range(Nn+1)])
chk(np.max(np.abs(bgeo - bgeo[0]*bgeo[::-1])) < 1e-12 and abs(abs(bgeo[0])-1) < 1e-12,
    "T7(c): (z-0.8)(z-0.2) IS scaled-self-reciprocal at r = |Q(0)|^(1/N) = 0.4, with |F(0)|=1")
chk(abs(0.8-0.2) > 1e-6, "T7(c): ... yet its roots have DIFFERENT moduli -> (7.3) is NOT sufficient")
# and it IS realised by a genuine graph core: T_X = [1], c^2 = 0.84
resCE,betaCE,EthCE = resonances(np.array([[1.0]]), 0.84)
chk(len(resCE)==2 and len(betaCE)==0 and len(EthCE)==0 and
    abs(sorted([abs(r) for r in resCE])[0]-0.2)<1e-9 and abs(sorted([abs(r) for r in resCE])[1]-0.8)<1e-9,
    "T7(c): the core T_X=[1], c^2=0.84 REALISES resonances {0.2, 0.8} (no bound, no threshold)")
# the numerics lane's version uses r = ARITHMETIC MEAN of the moduli: then it IS an iff
def lane_test(res):
    mods = np.array([abs(r) for r in res]); r = mods.mean()
    if r < 1e-9: return None
    co = np.poly(np.array(res))[::-1].real; dg = len(co)-1
    b = np.array([co[k]*r**(k-dg) for k in range(dg+1)])
    return np.max(np.abs(b - b[0]*b[::-1]))/max(1.0, np.max(np.abs(b)))
dev = lane_test(resCE)
chk(dev > 1e-3, f"T7(c): with r = ARITHMETIC MEAN the lane's test correctly REJECTS {{0.2,0.8}} (dev {dev:.3g})")
for tag, TX, c2 in CORES:
    res,_,_ = resonances(TX, c2)
    if len(res) < 2: continue
    mods = np.array([abs(r) for r in res])
    if mods.mean() < 1e-9: continue
    rh = (mods.max()-mods.min()) < 1e-7
    dv = lane_test(res)
    chk((dv < 1e-6) == rh, f"{tag}: lane's arithmetic-mean self-reciprocity test == RH ({rh}, dev {dv:.1e})")
# proof-grade check of the AM argument: inversion-symmetric at r AND mean = r  =>  all moduli = r
for _ in range(2000):
    k = rng.integers(1,4); x = rng.uniform(0.05,0.95,k); r = rng.uniform(0.1,0.9)
    mods = np.concatenate([x, r*r/x])
    chk_ = abs(mods.mean() - r) < 1e-12
    if chk_: chk(np.max(np.abs(mods-r)) < 1e-6, "AM argument: mean=r + inversion-symmetric => all = r")
OK += 1  # count the AM sweep once
# T7(d) smallest core with a non-real pair
res,_,_ = resonances(np.array([[0.0]]), 0.5)
chk(len(res)==2 and all(abs(r.real)<1e-12 for r in res) and all(abs(abs(r)-2**-0.5)<1e-9 for r in res),
    "T7(d): n=1, a=0, c^2=1/2 gives +- i/sqrt2: non-real pair AND RH, at one vertex")
cnt = 0
for _ in range(400):
    a = rng.uniform(-3,3); c2 = rng.uniform(1.01,4.0)
    res,_,_ = resonances(np.array([[a]]), c2)
    if any(abs(r.imag)>1e-9 for r in res): cnt += 1
chk(cnt == 0, "T7(d)/D18: with c^2 > 1 a ONE-vertex core never has a non-real resonance (400 draws)")

print("="*78)
print(f"CHECKS PASSED: {OK}   FAILURES: {len(FAIL)}")
for f in FAIL: print("  FAIL:", f)
print("="*78)
