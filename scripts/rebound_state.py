#!/usr/bin/env python3
"""The rebound state inside the model space: finite Gram evidence for T1--T6.

Numerics lane for the brief `notes/rebound-state/astra-brief.md` (drafted statements
T1--T7, conventions C1--C4).  Independent of the prover's file.  Deterministic
(seed 20260919); every check is an assertion, tally printed at the end.

--------------------------------------------------------------------------------
CONVENTIONS AND THE CONSTANTS FIXED HERE  (these are derived, not assumed)
--------------------------------------------------------------------------------
Hardy space of the upper half plane with the NORMALISED inner product

    <f|g> = (1/2pi) int_R conj(f(x)) g(x) dx        (conjugate-linear in the FIRST slot)

and the Paley-Wiener transform  f(tau) = int_0^inf fhat(x) e^{i tau x} dx, under which
Plancherel reads <f|g> = int_0^inf conj(fhat) ghat dx.

Kernel functions (the brief's normalisation, with no 2 pi i put in):

    k_w(tau) = 1/(tau - conj w),   w in C_+ ,       khat_w = k_w/||k_w|| .

Its Paley-Wiener transform is    F k_w (x) = -i e^{-i conj(w) x}   on (0, inf)
(check: int_0^inf (-i) e^{-i conj(w) x} e^{i tau x} dx = -i * i/(tau - conj w) = k_w(tau),
convergent because Im(tau - conj w) = Im tau + Im w > 0).  So |F k_w| decays at rate Im w.

GRAM CONSTANT (C1).  By Plancherel, or by closing the x-integral in the upper half plane
on the single pole at w_n,

    G_nm = <k_n|k_m> = int_0^inf e^{i (w_n - conj w_m) x} dx = i/(w_n - conj w_m),

i.e. the brief's constant is  c = i  for the measure dx/(2pi)  (equivalently c = 2 pi i for
plain Lebesgue dx).  Diagonal: G_nn = 1/(2 Im w_n) > 0.  G is a Cauchy matrix, positive
definite for distinct modes, and G_nm is NEVER zero: distinct kernel modes are never
orthogonal.  (This last remark is what breaks T5(b) below.)

NO-EVENT SEMIGROUP (C1).  C_t = Z_t^* is the backward translation in the time domain,
    (F C_t psi)(x) = (F psi)(x + t),   hence   C_t k_w = e^{-i conj(w) t} k_w,
    K_gen k_w = -i conj(w) k_w,        decay rate Im w, frequency -Re w.

EXIT VECTOR NORMALISATION (C2).  With psi = sum_n c_n k_n, integration by parts gives
    -(<K psi|phi> + <psi|K phi>) = -[ conj(psihat) phihat ]_0^inf = conj(psihat(0)) phihat(0),
so the exit functional is EXACTLY  j psi = psihat(0) = -i sum_n c_n  (no free constant left).
In the mode basis this is the one-row exit  j = -i 1^T ;  equivalently, in the mode basis,
    -(D^* G + G D) = 1 1^T   with D = diag(-i conj w_n),
an identity we verify entrywise: (i w_n - i conj w_m) * i/(w_n - conj w_m) = -1.

FINITE MATRIX MODEL.  R = G^{1/2}, the coefficient vector c maps to the orthonormal vector
v = R c, so |k_n> = R e_n and
    K_mat = R diag(-i conj w) R^{-1},        |j> = i R^{-1} 1   (global phase irrelevant),
    -(K_mat + K_mat^dagger) = |j><j|         (rank one: the one-exit identity),
    <j|k_n> = -i != 0 for every mode         (C3: no mode decoupled from the exit),
    H = (i/2)(K - K^dagger) = H^dagger,      K = -i H - (1/2)|j><j| .

RENEWAL GENERATOR.  L_Omega(rho) = K rho + rho K^dagger + Tr(|j><j| rho) Omega, built as an
N^2 x N^2 superoperator in ROW-MAJOR vec: vec(A rho B) = (A kron B^T) vec(rho).

MODE-BASIS TRANSFORM.  rho = R rho_k R, rho_k = R^{-1} rho R^{-1}; rho_k[n,m] is the
coefficient of |k_n><k_m|.  Two formulas used throughout:
    int_0^inf C_t rho C_t^dagger dt   has mode matrix   rho_k * conj(G)   (entrywise),
    mhat_Omega(z) = sum_{n,m} Omega_k[n,m] / (z + i conj(w_n) - i w_m).
--------------------------------------------------------------------------------
"""
import os
import numpy as np
_trapz = getattr(np, 'trapezoid', None) or getattr(np, 'trapz')  # numpy 2 renamed trapz

import scipy.linalg as sla
from numpy.polynomial import polynomial as Pl
from scipy.optimize import nnls

np.set_printoptions(linewidth=160, precision=6, suppress=False)
rng = np.random.default_rng(20260919)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CHECKS = 0
FLAGS = []


def check(cond, msg):
    global CHECKS
    CHECKS += 1
    assert cond, f"FAILED  {msg}"
    print(f"  ok {CHECKS:2d}  {msg}")


def flag(msg):
    FLAGS.append(msg)
    print(f"  !! {msg}")


# ---------------------------------------------------------------- the finite Gram model
def gram(ws):
    return 1j / (ws[:, None] - np.conj(ws)[None, :])


def model(ws):
    """Everything the finite one-exit model needs, from the mode list ws in C_+."""
    N = len(ws)
    G = gram(ws)
    ev, U = np.linalg.eigh(G)
    assert ev.min() > 0, "Gram matrix not positive definite"
    R = U @ np.diag(np.sqrt(ev)) @ U.conj().T
    Ri = U @ np.diag(1.0 / np.sqrt(ev)) @ U.conj().T
    D = np.diag(-1j * np.conj(ws))
    K = R @ D @ Ri
    j = 1j * (Ri @ np.ones(N))
    J = np.outer(j, j.conj())
    H = 0.5j * (K - K.conj().T)
    return dict(N=N, ws=ws, G=G, R=R, Ri=Ri, D=D, K=K, j=j, J=J, H=H, cond=ev.max() / ev.min())


def to_mode(M, m):
    return m["Ri"] @ M @ m["Ri"]


def from_mode(Mk, m):
    return m["R"] @ Mk @ m["R"]


def Ct(m, t):
    return sla.expm(t * m["K"])


def superop(m, Om, K=None, J=None):
    """L_Omega as an N^2 x N^2 matrix in row-major vec."""
    K = m["K"] if K is None else K
    J = m["J"] if J is None else J
    n = K.shape[0]
    I = np.eye(n)
    return (np.kron(K, I) + np.kron(I, K.conj())
            + np.outer(Om.reshape(-1), J.T.reshape(-1)))


def apply_L(m, Om, rho, K=None, J=None):
    K = m["K"] if K is None else K
    J = m["J"] if J is None else J
    return K @ rho + rho @ K.conj().T + np.trace(J @ rho) * Om


def stat_mode(m, Om):
    """rho_inf and mu from the closed mode-basis form (the renewal integral)."""
    X = from_mode(to_mode(Om, m) * m["G"].conj(), m)
    mu = np.trace(X).real
    return X / mu, mu


def stat_lyap(m, Om):
    X = sla.solve_continuous_lyapunov(m["K"], -Om)   # K X + X K^dagger = -Om
    mu = np.trace(X).real
    return X / mu, mu


