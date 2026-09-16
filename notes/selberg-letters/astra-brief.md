# Brief: an infinite-object zeta whose odd-block form is derived from the letters (Selberg). Prove or correct D1-D8.

You are the prover lane of a research notebook (repo root = working directory). Read, in this
order: `notes/selberg-letters/draft.md` (the orchestrator's draft, statements D1-D8: your main
input); `HANDOFF.md` sections "CENTRAL PRIORITY" and "The Ramanujan property for graded transfer
channels"; the lab-book shards `report/sections/02h_definitions_graded_ramanujan.tex`
(def:graded-transfer-channel, def:graded-rh-fe-ramanujan, def:graded-hashimoto),
`03c_graded_ramanujan.tex` (thm:graded-qihara-bass, thm:graded-harrow, prop:qubit-graded-zeta),
`03d_graded_ramanujan_continuum.tex` (prop:graded-chernoff, obs:divisor-regular-data,
obs:graded-continuous-harrow, obs:selberg-grading-choice, obs:graded-ramanujan-status),
`02b_definitions_arithmetic.tex` (def:geodesic-flow, def:selberg-zeta, def:flat-trace,
def:flat-tower, def:scattering-determinant), `09b_selberg_dictionary.tex` and
`09c_selberg_tower_cusp.tex` (prop:lindblad-sum-of-squares, prop:casimir-laplacian,
prop:quantum-lindblad-tensor, prop:poincare-jacobian, prop:flat-tower, prop:tower-divisor-band,
prop:graph-tower-ruelle, prop:cusp-prime-comb, the "not established" list), `02f_definitions_graded_cmps.tex`
and `04f_cmps_twisted_supertrace.tex` (ring norm = supertrace, ring zeta 1/sdet),
`08_quantum_ihara_general.tex` (thm:qihara-general), `04_riemann_channel.tex` and
`04b_phantasm_forced.tex` (the Riemann channel, prop:riemann-graded-generator). The previous
prover report `notes/selberg/astra-proofs.md` (T2.1, T2.2: conventions for the left-invariant
fields, the sign of the Casimir, H-AN) and `notes/ramanujan-graded/astra-proofs.md` (Conventions,
"Definitions: verdict", D10 relative resonance divisor) are yours to reuse. Sources under
`refs/src/`: Dyatlov-Faure-Guillarmou 1403.0256 (`RuelleResonForHn.tex`: Theorem t:dim2 lines
180-192; horocyclic fields and commutation relations 519-544; Res^0_X, the pushforward e:pushy,
the boundary representation e:poppy, the Poisson operator e:peasy, lines 593-640; the ladder
U_-^m U_+^m and the decomposition of Res_X, lines 557-591), Dyatlov-Zworski 1306.4203 (`zeta.tex`:
flat trace on k-forms eq:guill 495-505, the Lefschetz identity 525-526, zeta_1 at 211), Marklof
math/0407288 (`selberg07.tex`, trace formula and Selberg zeta), Friedman-Jorgenson-Smajlovic
1607.08053 (`main.tex` 592-594, scattering determinant), Hastings 0706.0556, Harrow 0709.1142.
Numerics you can run and extend: `scripts/selberg_lindblad.py`, `scripts/graded_ramanujan.py`
(graded Hashimoto machinery, PGL_2(F_p) and Pauli examples), `scripts/qihara.py`,
`scripts/weil_lps.py`. python3 with numpy, scipy, sympy, mpmath. Write any scripts to
`notes/selberg-letters/finite/` (you own it) and the report to
`notes/selberg-letters/astra-proofs.md`. Do not modify anything else. Do not overwrite `draft.md`.

## Task

For each of D1-D8 in `draft.md`: state it precisely (fix conventions; declare every hypothesis as
H-<name> with a one-line note on whether it is standard and where it is proved in the sources, by
file and line), then PROVE it, or CORRECT it (the true statement, proved), or REFUTE it (explicit
counterexample, verified by a script where finite), or mark OPEN with exactly what is missing. Keep
a correction ledger (one row per change to the draft: claimed / true / why). Where the draft asks
"say precisely what is derived from the letters", answer as a theorem with a labelled list of
inputs: Haar invariance of the letters, the sl2 relations, DFG analysis (cited by line), the
coercivity (Selberg 1/4). Do not prove DFG's analytic theorems again; isolate the algebra you prove
from the analysis you cite.

Priorities, in order (spend the effort here):
1. D3 (the first-band mechanism: algebra of Omega on Res^0, reality from the letters, the form G,
   the operator-form FE) and D2 (exact bookkeeping of the graded ring zeta: signs, the trivial
   divisor with multiplicities, which of zeta_R / Z_S / D_tow is the right ring zeta, the precise
   statement of (RH)/(FE)/(Ram) for it). These two are the deliverable: the Selberg zeta as a
   graded transfer whose odd-block form is derived from the letters.
2. D7 (the same mechanism for graphs and for the graded quantum Hashimoto operator, with scripts):
   this is finite, fully checkable, and closes an open item of the notebook.
3. D4, D5, D8 (operator-level Ihara-Bass; what the transfer realisation is and on which regular
   data; the K-type supercancellation).
4. D6 (modular surface; exploratory; hypotheses flagged; no invented citations).

## Conventions (must match the notebook; see draft.md "Conventions" for the full list)

- G = PSL_2(R), left-invariant fields, H = diag(1,-1), E = ((0,1),(1,0)), W = ((0,1),(-1,0)),
  Omega = (1/4)(H^2 + E^2 - W^2), X = H/2, U_pm = (E pm W)/2, [X, U_pm] = pm U_pm, [U_+, U_-] = 2X.
  Delta positive; Delta = -Omega = -(1/4)(H^2 + E^2) on right-K-invariant functions. Koopman
  (e^{-tX} f)(m) = f(phi_{-t} m). Flat trace as in def:flat-trace and DZ eq:guill; the Laplace
  variable of the flat trace is the notebook's varsigma with poles at -1/2 - k pm i r_j; DFG's
  lambda in (X + lambda)u = 0 is the same variable.
- Ring zeta convention: Z(u) = exp(sum_n N_P(n) u^n/n) = 1/sdet(1 - u E_d), zeros from the odd
  sector; continuum: Z(s) = exp(int_0^infty e^{-st} str(t) dt/t) up to the normalisation you fix
  and state. Divisor nu = m_0 - m_1 (even minus odd); trivial divisor signed with parities; pair of
  reference rates; critical line = midpoint.
- Graded CP transfer vs graded spectral transfer as in `notes/ramanujan-graded/astra-proofs.md`.

## Deliverable format

`notes/selberg-letters/astra-proofs.md`: a short "Main conclusions" list first; then for each
D-item a block "Statement (as proved) / Hypotheses H-* / Proof / Status: PROVED | CORRECTED (with
the ledger row) | REFUTED (with script) | OPEN (with what is missing)"; then the correction ledger
as a table; then a section "What is derived from the letters" (the labelled-inputs theorem of D3,
restated for D7); then "Numerical checks" listing every script you wrote with its printed tally.
Proofs in Lamport style where they are more than a few lines (numbered steps, each with its
justification). Print the final tally PROVED/CORRECTED/REFUTED/OPEN at the end of the report.
