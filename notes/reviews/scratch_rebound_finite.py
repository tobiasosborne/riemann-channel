#!/usr/bin/env python3
"""REFUTE lane: finite-mode checks of T2(b), T4(a)(b)(c), T5(a)(b)(c), T6(c).

Built from scratch in the PROVER's normalised-mode coordinates (his eqs (3),
(7), (8), (10)-(14), (18)-(19)).  Independent of scripts/rebound_state.py:
here the synthesis map is R = G^{1/2} with G_nm = 2i sqrt(y_n y_m)/(w_n - conj w_m)
(the NORMALISED Gram, where the two lanes' conventions coincide), the exit
covector is j e_n = -i sqrt(2 y_n), and everything is recomputed by hand.
"""
import itertools
import numpy as np
import scipy.linalg as sla

np.set_printoptions(linewidth=200, precision=10, suppress=False)
N = 0
FAIL = []


def ck(cond, msg, dev=None):
    global N
    N += 1
    if not cond:
        FAIL.append(msg)
    print(f"  {'ok ' if cond else 'FAIL'} {N:3d}  {msg}" + ("" if dev is None else f"   dev={dev:.3e}"))


def msort(v):
    v = np.asarray(v, complex)
    return v[np.lexsort((np.round(v.imag, 8), np.round(v.real, 8)))]


def build(ws):
    """Normalised-mode finite model.  Returns dict."""
    ws = np.asarray(ws, complex)
    y, x = ws.imag, ws.real
    G = 2j * np.sqrt(np.outer(y, y)) / (ws[:, None] - np.conj(ws)[None, :])
    ev, U = np.linalg.eigh(G)
    assert ev.min() > 1e-12
    R = U @ np.diag(np.sqrt(ev)) @ U.conj().T          # synthesis: e_n = R[:, n]
    Ri = np.linalg.inv(R)
    b = -1j * np.conj(ws)                              # B e_n = b_n e_n
    B = R @ np.diag(b) @ Ri
    jvec = R.conj().T @ np.zeros(len(ws))              # placeholder
    # j psi = <jvec, psi> = jvec^dagger psi ; j e_n = -i sqrt(2 y_n)
    jvec = np.linalg.solve(R.conj().T, np.conj(-1j * np.sqrt(2 * y)))
    return dict(ws=ws, x=x, y=y, G=G, R=R, Ri=Ri, b=b, B=B, j=jvec,
                J=np.outer(jvec, jvec.conj()), lam=b[:, None] + np.conj(b)[None, :],
                q=2 * np.sqrt(np.outer(y, y)))


def synth(m, W):
    """sum_nm W_nm |e_n><e_m|  as a matrix in the ambient ON basis."""
    return m["R"] @ W @ m["R"].conj().T


def coeff(m, X):
    return m["Ri"] @ X @ m["Ri"].conj().T


def superL(m, Om):
    n = len(m["ws"])
    I = np.eye(n)
    # vec row-major: vec(A X B) = (A kron B^T) vec(X)
    return (np.kron(m["B"], I) + np.kron(I, m["B"].conj())
            + np.outer(Om.reshape(-1), m["J"].T.reshape(-1)))


ONLINE = [0.25j, 7.0673 + 0.25j, 10.5121 + 0.25j, 12.5379 + 0.25j]   # gamma/2, RH
OFFLINE = [0.0 + 0.25j, 7.0673 + 0.19j, 10.5121 + 0.31j, 12.5379 + 0.225j]
COLLIDE = [0.0 + 0.25j, 1.0 + 0.25j, 2.0 + 0.25j]     # lambda_12 = lambda_23: collision
SETS = {"online": ONLINE, "offline": OFFLINE, "collide": COLLIDE,
        "mixed": [0.3 + 0.4j, -1.1 + 0.12j, 2.2 + 0.47j]}

rng = np.random.default_rng(31337)

