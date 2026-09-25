# Lane B1: the exact theorems and their sources

Author: `claude:opus`, 2026-09-24 (repo at `b9ab4c7`). Brief: `notes/rtp-round-1/brief.md`, section "Lane B1".
Proposed provenance rows: `notes/rtp-round-1/lane-B1-provenance-rows.tsv` (52 rows plus a header line, in the column
format of `db/provenance.tsv`). Each row was checked with the whitespace-normalised containment test of
`scripts/labbook_check.py`. Each quote also occurs exactly once in its source file. Numerical side check:
`notes/rtp-round-1/lane-B1-arch-check.py` (mpmath, deterministic).

**Line-number convention.** `labbook_check.py` numbers lines with Python `str.splitlines()`. That function also
splits at the form feeds `pdftotext` writes between pages. In every `pdftotext` file the numbers below and in the
TSV are therefore **larger than `grep -n` numbers**; for example the existing row `prov:sorensen-thm72` is 1439 by
Python and 1413 by grep. I used the Python convention throughout.

## Summary

| # | item | source status | key statement (one sentence) | surprise relative to the notes |
|---|------|---------------|------------------------------|--------------------------------|
| 1 | Bombieri 2000 | **local** `refs/src/bombieri-2000/` (bdim.eu scan with text layer) | Theorem 12: if `F` has support in an interval of length `\|I\| < log 2`, then `T[F * F(-x)-bar] >= (log(1/\|I\|) - log^+ log(1/\|I\|) - O(1)) \|\|F\|\|^2`. This is unconditional, but it gives positivity only for `\|I\|` small enough, with the `O(1)` unspecified. | Bombieri does **not** prove positivity up to `log 2`. He cites Yoshida for the `log 2` case (Yoshida's `t = (log 2)/2`). |
| 2 | Yoshida 1992 | **local** `refs/src/yoshida-1992/` (Project Euclid PDF, OCR text layer) | Theorem 1 (`k = Q`, `a = log 2 / 2`): `<phi, phi> = T_Q(phi * phi~) >= 0` for every `phi` in `K(a)` (so for every smooth `phi` supported in `[-a, a]`), with equality only for `phi = 0`. The proof is computer-assisted. | Yoshida's "local positive definiteness" (section 2) means **small support**, not archimedean or p-adic local places. Neither paper proves positivity of a local form place by place. See also the next line. |
| 1–2 | archimedean form alone | local (Connes–Consani 2020 `2006.13771`, plus my numerics) | The archimedean distribution alone is positive on support `(1/2, 2)` **only after the pole terms are removed** (Fourier transform vanishing at `+-i/2`). Its Fourier symbol `h_+(t) = -log pi + Re psi(1/4 + it/2)` is negative for `\|t\| < 6.2898`. | Notes 4.3 say positivity on short support "is a statement about the archimedean local factor alone". It is a statement about **pole plus archimedean**. The even box of width `log 2` gives archimedean part `-1.2168`, pole part `+1.4002`, total `+0.1834`. |
| 3 | Landau 1912; Gonek 1993 | Landau: **local scan** `refs/src/landau-1912/` (GDZ, tesseract OCR; formulas read from the page images). Gonek: **no local source** (AMS Contemp. Math. 143); byte-cited through Kaczorowski–Languasco–Perelli 2000 (`klp-2000`) and Ford–Zaharescu (`math/0405459`) | Landau Satz 1 (fixed `x > 1`): `sum_{0<gamma<=T} x^rho = -(T/2pi) log p + O(log T)` if `x = p^m`, and `O(log T)` otherwise. Gonek's version is uniform in `x` and `T`, with error `O(x log 2xT log log 3x) + O(log x min(T, x/<x>)) + O(log 2T min(T, 1/log x))`. | For `0 < x < 1` (Landau Satz 3) the main term is `-(T/2pi) x log p` at `x = p^{-m}`: there is an **extra factor `x`**. Landau's `O(log T)` constant depends on `x`, and Gonek's error grows linearly in `x`. Landau writes `rho = gamma + beta i`, so his `beta` is the ordinate. |
| 4 | Burg 1975; Dempster 1972; Grone–Johnson–Sá–Wolkowicz 1984 | Burg: **local scan** `refs/src/burg-1975/` (Stanford SEP, tesseract OCR). Dempster and GJSW: **no local source** (JSTOR; Elsevier refuses the proxy); byte-cited through Vandenberghe–Andersen 2015 (`vandenberghe-andersen-2015`) | Burg: the admissible next lag lies in a disc whose radii do not increase. Choosing the centre at every step (zero reflection coefficients from then on) generates the maximum-entropy spectrum, which always exists and is unique. Max-det completion: it is the maximum-entropy completion, and its inverse vanishes on the unspecified entries (the unique PD solution of `Pi_E(S^{-1}) = X`). | None for Burg: the disc-centre identification in notes 7.3 is exactly Burg's statement. The claim that for banded Toeplitz data the finite max-det completion is the AR extension is not stated in any local source. It follows from the zero-inverse property (derivation in item 4). |
| 5 | Bombieri–Lagarias 1999 | **no local source** (Elsevier refuses; OpenAlex lists no repository copy); byte-cited through Coffey (`math-ph/0505052`, already in `refs/`) | `lambda_n = -sum_{m=1}^n C(n,m) eta_{m-1} + sum_{m=2}^n (-1)^m C(n,m)(1 - 2^{-m}) zeta(m) + 1 - (n/2)(gamma + log pi + 2 log 2)`, where `zeta'/zeta(s) = -(s-1)^{-1} - sum_p eta_p (s-1)^p`. | The "Laurent coefficients at `s = 1`" are those of `zeta'/zeta` (the `eta_j`), not of `zeta`. The theorem number in BL is unverified. |
| 6 | Davis–Matiyasevich–Robinson 1976; Lagarias 2002 | Lagarias: **local** `refs/src/math/0008177/`. DMR: **no local source** (AMS PSPUM 28); statement byte-cited through Yedidia–Aaronson (`1605.04343`) | Lagarias: RH holds iff `sigma(n) <= H_n + exp(H_n) log H_n` for all `n >= 1`, with equality only at `n = 1`. DMR (as quoted by Y–A): RH holds iff `(sum_{k<=delta(n)} 1/k - n^2/2)^2 < 36 n^3` for all `n >= 1`. Y–A build a Turing machine that halts iff RH is false. | Yedidia–Aaronson attribute the `delta(n)` statement to "Lagarias", but their bibliography entry is the PSPUM 28 volume, i.e. DMR. Lagarias 2002 never says "`Pi^0_1`" (the `Pi^0_1` reading is ours), and its only DMR pointer is a commented-out TeX line. |
| 7 | Hulthén 1938; Tarski–Seidenberg | Hulthén: **no local source** (Arkiv Mat. Astr. Fys. 26A); value byte-cited through Franchini (`1609.02100`) and Sakai–Shiroishi–Nishiyama–Takahashi (`cond-mat/0302564`). Tarski–Seidenberg: **local** projection and first-order forms (Coste 2002 notes, `coste-2002`); the "defined over a real closed subfield" form has **no local source** | With `J = -1` in `H = -J sum S_n . S_{n+1}`, `E = N(1/4 - ln 2)`. Projections of semialgebraic sets are semialgebraic, and first-order definable sets are semialgebraic. | The subfield form used in finite-prime-language.md section 2 (optima are algebraic) needs quantifier elimination with coefficients in the input ring. That is in BCR and BPR, which I could not reach. It is from memory, unverified. |

## 1. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers, I*

**Source.** Rend. Mat. Acc. Lincei (9) 11 (2000) 183–233. `refs/src/bombieri-2000/paper.pdf`, the bdim.eu
digitisation (`http://www.bdim.eu/item?fmt=pdf&id=RLIN_2000_9_11_3_183_0`, free for research use). The text layer
`paper.txt` comes from `pdftotext -layout`. It turns `/` into `=` (so `(log 2)=2` means `(log 2)/2`) and drops
hats and overlines. I confirmed every formula below against the rendered pages (PDF pp. 45–46 = journal pp. 225–226).

**Exact statements.**

- Normalisation (section 12, journal p. 226): additive variable, `T[F] = int 2 cosh(x/2) F(x) dx - sum Lambda(n)
  n^{-1/2} [F(log n) + F(-log n)] - (log 4pi + gamma) F(0) - int_0^inf [...]`. The last two terms equal
  `-(log pi) F(0) + (1/2pi) int Re Gamma'/Gamma(1/4 + iv/2) F^(v) dv`.
- **Theorem 12** (`paper.txt:2649`, row `prov:bomb00-thm12`): "If `F(x)` has compact support in an interval `I` of
  length `|I| < log 2` we have `T[F(x) * F(-x)-bar] = sum_gamma F^(gamma) F^(gamma-bar)-bar >= (log(1/|I|) - log^+
  log(1/|I|) - O(1)) ||F||^2`" (formula read from p. 226).
- Proof step (`paper.txt:2660-2661`, `prov:bomb00-no-primes`): "a < log 2. Then G (x) is supported in [−a; a] ⊂ (−
  log 2; log 2). Thus in the Explicit Formula as above for T [G ], the contribution of the sum involving Λ(n)
  vanishes." The pole term is bounded in absolute value, `|int 2cosh(x/2) G| <= 4a cosh(a/2) ||F||^2` (eq. 12.6),
  and positivity comes from `Re Gamma'/Gamma(1/4 + iv/2) = log^+|v| + O(1)` (`paper.txt:2693`,
  `prov:bomb00-digamma-asymp`; the text layer shows only "( + i ) = log+ |v | + O(1);").
