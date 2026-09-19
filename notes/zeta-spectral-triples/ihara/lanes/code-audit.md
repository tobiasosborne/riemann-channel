# Code audit: `zst/` against a second vertical MVP for the Ihara zeta

Lane of `notes/zeta-spectral-triples/plan.md` §6.4 / `notes/zeta-spectral-triples/ihara/`. Read in
full: `zst/README.md`, `zst/include/zst.h`, `zst/src/*.c`, `zst/tests/*.c`, `zst/tools/zst.c`,
`zst/tools/mutate.py`, `zst/Makefile`, `notes/zeta-spectral-triples/plan.md` §3 and §6.4,
`docs/worklog/2026-09-17.md`, `docs/worklog/2026-09-18.md`. `notes/zeta-spectral-triples/ihara/
ihara_proto.py` does not exist yet at the time of this audit (checked; the `ihara/` directory holds
only `lanes/literature.md` and `lanes/notebook-extract.md`), so nothing here depends on it. Ground
truth for the graph side is already in this repo: `report/sections/02_definitions.tex:87-102`
(`def:ihara-bass`, `def:ramanujan-graph`) and `report/sections/08_quantum_ihara_general.tex:27-31`
(trivial-eigenvalue formula), both extracted with citations in `lanes/notebook-extract.md`. Nothing
under `zst/` or elsewhere in the repo was modified; this file and its directory are the only write.

Environment: FLINT 3.0.1 (`libflint-dev` 3.0.1-3.1build1, matches `zst/README.md`), gcc 13.3.0,
clang 18.1.3, antic bundled (`nf_elem.h`, `nf.h` present). All smoke programs below compiled with
`gcc -O2 -std=c11 -Wall -lflint -lmpfr -lgmp -lm` and ran in
`/tmp/claude-0/.../scratchpad/smoke/` (not committed; paths given are on that scratch tree and are
reproducible from the snippets pasted here).

## 1. Classification table

### Per file

