#!/usr/bin/env python3
"""Fermion parity of a boson--fermion (c)MPS ring, checked against explicit Fock vectors.

Evidence for shard 04e (thm:cmps-overlap-parity, thm:cmps-twisted-supertrace,
thm:cmps-sdet, prop:cmps-twist-translation).

Lattice part (exact at fixed lattice spacing, no continuum limit involved).
Sites 1..N, local space {empty, boson b, fermion f1, fermion f2} with at most
one particle per site; fermions carry an explicit Jordan--Wigner string, so
the statistics signs come from the operators, not from the formula under test.
The state is Tr[B A_1 ... A_N] Omega with the operator-valued matrix
A_k = (1 + eps Q) (x) 1 + sqrt(eps) sum_alpha R_alpha (x) c^dag_{alpha,k},
multiplied with site 1 leftmost (the ordering of the cMPS calculus paper).
Checked: <Psi_B'|Psi_B> = Tr[(B (x) conj B') E^N], <Psi|(-1)^F|Psi> =
Tr[(B (x) conj B) E_eta^N] with and without a bond grading, (-1)^F Psi_B =
Psi_{PBP}, ||Psi_P||^2 = str_Gamma E^N with Gamma = P (x) conj P, the odd
sector as the interference 2 Re <Psi_{Pi-}|Psi_{Pi+}>, and the periodic /
antiperiodic translation invariance of Psi_P / Psi_1.

Continuum part: the Dyson expansion against expm, the lattice transfer
matrices converging to exp(L T), and the Laplace / Frullani identities giving
str (s - T)^{-1} and sdet_Gamma(s - T) from the twisted ring norms.
Deterministic stdout; assertions give a nonzero exit status on failure.
Run from the repository root: python3 scripts/cmps_parity_supertrace.py
"""

import numpy as np
import scipy.sparse as sp
from scipy.integrate import quad
from scipy.linalg import expm

CHECKS = 0


def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def close(a, b, tol, message):
    a, b = complex(a), complex(b)
    check(abs(a - b) <= tol * max(1.0, abs(b)), f"{message}: {a} vs {b}")


# ---------------------------------------------------------------- lattice Fock model
LOC = 4                      # 0 empty, 1 boson, 2 fermion f1, 3 fermion f2
SPECIES = [(1, +1), (2, -1), (3, -1)]   # (local state, eta)


def kron_chain(N, factor):
    out = sp.identity(1, dtype=complex, format="csr")
    for j in range(N):
        out = sp.kron(out, factor(j), format="csr")
    return out


def creation_ops(N):
    """Sparse lattice creation operators c^dag_{alpha,k}; fermions carry the Jordan--Wigner string."""
    Z = sp.diags([1, 1, -1, -1]).astype(complex)
    I = sp.identity(LOC, dtype=complex)
    ops = []
    for k in range(N):
        per_species = []
        for state, eta in SPECIES:
            up = sp.csr_matrix(([1.0 + 0j], ([state], [0])), shape=(LOC, LOC))
            per_species.append(kron_chain(N, lambda j: up if j == k else (Z if (eta == -1 and j < k) else I)))
        ops.append(per_species)
    return ops


def occupations(N):
    digits = np.array(np.unravel_index(np.arange(LOC ** N), [LOC] * N))   # shape (N, dim)
    return digits


def parity_diag(N):
    nf = (occupations(N) >= 2).sum(axis=0)
    return (-1.0) ** nf


def translation_op(N, antiperiodic):
    """Occupation-basis translation site k -> k+1, site N -> 1, with the fermionic sign
    from moving the wrapped fermion to the front; antiperiodic adds (-1)^{n_f(N)}."""
    dig = occupations(N)
    last = dig[-1]
    nf_rest = (dig[:-1] >= 2).sum(axis=0)
    sign = np.where(last >= 2, (-1.0) ** nf_rest, 1.0)
    if antiperiodic:
        sign = np.where(last >= 2, -sign, sign)
    new = np.vstack([last, dig[:-1]])
    rows = np.ravel_multi_index(tuple(new), [LOC] * N)
    dim = LOC ** N
    return sp.csr_matrix((sign.astype(complex), (rows, np.arange(dim))), shape=(dim, dim))