print("=" * 78)
print("Model sanity: the one-exit identity and the eigen-structure")
print("=" * 78)
M = {}
for name, ws in SETS.items():
    m = build(ws)
    M[name] = m
    ck(np.allclose(-(m["B"] + m["B"].conj().T), m["J"]),
       f"[{name}] -(B + B^dag) = |j><j| (rank one)",
       float(np.max(np.abs(-(m["B"] + m["B"].conj().T) - m["J"]))))
    ck(np.allclose(msort(np.linalg.eigvals(m["B"])), msort(m["b"])),
       f"[{name}] spec B = {{-i conj w_n}}")
    jn = m["j"].conj() @ m["R"]
    ck(np.allclose(jn, -1j * np.sqrt(2 * m["y"])),
       f"[{name}] j e_n = -i sqrt(2 y_n) != 0 (C3)")

print()
print("=" * 78)
print("T2(b) eq (3): mu and rho_inf from the Gram matrix")
print("=" * 78)
for name in SETS:
    m = M[name]
    a = 1j * np.conj(m["ws"])                       # a_n = i conj w_n = y_n + i x_n
    for trial in range(3):
        A = rng.normal(size=(len(m["ws"]),) * 2) + 1j * rng.normal(size=(len(m["ws"]),) * 2)
        W = A @ A.conj().T
        Om = synth(m, W)
        W = W / np.trace(Om).real
        Om = Om / np.trace(Om).real
        ck(abs(np.trace(W @ m["G"]) - 1) < 1e-12, f"[{name}] Tr(W G) = 1 (prover's normalisation)")
        denom = a[:, None] + np.conj(a)[None, :]
        mu_f = np.sum(W * m["G"].T / denom).real
        mu_num = np.trace(sla.solve_continuous_lyapunov(m["B"], -Om)).real
        ck(abs(mu_f - mu_num) < 1e-10 * mu_num, f"[{name}] mu = sum w_nm G_mn/(a_n + conj a_m)  (eq 3)",
           abs(mu_f - mu_num))
        rho_f = synth(m, W / denom) / mu_f
        rho_num = sla.solve_continuous_lyapunov(m["B"], -Om) / mu_num
        ck(np.allclose(rho_f, rho_num, atol=1e-10),
           f"[{name}] rho_inf = mu^-1 sum w_nm/(a_n+conj a_m)|e_n><e_m| (eq 3)",
           float(np.max(np.abs(rho_f - rho_num))))
        ck(abs(np.trace(m["J"] @ rho_f).real - 1 / mu_f) < 1e-10,
           f"[{name}] ell(rho_inf) = 1/mu  (T6(a) eq 16)")

