"""Weil positivity for an arbitrary finite-dimensional transfer operator: numerical tests.

Conventions follow scripts/qihara_general.py and notes/quantum-ihara-general.md sections 1-2:
V = M_n with the Hilbert-Schmidt inner product, N = n^2, Ad(A) = conj(A) (x) A in column
stacking, D = 2m operators B_1..B_D with a fixed-point-free reversal i -> ibar, and the
non-backtracking superoperator T(v (x) |i>) = sum_{j != ibar} Ad(B_i) v (x) |j> on V (x) C^D.

Weil data.  For a matrix X, a trivial multiset S of eigenvalues (matched to the nearest
computed eigenvalues) and a radius r > 0,
    nu_l = r^{-l} ( Tr X^l - sum_{mu in S} mu^l ) = sum_{mu in spec(X) - S} (mu/r)^l,  l >= 0,
    nu_{-l} = conj(nu_l),
and the Weil (Toeplitz) form is the Hermitian matrix W_{lm} = nu_{l-m}, 0 <= l,m <= L.
"Weil positive" = min eig(W) >= -1e-9 * scale(W).  "One-sided bound" = max |mu| over
spec(X) - S is <= r (1 + 1e-9).  J(mu) = r^2 / conj(mu) is the reflection in the circle |mu|=r,
f_c(z) = sum_l c_l z^l, and the mode-pairing form is M(c) = sum_mu f_c(mu/r) conj(f_c(J(mu)/r)).

Tests T1..T5 are the ones set out in the brief; each prints PASS/FAIL with numbers.  Where a
drafted statement is contradicted by the numerics, the drafted form is printed as a FAIL and the
corrected form immediately after it as a separate check -- nothing is tuned away.
"""
import itertools
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linear_sum_assignment

np.seterr(over='ignore', invalid='ignore')
RESULTS = []


def record(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(f'  [{"PASS" if ok else "FAIL"}] {name}' + (f'   {detail}' if detail else ''))


def head(title):
    print('\n' + '=' * 100)
    print(title)
    print('=' * 100)


# ---------------------------------------------------------------- basic objects ----------
def ad(A):                                   # rho -> A rho A^dagger, column stacking
    return np.kron(A.conj(), A)


def hashimoto(Es, inv):                      # T(v (x) |i>) = sum_{j != inv[i]} E_i v (x) |j>
    N = Es[0].shape[0]
    D = len(Es)
    T = np.zeros((N * D, N * D), complex)
    for i in range(D):
        for j in range(D):
            if j != inv[i]:
                T[j * N:(j + 1) * N, i * N:(i + 1) * N] = Es[i]
    return T


def kraus_T(Bs, inv):
    return hashimoto([ad(B) for B in Bs], inv)


def cgauss(rng, n):
    return rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))


def haar(rng, n):
    z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / abs(np.diag(r)))


# ---------------------------------------------------------------- Weil machinery ----------
def nu_sequence(evals, r, L):
    z = np.asarray(evals, complex) / r
    return np.array([np.sum(z ** l) for l in range(L + 1)])


def weil_matrix(nu):
    L1 = len(nu)
    k = np.subtract.outer(np.arange(L1), np.arange(L1))
    return np.where(k >= 0, nu[np.abs(k)], np.conj(nu[np.abs(k)]))


def psd_report(W, tol=1e-9):
    w = np.linalg.eigvalsh((W + W.conj().T) / 2)
    scale = max(1.0, float(np.max(np.abs(W))))
    return float(w[0]), float(w[0] / scale), bool(w[0] >= -tol * scale)


def weil_psd(evals, r, L=40, tol=1e-9):
    return psd_report(weil_matrix(nu_sequence(evals, r, L)), tol)


def one_sided(evals, r):
    mx = float(np.max(np.abs(evals))) if len(evals) else 0.0
    return mx, bool(mx <= r * (1 + 1e-9))


def remove_nearest(evals, S):
    """Remove, for each s in S, the not-yet-removed eigenvalue closest to s."""
    ev = list(np.asarray(evals, complex))
    worst = 0.0
    for s in S:
        d = [abs(e - s) for e in ev]
        i = int(np.argmin(d))
        worst = max(worst, d[i])
        ev.pop(i)
    return np.array(ev, complex), worst


def multiset_dist(A, B):
    """Optimal-matching (bottleneck) distance between two equal-size multisets."""
    A = np.asarray(A, complex)
    B = np.asarray(B, complex)
    if len(A) != len(B):
        return np.inf
    if len(A) == 0:
        return 0.0
    C = np.abs(A[:, None] - B[None, :])
    C = np.where(np.isfinite(C), C, 1e300)
    r, c = linear_sum_assignment(C)
    return float(C[r, c].max())


