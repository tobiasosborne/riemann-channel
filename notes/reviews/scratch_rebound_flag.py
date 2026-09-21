#!/usr/bin/env python3
"""REFUTE lane: T2(c) formula (4), T3 (graded), T6(d) invariant flags, T6(e) Gibbs flag,
and the cross-check against the numerics lane's |H_ab| necessary condition.

Rebuilt from scratch; nothing imported from scripts/rebound_state.py.
"""
import numpy as np
import scipy.linalg as sla
from scipy.integrate import quad

np.set_printoptions(linewidth=200, precision=10, suppress=False)
N = 0
FAIL = []


def ck(cond, msg, dev=None):
    global N
    N += 1
    if not cond:
        FAIL.append(msg)
    print(f"  {'ok ' if cond else 'FAIL'} {N:3d}  {msg}" + ("" if dev is None else f"   dev={dev:.3e}"))


def build(ws):
    ws = np.asarray(ws, complex)
    y, x = ws.imag, ws.real
    G = 2j * np.sqrt(np.outer(y, y)) / (ws[:, None] - np.conj(ws)[None, :])
    ev, U = np.linalg.eigh(G)
    assert ev.min() > 1e-12, ev
    R = U @ np.diag(np.sqrt(ev)) @ U.conj().T
    Ri = np.linalg.inv(R)
    b = -1j * np.conj(ws)
    B = R @ np.diag(b) @ Ri
    jvec = np.linalg.solve(R.conj().T, np.conj(-1j * np.sqrt(2 * y)))
    H = 0.5j * (B - B.conj().T)
    return dict(ws=ws, x=x, y=y, G=G, R=R, Ri=Ri, b=b, B=B, j=jvec,
                J=np.outer(jvec, jvec.conj()), H=H)


print("=" * 78)
print("T2(c): the Takenaka-Malmquist mean, formula (4)")
print("=" * 78)


def tm_vec(zs):
    """f_N(tau) as a python function, zs = [z_1..z_N], last one is the kernel."""
    zs = np.asarray(zs, complex)
    zN = zs[-1]

    def f(t):
        v = np.sqrt(zN.imag / np.pi) / (t - np.conj(zN))
        for zk in zs[:-1]:
            v = v * (t - zk) / (t - np.conj(zk))
        return v
    return f


def quad_c(g, a, b, **kw):
    return (quad(lambda t: g(t).real, a, b, **kw)[0]
            + 1j * quad(lambda t: g(t).imag, a, b, **kw)[0])


for zs in ([0.25j, 1.3 + 0.25j],
           [0.25j, 1.3 + 0.3j, -0.6 + 0.45j],
           [0.2j, 0.4 + 0.33j, 1.1 + 0.26j, -0.9 + 0.49j]):
    zs = np.asarray(zs, complex)
    f = tm_vec(zs)
    # norm 1?
    nrm = quad_c(lambda th: abs(f(np.tan(th))) ** 2 / np.cos(th) ** 2,
                 -np.pi / 2, np.pi / 2, limit=800).real
    ck(abs(nrm - 1) < 1e-8, f"||f_N||^2 = 1 for zs={list(np.round(zs,3))}", abs(nrm - 1))
    # mean = -i int conj(f) f'  (Plancherel: x on the Fourier side is -i d/dtau)
    eps = 1e-6

    def fp(t):
        return (f(t + eps) - f(t - eps)) / (2 * eps)
    mean_num = (-1j * quad_c(lambda th: np.conj(f(np.tan(th))) * fp(np.tan(th)) / np.cos(th) ** 2,
                             -np.pi / 2, np.pi / 2, limit=800)).real
    zN = zs[-1]
    mean_f = 1 / (2 * zN.imag) + sum(
        2 * (zN.imag + zk.imag) / ((zN.real - zk.real) ** 2 + (zN.imag + zk.imag) ** 2)
        for zk in zs[:-1])
    ck(abs(mean_num - mean_f) < 2e-5 * mean_f,
       f"formula (4) mean = {mean_f:.10f}, numeric {mean_num:.10f}", abs(mean_num - mean_f))