- Abstract (`paper.txt:51-52`, `prov:bomb00-abstract-small-t`): "prove again Yoshida’s theorem that it is positive
  definite if t is sufficiently small."
- Introduction, on Yoshida (`paper.txt:111-112`, `prov:bomb00-yoshida-log2`): "of this functional for functions
  supported in a fixed interval [−t; t ] can be reduced to a finite calculation (depending on t ), and verifies
  this positivity for t = (log 2)=2."
- On the archimedean term (`paper.txt:117-119`, `prov:bomb00-prime-at-infinity`): "It is noteworthy that the proof
  of the first result hinges on the special structure of the term for the «prime at infinity» in the Explicit
  Formula." Here "the first result" is the existence of minimisers (Theorem 3), not positivity.
- Also relevant to 7.2 (`paper.txt:54-56`, `prov:bomb00-neg-eigen`): if RH fails with only finitely many
  exceptional zeros, "the number of negative eigenvalues is precisely one-half of the number of zeros failing to
  satisfy the Riemann Hypothesis, provided the truncation is big enough."
- RH criterion: Theorem 1 (`paper.txt:544`) and Theorem 2 (`paper.txt:672-690`, `T[f * f*-bar] >= 0` on
  `C_0^inf((0, inf))`). Their formulas are garbled in the text layer; no rows proposed.