def threshold_radius(evals, L=40, tol=1e-9, lo=None, hi=None, iters=28):
    """Smallest r for which the Weil form is PSD, by bisection (PSD is monotone in r)."""
    mx = float(np.max(np.abs(evals)))
    lo = 0.7 * mx if lo is None else lo
    hi = 1.05 * mx if hi is None else hi
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if weil_psd(evals, mid, L, tol)[2]:
            hi = mid
        else:
            lo = mid
    return hi


def weil_form(c, evals, r):
    nu = nu_sequence(evals, r, len(c) - 1)
    return complex(np.einsum('l,m,lm->', c, c.conj(), weil_matrix(nu)))


def mode_pairing_form(c, evals, r):
    z = np.asarray(evals, complex) / r
    f = lambda w: np.sum(c * np.power.outer(w, np.arange(len(c))), axis=-1)
    return complex(np.sum(f(z) * np.conj(f(r / np.conj(np.asarray(evals, complex))))))


# ==========================================================================================
head('T1.  Adjoint-paired Kraus families:  Weil positivity  <=>  one-sided bound')
print("""Random B_1..B_m with complex Gaussian entries, B_{m+k} = B_k^dagger, reversal i -> i+m.
mu_0 = Perron eigenvalue of T (largest modulus), r = sqrt(mu_0), S = {mu_0}, L = 40.
The family is also rescaled by c (B -> cB scales spec(T) by c^2 and r by |c|), which moves the
one-sided bound across its threshold, so both regimes are exercised.

The theorem is "positive definite for EVERY L", so at a fixed L only one half is an identity:
  bound  ==>  W(L) PSD for every L,
  no bound  ==>  W(L) not PSD for L large enough.
A mode just outside the circle is masked at small L by the strictly positive contribution of the
modes inside it, so the second half is checked with an increasing-L escalation.""")

t1_cases = [(2, 2), (2, 3), (3, 2)]
scales = [0.35, 0.6, 1.0, 1.6, 3.0]
n_bound, n_tot, n_viol, masked = 0, 0, 0, []
perron_ok, conj_seeds, thr_seeds = True, [], []
for (n, m) in t1_cases:
    agree_c, bound_c, tot_c, viol_c = 0, 0, 0, 0
    for seed in range(20):
        rng = np.random.default_rng(10000 + 100 * n + 10 * m + seed)
        Bs = [cgauss(rng, n) for _ in range(m)]
        Bs = Bs + [B.conj().T for B in Bs]
        D = 2 * m
        inv = [(i + m) % D for i in range(D)]
        T = kraus_T(Bs, inv)
        ev, vec = np.linalg.eig(T)
        k0 = int(np.argmax(np.abs(ev)))
        mu0 = ev[k0]
        if seed < 3:
            # Perron: mu_0 real positive, eigenvector blockwise PSD (up to a global phase)
            v = vec[:, k0]
            blocks = [v[i * n * n:(i + 1) * n * n].reshape(n, n, order='F') for i in range(D)]
            ph = np.exp(-1j * np.angle(np.trace(blocks[0])))
            mins = [np.linalg.eigvalsh((ph * B + (ph * B).conj().T) / 2)[0] for B in blocks]
            herm = max(np.max(np.abs(ph * B - (ph * B).conj().T)) for B in blocks)
            okp = (abs(mu0.imag) < 1e-8 * abs(mu0)) and mu0.real > 0 and min(mins) > -1e-8 and herm < 1e-8
            perron_ok = perron_ok and okp
        mu0 = mu0.real
        for c in scales:
            evs = ev * c ** 2
            r = np.sqrt(mu0 * c ** 2)
            nt, matchd = remove_nearest(evs, [mu0 * c ** 2])
            mx, bound = one_sided(nt, r)
            mn, mnr, psd = weil_psd(nt, r, 40)
            tot_c += 1
            bound_c += int(bound)
            agree_c += int(bound == psd)
            if bound and not psd:
                viol_c += 1
            if (not bound) and psd:
                masked.append((n, m, seed, c, mx, r, nt.copy()))
            if seed == 0 and abs(c - 1.0) < 1e-12:
                mn80, _, psd80 = weil_psd(nt, r, 80)
                print(f'    n={n} m={m} seed 0, c=1: r = {r:.4f}, max|mu| off S = {mx:.4f}, '
                      f'min eig W(L=40) = {mn:.3e}, min eig W(L=80) = {mn80:.3e}, '
                      f'bound={bound}, PSD(L=40)={psd}, PSD(L=80)={psd80}')
        if seed < 3:
            nt, _ = remove_nearest(ev, [mu0])
            safe = np.where(np.abs(nt) > 1e-12, nt, 1.0)
            img = np.where(np.abs(nt) > 1e-12, mu0 / safe, 1e150)
            conj_seeds.append((n, m, seed, multiset_dist(nt, np.conj(nt)), multiset_dist(nt, img)))
            if seed == 0:
                thr_seeds.append((n, m, seed,
                                  [threshold_radius(nt, L=LL) for LL in (40, 160, 640)],
                                  float(np.max(np.abs(nt)))))
    print(f'  n={n}, m={m}, D={2*m}: {agree_c}/{tot_c} (seed, scale) cases agree at L = 40; '
          f'one-sided bound held in {bound_c}/{tot_c} of them')
    n_bound += bound_c
    n_tot += tot_c
    n_viol += viol_c

