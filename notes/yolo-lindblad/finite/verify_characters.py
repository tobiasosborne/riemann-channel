#!/usr/bin/env python3
"""N2: all characters for b|120; distinguish adjoint eigenvectors from coherences."""
import ast
from fractions import Fraction
import math
from pathlib import Path
import numpy as np
import scipy.sparse as ss
from finite_common import (Checks, characters, divisors, phi, fourier_jump,
                           gauss_vector, galois_fourier, primes, maxabs)


def forward(v, p):
    out = {}
    for r, value in v.items():
        for k in range(p):
            s = (r + k)/p
            out[s] = out.get(s, 0) + value/np.sqrt(p)
    return out


def coherence_action(values, pp, beta):
    """Exact finite support of T(|e0><g|), no ambient denominator cutoff.

    Compute its Rayleigh scalar and orthogonal HS residual from Gram matrices.
    """
    b = len(values)
    g = {Fraction(a, b): values[a]/np.sqrt(phi(b)) for a in range(b) if abs(values[a]) > 0}
    e0 = {Fraction(0): 1.}
    av, bv = [forward(e0, p) for p in pp], [forward(g, p) for p in pp]
    modes = sorted(set().union(e0, g, *av, *bv))
    def cols(vv):
        return np.array([[v.get(r, 0) for v in vv] for r in modes], complex)
    A, B = cols(av), cols(bv)
    E, G = cols([e0])[:, 0], cols([g])[:, 0]
    rates = np.array(pp, float)**-beta
    c = np.sum(rates * (E.conj() @ A) * (B.conj().T @ G))
    norm2 = np.real(rates @ ((A.conj().T @ A) * (B.conj().T @ B).conj()) @ rates)
    residual = np.sqrt(max(0., norm2 - abs(c)**2))
    return c - sum(rates), residual


def load_bc_transfer():
    # Reuse the actual repo function without executing its expensive demo at import.
    source = Path(__file__).resolve().parents[3]/"scripts/bcmpo.py"
    tree = ast.parse(source.read_text())
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "transfer")
    namespace = {"np": np}
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(source), "exec"), namespace)
    return namespace["transfer"]


def main():
    check = Checks("verify_characters")
    transfer = load_bc_transfer()
    B, pp = 120, primes(13)
    err_adj = err_galois = err_bc = 0.
    total = 0
    for b in divisors(B):
        chars = characters(b); total += len(chars)
        units = [a for a in range(b) if math.gcd(a, b) == 1]
        C = np.array([v[units] for _, v in chars]).T/np.sqrt(phi(b))
        check(len(chars) == phi(b) and maxabs(C.conj().T @ C - np.eye(phi(b))) < 1e-12,
              f"b={b}: all {phi(b)} characters, orthonormality")
        vectors = np.array([gauss_vector(v, b) for _, v in chars]).T
        eg = max(maxabs(galois_fourier(b, a) @ vectors - vectors*np.array([v[a % b] for _, v in chars]))
                 for a in units) if b > 1 else 0.
        err_galois = max(err_galois, eg)
        check(eg < 1e-12, f"b={b}: U_a g_chi = chi(a) g_chi for every unit")
        for p in pp:
            if b % p == 0:
                continue
            V = fourier_jump(p*b, p)
            out = np.array([gauss_vector(v, p*b) for _, v in chars]).T
            pred = vectors*np.array([np.conj(v[p % b])/np.sqrt(p) for _, v in chars])
            err = maxabs(V.T @ out - pred)
            err_adj = max(err_adj, err)
            check(err < 1e-12, f"b={b}, p={p}: S3 adjoint scalar for all characters")
        beta = 1.2
        E = np.eye(b)
        for p in primes(47):
            E = transfer(p, b, beta, K=80) @ E
        eig = np.array([np.prod([(1-p**-beta)/(1-np.conj(v[p % b])*p**-beta)
                                 for p in primes(47)]) for _, v in chars])
        err = maxabs(E[np.ix_(units, units)] @ C - C*eig)
        err_bc = max(err_bc, err)
        check(err < 1e-12, f"b={b}: bcmpo.transfer units block has L_P(beta,conj chi)/zeta_P(beta)")
    check(total == B, "sum_{b|120} phi(b)=120: complete Gauss basis of L2(Z/120)")
    # Complex characters mod 5 detect the conjugation convention; all chars above
    # were already checked, these rows make the failed scalar inference explicit.
    rows = []
    for label, values in characters(5):
        for beta in (1., 1.05, 1.2, 2.):
            pp = primes(47)
            actual, residual = coherence_action(values, pp, beta)
            chi = np.conj(values[np.array(pp) % 5])
            rates = np.array(pp, float)**-beta
            predicted = np.sum(rates*(chi/np.array(pp) - 1))
            proposed = np.sum(rates*(chi - 1))
            # Real logarithm difference is unambiguous; complex logs summed locally.
            log_difference = np.sum(np.log(1-chi*rates) - np.log(1-rates))
            power_correction = sum(np.sum((1-chi**k)*rates**k)/k for k in range(2, 161))
            eta = np.prod((1-rates)/(1-chi*rates))
            check(abs(actual-predicted) < 1e-12 and residual > 1e-4,
                  f"chi={label}, beta={beta}: projected scalar corrected; coherence is NOT an eigenvector")
            check(abs(log_difference - (-proposed + power_correction)) < 1e-12
                  and abs(np.exp(-log_difference)-eta) < 1e-12,
                  f"chi={label}, beta={beta}: exact Euler log with bad primes and prime powers")
            rows.append(dict(chi=list(label), beta=beta, projected_real=float(actual.real),
                             projected_imag=float(actual.imag), nonscalar_residual=float(residual),
                             proposed_real=float(proposed.real), log_difference_real=float(log_difference.real),
                             prime_power_correction_real=float(power_correction.real),
                             bc_real=float(eta.real), bc_imag=float(eta.imag)))
    print("max adjoint/Galois/BC errors:", err_adj, err_galois, err_bc)
    print("sample rows:", [r for r in rows if r["chi"] == [1]])
    check.finish(dict(B=B, characters=total, adjoint_error=err_adj, galois_error=err_galois,
                      bc_error=err_bc, rows=rows))


if __name__ == "__main__":
    main()
