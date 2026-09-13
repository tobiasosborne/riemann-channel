#!/usr/bin/env python3
"""Finite residue models for the BC-stationary, arithmetic-covariant inverse problem.

This is NOT a finite representation of the full Bost--Connes algebra or an
adelic Lindbladian.  The critical BC phase marginal is uniform; its diagonal
extension to M_p is I/p.  We distinguish multiplicative (Galois), linear
symplectic (Weil), and additional Weyl-translation covariance.

Exact finite-field orbit counts give dimensions of the real linear spans of
the corresponding GKLS cones.  Independent matrix checks test covariance,
stationarity, conditional Choi positivity, actual finite-time complete
positivity, odd-sector spectra, and a two-prime compatible coupling.
Deterministic stdout; assertions give a nonzero exit status on failure.
Run from the repository root: python3 scripts/bc_symmetry_generators.py
"""

from collections import Counter, deque
import itertools

import mpmath as mp
import numpy as np
from scipy.linalg import expm
from sympy import primitive_root


CHECKS = 0
TOL = 2e-9


def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def near(a, b, message):
    check(np.linalg.norm(np.asarray(a) - np.asarray(b)) < TOL, message)


def vec(x):
    return x.reshape(-1, order="F")


def ad(u):
    return np.kron(u.conj(), u)


def points(p):
    return list(itertools.product(range(p), repeat=2))


def act(g, v, p):
    a, b, c, d = g
    x, y = v
    return ((a*x + b*y) % p, (c*x + d*y) % p)


def mul(g, h, p):
    a, b, c, d = g
    e, f, k, l = h
    return ((a*e+b*k) % p, (a*f+b*l) % p,
            (c*e+d*k) % p, (c*f+d*l) % p)


def inverse(g, p):
    a, b, c, d = g
    return (d, -b % p, -c % p, a)


def sl2(p):
    return [g for g in itertools.product(range(p), repeat=4)
            if (g[0]*g[3]-g[1]*g[2]) % p == 1]


def permutation(g, p, pts):
    lookup = {v: i for i, v in enumerate(pts)}
    return np.array([lookup[act(g, v, p)] for v in pts])


def pair_orbits(perms):
    """Orbit matrices on ordered pairs, computed by generator BFS."""
    n = len(perms[0])
    unseen = set(itertools.product(range(n), repeat=2))
    result = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        todo = deque([start])
        orbit = [start]
        while todo:
            i, j = todo.popleft()
            for perm in perms:
                nxt = (int(perm[i]), int(perm[j]))
                if nxt in unseen:
                    unseen.remove(nxt)
                    todo.append(nxt)
                    orbit.append(nxt)
        result.append(orbit)
    return result


def weyl(p, v):
    x, y = v
    u = np.zeros((p, p), complex)
    for r in range(p):
        u[(r+x) % p, r] = np.exp(2j*np.pi*((y*(r+x*pow(2, -1, p))) % p)/p)
    return u


def frame(p):
    return np.column_stack([vec(weyl(p, v))/np.sqrt(p) for v in points(p)])


def choi(s, p):
    """C(S) = sum_ij |i><j| tensor S(|i><j|), unnormalised."""
    out = np.zeros((p*p, p*p), complex)
    for i in range(p):
        for j in range(p):
            out[i*p:(i+1)*p, j*p:(j+1)*p] = s[:, i+j*p].reshape((p, p), order="F")
    return out


def certify_generator(l, p, state, symmetries):
    ident = np.eye(p)
    near(vec(ident).conj() @ l, np.zeros(p*p), "trace preservation")
    near(l @ vec(state), np.zeros(p*p), "stationarity")
    for u in symmetries:
        near(l @ ad(u), ad(u) @ l, "generator covariance")
    c = choi(l, p)
    near(c, c.conj().T, "Hermiticity preservation")
    bell = vec(ident)/np.sqrt(p)
    project = np.eye(p*p)-np.outer(bell, bell)
    cc = project @ c @ project
    check(np.linalg.eigvalsh(cc).min() > -TOL, "conditional Choi positivity")
    for t in (0.17, 0.8):
        channel = expm(t*l)
        ct = choi(channel, p)
        near(ct, ct.conj().T, "finite-time Choi Hermitian")
        check(np.linalg.eigvalsh(ct).min() > -TOL, "finite-time complete positivity")
    check(np.count_nonzero(abs(np.linalg.eigvals(l)) < TOL) == 1,
          "unique stationary density")


