# riemann-channel

**Aim.** Find a formulation of the Riemann hypothesis in the language of
tensor networks and operational quantum mechanics (channels, Kraus
operators, transfer matrices, matrix-product states) that

1. captures the salient mechanisms of the RH proofs that exist (Weil's
   for curves, Deligne's for varieties over finite fields, Ihara–Bass and
   the Ramanujan property for regular graphs), and
2. connects more directly to quantum mechanics than the classical
   Hilbert–Pólya programme does,

with a view to understanding what a Hilbert–Pólya type approach is
missing. Nothing in this repository proves anything about RH. It is a
research notebook: computations, write-ups, and the conversation that
produced them.

## The working picture

Every zeta function in sight has two sides.

- **Side A, the gas.** A nonnegative count of closed orbits (prime cycles
  of a graph, points of a curve, prime powers with weight $\log p$) and
  its Euler product. This side is a product state: the primes do not talk
  to each other.
- **Side B, the transfer matrix.** A small non-Hermitian operator whose
  power sums reproduce the counts. Its eigenvalues are the zeros. RH is
  the statement that all of them have the same modulus, i.e. that the
  transfer matrix is a scalar times a unitary on its nontrivial part.
  For a $(q+1)$-regular graph this is the Ramanujan property; for the
  Riemann zeta it is a uniform decay rate for a contraction semigroup with
  one mode per zero.

In tensor-network terms, side A is the ring-norm sequence of a
matrix-product state and side B is its transfer matrix. The founding
session established the dictionary (quantum Ihara–Bass for mixed-unitary
channels; Bost–Connes as a matrix-product operator over the prime chain;
the Lax–Phillips scattering symbol of the modular surface as the phase of
the Bost–Connes Lévy exponent at $\beta = 1$), computed concrete
Ramanujan quantum expanders from the Weil representation and
Lubotzky–Phillips–Sarnak generators, and gave an exact matrix-product
formulation of the Weil conjectures for quadratic Artin–Schreier curves,
where RH is manifest as $EE^\dagger = qI$ for the transfer matrix.

The existing proofs then sort themselves by *where the unitarity comes
from*:

| proof | what supplies $\lvert\mu\rvert = \sqrt q$ | Hilbert–Pólya operator exhibited? |
|---|---|---|
| Artin–Schreier transfer matrix | Parseval for additive characters | yes, explicitly |
| Weil, curves | Hodge index on $C\times C$ | yes (Rosati positivity) |
| Deligne, varieties | positivity of even tensor powers, fixed loss paid by a base curve, roots as $k\to\infty$ | no |
| LPS graphs | Deligne/Weil via Eichler–Shimura | inherited |
| random graphs, interlacing families | trace method / real-rootedness | no |

Deligne's route reaches the spectral bound with no inner product at all.
What it needs instead is a positivity, an operation under which
eigenvalues multiply while the trivial loss stays fixed (products of
varieties), and the sign that puts the interesting eigenvalues in the
numerator of the zeta function. The Riemann zeta has the positivity and
the sign; it lacks the product. Where the Hermitian structure enters, or
whether it must, is the question this notebook circles.

## What is and is not established

Established (standard theory, numerically confirmed, see `notes/`):
the quantum Ihara–Bass identity; the Bost–Connes MPO structure; the
scattering-symbol identity for $\zeta$ and the 3000-zero ring-norm test;
the Weil–LPS channels as exact Ramanujan quantum expanders; the
Artin–Schreier transfer matrix.

Not established: RH; a Stinespring form of the compressed Lax–Phillips
semigroup with prime dilations as jump operators; any construction that
couples the primes non-abelianly on the $\zeta$ side. See `HANDOFF.md`
for the live list of open steps.

## The lab book

`report.tex` is the pdflatex lab book, sharded under `report/sections/`
following the parent repository's pattern. Four databases under `db/` are the
single source of truth: `notation.tsv` (rendered to `report/macros.tex`; no
shard may define a macro), `definitions.tsv` (each concept defined once, in
`report/sections/02_definitions.tex`), `claims.tsv` (one row per theorem-like
environment, with a status derived rk-light style and printed inside the
environment) and `provenance.tsv` (quotes byte-checked against the arXiv TeX
sources under `refs/src/`). `make regen` rewrites the generated files,
`make check` runs the parity gate, `make ci` adds a fresh build and re-runs
the fast scripts against `outputs/`, and `make hooks` installs `make ci` as
a git pre-commit hook. See `report/README.md` for the shard map.

