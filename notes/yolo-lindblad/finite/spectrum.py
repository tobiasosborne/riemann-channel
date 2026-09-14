#!/usr/bin/env python3
"""N5: compressed odd spectrum, parity leakage, actual Galois dephasing."""
import math
import numpy as np
import scipy.linalg as la
import scipy.sparse as ss
from finite_common import (Checks, primes, shell_jump, maxabs, characters,
                           divisors, gauss_vector, galois_fourier)


def main():
    check = Checks("spectrum")
    B, pp = 30, primes(5)
    V = {p: shell_jump(list(range(1, B+1)), p) for p in pp}
    T = sum((ss.kron(V[p], V[p])-ss.eye(B*B))/p for p in pp).tocsr()
    pi = np.full(B, -1); pi[0] = 1
    grading = np.kron(pi, pi)
    odd, even = np.where(grading == -1)[0], np.where(grading == 1)[0]
    leak = T[even][:, odd]
    comm = ss.diags(grading) @ T - T @ ss.diags(grading)
    check(maxabs(leak) > .01 and maxabs(comm) > .01,
          "odd coherences NOT invariant; Gamma_b does NOT commute with T")
    trace = np.eye(B).ravel()
    trace_loss = trace @ T
    check(maxabs(trace_loss) > .01, "requested truncated T is trace decreasing, not trace preserving")
    projected = T[odd][:, odd].toarray()
    ev = la.eigvals(projected)
    pred = np.array([sum(1/p**2 for p in pp if b % p)-sum(1/p for p in pp) for b in range(2, B+1)]*2)
    check(max(abs(np.sort(ev.real)-np.sort(pred))) < 1e-12 and max(abs(ev.imag)) < 1e-12,
          "explicit odd compression eigenspectrum agrees with triangular diagonal")
    # Compare the whole doubled matrix's eigenvalues with its known diagonal.
    all_ev = la.eigvals(T.toarray())
    check(max(abs(np.sort(all_ev.real)-np.sort(T.diagonal()))) < 1e-12 and max(abs(all_ev.imag)) < 1e-12,
          "full finite doubled T also has entirely real spectrum")
    rows = []
    for P in primes(47)[2:]:
        pp = primes(P)
        for B in (64, 256, 1024, 3072):
            for beta in ((1., 1.05, 1.2) if P == 47 else (1.,)):
                # Exact row-closed compression; its two diagonal blocks are H-Lambda.
                H = sum(p**(-beta-.5)*shell_jump(list(range(1, B+1)), p) for p in pp)
                C = H[1:, 1:]-sum(p**-beta for p in pp)*ss.eye(B-1)
                diag = C.diagonal()
                expected = np.array([sum(p**(-beta-1) for p in pp if b % p)-sum(p**-beta for p in pp)
                                     for b in range(2, B+1)])
                check(maxabs(ss.triu(C, k=1)) < 1e-12 and maxabs(diag-expected) < 1e-12,
                      f"P={P}, Bmax={B}, beta={beta}: exact triangular odd compression")
                rows.append(dict(P=P, Bmax=B, beta=beta, dimension=2*(B-1),
                                 min_real=float(min(diag)), max_real=float(max(diag)),
                                 max_abs_imag=0., distinct_real=len(np.unique(np.round(diag, 12)))))
    # Actual finite Galois group, including repeated copies of a character in
    # different denominator shells; equal characters must not dephase.
    B, gamma = 120, .125
    units = [a for a in range(B) if math.gcd(a, B) == 1]
    vectors, eigencharacters = [], []
    for b in divisors(B):
        for _, values in characters(b):
            vectors.append(gauss_vector(values, B))
            eigencharacters.append([values[a % b] for a in units])
    W = np.array(vectors).T
    X = np.array(eigencharacters)
    check(maxabs(W.conj().T @ W-np.eye(B)) < 1e-12, "complete Gauss-character basis at B=120")
    same = np.max(abs(X[:, None, :]-X[None, :, :]), axis=2) < 1e-10
    D = gamma*(X @ X.conj().T/len(units)-1)
    error = maxabs(D-np.where(same, 0., -gamma))
    check(error < 1e-12, "total-rate gamma Galois dissipator: exactly -gamma across characters, zero within")
    trivial = np.max(abs(X-1), axis=1) < 1e-10
    check(int(sum(trivial)) == len(divisors(B)) and maxabs(D[np.ix_(trivial, trivial)]) < 1e-12,
          "every Ramanujan shell is Galois trivial: their doubled sector has zero shift")
    covariance_error = 0.
    for p in primes(13):
        A = ss.csr_matrix((np.full(B, p**-.5), (np.arange(B), (p*np.arange(B)) % B)), shape=(B, B))
        G = W.conj().T @ (A @ W)
        covariance_error = max(covariance_error, maxabs(G[~same]))
        check(maxabs(G[~same]) < 1e-12, f"p={p}: finite phase compression preserves every Galois-character sector")
    # Apply the unitary average directly to seeded rank-one coherences.
    for i, j in [(0, 1), (0, 0)] + [tuple(pair) for pair in check.rng.integers(0, B, (12, 2))]:
        rho = np.outer(W[:, i], W[:, j].conj())
        avg = np.zeros_like(rho)
        for a in units:
            U = galois_fourier(B, a)
            avg += (U @ rho) @ U.T/len(units)
        expected = (0 if same[i, j] else -gamma)*rho
        check(maxabs(gamma*(avg-rho)-expected) < 1e-12,
              f"coherence {i},{j}: explicit group average shift {0 if same[i,j] else -gamma}")
    print("leakage/commutator max:", maxabs(leak), maxabs(comm))
    print("Bmax=3072 spectra:", [r for r in rows if r["Bmax"] == 3072])
    check.finish(dict(rows=rows, parity_leakage_max=maxabs(leak), parity_commutator_max=maxabs(comm),
                      trace_defect_max=maxabs(trace_loss), galois_error=error,
                      covariance_error=covariance_error, gamma=gamma,
                      character_within_pairs=int(np.sum(same)), character_cross_pairs=int(np.sum(~same)),
                      trivial_shells=int(sum(trivial))))


if __name__ == "__main__":
    main()