def stat_null(m, Om, K=None, J=None):
    L = superop(m, Om, K, J)
    w, V = np.linalg.eig(L)
    k = int(np.argmin(np.abs(w)))
    n = K.shape[0] if K is not None else m["N"]
    rho = V[:, k].reshape(n, n)
    rho = 0.5 * (rho + rho.conj().T)
    return rho / np.trace(rho).real, abs(w[k])


def stat_eig(m, Om):
    """Fourth, independent route: eigendecomposition of K_mat (no mode structure used)."""
    lam, V = np.linalg.eig(m["K"])
    Vi = np.linalg.inv(V)
    B = Vi @ Om @ Vi.conj().T
    X = V @ (B / (-(lam[:, None] + np.conj(lam)[None, :]))) @ V.conj().T
    mu = np.trace(X).real
    return X / mu, mu


def mhat_rational(m, Om, z):
    Ok = to_mode(Om, m)
    zs = -1j * np.conj(m["ws"])[:, None] + 1j * m["ws"][None, :]
    return np.sum(Ok / (z - zs))


def mhat_resolvent(m, Om, z):
    n = m["N"]
    L0 = superop(m, np.zeros((n, n), complex))
    X = np.linalg.solve(z * np.eye(n * n) - L0, Om.reshape(-1)).reshape(n, n)
    return np.trace(m["J"] @ X)


def orbit(m, psi):
    """Phi(psi) = int_0^inf |C_t psi><C_t psi| dt, by the Lyapunov equation."""
    return sla.solve_continuous_lyapunov(m["K"], -np.outer(psi, psi.conj()))


def rand_density(n, rank=None, gen=None):
    g = gen or rng
    r = rank or n
    A = g.normal(size=(n, r)) + 1j * g.normal(size=(n, r))
    rho = A @ A.conj().T
    return rho / np.trace(rho).real


def haar(n, gen=None):
    g = gen or rng
    A = g.normal(size=(n, n)) + 1j * g.normal(size=(n, n))
    Q, Rr = np.linalg.qr(A)
    return Q * (np.diag(Rr) / np.abs(np.diag(Rr)))


def mode_diag(m, p):
    """Omega = sum p_n |khat_n><khat_n|, khat_n = k_n/||k_n||."""
    return from_mode(np.diag(p / np.diag(m["G"]).real), m)


def sort_c(z):
    return np.array(sorted(z, key=lambda t: (round(t.real, 7), round(t.imag, 7))))


def match(a, b, tol):
    a, b = sort_c(a), sort_c(b)
    return len(a) == len(b) and np.max(np.abs(a - b)) < tol


# ---------------------------------------------------------------- mode sets
GAM = np.load(os.path.join(ROOT, "data", "zeros3000.npy"))
N = 5
W_ON = GAM[:N] / 2 + 0.25j                                     # RH true: Im w = 1/4
SIG_OFF = np.array([0.50, 0.62, 0.38, 0.55, 0.50])             # RH false
W_OFF = GAM[:N] / 2 + 1j * (1 - SIG_OFF) / 2
W_FE = np.array([GAM[0] / 2, -GAM[0] / 2, GAM[1] / 2, -GAM[1] / 2]) + 0.25j   # both signs

print(__doc__.split("---")[0].strip())
print()
print(f"modes: N = {N};  on-line Im w = {np.unique(np.round(W_ON.imag, 12))};"
      f"  off-line Im w = {np.round(W_OFF.imag, 4)}")

M_ON, M_OFF, M_FE = model(W_ON), model(W_OFF), model(W_FE)
print(f"Gram condition numbers: on-line {M_ON['cond']:.4f}, off-line {M_OFF['cond']:.4f}, "
      f"both-signs {M_FE['cond']:.4f}")

# ================================================================ 0. conventions C1-C4
print("\n0. conventions: Gram constant, one-exit identity, mode eigenvalues (C1-C4)")

for name, m in (("on-line", M_ON), ("off-line", M_OFF), ("both-signs", M_FE)):
    ws = m["ws"]
    # Gram by direct numerical quadrature of (1/2pi) int conj(k_n) k_m dx on the real line
    x = np.linspace(-4e4, 4e4, 4_000_001)
    kn = 1.0 / (x[:, None] - np.conj(ws)[None, :])
    Gq = (kn.conj().T @ kn) * (x[1] - x[0]) / (2 * np.pi)
    check(np.max(np.abs(Gq - m["G"])) < 2e-4,
          f"{name}: <k_n|k_m> = i/(w_n - conj w_m) by quadrature of (1/2pi)int conj(k_n)k_m dx "
          f"(max dev {np.max(np.abs(Gq - m['G'])):.1e}); the Gram constant is c = i")
    del x, kn, Gq

for name, m in (("on-line", M_ON), ("off-line", M_OFF), ("both-signs", M_FE)):
    ws, G = m["ws"], m["G"]
    check(np.allclose(np.diag(G).real, 1 / (2 * ws.imag)) and np.allclose(G, G.conj().T),
          f"{name}: G Hermitian, G_nn = 1/(2 Im w_n), lambda_min(G) = "
          f"{np.linalg.eigvalsh(G).min():.4f} > 0")
    offmin = np.min(np.abs(G + 1e9 * np.eye(m["N"])))
    check(offmin > 1e-3,
          f"{name}: no two kernel modes are orthogonal, min_{{n!=m}}|G_nm| = "
          f"{offmin:.4f} (this is what breaks T5(b), see below)")
    D = m["D"]
    check(np.max(np.abs(-(D.conj().T @ G + G @ D) - np.ones((m["N"], m["N"])))) < 1e-12,
          f"{name}: mode-basis exit identity -(D^* G + G D) = 1 1^T exactly")

for name, m in (("on-line", M_ON), ("off-line", M_OFF), ("both-signs", M_FE)):
    K, j = m["K"], m["j"]
    A = -(K + K.conj().T)
    sv = np.linalg.svd(A, compute_uv=False)
    check(sv[1] / sv[0] < 1e-12,
          f"{name}: -(K+K^dag) has numerical rank 1 (sv2/sv1 = {sv[1]/sv[0]:.1e})")
    check(np.max(np.abs(A - np.outer(j, j.conj()))) < 1e-12,
          f"{name}: -(K+K^dag) = |j><j| with |j> = i R^(-1) 1 (C2), ||j||^2 = 1^T G^(-1) 1 = "
          f"{np.vdot(j, j).real:.6f}")
    jk = j.conj() @ m["R"]                              # <j|k_n>
    check(np.max(np.abs(jk + 1j)) < 1e-12,
          f"{name}: <j|k_n> = -i != 0 for EVERY mode (C3: no mode decoupled from the exit)")
    lam = np.linalg.eigvals(K)
    check(match(lam, -1j * np.conj(m["ws"]), 1e-10),
          f"{name}: spec(K_mat) = {{-i conj(w_n)}}, decay rates Im w_n = "
          f"{np.round(np.sort(m['ws'].imag), 4)}")
    for t in (0.3, 1.7, 5.0):
        C = Ct(m, t)
        err = max(np.max(np.abs(C @ (m["R"] @ np.eye(m["N"])[:, n])
                                - np.exp(-1j * np.conj(m["ws"][n]) * t) * (m["R"] @ np.eye(m["N"])[:, n])))
                  for n in range(m["N"]))
        assert err < 1e-10
    check(True, f"{name}: C_t k_n = e^(-i conj(w_n) t) k_n for t = 0.3, 1.7, 5.0 (C1, corrected sign)")
    H = m["H"]
    check(np.max(np.abs(H - H.conj().T)) < 1e-12
          and np.max(np.abs(K - (-1j * H - 0.5 * m["J"]))) < 1e-12,
          f"{name}: K = -i H - (1/2)|j><j| with H = (i/2)(K-K^dag) Hermitian (GKLS form)")
    nrm = [np.linalg.norm(Ct(m, t), 2) for t in (0.0, 0.5, 2.0, 10.0, 40.0)]
    check(nrm[0] == 1.0 and all(nrm[i] < 1 - 1e-9 for i in range(1, 5)) and nrm[-1] < 1e-3,
          f"{name}: ||C_t||_2 = {np.round(nrm,6)} at t = 0,.5,2,10,40 -- contractive, -> 0, and "
          f"STRICTLY < 1 for t>0 (C4: ||C_t||=1 is false in the finite model)")