| file | LOC | classification | for the graph path |
|---|---:|---|---|
| `src/riemann_ab.c` | 209 | zeta-specific | not reusable. Builds `(a_n,b_n)` from digamma/polygamma/Lerch sums of the archimedean gamma factor and the prime-power atoms. The Ihara case has **no archimedean kernel at all** (§2 below): the window data is `t_k = q^{-k/2}(\Tr B^k - \text{trivial}_k)` from exact integer traces, no special functions, no series tails to bound. A new, much smaller builder (`src/cycles.c` + `src/toeplitz_weil.c`) replaces it outright. |
| `src/blocks.c` | 62 | reusable with a variant | `zst_even_block`/`zst_odd_block` implement the **Loewner** form `tau_{nm}=(b_n-b_m)/(n-m)`, `tau_{nn}=a_n` (`blocks.c:1-6`, citing the paper's Lemma `basicexpli`). A genuine Toeplitz matrix `T_{jj'}=t_{j-j'}` is *not* of Loewner form (its entries are a function of `j-j'` directly, not a divided difference of a sequence `b`), so `loewner_pair` (`blocks.c:9-21`) does not apply. The even/odd block-diagonalization itself is identical mathematics (the flip `j -> -j` commutes with any Toeplitz matrix since `t_{-k}=t_k`, same as `tau` commuting with `gamma` at `blocks.c:4-5`), so the *structure* of the two functions (loop nests, `E`/`O` shapes `M+1` / `M`, the `sqrt2` row/column for `V_0`) carries over verbatim; only the entry formula changes from `loewner_pair` to a direct `t[|i-j|] ± t[i+j]` lookup, which is simpler code, not harder. New file `src/toeplitz_blocks.c`, same shape as `blocks.c`, roughly half the length (no divided-difference algebra). |
| `src/eigmin.c` | 356 | **generic, reusable as-is** | `zst_eigmin` (`zst.h:38-41`) takes an arbitrary real symmetric `arb_mat_t E` and returns its certified minimal eigenpair by inverse iteration + a hand-rolled Krawczyk/Rump verification (`eigmin.c:18-216`); nothing in the body refers to zeta, the window, or the Loewner structure. `zst_inertia_neg` (ball `LDL^T` inertia, `eigmin.c:218-252`) and `zst_certify_even_simple` (deflated-Cholesky positive-definiteness certificate on `E - s` and `O - s`, `eigmin.c:316-356`) are equally generic: they take `E`, `O`, `eps`, `v` as plain matrices/vectors with no reference to `riemann_ab.c` or `blocks.c`. All three link and run unchanged against a Toeplitz `E`/`O` pair. The only thing that is zeta-specific is the *comment* citing `Definition even-simple` of the CCM paper (`eigmin.c:1-13`); the Ihara analogue of "even-simple" (minimal eigenvalue of `T` is simple and even) needs its own citation to `def:ihara-bass`/Perron-Frobenius-on-the-window reasoning, not a code change. |
| `src/secular.c` | 401 | zeta-specific, not reusable, but the replacement is structurally analogous | `zst_secular_roots`/`zst_secular_verify` solve `g(s) = \sum_j \xi_j/(j-s) = 0`, a **pole-sum** secular function tied to the Fourier-Laplace duality of the CCM construction (`secular.c:1-25`). The Ihara analogue is not a pole sum: it is the **self-reciprocal polynomial** `z^M \hat\xi(z) = \sum_j \xi_j z^{j+M}`, and its roots on `|z|=\sqrt q` are wanted, not real poles. §3 below derives the correct real reduction (`\theta`-substitution / Chebyshev) and §4.5 gives the smoke-tested route. The *engineering lesson* of `secular.c` carries over even though the code does not: point-plus-tiny-interval Newton beats global ball isolation when the coefficients are highly amplified (`secular.c:20-25`, `README.md` "Design notes"); the graph case is milder (`\xi` is not amplified by 18-28 orders of magnitude the way the zeta window edge is, since there is no continuum tail to truncate), but the same interval-Newton machinery (`arb_calc_refine_root_newewton`, smoke-tested below) is the right tool. |
| `src/compare.c` | 17 | zeta-specific, not reusable | Calls `acb_dirichlet_zeta_zeros` (`compare.c:4-17`), meaningless for graphs. Replaced by a **stronger** truth oracle: the exact integer spectrum of `B` itself (§4.4, §4.6), which needs no external oracle and is certified by the same FLINT machinery, not looked up. |
| `tests/*.c` | 310 | pattern reusable, content not | The red-green style (closed-form 2x2/N=1 cases, an end-to-end pinned run, `arb_contains`/`mag_cmp_2exp_si` idioms) transfers directly; the actual pinned numbers are all zeta-specific and get replaced by K4/cube/Petersen closed forms (§5). |
| `tools/zst.c` | 128 | pattern reusable, content not | CLI shape (options, timing prints, `flint_printf`/`arb_printn` reporting) transfers; the pipeline calls change. |
| `tools/mutate.py` | 94 | **generic, reusable as-is** | Stdlib-only, operates on `src/*.c` by pattern, rebuilds with `make check` under ASan (`mutate.py:9-26,56-62`). Point it at the new `src/*.c` files (`--files` flag already exists, `mutate.py:53`) with zero changes to the script. |
| `Makefile` | 56 | **generic, reusable as-is (as a template)** | No zeta-specific content; copy to the new directory with `SRC`/`TESTS` globs unchanged. |

### Per function (the four named in the task)

- **`zst_eigmin`**: works for any real symmetric `arb_mat_t`; confirmed by reading (§ above) and by
  smoke-testing the identical Krawczyk/Rump pattern's building blocks (`arb_mat_approx_lu`,
  `arb_mat_approx_solve_lu_precomp`, `arb_mat_approx_inv`) against FLINT 3.0.1 — all present, used
  exactly as declared. No change needed to call it on a Toeplitz `E`.
- **`zst_certify_even_simple`**: needs `E` and `O` blocks, which the even/odd split of a Toeplitz
  matrix supplies as a "trivial basis change" *in the same sense* as the zeta case — trivial as
  *structure* (both are the `\mathbb Z/2` quotient by `j \to -j`, `blocks.c:4-5` vs. the Toeplitz
  symmetry `t_{-k}=t_k`), not trivial as *code*, because the entry formula differs (Loewner vs.
  direct Toeplitz lookup, per the `blocks.c` row above). Once `toeplitz_blocks.c` produces `E`/`O`
  in the same `arb_mat_t` layout, `zst_certify_even_simple` is called unmodified.
- **`zst_secular_roots` / `zst_secular_verify`**: specific to `\sum \xi_j/(j-s)`; the Ihara
  replacement is root-finding for the self-reciprocal polynomial `z^M\hat\xi(z)` on `|z|=\sqrt q`,
  detailed in §3-4.5 (a new module, `src/circle_roots.c`, not a reuse of `secular.c`'s code, though
  it reuses the *interval-Newton-after-cheap-candidate-generation* strategy).
- **`zst_riemann_ab` and `blocks.c`**: zeta-specific, confirmed above (`riemann_ab.c` not reusable
  at all; `blocks.c` reusable only as a structural template).
- **`compare.c`**: zeta-specific, confirmed above; replaced by an internal certified-truth oracle,
  not an external lookup.

## 2. FLINT 3.0.1 API check

All programs below are pasted in full or in their load-bearing part; every one was compiled and run
in this session. Full sources are under the scratch smoke directory as `smoke1_fmpz.c` through
`smoke5_timing.c`.

### 2.1 `fmpz_mat`: build `B`, powers, traces, charpoly

K4's Hashimoto operator (12 = 2|E| directed arcs, non-backtracking condition `to[i]==from[j] &&
to[j]!=from[i]`):

```c
fmpz_mat_t B; fmpz_mat_init(B, narcs, narcs);
for (i = 0; i < narcs; i++)
    for (j = 0; j < narcs; j++)
    {
        int ok = (to[i] == from[j]) && (to[j] != from[i]);
        fmpz_set_ui(fmpz_mat_entry(B, i, j), ok ? 1 : 0);
    }
fmpz_t tr; fmpz_init(tr);
fmpz_mat_trace(tr, B);                       /* Tr B^1 */
fmpz_mat_t Bk; fmpz_mat_init(Bk, narcs, narcs);
fmpz_mat_pow(Bk, B, k); fmpz_mat_trace(tr, Bk);   /* Tr B^k, k=2..6 */
fmpz_poly_t cp; fmpz_poly_init(cp);
fmpz_mat_charpoly(cp, B);
```

Output:

```
Tr B^1 = 0
Tr B^2 = 0
Tr B^3 = 24
Tr B^4 = 24
Tr B^5 = 0
Tr B^6 = 96
charpoly(B) degree = 12
charpoly(B) = u^12-8*u^9-6*u^8+16*u^6+24*u^5-3*u^4-16*u^3-24*u^2+16
```

`Tr B^3 = 24` matches by hand: K4 has 4 triangles, 2 orientations, 3 rotations each = 24 non-
backtracking closed 3-walks. `fmpz_mat_mul`, `fmpz_mat_pow`, `fmpz_mat_trace`,
`fmpz_mat_charpoly` all present and correct in FLINT 3.0.1 (need `#include <flint/fmpz.h>`
explicitly for `fmpz_set_ui`/`fmpz_print`/`fmpz_init` — omitting it compiles with implicit-
declaration warnings but still links, because `fmpz_mat.h` pulls in enough of the ABI; do not rely
on that, include `flint/fmpz.h`). `fmpz_mat_charpoly` dispatches to
`fmpz_mat_charpoly_modular` by default (`fmpz_mat.h:351-365` in the installed header): CRT-based,
not the naive `O(n^4)` Berkowitz method, so it scales to the graph sizes this MVP needs (confirmed
at `n=24` below, sub-millisecond).

For **all** powers `k=1..M` (needed for the atom data, not just one `k`), use repeated
`fmpz_mat_mul(Bk, Bk, B)` from a running product, not `M` separate `fmpz_mat_pow` calls (each of
which recomputes from scratch); `O(M)` matrix multiplications of `O(n^{2.x})` each, confirmed
sub-millisecond at `n=24` for `M=8` in §2.6.

### 2.2 `arb_mat_cho` / `arb_mat_ldl` / `arb_mat_spd_solve`

