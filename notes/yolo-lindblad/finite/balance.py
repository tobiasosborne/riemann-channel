#!/usr/bin/env python3
"""N6: test the proposed reverse rates, then separate classical and quantum fixes."""
import math
import numpy as np
import scipy.linalg as la
import scipy.sparse as ss
from scipy.sparse.linalg import spsolve
import sympy as sp
import mpmath as mp
from finite_common import (Checks, shell_jump, lindblad_matrix, divisors,
                           dissipator, maxabs, primes)


def stationary(L, n):
    A = L.tolil(copy=True)
    A[0, :] = np.eye(n).ravel()
    rhs = np.zeros(n*n, complex); rhs[0] = 1
    rho = spsolve(A.tocsr(), rhs).reshape(n, n)
    return (rho+rho.conj().T)/2


def populations(V, r, rate):
    W = V.multiply(V).toarray()
    Q = rate*(W+r*W.T)
    np.fill_diagonal(Q, 0)
    Q -= np.diag(Q.sum(axis=0))
    return Q


def main():
    check = Checks("balance")
    # Minimal exact counterexample (p=2, shells {1,2}, beta=2).
    V = sp.Matrix([[1, 0], [1, 0]])/sp.sqrt(2)
    rho = sp.diag(sp.Rational(4, 5), sp.Rational(1, 5))
    def D(A, X):
        return A*X*A.T-(A.T*A*X+X*A.T*A)/2
    residual = D(V, rho)/2+D(V.T, rho)/8
    check(residual == sp.Matrix([[-sp.Rational(3, 16), sp.Rational(27, 160)],
                                [sp.Rational(27, 160), sp.Rational(3, 16)]]),
          "exact p=2 beta=2 counterexample: proposed Gibbs density is not stationary")
    local_rows = []
    for p in (2, 3, 5):
        n = 7; basis = [p**k for k in range(n)]
        V = shell_jump(basis, p)
        for beta in (2., 1.2, 1.05, 1.01, 1.001, 1.):
            rate, r = 1/p, p**-beta
            L = lindblad_matrix([np.sqrt(rate)*V, np.sqrt(rate*r)*V.T])
            gibbs = np.array(basis, float)**-beta; gibbs /= gibbs.sum()
            inverted = np.array(basis, float)**beta; inverted /= inverted.sum()
            actual = stationary(L, n)
            err = maxabs(L @ actual.ravel())
            positive = float(min(la.eigvalsh(actual)))
            check(err < 1e-11 and positive > -1e-12 and abs(np.trace(actual)-1) < 1e-12,
                  f"p={p}, beta={beta}: actual finite GKSL stationary state, positive and trace one")
            Q = populations(V, r, rate)
            check(maxabs(Q @ inverted) < 1e-12 and maxabs(Q @ gibbs) > 1e-4,
                  f"p={p}, beta={beta}: classical balance gives b^(+beta), not b^(-beta)")
            # Swap the rate orientation: populations now balance, but coherences remain.
            Lcorrect = lindblad_matrix([np.sqrt(rate*r)*V, np.sqrt(rate)*V.T])
            Qcorrect = r*populations(V, 1/r, rate)
            off = (Lcorrect @ np.diag(gibbs).ravel()).reshape(n, n)
            check(maxabs(Qcorrect @ gibbs) < 1e-12 and maxabs(np.diag(off)) < 1e-12
                  and maxabs(off-np.diag(np.diag(off))) > 1e-4,
                  f"p={p}, beta={beta}: corrected rate orientation fixes populations but creates shell coherences")
            local_rows.append(dict(p=p, levels=n, beta=beta,
                                   gibbs_residual=float(la.norm(L @ np.diag(gibbs).ravel())),
                                   corrected_rate_gibbs_residual=float(la.norm(off)),
                                   actual_residual=err, stationary_min_eigenvalue=positive,
                                   stationary_vacuum=float(actual[0, 0].real),
                                   stationary_top=float(actual[-1, -1].real),
                                   stationary_coherence_norm=float(la.norm(actual-np.diag(np.diag(actual))))))
    # Tensor product/divisor shell model, using the same V_p as the hunt.
    B = 2**3*3**2*5
    basis, pp = divisors(B), (2, 3, 5)
    V = {p: shell_jump(basis, p) for p in pp}
    product_rows = []
    for beta in (2., 1.2, 1.05, 1.01, 1.):
        jumps = [A for p in pp for A in (V[p]/np.sqrt(p), np.sqrt(p**(-beta-1))*V[p].T)]
        L = lindblad_matrix(jumps)
        rho = stationary(L, len(basis))
        g = np.array(basis, float)**-beta; g /= g.sum()
        check(maxabs(L @ rho.ravel()) < 1e-11 and min(la.eigvalsh(rho)) > -1e-12,
              f"B={B}, beta={beta}: finite divisor-shell stationary density computed")
        check(maxabs(np.eye(len(basis)).ravel() @ L) < 1e-12,
              f"B={B}, beta={beta}: anticommutators restore exact trace preservation")
        product_rows.append(dict(B=B, states=len(basis), beta=beta,
                                 gibbs_residual=float(la.norm(L @ np.diag(g).ravel())),
                                 vacuum=float(rho[0, 0].real), top=float(rho[-1, -1].real),
                                 coherence_norm=float(la.norm(rho-np.diag(np.diag(rho))))))
    # A genuinely classical/number-ladder repair, stated as a different model:
    # resolve every edge as its own jump and use upward/downward ratio p^-beta.
    repaired_rows = []
    for beta in (2., 1.2, 1.01, 1.):
        basis = list(range(1, 65)); n = len(basis)
        jumps = []
        for p in primes(7):
            for b in basis:
                if p*b <= n:
                    A = ss.csr_matrix(([1.], ([p*b-1], [b-1])), shape=(n, n))
                    jumps.extend([np.sqrt(p**(-beta-1))*A, A.T/np.sqrt(p)])
        L = lindblad_matrix(jumps)
        g = np.array(basis, float)**-beta; g /= g.sum()
        error = maxabs(L @ np.diag(g).ravel())
        check(error < 1e-12, f"resolved edges, beta={beta}: b^-beta Gibbs weights genuinely stationary")
        repaired_rows.append(dict(Bmax=64, P=7, beta=beta, error=error))
    # Cutoff mass of the proposed number-shell Gibbs family: finite-prime critical
    # limits are regular; divergence appears only when the prime/state cutoff grows.
    critical = []
    mp.mp.dps = 35
    for beta in (2., 1.2, 1.05, 1.01, 1.):
        for B in (64, 256, 1024, 3072):
            Z = float(sum(np.arange(1, B+1, dtype=float)**-beta))
            captured = float(Z/mp.zeta(beta)) if beta > 1 else None
            check(Z > 1 and (captured is None or 0 < captured < 1),
                  f"Bmax={B}, beta={beta}: finite Gibbs partition and captured infinite mass")
            critical.append(dict(beta=beta, Bmax=B, Z=Z, captured_mass=captured, vacuum=1/Z))
    smooth = [dict(P=P, Z_at_beta1=float(np.prod([1/(1-1/p) for p in primes(P)]))) for P in (5, 7, 13, 31, 47)]
    print("p=2 stationary states:", [r for r in local_rows if r["p"] == 2])
    print("product states:", product_rows)
    print("critical cutoff rows:", critical)
    check.finish(dict(exact_counterexample=[[str(x) for x in row] for row in residual.tolist()],
                      local_rows=local_rows, product_rows=product_rows, repaired_rows=repaired_rows,
                      critical=critical, smooth=smooth))


if __name__ == "__main__":
    main()