print()
print("=" * 78)
print("T4(a)/(b)/(c): determinant identity (8), secular equation (9), Gram m-hat (10)")
print("=" * 78)
for name in SETS:
    m = M[name]
    n = len(m["ws"])
    A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    W = A @ A.conj().T
    Om = synth(m, W)
    W = W / np.trace(Om).real
    Om = Om / np.trace(Om).real
    L0 = superL(m, np.zeros((n, n), complex))
    LO = superL(m, Om)
    # (10): m-hat from the Gram coefficients
    for z in (0.83 + 0.21j, -0.31 + 1.7j, 2.0):
        mh = np.sum(2 * np.sqrt(np.outer(m["y"], m["y"])) * W / (z - m["lam"]))
        mh_res = np.trace(m["J"] @ np.linalg.solve(z * np.eye(n * n) - L0,
                                                   Om.reshape(-1)).reshape(n, n))
        ck(abs(mh - mh_res) < 1e-10, f"[{name}] m-hat (10) = ell (z-A)^-1 Omega at z={z}", abs(mh - mh_res))
        d1 = np.linalg.det(z * np.eye(n * n) - LO)
        d2 = np.linalg.det(z * np.eye(n * n) - L0) * (1 - mh)
        ck(abs(d1 - d2) < 1e-8 * max(1.0, abs(d1)),
           f"[{name}] det(z-L_Om) = det(z-L_0)(1 - m-hat(z)) at z={z}", abs(d1 - d2))
    # (8) with grouped multiplicities, evaluated on a grid INCLUDING a collision point
    lam_flat = m["lam"].reshape(-1)
    uniq = []
    for lv in lam_flat:
        if not any(abs(lv - u) < 1e-9 for u in uniq):
            uniq.append(lv)
    print(f"     [{name}] {n*n} pair eigenvalues, {len(uniq)} distinct"
          + ("   <-- COLLISION present" if len(uniq) < n * n else ""))
    for z in (1.3 - 0.4j,):
        prod = np.prod([(z - u) ** sum(1 for lv in lam_flat if abs(lv - u) < 1e-9) for u in uniq])
        rl = []
        for u in uniq:
            # r_lambda = ell(P_lambda Omega): P_lambda picks the coefficient block
            mask = np.abs(m["lam"] - u) < 1e-9
            rl.append(np.sum((W * m["q"])[mask]))
        det8 = prod * (1 - sum(r / (z - u) for r, u in zip(rl, uniq)))
        ck(abs(det8 - np.linalg.det(z * np.eye(n * n) - LO)) < 1e-7 * max(1, abs(det8)),
           f"[{name}] eq (8) det = prod (z-lam)^d (1 - sum r_lam/(z-lam)) at z={z}",
           abs(det8 - np.linalg.det(z * np.eye(n * n) - LO)))
    # persistence at a COLLIDED eigenvalue: algebraic multiplicity d-1 when r != 0
    if len(uniq) < n * n:
        for u in uniq:
            d = sum(1 for lv in lam_flat if abs(lv - u) < 1e-9)
            if d >= 2:
                mask = np.abs(m["lam"] - u) < 1e-9
                r = np.sum((W * m["q"])[mask])
                ev = np.linalg.eigvals(LO)
                mult = int(np.sum(np.abs(ev - u) < 1e-7))
                ck((abs(r) > 1e-12 and mult == d - 1) or (abs(r) < 1e-12 and mult >= d),
                   f"[{name}] collided lambda={u:.4f} d={d}, r!=0 -> multiplicity d-1={d-1}, got {mult}")
    # T4(a): every eigen-operator has ell(E_nm) != 0 (first disjunct never fires, ungraded)
    ck(np.all(np.abs(m["q"]) > 1e-9), f"[{name}] ell(E_nm) != 0 for all n,m: first disjunct never fires")
    # eigenspaces of dim >= 2 still give d-1 operators in ker ell
    ck(True, f"[{name}] (see collision rows above for the ker-ell replacement)")

print()
print("=" * 78)
print("T5(a),(b),(c): mode-diagonal rebound")
print("=" * 78)
for name in ("online", "offline"):
    m = M[name]
    n = len(m["ws"])
    for trial in range(4):
        p = rng.dirichlet(np.ones(n))
        W = np.diag(p.astype(complex))
        Om = synth(m, W)
        ck(abs(np.trace(Om).real - 1) < 1e-12, f"[{name}] modal mixture has trace 1 (Tr(WG)=Sum p_n G_nn=1)")
        mu = float(np.sum(p / (2 * m["y"])))
        rho = synth(m, np.diag((p / (2 * m["y"]) / mu).astype(complex)))
        rho_num = sla.solve_continuous_lyapunov(m["B"], -Om)
        ck(abs(np.trace(rho_num).real - mu) < 1e-10, f"[{name}] mu = sum p_n/(2 y_n) (eq 11)")
        ck(np.allclose(rho, rho_num / mu, atol=1e-12), f"[{name}] rho_inf (eq 11)",
           float(np.max(np.abs(rho - rho_num / mu))))
        same = np.allclose(rho, Om, atol=1e-10)
        equal_widths = np.allclose(m["y"][p > 1e-12], m["y"][p > 1e-12][0])
        ck(same == equal_widths,
           f"[{name}] rho_inf = Omega IFF all widths with p_n>0 equal (T5(a)) [{same}]")
        # T5(b): spectrum is the GRAM spectrum, not p
        r = p / (2 * m["y"]) / mu
        sp_gram = np.sort(np.linalg.eigvalsh(
            np.diag(np.sqrt(r)) @ m["G"] @ np.diag(np.sqrt(r))))[::-1]
        sp_true = np.sort(np.linalg.eigvalsh(rho_num / mu))[::-1]
        ck(np.allclose(sp_gram, sp_true, atol=1e-11),
           f"[{name}] spec rho_inf = spec(D_r^{{1/2}} G D_r^{{1/2}}) (T5(b) eq 12)",
           float(np.max(np.abs(sp_gram - sp_true))))
        ck(not np.allclose(sp_true, np.sort(r)[::-1], atol=1e-3),
           f"[{name}] spec rho_inf != {{p_n/(2y_n)/mu}}: the BRIEF's T5(b) is FALSE "
           f"(max gap {np.max(np.abs(sp_true - np.sort(r)[::-1])):.4f})")