```c
arb_mat_t A; /* [[4,1,0],[1,3,1],[0,1,2]], SPD */
arb_mat_cho(L, A, prec);          /* -> certified */
arb_mat_ldl(L, A, prec);          /* -> certified */
arb_mat_spd_solve(X, A, B, prec); /* -> certified, x = (0.2222..., 0.1111..., 1.4444...) */
```
All three present, ran, certified on the first try at `prec=200`. These are exactly the primitives
`zst_eigmin`'s `verify_pd` (`eigmin.c:260-314`) hand-rolls via an approximate Cholesky plus a ball
residual bound rather than calling `arb_mat_cho` directly — worth reconsidering for the Ihara port:
`arb_mat_spd_solve` is a public, presumably better-tested equivalent of the same Rump-style
certificate (`spd_solve` almost certainly calls into the same `cho`/residual pattern internally).
Using the library routine instead of `verify_pd`'s hand-rolled version is a candidate simplification
for **both** verticals, out of scope for this audit but worth a follow-up ticket.

### 2.3 `acb_mat_eig_simple_rump` / `acb_mat_eig_multiple_rump`

First attempt at `n=4` (K4 adjacency, eigenvalues `3, -1, -1, -1`) with a tight tolerance and
reduced-precision QR **failed** both simple and multiple:

```c
mag_set_ui_2exp_si(tol, 1, -30);
acb_mat_approx_eig_qr(Eapprox, NULL, Rapprox, A, tol, 0, 64);   /* prec=64, not matching cert. prec=200 */
acb_mat_eig_multiple_rump(E, A, Eapprox, Rapprox, 200);         /* -> 0, FAILED */
```

Fixed by mirroring FLINT's own test (`src/acb_mat/test/t-eig_multiple.c` upstream, fetched and read
for this audit): pass `tol=NULL` to `acb_mat_approx_eig_qr` and run the approximate QR at the
**same** precision as the certification, not a cheap reduced one:

```c
acb_mat_approx_eig_qr(Eapprox, NULL, Rapprox, A, NULL, 0, prec);   /* prec matches the cert. call */
int ok_simple = acb_mat_eig_simple_rump(E, NULL, NULL, A, Eapprox, Rapprox, prec);
/* -> 0, correctly refuses (K4 adjacency has eigenvalue -1 with multiplicity 3) */
int ok_mult = acb_mat_eig_multiple_rump(E, A, Eapprox, Rapprox, prec);
/* -> 1, certified: eig[0]=3, eig[1..3]=-1 (all radius ~3e-19 at prec=200) */
```

So: `eig_simple_rump` correctly and reliably refuses multiplicity (confirming the task's Petersen
worry generalizes — any graph with a symmetric automorphism group, which is most of the small test
cases, will have repeated adjacency/Hashimoto eigenvalues and defeat `eig_simple_rump`).
`eig_multiple_rump` is the right call, **but it is not robust to under-precision inputs** — it needs
the approximate eigendata computed at (at least) the certification precision, not a cheap pre-pass.
At `n=24` (hypercube `Q_3`'s Hashimoto operator, §2.6) it **failed even with matching `prec=200`**
in a single attempt; FLINT's own test harness handles this by doubling `prec` in a retry loop
(`for (prec = 32; ; prec *= 2) { ...eig_multiple_rump...; if (result) break; }`,
`t-eig_multiple.c` upstream). Recommendation for the Ihara port: treat `eig_multiple_rump` as a
**secondary cross-check with a doubling-precision retry**, not the primary truth route — §2.4 gives
a route that was faster and unconditionally reliable at the same size.

### 2.4 Certified roots of an exact integer polynomial: a real trap

`arb_fmpz_poly_complex_roots`, the function that looks purpose-built for "certified spectrum of an
exact integer matrix via its charpoly", **does not terminate on K4's charpoly** (which has a genuine
multiplicity-3 root, `(-1\pm i\sqrt7)/2`, magnitude `\sqrt2`) — confirmed by running it to a 20s
timeout and independently by reading the FLINT 3.0.1 source
(`src/arb_fmpz_poly/complex_roots.c`, fetched for this audit):

```c
for (prec = initial_prec; ; prec *= 2)          /* UNBOUNDED */
{
    ...
    isolated = acb_poly_find_roots(roots_deflated, cpoly_deflated, ..., prec);
    if (isolated == deg_deflated) { ...; break; }
}
```

The loop only exits when `acb_poly_find_roots` returns `deg_deflated` **pairwise-disjoint** balls
(`check_isolation`, same file). Two balls around a genuinely repeated root can never be made
disjoint at any finite precision — the loop runs forever (or until `prec` overflows/OOMs). The
function's own "deflation" only strips a `poly(x^d)` structure (`arb_fmpz_poly_deflation`), not
root multiplicity; it explicitly assumes the input is squarefree (comment `complex_roots.c`:
"by assumption that poly is squarefree, must be just one").

**Fix**, smoke-tested and instantaneous (`< 30s` wall including compile; the run itself is
sub-millisecond at `n=12` and `n=24`, §2.6):

```c
fmpz_poly_factor_t fac; fmpz_poly_factor_init(fac);
fmpz_poly_factor_squarefree(fac, cp);           /* exact, over Z */
for (i = 0; i < fac->num; i++)
{
    slong deg = fmpz_poly_degree(fac->p + i), mult = fac->exp[i];
    acb_ptr roots = _acb_vec_init(deg);
    arb_fmpz_poly_complex_roots(roots, fac->p + i, 0, prec);   /* each factor is now squarefree */
    ...
}
```

Output on K4 (matches the hand-derived spectrum from `def:ihara-bass`, §3):

```
fmpz_poly_factor_squarefree: 3 squarefree factors (c = 1)
  factor 0: degree 1, multiplicity 1 -- roots: (+2.00000+0.00000i, |.|=2.00000)
  factor 1: degree 1, multiplicity 2 -- roots: (-1.00000+0.00000i, |.|=1.00000)
  factor 2: degree 3, multiplicity 3 -- roots: (+1.00000...) (-0.50000+1.32288i, |.|=1.41421) (-0.50000-1.32288i, |.|=1.41421)
```