# ================================================================ 1. T1 conservativity
print("\n1. T1 (conservativity): trace preservation and complete positivity")

OMS_ON = {
    "mode-diagonal p=(.4,.3,.15,.1,.05)": mode_diag(M_ON, np.array([.4, .3, .15, .1, .05])),
    "pure on one mode khat_1": mode_diag(M_ON, np.array([1., 0, 0, 0, 0])),
    "generic full-rank density": rand_density(N),
    "rank-one on a random vector": rand_density(N, rank=1),
}
OMS_OFF = {
    "mode-diagonal p=(.4,.3,.15,.1,.05)": mode_diag(M_OFF, np.array([.4, .3, .15, .1, .05])),
    "pure on one mode khat_1": mode_diag(M_OFF, np.array([1., 0, 0, 0, 0])),
    "generic full-rank density": rand_density(N),
    "rank-one on a random vector": rand_density(N, rank=1),
}

for lab, m, oms in (("on-line", M_ON, OMS_ON), ("off-line", M_OFF, OMS_OFF)):
    for name, Om in oms.items():
        L = superop(m, Om)
        rho = rand_density(N)
        check(abs(np.trace(apply_L(m, Om, rho))) < 1e-12
              and np.max(np.abs(np.eye(N).reshape(-1) @ L)) < 1e-12,
              f"T1 {lab}, Omega = {name}: Tr L_Omega(rho) = 0 (vec(1) is a left null vector)")

m, Om = M_ON, OMS_ON["generic full-rank density"]
for t in (0.1, 1.0, 6.0):
    T4 = sla.expm(t * superop(m, Om)).reshape(N, N, N, N)      # T4[a,b,i,j] = <a|E(|i><j|)|b>
    C4 = T4.transpose(2, 0, 3, 1)                              # sum_ij |i><j| (x) E(|i><j|)
    choi = C4.reshape(N * N, N * N)
    lo = np.linalg.eigvalsh(0.5 * (choi + choi.conj().T)).min()
    assert lo > -1e-10, lo
    assert np.max(np.abs(np.einsum("iaja->ij", C4) - np.eye(N))) < 1e-10
check(True, "T1 on-line, generic Omega: e^(t L_Omega) is CPTP for t = 0.1, 1, 6 "
            "(Choi >= 0 to 1e-10, partial trace = 1); jumps L_a = sqrt(w_a)|phi_a><j|")

for lab, m, oms in (("on-line", M_ON, OMS_ON), ("off-line", M_OFF, OMS_OFF)):
    for name, Om in oms.items():
        ts = np.linspace(0, 140, 28001)
        surv = np.array([np.trace(Ct(m, t) @ Om @ Ct(m, t).conj().T).real for t in ts[::40]])
        dt = ts[40] - ts[0]
        mden = -np.gradient(surv, dt)
        tot = _trapz(mden, ts[::40])
        check(mden.min() > -1e-9 and abs(tot - 1) < 1e-4,
              f"T1 {lab}, Omega = {name}: m_Omega(t) = -d/dt Tr(C_t Omega C_t^dag) >= 0 and "
              f"int_0^inf m_Omega = {tot:.6f} (a proper holding-time density)")

# ================================================================ 2. T2 stationary state
print("\n2. T2 (stationary state and the renewal theorem)")

for lab, m, oms in (("on-line", M_ON, OMS_ON), ("off-line", M_OFF, OMS_OFF)):
    for name, Om in oms.items():
        r1, mu1 = stat_mode(m, Om)
        r2, mu2 = stat_lyap(m, Om)
        r3, mu3 = stat_eig(m, Om)
        r4, res = stat_null(m, Om)
        if np.vdot(r4.reshape(-1), r1.reshape(-1)).real < 0:
            r4 = -r4
        d = max(np.max(np.abs(r1 - r2)), np.max(np.abs(r1 - r3)), np.max(np.abs(r1 - r4)))
        check(d < 1e-10 and abs(mu1 - mu2) < 1e-10 and abs(mu1 - mu3) < 1e-10,
              f"T2 {lab}, Omega = {name}: rho_inf from the mode integral = Lyapunov solve = "
              f"K-eigenbasis integral = null vector of L_Omega, max dev {d:.1e}; mu = {mu1:.6f}")
        check(np.linalg.eigvalsh(r1).min() > -1e-12 and abs(np.trace(r1) - 1) < 1e-12
              and abs(np.trace(m["J"] @ r1).real - 1 / mu1) < 1e-10,
              f"T2 {lab}, Omega = {name}: rho_inf is a density and Tr(|j><j| rho_inf) = 1/mu = "
              f"{1/mu1:.6f} (mean holding time {mu1:.6f} < inf)")

for lab, m in (("on-line", M_ON), ("off-line", M_OFF)):
    Om = OMS_ON["generic full-rank density"] if lab == "on-line" else OMS_OFF["generic full-rank density"]
    L = superop(m, Om)
    ev = np.linalg.eigvals(L)
    nz = ev[np.abs(ev) > 1e-8]
    rinf, _ = stat_mode(m, Om)
    rho0 = rand_density(N)
    rT = (sla.expm(60 * L) @ rho0.reshape(-1)).reshape(N, N)
    check(np.sum(np.abs(ev) < 1e-8) == 1 and nz.real.max() < -1e-6
          and np.max(np.abs(rT - rinf)) < 1e-9,
          f"T2 {lab}: ker L_Omega is 1-dimensional, gap = {-nz.real.max():.6f}, and "
          f"e^(60 L)rho_0 -> rho_inf (dev {np.max(np.abs(rT - rinf)):.1e}) -- unique, globally attracting")

p = np.array([.4, .3, .15, .1, .05])
for lab, m in (("on-line", M_ON), ("off-line", M_OFF)):
    Om = mode_diag(m, p)
    _, mu = stat_mode(m, Om)
    check(abs(mu - np.sum(p / (2 * m["ws"].imag))) < 1e-10,
          f"T2 {lab}: mode-diagonal mu = sum_n p_n/(2 Im w_n) = {mu:.6f}")
for _ in range(3):
    q = rng.random(N); q /= q.sum()
    _, mu = stat_mode(M_ON, mode_diag(M_ON, q))
    assert abs(mu - 2.0) < 1e-10
check(True, "T2 on-line: under RH every mode-diagonal Omega has mu = 1/(2*1/4) = 2 exactly, "
            "so no mode-diagonal rebound state on the critical line can have mu = infinity")