# T5(b) prover's explicit 2-mode example
m2 = build([0.25j, 1.0 + 0.25j])
p = np.array([0.5, 0.5])
mu = float(np.sum(p / (2 * m2["y"])))
r = p / (2 * m2["y"]) / mu
sp = np.sort(np.linalg.eigvalsh(np.diag(np.sqrt(r)) @ m2["G"] @ np.diag(np.sqrt(r))))[::-1]
ck(abs(abs(m2["G"][0, 1]) - 1 / np.sqrt(5)) < 1e-13, "T5(b) example |G_12| = 1/sqrt 5")
ck(np.allclose(sp, [(1 + 5 ** -0.5) / 2, (1 - 5 ** -0.5) / 2]),
   f"T5(b) example spectrum {sp[0]:.10f}, {sp[1]:.10f} = (1 +- 1/sqrt5)/2 (prover's numbers)")

print()
print("--- T5(c): characteristic polynomial (13) and the RH spectrum (14)")
for name in ("online", "offline"):
    m = M[name]
    n = len(m["ws"])
    p = rng.dirichlet(np.ones(n))
    Om = synth(m, np.diag(p.astype(complex)))
    LO = superL(m, Om)
    h = 2 * m["y"]
    # roots of (13)
    roots = [m["lam"][i, j] for i in range(n) for j in range(n) if i != j]
    Mdiag = -np.diag(h) + np.outer(p, h)
    roots += list(np.linalg.eigvals(Mdiag))
    ev = np.linalg.eigvals(LO)
    ck(np.allclose(msort(roots), msort(ev), atol=1e-9),
       f"[{name}] char poly (13): spec = {{lam_nm, n!=m}} u spec(-diag h + p h^T)",
       float(np.max(np.abs(msort(roots) - msort(ev)))))
    ck(np.min(np.abs(ev)) < 1e-10, f"[{name}] 0 is an eigenvalue (stationary state)")
    dm = np.linalg.eigvals(Mdiag)
    ck(np.allclose(dm.imag, 0, atol=1e-10) and np.all(dm.real < 1e-10),
       f"[{name}] diagonal-block roots are real and <= 0")
    if name == "online":
        ck(np.allclose(np.sort(dm.real), np.sort([-0.5] * (n - 1) + [0.0]), atol=1e-10),
           f"[{name}] under RH: {{0}} u {{-1/2}}^(N-1)  (eq 14)")
        offs = np.array([m["lam"][i, j] for i in range(n) for j in range(n) if i != j])
        ck(np.allclose(offs.real, -0.5),
           f"[{name}] under RH off-diagonals have Re = -1/2, freq x_m - x_n (eq 14)")
        for z in (0.4, 1.9 + 0.3j):
            mh = np.sum(2 * np.sqrt(np.outer(m["y"], m["y"])) * np.diag(p) / (z - m["lam"]))
            ck(abs(mh - 0.5 / (z + 0.5)) < 1e-12,
               f"[{name}] under RH m-hat(z) = (1/2)/(z+1/2) for EVERY p, at z={z}", abs(mh - 0.5 / (z + 0.5)))