This is exactly Ihara-Bass (`report/sections/02_definitions.tex:87-94`): trivial eigenvalues
`q=2` (mult 1, from `\lambda=q+1=3`) and `1` (mult 1 from the same pair, joined by
`(|E|-|V|)=2` more copies from the `(1-u^2)^{|E|-|V|}` factor, total mult 3), `-1` (mult
`|E|-|V|=2`), and the nontrivial pair `\mu^2+\mu+2=0` (from `\lambda=-1`, mult 3, Ramanujan
magnitude `\sqrt2` exactly). **Correction to the task prompt's worked example**: K4 is 3-regular,
so `q=2`, not `3`; the correct closed form is `\mu^2+\mu+2=0` (roots `(-1\pm i\sqrt7)/2`), not
`\mu^2+\mu+3=0`. Verified two independent ways (direct Hashimoto-matrix construction +
squarefree-factored charpoly, and the general formula `\mu^2-\lambda\mu+q=0` at
`report/sections/02_definitions.tex:87-94` with `\lambda=-1,q=2`); both agree to the displayed
digits.

**Recommendation for the truth oracle (§4.4/4.6)**: `fmpz_mat_charpoly` ->
`fmpz_poly_factor_squarefree` -> `arb_fmpz_poly_complex_roots` per factor is the primary route
(exact input, fast, terminates unconditionally, multiplicities come free from the factorization
exponents). `acb_mat_eig_multiple_rump` is a secondary cross-check, needed only because it also
returns certified eigen*vectors* (useful for comparing to `\xi`'s own eigenvector, not just its
eigenvalues), with the doubling-precision retry noted in §2.3.

### 2.5 Root isolation on the unit circle: the `\theta`-substitution works cleanly

`z^M\hat\xi(z)` at `z=e^{i\theta}` factors (using `\xi_{-j}=\xi_j`) as
`e^{iM\theta} R(\theta)`, `R(\theta) = \xi_0 + 2\sum_{j=1}^M \xi_j\cos(j\theta)`, a genuine
real-valued function of a real variable — none of the "difference of huge terms" problem that forced
`secular.c` away from `arb_calc_isolate_roots` in the zeta case (`secular.c:20-25`,
`docs/worklog/2026-09-17.md` bug (2)). Smoke-tested end to end with `M=1`, `\xi_0=\xi_1=1`
(`R(\theta)=1+2\cos\theta`, roots at `2\pi/3, 4\pi/3` exactly):

```c
static int R_func(arb_ptr out, const arb_t theta, void *param, slong order, slong prec)
{ /* out[0] = xi_0 + 2 sum_j xi_j cos(j theta); out[1] = derivative if order > 1 */ }
...
slong n = arb_calc_isolate_roots(&blocks, &flags, R_func, &P, block, 30, 10000, 100, prec);
/* n = 2 candidate blocks */
arb_calc_newton_conv_factor(conv_factor, R_func, &P, conv_region, prec);
arb_calc_refine_root_newton(r, R_func, &P, start, conv_region, conv_factor, 20, prec);
```
Output: both roots certified, `2.0943951023931954923 +/- 8.43e-21` and
`4.1887902047863909846 +/- 1.69e-20` against exact `2\pi/3 = 2.0943951023931953...`. `arb_calc_
isolate_roots`, `arb_calc_newton_conv_factor`, `arb_calc_refine_root_newton` all present, correct,
fast.

**Alternative (Chebyshev, no trigonometric evaluation at all)**: substitute `x=\cos\theta`; since
`\cos(j\theta)=T_j(x)` (Chebyshev), `R` becomes an ordinary real polynomial `P(x) = \xi_0 +
2\sum_j \xi_j T_j(x)` of degree `M` in `x`, and root-finding on `[-1,1]` reduces to real polynomial
root isolation (`arb_fmpz_poly`/`arb_poly` machinery, or the same `arb_calc` route with a polynomial
`R_func`). This avoids `M` `arb_cos`/`arb_sin` evaluations per candidate; worth doing if `M` is
large (§6 performance), not needed for the MVP sizes.

Recommended primary route for `src/circle_roots.c`: the `\theta`-form (§2.5) directly, with the
Chebyshev reduction as a documented but initially-unimplemented speed-up (mirrors `zst`'s own
"structured `O(N^2)` solvers later" deferral, `plan.md:328-331`).

### 2.6 Timing at a slightly larger size (`Q_3`, hypercube, `n=2|E|=24`)

```
Q3: n = 2|E| = 24
  Tr B^1..8 by repeated fmpz_mat_mul: 0.000s
  fmpz_mat_charpoly: 0.000s (degree 24)
  fmpz_poly_factor_squarefree: 0.000s, 3 factors (degrees 2, 4, 5; mults 1, 3, 5)
  squarefree-then-complex_roots route: 0.000s total, 8 roots
  acb_mat_eig_multiple_rump route: 0.081s, certified=0   <-- FAILED at prec=200 in one shot
```
Confirms §2.3's warning (`eig_multiple_rump` needs a retry loop even at matching `prec`) and §2.4's
recommendation (the squarefree-charpoly route was faster **and** unconditionally correct at this
size). Sizes relevant to the MVP's test plan (K4: 12, cube `Q_3`: 24, Petersen: 30, `K_{3,3}`: 18,
small LPS graphs: a few hundred) are all comfortably inside the sub-second regime for the exact
route; `acb_mat_eig_multiple_rump`'s reliability at those sizes needs its own small study before it
is trusted as more than a cross-check (flagged as a risk, §7).

### 2.7 Exact arithmetic over `Q(\sqrt q)`: is it needed?