mus = [stat_mode(M_ON, rand_density(N))[1] for _ in range(300)]
check(min(mus) > 0, f"T2 on-line: over 300 random full-rank Omega, mu ranges over "
                    f"[{min(mus):.4f}, {max(mus):.4f}] -- NOT constant = 2 off the mode-diagonal "
                    f"(the mu = 2 identity is special to mode-diagonal Omega)")
w_small = GAM[:N] / 2 + 1j * np.array([.25, .25, .25, .25, .002])
m_small = model(w_small)
_, mu_s = stat_mode(m_small, mode_diag(m_small, np.array([.2] * 4 + [.2])))
check(mu_s > 40, f"T2: mu blows up as a mode approaches the real axis: Im w_5 = 0.002 gives "
                 f"mu = {mu_s:.2f} ~ p_5/(2 Im w_5) = 50 (finite-dimensional shadow of mu = infinity)")

# ================================================================ 3. T4 secular equation
print("\n3. T4 (persistence criterion and secular equation)")

for lab, m, oms in (("on-line", M_ON, OMS_ON), ("off-line", M_OFF, OMS_OFF)):
    for name, Om in oms.items():
        zs = [1.3 + 0.7j, -0.2 + 2.1j, 0.05 - 0.9j]
        d = max(abs(mhat_rational(m, Om, z) - mhat_resolvent(m, Om, z)) for z in zs)
        ts = np.linspace(0, 160, 160001)
        surv = np.array([np.trace(Ct(m, t) @ Om @ Ct(m, t).conj().T).real for t in ts[::20]])
        tt = ts[::20]
        mden = -np.gradient(surv, tt[1] - tt[0])
        lap = _trapz(np.exp(-0.8 * tt) * mden, tt)
        check(d < 1e-10 and abs(lap - mhat_rational(m, Om, 0.8).real) < 1e-4,
              f"T4 {lab}, Omega = {name}: mhat(z) = Tr(|j><j|(z-L_0)^(-1)Omega) = "
              f"sum_nm Omega_k[n,m]/(z + i conj w_n - i w_m) = Laplace(m_Omega)(z) "
              f"(dev {d:.1e}, Laplace at z=0.8 {abs(lap - mhat_rational(m, Om, 0.8).real):.1e})")

for lab, m, oms in (("on-line", M_ON, OMS_ON), ("off-line", M_OFF, OMS_OFF)):
    for name, Om in oms.items():
        L0 = superop(m, np.zeros((N, N), complex))
        L = superop(m, Om)
        rel = []
        for z in (2.0 + 0.3j, -0.35 + 1.1j, 0.9 - 2.2j):
            a = np.linalg.det(z * np.eye(N * N) - L)
            b = np.linalg.det(z * np.eye(N * N) - L0) * (1 - mhat_rational(m, Om, z))
            rel.append(abs(a - b) / abs(b))
        check(max(rel) < 1e-8,
              f"T4(b) {lab}, Omega = {name}: det(z - L_Omega) = det(z - L_0)(1 - mhat(z)) "
              f"exactly (max rel dev {max(rel):.1e}) -- rank-one secular identity")

for lab, m in (("on-line", M_ON), ("off-line", M_OFF)):
    zs = (-1j * np.conj(m["ws"])[:, None] + 1j * m["ws"][None, :]).reshape(-1)
    Xnm = [np.outer(m["R"][:, n], m["R"][:, mm].conj()) for n in range(N) for mm in range(N)]
    pair = np.array([np.trace(m["J"] @ X) for X in Xnm])
    check(np.max(np.abs(pair - 1)) < 1e-10,
          f"T4(a) {lab}: Tr(|j><j| X_nm) = 1 for ALL N^2 eigen-operators X_nm = |k_n><k_m| -- "
          f"the first disjunct of T4(a) NEVER fires in the ungraded model (operator form of C3)")

m = M_ON
Om = OMS_ON["mode-diagonal p=(.4,.3,.15,.1,.05)"]
Ok = to_mode(Om, m)
zs = (-1j * np.conj(m["ws"])[:, None] + 1j * m["ws"][None, :])
ev = np.linalg.eigvals(superop(m, Om))
off = [zs[n, mm] for n in range(N) for mm in range(N) if n != mm]
kept = [z for z in off if np.min(np.abs(ev - z)) < 1e-8]
check(len(kept) == N * N - N,
      f"T4(a) on-line, mode-diagonal Omega: all {N*N-N} off-diagonal eigenvalues z_nm (n!=m) "
      f"persist (their residue Omega_k[n,m] = 0); max |Omega_k off-diag| = "
      f"{np.max(np.abs(Ok - np.diag(np.diag(Ok)))):.1e}")
mult = np.sum(np.abs(ev - (-0.5)) < 1e-8)
check(mult == N - 1,
      f"T4(a) on-line: the N-fold degenerate L_0 eigenvalue -1/2 (all diagonal X_nn) keeps "
      f"multiplicity N-1 = {N-1} under the rank-one perturbation; one copy moves to the secular root")
new = ev[np.array([np.min(np.abs(zs.reshape(-1) - z)) > 1e-7 for z in ev])]
check(len(new) == 1 and abs(new[0]) < 1e-10,
      f"T4(b)+T5(c) on-line: the ONLY new eigenvalue is z = {new[0]:.2e} = 0, the unique root "
      f"of 1 = mhat(z) = (1/2)/(z+1/2)")

m3 = model(GAM[:3] / 2 + 0.25j)
for name, Om3 in (("generic full-rank", rand_density(3)), ("rank-one random", rand_density(3, 1))):
    Ok3 = to_mode(Om3, m3).reshape(-1)
    zs3 = (-1j * np.conj(m3["ws"])[:, None] + 1j * m3["ws"][None, :]).reshape(-1)
    poly = Pl.polyfromroots(zs3).astype(complex)
    for a in range(9):
        poly = Pl.polysub(poly, Ok3[a] * Pl.polyfromroots(np.delete(zs3, a)))
    roots = Pl.polyroots(poly)
    ev3 = np.linalg.eigvals(superop(m3, Om3))
    check(match(roots, ev3, 1e-7),
          f"T4 N=3, Omega = {name}: spec(L_Omega) equals the roots of "
          f"prod(z - z_nm) - sum_nm Omega_k[n,m] prod_(others) exactly (max dev "
          f"{np.max(np.abs(sort_c(roots) - sort_c(ev3))):.1e}); all 9 L_0 eigenvalues destroyed")

# ================================================================ 4. T5 mode-diagonal
print("\n4. T5 (mode-diagonal rebound states; RH reformulation)")

for lab, m in (("on-line", M_ON), ("off-line", M_OFF), ("both-signs", M_FE)):
    n = m["N"]
    q = rng.random(n); q /= q.sum()
    Om = mode_diag(m, q)
    rinf, mu = stat_mode(m, Om)
    predicted = from_mode(np.diag(q / (2 * m["ws"].imag) / mu / np.diag(m["G"]).real), m)
    check(np.max(np.abs(rinf - predicted)) < 1e-12,
          f"T5 {lab}: rho_inf = mu^(-1) sum_n p_n (2 Im w_n)^(-1) |khat_n><khat_n| with "
          f"mu = sum p_n (2 Im w_n)^(-1) = {mu:.6f} (dev {np.max(np.abs(rinf-predicted)):.1e})")

