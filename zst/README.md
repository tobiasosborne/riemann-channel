# zst: zeta spectral triples on FLINT/arb

A rigorous C implementation of the construction of Connes, Consani and Moscovici, "Zeta spectral
triples" (arXiv:2511.22755): the truncated Weil quadratic form on the window `[lambda^-1, lambda]`,
its minimal even eigenvector, the rank-one perturbation of the scaling operator, and the real
spectrum that approximates the zeros of `zeta(1/2 + is)`. Every output is a ball (an interval with
certified error), so a run is a computer-verified statement. Reading notes, formula sheet and plan:
`../notes/zeta-spectral-triples/plan.md`.

Status (2026-09-17): vertical tracer-bullet MVP, zeta only. At the paper's own parameters
`x = lambda^2 = 13`, `N = 120`, 700 bits, the whole pipeline runs in 5 s and returns the paper's
table as certified upper bounds: `|z_1 - gamma_1| <= 2.44e-55`, ..., `|z_50 - gamma_50| <= 2.04e-3`,
with the even-simple hypothesis certified and all 120 positive spectral values accounted for
(`../notes/zeta-spectral-triples/zst_run_x13_N120.txt`; the mpmath prototype needed 108 s for the
same case without certification).

## Build and run

    make            # build/libzst.a and the driver build/zst   (FLINT >= 3.0: apt install libflint-dev)
    make check      # unit and integration tests
    ./build/zst --x 13 --N 120 --prec 700 --zeros 50

Options: `--x` (`lambda^2`; prime powers `<= x` enter), `--N` (Fourier truncation, matrix size `2N+1`),
`--prec` (bits), `--zeros` (how many `gamma_k` to compare against), `--iters` (inverse-iteration cap).

## Pipeline and what is certified

| step | module | output | certification |
|---|---|---|---|
| explicit-formula data `(a_n, b_n)` | `src/riemann_ab.c` | Loewner data of the Weil form matrix | balls; series tails bounded (`mag_geom_series`) |
| even / odd blocks | `src/blocks.c` | `E` (`N+1`), `O` (`N`) | exact ball arithmetic |
| minimal eigenpair | `src/eigmin.c` | `eps_N`, `xi` | Krawczyk operator on the bordered system (Rump's method), contracted to the residual-limited width |
| even-simple hypothesis | `src/eigmin.c` | inertia counts | unpivoted `LDL^T` in balls: exactly one even eigenvalue below `2 eps_N`, no odd one |
| spectrum | `src/secular.c` | `N` positive roots `s_k` | QR candidates from the odd block of `D'^2`, each root by interval Newton; `N` disjoint roots is a complete list |
| comparison | `src/compare.c` | `\|z_k - gamma_k\|` bounds | `acb_dirichlet_zeta_zeros` |

Design notes that cost a day to learn and are worth keeping: arb's `acb_mat_eig_enclosure_rump`
returns its inflated containment box, so the eigenvector had to be re-verified and contracted by hand;
the normalisation `sum_j xi_j = 1` amplifies the eigenvector by the 18 to 28 digits by which the
eigenfunction is small at the window edge, and the secular function is then a difference of huge
terms, so global root isolation by ball arithmetic is hopeless while point plus tiny-interval Newton
verification is easy; two of the `N` positive roots lie far beyond the last pole (`s ~ 107, 339` at
`N = 40`), so completeness must be by count, never by a search range.

## Rules of the house

1. Red-green TDD. A failing test precedes every change of behaviour. The test files under `tests/`
   are the specification; `tests/test_ab.c` pins `(a_n, b_n)` to 50-digit mpmath reference values,
   `tests/test_pipeline.c` pins the end-to-end numbers of the prototype, `tests/test_secular.c` and
   `tests/test_eigmin.c` pin closed-form cases. History of this MVP: the eigenvector-width and
   root-isolation bugs above were found by tests that were red first.
2. Mutation testing. `make mutate` (`tools/mutate.py`) applies single-point mutants to `src/*.c`
   (operator swaps, comparison flips, off-by-one, dropped negations, wrong constants), rebuilds the
   tests under AddressSanitizer, runs `make check`, and lists every survivor with its diff. A survivor
   is a gap in the tests; the next red test targets it. Record for this MVP (2026-09-17): batches of
   30 and 40 mutants, 27/30 and 35/40 (seed 1), 29/40 (seed 2) killed. Two real gaps were found and
   closed by new tests (`test_root_beyond_last_pole`: the `j = N` branch; `test_verify_from_perturbed_start`:
   the Newton contraction step, which needed `zst_secular_verify` in the API). Remaining survivors, all
   inspected: equivalent mutants (loop-termination and search-schedule constants, comparator ties,
   `i*i` versus `i*j` under `i == j`, a mutation inside a comment), one mutant of the QR candidate
   matrix that the Newton polishing absorbs (the certified output does not depend on the candidate
   generator, which is therefore only tested through it), and two out-of-bounds reads in the sort and
   disjointness loops of `secular.c` that happen inside uninstrumented FLINT calls and so escape ASan.
   The last two are the known debt.
3. Fuzzing. `make fuzz` builds libFuzzer harnesses with AddressSanitizer for the secular-root module
   (`fuzz/fuzz_secular.c`: arbitrary normalised `xi`, invariants: every returned root is a certified
   zero, roots increasing and disjoint, count in range) and for the data and block builders
   (`fuzz/fuzz_ab.c`: random `x, N, prec`; finiteness, radius bounds, two-precision consistency,
   `b_0 = 0`, block symmetry). `make fuzz-plain` drives the same harnesses from a seeded PRNG without
   clang. First catch: `b_0` was a rounding neighbourhood of zero instead of exactly zero.
4. Ground truth is cited in code. Every formula in `src/` cites the local copy of its source by file
   and line (`refs/src/2511.22755/mc2arXiv.tex`, sha256 in `refs/manifest.sha256`, fetched by
   `refs/fetch_sources.sh`), or the mpmath prototype and its run record under
   `notes/zeta-spectral-triples/`. A formula without a citation is a bug.

## Layout

    include/zst.h     public API (documented per function)
    src/              riemann_ab.c  blocks.c  eigmin.c  secular.c  compare.c
    tools/zst.c       command-line driver;  tools/mutate.py  mutation testing
    tests/            test_ab  test_eigmin  test_secular  test_pipeline   (make check)
    fuzz/             fuzz_secular.c  fuzz_ab.c   (make fuzz, make fuzz-plain)

## Next (plan.md milestones)

M3: the general explicit-formula data model (`zst_weil_t`: atoms, exponential-series kernels,
trivial-divisor poles, identity shift) with the archimedean constants derived rather than typed, and
Dirichlet characters as the first extension. M4: scale (`x ~ 100`, `N ~ 10^3`, thousands of digits;
OpenMP; the Loewner displacement structure). M5: `det_reg -> Xi` and the prolate comparison.