def mps_state(N, eps, Q, Rs, B, cre):
    """Tr[B A_1 ... A_N] Omega with site 1 leftmost, contracted right to left."""
    D = Q.shape[0]
    dim = LOC ** N
    M = np.zeros((D, D, dim), complex)
    for i in range(D):
        M[i, i, 0] = 1.0
    A0 = np.eye(D) + eps * Q
    As = [np.sqrt(eps) * R for R in Rs]
    for k in reversed(range(N)):
        new = np.einsum("il,ljv->ijv", A0, M)
        for a, A in enumerate(As):
            moved = (cre[k][a] @ M.reshape(D * D, dim).T).T.reshape(D, D, dim)
            new += np.einsum("il,ljv->ijv", A, moved)
        M = new
    return np.einsum("ji,ijv->v", B, M)


def transfer(eps, Q, Rs, Qp, Rps, signs):
    D = Q.shape[0]
    A0, A0p = np.eye(D) + eps * Q, np.eye(D) + eps * Qp
    E = np.kron(A0, A0p.conj())
    for s, R, Rp in zip(signs, Rs, Rps):
        E += s * eps * np.kron(R, Rp.conj())
    return E


def random_graded(rng, dp, dm, scale=0.6):
    D = dp + dm
    P = np.diag([1.0] * dp + [-1.0] * dm).astype(complex)
    even = np.zeros((D, D), bool)
    even[:dp, :dp] = even[dp:, dp:] = True

    def rnd():
        return scale * (rng.standard_normal((D, D)) + 1j * rng.standard_normal((D, D)))
    Q = np.where(even, rnd(), 0)
    Rs = [np.where(even, rnd(), 0), np.where(~even, rnd(), 0), np.where(~even, rnd(), 0)]
    return P, Q, Rs


