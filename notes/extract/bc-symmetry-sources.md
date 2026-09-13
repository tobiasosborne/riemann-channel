# Sources for the finite BC symmetry calculation

2026-09-13. Existing local arXiv TeX sources reused; no new downloads.
The source identities below are registered in `db/provenance.tsv` and
checked by the lab-book gate after whitespace normalisation. The deductions
in `notes/bc-symmetry-generators.md` are our unreviewed arguments.

## BC finite phase state and algebra relations

Connes–Marcolli, *From Physics to Number Theory via Noncommutative Geometry.
Part I: Quantum Statistical Mechanics of Q-lattices*, math/0404128,
`houcheschapter1final7.tex`.

Lines 1824–1827 (within the stated range 0 < beta <= 1):

```tex
\varphi_{\beta} \left( e(a/b) \right) = b^{-\beta}
\prod_{p \, {\rm prime,} \, p \mid b} \left( \frac{1 - p^{\beta -
1}}{1 - p^{-1}}
\right) \, .
```

The fraction a/b here is reduced. Lines 1829–1837 give the beta > 1
extremal-state Gibbs sum, reused through the existing BC citation.

Line 1767 gives `\mu_n^*\mu_n =1`; line 1773 gives

```tex
 \mu_n\, e(r)\, \mu_n^* = \frac{1}{n} \sum_{ns=r} e(s).
```

These relations, not any approximation of the zeta zeros, give the finite
representation obstruction B0.2. The prime-level matrix extension in B1.1
is stipulated and analysed here; it is not claimed in this source.

## Bounded GKLS form and exit-space caution

Siemon–Holevo–Werner, *Unbounded generators of dynamical semigroups*,
1707.02266, `TORUN.tex:158–164`, recalls the standard bounded form. Line 160:

```tex
  \gen\rho&=&K\rho+\rho K^*+\sum_\alpha L_\alpha\rho L_\alpha^*\qquad\mbox{with}\\
```

The following line bounds the sum of jump losses by -(K+K^*). Our finite
cone uses equality, for trace preservation, and derives its conditional
Choi description explicitly. The source's unbounded-domain and
conservativity caveats remain applicable to any future adelic limit;
finite-dimensional feasibility alone is not such a limit theorem.

Primary source links: https://arxiv.org/abs/math/0404128 and
https://arxiv.org/abs/1707.02266 . Canonical uniqueness is also treated in
Frederik vom Ende, *Understanding and Generalizing Unique Decompositions
of Generators of Dynamical Semigroups*, https://arxiv.org/abs/2310.04037
(abstract consulted, not used as a premise or registered claim).