FLINT 3's antic module is present (`nf_elem.h`, `nf.h`, `nf_init(nf_t nf, const fmpq_poly_t pol)`),
so `Q(\sqrt q)` is directly constructible (`pol = x^2 - q`) and `nf_elem_t` arithmetic is exact. But
§3 shows the pipeline does not need it: the only places an irrational `q^{k/2}` appears are (a) the
atom values `t_k` themselves, which must end up as `arb_t` balls anyway to feed the same
`arb_mat_t`-based `zst_eigmin`/`zst_certify_even_simple` used for zeta (`nf_elem` would have to be
converted to `arb_t` at that boundary regardless, so introducing it buys nothing there), and (b) the
diagonal rescaling `D=\mathrm{diag}(q^{j/2})`, addressed precisely in §3: the *symmetric congruence*
`D\,T\,D` is an **exact integer** matrix (no `Q(\sqrt q)` needed at all, not even as an intermediate),
while the *similarity* `D\,T\,D^{-1}` (which would need irrational entries, whether typed as `arb_t`
or `nf_elem_t`) is not symmetric and gains nothing. **Conclusion: no `nf_elem`/antic dependency is
needed for the Ihara MVP.** `q^{-k/2}` is computed once per `k` as an `arb_t` ball
(`arb_sqrt_ui`/`arb_pow`), exactly as `zst_riemann_ab` already does for other constants
(`riemann_ab.c:96-116`); it is the trivial route and there is no exactness to be gained by avoiding
it for the `t_k` themselves. `nf_elem` remains available as a later option if a fully rational
inertia-only pipeline (§3, last paragraph) is worth building as a genuine alternative to ball
arithmetic for the definiteness certificates specifically — a real possibility, flagged as an
opportunity in §6, not a requirement.

## 3. The `D T D` question, worked out precisely

Index the window `0..2M` (shift `j \to j+M` from the natural `-M..M` labeling; this is just a
choice of coordinates, not a mathematical restriction). `T_{jj'} = t_{|j-j'|}`, `t_k = q^{-k/2}
c_k`, `c_k := \Tr B^k - q^k - 1 - (|E|-|V|)(1+(-1)^k)` **exact integer** for `k\ge0`
(`c_k = \sum_{\mu\ \mathrm{nontrivial}} \mu^k`, from `report/sections/08_quantum_ihara_general.tex:
27-31`; `c_0 = 2|E|-2 - 2(|E|-|V|) - (\text{fix at }k=0)`, handled as a special case like the
zeta code's `b_0` — see the fuzzing lesson in `zst/README.md` "First catch", same failure mode is
worth testing for here too).

Let `D = \mathrm{diag}(d_0,\dots,d_{2M})`, `d_j = q^{j/2}`.

**Congruence `D\,T\,D`** (not a similarity — does *not* preserve `T`'s eigenvalues):
```
(DTD)_{jj'} = d_j T_{jj'} d_{j'} = q^{(j+j')/2} q^{-|j-j'|/2} c_{|j-j'|}
            = q^{(j+j'-|j-j'|)/2} c_{|j-j'|} = q^{\min(j,j')} c_{|j-j'|}.
```
Using `(a+b-|a-b|)/2=\min(a,b)`. Since `j,j'\in\{0,\dots,2M\}`, `\min(j,j')\ge0`, so this is an
**exact non-negative integer** for every entry — despite `D` itself having irrational entries
(`q^{1/2}` for odd `j`). Verified by hand on the `2\times2` corner (`j=0,j'=1`:
`d_0 T_{01} d_1 = 1\cdot q^{-1/2}c_1\cdot q^{1/2} = c_1`, integer, matches `\min(0,1)=0`,
`q^0 c_1=c_1`). By Sylvester's law of inertia, `D\,T\,D` has the **same number of positive,
negative and zero eigenvalues** as `T` (congruence preserves inertia, not eigenvalues), which is
*exactly* what `zst_inertia_neg`/`zst_certify_even_simple`'s deflated-Cholesky certificate need —
they only ever ask for signs, never for eigenvalues themselves.

**Similarity `D\,T\,D^{-1}`** (preserves eigenvalues, is the "obvious" fix, and does not help):
```
(DTD^{-1})_{jj'} = q^{(j-j')/2} q^{-|j-j'|/2} c_{|j-j'|}
                 = c_{j-j'}                       (j \ge j')
                 = q^{-(j'-j)} c_{j'-j}            (j < j').
```
Not symmetric (upper triangle integer, lower triangle a negative power of `q` — genuinely
irrational unless `q` is a perfect square), and still needs ball/irrational arithmetic below the
diagonal. No exactness gain, and the loss of symmetry is a real cost (breaks the `arb_mat_cho`/`ldl`
family, which assume symmetric input). **Do not use this transform.**

**What this buys, precisely.** For a *fixed rational shift* `s\in\mathbb Q` (e.g. a bisection point
when hunting for the minimal eigenvalue, or `s=0` to test whether `T` itself is positive definite):
```
D(T - sI)D = DTD - s D^2,   (D^2)_{jj} = q^j  (exact integer, since j \ge 0 in shifted coordinates)
```
is an **exact rational matrix** whenever `s\in\mathbb Q`. Its inertia (via exact-rational `LDL^T`,
`fmpq_mat`, fraction-free if wanted) certifies the inertia of `T-sI` with **zero precision loss and
zero ball-radius bookkeeping** — a strictly stronger and simpler certificate than `zst_inertia_neg`'s
ball `LDL^T` (`eigmin.c:218-252`) for any rational-shift bisection scheme. This does *not* replace
`zst_eigmin` itself (the minimal eigenvalue `\eps` of `T` is generically irrational, so the
eigen*vector*/eigen*value* computation still needs `arb_mat`/ball arithmetic exactly as in the zeta
port), but it is a genuine, sound simplification for the *inertia-counting* half of the pipeline
(root bisection to localize `\eps`, and the definiteness half of `zst_certify_even_simple`'s
Ihara analogue *if* the deflation shift `s` is chosen rational, which is free to do — `s` only needs
to be an upper bound on `2\eps`, and any rational number above the certified ball's upper bound
works). Flagged as a genuine opportunity for the Ihara port, not required for the MVP: start with
the direct `arb_mat` port of `eigmin.c` unchanged (§1), add the exact-rational inertia fast path as
a follow-up once the MVP's tests are green (mirrors `zst`'s own M3/M4 staging in `plan.md:353-378`).

## 4. Proposed module layout and public API

