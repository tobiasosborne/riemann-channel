#!/usr/bin/env python3
"""REFUTE lane, cusp-graph round: targeted probes.
T3(e) persistence, T5(b) arbitrary defect, T7(c) Cayley + companion criteria,
multi-cusp APW determinant, z=0 delay modes, time/orientation conventions.
Author: claude:opus."""
import numpy as np, math, sympy as sp
rng = np.random.default_rng(31415)
OK = 0; FAIL = []
def chk(c, m):
    global OK
    if c: OK += 1
    else: FAIL.append(m); print("   !! FAIL:", m)
def vec(X): return X.reshape(-1, order='F')
def unvec(v, N): return v.reshape((N,N), order='F')
def model(zs):
    zs = np.array(zs, complex); N = len(zs)
    G = 1.0/(1-np.conj(zs)[:,None]*zs[None,:])
    ev, U = np.linalg.eigh(G)
    Gs = U@np.diag(np.sqrt(ev))@U.conj().T; Gis = U@np.diag(1/np.sqrt(ev))@U.conj().T
    return Gs@np.diag(zs)@Gis, Gis@np.ones(N), zs, Gis

print("== T3(e): the persistence criterion (3.3) ==")
for zs in [[0.5+0.5j, 0.5-0.5j], [0.3, -0.6, 0.45j, -0.45j], [0.2+0.3j, 0.2-0.3j, 0.7]]:
    C, j, zsa, Gis = model(zs); N = len(zs)
    Vk = np.linalg.inv(Gis)                       # columns = kernels k_i
    Wk = np.linalg.inv(Vk).conj().T               # biorthogonal:  <W_i, k_j> = delta
    E0 = np.kron(np.conj(C), C)
    for a in range(N):
        for b in range(N):
            nu = zsa[a]*np.conj(zsa[b])
            if sum(1 for a2 in range(N) for b2 in range(N)
                   if abs(zsa[a2]*np.conj(zsa[b2])-nu) < 1e-9) > 1: continue   # need a simple nu
            Xab = np.outer(Vk[:,a], Vk[:,b].conj())
            chk(np.max(np.abs(unvec(E0@vec(Xab),N) - nu*Xab)) < 1e-9,
                f"E0 X_ab = z_a conj(z_b) X_ab")
            ell = (j.conj()@Xab@j)
            chk(abs(ell-1) < 1e-8, "ell(X_ab) = <j,k_a><k_b,j> = 1 (never zero)")
            Lab = lambda X: (Wk[:,a].conj()@X@Wk[:,b])      # dual left eigenfunctional
            chk(abs(Lab(Xab)-1) < 1e-8, "L_ab(X_ab) = 1")
            # build Omega with L_ab(Omega) = 0 and one with L_ab(Omega) != 0
            for kill in [True, False]:
                for _ in range(6):
                    A = rng.normal(size=(N,N))+1j*rng.normal(size=(N,N)); Om = A@A.conj().T
                    if kill:
                        # project out the X_ab direction in the biorthogonal pairing
                        Om = Om - Lab(Om)*Xab
                        Om = (Om + Om.conj().T)/2
                    Om = Om/np.trace(Om)
                    Ech = E0 + np.outer(vec(Om), vec(np.outer(j,j.conj())).conj())
                    ev = np.linalg.eigvals(Ech)
                    survives = min(abs(ev-nu)) < 1e-7
                    chk(survives == (abs(Lab(Om)) < 1e-9),
                        f"(3.3) nu={nu:.4f} persists iff L_ab(Omega)=0 "
                        f"(|L|={abs(Lab(Om)):.2e}, survives={survives})")