# the >= 1/2 per-summand bound inside the strip 1/4 <= y < 1/2, |dx| <= 1
worst = 1e9
for _ in range(20000):
    r = np.random.default_rng(int(_ * 7 + 1))
    yN, yk = r.uniform(0.25, 0.4999, 2)
    dx = r.uniform(-1, 1)
    worst = min(worst, 2 * (yN + yk) / (dx ** 2 + (yN + yk) ** 2))
ck(worst >= 0.5 - 1e-12, f"each summand of (4) >= 1/2 in the strip with |dx| <= 1 (worst {worst:.6f})")
ck(sum(2 ** -r * 4 ** r for r in range(1, 60)) > 1e15,
   "sum_r 2^-r 4^r diverges, so mu(Omega_inf) = infinity; Tr Omega_inf = sum 2^-r = 1")
ck(abs(sum(2.0 ** -r for r in range(1, 200)) - 1.0) < 1e-12,
   "Omega_inf = sum_r 2^-r |f_r><f_r| is a density: positive, trace class, trace 1")

print()
print("=" * 78)
print("T3: graded space, odd eigen-operators, parity, stationary segment")
print("=" * 78)
ws = [0.25j, 7.0673 + 0.25j, 10.5121 + 0.19j]
m = build(ws)
n = len(ws)
Bt = np.zeros((n + 1, n + 1), complex)
Bt[1:, 1:] = m["B"]
jt = np.zeros(n + 1, complex)
jt[1:] = m["j"]
Jt = np.outer(jt, jt.conj())
ck(np.allclose(-(Bt + Bt.conj().T), Jt), "graded one-exit identity -(Bt+Bt^dag) = |jt><jt|")


def Lg(Om, rho):
    return Bt @ rho + rho @ Bt.conj().T + np.trace(Jt @ rho) * Om


vac = np.zeros(n + 1, complex)
vac[0] = 1
rng = np.random.default_rng(4242)


def rand_dens(k):
    A = rng.normal(size=(k, k)) + 1j * rng.normal(size=(k, k))
    r = A @ A.conj().T
    return r / np.trace(r).real


OMS = {}
Ok = np.zeros((n + 1, n + 1), complex)
Ok[1:, 1:] = rand_dens(n)
OMS["inside K"] = Ok
OMS["full graded"] = rand_dens(n + 1)
Ov = np.zeros((n + 1, n + 1), complex)
Ov[0, 0] = 1
OMS["vacuum"] = Ov
Oc = np.zeros((n + 1, n + 1), complex)          # with vac-K coherences
v = np.zeros(n + 1, complex)
v[0] = 0.6
v[1:] = 0.8 * m["R"][:, 0] / np.linalg.norm(m["R"][:, 0])
Oc = np.outer(v, v.conj())
Oc = Oc / np.trace(Oc).real
OMS["coherent"] = Oc

for nm, Om in OMS.items():
    for k in range(n):
        e = np.zeros(n + 1, complex)
        e[1:] = m["R"][:, k]
        e = e / np.linalg.norm(e)
        X = np.outer(e, vac.conj())          # |e_n><vac|
        Y = np.outer(vac, e.conj())          # |vac><e_n|
        ck(np.allclose(Lg(Om, X), m["b"][k] * X, atol=1e-12),
           f"[{nm}] L(|e_{k}><vac|) = -i conj(w) |e><vac|  (T3(a) eq 5)",
           float(np.max(np.abs(Lg(Om, X) - m["b"][k] * X))))
        ck(np.allclose(Lg(Om, Y), np.conj(m["b"][k]) * Y, atol=1e-12),
           f"[{nm}] L(|vac><e_{k}|) = +i w |vac><e|  (T3(a) eq 5)")
    ck(np.allclose(Lg(Om, np.outer(vac, vac.conj())), 0, atol=1e-14),
       f"[{nm}] the vacuum is stationary for EVERY rebound (T3(c))")
    # parity
    P = np.diag([1.0] + [-1.0] * n).astype(complex)
    rho = rand_dens(n + 1)
    par = np.allclose(Lg(Om, P @ rho @ P), P @ Lg(Om, rho) @ P, atol=1e-12)
    even = np.allclose(P @ Om @ P, Om, atol=1e-14)
    ck(par == even, f"[{nm}] generator parity-covariant IFF P Om P = Om (T3(b)); "
                    f"even={even}, covariant={par}")