def lattice_checks():
    print("== lattice: explicit Jordan--Wigner Fock vectors, N = 6 sites, bond 2+2")
    rng = np.random.default_rng(20260913)
    N, eps = 6, 0.35
    etas = [eta for _, eta in SPECIES]
    cre = creation_ops(N)
    pf = parity_diag(N)
    PF = sp.diags(pf).astype(complex)
    dp, dm = 2, 2
    P, Q, Rs = random_graded(rng, dp, dm)
    D = dp + dm
    tol = 1e-10

    # (0) the creation operators obey the graded relations (the Fock input)
    ok = True
    for k in range(N):
        for l in range(N):
            for a, (_, ea) in enumerate(SPECIES):
                for b, (_, eb) in enumerate(SPECIES):
                    if (k, a) == (l, b):
                        continue
                    eab = -1 if (ea == -1 and eb == -1) else 1
                    X, Y = cre[k][a], cre[l][b]
                    ok &= abs(X @ Y - eab * Y @ X).max() < 1e-12 if (X @ Y).nnz or (Y @ X).nnz else True
                    if k != l:
                        W = X.conj().T @ Y - eab * Y @ X.conj().T
                        ok &= (W.nnz == 0) or abs(W).max() < 1e-12
    check(ok, "graded commutation relations of the lattice creation operators")
    for k in range(N):
        for a, (_, ea) in enumerate(SPECIES):
            check(abs(PF @ cre[k][a] @ PF - ea * cre[k][a]).max() < 1e-12, "(-1)^F a^dag (-1)^F = eta a^dag")
    print("   graded relations and parity action of the Fock operators: ok")

    # (1) general overlap, no grading used (independent random data for bra and ket)
    Qg = 0.6 * (rng.standard_normal((D, D)) + 1j * rng.standard_normal((D, D)))
    Rg = [0.6 * (rng.standard_normal((D, D)) + 1j * rng.standard_normal((D, D))) for _ in SPECIES]
    Qh = 0.6 * (rng.standard_normal((D, D)) + 1j * rng.standard_normal((D, D)))
    Rh = [0.6 * (rng.standard_normal((D, D)) + 1j * rng.standard_normal((D, D))) for _ in SPECIES]
    Bg = rng.standard_normal((D, D)) + 1j * rng.standard_normal((D, D))
    Bh = rng.standard_normal((D, D)) + 1j * rng.standard_normal((D, D))
    psi = mps_state(N, eps, Qg, Rg, Bg, cre)
    phi = mps_state(N, eps, Qh, Rh, Bh, cre)
    for label, signs, op in (("overlap", [1, 1, 1], sp.identity(len(psi), dtype=complex)), ("(-1)^F", etas, PF)):
        fock = np.vdot(phi, op @ psi)
        E = transfer(eps, Qg, Rg, Qh, Rh, signs)
        formula = np.trace(np.kron(Bg, Bh.conj()) @ np.linalg.matrix_power(E, N))
        close(fock, formula, tol, f"ungraded {label}")
        print(f"   ungraded {label:7s}: Fock vs transfer formula agree (|value| = {abs(fock):.6e})")
    exp_par = np.vdot(psi, PF @ psi) / np.vdot(psi, psi)
    E_eta = transfer(eps, Qg, Rg, Qg, Rg, etas)
    E_one = transfer(eps, Qg, Rg, Qg, Rg, [1, 1, 1])
    Bk = np.kron(Bg, Bg.conj())
    pred = np.trace(Bk @ np.linalg.matrix_power(E_eta, N)) / np.trace(Bk @ np.linalg.matrix_power(E_one, N))
    close(exp_par, pred, tol, "ungraded normalised <(-1)^F>")
    check(abs(exp_par.real) < 1 - 1e-3, "ungraded <(-1)^F> is not +-1")
    print(f"   ungraded <(-1)^F> = {exp_par.real:+.6f} (nontrivial without a bond grading)")

    # (2) graded bond: parity acts on the boundary, and the physical parity is trivial
    Gam = np.kron(P, P.conj())
    E = transfer(eps, Q, Rs, Q, Rs, [1, 1, 1])
    Eeta = transfer(eps, Q, Rs, Q, Rs, etas)
    PI = np.kron(P, np.eye(D))
    check(np.allclose(Gam @ E, E @ Gam), "[Gamma, E] = 0")
    check(np.allclose(PI @ E @ PI, Eeta), "(P (x) 1) E (P (x) 1) = E_eta")
    Bgen = rng.standard_normal((D, D)) + 1j * rng.standard_normal((D, D))
    psiB = mps_state(N, eps, Q, Rs, Bgen, cre)
    psiPBP = mps_state(N, eps, Q, Rs, P @ Bgen @ P, cre)
    check(np.allclose(PF @ psiB, psiPBP), "(-1)^F Psi_B = Psi_{PBP}")
    print("   (-1)^F Psi_B = Psi_{PBP} as Fock vectors: ok")
    EN = np.linalg.matrix_power(E, N)
    psi1 = mps_state(N, eps, Q, Rs, np.eye(D), cre)
    psiP = mps_state(N, eps, Q, Rs, P, cre)
    close(np.vdot(psi1, PF @ psi1), np.vdot(psi1, psi1), tol, "<Psi_1|(-1)^F|Psi_1> = ||Psi_1||^2")
    close(np.vdot(psiP, PF @ psiP), np.vdot(psiP, psiP), tol, "<Psi_P|(-1)^F|Psi_P> = ||Psi_P||^2")
    close(np.vdot(psi1, psi1), np.trace(EN), tol, "||Psi_1||^2 = Tr E^N")
    close(np.vdot(psiP, psiP), np.trace(Gam @ EN), tol, "||Psi_P||^2 = str_Gamma E^N")
    close(np.vdot(psiP, PF @ psiP), np.trace(Gam @ np.linalg.matrix_power(Eeta, N)), tol,
          "<Psi_P|(-1)^F|Psi_P> = Tr[Gamma E_eta^N]")
    even = 0.5 * (np.eye(D * D) + Gam)
    odd = 0.5 * (np.eye(D * D) - Gam)
    tr_even, tr_odd = np.trace(even @ EN), np.trace(odd @ EN)
    close(np.trace(Gam @ EN), tr_even - tr_odd, tol, "str = Tr_even - Tr_odd")
    Pip, Pim = 0.5 * (np.eye(D) + P), 0.5 * (np.eye(D) - P)
    psip = mps_state(N, eps, Q, Rs, Pip, cre)
    psim = mps_state(N, eps, Q, Rs, Pim, cre)
    close(tr_even, np.vdot(psip, psip) + np.vdot(psim, psim), tol, "Tr_even = ||Psi_Pi+||^2 + ||Psi_Pi-||^2")
    close(tr_odd, 2 * np.vdot(psim, psip).real, tol, "Tr_odd = 2 Re <Psi_Pi-|Psi_Pi+>")
    check(tr_odd.real > 0, "the chosen example has a positive odd-sector trace")
    print(f"   graded: <(-1)^F> = 1 in Psi_1 and in Psi_P; ||Psi_1||^2 = Tr E^N = {np.trace(EN).real:.6e}")
    print(f"   graded: ||Psi_P||^2 = str E^N = {np.trace(Gam @ EN).real:.6e} = Tr_even {tr_even.real:.6e}"
          f" - Tr_odd {tr_odd.real:.6e}")
    print("   odd sector = interference 2 Re <Psi_Pi-|Psi_Pi+>: ok")

    # (3) Dyson form: signed sum of squares over occupation configurations
    coeffs = psiP
    nf = (occupations(N) >= 2).sum(axis=0)
    close(np.sum((-1.0) ** nf * abs(coeffs) ** 2), np.trace(Gam @ np.linalg.matrix_power(Eeta, N)), tol,
          "signed sum of squares = Tr[Gamma E_eta^N]")
    check(np.allclose(coeffs[nf % 2 == 1], 0), "Psi_P has no odd-fermion-number amplitudes")
    print("   Psi_P has only even fermion number; signed and unsigned sums of squares coincide: ok")

    # (4) boundary conditions: Psi_P periodic, Psi_1 antiperiodic
    Tper, Tap = translation_op(N, False), translation_op(N, True)
    for k in range(N):
        for a in range(len(SPECIES)):
            check(abs(Tper @ cre[k][a] - cre[(k + 1) % N][a] @ Tper).max() < 1e-12, "periodic translation covariance")
            sgn = -1 if (k == N - 1 and SPECIES[a][1] == -1) else 1
            check(abs(Tap @ cre[k][a] - sgn * cre[(k + 1) % N][a] @ Tap).max() < 1e-12, "antiperiodic translation covariance")
    check(np.allclose(Tper @ psiP, psiP), "Psi_P invariant under periodic fermionic translation")
    check(np.allclose(Tap @ psi1, psi1), "Psi_1 invariant under antiperiodic fermionic translation")
    check(not np.allclose(Tper @ psi1, psi1), "Psi_1 not invariant under periodic translation")
    check(not np.allclose(Tap @ psiP, psiP), "Psi_P not invariant under antiperiodic translation")
    print("   Psi_P is invariant under the periodic, Psi_1 under the antiperiodic translation (and not conversely): ok")