print()
print("=" * 78)
print("T6(c): Schur criterion (18), the rank-two indefinite matrix, bound (19)")
print("=" * 78)
for name in SETS:
    m = M[name]
    n = len(m["ws"])
    a = 1j * np.conj(m["ws"])
    Mmat = a[:, None] + np.conj(a)[None, :]
    ck(np.allclose(Mmat, Mmat.conj().T), f"[{name}] (a_n + conj a_m) is Hermitian")
    ck(np.linalg.matrix_rank(Mmat, tol=1e-9) <= 2, f"[{name}] rank <= 2")
    evM = np.sort(np.linalg.eigvalsh(Mmat))
    ck(evM[0] < -1e-9 < 1e-9 < evM[-1], f"[{name}] indefinite: signature (1,1) "
       f"[{evM[0]:.4f}, {evM[-1]:.4f}]")
    for (i, k) in itertools.combinations(range(n), 2):
        d2 = 4 * m["y"][i] * m["y"][k] - abs(Mmat[i, k]) ** 2
        pred = -(m["y"][i] - m["y"][k]) ** 2 - (m["x"][i] - m["x"][k]) ** 2
        ck(abs(d2 - pred) < 1e-12, f"[{name}] 2x2 det = -(dy)^2-(dx)^2 < 0 for ({i},{k})")
    # (18) <=> positivity of Q_sigma, checked on random sigma
    ok18 = 0
    for trial in range(300):
        A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        S = A @ A.conj().T
        sig = synth(m, S)
        S = S / np.trace(sig).real
        sig = sig / np.trace(sig).real
        Q = -(m["B"] @ sig + sig @ m["B"].conj().T)
        lhs = np.linalg.eigvalsh(Q).min() > -1e-11
        rhs = np.linalg.eigvalsh(Mmat * S).min() > -1e-11
        if lhs == rhs:
            ok18 += 1
        # (19) necessary condition
        if lhs:
            for (i, k) in itertools.combinations(range(n), 2):
                l19 = abs(S[i, k]) ** 2 * ((m["y"][i] + m["y"][k]) ** 2 + (m["x"][i] - m["x"][k]) ** 2)
                r19 = 4 * m["y"][i] * m["y"][k] * S[i, i].real * S[k, k].real
                assert l19 <= r19 + 1e-9, "(19) violated on an admissible sigma"
    ck(ok18 == 300, f"[{name}] (18) Q_sigma >= 0 <=> ((a_n+conj a_m) s_nm) >= 0 on 300 random sigma")
    # mode-diagonal sigma always admissible
    for trial in range(20):
        pp = rng.dirichlet(np.ones(n))
        S = np.diag((pp / np.sum(pp / (2 * m["y"]) * 0 + 1)).astype(complex))
        ck(np.linalg.eigvalsh(Mmat * S).min() > -1e-14 if trial == 0 else True,
           f"[{name}] mode-diagonal sigma admissible (diagonal 2 y_n p_n >= 0)" if trial == 0 else "")
        break
    # pure nonmodal superposition is NOT admissible
    c = rng.normal(size=n) + 1j * rng.normal(size=n)
    psi = m["R"] @ c
    psi = psi / np.linalg.norm(psi)
    Qp = -(m["B"] @ np.outer(psi, psi.conj()) + np.outer(psi, psi.conj()) @ m["B"].conj().T)
    ck(np.linalg.eigvalsh(Qp).min() < -1e-8,
       f"[{name}] a non-modal pure state is NOT admissible (T6(c) sharp restriction)",
       float(np.linalg.eigvalsh(Qp).min()))
    # a modal pure state IS admissible
    e0 = m["R"][:, 0]
    Qm = -(m["B"] @ np.outer(e0, e0.conj()) + np.outer(e0, e0.conj()) @ m["B"].conj().T)
    ck(np.linalg.eigvalsh(Qm).min() > -1e-12, f"[{name}] a modal pure state IS admissible")

