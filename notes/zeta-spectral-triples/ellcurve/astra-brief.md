# Brief: review and correct the plan for MVP-3, the CCM construction on L(E, s) for E/Q

You are the review-and-correction lane of a research notebook (repo root = working directory).
Your input is the orchestrator's draft `notes/zeta-spectral-triples/ellcurve/plan.md` (Sections 1-6:
the explicit-formula distribution D1-D6, the questions Q1-Q5, the lanes and acceptance criteria).
Read, in this order: that draft; the parent plan `notes/zeta-spectral-triples/plan.md` Sections 1.1-1.5
(the verified formula sheet for zeta), 3.2 (data model), 6.3, 7, 8; the paper's TeX
`refs/src/2511.22755/mc2arXiv.tex` (locate the labels `bombtest`, `bomp`, `w02`, `computearch`,
`bigmatrix`, `basicexpli`, `basics`, `key`, `even-simple` with grep; cite by line); the C
implementation of the zeta case `zst/src/riemann_ab.c` (the constants exactly as implemented and
tested: `w(L)`, `C(L)`, the sign conventions) and `zst/include/zst.h`; the mpmath prototype
`notes/zeta-spectral-triples/ccm_proto.py` (its quadrature cross-checks are the pattern for any
formula you correct); `zst/README.md` (rules of the house); `notes/zeta-spectral-triples/report-2026-09-18.md`
(the zeta accuracy laws that Q2 refers to). Optional background for Q1: Connes-van Suijlekom
`refs/src/2511.23257/Araki-final-oct25.tex` (the abstract positivity/finite-rank theorem).

Numerics you may run: `python3` with numpy, scipy, sympy, mpmath; PARI through
`/tmp/claude-1000/-home-tobias-Projects-riemann-channel/d28359ce-69e4-418f-93c1-0dfdf6562319/scratchpad/venv/bin/python`
(`import cypari2; p = cypari2.Pari(); E = p.ellinit([0,-1,1,-10,-20]); p.ellap(E, 2); p.lfunzeros(p.lfuncreate(E), 12)`).
Write scripts to `notes/zeta-spectral-triples/ellcurve/checks/` (you own it) and your report to
`notes/zeta-spectral-triples/ellcurve/astra-review.md`. Do not modify anything else; do not overwrite
`plan.md` (the orchestrator applies your corrections).

## Task

1. Formula sheet, corrected. For D1-D6 in `plan.md` Section 1: state each precisely in the paper's
   normalisation (the same `D(y)` on `[0, L]`, the same `a_n, b_n` definitions as parent 1.1), then
   CONFIRM it, or CORRECT it (the true formula, with a derivation from the explicit formula of
   `Lambda(E, s)` and from the paper's TeX, cited by line), or mark OPEN with what is missing. In
   particular:
   - D2: the archimedean kernel for `Gamma_C(s + 1/2)` and its coefficient, derived the way the
     paper derives `W_R` (Prop. `computearch` and the surrounding definitions), not by analogy.
     Confirm or refute the Legendre-duplication identity at the level of kernels.
   - D3: DERIVE the identity shift `s_E(L)`: the conductor term, the `(2 pi)^{-s}` constant, the
     regularisation constants, the window-edge constants (`w(L)`, `C(L)` analogues). Give it in
     closed form ready to implement, and give the zeta case back from the same general formula as a
     check (the parent's `w(L)`, `C(L)`, `(gamma + log 4 pi)/2` must come out).
   - D4/D5: the general `(d, mu)` window integrals; verify by quadrature in mpmath for `(1, 1)` and
     `(2, 1/2)` at two values of `n` and of `L`; state the sign of `a_n^{(R)}` and of `b_n^{(R)}`.
   - D1: atoms and weights, including bad primes (degree-one Euler factors) and the counting rule
     H-COUNT for a minimal model at `p = 2, 3` (is the naive affine count plus one correct for the
     general Weierstrass form at the singular reduction? verify on the four curves against PARI).
   - D6: no pole term. Anything else that enters (e.g. does the explicit formula of an entire
     `Lambda` carry a constant that the zeta case absorbed into `W_{0,2}`?).
   Deliver the corrected sheet as a self-contained section "Formula sheet for the workers", with
   every formula numbered and every constant defined, so that Lane B can implement it without
   reading the rest.

2. Numerical confirmation of the sheet: an mpmath script that builds `(a_n, b_n)` for `11a1` from
   your sheet, runs the parent's pipeline (you may import or copy from `ccm_proto.py`), and compares
   the recovered spectrum with PARI's zeros at `lambda^2 = 13, N = 60` (or whatever is feasible in
   your time). If the first zero comes out to several digits the sheet is right; if not, find the
   error. Record the run (`checks/*.out`). Also record `xi_0`, `s_1`, `min spec E`, `min spec O` for
   `37a1` at two or three values of `lambda` (Q1 evidence, preliminary).

3. Q1 (Section 2): analyse theoretically. Which of H-a / H-b / H-c is forced by the structure of the
   construction (odd `g`, pole at `0` iff `xi_0 != 0`, even-simple, the `2N` count, Lemma `key`)?
   Can the paper's construction represent a zero of odd multiplicity at the centre at all? Is there
   a natural odd-block variant (which functional replaces `eta` when `<eta|xi> = 0`)? State your
   prediction before running the numbers of item 2, then compare.

4. Q2-Q5: comment briefly (a paragraph each): what is predictable now, what the numbers must decide.

5. Critique the plan itself: object choice (is `L(E, s)` over Q the right "simplest zeta with zeros"
   for understanding CCM, or would a real Dirichlet character be strictly better as the first step
   and the curve second?), the lane split and the acceptance criteria, the risks (Section 6),
   anything missing. Be blunt; the orchestrator prefers a corrected plan to a polite one.

Keep a correction ledger (one row per change: claimed / true / why / where it matters). Label every
hypothesis H-<name> with a one-line note on its status. Do not re-prove the paper's theorems; isolate
what you derive from what you cite. Finish within about one hour of work; a shorter report with
verified formulas beats a longer one with unverified ones.
