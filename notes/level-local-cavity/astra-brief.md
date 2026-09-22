# Brief for the prover: the local factors of the prime-level scattering matrix are the finite cusp-graph scattering of the tree quotient at the level prime; the delay is the edge; the level-q model space is (arithmetic zero modes) plus (a finite cavity with the cusp comb); "a cusp per prime" made literal at one prime

You are the prover in a mathematical research notebook (git repo, current directory). Author line for
everything you write: `codex:gpt-6-astra`. Write ONLY the file `notes/level-local-cavity/astra-proofs.md`
(create it; overwrite if present) and, if you want scratch computations, python files under
`notes/level-local-cavity/checks/`. Do not edit anything else. Do not run git. python3 with numpy, mpmath,
sympy, scipy is installed. Read first:

1. `notes/deninger-cusp/astra-proofs.md` (this morning's lane; binding conventions): D3.4 the trivial-nebentypus
   prime-level scattering matrix `Phi_1(s) = phi(s)/(q^{2s} - 1) [[q - 1, q^s - q^{1-s}],[q^s - q^{1-s}, q - 1]]`,
   its eigenchannels `phi_±(s) = phi(s)(1 ± q^{1-s})/(1 ± q^s)`, `det Phi_1 = phi^2 (1 - q^{2-2s})/(1 - q^{2s})`,
   residue `3/(pi(q+1))` times the all-ones matrix; D3.6 the nontrivial even nebentypus block
   `[[0, A_psi],[A_{bar psi}, 0]]`, `A_psi(s) = q^{1/2-s} Lambda_psi(2s-1)/Lambda_psi(2s)`; D3.14 the squarefree
   trivial-character tensor product `bigotimes_{r | N} (1/(r^{2s}-1)) [[r-1, r^s - r^{1-s}],[r^s - r^{1-s}, r-1]]`;
   D5.1 the inner model: `u = e^{i tau log q}`, `a = q^{-1/2}`, `b_c(u) = (u - c)/(1 - c u)`, local inner factors
   `L_+ = u b_{-a}(u)`, `L_- = u b_a(u)`, `phi_±(1/2 + i tau)^{-1} = r(tau)^{-1} Theta_1(tau) L_±(tau)`, the
   reduction `I_+ = Theta_1 L_+`, `I_- = Theta_1 L_-/r`; (D5.5) the full model space includes local factors and
   delays, `K_{AB} = K_A (+) A K_B`; the local factors "have additional periodic zeros at height 1/2"; the delay
   `e^{i tau log q}` has model space `L^2(0, log q)`.
2. The notebook's finite cusp graphs: `report/sections/04i_cusp_graph_scattering.tex` (a finite graph with a
   cusp: scattering, resonances, bound states, the one-exit contraction), `04j_cusp_graph_renewal.tex`,
   `04k_elliptic_cavity_scattering.tex` (`thm:multi-exit-scattering`: `S(z) = -Q(z)^{-1} Q(1/z)`, `det S = (-1)^h p/ptilde`,
   `z = q^{s - 1/2}`), `04l_elliptic_cavity_channel.tex` (`thm:h-exit-model`), `09c_selberg_tower_cusp.tex` (the
   Selberg tower and the cusp comb: search `comb`), `03f_selberg_letters_finite.tex`, `02d_definitions_complexes.tex`
   (buildings, trees), and `notes/cusp-graph/` if present.
3. `report/sections/04r_h_theta_channels.tex` (`prop:siegel-constant-term`, `obs:symbol-is-reduced-causal-factor`),
   `notes/h-theta/astra-proofs.md` (conventions), `refs/src/uetake-2007/paper.txt`.

Be explicit. A numerics lane will test every displayed formula and a hostile reviewer will try to refute every
claim. Label PROVED, REFUTED, SHARPENED or OPEN. Keep a correction ledger. Do not pad.

## 0. Why this round

The notebook's programme (HANDOFF, 2026-09-20 evening) sketched "an arithmetic cavity coupled to cusps, a
cusp per prime, cusps integrated out into sinks patched by exit spaces". This morning's lane found that the
prime-level scattering matrix of `Gamma_0(q)` factors as (archimedean `xi`-ratio) times (an explicit rational
`2 x 2` matrix in `q^{-s}`), and that the inverse symbol's local factors `L_± = u b_{∓a}(u)`, `u = q^{i tau}`,
carry periodic zeros at height `1/2` and a delay `log q`. The author of this brief (`claude:fable-5.1`)
believes these local factors ARE the scattering data of the notebook's finite graph with a cusp for the
quotient graph `Gamma_0(q) \ T_{q+1}` (one edge, two vertices, each vertex a cusp of the modular curve: the
two cusps `0, infinity` of `X_0(q)`), i.e. the local part of the level-`q` modular surface is literally a finite
tree cavity with two cusps in the sense of 04i/04k, with the zeta ratio `phi(s)` as the archimedean
"reflection coefficient" and the delay `log q` as the edge length. Prove, refute or sharpen:

**L1 (the local matrix is a tree scattering matrix).** Write `z = q^{-s}` (or the notebook's `z = q^{s-1/2}`;
fix the convention from 04k and say which). Prove that the rational matrix
`M_q(s) = (1/(q^{2s} - 1)) [[q - 1, q^s - q^{1-s}],[q^s - q^{1-s}, q - 1]]` is, after the change of variable, the
scattering matrix `S(z)` of `thm:multi-exit-scattering` for an explicit finite diagram: a core with two cusps
(rays) attached; identify the core (`n` vertices, `T_X`, couplings `c_a`), verify `M_q = -Q(z)^{-1} Q(1/z)` with the
identified `Q`, and identify `det M_q = (1 - q^{2-2s})/(1 - q^{2s})` with `(-1)^h p(z)/ptilde(z)`: what are `p`
and `ptilde`, what are the resonances (zeros of `p` in `|z| < 1`) and the bound states? The expectation: the
core is the single edge of the tree quotient (two vertices of degree `q + 1` in the tree, each with a cusp), the
resonances are the height-`1/2` comb `tau = i/2 + 2 pi k/log q` seen in `L_-`, and the bound state is the
constant (the pole at `s = 1`). If `M_q` is not exactly of the form `-Q^{-1}Q(1/z)` for a symmetric core, say
what the obstruction is (the two cusps of `X_0(q)` have different widths `1` and `q`; the width-one
normalisation of D3.2 may not be the notebook's equal-depth cut of `prop:cusps-are-class-group-bond`/H-CLASS)
and give the correct finite object.

**L2 (the model space splits into arithmetic modes plus the finite cavity).** With `I_± = Theta_1 L_±` (and
`L_-/r`), prove `K_{I_±} = K_{Theta_1} (+) Theta_1 K_{L_±}` (the factorisation `K_{AB} = K_A (+) A K_B`), identify
`K_{L_±}` explicitly as a finite-dimensional-per-period space: the delay part `L^2(0, log q)` (in the Fourier
picture; in the `X = log y` picture: functions supported on `(0, log q)`, the "edge") plus the Blaschke part
(the comb of height-`1/2` zeros, one per period `2 pi/log q`), and say which of these are the notebook's
"delay modes at `z = 0`" of `thm:h-exit-model` and which are resonances. Then state the level-`q` Riemann
channel as: `(Z_t, J)` on `K_{Theta_1}` (the arithmetic modes, the jets of the zeta zeros, as in
`thm:model-space-jets`) coupled through the exit to a finite cavity `K_{L_±}` with the cusp comb; give the
`2 x 2`-block form of the compression `Z_t` in the decomposition (the arithmetic block, the local block, and the
coupling), and the exit functional. Is the coupling triangular (the arithmetic modes feed the cavity but not
conversely, or the reverse)? This is the concrete "cusp integrated out into a sink patched by an exit space".

**L3 (a cusp per prime: squarefree level).** For `N = q_1 q_2` squarefree with trivial character (D3.14), prove
that the local matrix is the tensor product of the two prime-level tree scattering matrices, hence the
scattering matrix of the *product* diagram (the quotient of `T_{q_1 + 1} x T_{q_2 + 1}` by `Gamma_0(N)`'s local
data: a square with four cusps `0, 1/q_1, 1/q_2, infinity`), and that the model space is the arithmetic
`K_{Theta_1}` (with multiplicity `h = 4`?) coupled to the product cavity. Compare with `prop:cusps-are-class-group-bond`
(cusps = divisors of `N` ↔ the "class group" `(Z/2)^{omega(N)}`) and H-CLASS (group matrix block-diagonalised by
the Fourier transform: here the `±` eigenchannels of each prime factor are exactly that Fourier transform).
So "a cusp per prime" is literally the cusps `1/d`, `d | N`, and the finite cavity per prime is the tree
quotient's edge. State the theorem for squarefree `N` and say what changes at prime powers (the local
matrix of `Gamma_0(q^2)` is not a tensor product; give it if cheap, else OPEN).

**L4 (the cusp comb and the Selberg tower).** The notebook's 09c has a "cusp comb" in the Selberg tower.
Identify: is the comb `tau = i/2 + 2 pi k/log q` of `L_-` the same object (the same spacing `2 pi/log q`, the
same height), and does the tower over `q` (levels `q, q^2, ...`) produce combs of spacing `2 pi/(n log q)`?
Two paragraphs; cite 09c by line; mark speculation.

**L5 (what this changes).** One structured page: the level-`q` modular surface as "the Riemann channel plus a
finite cavity with two cusps", the exit through the cavity, and what it says for the arithmetic-cavity
programme (04k/04l: `h` exits, one per cusp; now the arithmetic modes see the cusps only through the local
cavity). Which statements of 04i–04l apply verbatim to the local part; which open items of
`obs:h-theta-next`/`obs:graded-toys-next` this closes.

## Output format

`notes/level-local-cavity/astra-proofs.md`: ledger table (L1–L5, verdicts); full proofs with hierarchical steps;
external theorems stated precisely and marked "not byte-cited"; repo sources quoted by file and line; a
section "Numerical checks for the blind lane" (explicit: `M_q(s)` at `q = 5, 7`, `s = 0.7 + 0.3i` against
`-Q(z)^{-1}Q(1/z)` for the identified core; the determinant identity; the comb zeros of `L_-` and their
height; the delay model space dimension per period; the tensor-product identity for `N = 35`); a section
"Corrections to the brief"; and a closing "What this changes in the notebook" with, per claim, the status
to register and the one-sentence statement.

## Durability (the network is unreliable today; this is mandatory)

Write your output file **incrementally**: create `astra-proofs.md` with the ledger table (all verdicts
`PENDING`) before you start on the mathematics, and after finishing each claim rewrite the file with that
claim's section and its updated ledger row. If you are resumed after an interruption, read your own
`astra-proofs.md` first, keep everything already written, and continue from the first `PENDING` row. Keep a
one-line `notes/level-local-cavity/progress.txt` with the claim you are working on.
