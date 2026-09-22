# Certified level-one Sonine enclosure

Author: `codex:gpt-6-astra`

## Ledger

| Item | Verdict | Scope |
|---|---|---|
| S1 | PENDING | Distinct evaluator phases at the first three zeros |
| S2 | PENDING | Failure of contractivity on three evaluator modes |
| R1 | PROVED | Norm < 0.735785 < 3/4; explicit super-exponential Galerkin error |
| R2 | PENDING | Resolvent, vectors, continuation and derivative tails |
| R3 | PENDING | Scalar, kernel, normalized Gram and loss enclosures |
| R4 | PROVED (input convention) | Uniform enclosures on ordinate boxes; identification with the first three zeros is assumed from the literature as permitted |

## Correction ledger

The mandatory progress file is treated as the explicit exception to the brief's initial file restriction.

## Work in progress

Reading the binding construction and registered shard before selecting the certificate.

## R4 — Zero input convention

Author: `codex:gpt-6-astra`

Use the exact rational boxes of radius \(10^{-23}\) around
\(14.13472514173469379045725\),
\(21.02203963877155499262848\), and
\(25.01085758014568876321379\).
Every subsequent enclosure is uniform on these boxes. As expressly permitted in R4, the assertion that the first three critical-line zero ordinates belong to these boxes is accepted as literature input, in the convention of the morning lane's numerical-check item 1. This lane does not certify zeta zeros, their ordering, RH, or simplicity. Its Gram and noncontractivity statements apply to every triple of critical-line points in the boxes, whether or not they are zeros.

Two corrections already established: the loss matrix is complex Hermitian, not real symmetric; the closest displayed phases differ by about 0.0159, not more than 0.03. Neither affects the proposed certificate.


## R1 — Operator certificate and convergence

Author: `codex:gpt-6-astra`

Let \(\phi_k(x)=\sqrt{2k+1}P_k(2x-1)\), \(k\geq1\); these form an orthonormal basis of \(L^2_0(0,1)\). Write \(\Pi_N\) for its first \(N\) modes. For \(M=24,N=48\), use
\[
 C_M(x,y)=\sum_{n=0}^M c_nx^{2n}y^{2n},\qquad
 c_n=\frac{2(-1)^n(2\pi)^{2n}}{(2n)!},\qquad A=QC_MQ.
\]
It acts inside \(\Pi_N\). Its exact matrix is
\[
 A_{kl}=\sum_{n=1}^M c_n u_{nk}u_{nl},\quad
 u_{nk}=\sqrt{2k+1}\,\mu_k(2n+1),\quad
 \mu_k(s)=\frac1s\prod_{j=1}^k\frac{s-j}{s+j}.
\]
In particular \(u_{nk}=0\) for \(k>2n\), exactly. All these moments are rational times one square root; no quadrature occurs.

Taylor's integral remainder on the real interval \([0,2\pi]\) gives
\[
 \|C-C_M\|_{\infty,[0,1]^2}\leq
 \epsilon_M:=\frac{2(2\pi)^{2M+2}}{(2M+2)!}.
\]
The Hilbert–Schmidt bound and contractivity of \(Q\) imply
\(\|T-A\|_{2\to2}\leq\epsilon_M\). On mean-zero inputs also
\(\|T-A\|_{2\to\infty}\leq2\epsilon_M\) and
\(\|T\|_{2\to\infty}\leq4\).
The interval computation gives
\[
 \|A\|\leq\|A\|_F<0.735784376241750,\qquad
 \epsilon_{24}<5.332718\,10^{-25}.
\]
Consequently
\[
 \boxed{\|T\|<0.735785< t_0:=3/4},\qquad
 \boxed{\|(I-T^2)^{-1}\|\leq16/7}.
\]
This uses the Frobenius norm, not an uncertified eigenvalue computation.

For the genuine Galerkin operator \(T_N=\Pi_NT\Pi_N\), put \(m=\lfloor N/2\rfloor\). Since \(QC_mQ=\Pi_NQC_mQ\Pi_N\),
\[
 \boxed{\|T-T_N\|\leq2\epsilon_m
 =\frac{4(2\pi)^{2m+2}}{(2m+2)!}}.
\]
The same argument gives \(\|T_N-A\|\leq\epsilon_{24}\) at \(N=48\). Thus the Taylor matrix is an explicitly controlled approximation to the Legendre Galerkin matrix, and the requested super-exponential convergence is proved.