**Reading.** Bombieri proves unconditional positivity of the full Weil functional (pole plus archimedean; the prime
sum vanishes) on test functions `F` supported in an interval of length `|I|` for which `log(1/|I|) - log^+
log(1/|I|)` exceeds an unspecified constant. The hypothesis `|I| < log 2` only guarantees that no prime enters; it
is **not** the range of positivity. The lower bound grows like `log(1/|I|)`. That is a usable statement for the
learning-rate question: the minimal eigenvalue of the Weil form on support width `L` is at least `log(1/L) - log
log(1/L) - C` as `L -> 0`. Bombieri does not treat the archimedean term as positive definite by itself. He
absorbs the (indefinite) pole term with a crude bound and uses only the growth `log^+|v|` of the digamma symbol at
large `|v|`, supplied by the uncertainty principle for small support. For the notes: 4.3's attribution
"Archimedean positivity: Yoshida, Bombieri" is right about who proved short-support positivity, but the interval
`log 2` is Yoshida's, and the object is pole plus archimedean.

## 2. Yoshida, *On Hermitian forms attached to zeta functions*

**Source.** Zeta Functions in Geometry, Adv. Stud. Pure Math. 21 (1992) 281–325. `refs/src/yoshida-1992/paper.pdf`
(Project Euclid chapter PDF; the chapter URL `.../10.2969/aspm/02110281.pdf` served it with a browser UA).
`paper.txt` is `pdftotext -layout` of Project Euclid's own OCR layer: prose is fine, formulas are garbled. I read
Theorem 1 and (2.1)–(2.4) from the rendered pages (PDF pp. 8, 30).

**Exact statements.**

- Conventions: `Phi(s) = int F(x) e^{(s-1/2)x} dx`, `C(a) = {phi in C_c^inf(R) : supp phi in [-a, a]}`, and `K(a)`
  is the restrictions to `[-a, a]` of smooth `2a`-periodic functions (so `C(a)` is contained in `K(a)`), with
  `<phi_1, phi_2> = T_k(phi_1 * phi_2~)`. For `phi` in `K(a)`, `F = phi * phi~` has support in `[-2a, 2a]`.
- **Theorem 1** (`paper.txt:1740`, `prov:yosh92-thm1`: "Theorem 1. Let a= log 2/2. We have"; `paper.txt:1744`,
  `prov:yosh92-thm1-equality`: "where equality holds if and only if cp = 0."). Read from p. 310: "Let `a = log 2 /
  2`. We have `<phi, phi> = T_Q(phi * phi~) >= 0` for every `phi` in `K(a)`, where equality holds if and only if
  `phi = 0`."
- Introduction (`paper.txt:122-123`, `prov:yosh92-log2-intro`): "faithfully, when a= log 2/2: We find ( , )IK(a) is
  positive definite for a :::; log 2/2 (Theorem 1)." The OCR has `:::;` for `<=`.
- The proof is computer-assisted (`paper.txt:1690-1691`, `prov:yosh92-computer`): "every diagonal entries are
  positive at the final step. This fact can be verified rather easily on a computer." It uses a 200 x 200 matrix
  and rigorous tail bounds (6.24)–(6.27).
- Small `a` for any number field (Lemma 2; intro `paper.txt:64`, `prov:yosh92-small-a`): "is positive definite if a
  is sufficiently small." The section is titled "§2. Local positive definiteness" (`paper.txt:343`,
  `prov:yosh92-local-means-support`): **"local" means small support**.
- The digamma threshold (`paper.txt:1265`, `prov:yosh92-t0`): "We have t 0 = 2.0320 · · ·", the point where `Re
  psi(1/4 + it/2) >= 0` begins. My script reproduces 2.03205843.
- Also: Proposition 6 (if RH fails, positivity on `C(a)` and `K(a)` holds exactly for `a <= a_0`), Theorem 2 (RH
  holds iff the completed form on `K(a)` is non-degenerate for every `a`; `paper.txt:2265`), and Proposition 7 (for
  `k = Q`, non-degeneracy on `K(a)` for every `a`).

**Reading.** Yoshida proves, unconditionally and by a computer-assisted rigorous calculation, that the Weil form of
`zeta` is positive definite on all test functions `phi` supported in `[-log 2 / 2, log 2 / 2]`. In the notebook's
multiplicative coordinate that is `g` supported in `[2^{-1/2}, 2^{1/2}]`, so `f = g * g~` is supported in `[1/2,
2]`, and by translation invariance any interval of width `log 2`. On that space the prime sum vanishes, so the
theorem is about the **pole plus archimedean** form. Beyond width `log 2` nothing is proved (the prime 2 enters).
Neither Yoshida nor Bombieri discusses a p-adic local form. Yoshida's "local positivity" is small-support
positivity, so the brief's phrase "positivity of the local (archimedean and p-adic) Hermitian forms" does not
match anything in the paper.

**Is the archimedean local form positive definite on its own?** No. Sources and numbers:

- Connes–Consani 2020 (`refs/src/2006.13771/weil-compo.tex`, already fetched by `refs/fetch_sources.sh`) write
  `W_inf = -W_R` as the Fourier multiplier `h_+(tau) = -log pi + Re(Gamma'/Gamma(1/4 + i tau/2))` (line 2060,
  `prov:cc20-hplus`). The positivity they attribute to Yoshida is conditional on removing the pole (line 116,
  `prov:cc20-weil-ineq-1half-2`): "For any smooth, positive definite function $f$ with support in the interval
  $(1/2,2)$ and whose Fourier transform vanishes at $\pm \frac i2$ one has: $W_\infty(f)\geq 0$". Line 118
  (`prov:cc20-proved-by-yoshida`): "This result was proved in \cite{yoshida} by reducing it to an explicit
  computation." Line 2054 (`prov:cc20-bombieri-small`) credits Bombieri and Burnol with positivity "for test
  functions with support in a small enough interval around $1$".