# T3(c): the stationary segment for Om inside K, and uniqueness when q > 0
def superLg(Om):
    k = n + 1
    I = np.eye(k)
    return (np.kron(Bt, I) + np.kron(I, Bt.conj()) + np.outer(Om.reshape(-1), Jt.T.reshape(-1)))


for nm, Om in OMS.items():
    L = superLg(Om)
    ev = np.abs(np.linalg.eigvals(L))
    dimker = int(np.sum(ev < 1e-9))
    q = Om[0, 0].real
    expect = 2 if q < 1e-12 else 1
    ck(dimker == expect,
       f"[{nm}] dim ker L = {dimker}, expected {expect} (q = <vac|Om|vac> = {q:.4f})  (T3(c))")

# the segment itself
Om = OMS["inside K"]
rinf = sla.solve_continuous_lyapunov(m["B"], -Om[1:, 1:])
rinf = rinf / np.trace(rinf).real
for qq in (0.0, 0.37, 1.0):
    S = np.zeros((n + 1, n + 1), complex)
    S[0, 0] = qq
    S[1:, 1:] = (1 - qq) * rinf
    ck(np.allclose(Lg(Om, S), 0, atol=1e-12),
       f"[inside K] q={qq}: q|vac><vac| + (1-q)(0 + rho_inf) is stationary (eq 6)",
       float(np.max(np.abs(Lg(Om, S)))))
# and vacuum mass is conserved
rho0 = rand_dens(n + 1)
ev = sla.expm(200 * superLg(Om)) @ rho0.reshape(-1)
rho60 = ev.reshape(n + 1, n + 1)
ck(abs(rho60[0, 0].real - rho0[0, 0].real) < 1e-8,
   f"[inside K] vacuum mass conserved: q(0)={rho0[0,0].real:.6f} -> q(200)={rho60[0,0].real:.6f}")
Sp = np.zeros((n + 1, n + 1), complex)
Sp[0, 0] = rho0[0, 0].real
Sp[1:, 1:] = (1 - rho0[0, 0].real) * rinf
ck(np.allclose(rho60, Sp, atol=1e-7),
   "[inside K] e^{200 L} rho_0 -> q|vac><vac| + (1-q) rho_inf (T3(c) convergence)",
   float(np.max(np.abs(rho60 - Sp))))
# q > 0 rebound: everything drains to the vacuum
Omq = 0.3 * Ov + 0.7 * Ok
ev = sla.expm(400 * superLg(Omq)) @ rho0.reshape(-1)
r400 = ev.reshape(n + 1, n + 1)
ck(np.allclose(r400, np.outer(vac, vac.conj()), atol=1e-6),
   f"[q>0] every state -> |vac><vac| (T3(c) second half); residual "
   f"{np.max(np.abs(r400 - np.outer(vac, vac.conj()))):.2e}")

