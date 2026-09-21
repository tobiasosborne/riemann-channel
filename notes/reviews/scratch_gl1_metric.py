#!/usr/bin/env python3
"""REFUTE review, GL_1 bond round (2026-09-21), reviewer `claude:opus`.

Two things proposition B5 and the "Reading" of B3 in `notes/gl1-bond/proofs.md`
assert without proof, recomputed here.

(1) B5: "On K_HW, any metric for which FROBENIUS is normal is diagonal in its
    eigenbasis, and the reality and bipartite symmetries fix the ratios".
    thm:arithmetic-metric is a statement about Z (four distinct eigenvalues
    {a,-a,abar,-abar}), not about Frobenius: on K_HW one has Z^2 ~ Fr^{-1} (x) I_2, so
    Frobenius has each eigenvalue TWICE and its normalising metrics form a strictly
    larger, block-diagonal cone.  The two cones are computed here as real vector
    spaces, before and after imposing the bipartite and reality symmetries.
    Also: the genus-one cases where the two Frobenius eigenvalues coincide (q a
    square), where even the H^1 (x) C version of the sentence fails.

(2) B3 "Reading": "H-CLASS ... i.e. the GL_2 scattering matrix is the Fourier
    transform on the GL_1 bond l^2(Pic^0)".  H-CLASS (obs:h-class) states the matrix
    is M . P_inv with M a Pic-group matrix.  Conjugating by the character (Fourier)
    matrix does NOT diagonalise M . P_inv: it block-diagonalises it, with a 2x2
    off-diagonal block on each inverse pair {chi, chibar}.  For Z/4 this is computed
    exactly, and reconciled with thm:d3-channels' eigenvalues {zeta channel, 1, 1, -1}.

(3) B5 support: the genus-one equal-modulus property holds exactly on the Hasse
    interval, with the witness q = 2, h = 6.

python3 notes/reviews/scratch_gl1_metric.py
"""

import itertools

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0


def check(cond, msg):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("ok   %s" % msg)
    else:
        FAIL += 1
        print("FAIL %s" % msg)


# ---------------------------------------------------------------------------
# real dimension of a space of Hermitian 4x4 matrices cut out by linear conditions
# ---------------------------------------------------------------------------

def herm_basis(n=4):
    """a real basis of the n x n Hermitian matrices"""
    B = []
    for i in range(n):
        E = np.zeros((n, n), dtype=complex)
        E[i, i] = 1
        B.append(E)
    for i in range(n):
        for j in range(i + 1, n):
            E = np.zeros((n, n), dtype=complex)
            E[i, j] = 1
            E[j, i] = 1
            B.append(E)
            E = np.zeros((n, n), dtype=complex)
            E[i, j] = 1j
            E[j, i] = -1j
            B.append(E)
    return B


def real_dim(conditions, n=4):
    """dimension of {H hermitian : c(H) = 0 for every c in conditions}.

    each condition maps an n x n complex matrix to an n x n complex matrix; the
    resulting real linear system is solved by SVD."""
    B = herm_basis(n)
    rows = []
    for c in conditions:
        for b in B:
            pass
    M = []
    for b in B:
        col = []
        for c in conditions:
            R = c(b)
            col += list(R.real.flatten()) + list(R.imag.flatten())
        M.append(col)
    M = np.array(M).T           # (#eqs) x (#params)
    if M.size == 0:
        return len(B)
    s = np.linalg.svd(M, compute_uv=False)
    rank = int(np.sum(s > 1e-9 * max(1.0, s[0])))
    return len(B) - rank


print("=" * 78)
print("SECTION 1  the metric cones on K_HW  (B5 against thm:arithmetic-metric)")
print("=" * 78)