- `h_+(0) = -5.3722` and `h_+ < 0` for `|tau| < 6.28984`. On unrestricted test functions the archimedean form is
  therefore indefinite.
- **Even on the short-support space it is not positive without the pole.** Take the even box `phi = (2a)^{-1/2}
  1_[-a,a]` with `a = log 2 / 2` (it lies in `K(a)`). In Yoshida's normalisation the archimedean part `-log pi +
  (1/2pi) int |phi^|^2 Re psi(1/4 + it/2) dt` equals **-1.21684**, the pole part `2|int phi e^{x/2}|^2` equals
  **+1.40023**, and the total is **+0.18338 > 0**, consistent with Theorem 1 (`lane-B1-arch-check.py`; quadrature
  to 2000 plus an asymptotic tail, stable to 5 digits between cutoffs 400 and 2000).
- For odd `phi`, Yoshida's (6.2) makes the pole part `-2|int phi e^{x/2}|^2 <= 0`. So on odd short-support
  functions the archimedean part alone is at least the positive quantity `2|int phi e^{x/2}|^2`. The failure above
  is in the even sector.

**Consequence for the notes.** In 4.3, "positivity there is a statement about the archimedean local factor alone"
should read "about the pole plus archimedean terms (Yoshida 1992, Theorem 1, width `<= log 2`; the archimedean
term alone is positive there only on the pole-free subspace, Connes–Consani 2020)". The Correction paragraph's
"pure pole-plus-archimedean" wording for mixed entries is correct. Lane A2's third decomposition ("prime terms
removed") is exactly the pole-plus-archimedean form, and Yoshida's theorem says that form is positive definite
only as long as the **differences** `x - y` of the test-function supports stay in `[-log 2, log 2]`. The
`{p, q}`-lattice families of A2 violate this, so no positivity of the mixed block is guaranteed by any source.

## 3. Landau's formula and Gonek's uniform version

**Landau source.** E. Landau, *Über die Nullstellen der Zetafunktion*, Math. Ann. 71 (1912) 548–564 (signed
"Göttingen, den 1. Juli 1911"). `refs/src/landau-1912/paper.pdf` is the GDZ image PDF
(`https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0071/LOG_0057.pdf`, no text layer; `gdz-cover.txt`
is its cover page). `img/566.jpg` to `img/582.jpg` are the page images
(`http://gdz.sub.uni-goettingen.de/content/PPN235181684_0071/1000/0/00000NNN.jpg`, `NNN` = 566..582 = journal pp.
548–564). `paper.ocr.txt` is tesseract 5.3.4 `-l deu --psm 6` over those images, pages separated by form feeds.
OCR prose is usable and formulas are not. I read the formulas below from `img/571.jpg`, `img/573.jpg` and
`img/578.jpg`.

- **Satz 1** (p. 553, restated p. 555; `paper.ocr.txt:236`, `prov:landau12-satz1`, OCR "Satz 1: Es ist bei festem
  «>1"). Read from the image: *Es ist bei festem x > 1*
  `sum_{0 < beta <= T} x^rho = -(T/2pi) log p + O(log T)` for `x = p^m`, and `O(log T)` for `x != p^m`.
  Landau writes `rho = gamma + beta i` (p. 548): **his `beta` is the imaginary part**.
- **Satz 3** (p. 560; `paper.ocr.txt:549`, `prov:landau12-satz3`, OCR "Satz 3: Bei festem x auf der Strecke O<x<1
  ist"). Read from the image: for fixed `0 < x < 1`, `sum_{0 < beta <= T} x^rho = -(T/2pi) x log p + O(log T)` for
  `x = 1/p^m`, and `O(log T)` otherwise. The proof conjugates Satz 1: `sum x^rho = x * conj(sum (1/x)^rho)`.
- Satz 2: uniformity in `x` on compact intervals of `(1, inf)` free of prime powers.

**Byte-exact secondary statements** (clean TeX):

- Ford–Zaharescu, *On the distribution of imaginary parts of zeros of the Riemann zeta function*
  (`refs/src/math/0405459/fz.tex:134-137`, `prov:fz05-landau`): "an old formula of Landau \cite{L}, which states
  that for each fixed $x>1$, ... \sum_{0<\gamma\le T} x^{\rho} = -\frac{T}{2\pi} \Lambda(x) + O(\log T)." Their
  Lemma 1 (`fz.tex:503-512`) is a uniform version "nearly identical to the proof of Theorem 1 of Gonek"
  (`fz.tex:513-514`, `prov:fz05-uniform`). Their bibliography gives Landau's pages as 548–568. The article ends on
  p. 564; the next article (von Schrutka) starts on p. 565.
- Kaczorowski–Languasco–Perelli, *A note on Landau's formula* (last preprint of Funct. Approx. Comment. Math. 28
  (2000) 173–186; `refs/src/klp-2000/paper.pdf` from `http://www.dei.unipd.it/~languasco/lavoripdf/R12.pdf`):
  `paper.txt:22` "In 1911, Landau [11] proved that for any fixed x > 1" (`prov:klp00-landau`); `paper.txt:36` "this
  direction was obtained by Gonek [4], [5]. He proved that for T > 1" (`prov:klp00-gonek`); `paper.txt:38` "+ O(x
  log 2xT log log 3x)" (`prov:klp00-gonek-error`); `paper.txt:45` "where < x > denotes the distance between x and
  the nearest prime power other that x itself." (`prov:klp00-gonek-bracket`).

**Gonek 1993.** S. M. Gonek, *An explicit formula of Landau and its applications to the theory of the
zeta-function*, in *A tribute to Emil Grosswald*, Contemp. Math. 143 (1993) 395–413 (earlier: *A formula of Landau
and mean values of zeta(s)*, Topics in Analytic Number Theory, Univ. Texas Press 1985, 92–97). **No local source**:
AMS paywall, and Gonek's Rochester pages are unreachable (404 / 503 / reset). The statement as quoted by KLP (their
(2)): for `x, T > 1`,
`sum_{0<gamma<=T} x^rho = -(T/2pi) Lambda(x) + O(x log 2xT log log 3x) + O(log x min(T, x/<x>)) + O(log 2T min(T,
1/log x))`.

