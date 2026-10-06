# Partial review: `notes/adelic-gkp/window-similitude.md`, `repeated-root.md`, `tower-pairing.md`

- **Date:** 2026-10-06
- **Reviewer:** claude:fable-5.1 (the session's orchestrator; a different model from the authors, but not an independent lane: it wrote the
  briefs for these pages and the synthesis that uses them)
- **Authors under review:** claude:opus-5.5, lanes R, S, U
- **Scope:** partial. The full REFUTE review of these three pages was started by an Opus lane and stopped when TJO restricted the session to
  Fable alone. This file records the statements the orchestrator re-derived or recomputed from the statements only, in
  `notes/reviews/scratch_gkp_rsu_fable.py`, and leaves the rest unadjudicated. Nothing below promotes a status beyond what the pages say.

**Headline.** 12 statements adjudicated: 12 VALID / 0 MINOR / 0 INVALID (two by derivation from standard inputs, U-L1 and U-L2 below). Unadjudicated: lane R's edge-share numerics and its full-rank proof; lane S's
Kani–Rosen decomposition, the group-law check on $E'$, and the companion order's trace-form rank; lane U's 42 PARI comparisons and the $N=8$ separation (its pairing identities are adjudicated by derivation below).

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

## U-L1, U-L2 — the pairing identities and their well-definedness

**Claim.** $e_N(P,Q)=c(N\tilde P,\tilde Q)$ on $E[N]$ and $t_N(P,Q)=c(\tilde P,(M^k-1)\tilde Q)$ on $E(\mathbb F_{q^k})[N]\times E(\mathbb F_{q^k})$, with
$c(a,b)=e^{2\pi i\Omega(a,b)}$; the Tate formula is well defined iff $N\mid q^k-1$.