record('T1a  one-sided bound ==> Weil form PSD at L = 40 (no counterexample)',
       n_viol == 0, f'{n_tot} cases, bound true in {n_bound}, false in {n_tot - n_bound}, '
                    f'violations {n_viol}')

esc_ok, esc_lines = True, []
for (n, m, seed, c, mx, r, nt) in masked:
    LL = None
    for Ltry in (160, 640, 2560):
        if not weil_psd(nt, r, Ltry)[2]:
            LL = Ltry
            break
    esc_ok = esc_ok and LL is not None
    esc_lines.append(f'    n={n} m={m} seed {seed} scale {c}: max|mu|/r = {mx/r:.6f}, '
                     f'PSD at L=40, first failure at L = {LL}')
print(f'  cases with max |mu| > r that are still PSD at L = 40 (finite-L masking): {len(masked)}')
for line in esc_lines:
    print(line)
record('T1a2  every such case loses positivity at larger L (no bound ==> not PSD eventually)',
       esc_ok and len(masked) > 0,
       f'{len(masked)} masked cases, all resolved by L <= 2560')
record('T1b  Perron eigenvalue of T is real > 0 with a blockwise-PSD eigenvector', perron_ok)

print('  threshold radius (smallest r with W PSD) vs max |mu| off S, as L grows:')
thr_ok, mono_ok = True, True
for (n, m, seed, thr, mx) in thr_seeds:
    rels = [abs(t - mx) / mx for t in thr]
    thr_ok = thr_ok and rels[-1] < 1e-3
    mono_ok = mono_ok and thr[0] < thr[1] < thr[2] <= mx * (1 + 1e-9)
    print(f'    n={n} m={m} seed {seed}: max|mu| = {mx:.6f};  '
          + ',  '.join(f'L={LL}: {t:.6f} (rel {rl:.1e})' for LL, t, rl in zip((40, 160, 640), thr, rels)))
record('T1c  threshold radius increases with L to max |mu| off S, agreeing to 3 digits at L = 640',
       thr_ok and mono_ok)

print('  nontrivial spectrum: distance to its complex conjugate, and to its image under mu -> mu_0/mu:')
conj_ok, inv_ok = True, True
for (n, m, seed, dc, di) in conj_seeds:
    conj_ok = conj_ok and dc < 1e-8
    inv_ok = inv_ok and di > 1e-3
    print(f'    n={n} m={m} seed {seed}: d(spec, conj spec) = {dc:.2e}, d(spec, mu_0/spec) = {di:.3e}')
record('T1d  nontrivial spectrum closed under complex conjugation (< 1e-8)', conj_ok)
record('T1e  nontrivial spectrum NOT invariant under mu -> mu_0/mu', inv_ok)


# ==========================================================================================
head('T2.  Unitary Kraus families:  Ihara-Bass, the duality of the spectrum, Hastings bound')


