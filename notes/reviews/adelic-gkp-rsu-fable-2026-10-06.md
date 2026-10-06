# Partial review: `notes/adelic-gkp/window-similitude.md`, `repeated-root.md`, `tower-pairing.md`

- **Date:** 2026-10-06
- **Reviewer:** claude:fable-5.1 (the session's orchestrator; a different model from the authors, but not an independent lane: it wrote the
  briefs for these pages and the synthesis that uses them)
- **Authors under review:** claude:opus-5.5, lanes R, S, U
- **Scope:** partial. The full REFUTE review of these three pages was started by an Opus lane and stopped when TJO restricted the session to
  Fable alone. This file records the statements the orchestrator re-derived or recomputed from the statements only, in
  `notes/reviews/scratch_gkp_rsu_fable.py`, and leaves the rest unadjudicated. Nothing below promotes a status beyond what the pages say.

**Headline.** 7 statements adjudicated: 7 VALID / 0 MINOR / 0 INVALID. Unadjudicated: lane R's edge-share numerics and its full-rank proof; lane S's
Kani–Rosen decomposition, the group-law check on $E'$, and the companion order's trace-form rank; lane U's pairing identities beyond the dual-lattice
and intertwiner facts, and its 42 PARI comparisons.

---

## S1 — the Fermat quartic: counts and $L$-polynomial

**Claim.** $C:y^4=t^4+1$ over $\mathbb F_5$ has $\#C(\mathbb F_{5^k})=8,44,104$ for $k=1,2,3$ (four rational places at infinity), and
$L_C=(1+2u+5u^2)^2(1-2u+5u^2)$.

**VERDICT S1: VALID.** Brute-force affine counts over $\mathbb F_5$, $\mathbb F_{25}=\mathbb F_5[x]/(x^2-2)$ and $\mathbb F_{125}=\mathbb F_5[x]/(x^3+x+1)$ give
$4,40,100$; with four places at infinity, $8,44,104$; the traces of the stated $L_C$ give the same three numbers. The place count at infinity is
taken from the page (the model $y^4=t^4+1$ has $t^4+1$ of even degree with leading coefficient a fourth power, so the four points are rational).

## S3 — Connes's cokernel and multiple zeros

**Claim.** `math/9811068:main.tex:949-952` says a multiple zero gives a non-trivial Jordan form.

**VERDICT S3: VALID.** The lines read: "When the zeros of $L$ have multiplicity and $\delta$ is large enough the operator $D$ is *not* semisimple
and has a non trivial Jordan form (cf. Appendix I). This is compatible with the almost unitary condition (22) but not with skew symmetry for $D$."

## U1 — the dual lattice and the one-mode identity

**Claim.** $\Lambda_k^\perp=(1-M^k)^{-1}L$ and $(1-M^k)(1-V^k)=h_k$ for one mode.

**VERDICT U1: VALID.** Proof of the first: with $M^T\Omega M=q\Omega$ the $\Omega$-adjoint of $M$ is $\Omega^{-1}M^T\Omega=qM^{-1}=V$, so
$\Omega((1-V^k)l,x)=\Omega(l,(1-M^k)x)$ and $\Lambda_k^\perp=\{x:(1-M^k)x\in L\}$. The second: $V$ has the conjugate eigenvalues, so
$(1-M^k)(1-V^k)$ has both eigenvalues $|1-\mu^k|^2=h_k$ and is scalar. Both recomputed for E1 and the two $q=7$ lattices, $k\le6$.

## U-K3 — no unimodular intertwiner mod 8

**Claim.** Invertible $g$ mod 8 with $gM_{(1,0,6)}=M_{(2,0,3)}g$ have determinant 3 or 5, never $\pm1$.

**VERDICT U-K3: VALID.** Exhaustive search over the $8^4$ matrices: the determinant set is $\{3,5\}$.

## R-A2 — translation invariance of the zero-sum form

**Claim.** $Z(h(\cdot-t))=Z(h)$ for every $t$ in the critical-zero model.

**VERDICT R-A2: VALID.** $|\hat h(\gamma)e^{i\gamma t}|^2=|\hat h(\gamma)|^2$ termwise; numerically $1.5\times10^{-16}$ relative difference for a
narrow Gaussian packet and $t=\log2$ on 50 zeros.

## S-CM — the one-lattice check (orchestrator's own, `checks/check_cm_tower.py`)

Not a claim of the pages but their corollary: 27 of 27 (groups of every reduction of 441d1 at $p\le37$ from $\mathcal O_K$ with $\psi(\mathfrak p)$;
Tate pairing up to $\mathrm{Aut}(\mu_N)$). Recorded as consistency, not separation.

## Statements left unadjudicated

Lane R: B1–B10, C2–C5, D1–D5 (edge share, Toeplitz digits, full rank, $\Omega_D$). Lane S: A11–A13, B1–B6, C1–C10 (Kani–Rosen, $\pi_{E'}=-1-2\iota$,
the companion order). Lane U: L1–L2 (the pairing identities), C1–C10 (the 42 comparisons and the $N=8$ separation), K1. These keep the statuses
their pages give them.