for lab, m in (("on-line", M_ON), ("both-signs", M_FE)):
    worst = 0.0
    for _ in range(6):
        q = rng.random(m["N"]); q /= q.sum()
        Om = mode_diag(m, q)
        rinf, mu = stat_mode(m, Om)
        worst = max(worst, np.max(np.abs(rinf - Om)))
    check(worst < 1e-12,
          f"T5(a) {lab} (RH TRUE, all Im w = 1/4): rho_inf = Omega for every mode-diagonal "
          f"Omega, 6 random p, max dev {worst:.1e}")

dev, tr1 = [], []
for _ in range(6):
    q = rng.random(N); q /= q.sum()
    Om = mode_diag(M_OFF, q)
    rinf, mu = stat_mode(M_OFF, Om)
    dev.append(np.max(np.abs(rinf - Om)))
    tr1.append(np.sum(np.abs(np.linalg.eigvalsh(rinf - Om))))
check(min(dev) > 1e-3,
      f"T5(a) off-line (RH FALSE, Im w = {np.round(W_OFF.imag,3)}): rho_inf != Omega for all 6 "
      f"random p; max-entry gap in [{min(dev):.4f}, {max(dev):.4f}], trace distance "
      f"||rho_inf - Omega||_1 in [{min(tr1):.4f}, {max(tr1):.4f}]")

q = np.array([.5, 0., 0., 0., .5])            # supported on the two modes with Im w = 1/4
Om = mode_diag(M_OFF, q)
rinf, mu = stat_mode(M_OFF, Om)
check(np.max(np.abs(rinf - Om)) < 1e-12,
      f"T5(a) exact quantifier: off-line, but p supported on the two modes with EQUAL Im w = 1/4, "
      f"gives rho_inf = Omega again (dev {np.max(np.abs(rinf-Om)):.1e}) -- the criterion is "
      f"'all Im w_n with p_n > 0 are equal', not 'all zeros on the line'")

# ---- T5(b): the entanglement spectrum
print("   T5(b): entanglement spectrum of rho_inf")
q = np.array([.4, .3, .15, .1, .05])
Om = mode_diag(M_ON, q)
rinf, mu = stat_mode(M_ON, Om)
spec = np.sort(np.linalg.eigvalsh(rinf))[::-1]
claim = np.sort(q)[::-1]
gap = np.max(np.abs(spec - claim))
flag(f"T5(b) FAILS AS STATED. On-line, p = {q}: the drafted claim is that the entanglement "
     f"spectrum of rho_inf is {{p_n (2 Im w_n)^(-1)/mu}} = {claim}; the actual spectrum of "
     f"rho_inf is {np.round(spec,6)}. Max discrepancy {gap:.4f} (relative {gap/claim.max():.1%}); "
     f"entropies {-np.sum(spec*np.log(spec)):.6f} vs {-np.sum(claim*np.log(claim)):.6f} nats.")
check(gap > 1e-2,
      f"T5(b) DISPROVED: spec(rho_inf) != {{p_n(2 Im w_n)^(-1)/mu}}, discrepancy {gap:.4f}. "
      f"Reason: khat_n are NEVER orthogonal (G_nm = i/(w_n - conj w_m) != 0), so "
      f"sum_n lambda_n |khat_n><khat_n| is not a spectral decomposition")
corrected = np.sort(np.linalg.eigvals(np.diag(q / (2 * M_ON["ws"].imag) / mu
                                              / np.diag(M_ON["G"]).real) @ M_ON["G"]).real)[::-1]
check(np.max(np.abs(spec - corrected)) < 1e-10,
      f"T5(b) CORRECTED and verified: spec(rho_inf) = spec(diag(p_n(2 Im w_n)^(-1)/(mu G_nn)) G) "
      f"= spec(G^(1/2) diag(...) G^(1/2)), dev {np.max(np.abs(spec-corrected)):.1e}; it reduces to "
      f"{{p_n}} only in the (never realised) limit of orthogonal modes")
check(np.max(np.abs(np.sort(np.linalg.eigvalsh(rinf)) - np.sort(np.linalg.eigvalsh(Om)))) < 1e-12,
      f"T5(b) what survives: under RH spec(rho_inf) = spec(Omega) exactly (a corollary of T5(a)), "
      f"so the entanglement spectrum IS the rebound state's own spectrum -- just not {{p_n}}")
qq = np.array([1., 0, 0, 0, 0])
r1, _ = stat_mode(M_ON, mode_diag(M_ON, qq))
check(abs(np.sort(np.linalg.eigvalsh(r1))[-1] - 1) < 1e-12,
      "T5(b) boundary case: a single mode (p = delta_1) does give the exact spectrum {1,0,..,0}; "
      "the failure is strictly a multi-mode non-orthogonality effect")

# ---- T5(c)
zsamp = [0.3, 1.2 + 0.4j, -0.1 + 0.9j]
q = rng.random(N); q /= q.sum()
Om = mode_diag(M_ON, q)
d = max(abs(mhat_rational(M_ON, Om, z) - 0.5 / (z + 0.5)) for z in zsamp)
check(d < 1e-12,
      f"T5(c) on-line: mhat_Omega(z) = (1/2)/(z + 1/2) for EVERY mode-diagonal Omega "
      f"(independent of p), dev {d:.1e}; unique root z = 0")
Om = mode_diag(M_OFF, q)
b = 2 * M_OFF["ws"].imag
pol = Pl.polyfromroots(-b).astype(complex)
for n in range(N):
    pol = Pl.polysub(pol, q[n] * b[n] * Pl.polyfromroots(np.delete(-b, n)))
roots = Pl.polyroots(pol)
ev = np.linalg.eigvals(superop(M_OFF, Om))
newev = ev[np.array([np.min(np.abs((-1j*np.conj(M_OFF["ws"])[:,None]+1j*M_OFF["ws"][None,:]).reshape(-1) - z)) > 1e-7 or abs(z) < 1e-9 for z in ev])]
check(min(np.abs(roots)) < 1e-12 and all(np.min(np.abs(ev - r)) < 1e-8 for r in roots),
      f"T5(c) off-line: the N diagonal L_0 eigenvalues -2 Im w_n are replaced by the N roots of "
      f"1 = sum_n p_n 2 Im w_n/(z + 2 Im w_n), = {np.round(np.sort(roots.real),6)}; z = 0 is always "
      f"a root (trace preservation)")

allev = np.linalg.eigvals(superop(M_ON, mode_diag(M_ON, q)))
check(np.max(np.abs(allev[np.abs(allev) > 1e-9].real + 0.5)) < 1e-9,
      f"T5(c) on-line: EVERY nonzero eigenvalue of L_Omega has Re = -1/2 = -2*(1/4); the even-sector "
      f"relaxation rate is exactly twice the common zero-decay rate. Frequencies = "
      f"(gamma_m - gamma_n)/2, the pair differences")

# ================================================================ 5. T3 graded
print("\n5. T3 (graded version on C vac + K: the zeros survive for every rebound state)")


def graded(m):
    n = m["N"]
    Kg = np.zeros((n + 1, n + 1), complex)
    Kg[1:, 1:] = m["K"]
    jg = np.zeros(n + 1, complex)
    jg[1:] = m["j"]
    return Kg, np.outer(jg, jg.conj()), jg


Kg, Jg, jg = graded(M_ON)
vac = np.zeros(N + 1, complex); vac[0] = 1
kk = [np.concatenate(([0], M_ON["R"][:, n])) for n in range(N)]
check(np.max(np.abs(-(Kg + Kg.conj().T) - Jg)) < 1e-12,
      "T3: the graded one-exit identity -(Kbar + Kbar^dag) = |j><j| still holds on C vac + K "
      "(Kbar = 0 (+) K, j supported on K)")