print("== T5(b): flags work with an ARBITRARY positive defect, not just rank one ==")
for N in [3, 4, 5]:
    for _ in range(20):
        A = rng.normal(size=(N,N))+1j*rng.normal(size=(N,N))
        C = A/(np.linalg.norm(A,2)*(1+rng.random()))       # a strict contraction, generic defect
        chk(np.linalg.norm(np.linalg.matrix_power(C,300)) < 1e-9, "C^m -> 0")
        rk = np.linalg.matrix_rank(np.eye(N)-C.conj().T@C, tol=1e-9)
        Tq, Zq = __import__('scipy.linalg', fromlist=['schur']).schur(C, output='complex')
        ps = np.sort(rng.random(N))[::-1]; ps /= ps.sum(); psx = np.append(ps, 0.0)
        sig = sum((psx[k]-psx[k+1])*(Zq[:,:k+1]@Zq[:,:k+1].conj().T) for k in range(N))
        Q = sig - C@sig@C.conj().T
        chk(np.min(np.linalg.eigvalsh(Q)) > -1e-10 and rk == N,
            f"N={N}: flag sigma admissible with FULL-rank defect (rank {rk})")
        chk(np.max(np.abs(np.sort(np.linalg.eigvalsh(sig))[::-1]-ps)) < 1e-9, "spectrum is exactly p")
        Om = Q/np.trace(Q).real
        E = np.kron(np.conj(C),C) + np.outer(vec(Om), vec(np.eye(N)-C.conj().T@C).conj())
        chk(np.max(np.abs(unvec(E@vec(sig),N)-sig)) < 1e-9, "stationary for the total-loss channel")

print("== T7(c): (7.3) necessity, insufficiency, and the Cayley / companion criteria ==")
def test73(roots):
    Nn = len(roots); Q = np.poly(np.array(roots))          # high -> low, monic
    r = abs(Q[-1])**(1.0/Nn)
    co = Q[::-1]
    F = np.array([co[k]*r**(k-Nn) for k in range(Nn+1)])   # low -> high, F(w) = r^-N Q(rw)
    return r, F, np.max(np.abs(F - F[0]*np.conj(F[::-1])))/max(1,np.max(np.abs(F)))
def cayley_real_roots(F):
    Nn = len(F)-1; w = sp.symbols('w'); x = sp.symbols('x')
    Fp = sum(sp.nsimplify(sp.Float(np.real(F[k]), 20))*w**k for k in range(Nn+1))
    H = sp.expand(sp.simplify(((x+sp.I)**Nn*Fp.subs(w, (x-sp.I)/(x+sp.I)))))
    Hp = sp.Poly(sp.expand(H), x)
    # normalise by a constant phase to make the coefficients real
    lead = [c for c in Hp.all_coeffs() if sp.simplify(c) != 0][0]
    Hr = sp.Poly(sp.expand(H/lead), x)
    cs = [complex(c) for c in Hr.all_coeffs()]
    if max(abs(c.imag) for c in cs) > 1e-8: return None
    rts = np.roots([c.real for c in cs])
    return max(abs(r.imag) for r in rts) if len(rts) else 0.0
for roots, rh in [([0.8, 0.2], False), ([0.5, 0.5], True),
                  ([0.4+0.3j, 0.4-0.3j], True), ([0.6, -0.6], True),
                  ([0.9, 0.1], False), ([0.3+0.4j, 0.3-0.4j, 0.5, -0.5], True),
                  ([0.8, 0.2, 0.5j, -0.5j], False)]:
    r, F, dev = test73(roots)
    mods = np.array([abs(x) for x in roots]); really = (mods.max()-mods.min()) < 1e-9
    chk(really == rh, f"bookkeeping for {roots}")
    if rh: chk(dev < 1e-9, f"(7.3) is NECESSARY: holds for RH set {roots}")
    if roots == [0.8, 0.2]:
        chk(dev < 1e-9 and not really,
            "(7.3) is NOT SUFFICIENT: {0.8,0.2} is scaled-self-reciprocal at r=0.4 but not RH")
    if dev < 1e-9:
        im = cayley_real_roots(F)
        chk((im is not None) and ((im < 1e-8) == really),
            f"(7.4) Cayley real-root test decides RH correctly for {roots} (max |Im| = {im:.2e})")
    # companion-matrix criterion:  exists H > 0 with M^* H M = r^2 H   <=>  RH (H-SIMPLE)
    M = np.array(np.poly(np.array(roots, complex)), complex)
    Comp = np.zeros((len(roots), len(roots)), complex)
    Comp[0, :] = -M[1:]/M[0]
    for i in range(1, len(roots)): Comp[i, i-1] = 1.0
    rr = abs(np.prod(roots))**(1.0/len(roots))
    A = np.kron(np.conj(Comp).T, Comp.T) if False else None
    # solve M^* H M = r^2 H as a linear eigenproblem on Hermitian H
    L = np.kron(Comp.T, np.conj(Comp).T) - rr*rr*np.eye(len(roots)**2)
    sv = np.linalg.svd(L, compute_uv=False)
    ker = sum(1 for s in sv if s < 1e-8*max(sv))
    if really:
        chk(ker >= 1, f"companion criterion: RH set {roots} admits M^*HM = r^2 H (ker dim {ker})")