**Reading.** The Correction paragraph of `metric-as-state.md` uses Landau to say that the one-place restriction
sees the distribution of `p^{-i gamma}` on the unit circle. The sources support that with three caveats. (a) For
the arguments `x = p^{-k} < 1` that occur in `P(p^{-rho})`, the drift term is `-(T/2pi) p^{-k} log p`: Satz 3's
factor `x` is present. The same factor is `p^{-k/2} * p^{-k/2}` in the symmetric normalisation `x^{rho - 1/2}`, so
the right object is `sum_gamma p^{-ik gamma} ~ -(T/2pi) p^{-k/2} log p`. (b) Landau's error term is `O_x(log T)`
with an `x`-dependent constant, so a statement about many `k` simultaneously needs Gonek. Gonek's error `O(x log(xT)
log log x)` beats the main term `T Lambda(x)/2pi` only for `T >> x log(xT) log log x / log p`, i.e. roughly `T >> k p^k
log log p^k` at `x = p^k`: the folding is visible only at heights exponentially large in `k log p`. (c) Neither formula assumes RH, so both are admissible inputs under rule
2 of the brief, but only as comparison statements about zeros; neither enters a form.

## 4. Burg's maximum-entropy extension; Dempster; Grone–Johnson–Sá–Wolkowicz

**Burg source.** J. P. Burg, *Maximum Entropy Spectral Analysis*, PhD thesis, Stanford 1975 (SEP-6). Chapter scans
are linked from `https://sep.sites.stanford.edu/publications/theses/maximum-entropy-spectral-analysis-sep-6-1975`
(Google Drive ids in the page). `refs/src/burg-1975/{abstract,ch1,ch2,ch2a,ch2b}.pdf` are image-only.
`pdftotext` gives nothing, so `*.ocr.txt` are tesseract 5.3.4 (`--psm 6`, eng) over `pdftoppm -r 300` renderings,
pages separated by form feeds. The OCR is good on prose and poor on formulas.

- Principle (`ch1.ocr.txt:34-35`, `prov:burg75-principle`): "the maximum entropy stationary time series is the
  gaussian time series whose spectrum maximizes (I-1) under the constraint equations (I-2)." Here (I-1) is `int log
  P(f) df`.
- Existence and uniqueness (`ch2a.ocr.txt:349-350`, `prov:burg75-exist-unique`): "Fourth, from the derivation, it
  is clear that the maximum entropy solution for any consistent set of constraint equations (II-2) will always
  exist". The OCR continues "and be uniaue.", sic.
- The disc (`ch2b.ocr.txt:303-304`, `prov:burg75-disc`): "the value of R(N) in the complex plane lies on or inside a
  circle of radius", namely `P_{N-1}` (the order-`(N-1)` prediction-error power) centred at `-sum_{n=1}^{N-1}
  R(N-n) b_n`, under `|c_N| <= 1` (eq. II-33).
- Radii (`ch2b.ocr.txt:312-314`, `prov:burg75-radii`): "the radii of the sequence of circles cannot t increase and
  will decrease unless the c's are zero." The stray "t" is an OCR artefact at a line start. The preceding line
  gives `P_N = P_{N-1}(1 - |c_N|^2)`.
- Centre equals MaxEnt (`ch2b.ocr.txt:337-340`, `prov:burg75-centre`): "if one extends the autocorrelation function
  to infinity by always selecting the center value for each consecutive lag value, one generates the
  autocorrelation function corresponding to the maximum entropy spectrum."
- Zero reflection coefficients (`ch2b.ocr.txt:607-609`, `prov:burg75-zero-reflection`): "infinite extension of the
  autocorrelation function corresponding to setting all the rest of the reflection coefficients to zero is
  generated by using the prediction error filter in a feedback operation." That is the AR(N) recursion (II-34),
  `sum_{n=0}^N R(m-n) a_n = 0` for `m > N`.

**Dempster 1972 and GJSW 1984.** A. P. Dempster, *Covariance selection*, Biometrics 28 (1972) 157–175 (JSTOR, not
open). R. Grone, C. R. Johnson, E. M. Sá, H. Wolkowicz, *Positive definite completions of partial Hermitian
matrices*, Linear Algebra Appl. 58 (1984) 109–124: Elsevier open archive, but ScienceDirect returns 403 to the
proxy. **No local source for either.** Byte-exact statements come from L. Vandenberghe, M. S. Andersen, *Chordal
graphs and semidefinite optimization*, Found. Trends Optim. 1 (2015) 241–433 (author copy
`https://www.seas.ucla.edu/~vandenbe/publications/chordalsdp.pdf` in `refs/src/vandenberghe-andersen-2015/`):

- `paper.txt:5035-5036` (`prov:va15-maxent-completion`): "The solution W is also called the maximum entropy
  completion of A, since it maximizes the entropy", i.e. the entropy of `N(0, W)`, with a reference to Dempster.