print()
print(f"TOTAL {N} checks, {len(FAIL)} failures")
for f in FAIL:
    print("   FAILED:", f)


print()
print("=" * 78)
print("ADVERSARIAL PROBES (refuter additions)")
print("=" * 78)
# (P1) off-diagonal / diagonal eigenvalue COLLISION with a mode-diagonal rebound:
#      does (13) survive?   x_1 = x_2, y_1 + y_2 = 2 y_3
mp = build([0.0 + 0.10j, 0.0 + 0.40j, 3.0 + 0.25j])
lam = mp["lam"]
ck(abs(lam[0, 1] - lam[2, 2]) < 1e-12,
   f"probe: lambda_12 = {lam[0,1]:.4f} collides with the DIAGONAL lambda_33 = {lam[2,2]:.4f}")
for p in ([0.5, 0.3, 0.2], [1 / 3] * 3):
    p = np.array(p)
    Om = synth(mp, np.diag(p.astype(complex)))
    LO = superL(mp, Om)
    h = 2 * mp["y"]
    roots = [lam[i, j] for i in range(3) for j in range(3) if i != j]
    roots += list(np.linalg.eigvals(-np.diag(h) + np.outer(p, h)))
    ck(np.allclose(msort(roots), msort(np.linalg.eigvals(LO)), atol=1e-9),
       f"probe: (13) still exact at an off-diagonal/diagonal collision, p={list(p)}",
       float(np.max(np.abs(msort(roots) - msort(np.linalg.eigvals(LO))))))

# (P2) finite-rank / pure NON-modal rebound on a 4-mode space: is the stationary state
#      still unique and attracting (T2(a) uniqueness with Omega of small support)?
m4 = M["offline"]
for tag, Om in [("rank-1 modal", synth(m4, np.diag([1.0, 0, 0, 0]).astype(complex))),
                ("rank-1 non-modal", None), ("rank-2", None)]:
    if Om is None:
        c = rng.normal(size=4) + 1j * rng.normal(size=4)
        psi = m4["R"] @ c
        psi = psi / np.linalg.norm(psi)
        Om = np.outer(psi, psi.conj())
        if tag == "rank-2":
            c2 = rng.normal(size=4) + 1j * rng.normal(size=4)
            p2 = m4["R"] @ c2
            p2 = p2 / np.linalg.norm(p2)
            Om = 0.5 * Om + 0.5 * np.outer(p2, p2.conj())
    Om = Om / np.trace(Om).real
    LO = superL(m4, Om)
    ev = np.linalg.eigvals(LO)
    ck(int(np.sum(np.abs(ev) < 1e-9)) == 1,
       f"probe [{tag} Omega]: dim ker L_Omega = 1 (T2(a) uniqueness holds for small-support Omega)")
    gap = -np.max(ev.real[np.abs(ev) > 1e-9])
    A0 = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    r0 = A0 @ A0.conj().T
    r0 = r0 / np.trace(r0).real
    rT = (sla.expm(300 * LO) @ r0.reshape(-1)).reshape(4, 4)
    rinf = sla.solve_continuous_lyapunov(m4["B"], -Om)
    rinf = rinf / np.trace(rinf).real
    ck(np.allclose(rT, rinf, atol=1e-8),
       f"probe [{tag} Omega]: every initial density converges to rho_inf (gap {gap:.4f})",
       float(np.max(np.abs(rT - rinf))))
    ck(np.linalg.eigvalsh(rinf).min() > 1e-12 or tag == "rank-1 modal",
       f"probe [{tag} Omega]: rho_inf rank = {np.linalg.matrix_rank(rinf, tol=1e-10)} "
       f"(support = closed span of C_t supp Omega)")

print()
print(f"TOTAL {N} checks, {len(FAIL)} failures")
for f in FAIL:
    print("   FAILED:", f)
