#!/usr/bin/env python3
"""N1: direct Haar quotient/Fourier checks BEFORE constructing shell models."""
import math
import numpy as np
import scipy.sparse as ss
from finite_common import (Checks, divisors, phi, shell_fourier, position_jump,
                           fourier_jump, galois_fourier, shell_jump, maxabs)


def main():
    check = Checks("verify_phase")
    errors = dict(isometry=0., fourier=0., shell_forward=0., shell_adjoint=0.,
                  covariance=0., commute=0.)
    for N in (12, 30, 60, 84, 120):
        F = np.exp(2j*np.pi*np.outer(np.arange(N), np.arange(N))/N)/np.sqrt(N)
        for p in (2, 3, 5, 7):
            if N % p:
                continue
            M = N//p
            Fm = np.exp(2j*np.pi*np.outer(np.arange(M), np.arange(M))/M)/np.sqrt(M)
            J, V = position_jump(N, p), fourier_jump(N, p)
            ei = maxabs(J.T @ J - ss.eye(M))
            ef = maxabs(F.conj().T @ (J @ Fm) - V.toarray())
            errors["isometry"] = max(errors["isometry"], ei)
            errors["fourier"] = max(errors["fourier"], ef)
            check(ei < 1e-12 and ef < 1e-12, f"N={N}, p={p}: direct isometry and both Fourier formulas")
            ec = max(maxabs(galois_fourier(N, a) @ V - V @ galois_fourier(M, a % M))
                     for a in range(1, N) if math.gcd(a, N) == 1)
            errors["covariance"] = max(errors["covariance"], ec)
            check(ec < 1e-12, f"N={N}, p={p}: V_p U_a = U_a V_p for every unit")
    for p in (2, 3, 5, 7):
        M, N = 60, p*60
        J = position_jump(N, p)
        for b in divisors(M):
            v = shell_fourier(b, M)
            # Explicit position map, followed by the Fourier transform.
            direct = np.fft.fft(J @ (np.fft.ifft(v)*np.sqrt(M)))/np.sqrt(N)
            pred = (shell_fourier(b, N) + np.sqrt(p - 1)*shell_fourier(p*b, N))/np.sqrt(p) if b % p else shell_fourier(p*b, N)
            ef = maxabs(direct - pred)
            direct_adj = np.fft.fft(J.T @ (np.fft.ifft(shell_fourier(b, N))*np.sqrt(N)))/np.sqrt(M)
            pred_adj = shell_fourier(b, M)/np.sqrt(p) if b % p else np.sqrt(phi(b)/(p*phi(b//p)))*shell_fourier(b//p, M)
            ea = maxabs(direct_adj - pred_adj)
            errors["shell_forward"] = max(errors["shell_forward"], ef)
            errors["shell_adjoint"] = max(errors["shell_adjoint"], ea)
            check(max(ef, ea) < 1e-12, f"b={b}, p={p}: S2 and its adjoint in position space")
    for N, p, q in ((60, 2, 3), (210, 3, 7), (420, 5, 7), (120, 2, 2)):
        err = maxabs(position_jump(N, p) @ position_jump(N//p, q)
                     - position_jump(N, q) @ position_jump(N//q, p))
        errors["commute"] = max(errors["commute"], err)
        check(err < 1e-12, f"N={N}: V_{p} V_{q} = V_{q} V_{p}, compatible quotients")
    truncation = []
    for B in (30, 120, 420):
        basis = divisors(B)
        for p in (2, 3, 5, 7):
            V = shell_jump(basis, p)
            loss = np.array([0. if p*b in basis else ((p - 1)/p if b % p else 1.) for b in basis])
            check(maxabs(ss.eye(len(basis)) - V.T @ V - ss.diags(loss)) < 1e-12,
                  f"B={B}, p={p}: exact dropped-column norm formula")
            truncation.append(dict(B=B, states=len(basis), p=p, max_loss=float(max(loss)), mean_loss=float(np.mean(loss))))
    print("maximum errors:", errors)
    check(max(errors.values()) < 1e-12, "all S1/S2 errors below 1e-12")
    check.finish(dict(errors=errors, truncation=truncation))


if __name__ == "__main__":
    main()
