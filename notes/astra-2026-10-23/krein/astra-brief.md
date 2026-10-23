# Lane K: Krein–Ramanujan rigidity for SU(1,1) gauge fields on finite graphs

You are `codex:gpt-6-astra`, a prover and constructive verifier in a mathematical research notebook (git repo, current
directory). Read `notes/astra-2026-10-23/brief.md` first (binding). Then read `notes/adelic-gkp/gauge-groups.md` (the SU(1,1)
section and "Next"), `notes/adelic-gkp/graph-ihara.md` §4 and §6, `notes/adelic-gkp/lattice-tower.md` §5, and the tutorial's
Section 6 in `notes/adelic-gkp/tutorial/page.html` (search for "Casoratian"; the page is long, read only 6a–6d and the glossary
entry for Ω). Shard `report/sections/04q*.tex` has `thm:deninger-invariant-polarisation` (the Krein-definite distinction) if you
want the registered form. Write only `notes/astra-2026-10-23/krein/{astra-proofs.md,progress.txt,checks/}`.

## 0. Setting (fix it, then do not re-derive it differently)

Y finite connected (q+1)-regular, n vertices, oriented edges e with reverse ē. A gauge field ρ assigns to each oriented edge a
matrix ρ(e) ∈ SU(1,1) = {g ∈ SL(2,C): g^† η g = η}, η = diag(1, −1), with ρ(ē) = ρ(e)^{-1} = η ρ(e)^† η. The twisted adjacency
A_ρ on C^n ⊗ C² is (A_ρ f)(x) = Σ_{e: x→y} ρ(e) f(y). Then (1 ⊗ η) A_ρ (1 ⊗ η) = A_ρ^†: A_ρ is self-adjoint for the indefinite form
⟨f, g⟩_η = Σ_x f(x)^† η g(x) of signature (n, n). Gauge transformations g: V → SU(1,1) act by ρ(e) ↦ g(x) ρ(e) g(y)^{-1} and
conjugate A_ρ by a unitary of the η-form; the holonomy group Γ_x ⊂ SU(1,1) of ρ at a base vertex is defined up to conjugacy.
Definitions: ρ is BOUNDED if Γ_x has compact closure (equivalently: Γ_x fixes a point of the unit disc; equivalently: there is
a positive-definite Hermitian form h on C² with g^† h g = h for all g ∈ Γ_x, i.e. ρ is gauge-equivalent, by a GL(2,C)-valued
gauge transformation, to a U(2)-valued gauge field). ρ is RAMANUJAN if the spectrum of A_ρ is real, A_ρ is diagonalisable, and
every eigenvalue lies in [−2√q, 2√q] (there is no trivial eigenvalue q+1 unless the holonomy fixes a vector; treat that case
separately and say how). Krein sign of a real simple eigenvalue λ with eigenvector v: sign ⟨v, v⟩_η. κ(ρ) = number of real
in-band eigenvalues with negative Krein sign (counted with multiplicity where defined). The Weil (Krein) form of the page:
Q_ρ = ½ (Ω ⊗ η)(M_ρ − V_ρ) on the label space (C^n ⊗ C²)² with M_ρ = ((A_ρ, −q), (1, 0)); check the page's claim that
M_ρ^† (Ω ⊗ η) M_ρ = q (Ω ⊗ η) with the record's Ω convention and fix any sign.

## 1. The conjectures

K1 (Krein–Ramanujan rigidity). Two implications; decide each. (a) If ρ is bounded then ρ is Ramanujan iff the U(2) gauge field it is
equivalent to is Ramanujan in the usual sense (should be elementary; prove it, including what "trivial eigenvalue" means for
reducible holonomy). (b) THE CONJECTURE: if ρ is unbounded (Γ_x contains a hyperbolic or parabolic element, or is nonelementary
without a fixed point in the disc) then ρ is not Ramanujan: A_ρ has a non-real eigenvalue, or a real eigenvalue outside the band,
or a nontrivial Jordan block. Equivalently, the Ramanujan locus of SU(1,1) gauge fields is exactly the bounded locus.
Prove or refute. Known facts to use or refute with: for the cycle graph C_n (q = 1) with holonomy g the spectrum of A_ρ is
{ζ μ + (ζ μ)^{-1}: ζ^n = 1, μ an eigenvalue of g} — compute it and see that hyperbolic g gives non-real eigenvalues and parabolic
g gives Jordan blocks; this is the one-cycle case. The content of K1(b) is the general graph, where the holonomy group can be
nonelementary. Pontryagin-space facts you may need (cite Gohberg–Lancaster–Rodman, "Indefinite Linear Algebra"): an η-self-adjoint
matrix with real simple spectrum has definite Krein signs; with κ negative signs it is similar to a Hermitian matrix, but the
similarity need not be a gauge transformation (vertexwise), and that gap is where K1(b) lives. Expected route to a proof or a
counterexample: a variational argument (the top of the band as a sup over η-positive vectors fails in a Pontryagin space), or an
explicit nonelementary two-generator holonomy on K_4 (π_1 free of rank 3) that happens to have real in-band simple spectrum.