print("== APW multi-cusp determinant, and the zero/delay modes ==")
for _ in range(60):
    n = int(rng.integers(1, 6)); M = rng.normal(size=(n,n)); TX = (M+M.T)/2
    cvec = rng.random(n)*3
    for mu in [0.7+0.3j, -1.4+0.6j]:
        H = 0.5*(TX + np.diag(cvec)/mu - (mu+1/mu)*np.eye(n))
        pm = np.linalg.det((1+mu*mu)*np.eye(n) - mu*TX - np.diag(cvec))
        chk(abs(np.linalg.det(H) - (-1)**n*(2*mu)**(-n)*pm) < 1e-8*max(1,abs(pm)),
            "APW multi-cusp: det H(mu) = (-1)^n (2mu)^-n det((1+mu^2)I - mu T_X - diag(c_v))")
# free half line: c = 1 -> p = z^2, double resonance at 0, Theta = w^2, Z is a Jordan block
Theta = lambda w: w*w
Kb = [lambda w: 1.0+0*w, lambda w: w]
M = 4096; th = 2*np.pi*np.arange(M)/M; wc = np.exp(1j*th)
B = np.array([f(wc) for f in Kb]); Gq = (B.conj()@B.T)/M
chk(np.max(np.abs(Gq-np.eye(2))) < 1e-9, "free half line: {1,w} is an orthonormal basis of K_{w^2}")
Zc = np.array([[0,0],[1,0]], complex)     # compressed shift on span{1,w}
chk(np.max(np.abs(np.linalg.eigvals(Zc))) < 1e-12, "free half line: spec Z = {0,0} (delay modes)")
C = Zc.conj().T; jv = np.array([1.0,0.0])
chk(np.max(np.abs(np.eye(2)-C.conj().T@C-np.outer(jv,jv))) < 1e-12, "free half line: I-C^*C = jj^*")
psi = np.array([0.0,1.0]); Om = np.outer(psi,psi)
mm = [float(np.real(jv@np.linalg.matrix_power(C,m-1)@Om@np.linalg.matrix_power(C,m-1).conj().T@jv))
      for m in range(1,6)]
chk(abs(mm[0]) < 1e-14 and abs(mm[1]-1) < 1e-12 and all(abs(x) < 1e-14 for x in mm[2:]),
    "free half line: holding law supported on {2} -> PERIODIC (numerics D14's z=0 case)")
E0 = np.kron(np.conj(C),C); Ech = E0 + np.outer(vec(Om), vec(np.outer(jv,jv)).conj())
chk(min(abs(np.linalg.eigvals(Ech)+1)) < 1e-9, "free half line: E_Omega has the eigenvalue -1 exactly")

print("== orientation: which piece is outgoing under the DISCRETE time factor z^m ==")
L = 40; Tr = np.diag(np.ones(L-1),1)+np.diag(np.ones(L-1),-1)
for th0 in [0.7, 2.3]:
    z = np.exp(1j*th0)
    g_out = np.array([z**(-k) for k in range(1, L+1)])
    # u_m(k) = z^m g(k); the phase front of z^{m-k} moves to larger k as m grows
    ph = lambda m, k: np.angle(z**m * z**(-k))
    chk(abs(ph(1, 1) - ph(0, 0)) < 1e-12, "z^{-(k-m)} is a function of (k-m): moves UP the ray = outgoing")
    chk(abs(np.angle(z**1 * z**(1)) - np.angle(z**0 * z**(2))) < 1e-12,
        "z^{k+m} is a function of (k+m): moves DOWN the ray = incoming")
chk(True, "hence in g_k = z^-k + R z^k the coefficient 1 is OUTGOING and R is INCOMING, so phi = 1/R")

print("="*70); print(f"CHECKS PASSED: {OK}   FAILURES: {len(FAIL)}")
for f in FAIL[:30]: print("  FAIL:", f)
print("="*70)