def unitary_case(label, Us, n, verbose=True):
    """Us = U_1..U_m followed by their adjoints."""
    D = len(Us)
    m = D // 2
    N = n * n
    q = D - 1
    inv = [(i + m) % D for i in range(D)]
    T = kraus_T(Us, inv)
    Sig = sum(ad(U) for U in Us)
    Phi = Sig / D
    out = {'label': label, 'n': n, 'D': D, 'T': T, 'Phi': Phi}

    # (i) det(1-uT) = (1-u^2)^{N(D-2)/2} det(1 - u Sigma + (D-1) u^2)
    worst = 0.0
    for u in (0.13, 0.21 + 0.09j, -0.17):
        lhs = np.linalg.det(np.eye(N * D) - u * T)
        rhs = (1 - u * u) ** (N * (D - 2) / 2) * np.linalg.det(np.eye(N) - u * Sig + q * u * u * np.eye(N))
        worst = max(worst, abs(lhs / rhs - 1))
    out['det_err'] = worst

    # Phi is HS-self-adjoint, so its spectrum is real
    out['sa_err'] = float(np.max(np.abs(Sig - Sig.conj().T)))
    lam = np.linalg.eigvals(Phi)
    out['lam_imag'] = float(np.max(np.abs(lam.imag)))
    lam = np.sort_complex(lam).real

    # trivial multiset S
    S = [1.0] * (N * (D - 2) // 2) + [-1.0] * (N * (D - 2) // 2)
    for l in lam:
        if abs(l - 1) < 1e-8:
            S += [float(q), 1.0]
        elif abs(l + 1) < 1e-8:
            S += [-float(q), -1.0]
    nontriv_lam = np.array([l for l in lam if abs(l - 1) >= 1e-8 and abs(l + 1) >= 1e-8])
    ev = np.linalg.eigvals(T)
    nt, matchd = remove_nearest(ev, S)
    out['match'] = matchd
    out['nt'] = nt
    out['lam_nt'] = nontriv_lam
    r = np.sqrt(q)
    out['r'] = r

    out['fe_dist'] = multiset_dist(nt, q / nt)                     # mu -> (D-1)/mu
    out['J_dist'] = multiset_dist(nt, q / np.conj(nt))             # mu -> (D-1)/conj(mu)
    out['circle'] = float(np.max(np.abs(np.abs(nt) - r)))          # 0 iff all on |mu| = sqrt(D-1)
    out['Jfix'] = float(np.max(np.abs(q / np.conj(nt) - nt)))      # 0 iff every mode is J-fixed
    out['hast'] = float(np.max(np.abs(nontriv_lam))) if len(nontriv_lam) else 0.0
    out['hast_bd'] = 2 * np.sqrt(q) / D
    out['hast_ok'] = out['hast'] <= out['hast_bd'] * (1 + 1e-9)
    mn, mnr, psd = weil_psd(nt, r, 40)
    out['min_eig'] = mn
    out['psd'] = psd
    out['mx'], out['bound'] = one_sided(nt, r)
    if verbose:
        print(f'  {label}: n={n}, D={D}, dim T = {N*D}, trivial |S| = {len(S)}, '
              f'nontrivial modes {len(nt)}')
        print(f'    Ihara-Bass det identity: max rel err {out["det_err"]:.2e};  '
              f'|Sigma - Sigma^dag| = {out["sa_err"]:.2e};  max |Im lambda(Phi)| = {out["lam_imag"]:.2e}')
        print(f'    nearest-match residual when removing S: {matchd:.2e}')
        print(f'    nontrivial spec(Phi) = {np.array2string(nontriv_lam, precision=4)}')
        print(f'    max |lambda| off +-1 = {out["hast"]:.6f}  vs  Hastings 2 sqrt(D-1)/D = '
              f'{out["hast_bd"]:.6f}  -> bound {out["hast_ok"]}')
        print(f'    max |mu| off S = {out["mx"]:.6f}  vs  r = sqrt(D-1) = {r:.6f};  '
              f'max ||mu| - r| = {out["circle"]:.2e}')
        print(f'    min eig of Weil form (L=40) = {mn:.3e}  -> Weil positive {psd}')
    return out


cases = []
rng = np.random.default_rng(20260912)
Us = [haar(rng, 2) for _ in range(2)]
cases.append(unitary_case('Haar n=2, D=4 (seed 20260912)', Us + [U.conj().T for U in Us], 2))
rng3 = np.random.default_rng(3141)
Us3 = [haar(rng3, 3) for _ in range(3)]
cases.append(unitary_case('Haar n=3, D=6 (seed 3141)', Us3 + [U.conj().T for U in Us3], 3))
X = np.array([[0, 1], [1, 0]], complex)
Z = np.array([[1, 0], [0, -1]], complex)
cases.append(unitary_case('Pauli X,Z  n=2, D=4 (Ramanujan, Phi has eigenvalue -1)',
                          [X, Z, X.conj().T, Z.conj().T], 2))

# families VIOLATING the Hastings bound (the equivalence must be checked on both sides)
for (nn, mm, sd) in ((2, 2, 900000), (2, 3, 900000)):
    rv = np.random.default_rng(sd)
    Uv = [haar(rv, nn) for _ in range(mm)]
    cases.append(unitary_case(f'Haar n={nn}, D={2*mm}, seed {sd} (violates the Hastings bound)',
                              Uv + [U.conj().T for U in Uv], nn))

# search for a Haar D=4, n=2 family meeting the Hastings bound
found = None
for s in range(200):
    rs = np.random.default_rng(500000 + s)
    U2 = [haar(rs, 2) for _ in range(2)]
    fam = U2 + [U.conj().T for U in U2]
    Sig = sum(ad(U) for U in fam)
    lam = np.sort(np.linalg.eigvals(Sig / 4).real)
    lnt = np.array([l for l in lam if abs(l - 1) >= 1e-8 and abs(l + 1) >= 1e-8])
    if len(lnt) and np.max(np.abs(lnt)) <= 2 * np.sqrt(3) / 4:
        found = (s, fam)
        break
if found is not None:
    print(f'  Hastings-bound search over 200 Haar seeds: first passing seed = {found[0]}')
    cases.append(unitary_case(f'Haar n=2, D=4, searched Ramanujan seed {found[0]}', found[1], 2))
else:
    print('  Hastings-bound search over 200 Haar seeds: none found')

record('T2a  Ihara-Bass det identity det(1-uT) = (1-u^2)^{N(D-2)/2} det(1-u Sigma+(D-1)u^2)',
       all(c['det_err'] < 1e-9 for c in cases),
       f'max rel err {max(c["det_err"] for c in cases):.2e}')
record('T2b  Sigma is HS-self-adjoint, spec(Phi) real',
       all(c['sa_err'] < 1e-10 and c['lam_imag'] < 1e-9 for c in cases))
record('T2c  nontrivial spec(T) invariant under mu -> (D-1)/mu (always)',
       all(c['fe_dist'] < 1e-7 for c in cases),
       'max matching distance ' + f'{max(c["fe_dist"] for c in cases):.2e}')
record('T2d  Weil positivity (r = sqrt(D-1), S as above) == Hastings bound |lambda| <= 2 sqrt(D-1)/D',
       all(c['psd'] == c['hast_ok'] for c in cases),
       'passing cases: ' + ', '.join(f'{c["label"].split(",")[0]}:{c["hast_ok"]}' for c in cases))
record('T2e  Weil positivity == one-sided bound max |mu| <= sqrt(D-1)',
       all(c['psd'] == c['bound'] for c in cases))

print('  drafted claim (ii): "nontrivial spec is J-invariant, J(mu) = (D-1)/conj(mu), exactly when')
print('  it lies on the circle |mu| = sqrt(D-1)".  Measured, per case:')
for c in cases:
    print(f'    {c["label"]}: d(spec, J spec) = {c["J_dist"]:.2e}, '
          f'max ||mu| - r| = {c["circle"]:.2e}, max |J(mu) - mu| = {c["Jfix"]:.2e}')
record('T2f  DRAFTED: J-invariance of the multiset holds exactly when the modes are on the circle',
       all((c['J_dist'] < 1e-7) == (c['circle'] < 1e-7) for c in cases),
       'see the corrected statements T2g/T2h below')
record('T2g  CORRECTED: the multiset is J-invariant in every case (conjugation-closed and '
       'mu -> (D-1)/mu invariant, hence closed under the composite J)',
       all(c['J_dist'] < 1e-7 for c in cases))
record('T2h  CORRECTED: every mode is a FIXED POINT of J  <=>  all modes on |mu| = sqrt(D-1)',
       all((c['Jfix'] < 1e-7) == (c['circle'] < 1e-7) for c in cases))

# W(c) = M(c) for random coefficient vectors
rngc = np.random.default_rng(77)
wm_err = 0.0
for c in cases:
    for _ in range(5):
        cc = rngc.normal(size=13) + 1j * rngc.normal(size=13)
        a = weil_form(cc, c['nt'], c['r'])
        b = mode_pairing_form(cc, c['nt'], c['r'])
        wm_err = max(wm_err, abs(a - b) / max(1.0, abs(a)))
record('T2i  W(c) = M(c) (Weil form = mode-pairing form) for 5 random c per unitary case',
       wm_err < 1e-9, f'max relative difference {wm_err:.2e}')


# ==========================================================================================
head('T3.  Inverse-paired but non-unitary Kraus family:  B_{m+k} = B_k^{-1}, n = 2, m = 2')
print("""Corollary 3 applies (E_ibar = E_i^{-1}), so the nontrivial spectrum (spec(T) minus +-1
with multiplicity N(D-2)/2 each) must be invariant under mu -> (D-1)/mu = 3/mu.""")

fe_ok, det_ok, nonunit = True, True, 0.0
conj_dists, fe_dists, trace_min, trace_imag, word_err = [], [], [], [], 0.0
for seed in range(5):
    rng = np.random.default_rng(4242 + seed)
    Bs = [cgauss(rng, 2) for _ in range(2)]
    Bs = Bs + [np.linalg.inv(B) for B in Bs]
    D, m, n, N = 4, 2, 2, 4
    inv = [(i + m) % D for i in range(D)]
    T = kraus_T(Bs, inv)
    Sig = sum(ad(B) for B in Bs)
    # the family is genuinely not unitary up to a scalar: B^dag B is not a multiple of 1
    for B in Bs[:2]:
        G = B.conj().T @ B
        nonunit = max(nonunit, float(np.max(np.abs(G - np.trace(G) / n * np.eye(n)))) / float(np.trace(G).real / n))
    for u in (0.031, 0.017 + 0.009j):
        lhs = np.linalg.det(np.eye(N * D) - u * T)
        rhs = (1 - u * u) ** (N * (D - 2) / 2) * np.linalg.det(np.eye(N) - u * Sig + (D - 1) * u * u * np.eye(N))
        det_ok = det_ok and abs(lhs / rhs - 1) < 1e-8
    ev = np.linalg.eigvals(T)
    S0 = [1.0] * (N * (D - 2) // 2) + [-1.0] * (N * (D - 2) // 2)
    nt, matchd = remove_nearest(ev, S0)
    d_fe = multiset_dist(nt, (D - 1) / nt)
    fe_ok = fe_ok and d_fe < 1e-6
    fe_dists.append(d_fe)
    conj_dists.append(multiset_dist(nt, np.conj(nt)))
    tr = np.array([np.trace(np.linalg.matrix_power(T, l)) for l in range(1, 9)])
    trace_min.append(float(np.min(tr.real / np.abs(tr))))          # relative: sign of Tr T^l
    trace_imag.append(float(np.max(np.abs(tr.imag) / np.abs(tr))))  # relative: is it real?
    if seed == 0:
        print(f'  seed 0: |S_0| = {len(S0)} (removal residual {matchd:.2e}), nontrivial modes {len(nt)}')
        print(f'    d(spec, 3/spec) = {d_fe:.2e},   d(spec, conj spec) = {conj_dists[-1]:.2e}')
        print(f'    |mu| for the nontrivial modes: '
              f'{np.array2string(np.sort(np.abs(nt)), precision=4)}   (sqrt(3) = {np.sqrt(3):.4f})')
        print(f'    Tr T^l, l = 1..8: {np.array2string(tr, precision=4)}')
    # Corollary 2 trace formula, which does not use the pairing
    for l in range(1, 6):
        tot = 0
        for w in itertools.product(range(D), repeat=l):
            if all(w[(k + 1) % l] != inv[w[k]] for k in range(l)):
                P = np.eye(n, dtype=complex)
                for i in w:
                    P = Bs[i] @ P
                tot += abs(np.trace(P)) ** 2
        tl = np.trace(np.linalg.matrix_power(T, l))
        word_err = max(word_err, abs(tl - tot) / max(1.0, abs(tl)))

record('T3a  the family is inverse-paired but NOT unitary up to a scalar (B^dag B is not a '
       'multiple of 1), so the two pairings genuinely differ', nonunit > 0.1,
       f'max relative deviation of B^dag B from a scalar over 5 seeds: {nonunit:.3f}')
record('T3a2 Corollary 3 determinant identity holds for the inverse-paired family', det_ok)
record('T3b  nontrivial spectrum invariant under mu -> (D-1)/mu  (Corollary 3 functional equation)',
       fe_ok, f'5 seeds, max matching distance {max(fe_dists):.2e}')
record('T3c  DRAFTED: spectrum is generally NOT closed under complex conjugation',
       max(conj_dists) > 1e-6,
       f'measured d(spec, conj spec) over 5 seeds: max {max(conj_dists):.2e} -- it IS closed')
record('T3d  CORRECTED: spec(T) IS closed under conjugation for any family E_i = Ad(B_i), '
       'because C(v) = v^dagger is an antiunitary commuting with every Ad(B)',
       max(conj_dists) < 1e-6)
record('T3e  DRAFTED: some Tr T^l is negative or non-real',
       (min(trace_min) < -1e-8) or (max(trace_imag) > 1e-8),
       f'over 5 seeds, l <= 8 (relative to |Tr T^l|): min Re/|.| = {min(trace_min):.6f}, '
       f'max |Im|/|.| = {max(trace_imag):.2e} (rounding noise)')
record('T3f  CORRECTED: Tr T^l = sum_w |Tr B_w|^2 >= 0 also for the inverse pairing '
       '(the trace formula never uses the adjoint pairing)',
       word_err < 1e-7 and min(trace_min) >= -1e-8,
       f'max rel. difference from the word sum over l <= 5 = {word_err:.2e}')

# where the drafted claim IS true: superoperators that are not of Ad type
rngg = np.random.default_rng(9)
Fs = [rngg.normal(size=(4, 4)) + 1j * rngg.normal(size=(4, 4)) for _ in range(2)]
Fs = Fs + [np.linalg.inv(F) for F in Fs]
Tg = hashimoto(Fs, [2, 3, 0, 1])
trg = np.array([np.trace(np.linalg.matrix_power(Tg, l)) for l in range(1, 7)])
print(f'  generic (non-Ad) inverse-paired superoperators, Tr T^l for l = 1..6:\n    '
      f'{np.array2string(trg, precision=3)}')
record('T3g  for superoperator families NOT of the form Ad(B), Tr T^l is indeed non-real / negative',
       (np.max(np.abs(trg.imag)) > 1e-6) or (np.min(trg.real) < -1e-6),
       f'max |Im| = {np.max(np.abs(trg.imag)):.3e}, min Re = {np.min(trg.real):.3e}')


# ==========================================================================================
head('T4.  Continuous case:  L(rho) = K rho + rho K^dag + sum_j R_j rho R_j^dag on M_n')


def lindblad(K, Rs):
    n = K.shape[0]
    I = np.eye(n)
    return np.kron(I, K) + np.kron(K.conj(), I) + sum(ad(R) for R in Rs)


def expK_factory(K):
    d, P = np.linalg.eig(K)
    Pinv = np.linalg.inv(P)

    def E(s):
        s = np.asarray(s, dtype=complex)
        return np.einsum('ab,...b,bc->...ac', P, np.exp(s[..., None] * d), Pinv)
    return E


def dyson_trace(K, Rs, t, kmax=3, nq=16):
    """sum_{k<=kmax} sum_{j} int_{0<t_1<..<t_k<t} |Tr(e^{(t-t_k)K} R_{j_k} .. R_{j_1} e^{t_1 K})|^2."""
    E = expK_factory(K)
    total = abs(np.trace(E(np.array(t)))) ** 2
    x, w = np.polynomial.legendre.leggauss(nq)
    u, wu = (x + 1) / 2, w / 2
    for k in range(1, kmax + 1):
        shp = lambda a: [nq if ax == a else 1 for ax in range(k)]
        us = [u.reshape(shp(a)) for a in range(k)]
        ws = wu.reshape(shp(0))
        for a in range(1, k):
            ws = ws * wu.reshape(shp(a))
        tl = [None] * k                      # tl[i] = t_{i+1}
        tl[k - 1] = t * us[0]
        for a in range(1, k):
            tl[k - 1 - a] = tl[k - a] * us[a]
        jac = t * np.ones_like(tl[0])
        for i in range(1, k):
            jac = jac * tl[i]
        gaps = [tl[0]] + [tl[i] - tl[i - 1] for i in range(1, k)] + [t - tl[k - 1]]
        Eg = [E(g) for g in gaps]
        for js in itertools.product(range(len(Rs)), repeat=k):
            M = Eg[0]
            for i in range(k):
                M = Eg[i + 1] @ (Rs[js[i]] @ M)
            tr = np.trace(M, axis1=-2, axis2=-1)
            total += float(np.sum(ws * jac * np.abs(tr) ** 2))
    return total


t4_dyson_ok, t4_pos_ok, t4_conj_ok, t4_equiv_ok, t4_thr_ok = True, True, True, True, True
for n in (2, 3):
    rng = np.random.default_rng(808 + n)
    K = 0.5 * cgauss(rng, n)
    Rs = [0.5 * cgauss(rng, n) for _ in range(2)]
    L = lindblad(K, Rs)
    print(f'  n = {n}: dim = {n*n}')

    # (i) positivity of Tr e^{tL} and the Dyson expansion at small t
    tg = np.arange(0.0, 5.0001, 0.1)
    trs = np.array([np.trace(expm(t * L)) for t in tg])
    relim = float(np.max(np.abs(trs.imag) / np.abs(trs)))
    pos = bool(np.min(trs.real) >= -1e-9 and relim < 1e-12)
    t4_pos_ok = t4_pos_ok and pos
    print(f'    Tr e^{{tL}} on t in [0,5] step 0.1: min = {np.min(trs.real):.6f}, '
          f'max |Im|/|Tr| = {relim:.2e}')
    derr = 0.0
    for t in (0.0025, 0.005, 0.01, 0.02):
        exact = np.trace(expm(t * L)).real
        dy = dyson_trace(K, Rs, t, kmax=3)
        if t <= 0.01:
            derr = max(derr, abs(exact - dy))
        print(f'    t = {t:<6}: Tr e^(tL) = {exact:.10f}, Dyson (k<=3) = {dy:.10f}, '
              f'diff = {abs(exact-dy):.2e}'
              + ('   (k=4 truncation, O(t^4); outside the 1e-6 gate)' if t > 0.01 else ''))
    t4_dyson_ok = t4_dyson_ok and derr < 1e-6

    # (ii) Weil/Bochner form
    rho = np.linalg.eigvals(L)
    i0 = int(np.argmax(rho.real))
    rho0 = rho[i0]
    nt, matchd = remove_nearest(rho, [rho0])
    a0 = rho0.real
    amax = float(np.max(nt.real))
    print(f'    leading eigenvalue rho_0 = {rho0:.6f} (|Im| = {abs(rho0.imag):.1e}), '
          f'a = Re rho_0 = {a0:.6f}; max Re over nontrivial modes = {amax:.6f}')

    def gram_psd(a, tj, tol=1e-9):
        s = np.subtract.outer(tj, tj)
        F = lambda x: np.sum(np.exp(np.multiply.outer(x, nt - a)), axis=-1)
        G = np.where(s >= 0, F(np.abs(s)), np.conj(F(np.abs(s))))
        return psd_report(G, tol)

    tj = np.arange(0.0, 20.0001, 0.25)            # the grid prescribed in the brief
    mn, mnr, psd = gram_psd(a0, tj)
    t4_equiv_ok = t4_equiv_ok and (psd == (amax <= a0 + 1e-12))
    print(f'    a = Re rho_0 = {a0:.6f}: min eig of the Gram matrix F(t_j - t_k) = {mn:.3e} -> PSD {psd}')
    bad = amax - 0.25
    mnb, _, psdb = gram_psd(bad, tj)
    t4_equiv_ok = t4_equiv_ok and (psdb == (amax <= bad + 1e-12))
    print(f'    a = {bad:.6f} (below max Re of the nontrivial modes = {amax:.6f}): '
          f'min eig = {mnb:.3e} -> PSD {psdb}')
    # the threshold in a sharpens as the time window grows (same finite-window masking as in T1c)
    thrs = []
    for Tmax in (20, 40, 80, 160):
        tjj = np.arange(0.0, Tmax + 1e-9, 0.25)
        lo, hi = amax - 0.3, amax + 0.3
        for _ in range(24):
            mid = 0.5 * (lo + hi)
            if gram_psd(mid, tjj)[2]:
                hi = mid
            else:
                lo = mid
        thrs.append(hi)
    print('    bisected threshold a* vs max Re(nontrivial rho) = '
          f'{amax:.8f}:  ' + ',  '.join(f'T={Tm}: {t:.6f} (gap {amax-t:.1e})'
                                        for Tm, t in zip((20, 40, 80, 160), thrs)))
    t4_thr_ok = t4_thr_ok and all(thrs[i] < thrs[i + 1] for i in range(3)) \
        and thrs[-1] <= amax + 1e-9 and abs(thrs[-1] - amax) < 5e-3

    dc = multiset_dist(rho, np.conj(rho))
    print(f'    d(spec L, conj spec L) = {dc:.2e}')
    t4_conj_ok = t4_conj_ok and dc < 1e-8

record('T4a  Tr e^{tL} >= 0 and real on a grid of t (continuous ring norms)', t4_pos_ok)
record('T4b  Dyson expansion (k <= 3, Gauss-Legendre on the simplex) matches Tr e^{tL} to 1e-6 for t <= 0.01',
       t4_dyson_ok)
record('T4c  Gram matrix of F(t) = e^{-at}(Tr e^{tL} - e^{t rho_0}) is PSD  <=>  max Re(rho) <= a',
       t4_equiv_ok)
record('T4d  bisected threshold in a increases with the time window up to max Re over the '
       'nontrivial spectrum (gap < 5e-3 at T = 160)', t4_thr_ok)
record('T4e  spec(L) closed under complex conjugation', t4_conj_ok)


# ==========================================================================================
head('T5.  Jordan-block blindness of the Weil form')
theta = 0.7
Xj = np.array([[np.exp(1j * theta), 1.0], [0.0, np.exp(1j * theta)]], complex)
Xd = np.diag([np.exp(1j * theta), np.exp(1j * theta)])
L5 = 40
nuJ = np.array([np.trace(np.linalg.matrix_power(Xj, l)) for l in range(L5 + 1)])
nuD = np.array([np.trace(np.linalg.matrix_power(Xd, l)) for l in range(L5 + 1)])
mnJ, _, psdJ = psd_report(weil_matrix(nuJ))
mnD, _, psdD = psd_report(weil_matrix(nuD))
sv = np.linalg.svd(Xj, compute_uv=False)
print(f'  X = [[e^(i theta), 1], [0, e^(i theta)]], theta = {theta}, r = 1, S = empty.')
print(f'    singular values of X: {np.array2string(sv, precision=6)}  (not unitary, not diagonalisable)')
print(f'    min eig of the Weil form, Jordan block: {mnJ:.3e};  diagonal matrix: {mnD:.3e}')
print(f'    max |nu_l(Jordan) - nu_l(diagonal)|, l <= {L5}: {np.max(np.abs(nuJ - nuD)):.2e}')
record('T5a  the Weil form of the Jordan block is PSD although X is not diagonalisable', psdJ,
       f'min eig {mnJ:.3e}')
record('T5b  Jordan block and the diagonal matrix with the same eigenvalues give identical nu',
       float(np.max(np.abs(nuJ - nuD))) < 1e-10)


# ==========================================================================================
head('SUMMARY')
npass = sum(1 for _, ok in RESULTS if ok)
for name, ok in RESULTS:
    print(f'  {"PASS" if ok else "FAIL"}  {name}')
print(f'\n{npass}/{len(RESULTS)} checks PASS.  '
      + ('ALL CHECKS PASS' if npass == len(RESULTS)
         else 'FAILURES: ' + '; '.join(name.split()[0] for name, ok in RESULTS if not ok)))