- `paper.txt:5066-5067` (`prov:va15-inverse-pattern`): "The two equalities show that the inverse of the maximum
  determinant completion W has sparsity pattern E." (optimality conditions (10.5): `Pi_E(W) = A`, `W > 0`, `W^{-1}
  = Y` in `S^n_E`).
- `paper.txt:5365-5366` (`prov:va15-unique`): the inverse of the max-det completion "is also the unique positive
  definite solution of the nonlinear equation" `Pi_E(S^{-1}) = X`.
- Bibliography rows `prov:va15-dempster` (`:7597`) and `prov:va15-gjsw` (`:7723-7725`). Theorem 10.1 (the chordal
  completable cone) is attributed to "[108, theorem 7]" = GJSW.
- From memory, unverified: GJSW's main theorem says every partial positive definite matrix with pattern `G` has a
  PD completion iff `G` is chordal. They also show the max-det completion is the unique completion whose inverse
  vanishes on the unspecified positions. Dym–Gohberg 1981 (*Extensions of band matrices with band inverses*, LAA
  36, 1–24; cited by V–A as [76]) is the banded case.

**Reading, and the Toeplitz step (notebook derivation, not in any local source).** Notes 7.3 say three things,
and each checks against Burg's own text. The admissible next lag is a disc, with radius Burg's `P_{K}` (in the
notebook `r_K = det W_K / det W_{K-1}`, the standard Schur-complement identity for the prediction-error power, not
byte-cited here). Its centre is the MaxEnt choice. Choosing the centre is the same as setting the next reflection
coefficient to zero. Two points go beyond Burg. (i) Burg's MaxEnt is over *stationary* extensions, i.e. spectra;
the notebook's finite window is a finite Toeplitz matrix. The link: the AR(`K`) covariance produced by Burg's
recursion on `n > K+1` points has a banded inverse (Gohberg–Semencul form; not byte-cited). By V–A's (10.5)
characterisation (`prov:va15-inverse-pattern`, `prov:va15-unique`) it is therefore the unique max-det completion of
the band. So for Toeplitz band data the finite max-det completion is automatically Toeplitz and equals Burg's
extension. (ii) For the non-Toeplitz `{p, q}`-lattice pattern of lane A2, the relevant facts are V–A's (10.5) and
uniqueness. They hold for any pattern `E`; chordality is needed only for the closed-form clique algorithm and for
existence of a PSD completion from clique-wise positivity (Theorem 10.1). Whether A2's pattern is chordal should
be checked before using the clique algorithm.

## 5. Bombieri–Lagarias 1999, the Li coefficients

**Source status.** E. Bombieri, J. C. Lagarias, *Complements to Li's criterion for the Riemann hypothesis*, J.
Number Theory 77 (1999) 274–287, doi 10.1006/jnth.1999.2392. **No local source.** ScienceDirect refuses (403),
and OpenAlex reports OA only at the publisher, with no repository copy. The statement is byte-cited from M. W.
Coffey, `refs/src/math-ph/0505052/lambda2.txt` (already in `refs/fetch_sources.sh`; hash matches
`refs/manifest.sha256`):

- `lambda2.txt:177-179` (`prov:coffey05-li-formula`): "$$\lambda_n=-\sum_{m=1}^n {n \choose m} \eta_{m-1}+\sum_{m=2}^n
  (-1)^m {n \choose m} (1-2^{-m})\zeta(m)+1-{n \over 2}(\gamma +\ln \pi + 2\ln 2), \eqno(10)$$"
- `lambda2.txt:187` (`prov:coffey05-eta`): "$${{\zeta'(s)} \over {\zeta(s)}}=-(s-1)^{-1}-\sum_{p=0}^\infty \eta_p
  (s-1)^p,"
- `lambda2.txt:220-221` (`prov:coffey05-bl-attrib`): "Equation (10) has been derived alternatively in Ref.
  \cite{bombieri} by a method connected with A. Weil's explicit formula."

Sanity check (notebook): `n = 1`, `eta_0 = -gamma` gives `lambda_1 = 1 + gamma/2 - (1/2) log 4pi = 0.0230957...`,
which matches the known value. From memory, unverified: BL state this as their Theorem 2 (the split `lambda_n =
S_inf(n) - S_0(n) + ...` into archimedean and arithmetic parts).

**Reading.** Every term except `eta_j` is archimedean or pole data: `gamma`, `log pi`, `log 2`, `zeta(m)` at even
and odd integers through `psi^{(m)}(1/2)`. The `eta_j` are the Laurent coefficients of `zeta'/zeta` at `s = 1`,
i.e. regularised moments `sum Lambda(m) log^k m / m` (Coffey eq. 11). So `lambda_n` is a finite combination of
prime data through the `eta_j`, consistent with rule 3 of the brief. The formula does not give a finite-`x`
truncation: each `eta_j` involves all primes. It is therefore not a window observable in the sense of section 4.1
without an error term.

## 6. RH as a `Pi^0_1` sentence

**Lagarias 2002** (local: `refs/src/math/0008177/main.tex`, Amer. Math. Monthly 109 (2002) 534–543).
`main.tex:101-103` (`prov:lag02-problemE`): "\sum_{d|n} d \le H_n + \exp (H_n) \log (H_n), \eeq with equality only
for $n=1$." `main.tex:118` (`prov:lag02-thm`): "Problem $E$ is equivalent to the Riemann hypothesis." Lagarias
nowhere says "`Pi^0_1`". His only pointer to Davis is a commented-out line (`main.tex:194`, `%There are a number of
other ``elementary'' versions of the Riemann hypothesis, e.g. Davis~\cite[p. 335]{Da76}.`). It is not in the
published text, so I propose no row.