# ---------------------------------------------------------------- continuum
def dyson(L, A, C, order, grid):
    """Sum_{n<=order} of the Dyson terms, by the recursion I_n(L) = int_0^L I_{n-1}(x) C e^{(L-x)A} dx
    evaluated with the composite Simpson rule on a uniform grid."""
    xs = np.linspace(0, L, grid + 1)
    h = L / grid
    w = np.ones(grid + 1)
    w[1:-1:2], w[2:-1:2] = 4, 2
    w *= h / 3
    expA = [expm(x * A) for x in xs]
    I_prev = [expA[j] for j in range(grid + 1)]
    total = I_prev[-1].copy()
    for _ in range(order):
        I_new = []
        for j in range(grid + 1):
            acc = np.zeros_like(A)
            for i in range(j + 1):
                wi = simpson_weight(i, j, h)
                if wi:
                    acc = acc + wi * I_prev[i] @ C @ expA[j - i]
            I_new.append(acc)
        I_prev = I_new
        total = total + I_prev[-1]
    return total


def simpson_weight(i, j, h):
    """Weights of a composite rule on [0, x_j]: Simpson when j is even, trapezoid otherwise."""
    if j == 0:
        return 0.0
    if j % 2 == 0:
        if i == 0 or i == j:
            return h / 3
        return 4 * h / 3 if i % 2 == 1 else 2 * h / 3
    return h / 2 if i in (0, j) else h