print()
print("=" * 78)
print("T6(d): invariant flags give EVERY finite density spectrum, without RH")
print("=" * 78)
for label, ws in [("N=3 off-line", [0.0 + 0.31j, 7.0673 + 0.19j, 10.5121 + 0.42j]),
                  ("N=4 off-line", [0.0 + 0.31j, 7.0673 + 0.19j, 10.5121 + 0.42j, 12.5379 + 0.11j]),
                  ("N=4 on-line", [0.0 + 0.25j, 7.0673 + 0.25j, 10.5121 + 0.25j, 12.5379 + 0.25j])]:
    m = build(ws)
    nn = len(ws)
    # Gram-Schmidt adapted to the flag V_1 c ... c V_N  (columns of R are the modes)
    U, _ = np.linalg.qr(m["R"])
    for k in range(nn):
        Vk = m["R"][:, :k + 1]
        Pk = Vk @ np.linalg.pinv(Vk)
        Qk = -(m["B"] @ Pk + Pk @ m["B"].conj().T)
        ck(np.linalg.eigvalsh(Qk).min() > -1e-11,
           f"[{label}] Q_k = -(B P_k + P_k B^*) >= 0 for k={k+1}  (eq 20)",
           float(np.linalg.eigvalsh(Qk).min()))
        ck(abs(np.trace(Qk).real - 2 * np.sum(m["y"][:k + 1])) < 1e-10,
           f"[{label}] Tr Q_k = 2 sum_{{n<=k}} y_n for k={k+1}  (eq 20)",
           abs(np.trace(Qk).real - 2 * np.sum(m["y"][:k + 1])))
        ck(np.linalg.matrix_rank(Qk, tol=1e-9) == 1,
           f"[{label}] Q_k has rank 1 (= j_k^* j_k, one-dimensional exit) for k={k+1}")
    for p in ([0.5, 0.3, 0.2], [0.6, 0.25, 0.15], [1/3, 1/3, 1/3],
              [0.4, 0.3, 0.2, 0.1], [0.25] * 4, [0.7, 0.1, 0.1, 0.1]):
        if len(p) != nn:
            continue
        p = np.array(sorted(p, reverse=True))
        sig = U[:, :nn] @ np.diag(p.astype(complex)) @ U[:, :nn].conj().T
        Q = -(m["B"] @ sig + sig @ m["B"].conj().T)
        r = np.trace(Q).real
        ck(np.allclose(np.sort(np.linalg.eigvalsh(sig))[::-1], p, atol=1e-12),
           f"[{label}] sigma has EXACTLY the prescribed spectrum {list(np.round(p,4))}",
           float(np.max(np.abs(np.sort(np.linalg.eigvalsh(sig))[::-1] - p))))
        ck(np.linalg.eigvalsh(Q).min() > -1e-11,
           f"[{label}] Q_sigma >= 0 for p={list(np.round(p,4))} (lam_min {np.linalg.eigvalsh(Q).min():+.3e})")
        ck(abs(r - 2 * np.sum(p * m["y"])) < 1e-10,
           f"[{label}] r = Tr Q_sigma = 2 sum p_n y_n = {2*np.sum(p*m['y']):.8f}")
        Om = Q / r
        ck(abs(np.trace(Om).real - 1) < 1e-12 and np.linalg.eigvalsh(Om).min() > -1e-11,
           f"[{label}] Omega = Q_sigma/r IS a genuine density (>=0, trace 1)")
        ck(np.allclose(m["B"] @ sig + sig @ m["B"].conj().T + np.trace(m["J"] @ sig) * Om, 0, atol=1e-11),
           f"[{label}] sigma is stationary for L_Omega",
           float(np.max(np.abs(m["B"] @ sig + sig @ m["B"].conj().T + np.trace(m["J"] @ sig) * Om))))
        ck(abs(np.trace(sla.solve_continuous_lyapunov(m["B"], -Om)).real - 1 / r) < 1e-8,
           f"[{label}] mu_Omega = 1/r = {1/r:.8f}  (eq 16)")
        rk = np.linalg.matrix_rank(Om, tol=1e-9)
        npos = int(np.sum(np.diff(np.append(p, 0.0)) < -1e-12))
        ck(rk == npos,
           f"[{label}] rank Omega = #{{p_k > p_{{k+1}}}} = {npos}, got {rk}  (T6(d))")
        if np.allclose(p, p[0]):
            ck(rk == 1, f"[{label}] FLAT spectrum -> PURE rebound (T6(d), ledger 31)")
        # cross-check with the numerics lane's necessary condition |H_ab| >= ...
        lam, phi = np.linalg.eigh(sig)
        ja = phi.conj().T @ m["j"]
        Hm = phi.conj().T @ m["H"] @ phi
        ok = True
        for a in range(nn):
            for bb in range(nn):
                if a == bb:
                    continue
                la, lb = lam[a], lam[bb]
                if la + lb <= 0:
                    continue
                need = 0.5 * abs(ja[a]) * abs(ja[bb]) * abs(np.sqrt(la) - np.sqrt(lb)) / (np.sqrt(la) + np.sqrt(lb))
                if abs(Hm[a, bb]) < need - 1e-9:
                    ok = False
        ck(ok, f"[{label}] the numerics lane's |H_ab| bound HOLDS on the flag sigma (consistent with T6(d))")
        comm = np.max(np.abs(m["H"] @ sig - sig @ m["H"]))
        ck(comm > 1e-6 or np.allclose(p, p[0]),
           f"[{label}] non-flat flag sigma does NOT commute with H (||[H,sigma]||={comm:.4f}): "
           "no clash with the numerics lane's 'commuting + non-degenerate is never admissible'")