for name, alpha, q in [("D2", complex(1, -1), 2), ("D3", complex(0, np.sqrt(3)), 3)]:
    a = np.sqrt(1 / alpha)
    z = np.array([a, -a, np.conj(a), -np.conj(a)])
    r = abs(z[0])
    check(abs(r - q ** (-0.25)) < 1e-12,
          "%s: the four Hasse-Weil wave parameters {a,-a,abar,-abar} with a^2 = "
          "1/alpha_+ have modulus r = q^{-1/4} = %.10f" % (name, r))
    check(len(set(np.round(z, 12))) == 4,
          "%s: the four z_i are distinct" % name)
    Z = np.diag(z)
    Z2 = Z @ Z
    check(len(set(np.round(np.diag(Z2), 12))) == 2,
          "%s: Z^2 (~ Fr^{-1} (x) I_2) has only TWO distinct eigenvalues, each double"
          % name)

    condZ = [lambda H, Z=Z, r=r: Z.conj().T @ H @ Z - r ** 2 * H]
    condF = [lambda H, Z2=Z2, r=r: Z2.conj().T @ H @ Z2 - r ** 4 * H]
    dZ = real_dim(condZ)
    dF = real_dim(condF)
    check(dZ == 4, "%s: {H > 0 : Z^*HZ = r^2 H} is the 4-real-dimensional diagonal "
                   "cone of thm:arithmetic-metric (computed dim %d)" % (name, dZ))
    check(dF == 8, "%s: {H : (Z^2)^*H(Z^2) = r^4 H}, i.e. the FROBENIUS-normal "
                   "metrics, is 8-real-dimensional (two 2x2 blocks), computed dim %d: "
                   "strictly larger, and NOT diagonal in the eigenbasis"
          % (name, dF))

    # parity (z -> -z) and reality (z -> zbar) as permutations of the four modes
    Pp = np.zeros((4, 4))
    for i, j in [(0, 1), (1, 0), (2, 3), (3, 2)]:
        Pp[i, j] = 1
    Rr = np.zeros((4, 4))
    for i, j in [(0, 2), (2, 0), (1, 3), (3, 1)]:
        Rr[i, j] = 1
    check(np.allclose(Pp @ Z @ Pp, -Z), "%s: the parity permutation realises z -> -z"
          % name)
    check(np.allclose(Rr @ Z.conj() @ Rr, Z),
          "%s: the reality permutation realises z -> zbar" % name)
    cond_par = [lambda H, Pp=Pp: Pp @ H @ Pp - H]
    cond_real = [lambda H, Rr=Rr: Rr @ H.conj() @ Rr - H]
    dZs = real_dim(condZ + cond_par + cond_real)
    dFs = real_dim(condF + cond_par + cond_real)
    check(dZs == 1, "%s: with parity AND reality imposed the Z-cone collapses to a "
                    "SINGLE RAY (dim %d) -- thm:arithmetic-metric's statement, which "
                    "is about Z" % (name, dZs))
    check(dFs > 1, "%s: with the SAME two symmetries the Frobenius-normal cone still "
                   "has real dimension %d > 1, so B5's sentence 'any metric for which "
                   "Frobenius is normal is diagonal ... and the symmetries fix the "
                   "ratios' is FALSE as stated on K_HW" % (name, dFs))
    # exhibit an explicit symmetric Frobenius-normal metric that is not diagonal
    found = None
    for t in [0.3, 0.5]:
        H = np.eye(4, dtype=complex)
        H[0, 1] = t
        H[1, 0] = t
        H[2, 3] = t
        H[3, 2] = t
        if (np.allclose(Z2.conj().T @ H @ Z2, r ** 4 * H)
                and np.allclose(Pp @ H @ Pp, H)
                and np.allclose(Rr @ H.conj() @ Rr, H)
                and min(np.linalg.eigvalsh(H)) > 0):
            found = (t, H)
    check(found is not None,
          "%s: explicit witness -- H = I + t(|1><2| + |2><1| + |3><4| + |4><3|) with "
          "t = %s is positive definite, parity- and reality-invariant, and makes "
          "Frobenius normal, yet is not diagonal (so the ratio is not fixed)"
          % (name, found[0] if found else "-"))

print()
print("=" * 78)
print("SECTION 2  genus one with q a square: even the H^1 (x) C version fails")
print("=" * 78)
T = sp.symbols("T")
deg = []
for q in [2, 3, 4, 5, 7, 8, 9, 11, 13, 16]:
    for h in range(0, 4 * q):
        t = q + 1 - h                    # trace of Frobenius
        if t ** 2 > 4 * q:
            continue
        if t ** 2 == 4 * q:
            deg.append((q, h, t))
check(deg == [(4, 1, 4), (4, 9, -4), (9, 4, 6), (9, 16, -6), (16, 9, 8), (16, 25, -8)],
      "the genus-one pairs (q,h) inside the Hasse interval with a DOUBLE Frobenius "
      "root are exactly %s -- all with q a square" % deg)
q, h, t = 4, 1, 4
P = 1 - t * T + q * T ** 2
check(sp.expand(P - (1 - 2 * T) ** 2) == 0,
      "q = 4, h = 1: P(T) = 1-4T+4T^2 = (1-2T)^2, a double Frobenius eigenvalue "
      "alpha = 2 = sqrt q")
Fr = np.array([[2.0, 0.0], [0.0, 2.0]])
dim_any = real_dim([lambda H, Fr=Fr: Fr.conj().T @ H @ Fr - 4 * H], n=2)
check(dim_any == 4,
      "with alpha_1 = alpha_2 the semisimple Frobenius on H^1 (x) C is the scalar 2, "
      "so EVERY metric normalises it: the cone has real dimension %d (all of the "
      "2x2 Hermitian matrices), and 'the reality and bipartite symmetries fix its "
      "ratios' has nothing to fix" % dim_any)
check(q ** 0.5 == 2.0,
      "this is a supersingular genus-one case over a square field, admissible by "
      "Hasse; it is excluded only by the standing hypothesis q in {2,3} of the round")