**VERDICT U-L1/L2: VALID, given three standard inputs** (the page labels them "sketched (standard inputs, from memory); checked numerically";
the derivation is short enough to record). (i) On a complex torus $\mathbb C/\Lambda$ with principal Riemann form $\Omega$ the Weil pairing on $N$-torsion
is $e_N(P,Q)=\exp(2\pi iN\Omega(\tilde P,\tilde Q))$ for lifts $\tilde P,\tilde Q\in\tfrac1N\Lambda$ (Mumford, *Abelian varieties*, from memory); this is
$c(N\tilde P,\tilde Q)$. (ii) Deligne's dictionary identifies $E[N]$ with $L/NL$, Frobenius with $M$, and the polarisation of $E$ with that of the lift
(Deligne 1969; Howe 1995 for the polarisation), so (i) is the Weil pairing of $E$. (iii) For $P\in E(\mathbb F_{q^k})[N]$, $Q\in E(\mathbb F_{q^k})$ and any $R$
with $NR=Q$, the Tate–Lichtenbaum (Frey–Rück) pairing is $t_N(P,Q)=e_N(P,\pi R-R)$ with $\pi$ the $q^k$-Frobenius (Schaefer 2005, "A new proof for
the non-degeneracy of the Frey–Rück pairing", from memory; sign conventions differ by inversion, which is the page's C10 remark). On the lattice,
$\tilde R=\tilde Q/N$ and $\pi R-R\leftrightarrow(M^k-1)\tilde Q/N$, so $e_N(P,\pi R-R)=\exp(2\pi iN\,\Omega(\tilde P,(M^k-1)\tilde Q/N))=c(\tilde P,(M^k-1)\tilde Q)$.
Well-definedness: changing $\tilde P$ by $l\in L$ changes the exponent by $\Omega(l,(M^k-1)\tilde Q)\in\mathbb Z$; changing $\tilde Q$ by $l$ changes it by
$\Omega(\tilde P,(M^k-1)l)=\Omega((V^k-1)\tilde P,l)$ (the $\Omega$-adjoint of $M$ is $V$), and with $M^k\tilde P=\tilde P+m$, $m\in L$, one has
$(V^k-1)\tilde P=(q^k-1)\tilde P-V^km$, which lies in $L$ iff $N\mid q^k-1$ when $\tilde P$ has exact order $N$ mod $L$. So the formula is well defined
exactly when $N\mid q^k-1$, as the page states. What remains numerical is only the normalisation of $\mu_N$ (the page's $\iota$), which is where the
$N=8$ separation lives; that part is not adjudicated here.

## U-C9 — one of the 42 comparisons, recomputed without the page's code

**Claim.** For E1 over $\mathbb F_{64}$ ($E(\mathbb F_{64})=\mathbb Z/56$, $N=7$) the Tate pairing agrees with $c(\tilde P,(M^6-1)\tilde Q)$ up to $\mathrm{Aut}(\mu_7)$, and the
six equivariant isomorphisms realise one coset of the squares in $(\mathbb Z/7)^\times$.

**VERDICT U-C9: VALID.** `scratch_gkp_rsu_fable_c9.py`: PARI gives $\#E(\mathbb F_{64})=56$, the 2-Frobenius acting as multiplication by $45\equiv3$ mod 7
on the cyclic group, Tate exponent 2 for $P=8g$, $Q=g$ with the root $\omega_7=g_0^{9}$; the lattice side has six fixed 7-torsion points on which $M$ acts
as multiplication by 3 (so equivariant isomorphisms exist), and the scales over the six isomorphisms are $\{1,2,4\}$, one coset of the squares (the
page reports the other coset for its own root normalisation; the claim is the coset structure, which holds).

## S-B1 — the Frobenius of $E':y^2=x^3+4x$ over $\mathbb F_5$

**Claim.** $\pi_{E'}=-1-2\iota$ with $\iota(x,y)=(-x,2y)$.

**VERDICT S-B1: VALID.** Checked by the group law in PARI on all 32 points of $E'(\mathbb F_{25})$ (31 affine plus $O$): $(x^5,y^5)=[-1]P+[-2]\iota P$ at every
point; $\#E'(\mathbb F_5)=8$, $\#E'(\mathbb F_{25})=32$, consistent with $1+2u+5u^2$.

## R-C5 — full rank for $\zeta$, rank $2g$ for a curve

**Claim.** In the critical-zero model the Toeplitz form of translates has full rank on every window for $\zeta$ and rank $2g$ for a curve.

**VERDICT R-C5: VALID as a model statement** (Carathéodory–Toeplitz, from memory): a Toeplitz form $\sum_\gamma m_\gamma e^{i\gamma(j-k)\log p}$ has
rank equal to the number of distinct atoms $\gamma\log p$ mod $2\pi$ among those with $m_\gamma>0$, once the window exceeds that number. A curve
has $2g$ atoms; $\zeta$'s atoms $\gamma\log p$ mod $2\pi$ are distinct for distinct $\gamma$ unless $(\gamma-\gamma')\log p\in2\pi\mathbb Z$, which for
the computed zeros never happens and for all zeros is the unproved assumption the page flags. So "full rank on every window" is exact for the
truncated model and conditional in general, as the page says.

## R-B6 — the frame fraction

**Claim.** For a frame of Gaussians centred at $j\delta$ with $\delta=\log2/16$ spanning a window of length $L$, the translation by $\log2$ is exact on
all but the last 16 elements, a fraction $1-\log2/L$ of the frame.

**VERDICT R-B6: VALID** (by inspection: the translation shifts the frame index by 16; only the 16 elements within $\log2$ of the window's end are
pushed out, and $16/(L/\delta)=\log2/L$).

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

Lane R: B1–B5, B7–B10, C2–C4, D1–D5 (edge-share numerics, Toeplitz digits, $\Omega_D$). Lane S: A11–A13, B2–B6, C1–C10 (Kani–Rosen, the companion order). Lane U: C1–C8, C10 (the remaining comparisons and the $N=8$ separation, which depend on the $\mu_N$ normalisation), K1. These keep the statuses
their pages give them.
