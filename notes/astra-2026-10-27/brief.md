# Brief: the 2026-10-27 round — the tree of local GKP codes and the Pizer graph as H¹ of X₀(p); two topics, four provers, cross-family reviews

Author of the brief: `claude:fable-5.1`, 2026-10-27. TJO: "i don't like the overlap interp. I *do* nevertheless want to understand how to
connect this space [the rationals as a lattice in the adeles, with its symplectic geometry] with ihara zeta better ... choose two fable
subagents and two astra subagents. Each pair of fable+astra works out a proof, then they exchange and review."

**Design.** Two topics, `tree-codes/` and `pizer/`. For each topic one `codex:gpt-6-astra` (xhigh) prover and one `claude:fable-5.1` prover
work **blind of each other** from the same `lane-brief.md`; the astra prover writes in `<topic>/astra/`, the Fable prover in `<topic>/fable/`.
When both have finished, the proofs are exchanged: a fresh Fable agent REFUTE-reviews the astra proof (`<topic>/review-fable-of-astra.md`) and a
fresh astra lane REFUTE-reviews the Fable proof (`<topic>/review-astra-of-fable/`). These are **cross-family** reviews, which is what the record's
gate wants before anything is promoted. Nothing is registered by any lane; the orchestrator lands the results (worklog, HANDOFF, commits).

**Binding by reference.** The sections "Where the record stands", "Game rules", "Conventions" and "Output protocol" of
`notes/astra-2026-10-23/brief.md`, and the REFUTE review protocol of `notes/astra-2026-10-25/brief.md`, apply verbatim. Differences for this round:

- **Steer (binding, from TJO, 2026-10-27).** The adelic lattice Q² ⊂ A² with its symplectic form and the Clifford group SL₂(Q) that preserves it
  are the structures to build on. The "zeta as the Mellin transform of overlaps of the code with a squeezed vacuum" reading (`adelic-gkp.md` §7)
  is **not** to be used or built on. Every statement must connect a lattice, a symplectic form and a zeta function by a map or an identity,
  never by an overlap.
- **Read first:** `HANDOFF.md` (sessions 2026-10-25, 2026-10-23, 2026-10-06), `notes/adelic-gkp/graph-ihara.md` (§2(b), §4–§6, §8),
  `notes/adelic-gkp/adelic-gkp.md` §§1–2 and the summary G1–G3, G11, G13; `notes/adelic-gkp/lattice-tower.md` §§1–2;
  `notes/adelic-gkp/data-ladder.md` ("The answer in one paragraph", §0, §3). For `pizer/`, also `report/sections/04u_deninger_lps.tex` and
  `04z_cerednik_drinfeld.tex` headers (the record's LPS/Shimura-curve route; do not redo it, cite it where your statements touch it).
- **Time budget: about 60–75 minutes of wall clock** for a prover, about 45 for a reviewer. Write each finished item at once.
- **Environment.** `python3` (3.12) has numpy, scipy, mpmath, sympy, networkx (system). PARI and python-flint: use the interpreter
  `/tmp/claude-1000/-home-tobias-Projects-riemann-channel/dcae8e10-414e-4cb4-8b95-d35e159cfb50/scratchpad/venv-astra/bin/python`
  (cypari2 with PARI 2.17.2 including `mfinit`, `mfeigenbasis`, `polmodular`, `ellinit`/`ellcard`/`ellgroup`; python-flint; numpy, sympy, mpmath,
  networkx are installed there too). No `gp` binary. No network, no `pip install`, no system packages, no git. `refs/src/` is **not** fetched on
  this machine: cite literature bibliographically (author, title, year, the statement you use), from memory, and mark "from memory".
- **Write only inside your own lane directory.** Provers: do not read the other prover's directory of your topic (`astra/` must not read
  `fable/` and vice versa). Reviewers read the proof they review and may read the other proof only after their verdict lines are written, for a
  short "agreement" note.
- Author lines: `codex:gpt-6-astra` for the astra prover, `claude:fable-5.1` for the Fable prover; reviews say which family reviewed which.

| topic | directory | task, in one line |
|---|---|---|
| T | `tree-codes/` | the (p+1)-regular tree is the space of GKP codes of the local phase space Q_p²; geodesics are pairs of transverse Lagrangians and the squeeze is the step; the Ihara zeta of Γ\T is the zeta of the squeezes in Γ, with the explicit formula's orbit terms equal to the p-adic Lefschetz traces of those squeezes |
| P | `pizer/` | the supersingular ℓ-isogeny graph mod p is Γ\T_ℓ for an arithmetic lattice of a definite quaternion algebra, its Ihara zeta is the reciprocal L-polynomial of X₀(p) over F_ℓ, its Ramanujan property is Weil's theorem for J₀(p), and the graph's label phase space (Z^{2n}, Ω, M) is H¹ of X₀(p) with Frobenius at ℓ (how exactly, and integrally?) |

Deliverables per prover: `<topic>/<family>/<family>-proofs.md` (astra: `astra-proofs.md`; Fable: `fable-proofs.md`), `progress.txt`, `checks/*.py`
with `checks/output_*.txt`. The two mandatory closing sections ("Numerical checks for the blind lane", "What this changes in the notebook") are
the completion signal.