print()
print("=" * 78)
print("SECTION 3  B5 support: equal modulus <=> the Hasse interval (genus one)")
print("=" * 78)
okint, okout = True, True
for q in [2, 3, 4, 5, 7, 9]:
    for h in range(0, 6 * q):
        t = q + 1 - h
        rts = np.roots([q, -t, 1.0])        # roots of qT^2 - tT + 1, i.e. 1/alpha
        al = [1 / rr for rr in rts]
        eq = abs(abs(al[0]) - abs(al[1])) < 1e-9
        inside = t ** 2 <= 4 * q
        if inside and not eq:
            okint = False
        if (not inside) and eq:
            okout = False
check(okint and okout,
      "for P = 1-(q+1-h)T+qT^2 the two roots have equal modulus exactly when "
      "|q+1-h| <= 2 sqrt q; nothing in B1--B4 forces that inequality")
t = 2 + 1 - 6
al = sorted([1 / r for r in np.roots([2.0, -float(t), 1.0])], key=abs)
check(abs(abs(al[0]) - 1) < 1e-9 and abs(abs(al[1]) - 2) < 1e-9,
      "witness q = 2, h = 6: P = 1+3T+2T^2 = (1+T)(1+2T), alpha = -1,-2, moduli "
      "1 and 2, neither equal to sqrt 2 -- B5(b) is right that h alone does not "
      "force Hasse")

print()
print("=" * 78)
print("SECTION 4  B3 'Reading': a Pic-group matrix TIMES INVERSION is not")
print("            diagonalised by the class characters")
print("=" * 78)
n = 4
w = np.exp(2j * np.pi / n)
Four = np.array([[w ** (i * j) for j in range(n)] for i in range(n)]) / np.sqrt(n)
f = np.array([1.7, 0.3, -0.9, 0.4])          # arbitrary group-matrix data on Z/4
M = np.array([[f[(b - a) % n] for b in range(n)] for a in range(n)])
Pinv = np.array([[1.0 if (b == (-a) % n) else 0.0 for b in range(n)]
                 for a in range(n)])
fh = np.array([sum(f[k] * w ** (-j * k) for k in range(n)) for j in range(n)])
D = Four.conj().T @ M @ Four
check(np.allclose(D, np.diag(np.diag(D))),
      "the Fourier matrix of Z/4 does diagonalise the group matrix M alone "
      "(character values %s)" % np.round(np.diag(D).real, 6))
A = Four.conj().T @ (M @ Pinv) @ Four
off = A - np.diag(np.diag(A))
check(not np.allclose(off, 0),
      "but it does NOT diagonalise M . P_inv: the off-diagonal part has norm %.4f"
      % np.linalg.norm(off))
check(abs(A[1, 3]) > 1e-9 and abs(A[3, 1]) > 1e-9
      and abs(A[1, 1]) < 1e-9 and abs(A[3, 3]) < 1e-9,
      "the surviving off-diagonal entries pair the inverse characters chi and "
      "chibar (here indices 1 and 3); the self-inverse characters 1 and -1 stay "
      "diagonal")
ev = np.sort_complex(np.linalg.eigvals(M @ Pinv))
pred = np.sort_complex(np.array([fh[0], fh[2],
                                 np.sqrt(fh[1] * fh[3]), -np.sqrt(fh[1] * fh[3])]))
check(np.allclose(ev, pred, atol=1e-9),
      "the eigenvalues of M . P_inv are fhat(1), fhat(-1) and +-sqrt(fhat(chi) "
      "fhat(chibar)): the inverse pair contributes a SIGN, not two character values")
# the D3 instance: all three nontrivial L-functions equal 1
fh3 = np.array([complex(2.3), 1.0, 1.0, 1.0])     # zeta channel + three L = 1
f3 = np.array([sum(fh3[j] * w ** (j * k) for j in range(n)) / n for k in range(n)])
M3 = np.array([[f3[(b - a) % n] for b in range(n)] for a in range(n)])
ev3 = np.sort_complex(np.linalg.eigvals(M3 @ Pinv))
check(np.allclose(np.sort_complex(np.array([2.3 + 0j, 1 + 0j, 1 + 0j, -1 + 0j])),
                  ev3, atol=1e-9),
      "with all three nontrivial character factors equal to 1 (the genus-one value "
      "L(T,chi) = 1) the eigenvalues of M . P_inv are {zeta channel, 1, 1, -1}: "
      "exactly thm:d3-channels' one zeta channel and three monomial channels, but "
      "the -1 comes from the INVERSION pairing of chi_i with chi_{-i}, not from a "
      "character value; the three monomial channels are therefore not in bijection "
      "with the three nontrivial characters")

print()
print("=" * 78)
print("CHECKS: %d passed, %d failed" % (PASS, FAIL))
print("=" * 78)