New sibling directory `ihz/` (mirrors `zst/`'s layout exactly: `include/`, `src/`, `tools/`,
`tests/`, `fuzz/`, `Makefile`, `README.md`), not a subdirectory of `zst/` (the task's own framing —
"second vertical MVP" — and the instruction not to touch `zst/` both point the same way). The three
generic files (`eigmin.c` and its declarations) are **duplicated**, not shared, for this MVP,
matching the project's own tracer-bullet ethos (`zst/README.md`'s M3 note: derive rather than share
prematurely); a shared `libzcore` extraction is a fine M2-for-`ihz` follow-up once both verticals are
stable, not a precondition.

```
ihz/
  include/ihz.h
  src/
    graph_io.c        edge-list parser; builders for K_n, Q_d (hypercube), Petersen, C_n, K_{m,n}
    hashimoto.c        graph (adjacency list) -> fmpz_mat_t B (Hashimoto operator), regularity check
    cycles.c           Tr B^k, k=1..M, by repeated fmpz_mat_mul; exact integer c_k (trivial-divisor
                       subtraction per report/sections/08_quantum_ihara_general.tex:27-31)
    toeplitz_weil.c    c_k -> t_k (arb_t balls, q^{-k/2} c_k) -> ihz_weil_discrete_t; ground truth
                       report/sections/02_definitions.tex:87-102, :27-31 above
    toeplitz_blocks.c  t_k -> even/odd Toeplitz blocks E (M+1 x M+1), O (M x M)      [variant of
                       zst/src/blocks.c, §1]
    eigmin.c           = zst/src/eigmin.c, copied verbatim (zst_eigmin, zst_inertia_neg,
                       zst_certify_even_simple), renamed ihz_ prefix only               [reuse, §1]
    circle_roots.c     xi -> R(theta) = xi_0 + 2 sum xi_j cos(j theta); arb_calc_isolate_roots +
                       arb_calc_refine_root_newton; theta -> mu = sqrt(q) e^{i theta}   [new, §2.5]
    truth.c            B -> certified exact spectrum: fmpz_mat_charpoly, fmpz_poly_factor_squarefree,
                       arb_fmpz_poly_complex_roots per factor (primary); acb_mat_eig_multiple_rump
                       as a cross-check with doubling-precision retry (secondary)       [new, §2.4]
    compare.c          certified |mu_k - truth_k| against truth.c, and theta vs Hashimoto angle
                       arg(mu)                                                          [new, §1]
  tools/ihz.c          CLI driver, mirrors tools/zst.c
  tools/mutate.py      = zst/tools/mutate.py, --files pointed at ihz/src/*.c              [reuse, §1]
  tests/               test_hashimoto, test_cycles, test_toeplitz, test_eigmin (ported unit tests +
                       a K4/cube closed-form case), test_circle_roots, test_truth, test_pipeline
  fuzz/                fuzz_cycles.c (random small regular-ish graphs; invariants below),
                       fuzz_circle_roots.c (arbitrary normalised xi; same invariant shape as
                       zst/fuzz/fuzz_secular.c)
```

### Public API (`include/ihz.h`), C prototypes

```c
/* graph_io.c */
typedef struct { slong nv; slong *deg; slong ne; slong *u, *v; } ihz_graph_t;  /* undirected edge list */
int  ihz_graph_read(ihz_graph_t *G, const char *path);           /* text format: "nv ne" then ne "u v" lines */
void ihz_graph_complete(ihz_graph_t *G, slong n);                 /* K_n */
void ihz_graph_hypercube(ihz_graph_t *G, slong d);                 /* Q_d */
void ihz_graph_petersen(ihz_graph_t *G);
void ihz_graph_complete_bipartite(ihz_graph_t *G, slong m, slong n);
void ihz_graph_cycle(ihz_graph_t *G, slong n);                     /* C_n: q=1, degenerate, see test plan */
int  ihz_graph_is_regular(const ihz_graph_t *G, slong *q_plus_1);  /* 0 if not (q+1)-regular */
void ihz_graph_clear(ihz_graph_t *G);

/* hashimoto.c */
void ihz_hashimoto(fmpz_mat_t B, const ihz_graph_t *G);  /* B: 2|E| x 2|E|, non-backtracking 0/1 */

/* cycles.c */
/* c[k], k=0..M: Tr B^k minus the trivial-divisor terms of report/sections/
 * 08_quantum_ihara_general.tex:27-31 (q^k + 1 + (|E|-|V|)(1+(-1)^k)), exact fmpz. */
void ihz_cycle_counts(fmpz *c, const fmpz_mat_t B, slong nv, slong ne, slong q, slong M);

/* toeplitz_weil.c */
typedef struct {
    slong M, q; slong nv, ne;
    arb_ptr t;                 /* t[0..M], t_k = q^{-k/2} c_k, ball */
} ihz_weil_discrete_t;
void ihz_weil_from_graph(ihz_weil_discrete_t *W, const ihz_graph_t *G, slong M, slong prec);
void ihz_weil_clear(ihz_weil_discrete_t *W);

/* toeplitz_blocks.c */
void ihz_even_block(arb_mat_t E, arb_srcptr t, slong M, slong prec);   /* (M+1) x (M+1) */
void ihz_odd_block(arb_mat_t O, arb_srcptr t, slong M, slong prec);    /* M x M */

/* eigmin.c -- signatures identical to zst_eigmin / zst_inertia_neg / zst_certify_even_simple,
 * renamed only; see zst/include/zst.h:41,45,53 for the exact contract this ports verbatim. */
int   ihz_eigmin(arb_t eps, arb_ptr v, const arb_mat_t E, slong iters, slong prec);
slong ihz_inertia_neg(const arb_mat_t A, const arb_t shift, slong prec);
int   ihz_certify_even_simple(const arb_mat_t E, const arb_mat_t O, const arb_t eps, arb_srcptr v, slong prec);

/* circle_roots.c */
/* Certified roots of R(theta) = xi_0 + 2 sum_{j=1}^M xi_j cos(j theta) on [0, 2pi); returns the
 * count found (<= maxroots), writes theta balls increasing, disjoint. mu = sqrt(q) e^{i theta}. */
slong ihz_circle_roots(arb_ptr thetas, slong maxroots, slong *unresolved,
                       arb_srcptr xi, slong M, slong prec);
int   ihz_circle_root_verify(arb_t theta, arb_srcptr xi, slong M, const arb_t theta_approx, slong prec);

/* truth.c: certified exact spectrum of B, with multiplicities, from the squarefree-factored
 * charpoly (primary route, §2.4); acb_mat_eig_multiple_rump cross-check optional via flag. */
typedef struct { acb_ptr mu; slong *mult; slong n; } ihz_truth_spectrum_t;
int  ihz_truth_spectrum(ihz_truth_spectrum_t *S, const fmpz_mat_t B, slong prec);
void ihz_truth_clear(ihz_truth_spectrum_t *S);

/* compare.c */
/* |theta_k*sqrt(q) - nontrivial Hashimoto angle_k| certified, matched by nearest-neighbour after
 * sorting both by angle; also checks root count == M and all |mu| = sqrt(q) to within radius. */
void ihz_compare(arb_ptr err, arb_srcptr thetas, slong nroots,
                 const ihz_truth_spectrum_t *S, slong q, slong prec);
```