GOMS = {
    "even (mode-diagonal on K)": None,
    "with vacuum-mode coherences": None,
    "Omega = |vac><vac| (vacuum decay)": None,
    "generic full-rank on C vac + K": None,
}
Ok = mode_diag(M_ON, np.array([.4, .3, .15, .1, .05]))
A = np.zeros((N + 1, N + 1), complex); A[1:, 1:] = Ok
GOMS["even (mode-diagonal on K)"] = A
B = rand_density(N + 1)
GOMS["with vacuum-mode coherences"] = B
C = np.zeros((N + 1, N + 1), complex); C[0, 0] = 1
GOMS["Omega = |vac><vac| (vacuum decay)"] = C
GOMS["generic full-rank on C vac + K"] = rand_density(N + 1)

for name, Omg in GOMS.items():
    worst = 0.0
    for n in range(N):
        Xa = np.outer(kk[n], vac.conj())      # |k_n><vac|
        Xb = np.outer(vac, kk[n].conj())      # |vac><k_n|
        la = Kg @ Xa + Xa @ Kg.conj().T + np.trace(Jg @ Xa) * Omg
        lb = Kg @ Xb + Xb @ Kg.conj().T + np.trace(Jg @ Xb) * Omg
        worst = max(worst,
                    np.max(np.abs(la - (-1j * np.conj(M_ON["ws"][n])) * Xa)),
                    np.max(np.abs(lb - (1j * M_ON["ws"][n]) * Xb)),
                    abs(np.trace(Jg @ Xa)), abs(np.trace(Jg @ Xb)))
    check(worst < 1e-12,
          f"T3, Omega = {name}: |k_n><vac| and |vac><k_n| are EXACT eigen-operators with "
          f"eigenvalues -i conj(w_n) and +i w_n (decay rate Im w_n = 1/4), for this Omega "
          f"(dev {worst:.1e}); the exit functional annihilates them")
flag("T3 labelling: with the convention <f|g> conjugate-linear in the first slot, it is "
     "|k_w><vac| that carries -i conj(w) and |vac><k_w| that carries +i w; the brief's T3 states "
     "the transpose. Not a mathematical error, but the draft's assignment must be swapped.")

check(np.max(np.abs(apply_L(M_ON, GOMS["generic full-rank on C vac + K"],
                            np.outer(vac, vac.conj()), K=Kg, J=Jg))) < 1e-14,
      "T3 (new): |vac><vac| is stationary for L_Omega for EVERY Omega -- the vacuum is never "
      "emptied, because Kbar|vac> = 0 and the exit functional vanishes on it")

for name, Omg in GOMS.items():
    Lg = superop(M_ON, Omg, K=Kg, J=Jg)
    evg = np.linalg.eigvals(Lg)
    qK = np.trace(Omg[1:, 1:]).real
    kerdim = int(np.sum(np.abs(evg) < 1e-9))
    expect = 2 if abs(qK - 1) < 1e-12 else 1
    check(kerdim == expect,
          f"T3, Omega = {name}: Tr(Omega|_K) = {qK:.4f}, dim ker L_Omega = {kerdim} "
          f"({'vacuum AND a mixed rho_inf: stationary state NOT unique' if expect == 2 else 'the vacuum alone is stationary: all population drains into vac'})")

zK = (-1j * np.conj(M_ON["ws"])[:, None] + 1j * M_ON["ws"][None, :])
L0g = superop(M_ON, np.zeros((N + 1, N + 1), complex), K=Kg, J=Jg)
for name, Omg in GOMS.items():
    Lg = superop(M_ON, Omg, K=Kg, J=Jg)
    evg = np.linalg.eigvals(Lg)
    OkK = to_mode(Omg[1:, 1:], M_ON)                       # only the K-block enters mhat
    rel = []
    for z in (2.0 + 0.3j, -0.35 + 1.1j, 0.9 - 2.2j):
        a = np.linalg.det(z * np.eye((N + 1) ** 2) - Lg)
        b = np.linalg.det(z * np.eye((N + 1) ** 2) - L0g) * (1 - np.sum(OkK / (z - zK)))
        rel.append(abs(a - b) / abs(b))
    prot = np.concatenate(([0.0], -1j * np.conj(M_ON["ws"]), 1j * M_ON["ws"]))
    dprot = max(np.min(np.abs(evg - z)) for z in prot)
    check(max(rel) < 1e-7 and dprot < 1e-8,
          f"T3, Omega = {name}: det(z - L_Omega) = det(z - L_0)(1 - mhat_K(z)) with mhat built "
          f"from the K-BLOCK of Omega alone (rel dev {max(rel):.1e}), and the 2N+1 protected "
          f"eigenvalues {{0}} u {{-i conj w_n}} u {{i w_n}} all lie in spec L_Omega "
          f"(dev {dprot:.1e})")

Lvac = superop(M_ON, GOMS["Omega = |vac><vac| (vacuum decay)"], K=Kg, J=Jg)
bb = -1j * np.conj(M_ON["ws"])
pred = np.concatenate(([0.0], bb, np.conj(bb), (bb[:, None] + np.conj(bb)[None, :]).reshape(-1)))
check(match(pred, np.linalg.eigvals(Lvac), 1e-9),
      f"T3 consistency with thm:vacuum-decay-finite: for Omega = |vac><vac|, spec L_vac = "
      f"{{0}} u spec(B) u conj spec(B) u {{b_i + conj b_j}}, dev "
      f"{np.max(np.abs(sort_c(pred) - sort_c(np.linalg.eigvals(Lvac)))):.1e}")
Ovac = GOMS["Omega = |vac><vac| (vacuum decay)"]
surv = [np.trace(sla.expm(t * Kg) @ Ovac @ sla.expm(t * Kg).conj().T).real for t in (0, 1, 10, 100)]
check(max(abs(np.array(surv) - 1)) < 1e-12,
      "T3 / prop:vacuum-renewal-trivial-entanglement: Tr(C_t Omega_vac C_t^dag) = 1 for all t, so "
      "m_vac = 0 and mu_vac = infinity -- the vacuum is the exact boundary case of T2's criterion")

# ================================================================ 6. T6 admissibility
print("\n6. T6 (the inverse problem: the cone of admissible stationary states)")


def omega_cand(m, sig):
    K = m["K"]
    num = -(K @ sig + sig @ K.conj().T)
    den = np.trace(m["J"] @ sig).real
    return num / den, den


for lab, m in (("on-line", M_ON), ("off-line", M_OFF)):
    worst = 1e9
    for _ in range(6):
        q = rng.random(m["N"]); q /= q.sum()
        sig = mode_diag(m, q)
        Oc, den = omega_cand(m, sig)
        worst = min(worst, np.linalg.eigvalsh(0.5 * (Oc + Oc.conj().T)).min())
        assert abs(np.trace(Oc).real - 1) < 1e-10
    check(worst > -1e-14,
          f"T6(a) {lab}: every mode-diagonal sigma is ADMISSIBLE (6 random p; worst "
          f"lambda_min(Omega_cand) = {worst:.1e}) and Tr Omega_cand = 1 automatically")