**DMR 1976.** M. Davis, Y. Matijasevič, J. Robinson, *Hilbert's tenth problem. Diophantine equations: positive
aspects of a negative solution*, in *Mathematical developments arising from Hilbert problems*, Proc. Sympos. Pure
Math. 28 (AMS 1976) 323–378. **No local source** (AMS; no open copy found). Byte-exact secondary: Yedidia–Aaronson,
*A relatively small Turing machine whose behavior is independent of set theory* (`refs/src/1605.04343/`):

- `busybeaver_arxiv_version.tex:65` (`prov:ya16-rh-machine`): "We also use Laconic to design two Turing machines,
  $G$ and $R$, that halt if and only if there are counterexamples to Goldbach's Conjecture and the Riemann
  Hypothesis, respectively."
- `:293` (`prov:ya16-dmr-statement`): for all `n >= 1`, "$$\left(\left(\sum_{k \le \delta(n)} \frac{1}{k}\right) -
  \frac{n^2}{2}\right)^2 < 36n^3$$", where `delta(n) = prod_{m<n} prod_{j<=m} eta(j)` with `eta(j) = p` if `j = p^k`
  and 1 otherwise.
- `:566` (`prov:ya16-dmr-bib`): the source they cite as "Lagarias" is "\bibitem{riemann} Browder, F. ``Mathematical
  Developments Arising from Hilbert Problems.'' American Mathematical Society. Volume 28, Part 1." That is the DMR
  volume. The `delta(n)` / `36 n^3` form is, from memory, DMR's section on RH (p. 335 per Lagarias's comment).