K2 (the Krein count). For bounded ρ, κ(ρ) is gauge-invariant and equals n (half the spectrum) iff ... determine: for an elliptic
U(1) ⊕ U(1)^{-1}-type holonomy (ρ equivalent to diag(e^{iφ}, e^{−iφ}) fluxes) one gets κ = n exactly; conjecture: for every
bounded ρ, κ(ρ) = n, i.e. the η-form restricted to the eigenspaces of A_ρ has signature (n, n) in every case, and for unbounded ρ
with partially real spectrum κ is a lower semicontinuous "Maslov-type" index of the holonomy: find the formula on the lollipop
graphs (one cycle with trees attached, any q) and on the theta graph (two vertices, three edges) and state the general conjecture.

K3 (RH and positivity separate, quantified). The page says RH and positivity separate for SU(1,1). Make it quantitative: on the
set of unbounded gauge fields with real in-band spectrum (if non-empty after K1!) or, if K1(b) holds, on the set of bounded ρ,
Q_ρ is positive on the band eigenspaces iff every Krein sign is positive; give the signature of Q_ρ in terms of κ and the number
of out-of-band or non-real modes. If K1(b) holds, then K3 collapses to the unitary case and you should say so and instead
quantify how the spectrum leaves the band as the holonomy becomes unbounded along a one-parameter family g_t = exp(t X), X
hyperbolic, on K_4: the first eigenvalue to go non-real, at which t, and whether it leaves through the band edge ±2√q or through
the interior (two real eigenvalues colliding inside the band and going complex = a Krein collision: this needs opposite Krein
signs, which is the mechanism to exhibit).

## 2. Numerics (checks/)

`checks/krein_scan.py`: K_4 (q = 2), the Petersen graph (q = 2), K_5 (q = 3), the cube (q = 2), the theta graph with q = 2
(multigraph: two vertices, three parallel edges). Gauge-fix on a spanning tree; the holonomy generators are one SU(1,1) element per
fundamental cycle (3, 6, 6, 5, 2 of them). Sample (i) bounded: random SU(2) conjugated into SU(1,1) by a fixed hyperbolic element
(so bounded but not obviously so), (ii) unbounded: random elements of SU(1,1) with Haar-like measure on compact parts and random
hyperbolic parts; for each sample compute the spectrum of A_ρ, test reality, in-band, diagonalisability (condition number of the
eigenvector matrix, with a stated threshold), Krein signs, κ, and the signature of Q_ρ. Report the fraction of unbounded samples
that are Ramanujan (K1(b) predicts 0; if any, print the generators to 15 digits and then verify in exact or 50-digit arithmetic
with mpmath that the spectrum is really real and in band — a false positive is worthless). Also the one-parameter family of K3.
Print everything to `checks/output_krein_scan.txt`.

## 3. Output

`astra-proofs.md`: §0 conventions and the sign check of M_ρ^†(Ω⊗η)M_ρ = q(Ω⊗η); §1 K1(a) PROVED; K1(b) PROVED / REFUTED (with the
counterexample and its certified spectrum) / SHARPENED; §2 K2 with the lollipop and theta formulas and the general conjecture; §3
K3; correction ledger; "Numerical checks for the blind lane"; "What this changes in the notebook" (candidate rows; what
`gauge-groups.md` must say about the SU(1,1) paragraph; whether "RH and positivity separate" survives as stated).
`progress.txt`: K0 (setting), K1a, K1b, K2, K3, NUM.