m = M_ON
sig = mode_diag(m, np.array([.4, .3, .15, .1, .05]))
Oc, den = omega_cand(m, sig)
a = -1j * m["ws"]
Mrk = np.conj(a)[:, None] + a[None, :]
check(np.max(np.abs(to_mode(Oc * den, m) - to_mode(sig, m) * Mrk)) < 1e-10,
      "T6 Schur form: Omega_cand_k[n,m] = sigma_k[n,m] (conj(a_n) + a_m), a_n = -i w_n "
      "(entrywise/Hadamard product with a rank-two matrix)")
evM = np.linalg.eigvalsh(Mrk)
check(np.sum(np.abs(evM) > 1e-10) == 2 and evM.min() < -1e-6 and evM.max() > 1e-6,
      f"T6 Schur form: M_nm = conj(a_n)+a_m has rank 2 and signature (1,1) "
      f"(eigenvalues {np.round(evM[np.abs(evM)>1e-10],4)}); x^dag M x = 2 Re(conj(v) u), "
      f"u = sum x_n, v = sum a_n x_n -- genuinely indefinite, so admissibility is a real restriction")
check(np.max(np.abs(Mrk - (0.5 * np.ones((N, N)) + 0.5j * (GAM[:N][:, None] - GAM[:N][None, :])))) < 1e-10,
      "T6 on-line explicit form: M_nm = 1/2 + i(gamma_n - gamma_m)/2 under RH "
      "(real part constant = 2 Im w, imaginary part the ordinate differences)")

# --- random Gibbs-like sigma with random eigenvectors
print("   T6(b): random eigenvectors with Gibbs-like spectrum n^(-beta)/Z")
for lab, m in (("on-line", M_ON), ("off-line", M_OFF)):
    for beta in (1.5, 2.0):
        lamb = np.arange(1, N + 1, dtype=float) ** (-beta)
        lamb /= lamb.sum()
        worst, fails, trials = 0.0, 0, 400
        g = np.random.default_rng(20260919 + int(100 * beta))
        for _ in range(trials):
            U = haar(N, g)
            sig = U @ np.diag(lamb) @ U.conj().T
            Oc, _ = omega_cand(m, sig)
            lo = np.linalg.eigvalsh(0.5 * (Oc + Oc.conj().T)).min()
            if lo < -1e-12:
                fails += 1
            worst = min(worst, lo)
        check(fails == trials,
              f"T6(b) {lab}, beta = {beta}: positivity of Omega_cand FAILS for {fails}/{trials} "
              f"Haar-random eigenbases (spectrum {np.round(lamb,4)}); most negative eigenvalue "
              f"{worst:.4f}. Prescribing the entanglement spectrum with random eigenvectors is "
              f"essentially never admissible")

# --- the exact necessary condition on the eigenbasis
print("   T6(b): a necessary condition on the eigenvectors of sigma")
m = M_ON


def nec_condition(m, sig):
    """Returns (max violation of the 2x2 minor bound, min slack of |H_ab| bound)."""
    lam, Phi = np.linalg.eigh(sig)
    jj = Phi.conj().T @ m["j"]
    Hm = Phi.conj().T @ m["H"] @ Phi
    worst = -1e9
    for a in range(len(lam)):
        for b in range(a + 1, len(lam)):
            need = 0.5 * abs(jj[a]) * abs(jj[b]) * abs(np.sqrt(lam[a]) - np.sqrt(lam[b])) \
                / (np.sqrt(lam[a]) + np.sqrt(lam[b]) + 1e-300)
            worst = max(worst, need - abs(Hm[a, b]))
    return worst


viol_bad, ok_good = [], []
g = np.random.default_rng(777)
lamb = np.arange(1, N + 1, dtype=float) ** (-2.0); lamb /= lamb.sum()
for _ in range(200):
    U = haar(N, g)
    sig = U @ np.diag(lamb) @ U.conj().T
    Oc, _ = omega_cand(m, sig)
    lo = np.linalg.eigvalsh(0.5 * (Oc + Oc.conj().T)).min()
    (viol_bad if lo < -1e-12 else ok_good).append(nec_condition(m, sig))
adm = [nec_condition(m, mode_diag(m, rng.dirichlet(np.ones(N)))) for _ in range(50)]
check(max(adm) < 1e-9,
      f"T6(b) necessary condition VERIFIED on admissible states: for every admissible sigma "
      f"with eigenpairs (lambda_a, phi_a), |H_ab| >= (1/2)|j_a||j_b| "
      f"|sqrt(lam_a)-sqrt(lam_b)|/(sqrt(lam_a)+sqrt(lam_b)) for all a != b "
      f"(50 mode-diagonal sigma, worst margin |H_ab| - bound = {-max(adm):.4f} >= 0)")
cert = sum(1 for v in viol_bad if v > 0)
check(len(ok_good) == 0 and cert > 0,
      f"T6(b) the condition is NECESSARY, not sufficient: of {len(viol_bad)} inadmissible "
      f"Gibbs-like samples (beta = 2, all 200 inadmissible) it certifies {cert} "
      f"({100*cert/len(viol_bad):.0f}%) outright; worst violation {max(viol_bad):.4f}, and no "
      f"admissible sample ever violates it")

lamH, PhiH = np.linalg.eigh(m["H"])
sigH = PhiH @ np.diag(lamb) @ PhiH.conj().T
OcH, _ = omega_cand(m, sigH)
check(np.linalg.eigvalsh(0.5 * (OcH + OcH.conj().T)).min() < -1e-3,
      f"T6(b) sharp corollary: if sigma COMMUTES with H and has non-degenerate spectrum "
      f"(and all j_a != 0) it can never be admissible -- the bound forces |H_ab| > 0. "
      f"Test with sigma = Gibbs in the eigenbasis of H: lambda_min(Omega_cand) = "
      f"{np.linalg.eigvalsh(0.5*(OcH+OcH.conj().T)).min():.4f} < 0")
flag("T6(b) BOST-CONNES READING: the obstruction reappears as FAILURE OF POSITIVITY, not as "
     "mu = infinity. mu stays finite for every finite-rank sigma; what fails is that a prescribed "
     "spectrum in a prescribed eigenbasis U forces |<U n|H|U m>| >= (1/2)|j_n||j_m| "
     "|sqrt(p_n)-sqrt(p_m)|/(sqrt(p_n)+sqrt(p_m)); an eigenbasis commuting with H (e.g. an "
     "'arithmetic' basis chosen independently of the modes) is excluded outright.")

# --- the cone of orbit states
print("   T6(c): the cone generated by the orbit states Phi(psi)")
m = M_ON
for _ in range(3):
    psi = rng.normal(size=N) + 1j * rng.normal(size=N)
    P = orbit(m, psi)
    resid = -(m["K"] @ P + P @ m["K"].conj().T) - np.outer(psi, psi.conj())
    assert np.max(np.abs(resid)) < 1e-10
check(True, "T6(c): -(K Phi(psi) + Phi(psi) K^dag) = |psi><psi| >= 0, so every orbit state is "
            "admissible (Lyapunov identity, dev < 1e-10)")

sig = mode_diag(m, np.array([.4, .3, .15, .1, .05]))
Oc, den = omega_cand(m, sig)
wq, Vq = np.linalg.eigh(0.5 * (Oc + Oc.conj().T))
recon = sum(den * wq[a] * orbit(m, Vq[:, a]) for a in range(N) if wq[a] > 1e-14)
check(np.max(np.abs(recon - sig)) < 1e-10,
      f"T6(c) forward: an admissible sigma is the POSITIVE combination "
      f"sigma = Tr(|j><j|sigma) sum_a omega_a Phi(phi_a) of orbit states over the eigenvectors of "
      f"Omega_cand (dev {np.max(np.abs(recon - sig)):.1e})")

