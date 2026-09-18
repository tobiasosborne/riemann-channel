# ihz: the Connes-Consani-Moscovici construction on the Ihara zeta of a regular graph

Second vertical MVP after `../zst/` (the Riemann zeta). Plan, theory and prototype:
`../notes/zeta-spectral-triples/ihara/` (`plan.md`, `lanes/theory.md` claims `IH-n`, `ihara_proto.py`).
Conventions: `include/ihz.h` (its header comment is the convention table every module follows).

Status (2026-09-18, evening): G1-G3 of the plan done in one session with three Opus workers plus the
orchestrator. On every graph tried (`K4 Q3 petersen K33 heawood pappus necklace:2 necklace:3 twoK4
necklace:6 prism:16 Cn:5`) and on the elliptic curve over `F_5`, the exact stage finds the critical
window `K = R + 1` and proves that the integer kernel polynomial of the exact Weil form equals the
squarefree retained characteristic polynomial (the EXACT ANCHOR line); the ball stage at that window
returns certified roots on the critical circle matching the certified truth to `1e-73`, certifies
the unitary key lemma `U^T (T - eps) U = T - eps` and the determinant identity, and returns Prony
weights whose balls contain the multiplicities. Captured runs: `../notes/zeta-spectral-triples/ihara/bench/`.

## Build and run

    make            # build/libihz.a and build/ihz   (FLINT >= 3.0)
    make check      # test_exact, test_toeplitz, test_roots, test_pipeline
    ./build/ihz --graph petersen --scan
    ./build/ihz --graph necklace:6 --scan --no-unitary
    ./build/ihz --counts 0,8,32,104,640 --q 5 --triv 5:1,1:1 --sign -1 --scan     # curve y^2 = x^3+4x+b / F_5

`--scan` prints one row per window `Mp = 0 .. Mcrit + 1`: exact rank and kernel dimension, the
certified minimum eigenvalue of the even and of the odd block (the full-form minimum is the smaller
of the two; it is negative exactly when the retained divisor has an off-circle pair), the number of
certified roots on the circle, the largest distance from a truth point to a root point, and whether
the unitary key lemma certified.

## Pipeline

| stage | module | what | certification |
|---|---|---|---|
| graph, Hashimoto `B`, `N_k = Tr B^k` | `graph_io.c hashimoto.c cycles.c` | exact | Ihara-Bass as an exact polynomial identity |
| retained charpoly, truth spectrum | `truth.c` | `charpoly(B)` / trivial factors, squarefree factorisation, roots per factor | exact division; `arb_fmpz_poly_complex_roots` on squarefree factors only |
| Weil data `t_k` | `weil_data.c weil_graph.c` | `c_k = N_k - trivial`, `t_k = sign q^{-k/2} c_k` | exact `c_k`, balls `t_k` |
| Toeplitz form, blocks, exact congruence | `toeplitz.c` | `T`, `E`, `O`, `D T D` integer | exact |
| critical window, kernel polynomial | `rank.c` | rank over `Q`, nullspace | exact |
| minimal eigenpair, even-simple | `eigmin.c` (= `zst/src/eigmin.c`) | Krawczyk, positive-definiteness certificate | balls; declines at `eps = 0` and at degenerate eigenvalues |
| roots on the circle | `circle_roots.c` | `R(theta) = xi_0 + 2 sum xi_j cos(j theta)`, isolate + interval Newton | balls, complete by count |
| unitary key lemma, determinant identity | `unitary.c` | `U = Z^* - |Z^* xi><eta|` | ball certificates of exact identities (IH-11) |
| multiplicities | `prony.c` | Vandermonde solve at the truth points | balls containing integers |
| comparison | `compare.c` | nearest root point per truth point | balls |

## Known limits (MVP)

- Regular graphs only; irregular graphs are covered by the prototype (the construction is
  structurally unable to return their divisor, plan 1.5).
- `ihz_eigmin` declines to certify a degenerate block eigenvalue (prism at `Mp = 6`, even block; the
  odd block of `Cn:5` at `Mp = 2`); the exact stage still carries the anchor there.
- Real retained points at `mu = +-sqrt q` (angle `0` or `pi`) are reported as unresolved by the
  circle-root finder; the exact kernel polynomial sees them.
- Testing discipline was relaxed for this build at TJO's request: one pinned test file per worker
  and the end-to-end anchor; no fuzz, no mutation yet.