**Reading.** Finite-prime-language.md section 5 is supported as follows. RH is equivalent to the non-halting of an
explicit Turing machine (Y–A, via DMR's statement), which is the `Pi^0_1` form. Lagarias's inequality is another
elementary equivalent. It becomes `Pi^0_1` by an extra step that is ours, not his: a strict violation `sigma(n) >
H_n + e^{H_n} log H_n` is detectable by finite-precision interval arithmetic, and the equality case is excluded
for `n > 1` by the statement itself. The attribution "Davis–Matiyasevich–Robinson 1976" is right. "Lagarias 2002"
is right for the inequality but not for a `Pi^0_1` claim. Kreisel's observation was not sourced by this lane.

## 7. Hulthén's energy; Tarski–Seidenberg

**Hulthén.** L. Hulthén, *Über das Austauschproblem eines Kristalles*, Arkiv för Matematik, Astronomi och Fysik 26A
no. 11 (1938). **No local source** (not digitised on any server I could reach). Secondary sources:

- F. Franchini, *An introduction to integrable techniques for one-dimensional quantum systems* (`refs/src/1609.02100/`):
  `Chap-XXXModel.tex:591` (`prov:franchini17-eafm`) "= N \left( {1 \over 4} - \ln 2 \right) \equiv E_{\rm AFM} \;
  ,"; `:593` (`prov:franchini17-hulthen`) "This result was originally derived by Hulthen \cite{hulthen38}."; sign
  convention `:30` (`prov:franchini17-afm-sign`) "$J >0$ favors ferromagnetic alignment, while $J<0$ gives an
  antiferromagnet." (`H = -J sum S_n . S_{n+1}`, and the AFM section sets `J = -1`, so `H = sum S_n . S_{n+1}`).
- Sakai, Shiroishi, Nishiyama, Takahashi, *Third neighbor correlators of spin-1/2 Heisenberg antiferromagnet*
  (`refs/src/cond-mat/0302564/main.tex:771-773`, `prov:ssnt03-hulthen`): `<S^z_j S^z_{j+1}> = 1/12 - (1/3) ln 2`
  "comes from the ground state energy of \eqref{Hami} derived by Hulth\'{e}n in 1938". By `SU(2)` invariance `e_0 =
  3 <S^z S^z> = 1/4 - ln 2`.

This matches finite-prime-language.md section 2 (`e_0 = 1/4 - log 2` for `H = sum S_i . S_{i+1}`).
Transcendence via Hermite–Lindemann is not sourced here.

**Tarski–Seidenberg.** M. Coste, *An introduction to semialgebraic geometry* (Oct. 2002 lecture notes;
`refs/src/coste-2002/paper.pdf` from `https://perso.univ-rennes1.fr/goulwen.fichou/RAG1.pdf`). This copy carries
handwritten annotations that appear as noise in the text layer; the theorem statements themselves are clean.
- `paper.txt:178-180` (`prov:coste02-ts-second`): "Theorem 2.3 (Tarski-Seidenberg – second form) Let A be a semialge-
  braic subset of Rn+1 and π : Rn+1 → Rn , the projection on the first n coordi- nates. Then π(A) is a
  semialgebraic subset of Rn ."
- `paper.txt:258-260` (`prov:coste02-ts-third`): the first-order-formula form.

**Not sourced (from memory, unverified).** The form used in Proposition A of finite-prime-language.md is that the
infimum of a semialgebraic function over a semialgebraic set, both defined over a real closed subfield `K` of `R`,
lies in `K`. It is in Bochnak–Coste–Roy, *Real Algebraic Geometry* (1998), chapter on the transfer principle, and
in Basu–Pollack–Roy, *Algorithms in Real Algebraic Geometry* (2nd ed. 2006), chapter 2 (quantifier elimination
with coefficients in the input ring). The BPR online copy (`perso.univ-rennes1.fr/marie-francoise.roy/bpr-ed2-
posted{1,2,3}.pdf`) now returns 404, and web.archive.org is closed by the proxy. Notebook sketch: quantifier
elimination is uniform, so `{e_d}` is defined by sign conditions on polynomials with coefficients in the ring
generated by the input coefficients. A point that is isolated in such a set is a root of one of these polynomials,
hence algebraic over `K`, hence in `K`, since `K` is real closed and the point is real.

## Sources fetched (refs/src is gitignored; recorded here for re-fetch)

| key | files | origin | sha256 of the cited text file |
|-----|-------|--------|-------------------------------|
| `bombieri-2000` | `paper.pdf`, `paper.txt` (pdftotext -layout) | bdim.eu | `a946b227c53b9c8e30f107f4e6cd1ec6b796b78f3336dbdba5da2773ce85eacb` |
| `yoshida-1992` | `paper.pdf`, `paper.txt` (pdftotext -layout of publisher OCR) | projecteuclid.org chapter PDF | `e05bd2543cdb674ed6d2ac921c68fa082c5e7cb125d3559f0cbb6aef5f81de41` |
| `landau-1912` | `paper.pdf` (images), `img/566..582.jpg`, `paper.ocr.txt` (tesseract 5.3.4 deu), `gdz-cover.txt` | GDZ Göttingen | `ecdf279615e5344602275b82fde0f81d569c269c5e098355a15640edff4f3da3` |
| `klp-2000` | `paper.pdf`, `paper.txt` | dei.unipd.it (Languasco) | `3d69c8a9c9526e7a731400a7e0087736d936cc43f3d0b822c6374f7b497b0538` |
| `math/0405459` | arXiv TeX `fz.tex` (+ pdf/txt) | arXiv | `a49cef5b6b3060645319162812e70efc499cbf8f8532e34b47b88e45ba59706b` |
| `burg-1975` | `{abstract,ch1,ch2,ch2a,ch2b}.pdf` (images), `*.ocr.txt` (tesseract 5.3.4 eng, 300 dpi) | Stanford SEP (Google Drive) | ch1 `cacf6cd2…`, ch2a `4ced44c7…`, ch2b `09ba32ca…` |
| `vandenberghe-andersen-2015` | `paper.pdf`, `paper.txt` | seas.ucla.edu | `f177c496787fc59c6e8933a2b234978b7b181290c4061e15e4155f8decca7936` |
| `math/0008177` | arXiv TeX `main.tex` (+ pdf/txt) | arXiv | `e6b14eb86b406dbfc91a11bae8b8133a9539da66e9f8e2954b3c1bf4132b30f4` |
| `1605.04343` | arXiv TeX (+ pdf/txt) | arXiv | `a295b209c94593bf8d55ce65471ea189eaa6d94e8d850d20a9bfa2a5e7bb9a39` |
| `1609.02100` | arXiv TeX (+ pdf/txt) | arXiv | `c8ad04d01e7a0657b7b07abda71216d7cfed706483820e1e51de2efdb497b201` |
| `cond-mat/0302564` | arXiv TeX (+ pdf/txt) | arXiv | `acba0d12c9de44fd6046c6d9ac472346e3f0cbd6cb23344a51ba2a7680d4a884` |
| `coste-2002` | `paper.pdf`, `paper.txt` | univ-rennes1.fr (Fichou course page) | `64b312a28bf187ca331a85940627fdb95c1900402c9552ed221887e9962d2882` |
| `2006.13771`, `math-ph/0505052` | already in `refs/fetch_sources.sh`; hashes match `refs/manifest.sha256` | arXiv | — |

The OCR files (`landau-1912`, `burg-1975`) depend on the tesseract version. Re-running OCR with another version
will move line numbers. For a durable record, commit-side hashing of the OCR text, or storing it, is the
orchestrator's call. The arXiv keys `math/0405459 math/0008177 1605.04343 1609.02100 cond-mat/0302564` can be
appended to `IDS` in `refs/fetch_sources.sh`. The non-arXiv keys need a separate fetch recipe (URLs above).

## Findings against the brief

1. **Short-support positivity (Step 3, notes 4.3).** It is unconditional and proved by Yoshida (1992, Theorem 1,
   computer-assisted) for test functions of width `<= log 2` (`a = log 2 / 2`; `f * f~` supported in `[-log 2,
   log 2]`, multiplicatively `[1/2, 2]`). Bombieri (2000, Theorem 12) reproves it only for width below an
   unspecified constant, with the quantitative bound `log(1/L) - log log(1/L) - O(1)`. The positive object is
   **pole plus archimedean**, not the archimedean local form: that form is indefinite in general (`h_+ < 0` on
   `|tau| < 6.2898`) and fails on an even width-`log 2` box (`-1.217`). It is positive on width `log 2` only on
   the pole-free subspace (Connes–Consani 2020, attributing the proof to Yoshida). No source treats p-adic local
   forms.
2. **Landau (Correction paragraph).** The sources confirm the folding on the `p`-circle, with the factor `x` for `x
   < 1` and with an `x`-dependent (Landau) or `x`-linear (Gonek) error term. The folding is visible only at heights
   `T >> k p^k log log p^k`.
3. **MaxEnt (7.3).** Burg's thesis states verbatim that the centre of each disc is the MaxEnt choice and that this
   equals zero reflection coefficients. Uniqueness and existence are stated. Dempster and GJSW are byte-cited only
   through a 2015 survey. The finite-Toeplitz identification rests on a two-line notebook derivation (banded
   inverse plus uniqueness), which REFUTE should check.
4. **Li coefficients.** The formula is byte-cited through Coffey, not from BL itself.
5. **`Pi^0_1`.** It is byte-cited through Yedidia–Aaronson, whose statement is DMR's (mislabelled "Lagarias" there).
   Lagarias 2002 gives the inequality, not the logic.