## Contents

    report.tex, report/   the lab book (master, shards, generated files, references.bib)
    db/                   notation, definitions, claims, provenance databases (TSV)
    Makefile, scripts/labbook_check.py, scripts/ci_local.sh   gate and local CI
    HANDOFF.md            live state and next steps (read first)
    docs/worklog/         dated session logs
    notes/                write-ups, Markdown and rendered HTML
    scripts/              python3 + numpy + mpmath + sympy; run from repo root
    data/                 first 3000 zeta zeros; ring-norm test arrays
    outputs/              captured stdout of each script
    transcript/           raw session log and a Markdown rendering
    refs/                 fetch script + sha256 manifest for the arXiv TeX sources quoted in notes/

Notes, in reading order:

- `notes/what-rh-has-become.md`: the translation note. Permutations,
  shifts, Ihara zeta, MPS transfer matrices; what RH means on side B.
- `notes/riemann-channel-note.md`: the main write-up. Scattering symbol
  $S(\tau) = \xi(1-2i\tau)/\xi(1+2i\tau)$, the functional-model semigroup,
  the prime-phase identity, the ring-norm test, the open Stinespring
  question.
- `notes/weil-lps-channels.md`: Weil-representation channels on
  $\ell^2(\mathbb F_p)$ with LPS generators; Hastings bound, Hecke
  relations, commuting channels, quantum Ihara zeta satisfying RH.
- `notes/artin-schreier-mps.md`: exact MPS formulation of the Weil
  conjectures for $y^q - y = g(x)$ with $g$ quadratic; RH as unitarity of
  the transfer matrix; why Dwork's operator cannot see RH.
- `notes/deligne-via-graphs.md`: Deligne's proof explained through regular
  graphs. Isolates the three ingredients (product, slicing over a curve,
  the sign) and what a Hilbert–Pólya approach would need to replace them.
- `notes/prior-art-quantum-ihara.md`: literature check on the quantum Ihara
  zeta, with byte-verified quotes. The matrix-weighted Ihara–Bass formula is
  known (Matsuura–Ohta, Watanabe–Fukumizu, Sunada); the RH-for-channels
  reading and the MPS dictionary were not found.
- `notes/quantum-ihara-general.md`: the Ihara–Bass formula for the
  non-backtracking superoperator of an arbitrary Kraus family, with a
  structured proof and reviewer verdicts.
- `notes/weil-positivity.md`: Weil positivity for an arbitrary transfer
  operator (one-sided bound without a duality, mode pairing with one, the
  Kraus dichotomy: inverse pairing buys the functional equation, adjoint
  pairing buys reality, unitarity buys both); proofs by the codex prover in
  `notes/weil-positivity/`, sources in `notes/extract/`.

## Reproduce

    python3 scripts/qihara.py              # quantum Ihara–Bass identity
    python3 scripts/bcmpo.py               # Bost–Connes phase operators as MPOs
    python3 scripts/scat.py                # scattering symbol: unimodularity, zeros, prime phase
    python3 scripts/ringnorm.py            # explicit-formula ring-norm test, 3000 zeros
    python3 scripts/weil_lps.py            # Weil–LPS channels, all admissible (p; q)
    python3 scripts/weil_lps_hashimoto.py  # direct edge superoperator for (13, 17)
    python3 scripts/artin_schreier_mps.py  # Artin–Schreier transfer matrices
    python3 scripts/qihara_general.py      # Ihara–Bass for arbitrary Kraus operators (float + exact)
    python3 scripts/weil_positivity.py     # Weil positivity: one-sided bound, duality, Kraus dichotomy, Bochner
    refs/fetch_sources.sh                  # re-fetch the quoted arXiv TeX sources

Notes render with `fmd-report notes/<name>.md -o notes/<name>.html`,
which verifies that every equation typeset.

## Conventions

Sober and accretive. Statements in `notes/` are labelled established or
not established; numerical checks are not proofs; no claims are
registered and no checker discipline is in force. The transcript is the
primary record and the notes are its distillation.

## Authorship and license

Tobias J. Osborne, steering and mathematics, working with Claude
(Anthropic) for computation, drafting, and the arguments recorded in the
transcript. Licensed under the GNU Affero General Public License v3.0;
see `LICENSE`.