def local_symmetries(p):
    a = int(primitive_root(p))
    dilation = np.eye(p)[:, [(a*r) % p for r in range(p)]]
    fourier = np.array([[np.exp(2j*np.pi*x*y/p)/np.sqrt(p)
                         for y in range(p)] for x in range(p)])
    chirp = np.diag([np.exp(2j*np.pi*((pow(2, -1, p)*x*x) % p)/p)
                     for x in range(p)])
    parity = np.eye(p)[:, [(-r) % p for r in range(p)]]
    return dilation, fourier, chirp, parity


def odd_basis(p):
    pts = points(p)
    lookup = {v: i for i, v in enumerate(pts)}
    columns = []
    for v in pts[1:]:
        neg = ((-v[0]) % p, (-v[1]) % p)
        if v < neg:
            b = np.zeros(p*p)
            b[lookup[v]], b[lookup[neg]] = 1/np.sqrt(2), -1/np.sqrt(2)
            columns.append(b)
    return np.column_stack(columns)


def spectral_summary(eigenvalues):
    counts = Counter((round(float(z.real), 6), round(float(z.imag), 6))
                     for z in eigenvalues)
    return "; ".join(f"{re:+.6f}{im:+.6f}i x{n}"
                     for (re, im), n in sorted(counts.items()))


def residue_states():
    print("1. BC phase marginals and matrix-state extensions")
    mp.mp.dps = 35
    for p in (3, 5, 7):
        dilation, fourier, chirp, parity = local_symmetries(p)
        for beta in (1.0, 2.0):
            r = p**(-beta)
            a = (1-r)/(p-1)
            diagonal = np.diag([r]+[a]*(p-1))
            coherent = a*np.eye(p)+(r-a)*parity
            near(np.diag(coherent), np.diag(diagonal), "same phase marginal")
            near(dilation @ diagonal @ dilation.conj().T, diagonal, "Galois-invariant marginal")
            for u in (fourier, chirp):
                near(u @ coherent @ u.conj().T, coherent, "Weil-invariant extension")
            check(np.linalg.eigvalsh(coherent).min() > 0, "faithful extension")
            defect = np.linalg.norm(fourier @ diagonal @ fourier.conj().T-diagonal)
            if beta == 1:
                near(diagonal, np.eye(p)/p, "critical uniformity")
                near(coherent, diagonal, "critical extension is trace")
            else:
                extremal = np.array([float(mp.zeta(beta, mp.mpf(k)/p)/(p**beta*mp.zeta(beta)))
                                     for k in range(1, p+1)])
                extremal = np.roll(extremal, 1)
                twirled = sum(np.array([extremal[(pow(a0, -1, p)*x) % p]
                                       for x in range(p)]) for a0 in range(1, p))/(p-1)
                near(twirled, np.diag(diagonal), "Hurwitz BC extremals averaged over Galois")
                check(np.linalg.norm(dilation @ np.diag(extremal) @ dilation.conj().T
                                     -np.diag(extremal)) > 0.01,
                      "one extremal state is not Galois-invariant")
                for state, symmetries in ((diagonal, (dilation,)),
                                          (coherent, (dilation, fourier, chirp))):
                    reset = np.outer(vec(state), vec(np.eye(p)))-np.eye(p*p)
                    certify_generator(reset, p, state, symmetries)
            print(f"  p={p} beta={beta:.0f}: mass(0)={r:.6f}; diagonal Fourier defect={defect:.6f};"
                  f" Weil-extension min eigenvalue={np.linalg.eigvalsh(coherent).min():.6f}")
        beta = 0.2
        r = p**(-beta)
        a = (1-r)/(p-1)
        check(2*a-r < 0, "hot marginal has no positive Weil-invariant extension")
    print("  Noncritical coherent extensions are state-extension examples, not BC bond identifications.")