## 5. Test plan

**Pinned closed-form cases** (all cross-checked by hand above or trivially so):
- `K_4`: `q=2`, adjacency `3,-1,-1,-1`; nontrivial Hashimoto roots of `\mu^2+\mu+2=0` (note: the
  task prompt's `\mu^2+\mu+3=0` is off by the value of `q`; §2.4 has the corrected derivation
  two independent ways). `n=12`.
- `Q_3` (cube): `q=2`, adjacency spectrum `3,1,1,1,-1,-1,-1,-3`; squarefree factor degrees/mults
  `2/1, 4/3, 5/?` measured in §2.6 (pin the exact factorization once `ihz_hashimoto` exists; used
  here only as a scale/timing check, re-derive the closed form for the actual test).
- `K_{3,3}`: bipartite, `q=2`; bipartite graphs have `\mathrm{spec}(A)` symmetric under negation, so
  the Ihara zeta has extra structure (`\mu \to -\mu` symmetry) worth a dedicated invariant.
- `C_n` (cycle): **degenerate case**, `q=1` — the Ramanujan bound `2\sqrt q=2` coincides with the
  regularity degree `q+1=2`, so *every* eigenvalue is "trivial" by the `|\lambda|\le2\sqrt q` test;
  Ihara zeta of a cycle is elementary (`\zeta_{C_n}(u)^{-1}=(1-u^2)(1-u^n)^2`-type closed form) and
  should be pinned as a boundary/degenerate regression, not a generic case — flag in the test file
  that `q=1` is out of scope for the "nontrivial roots on `|z|=\sqrt q`" story and is included only
  to make sure the code does not crash or silently mis-certify.
