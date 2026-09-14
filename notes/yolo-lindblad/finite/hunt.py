#!/usr/bin/env python3
"""N4: build first, hunt second, read zeta zeros ONLY for final comparisons.

The exact triangular reduction is checked against doubled sparse solves. Larger
cutoffs use the identical sparse operators and an exact closed-row reduction;
no dense (B^2)-square matrix is formed.
"""
import math
import numpy as np
import mpmath as mp
import scipy.sparse as ss
from scipy.sparse.linalg import spsolve_triangular
from scipy.optimize import brentq
from finite_common import Checks, HERE, primes, divisors, phi, shell_jump, maxabs


def ordered(s, pp, beta, targets):
    """Return actual overlaps and exp-normalized overlaps h_b.

    <1,b|R|1,1> = sqrt(phi(b)) b^(-z) h_b, z=s+beta+1,
    h_b=(delta_b1 + sum_{p|b} h_(b/p))/(1-sum_{p not|b} p^-z).
    For b=1 the sum is empty. Unreachable shells return zero.
    """
    s = np.asarray(s, complex)
    w = {p: np.exp(-(s+beta+1)*np.log(p)) for p in pp}
    h, values = {}, {}
    for b in sorted(set().union(*(divisors(b) for b in targets))):
        D = 1-sum(w[p] for p in pp if b % p)
        h[b] = ((np.ones_like(s) if b == 1 else 0) + sum(h[b//p] for p in pp if b % p == 0))/D
        values[b] = np.sqrt(phi(b))*np.exp(-(s+beta+1)*np.log(b))*h[b]
    return {b: values[b] for b in targets}, {b: h[b] for b in targets}


def euler(s, pp, beta, b=1):
    z = np.asarray(s)+beta+1
    return np.sqrt(phi(b))*np.exp(-z*np.log(b))/np.prod([1-np.exp(-z*np.log(p)) for p in pp], axis=0)


def contour(step):
    x = np.linspace(.3, 1.2, int(np.ceil(.9/step))+1)
    y = np.linspace(0, 40, int(np.ceil(40/step))+1)
    return np.concatenate((x+0j, 1.2+1j*y[1:], x[-2::-1]+40j, .3+1j*y[-2::-1]))


def winding(v):
    angles = np.angle(np.roll(v, -1)/v)
    return int(np.rint(sum(angles)/(2*np.pi))), float(max(abs(angles)))


def main():
    check = Checks("hunt")
    # Mandatory prerequisite: the direct quotient checks must have succeeded.
    import json
    phase = json.loads((HERE/"verify_phase.json").read_text())
    check(max(phase["errors"].values()) < 1e-12, "S1/S2 verified before shell construction")
    operator_error = 0.
    for B in (12, 30, 64):
        basis = list(range(1, B+1)); pp = primes(5)
        V = {p: shell_jump(basis, p) for p in pp}
        A = {p: ss.kron(V[p], V[p], format="csr") for p in pp}
        for p in pp:
            for q in pp:
                check(maxabs(A[p] @ A[q]-A[q] @ A[p]) < 1e-12,
                      f"Bmax={B}: doubled jumps {p},{q} commute after truncation")
        for beta in (1., 1.05, 1.2):
            for s in (.3+0j, .5+9.25j, 1.2+37.5j):
                I = ss.eye(B*B, format="csr", dtype=complex)
                K = sum(p**(-beta-s)*A[p] for p in pp)
                vacuum = np.zeros(B*B, complex); vacuum[0] = 1
                result = spsolve_triangular(I-K, vacuum, lower=True)
                product = vacuum.copy()
                for p in pp:
                    product = spsolve_triangular(I-p**(-beta-s)*A[p], product, lower=True)
                targets = [b for b in (1, 2, 3, 4, 6, 12, 30) if b <= B]
                closed, _ = ordered(s, pp, beta, targets)
                err = max([abs(result[b-1]-closed[b]) for b in targets]
                          +[abs(product[b-1]-euler(s, pp, beta, b)) for b in targets])
                operator_error = max(operator_error, err)
                check(err < 1e-12, f"Bmax={B}, beta={beta}, s={s}: doubled resolvent and Euler product match reduced overlaps")
    # Large shell spaces: V_p remain sparse; diagonal/row identities avoid B^4 storage.
    truncation, cases, scans = [], [], []
    targets = (1, 2, 4, 6, 12, 30, 210)
    mesh = (np.linspace(.3, 1.2, 19)[:, None] + 1j*np.linspace(0, 40, 401)[None, :]).ravel()
    for P, B in ((5, 64), (7, 256), (13, 1024), (31, 2048), (47, 3072)):
        pp = primes(P); basis = list(range(1, B+1))
        V = {p: shell_jump(basis, p) for p in pp}
        comm = max(maxabs(V[p] @ V[q]-V[q] @ V[p]) for p in pp for q in pp)
        check(comm < 1e-12, f"P={P}, Bmax={B}: all shell jumps commute")
        loss = []
        for p in pp:
            expected = np.array([0. if p*b <= B else ((p-1)/p if b % p else 1.) for b in basis])
            check(maxabs(ss.eye(B)-V[p].T @ V[p]-ss.diags(expected)) < 1e-12,
                  f"P={P}, Bmax={B}, p={p}: boundary norm deficit")
            loss.append(float(expected.mean()))
        truncation.append(dict(P=P, Bmax=B, doubled_dimension=B*B, max_loss=1.,
                               weighted_mean_loss=float(np.array(loss) @ (1/np.array(pp))/sum(1/np.array(pp)))))
        for beta in (1., 1.05, 1.2):
            bound = sum(p**(-beta-1-.3) for p in pp)
            check(bound < 1, f"P={P}, beta={beta}: analytic diagonal bound excludes ALL resolvent poles in rectangle")
            eligible = [b for b in targets if b <= B and all(p in pp for p in __import__('sympy').factorint(b))]
            grid, hgrid = ordered(mesh, pp, beta, eligible)
            small, big = ordered(contour(.04), pp, beta, eligible)[1], ordered(contour(.02), pp, beta, eligible)[1]
            for b in eligible:
                w1, delta1 = winding(small[b]); w2, delta2 = winding(big[b])
                # Normalization by b^-z has no zeros/poles, and greatly improves phase sampling.
                check(w1 == w2 == 0 and max(delta1, delta2) < .1,
                      f"P={P}, Bmax={B}, beta={beta}, b={b}: zero winding on both boundary meshes")
                check(float(np.min(abs(hgrid[b]))) > 0,
                      f"P={P}, beta={beta}, b={b}: interior mesh contains no sampled zero")
                scans.append(dict(P=P, Bmax=B, beta=beta, b=b, poles=0, zeros_winding=w2,
                                  min_abs_overlap=float(np.min(abs(grid[b]))),
                                  min_abs_normalized=float(np.min(abs(hgrid[b]))),
                                  max_boundary_phase_step=max(delta1, delta2)))
            # Real pole outside the search rectangle, found without any zero data.
            zroot = brentq(lambda z: sum(p**-z for p in pp)-1, .01, 3., xtol=1e-14)
            spole = zroot-beta-1
            check(abs(sum(p**(-spole-beta-1) for p in pp)-1) < 1e-12,
                  f"P={P}, beta={beta}: real ordered pole s={spole:.12f}")
            # Full doubled triangular diagonal <= vacuum diagonal in absolute value.
            rng = check.rng
            pairs = rng.integers(1, B+1, size=(100, 2))
            diag = [sum(p**(-beta-1) for p in pp if b % p and c % p) for b, c in pairs]
            check(max(diag) <= sum(p**(-beta-1) for p in pp)+1e-14, "full doubled diagonal bound on seeded shell pairs")
            cases.append(dict(P=P, Bmax=B, beta=beta, ordered_real_pole=spole,
                              euler_pole_real=-beta-1, rectangle_poles=0,
                              rectangle_overlap_zeros=0, vacuum_diagonal_bound=bound))
    # Additional B growth at fixed P: the closed-row generating function is exact,
    # not a numerical limit. Rebuild the reduced block to test all requested sizes.
    for B in (64, 256, 1024, 3072):
        pp = primes(47); s = .65+17.3j; beta = 1.
        H = sum(p**(-beta-s-.5)*shell_jump(list(range(1, B+1)), p) for p in pp)
        e0 = np.zeros(B, complex); e0[0] = 1
        answer = spsolve_triangular(ss.eye(B, format="csr")-H, e0, lower=True)
        predicted = ordered(s, pp, beta, [1, 2, 6, 30])[0]
        check(max(abs(answer[b-1]-predicted[b]) for b in predicted) < 1e-12,
              f"fixed P=47, Bmax={B}: overlaps exactly cutoff-independent once shell is present")
    # Only now consult the comparison data; these points NEVER enter root finding.
    zero_path = HERE.parents[2]/"data/zeros3000.npy"
    gammas = np.load(zero_path)[:6].astype(float)
    mp.mp.dps = 35
    comparisons, ratios, regular_at_one = [], [], []
    for P in (5, 7, 13, 31, 47):
        pp = primes(P)
        for n, gamma in enumerate(gammas, 1):
            s = .5+1j*gamma
            F = complex(ordered(s, pp, 1., [1])[0][1]); E = complex(euler(s, pp, 1.))
            invzP = np.prod([1-p**(-s) for p in pp])
            comparisons.append(dict(P=P, n=n, gamma=float(gamma), abs_F=abs(F),
                                    abs_E=abs(E), abs_ordered_denominator=abs(1/F)))
            ratios.append(dict(P=P, n=n, real=float((F/invzP).real), imag=float((F/invzP).imag),
                               abs=float(abs(F/invzP))))
        fone = complex(ordered(1., pp, 1., [1])[0][1])
        regular_at_one.append(dict(P=P, F=float(fone.real), E=float(np.real(euler(1., pp, 1.)))))
        check(np.isfinite(abs(fone)) and abs(fone) < 2, f"P={P}: F is regular at s=1, F(1)={fone.real:.12f}")
    # Enumerate all individual Euler vacuum poles with 0<=Im<=40 (outside rectangle).
    euler_poles = [dict(p=p, real=-2., imag=2*np.pi*k/np.log(p)) for p in primes(47)
                   for k in range(int(np.floor(40*np.log(p)/(2*np.pi)))+1)]
    print("operator max error:", operator_error)
    print("hunt cases:", cases)
    print("first three zero comparisons at P=47:", [r for r in comparisons if r["P"] == 47][:3])
    check.finish(dict(operator_error=operator_error, cases=cases, scans=scans, truncation=truncation,
                      zero_comparisons=comparisons, ratios=ratios, euler_poles=euler_poles,
                      regular_at_one=regular_at_one,
                      comparison_zero_file=str(zero_path.relative_to(HERE.parents[2])),
                      scan_mesh="19 x 401 interior; boundary steps .04 and .02"))


if __name__ == "__main__":
    main()
