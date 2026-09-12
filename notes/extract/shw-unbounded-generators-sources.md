# Sources: Siemon–Holevo–Werner, unbounded generators of dynamical semigroups

Fetched 2026-09-12 (TJO's pointer). arXiv:1707.02266, `TORUN.tex` (688 lines),
title line `1707.02266:TORUN.tex:129` "Unbounded generators of dynamical semigroups",
authors I. Siemon, A. S. Holevo, R. F. Werner (from the TeX header). Proceedings of
"40 years of the GKLS equation", Torun 2016. Quotes below are byte-verified
(whitespace-normalised, contiguous) at `1707.02266:TORUN.tex:<lines>`.

Assessment against the notebook: `docs/worklog/2026-09-12.md`, section "Siemon–Holevo–Werner".

## no-event-def

- `1707.02266:TORUN.tex:172-172`
```
A {\bf no-event semigroup} on a Hilbert space $\HH$ is a dynamical semigroup $\semg^0_t$, $t>0$ such that every pure state $\rho=\kettbra\psi$ is mapped to a multiple of a pure state.
```

## no-event-form

- `1707.02266:TORUN.tex:173-173`
```
It is necessarily of the form $\semg^0_t\rho=C_t\rho C_t^*$ with $C_t=\exp(tK)$ a strongly continuous contraction semigroup of Hilbert space operators.
```

## standard-def

- `1707.02266:TORUN.tex:185-185`
```
A dynamical semigroup is called {\bf standard} if it is the minimal solution arising from a completely positive perturbation of the generator of a no-event semigroup.
```

## exit-space

- `1707.02266:TORUN.tex:205-206`
```
\braket{j\psi}{j\phi}=-\frac d{dt}\Bigl\langle e^{tK}\psi\Bigm\vert e^{tK}\phi\Bigr\rangle =-\bigl(\braket{K\psi}{\phi}+\braket{\psi}{K\phi}\bigr).
```

## J-isometry

- `1707.02266:TORUN.tex:213-215`
```
\norm{J\phi}^2&=&\int_0^\infty\!\!dt\ \norm{je^{tK}\phi}_\Exit^2=-\int_0^\infty\!\!dt\ \frac d{dt}\norm{e^{tK}\phi}^2\nonumber\\ &=&\norm\phi^2-\lim_{t\to\infty}\norm{e^{tK}\phi}^2 \leq\norm\phi^2
```

## reinsertion

- `1707.02266:TORUN.tex:246-246`
```
\item[(a)] Completely positive ``reinsertion'' maps $\reins:\tc(\Exit)\to\th$ with\\ $\tr\reins(\sigma)\leq\tr\sigma$.
```

## jumps-from-reinsertion

- `1707.02266:TORUN.tex:253-254`
```
Possible choices of jump operators correspond precisely to choices of Kraus operators for $\reins$ or a basis $e_\alpha\in\transit$, with $\reins(\sigma)=\sum_\alpha M_\alpha\sigma M_\alpha^*$, via $L_\alpha=M_\alpha j$
```

## shift-example

- `1707.02266:TORUN.tex:442-442`
```
A fundamental example of a contraction semigroup with unbounded generator is the half-sided shift on $\HH=\LL^2(\Rl^+,dx)$, given by
```

## shift-exit

- `1707.02266:TORUN.tex:446-446`
```
This directly determines the exit space $\Exit=\Cx$ with $j\psi=\psi(0)$.
```

## rebound

- `1707.02266:TORUN.tex:450-450`
```
The intuitive picture is that whenever the system hits the boundary, it is reset to the ``rebound'' state $\Omega$.
```

## gauge-K

- `1707.02266:TORUN.tex:378-378`
```
K'\phi&=& K\phi+\sum_\alpha\overline{\lambda_\alpha}\,L_\alpha\phi+ \frac12\Bigl(i\beta+\sum_\alpha\abs{\lambda_\alpha}^2\Bigr)\phi \label{Kgauge}
```

## gauge-proof-sign

- `1707.02266:TORUN.tex:402-402`
```
2\re\braket\phi{K'\phi}&=& 2\re\braket\phi{K\phi}-2\re\sum_\alpha\braket{\lambda_\alpha\phi}{L_\alpha\phi}-\sum_\alpha\braket{\lambda_\alpha\phi}{\lambda_\alpha\phi}\\
```

## nonstandard-def

- `1707.02266:TORUN.tex:646-646`
```
\genh\rho=\gen\rho-\tr(\gen\rho)\rhoh,\qquad\dom\genh=\dom\gen.
```

## nonstandard-key

- `1707.02266:TORUN.tex:650-650`
```
The key observation is that $\gen$ is infinitesimally trace preserving on $\dom\gen^0$, so $\ppert=\gen-\gen^0$ is already as large as it can be.
```

## arveson-units

- `1707.02266:TORUN.tex:677-677`
```
Bill Arveson \cite{ArvesonB,ArvDomAlg} calls no-event semigroups $\semg_t^0$ with this property the {\it units} of $\semg_t$.
```

## first-order

- `1707.02266:TORUN.tex:147-147`
```
Further examples are given of semigroups \cite{DaviesN,HolevoExa}, which appear to be probability preserving to first order (i.e., when looking only at the generator on the finite-rank part of its domain), but not for finite times.
```

## Remark on the gauge lemma (sign)

The displayed equation (Kgauge) at line 378 has `K' = K + sum conj(lambda) L + (1/2)(i beta + sum |lambda|^2)`,
while the dissipativity computation in the proof (line 402) uses `K' = K - sum conj(lambda) L - (1/2) sum |lambda|^2 (+ i beta/2)`.
Only the second sign leaves the generator `K rho + rho K^* + sum L rho L^*` invariant under `L -> L + lambda`
(check: the cross terms `conj(lambda) L rho + lambda rho L^* + |lambda|^2 rho` from `L' rho L'^*` must cancel against `K'`).
Read (Kgauge) with the proof's sign.

## Verification

Each quote was located by a python scan of the TeX lines with whitespace normalisation; the loci above are the minimal contiguous windows.