def dimensions():
    print("\n2. Exact real dimensions at the critical tracial extension (time scale included)")
    print("  p | Galois | Weil-SL2 | Weyl+Galois | Weyl+SL2")
    for p in (3, 5, 7):
        nonzero = points(p)[1:]
        a = int(primitive_root(p))
        torus = (a, 0, 0, pow(a, -1, p))
        shear, rotation = (1, 0, 1, 1), (0, -1 % p, 1, 0)
        gt = pair_orbits([permutation(torus, p, nonzero)])
        gs = pair_orbits([permutation(shear, p, nonzero), permutation(rotation, p, nonzero)])
        expected_g, expected_s = (p-1)*(p+1)**2, 2*p-2
        check(len(gt) == expected_g, "Galois pair orbit dimension")
        check(len(gs) == expected_s, "symplectic pair orbit dimension")
        group = sl2(p)
        check(len(group) == p*(p*p-1), "SL2 order")
        # Independent Burnside counts, without the generator-orbit construction.
        fixed = [sum(act(g, v, p) == v for v in nonzero) for g in group]
        check(sum(n*n for n in fixed) == len(group)*expected_s,
              "Burnside commutant dimension")
        wt = sum(any(i == j for i, j in o) for o in gt)
        ws = sum(any(i == j for i, j in o) for o in gs)
        check((wt, ws) == (p+1, 1), "Weyl-diagonal invariant rate counts")
        print(f"  {p} | {len(gt):6d} | {len(gs):8d} | {wt:11d} | {ws:8d}")
        # Every orbit direction is Hermiticity preserving because -I belongs
        # to both groups.  Add a small direction to an interior depolarizer.
        b = frame(p)
        near(b.conj().T @ b, np.eye(p*p), "orthonormal Weyl frame")
        depol = np.diag([0]+[-1]*(p*p-1))
        for orbits in (gt, gs):
            for index in sorted(set((0, len(orbits)//2, len(orbits)-1))):
                direction = np.zeros((p*p, p*p))
                for i, j in orbits[index]:
                    direction[i+1, j+1] = 1
                l = b @ (depol + 1e-3*direction) @ b.conj().T
                cp = choi(l, p)
                near(cp, cp.conj().T, "orbit direction Hermiticity")
                bell = vec(np.eye(p))/np.sqrt(p)
                project = np.eye(p*p)-np.outer(bell, bell)
                check(np.linalg.eigvalsh(project @ cp @ project).min() > -TOL,
                      "interior perturbation remains GKLS")


def spectral_freedom():
    print("\n3. Full linear-symplectic covariance leaves odd spectral freedom")
    for p in (3, 5, 7):
        pts, group, b = points(p), sl2(p), frame(p)
        shear = (1, 0, 1, 1)
        conjugates = sorted({mul(mul(g, shear, p), inverse(g, p), p) for g in group})
        channel = np.zeros((p*p, p*p))
        for g in conjugates:
            perm = permutation(g, p, pts)
            channel[perm, np.arange(p*p)] += 1/len(conjugates)
        # A positive sum of class-averaged unitary jumps and depolarization.
        lw = 0.2*np.diag([0]+[-1]*(p*p-1)) + channel-np.eye(p*p)
        l = b @ lw @ b.conj().T
        dilation, fourier, chirp, parity = local_symmetries(p)
        certify_generator(l, p, np.eye(p)/p, (dilation, fourier, chirp, parity))
        # Verify the phase-free symplectic action directly on Hilbert matrices.
        for v in pts:
            near(chirp @ weyl(p, v) @ chirp.conj().T, weyl(p, act(shear, v, p)),
                 "chirp Egorov identity")
        odd = odd_basis(p)
        near(lw @ odd, odd @ (odd.T @ lw @ odd), "odd-sector invariance")
        eigen = np.linalg.eigvals(odd.T @ lw @ odd)
        print(f"  p={p}; shear class size={len(conjugates)}; odd spectrum: {spectral_summary(eigen)}")
        # Invariant parity Hamiltonian supplies freely variable oscillations.
        h = 0.37*parity
        lh = l-1j*(np.kron(np.eye(p), h)-np.kron(h.T, np.eye(p)))
        certify_generator(lh, p, np.eye(p)/p, (dilation, fourier, chirp))
        eigen_h = np.linalg.eigvals(odd.T @ (b.conj().T @ lh @ b) @ odd)
        check(abs(np.max(abs(eigen_h.imag))-np.max(abs(eigen.imag))) > 0.05,
              "invariant Hamiltonian changes frequencies")
        print(f"    with H=0.37 parity: {spectral_summary(eigen_h)}")

        # Scalar multiplication on phase space commutes with SL2, although
        # it need not itself be symplectic.  A sufficiently small HP,
        # trace-annihilating perturbation of an interior GKLS generator is
        # still GKLS.  ||C(R)|| <= ||C(R)||_F = sqrt(p^2-1) < p, whereas
        # the depolarizer's conditional Choi eigenvalue is 1/p.
        a = int(primitive_root(p))
        scalar = (a, 0, 0, a)
        perm = permutation(scalar, p, pts)
        direction = np.eye(p*p)[perm].T
        direction[0, 0] = 0
        eps = 1/(4*p*p)
        perturbed = np.diag([0]+[-1]*(p*p-1))+eps*direction
        certify_generator(b @ perturbed @ b.conj().T, p, np.eye(p)/p,
                          (dilation, fourier, chirp, parity))
        spectrum = np.linalg.eigvals(odd.T @ perturbed @ odd)
        if p == 7:
            check(len(set(np.round(spectrum.real, 6))) == 2,
                  "full Weil symmetry permits unequal odd decay rates")
            expected = [-1-eps]*8+[-1+eps/2+1j*np.sqrt(3)*eps/2]*8+[-1+eps/2-1j*np.sqrt(3)*eps/2]*8
            check(spectral_summary(spectrum) == spectral_summary(expected),
                  "exact scalar-orbit spectral prediction")
        print(f"    interior scalar-orbit perturbation: {spectral_summary(spectrum)}")


def weyl_noise():
    print("\n4. Additional Weyl covariance: real Galois spectrum and depolarizing SL2 ray")
    for p in (3, 5, 7):
        pts, b = points(p), frame(p)
        # Torus orbits: the two axes, and xy=c != 0.
        rates = {}
        for x, y in pts[1:]:
            key = 0 if y == 0 else 1 if x == 0 else 1+(x*y) % p
            rates[(x, y)] = (key+1)/(p*p)
        l = sum((r*(ad(weyl(p, v))-np.eye(p*p)) for v, r in rates.items()),
                np.zeros((p*p, p*p), complex))
        lw = b.conj().T @ l @ b
        near(lw, np.diag(np.diag(lw)), "Weyl-diagonal generator")
        check(np.max(abs(np.diag(lw).imag)) < TOL, "Galois -1 makes Weyl rates symmetric")
        dilation = local_symmetries(p)[0]
        certify_generator(l, p, np.eye(p)/p,
                          (dilation, weyl(p, (1, 0)), weyl(p, (0, 1))))
        uniform = sum((ad(weyl(p, v))-np.eye(p*p) for v in pts[1:]),
                      np.zeros((p*p, p*p), complex))/(p*p)
        expected = np.outer(vec(np.eye(p)), vec(np.eye(p)))/p-np.eye(p*p)
        near(uniform, expected, "full symplectic orbit gives depolarizing ray")
        print(f"  p={p}: {p+1} nonnegative Galois orbit rates, real spectrum; full SL2 leaves one rate.")


def two_prime_coupling():
    print("\n5. Two-prime coupling with unchanged one-prime restrictions")
    p, q, gamma_p, gamma_q = 3, 5, 0.7, 0.9
    # Work in tensor-product Weyl coordinates; the trace coordinate is first.
    ep, eq = np.diag([1]+[0]*(p*p-1)), np.diag([1]+[0]*(q*q-1))
    ip, iq = np.eye(p*p), np.eye(q*q)
    for c in (0.0, 0.2, 0.6):
        l = ((gamma_p-c)*np.kron(ep-ip, iq)
             +(gamma_q-c)*np.kron(ip, eq-iq)
             +c*(np.kron(ep, eq)-np.kron(ip, iq)))
        eig = np.diag(l)
        near(eig[1], -gamma_q, "q marginal unchanged")
        near(eig[q*q], -gamma_p, "p marginal unchanged")
        near(eig[q*q+1], -gamma_p-gamma_q+c, "correlation sector changes")
        check(min(gamma_p-c, gamma_q-c, c) >= 0, "CP reset rates")
        # Explicit channels D_p tensor id, id tensor D_q, D_p tensor D_q
        # commute, so positivity follows without diagonalising a 225x225 Choi matrix.
        print(f"  c={c:.1f}: p-only={eig[q*q]:+.3f}; q-only={eig[1]:+.3f};"
              f" joint traceless={eig[q*q+1]:+.3f}; additive defect={c:.3f}")


def main():
    residue_states()
    dimensions()
    spectral_freedom()
    weyl_noise()
    two_prime_coupling()
    print(f"\nALL {CHECKS} CHECKS PASS")
    print("Scope: finite phase-marginal models only; no adelic limit, scattering identification, or RH claim.")


if __name__ == "__main__":
    main()