cs = rng.random(4)
psis = [rng.normal(size=N) + 1j * rng.normal(size=N) for _ in range(4)]
comb = sum(c * orbit(m, p) for c, p in zip(cs, psis))
comb /= np.trace(comb).real
Oc2, _ = omega_cand(m, comb)
check(np.linalg.eigvalsh(0.5 * (Oc2 + Oc2.conj().T)).min() > -1e-13,
      f"T6(c) converse: any positive combination of orbit states is admissible "
      f"(lambda_min(Omega_cand) = {np.linalg.eigvalsh(0.5*(Oc2+Oc2.conj().T)).min():.1e})")


def herm_vec(A):
    n = A.shape[0]
    out = [A[i, i].real for i in range(n)]
    for i in range(n):
        for k in range(i + 1, n):
            out += [np.sqrt(2) * A[i, k].real, np.sqrt(2) * A[i, k].imag]
    return np.array(out)


g = np.random.default_rng(31337)
dic = [orbit(m, g.normal(size=N) + 1j * g.normal(size=N)) for _ in range(600)]
A = np.stack([herm_vec(P) for P in dic], axis=1)
U = haar(N, g)
bad = U @ np.diag(lamb) @ U.conj().T
lo_bad = np.linalg.eigvalsh(omega_cand(m, bad)[0]).min()
x_bad, r_bad = nnls(A, herm_vec(bad))
x_good, r_good = nnls(A, herm_vec(sig))
check(lo_bad < -1e-3 and r_bad > 1e-2 and r_good < 1e-6,
      f"T6(c) separation: an admissible sigma is fitted by nonnegative combinations of 600 random "
      f"orbit states to residual {r_good:.1e}, an inadmissible one only to {r_bad:.4f} "
      f"(its lambda_min(Omega_cand) = {lo_bad:.4f}) -- admissible cone = orbit cone, numerically")

rinf, _ = stat_mode(m, OMS_ON["generic full-rank density"])
Oc3, _ = omega_cand(m, rinf)
check(np.max(np.abs(Oc3 - OMS_ON["generic full-rank density"])) < 1e-10,
      f"T6 uniqueness/round trip: Omega_cand(rho_inf(Omega)) = Omega exactly "
      f"(dev {np.max(np.abs(Oc3 - OMS_ON['generic full-rank density'])):.1e})")

# ================================================================ 7. sanity N = 1, 2
print("\n7. sanity: N = 1 closed form and N = 2 by hand")

w1 = np.array([GAM[0] / 2 + 0.25j])
m1 = model(w1)
Om1 = np.array([[1.0 + 0j]])
L1 = superop(m1, Om1)
check(abs(L1[0, 0]) < 1e-14 and abs(m1["G"][0, 0] - 2) < 1e-12 and abs(m1["j"][0] * np.conj(m1["j"][0]) - 0.5) < 1e-12,
      f"N=1: G = 1/(2 Im w) = 2, |j|^2 = 2 Im w = 1/2, L_Omega = "
      f"(-2 Im w + |j|^2) rho = 0 identically; rho_inf = Omega = 1 trivially")
check(abs(mhat_rational(m1, Om1, 0.37) - 0.5 / (0.37 + 0.5)) < 1e-14,
      "N=1: mhat(z) = 2 Im w/(z + 2 Im w) = (1/2)/(z+1/2); the only root of 1 = mhat is z = 0")

m2 = model(GAM[:2] / 2 + 0.25j)
G2 = m2["G"]
detG = (G2[0, 0] * G2[1, 1] - abs(G2[0, 1]) ** 2).real
hand = (G2[0, 0] + G2[1, 1] - 2 * G2[0, 1].real).real / detG
check(abs(np.vdot(m2["j"], m2["j"]).real - hand) < 1e-12,
      f"N=2 by hand: ||j||^2 = 1^T G^(-1) 1 = (G11+G22-2Re G12)/det G = {hand:.6f}")
p2 = np.array([0.7, 0.3])
b2 = 2 * m2["ws"].imag
ev2 = np.linalg.eigvals(superop(m2, mode_diag(m2, p2)))
z_hand = -(b2[0] * p2[1] + b2[1] * p2[0])
zoff = [-1j * np.conj(m2["ws"][0]) + 1j * m2["ws"][1], -1j * np.conj(m2["ws"][1]) + 1j * m2["ws"][0]]
check(match(ev2, np.array([0.0, z_hand] + zoff), 1e-10),
      f"N=2 by hand, mode-diagonal p = {p2}: spec L_Omega = {{0, -(b1 p2 + b2 p1), z_12, z_21}} "
      f"= {{0, {z_hand:.6f}, -1/2 +- i(g2-g1)/2}} (exact solution of "
      f"(z+b1)(z+b2) = p1 b1(z+b2) + p2 b2(z+b1))")
r2, mu2 = stat_mode(m2, mode_diag(m2, p2))
check(np.max(np.abs(r2 - mode_diag(m2, p2))) < 1e-12 and abs(mu2 - 2) < 1e-12,
      f"N=2 by hand: on-line rho_inf = Omega and mu = p1/(1/2) + p2/(1/2) = 2 = {mu2:.6f}")
sp2 = np.sort(np.linalg.eigvalsh(r2))[::-1]
o12 = abs(G2[0, 1]) / np.sqrt(G2[0, 0].real * G2[1, 1].real)
check(abs(sp2[0] - p2[0]) > 1e-3,
      f"N=2 by hand, T5(b) again: mode overlap |<khat_1|khat_2>| = {o12:.6f}, so the spectrum of "
      f"rho_inf is {np.round(sp2,6)} and not p = {p2}; closed form "
      f"(1 +- sqrt((p1-p2)^2 + 4 p1 p2 |o|^2))/2 = "
      f"{np.round([(1+np.sqrt((p2[0]-p2[1])**2+4*p2[0]*p2[1]*o12**2))/2, (1-np.sqrt((p2[0]-p2[1])**2+4*p2[0]*p2[1]*o12**2))/2],6)}")
cf = np.array([(1 + np.sqrt((p2[0] - p2[1]) ** 2 + 4 * p2[0] * p2[1] * o12 ** 2)) / 2,
               (1 - np.sqrt((p2[0] - p2[1]) ** 2 + 4 * p2[0] * p2[1] * o12 ** 2)) / 2])
check(np.max(np.abs(sp2 - cf)) < 1e-12,
      f"N=2 by hand: the corrected entanglement spectrum closed form verified to "
      f"{np.max(np.abs(sp2-cf)):.1e}")

# ================================================================ summary
print(f"\nall {CHECKS} checks passed")
print(f"{len(FLAGS)} loud findings:")
for i, f in enumerate(FLAGS, 1):
    print(f"  ({i}) {f}")
print("\nverdicts: T1 supports | T2 supports | T3 supports (labels transposed; vacuum stationary "
      "for every Omega, so uniqueness fails in the graded model) | T4 supports | "
      "T5(a) supports, T5(c) supports, T5(b) CONTRADICTS | T6 supports (cone, Schur form, "
      "admissibility of mode-diagonal sigma) with a new necessary condition on eigenbases | "
      "T7 not a numerical statement")