# the numerics lane's sharp corollary, re-derived here
print()
print("--- cross-check: sigma commuting with H, non-degenerate spectrum, is never admissible")
m = build([0.0 + 0.25j, 7.0673 + 0.25j, 10.5121 + 0.19j, 12.5379 + 0.3j])
lamH, phiH = np.linalg.eigh(m["H"])
for beta in (1.5, 2.0):
    d = np.array([(k + 1.0) ** -beta for k in range(4)])
    d = d / d.sum()
    sig = phiH @ np.diag(d.astype(complex)) @ phiH.conj().T
    Q = -(m["B"] @ sig + sig @ m["B"].conj().T)
    ck(np.linalg.eigvalsh(Q).min() < -1e-6,
       f"Gibbs beta={beta} in the eigenbasis of H is NOT admissible "
       f"(lam_min {np.linalg.eigvalsh(Q).min():.4f}) -- numerics lane check 138 reproduced")

print()
print("=" * 78)
print("T6(e): the infinite flag with Gibbs weights; r = 2 sum d_n y_n, and r = 1/2 under RH")
print("=" * 78)
for label, ws in [("on-line (RH)", [0.0 + 0.25j] + [g / 2 + 0.25j for g in
                                                    (14.1347, 21.0220, 25.0109, 30.4249, 32.9351,
                                                     37.5862, 40.9187, 43.3271, 48.0052)]),
                  ("off-line", [0.0 + 0.31j] + [g / 2 + 1j * yy for g, yy in
                                                zip((14.1347, 21.0220, 25.0109, 30.4249, 32.9351,
                                                     37.5862, 40.9187, 43.3271, 48.0052),
                                                    (0.19, 0.42, 0.11, 0.27, 0.33, 0.22, 0.45, 0.16, 0.29))])]:
    m = build(ws)
    K = len(ws)
    U, _ = np.linalg.qr(m["R"])
    for beta in (1.5, 2.0, 3.0):
        d = np.array([(k + 1.0) ** -beta for k in range(K)])
        d = d / d.sum()
        sig = U @ np.diag(d.astype(complex)) @ U.conj().T
        Q = -(m["B"] @ sig + sig @ m["B"].conj().T)
        r = np.trace(Q).real
        ck(np.linalg.eigvalsh(Q).min() > -1e-11,
           f"[{label}] truncated Gibbs beta={beta} on the flag IS admissible "
           f"(lam_min {np.linalg.eigvalsh(Q).min():+.3e})")
        ck(np.allclose(np.sort(np.linalg.eigvalsh(sig))[::-1], np.sort(d)[::-1], atol=1e-12),
           f"[{label}] spectrum is exactly the (truncated, renormalised) Gibbs list, beta={beta}")
        ck(abs(r - 2 * np.sum(d * m["y"])) < 1e-10,
           f"[{label}] r = 2 sum d_n y_n = {2*np.sum(d*m['y']):.8f}, beta={beta}")
        if "on-line" in label:
            ck(abs(r - 0.5) < 1e-10 and abs(1 / r - 2.0) < 1e-9,
               f"[{label}] under RH r = 1/2 and mu_Omega = 2 EXACTLY, beta={beta} (T6(e))",
               abs(r - 0.5))
        Om = Q / r
        ck(np.linalg.matrix_rank(Om, tol=1e-9) == K,
           f"[{label}] Gibbs weights strictly decreasing -> rebound has full rank {K} (mixed), beta={beta}")
    hs = [float(np.sum([(k + 1.0) ** -1 for k in range(M)])) for M in (10**4, 10**6)]
    ck(hs[1] > hs[0] + 4.5,
       f"at beta = 1 the harmonic partial sums grow without bound ({hs[0]:.3f} -> {hs[1]:.3f}): "
       "no normal Gibbs density (prop:normal-kms-gibbs, trace-normalisation obstruction)")

print()
print(f"TOTAL {N} checks, {len(FAIL)} failures")
for f in FAIL:
    print("   FAILED:", f)