- Petersen: `q=2`, adjacency `3, 1^5, -2^4` (well-known spectrum, multiplicities 1,5,4) — the
  task's motivating example for `eig_simple` failing; exercises `ihz_truth_spectrum`'s squarefree
  route at real multiplicity depth (`5`, deeper than K4's `3`) and is the first real stress test of
  §2.3's finding that `eig_multiple_rump` is not a reliable primary route.

**Integration test**: exact recovery at the critical window `M \ge` (graph diameter, or a small
multiple — determine empirically, mirroring `zst`'s own `N \sim 10\lambda^2` rule of thumb,
`plan.md:314-316`): `ihz_circle_roots` returns exactly `M` certified roots, matched 1-1 by
`ihz_compare` to the `M` nontrivial Hashimoto angles nearest the window (by the analogue of
`zst`'s `s < N/2` "meaningful roots" rule, `plan.md:314`), to a tolerance tightening with `M`.

**Under-resolved regime**: numbers pinned from `notes/zeta-spectral-triples/ihara/ihara_proto.py`
once it exists (task says "being written in parallel... do not wait" — correctly not waited for
here; this row of the test plan is a placeholder to fill in when that file lands, not a blocker for
anything else in this audit).

**Fuzz targets** (mirroring `zst/fuzz/fuzz_secular.c`'s invariant-based style, `README.md` "3.
Fuzzing"):
- `fuzz_cycles.c`: random graphs from a configuration-model pairing (fixed degree sequence, `q+1`
  regular, reject multi-edges/self-loops or explicitly allow and test the multigraph case
  separately since `zst`'s own house style values catching edge-format bugs young); invariants:
  `c_0` exactly the expected constant (mirrors the `zst` `b_0` fuzz catch, `README.md` "First
  catch"), `\Tr B^k \ge 0` is *not* an invariant (can be negative), but `\Tr B^{2k} \ge` the count
  of length-`2k` trivial closed walks is; Ihara-Bass identity `\det(1-uB) \overset{?}{=}
  (1-u^2)^{|E|-|V|}\det(1-uA+qu^2I)` checked exactly over `fmpz`/`fmpq_poly` for small random `u`
  substitutions or as a full polynomial identity (`fmpz_poly_equal` after expanding the RHS) — this
  is the single strongest correctness invariant available and should be a **unit test**, not just a
  fuzz invariant (it is a closed-form exact-arithmetic check, no reason to leave it to chance).
- `fuzz_circle_roots.c`: arbitrary normalised `\xi` (not necessarily from a real graph), same
  invariant shape as `fuzz_secular.c` (`README.md`): every returned root is a certified zero of `R`,
  roots increasing and pairwise disjoint on `[0,2\pi)`, count `\le M`.
- Even/odd eigenvector invariant: for a random SPD-ish random Toeplitz `T` (not necessarily from a
  graph), the minimal eigenvector returned by `ihz_eigmin` on the even block, mapped back to the
  full `2M+1` vector, is genuinely even (`v_j = v_{-j}`) to the certified radius — a basic sanity
  invariant the zeta code gets for free from `blocks.c`'s construction and this MVP should test
  explicitly since `toeplitz_blocks.c` is new code.

**Mutation**: `tools/mutate.py --files ihz/src/hashimoto.c,ihz/src/cycles.c,ihz/src/toeplitz_weil.c,
ihz/src/toeplitz_blocks.c,ihz/src/circle_roots.c,ihz/src/truth.c,ihz/src/compare.c` (excludes
`eigmin.c`, whose mutation coverage was already established for the zeta port and is unchanged
code — re-running it is redundant, not wrong, and cheap enough to include anyway for defense in
depth given it is a straight copy that could pick up copy-paste errors).

## 6. Risks and effort estimate

| module | new LOC (rough, vs. `zst` analogue) | days | new vs. ported |
|---|---:|---:|---|
| `graph_io.c` (parser + 4 family builders) | ~180 | 1.5 | new |
| `hashimoto.c` | ~60 | 0.5 | new, trivial (confirmed by smoke1/smoke5) |
| `cycles.c` (traces + trivial-divisor subtraction) | ~80 | 1 | new; the `c_0` special case is the one place a `zst`-style off-by-one/sign bug is likely (mirrors the `b_0` fuzz catch) |
| `toeplitz_weil.c` | ~60 | 0.5 | new, but simple (`arb_pow`/`arb_sqrt_ui` on integers, no series, no tail bounds) — genuinely easier than `riemann_ab.c` (209 lines, most of it Lerch-sum tail bounding that has no analogue here) |
| `toeplitz_blocks.c` | ~40 | 1 | variant of `blocks.c` (62 lines); budget a day because block indexing errors are exactly the kind of thing that survives compilation and needs the closed-form K4 test to catch |
| `eigmin.c` | 0 (copy) | 0.5 | pure port; budget half a day for the rename and a compile/link/run smoke pass, not for new logic |
| `circle_roots.c` | ~150 | 2 | new, but de-risked: §2.5's smoke test is essentially the whole algorithm already working; the work is candidate generation at scale (mirroring `secular.c`'s scan-then-QR two-stage strategy, `secular.c:185-265`) and the Chebyshev speed-up if `M` gets large |
| `truth.c` | ~120 | 1.5 | new; §2.4 did the hard discovery work (the `complex_roots` hang and its fix) already — implementation is mostly wiring `fmpz_poly_factor_squarefree` output into a multiplicity-tagged spectrum struct |
| `compare.c` | ~50 | 0.5 | new, simple nearest-neighbour matching |
| `tools/ihz.c` | ~120 | 0.5 | port of `tools/zst.c`'s shape |
| tests (7 files, closed-form + integration) | ~350 | 2.5 | new pinned numbers throughout, K4/Petersen/cube hand-derivations to check against |
| fuzz (2 harnesses) | ~150 | 1 | new; Ihara-Bass exact-polynomial-identity check is the highlight and should be written first (red-green) |
| mutation, wiring, README, Makefile | — | 1 | mechanical |
| **total** | **~1360** | **~14 days** | roughly 90% new code by line count, but a large fraction of the *hard problems* (certified minimal eigenpair of a real symmetric ball matrix, deflated positive-definiteness certification, the interval-Newton-after-cheap-candidates pattern) are solved problems ported wholesale (`eigmin.c`) or import-modified (`circle_roots.c` reuses the *pattern*, not the code, of `secular.c`) |

**Risks, ranked**:
1. **`acb_mat_eig_multiple_rump` reliability at scale** (§2.3, §2.6): failed at `n=24` even with
   matching precision; needs the doubling-precision retry loop from FLINT's own test harness, and
   even then its robustness at Petersen-scale multiplicity (mult-5 eigenvalue) and beyond is
   unverified here. Mitigated by making it a secondary cross-check, not the primary truth route
   (§2.4's squarefree-charpoly route was both faster and reliable at every size tried).
2. **`arb_fmpz_poly_complex_roots` non-termination on repeated roots** (§2.4) is a real trap for
   *any* code path that calls it directly on a matrix's raw characteristic polynomial without first
   checking squarefreeness — worth a defensive comment (or an assertion that the input is
   squarefree) at every call site in `truth.c`, since a future edit that "simplifies" by removing
   the `fmpz_poly_factor_squarefree` step would silently hang, not fail loudly, on the very test
   graphs (K4, cube, Petersen) that exercise it.
3. **`c_0` / trivial-divisor arithmetic at the boundary `k=0`**: the formula
   `report/sections/08_quantum_ihara_general.tex:27-31` is stated for `\ell\ge1`; `k=0` (the
   Toeplitz diagonal `t_0`) needs its own derivation (`\Tr B^0 = 2|E|` trivially, but the trivial-
   divisor subtraction at `k=0` needs checking against the `(1-u^2)^{|E|-|V|}` factor's own `k=0`
   term, `=2(|E|-|V|)`, plus the `q^0+1=2` from the `q+1` pair) — flagged as the single most likely
   place for a `zst`-`b_0`-style off-by-one, and should get its own red test before any other work
   in `cycles.c`.
4. **Ground-truth citation infrastructure is thinner here than for zeta.** `zst/README.md`'s house
   rule ("every formula in `src/` cites... `refs/src/2511.22755/...` by file and line") worked
   because arXiv:2511.22755 is a single fetchable TeX source. The Ihara-Bass ground truth is spread
   across a paper (Bass 1992, not on arXiv) and a textbook (Terras 2010) — not fetchable the way
   `refs/fetch_sources.sh` fetches arXiv sources. This audit was able to cite everything needed to
   *this repo's own* `report/sections/02_definitions.tex` and `08_quantum_ihara_general.tex`
   instead, which already carry `stipulated`/`proved` status and their own upstream citations
   (`db/claims.tsv`, `db/definitions.tsv`) — recommend `ihz/src/*.c` cite those files by line
   (as this document does), the way `zst/src/*.c` cites `refs/src/2511.22755/mc2arXiv.tex`, rather
   than trying to stand up a `refs/src/` copy of a book. No code blocked on this; a documentation
   convention decision only.
5. **Window-size rule of thumb is unknown for this case** (unlike zeta's `N \sim 10\lambda^2` from
   `plan.md:314-316`, calibrated by the benchmark in `docs/worklog/2026-09-18.md`). Since Ihara has
   no second truncation `N` (the task states this explicitly — only `M`, the window itself), the
   relevant question is instead "how large must `M` be, relative to the graph, for `\xi`'s minimal
   eigenvalue to be well-separated and the window to resolve all nontrivial angles" — an empirical
   question for the integration test (§5) to answer once the code exists, not answerable from this
   audit alone.