def continuum_checks():
    print("== continuum: Dyson, lattice limit, Laplace and Frullani identities (bond 2+1)")
    rng = np.random.default_rng(31415)
    dp, dm = 2, 1
    P, Q, Rs = random_graded(rng, dp, dm, scale=0.5)
    D = dp + dm
    I = np.eye(D)
    etas = [1, -1, -1]
    A = np.kron(Q, I) + np.kron(I, Q.conj())
    C = sum(np.kron(R, R.conj()) for R in Rs)
    Ceta = sum(e * np.kron(R, R.conj()) for e, R in zip(etas, Rs))
    T, Teta = A + C, A + Ceta
    Gam = np.kron(P, P.conj())
    L = 0.8

    exact = expm(L * T)
    coarse = np.linalg.norm(dyson(L, A, C, order=14, grid=100) - exact)
    fine_approx = dyson(L, A, C, order=14, grid=200)
    fine = np.linalg.norm(fine_approx - exact)
    rich = np.linalg.norm((4 * fine_approx - dyson(L, A, C, order=14, grid=100)) / 3 - exact)
    check(3.0 < coarse / fine < 5.0, f"Dyson quadrature error is second order: {coarse / fine}")
    check(rich < 1e-5, f"Richardson-extrapolated Dyson series reproduces exp(L T): {rich}")
    print(f"   Dyson series (14 orders, nested quadrature) vs expm: error ratio {coarse / fine:.2f} under"
          " grid doubling, Richardson residual < 1e-5")

    errs = []
    for N in (100, 200, 400, 800):
        eps = L / N
        E = transfer(eps, Q, Rs, Q, Rs, [1, 1, 1])
        errs.append(abs(np.trace(Gam @ np.linalg.matrix_power(E, N)) - np.trace(Gam @ exact)))
    ratios = [errs[i] / errs[i + 1] for i in range(3)]
    check(all(1.8 < r < 2.2 for r in ratios), f"lattice str converges at first order, ratios {ratios}")
    print("   lattice str E^N -> str exp(L T) at first order in the spacing: error ratios "
          + ", ".join(f"{r:.2f}" for r in ratios))

    check(np.allclose(Gam @ T, T @ Gam), "[Gamma, T] = 0")
    check(np.allclose(np.kron(P, I) @ T @ np.kron(P, I), Teta), "(P (x) 1) T (P (x) 1) = T_eta")
    check(np.allclose(np.kron(I, P.conj()) @ T @ np.kron(I, P.conj()), Teta), "(1 (x) conj P) T (1 (x) conj P) = T_eta")
    close(np.trace(Gam @ expm(L * Teta)), np.trace(Gam @ exact), 1e-12, "str exp(L T_eta) = str exp(L T)")

    ev_even = np.linalg.eigvals(T[np.ix_(*(2 * [np.where(np.diag(Gam).real > 0)[0]]))])
    ev_odd = np.linalg.eigvals(T[np.ix_(*(2 * [np.where(np.diag(Gam).real < 0)[0]]))])
    omega = max(np.linalg.eigvals(T).real)
    check(len(ev_even) == dp * dp + dm * dm and len(ev_odd) == 2 * dp * dm, "sector dimensions")
    print(f"   sectors: even dim {len(ev_even)}, odd dim {len(ev_odd)}; spectral abscissa omega = {omega:.6f}")

    s, s0 = omega + 1.3, omega + 2.1
    Id = np.eye(D * D)
    cut = 60.0 / (s - omega)

    def damped(x, z):          # e^{-zL} ||Psi_P(L)||^2 = str exp(L (T - z)), no overflow
        return np.trace(Gam @ expm(x * (T - z * Id))).real

    lap = quad(lambda x: damped(x, s), 0, cut, limit=400, epsabs=1e-13, epsrel=1e-12)[0]
    res = np.trace(Gam @ np.linalg.inv(s * Id - T)).real
    close(lap, res, 1e-8, "Laplace transform of ||Psi_P(L)||^2 = str (s - T)^{-1}")
    dlog = (np.sum(1 / (s - ev_even)) - np.sum(1 / (s - ev_odd))).real
    close(res, dlog, 1e-10, "str (s - T)^{-1} = d/ds log sdet(s - T)")
    print(f"   int_0^inf e^(-sL) ||Psi_P(L)||^2 dL = {lap:.10f} = str (s-T)^(-1) = d/ds log sdet(s-T)")

    def frullani_integrand(x):
        if x < 1e-9:
            return (s0 - s) * np.trace(Gam).real
        return (damped(x, s) - damped(x, s0)) / x
    frull = quad(frullani_integrand, 0, cut, limit=400, epsabs=1e-13, epsrel=1e-12)[0]

    def sdet(z):
        return np.prod(z - ev_even) / np.prod(z - ev_odd)
    ratio = sdet(s) / sdet(s0)
    close(np.exp(-frull), ratio, 1e-8, "Frullani: exp(-int (e^-sL - e^-s0L) ||Psi_P||^2 dL/L) = sdet ratio")
    print(f"   exp(-int (e^(-sL)-e^(-s0 L)) ||Psi_P(L)||^2 dL/L) = {np.exp(-frull):.10f}"
          f" = sdet(s-T)/sdet(s0-T) = {ratio.real:.10f}")

    # untwisted ring: ordinary determinant
    lap1 = quad(lambda x: np.trace(expm(x * (T - s * Id))).real, 0, cut, limit=400,
                epsabs=1e-13, epsrel=1e-12)[0]
    close(lap1, np.trace(np.linalg.inv(s * np.eye(D * D) - T)).real, 1e-8, "untwisted ring gives Tr (s-T)^{-1}")
    print("   untwisted ring (B = 1): Laplace transform = Tr (s-T)^(-1) = d/ds log det(s-T): ok")


if __name__ == "__main__":
    lattice_checks()
    continuum_checks()
    print(f"all {CHECKS} checks passed")
