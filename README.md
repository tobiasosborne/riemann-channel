# riemann-channel

Exploratory project, spun out of `../arithmetic-quantum-mechanics` on
2026-09-11. Question: can the Hilbert–Pólya side of the Riemann zeta function
be read as the transfer / entanglement structure of a matrix-product-type
state whose rings are the primes, and does Bost–Connes supply the
thermodynamic (gas) side of that same structure?

Working conclusion so far (see `notes/riemann-channel-note.md`):

- The Lax–Phillips scattering symbol of the modular surface, `S(τ) =
  ξ(1−2iτ)/ξ(1+2iτ)`, is the *phase* of the Bost–Connes Lévy exponent at the
  critical temperature β = 1.
- The Sz.-Nagy–Foias functional model of that phase is a contraction
  semigroup with one mode per zeta zero, decaying at rate β_n/2 with
  frequency γ_n/2. RH is the statement that all modes decay at the single
  rate 1/4 (Faddeev–Pavlov 1972, Lax–Phillips 1976).
- The distributional trace of that semigroup is the von Mangoldt prime
  measure, checked numerically with 3000 zeros to 0.15 %.
- Nothing here proves RH. The open question isolated is whether the
  compressed semigroup admits a Stinespring form with the prime dilations as
  jump operators.

The conversation that produced this is preserved verbatim under
`transcript/`. It is the primary record; the note is its distillation.

## Layout

    HANDOFF.md            live state and next steps (read first)
    docs/worklog/         dated session logs
    notes/                the write-up, Markdown and rendered HTML
    scripts/              python3 + numpy + mpmath + sympy; run from repo root
    data/                 first 3000 zeta zeros; ring-norm test arrays
    outputs/              captured stdout of each script
    transcript/           raw session .jsonl and a Markdown rendering

## Reproduce

    python3 scripts/qihara.py     # quantum Ihara–Bass identity for mixed-unitary channels
    python3 scripts/bcmpo.py      # Bost–Connes phase operators as MPOs over the prime chain
    python3 scripts/scat.py       # scattering symbol: unimodularity, zeros, inner property, prime phase
    python3 scripts/ringnorm.py   # explicit-formula ring-norm test from data/zeros3000.npy

## Conventions

Sober and accretive, as in the parent project. Statements in `notes/` are
labelled established / not established; numerical checks are not proofs.
The parent project's laws (red-green checkers, local ground truth, claims
DAG) are not yet in force here; this is a research notebook, not a trunk.
