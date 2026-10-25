# Q3: exact short-row mean squares over F_q[t]

Author: `codex:gpt-6-astra`, 2026-10-25. Research record; no claims registered. No RH or zeros enter a family calculation.

**Verdict: PARTIAL on the requested independent H-MS proof.** The exact short-row formula, full requested tables, and Gauss/functional-equation reconstruction are established. No metaplectic proof of H-MS or counterexample is supplied. A separately labelled comparison shows that H-MS itself follows from Weil; that input is not used to claim an independent quasi-RH theorem. The missing cell is S(13,5,5)=1528527342888, checked by two routes.

## 1. Q3-1 — exact formula (PROVED); short-range estimate OPEN

Use the conventions and character embedding of Q2. Write χ_a(x)=(x/a)_6, κ for the order-six base-field character, R_a=Res(a,a′), and put χ_1(x)=1 even at x=0. All divisors below are monic. The fixed character ν is arbitrary in the identities; numerical tables retain Q2's quadratic ν of its specified irreducible cubic f.

For D≥1 and h≥0, set A_u(D)=Σ_{n monic,deg n=D}μ(n)ν(n)χ_n(u) and S(D,h)=Σ_{deg u≤h}|A_u(D)|², with all polynomials, including zero, in the outer sum. H-MS means S(D,h)≪_{q,ν,ϑ,ε}q^{(1+ε)D+h} for every fixed 0<ϑ≤1/10 and ε>0 at h=⌊(1+ϑ)D⌋.

**Correction to the question.** The diagonal formula stated there requires h≥D−1. For arbitrary h≥0 its exact value is

    Δ(D,h) = Σ_{n sf, deg n=D} |ν(n)|² Σ_{k|n} μ(k) q^{max(h−deg k+1,0)}.

The zero polynomial is included in each multiples count; inclusion–exclusion cancels it for n≠1. For h≥D−1 this simplifies to q^{h+1−D}Σ_n|ν(n)|²φ(n). In particular it is correct in the requested H-MS range, but not for every short h.

For n≠m squarefree of equal degree D, write g=(n,m), n=ga, m=gb, G=deg g, d=D−G>0. Then a,b,g are pairwise coprime and deg a=deg b=d. The primitive character of conductor ab is ρ=χ_a overline{χ_b}; the character modulo lcm(n,m)=gab has the additional unit mask 1_{(u,g)=1}. Define

    T_ab(H)=Σ_{deg w≤H} χ_a(w) overline{χ_b(w)}.

It is zero for H<0 (the only polynomial is zero, where this nonprincipal character vanishes), and for H≥2d−1 by complete-residue orthogonality. Otherwise exact finite Poisson gives

    T_ab(H)=q^{H+1−2d} G(ρ) Σ_{deg v≤2d−H−2} overline{χ_a(v)} χ_b(v).             (1)

Here e_c(x)=ψ₀([t^{-1}]x/c), G(χ)=Σ_{x mod c}χ(x)e_c(x), and ψ₀ is a fixed nontrivial additive character of F_q. Put τ_1=q^{−1/2}Σ_{c≠0}κ(c)ψ₀(c).

The dual degree cutoff in (1) is exact: for a monic modulus of degree M, products of degrees at most H and M−H−2 have degree at most M−2, so their t^{-1} coefficient after division by the modulus is zero. This gives a subspace of the annihilator of dimension M−H−1, equal to the full annihilator dimension by nondegeneracy. Finite Fourier inversion therefore has no omitted frequencies.

CRT and reciprocity give the particularly useful identity

    G(χ_a overline{χ_b})=G(χ_a) overline{G(χ_b)}.                              (2)

Indeed the CRT factor χ_a(b)overline{χ_b(a)} is κ(−1)^{d²}; conjugating G(χ_b) contributes κ(−1)^d, and d²+d is even. No resultant phase between a and b remains in (2). Hasse–Davenport as proved in Q2 gives G(χ_a)=q^{d/2}μ(a)(−τ_1)^d κ(R_a), so

    μ(a)μ(b)G(ρ)=q^d κ(R_a)overline{κ(R_b)}.                                 (3)

Consequently S=Δ+E, with the following exact finite sum (terms with H=h−deg k outside 0≤H≤2d−2 vanish):

    E = Σ_{g sf, G<D}|ν(g)|² Σ_{k|g} μ(k) q^{h−deg k+1−d}
          Σ_{a,b sf, deg a=deg b=d; (a,b)=(ab,g)=1}
             ν(a)overline{ν(b)} κ(R_a)overline{κ(R_b)} χ_a(k)overline{χ_b(k)}
          · Σ_{deg v≤2d−h+deg k−2} overline{χ_a(v)}χ_b(v).                    (4)

This is the requested Weyl-phase formula, including every common factor and zero mask. The exclusion of a=b follows automatically from (a,b)=1 and d>0. Derivation: expand the square, use 1_{(u,g)=1}=Σ_{k|g,k|u}μ(k), substitute u=kw, and apply (1)–(3). It works for prime powers q≡1 mod 6, with the usual trace in ψ₀.

**Computational factorisation (PROVED).** For fixed g,k,d and v put

    F_a(v)=ν(a)κ(R_a)χ_a(k)overline{χ_a(v)} ·1_{(a,g)=1},
    C_{g,k,d}(v)=Σ_{ell sf,deg ell≤d} μ(ell)|Σ_{a sf,deg a=d,ell|a}F_a(v)|².     (5)

Inserting Σ_{ell|(a,b)}μ(ell)=1_{(a,b)=1} shows that (4) is exactly

    E=Σ_g|ν(g)|² Σ_{k|g}μ(k)q^{h−deg k+1−d}
                   Σ_{deg v≤2d−h+deg k−2} C_{g,k,d}(v),                     (6)

with the same H restriction. This is a **signed sum of norms**, not the single positive dual norm suggested in the question. Since C(cv)=C(v) for c≠0 and C(0)=0, enumerate monic v only and multiply by q−1. At h≥D−1 the powers of q in (6) are nonnegative integers. The largest transform at (q,D,h)=(13,5,5) has monic v of degree at most 3; divisor aggregation enforces coprimality without enumerating pairs (n,m).

An exact formula does not bound the signed discriminant-family sums (5). No claim that Hasse–Davenport or Poisson alone proves H-MS is made.

## 2. Q3-2 — NUMERICAL, complete exact tables

The missing cell is evaluated by (6): **S(13,5,5)=1528527342888**, with ν=(·/(t³+t+5))₂. Its ratio to q^{D+h+1} is **117579026376/137858491849**, and D^{-1}log_q of that ratio is **−0.012407033674**. The complete pair-Poisson job (all h=5,…,10) took 112.607 seconds on twelve native Numba workers; `checks/output_13_5_poisson.txt` prints the timing and all integer intermediate shell totals. Independent reconstruction gives the same integer and took 84.706 seconds for all row degrees through 5 (`checks/output_13_reconstruct.txt`). Both are below the prescribed 20-minute budget.

At q=7 use ν=(·/(t³+t+1))₂, as in Q2. Fixing these characters is essential: there is no numerical value S(q,D,h) without specifying ν. Every nonzero polynomial is a constant times a unique monic polynomial, and χ_n(c)=κ(c)^D implies |A_{cu}(D)|=|A_u(D)|. For D>0 the zero row contributes zero. We therefore enumerate monic rows and multiply norms by q−1.

The interpretation of any finite table must respect the quantifiers. H-MS allows a constant depending on q,ν,ϑ,ε. A large value at one D, or a positive finite log ratio, does not refute it. Refutation would require an unbounded sequence for fixed permitted parameters with limsup D^{-1}log_q(S/q^{D+h})>0. Conversely, bounded small-D values do not prove it.

Define R=S/q^{D+h+1} and c_D=log_q(R)/D. The exponent for the question's normalization S/q^{D+h} is c_D+1/D. For the requested positive degrees (1≤D≤6 at q=7, and 1≤D≤5 at q=13) and D≤h≤2D, the **exact finite bounds** are

- q=7: 1692/2401 ≤ R ≤ 6/7;
- q=13: 693851640/815730721 ≤ R ≤ 12/13.

These are bounds on the computed range, not asymptotic claims. All c_D there are negative: the observed ratios are bounded and consistent with H-MS, with no observed exponential excess. The positive quantity c_D+1/D at small D does not establish growth; it includes the fixed row-count factor q.

The complete table follows. The D=0 entry uses χ_1(0)=1. Exponents are displayed to twelve decimal places; an independent 80/100-decimal-digit check verifies that rounding. Exact S and R carry the certificates.

| q | D | h | S (exact) | S/q^(D+h+1) (exact) | c_D |
|---:|---:|---:|---:|---:|---:|
| 7 | 0 | 0 | 7 | 1 | undefined |
| 7 | 1 | 0 | 54 | 54/49 | 0.049932289269 |
| 7 | 1 | 1 | 294 | 6/7 | -0.079217778838 |
| 7 | 1 | 2 | 2058 | 6/7 | -0.079217778838 |
| 7 | 2 | 0 | 24 | 24/343 | -0.683401702311 |
| 7 | 2 | 1 | 1080 | 1080/2401 | -0.205282930584 |
| 7 | 2 | 2 | 11844 | 1692/2401 | -0.089925543640 |
| 7 | 2 | 3 | 86436 | 36/49 | -0.079217778838 |
| 7 | 2 | 4 | 605052 | 36/49 | -0.079217778838 |
| 7 | 3 | 0 | 1350 | 1350/2401 | -0.098630920012 |
| 7 | 3 | 1 | 12828 | 12828/16807 | -0.046279146821 |
| 7 | 3 | 2 | 78774 | 78774/117649 | -0.068712083540 |
| 7 | 3 | 3 | 641214 | 13086/16807 | -0.042868116661 |
| 7 | 3 | 4 | 4238010 | 86490/117649 | -0.052704868410 |
| 7 | 3 | 5 | 30135294 | 87858/117649 | -0.050016653422 |
| 7 | 3 | 6 | 210947058 | 87858/117649 | -0.050016653422 |
| 7 | 4 | 0 | 20886 | 20886/16807 | 0.027915421977 |
| 7 | 4 | 1 | 94518 | 94518/117649 | -0.028125055376 |
| 7 | 4 | 2 | 568266 | 568266/823543 | -0.047667430280 |
| 7 | 4 | 3 | 4796166 | 4796166/5764801 | -0.023633386390 |
| 7 | 4 | 4 | 28877436 | 4125348/5764801 | -0.042990198542 |
| 7 | 4 | 5 | 211302504 | 4312296/5764801 | -0.037296192443 |
| 7 | 4 | 6 | 1477664580 | 4308060/5764801 | -0.037422455996 |
| 7 | 4 | 7 | 10316741652 | 613836/823543 | -0.037757135531 |
| 7 | 4 | 8 | 72217191564 | 613836/823543 | -0.037757135531 |
| 7 | 5 | 0 | 31104 | 31104/117649 | -0.136734903995 |
| 7 | 5 | 1 | 494688 | 494688/823543 | -0.052385615424 |
| 7 | 5 | 2 | 3036612 | 3036612/5764801 | -0.065884667341 |
| 7 | 5 | 3 | 33478266 | 33478266/40353607 | -0.019197631654 |
| 7 | 5 | 4 | 208944348 | 208944348/282475249 | -0.030990433319 |
| 7 | 5 | 5 | 1485729210 | 212247030/282475249 | -0.029378550759 |
| 7 | 5 | 6 | 10368010842 | 211592058/282475249 | -0.029696208382 |
| 7 | 5 | 7 | 72267596100 | 210692700/282475249 | -0.030133997599 |
| 7 | 5 | 8 | 505975512924 | 210735324/282475249 | -0.030113206952 |
| 7 | 5 | 9 | 3543059871288 | 4302216/5764801 | -0.030077482851 |
| 7 | 5 | 10 | 24801419099016 | 4302216/5764801 | -0.030077482851 |
| 7 | 6 | 0 | 232854 | 232854/823543 | -0.108193083606 |
| 7 | 6 | 1 | 4530672 | 4530672/5764801 | -0.020633049418 |
| 7 | 6 | 2 | 27465210 | 27465210/40353607 | -0.032954645145 |
| 7 | 6 | 3 | 251476158 | 251476158/282475249 | -0.009956159144 |
| 7 | 6 | 4 | 1500817896 | 1500817896/1977326743 | -0.023616676177 |
| 7 | 6 | 5 | 10555782234 | 10555782234/13841287201 | -0.023209547386 |
| 7 | 6 | 6 | 73319616510 | 10474230930/13841287201 | -0.023873824828 |
| 7 | 6 | 7 | 513274878774 | 1496428218/1977326743 | -0.023867556460 |
| 7 | 6 | 8 | 3539951729454 | 10320558978/13841287201 | -0.025139738059 |
| 7 | 6 | 9 | 24791698088682 | 10325571882/13841287201 | -0.025098146357 |
| 7 | 6 | 10 | 173565266535948 | 10326962964/13841287201 | -0.025086608230 |
| 7 | 6 | 11 | 1215016409322324 | 10327469076/13841287201 | -0.025082410743 |
| 7 | 6 | 12 | 8505114865256268 | 10327469076/13841287201 | -0.025082410743 |
| 13 | 0 | 0 | 13 | 1 | undefined |
| 13 | 1 | 0 | 300 | 300/169 | 0.223740776037 |
| 13 | 1 | 1 | 2028 | 12/13 | -0.031206350114 |
| 13 | 1 | 2 | 26364 | 12/13 | -0.031206350114 |
| 13 | 2 | 0 | 1728 | 1728/2197 | -0.046809525171 |
| 13 | 2 | 1 | 23040 | 23040/28561 | -0.041874182508 |
| 13 | 2 | 2 | 318240 | 24480/28561 | -0.030056284108 |
| 13 | 2 | 3 | 4112784 | 144/169 | -0.031206350114 |
| 13 | 2 | 4 | 53466192 | 144/169 | -0.031206350114 |
| 13 | 3 | 0 | 300 | 300/28561 | -0.592086407988 |
| 13 | 3 | 1 | 257784 | 257784/371293 | -0.047417373277 |
| 13 | 3 | 2 | 4244436 | 4244436/4826809 | -0.016709444663 |
| 13 | 3 | 3 | 54675660 | 4205820/4826809 | -0.017897209295 |
| 13 | 3 | 4 | 701860380 | 4153020/4826809 | -0.019539022078 |
| 13 | 3 | 5 | 9084428028 | 4134924/4826809 | -0.020106522797 |
| 13 | 3 | 6 | 118097564364 | 4134924/4826809 | -0.020106522797 |
| 13 | 4 | 0 | 393132 | 393132/371293 | 0.005570667979 |
| 13 | 4 | 1 | 4122156 | 4122156/4826809 | -0.015381323113 |
| 13 | 4 | 2 | 56631756 | 56631756/62748517 | -0.009996791557 |
| 13 | 4 | 3 | 721223688 | 721223688/815730721 | -0.012001695601 |
| 13 | 4 | 4 | 9020071320 | 693851640/815730721 | -0.015772839610 |
| 13 | 4 | 5 | 117876741528 | 697495512/815730721 | -0.015262311321 |
| 13 | 4 | 6 | 1534885926912 | 698628096/815730721 | -0.015104172733 |
| 13 | 4 | 7 | 19950963010992 | 53733744/62748517 | -0.015116649356 |
| 13 | 4 | 8 | 259362519142896 | 53733744/62748517 | -0.015116649356 |
| 13 | 5 | 0 | 8467200 | 8467200/4826809 | 0.043822642116 |
| 13 | 5 | 1 | 53682048 | 53682048/62748517 | -0.012168372827 |
| 13 | 5 | 2 | 703737648 | 703737648/815730721 | -0.011515133715 |
| 13 | 5 | 3 | 9378228528 | 9378228528/10604499373 | -0.009582059853 |
| 13 | 5 | 4 | 116611826592 | 116611826592/137858491849 | -0.013051099014 |
| 13 | 5 | 5 | 1528527342888 | 117579026376/137858491849 | -0.012407033674 |
| 13 | 5 | 6 | 19961541391584 | 118115629536/137858491849 | -0.012051987010 |
| 13 | 5 | 7 | 259385507232696 | 118063498968/137858491849 | -0.012086408696 |
| 13 | 5 | 8 | 3371988147043464 | 118062678024/137858491849 | -0.012086950885 |
| 13 | 5 | 9 | 43836864950451456 | 698611968/815730721 | -0.012085138262 |
| 13 | 5 | 10 | 569879244355868928 | 698611968/815730721 | -0.012085138262 |

For the requested fixed target grid ϑ∈{0,1/5,2/5,3/5,4/5,1}, the full [growth table](checks/table_growth.md) prints h=⌊(1+ϑ)D⌋, the actual h/D−1, exact R, and c_D. All 66 grid values are also printed in [output_tables.txt](checks/output_tables.txt); the table above contains every underlying cell. For the actual H-MS interval 0<ϑ≤1/10 at these degrees, h=D. In particular its terminal growth exponents are −0.023873824828 at q=7,D=6 and −0.012407033674 at q=13,D=5.

## 3. Q3-3 — PROVED reconstruction; exact implementation and audits

Here is a reconstruction that needs no RH. Let ψ be any nonprincipal primitive character of squarefree conductor F=∏P, with local exponents j_P∈{1,…,5} relative to κ, and M=deg F. Set J=Σ_P j_P deg P modulo 6, δ=1 if J=0 and δ=0 otherwise, and N=M−1−δ. Write

    L(z,ψ)=(1−z)^δ Λ(z,ψ),  Λ(z,ψ)=Σ_{j=0}^N b_j z^j.

Finite Fourier duality gives

    b_{N−j}=b_N q^{−j} overline{b_j},
    b_N=G(ψ)/T_J  (J≠0),    b_N=G(ψ)/q  (J=0),                            (7)

where T_j=Σ_{c≠0}κ(c)^j ψ₀(c). To see the leading-coefficient normalization directly, group the Gauss sum by degree and leading coefficient. For odd ψ all degrees below M−1 disappear under the constant sum; the remaining term is T_J [z^{M−1}]L. For even ψ, L(1)=0, so G(ψ)=−q[z^{M−1}]L=q b_N. The rest of (7) is the coefficient form of finite Poisson, or equivalently the usual finite-character functional equation; it does not use a root modulus.

All necessary Gauss sums have an explicit mixed-exponent evaluation:

    G(ψ)=(-1)^{M−#{P}} ∏_P T_{j_P}^{deg P}
          · κ( ∏_P Res(P,P′)^{j_P}
                ∏_{P<Q} Res(P,Q)^{j_P} Res(Q,P)^{j_Q} ).                  (8)

This follows by Hasse–Davenport on each prime and CRT. Formula (8) retains both directions of each resultant: their sign cannot be suppressed at q=7.

For the rows in the tables, reciprocity gives

    A_u(D)=κ(−1)^{D deg u} [z^D] 1/L(z, ν(·)(·/u)_6).                    (9)

Factor u, add exponent 3 at the fixed cubic prime f, and reduce exponents modulo 6 to obtain ψ. For row degree at most 5 every resulting exponent is nonzero, so the displayed character is already primitive modulo f·rad(u) with the common f counted once. An exponent zero requires an **omitted Euler factor**: reconstruct the primitive character first, then multiply L by ∏_{P excluded}(1−ψ(P)z^{deg P}). It would be incorrect merely to discard that zero mask. The implementation includes this branch for the extension over F₇ through row degree 7: it occurs in 7 monic rows of degree 6 and 42 of degree 7. The reduced numerator used for the primitive character is formed before restoring the omitted factor.

Algorithm: compute raw coefficients c_j=Σ_{monic n,deg n=j}ψ(n) only through j=⌊N/2⌋; if δ=1 take b_j=Σ_{i≤j}c_i. Evaluate b_N from (8), fill the remaining b_j using (7), restore 1−z when even, and invert the resulting polynomial by its triangular coefficient recurrence. In `shortrow_reconstruct.py`, base Gauss products are reduced **exactly** modulo Φ_{6q}; (7) then lies in Z[ζ₆], and all subsequent operations use pairs (a,b). Every division by q^j and every middle-coefficient self-duality is checked as an exact integer identity. Norms are a²+ab+b².

This is a computational acceleration, not a uniform estimate for inverse coefficients. The finite equation (7) alone puts reciprocal roots in conjugate pairs α,q/overline{α}; it does not force their absolute values.

### NUMERICAL extension beyond the request

Reconstruction supplies every row through degree 7 over F₇, including the omitted-factor branch, and pair Poisson supplies h≥8 for D=7. This gives the following entire extra degree. In particular S(7,7,7)=3620356559274, R=517193794182/678223072849 and c_D=−0.019899509456. This is a computational extension, not an asymptotic theorem. The reconstruction run took 358.572 seconds; the separate pair-Poisson run took 456.973 seconds. Their logs are [output_7_extension.txt](checks/output_7_extension.txt) and [output_7_7_poisson.txt](checks/output_7_7_poisson.txt).

| q | D | h | exact S | exact R | log_q(R)/D |
|---:|---:|---:|---:|---:|---:|
| 7 | 7 | 0 | 7194150 | 7194150/5764801 | 0.016261032798 |
| 7 | 7 | 1 | 15848166 | 15848166/40353607 | -0.068614752267 |
| 7 | 7 | 2 | 148891038 | 148891038/282475249 | -0.047012608402 |
| 7 | 7 | 3 | 1786260132 | 1786260132/1977326743 | -0.007460459000 |
| 7 | 7 | 4 | 10323605634 | 10323605634/13841287201 | -0.021526678086 |
| 7 | 7 | 5 | 74034938394 | 74034938394/96889010407 | -0.019750506588 |
| 7 | 7 | 6 | 518897812068 | 518897812068/678223072849 | -0.019658027014 |
| 7 | 7 | 7 | 3620356559274 | 517193794182/678223072849 | -0.019899509456 |
| 7 | 7 | 8 | 25138059864120 | 513021629880/678223072849 | -0.020494136835 |
| 7 | 7 | 9 | 176150061633000 | 513557031000/678223072849 | -0.020417560204 |
| 7 | 7 | 10 | 1215015069146550 | 506045426550/678223072849 | -0.021499290185 |
| 7 | 7 | 11 | 8505007732429782 | 72291372918/96889010407 | -0.021500133958 |
| 7 | 7 | 12 | 59537802794243088 | 506062973712/678223072849 | -0.021496744592 |
| 7 | 7 | 13 | 416765231030496600 | 72294816600/96889010407 | -0.021496636880 |
| 7 | 7 | 14 | 2917356617213476200 | 72294816600/96889010407 | -0.021496636880 |

The extension agrees with 39 cells of the original table, including the independently Poisson-computed D=6,h=6 and h=7 cells. The critical D=7,h=7 cell is computed by the functional equation; it has not been independently enumerated by the more expensive full pair-Poisson route at that particular h. No such limitation applies to (13,5,5), which has both routes.

## 4. Q3-4 — OPEN by the required metaplectic route; no refutation

**PARTIAL on the central request.** Equations (4)–(6) prove an exact short-row formula, not the H-MS inequality. This lane has not proved the needed uniform short-row bound without Weil, and has no asymptotic counterexample. It would be incorrect to label the numerical success an unconditional quasi-RH proof by this mechanism.

The diagonal really has the asserted order of magnitude in the H-MS range. This can be proved without RH. Put W_D=Σ_{n sf,deg n=D}|ν(n)|²φ(n), and d_P=deg P. Its generating series factors as

    Σ_D W_D z^D = H_ν(z)/(1−q²z),
    H_ν(z)=∏_P(1−z^{d_P}−q^{d_P}(q^{d_P}−1)z^{2d_P})
              /∏_{P|f}(1+(q^{d_P}−1)z^{d_P}).                           (10)

The numerator product converges absolutely for |z|<q^{−3/2}; the finite denominator has no zero there. Thus, for any fixed η∈(0,1/2),

    W_D=C_{q,f}q^{2D}+O_{q,f,η}(q^{(3/2+η)D}),
    C_{q,f}=∏_P(1−2q^{−2d_P}+q^{−3d_P})
                /∏_{P|f}(1+q^{−d_P}−q^{−2d_P}) > 0.                   (11)

For example, divide H_ν(z)−H_ν(q^{−2}) by 1−q²z and apply Cauchy's coefficient estimate on a circle strictly inside q^{−3/2}. Therefore Δ(D,h)∼C_{q,f}q^{D+h+1} uniformly in h≥D−1. Positivity of the diagonal does **not** make it a lower bound for S. The missing cell has E=−6323150808.

### The still-missing estimate

After (6) the remaining task is a uniform estimate for the signed families (5), with g, k, ell and ν retained. The number-field source uses its completed theta transformation, fixed-ray-class uniformity of the cusp sequences (Proposition 6.2 and Lemma 6.3), the quadratic sieve, and the two-Poisson transfer controlling the long cube divisors (Proposition 5.4). Neither finite Poisson nor the functional equation of an individual Dirichlet L-polynomial proves that uniform transformation/transfer bound.

This is a missing proof in this lane, **not a proof that a function-field analogue does not exist**. Hoffstein's function-field theta theory and Patterson's [Fourier-coefficient paper](https://arxiv.org/html/1411.7594) supply a framework. Patterson's [Selberg-sum paper, §5](https://arxiv.org/html/1411.7600) distinguishes metaplectic from general character twists and discusses rational generating functions and their unresolved general structure. These statements are not the uniform mean-square estimate needed here. No Katz equidistribution theorem is used; treating the remaining resultant phases as independent would be a heuristic, not a bound.

For context, the fixed-order large-sieve bounds in David–Florea–Lalín, [Theorems 1.4–1.5](https://arxiv.org/html/2506.07815v1), retain an extra q^{2(m+n)/3} term (and q^{n+m/3} for arbitrary monic rows). Substituting n=D,m=h does not give H-MS near h=D. The paper assumes q≡1 mod 2ℓ; its sextic statement directly covers q=13, not q=7 without a sign-extension argument. It is not used as an input here.

### Correct exponent of the established mechanism (PROVED)

If a volume-sized mean square is proved at h=αD+O(1), Q2's unchanged sixth-power amplifier gives

    θ(α)=max(1/2+5α/12, 1−α/6).                                         (12)

The only asymptotic volume-sized range established here without a further theorem is the inherited complete-row range h≥2D−1 (and its O(1) or o(D) variants by positivity). It gives **θ(2)=4/3**, worse than the elementary |A_1(D)|≤q^D. The effective unconditional conclusion from those two bounds is only **θ=1**. H-MS would give θ=11/12; a volume-sized bound with α<6/5 would already be needed for a nontrivial exponent from the first term in (12). The minimum of (12), even if all α were allowed, is 6/7 at α=6/7. These rational values are printed by `shortrow_certificates.py`.

### COMPARISON ONLY — the statement's truth is different from an independent metaplectic proof

There is a useful qualification to the proposed prove-or-refute dichotomy. **If Weil is admitted as a comparison theorem, H-MS for fixed q and ν follows from a uniform inverse-L bound.** This paragraph is not an input to any preceding identity, computation, or claimed non-geometric exponent.

Here is the elementary implication from the comparison theorem. Every nonzero row gives, up to a unit degree twist, a character ψ of modulus degree M≤h+deg f. For a nonprincipal ψ write

    log L(z,ψ)=Σ_{k≥1} T_k z^k/k.

The Euler product gives |T_k|≤q^k, while **Weil, used only in this comparison**, gives |T_k|≤M q^{k/2}, including the imprimitive roots of modulus one. Fix 0<a<1/2 and r=q^{−1/2−a}. Splitting at K=⌊2 log_q max(M,2)⌋ yields

    log max_{|z|=r}|1/L(z,ψ)|
        ≤Σ_{k≥1}min(q^k,Mq^{k/2})r^k/k
        ≪_{q,a} 1+M^{1−2a}.                                           (13)

Consequently

    |A_u(D)|≤q^{(1/2+a)D} exp(O_{q,a}(1+(h+deg f)^{1−2a})).              (14)

For principal rows use 1/L=(1−qz)∏_{P|m}(1−z^{deg P})^{−1}; the omitted-factor logarithm has coefficients bounded by min(q^k,M), so the same estimate, up to a fixed factor 1+q, holds. For h≤cD and fixed c, the extra exponential in (14) is q^{o(D)} uniformly in u. Choosing a smaller than ε/2 and summing the squared bound proves H-MS as a **consequence of Weil**. In fact the comparison gives the requisite mean square for every bounded h/D.

The extra factor q from the q^{h+1} rows is absorbed in the fixed-q implied constant. Thus an asymptotic counterexample with the fixed-q quantifiers of Q2 would contradict this known comparison theorem. A finite table cannot establish such a counterexample. The research question left open under the brief's restriction is an independent proof of H-MS by the metaplectic/finite-arithmetic route; invoking (13)–(14) to close that gap would violate the restriction. In the direct fixed-ν comparison, Weil already gives the stronger exponent 1/2, while the amplifier still pays its sparse-row cost.

## 5. Q3-5 — READING for the ladder and loss ledger

The family rung now has an exact, implementable description of its off-diagonal terms, including their negative contributions. The full requested finite table and the independently reconstructed missing cell strengthen the verification of that description. They supply neither a polarisation nor a uniform cancellation theorem.

Q1's loss ledger remains correct for the unchanged amplifier: the number of effective sixth-power rows costs q^{5h/6} in the square, and the deleted-prime error costs q^{2D−h/3}. The new computational acceleration removes neither loss. Before applying that ledger as a proved function-field quasi-RH argument, the independent short-row family estimate still has to be established. The exact reconstruction uses a finite functional equation, which by itself is weaker than a spectral-radius bound.

## Correction ledger

1. **REFUTED diagonal assertion for every short h.** The simplified diagonal is valid for h≥D−1, not for all h<2D−1. The smallest possible degree of failure is D=2: at q=7, ν=(·/t)₂, h=0 its actual value is 216, whereas the formula in the question gives 1548/7. `shortrow_certificates.py` enumerates it independently with FLINT. The correct formula is the inclusion–exclusion expression in §1.
2. **REFUTED proposed shortcut with the natural Gauss dual.** Let B_v=Σ_{n sf,deg n=D}ν(n)κ(R_n)overline{χ_n(v)}, which is the Möbius/Gauss dual after removing its common unit phase. For q=7,D=2,h=2, B_1=−6+2ζ₆ has norm 28, so the suggested q^{2(h+1)−2D}Σ_{deg v≤2D−h−2}|B_v|² is 8232, whereas S=11844. `shortrow_certificates.py` prints both. The correct route is (6), a signed divisor-norm sum with g and k masks. For q=13,D=5 the g=k=1 constant dual shell is −2744568, so the off-diagonal dual expression cannot itself be a nonnegative squared norm. The primitive conductor is ab; lcm(n,m) retains the common-factor mask.
3. **Normalization and quantifiers.** There are q^{h+1} rows. The requested S/q^{D+h} is q times the reported natural ratio R. The allowed implied constant depends on fixed q and ν. A single finite cell, and even a growing finite sample, cannot refute a big-O assertion. The comparison paragraph explains the stronger known truth if the prohibited input is admitted.
4. **Grid rounding.** At fixed target ϑ the implementation uses h=⌊(1+ϑ)D⌋ and prints the actual h/D−1. They coincide only at compatible degrees. For all requested D≤6 and 0<ϑ≤1/10, h=D.
5. **Reconstruction needs lower coefficients as well as Gauss sums.** A root number and functional equation do not determine an L-polynomial on their own. Equations (7)–(9) reconstruct the upper half from the lower half. Even characters require the 1−z factor, and cancelled local exponents require omitted Euler factors.
6. **No failed theta theorem has been demonstrated.** The unsupported step is the uniform transformed-family estimate and transfer, not the existence of function-field theta functions. The numerical computations do not locate a failure of Hoffstein, Patterson, or the number-field source.

## Reproducibility and verification scope

Run from this lane directory. Dependencies are the preinstalled `numpy`, `numba`, `python-flint`, `sympy`, and `mpmath`; no installation is needed. The main commands recompute, rather than sample, the indicated finite families:

```bash
python3 checks/shortrow_exact.py --audit > checks/output_audit.txt
python3 checks/shortrow_reconstruct.py --audit > checks/output_reconstruct_audit.txt
python3 checks/shortrow_exact.py --table > checks/output_tables.txt
python3 checks/shortrow_reconstruct.py --run 7 7 7 > checks/output_7_extension.txt
python3 checks/shortrow_exact.py --poisson 7 7 8 > checks/output_7_7_poisson.txt
python3 checks/shortrow_extend.py > checks/output_extension.txt
python3 checks/audit_masks.py > checks/output_masks.txt
python3 -B checks/rerun_q2.py > checks/output_q2_rerun.txt
python3 checks/shortrow_certificates.py > checks/output_certificates.txt
python3 checks/verify_outputs.py > checks/output_verification.txt
```

For the missing cell alone, `python3 checks/shortrow_exact.py --poisson 13 5 5` recomputes it and all larger h through 10; `python3 checks/shortrow_reconstruct.py --run 13 5 5` is the independent route. The `--reuse` option of the table builder explicitly reuses saved integer cells; it is not the default. The full requested table was also rerun without that option after the separate jobs.

Verification completed:

- Direct original rows and pair Poisson agree in the small audit, now including **every** short h at D≤3. The short-diagonal and negative-power-of-q branches use exact `Fraction`, with integrality checked at the end.
- Reconstruction checks full complex row coefficients against direct rows, with the q=7 reciprocity sign retained; the even-character case is included. Every functional-equation division and middle coefficient is checked exactly.
- The omitted-factor extension is independently audited on P⁶ and P⁶(P+2) using Horner evaluation of the physical rows: **228 complex coefficient comparisons**, through D=7 at q=7 and D=5 at q=13, all pass.
- The optimized resultant and Pellet signs pass **1200 independent FLINT samples for each q**, through polynomial degree 7 and including nonmonic leading coefficients. The weighted diagonals also agree with an independent Euler-product coefficient calculation through the largest computed D.
- Q2's unmodified main was executed with its output redirected into this lane, not its read-only input directory. The output is **byte-identical** to the saved Q2 output, including its exact Gauss checks. All its printed mean-square values agree with the new table.
- Integer bounds are audited before relying on `int64` inner loops; outer totals and powers use Python integers (and rational arithmetic where needed). The reported logarithms are not proof inputs; **164 displayed logarithms** agree with separate 80- and 100-decimal-digit evaluations to the stated twelve-place rounding.

The complete machine-readable union has **100 cells** in [cells_all_extended.json](checks/cells_all_extended.json). The requested table, grid, and extension are also available as [table_all.md](checks/table_all.md), [table_growth.md](checks/table_growth.md), and [table_extension.md](checks/table_extension.md).

Source map: Q2 [§1 and its checks](../../astra-2026-10-23/qrh-transpose/astra-proofs.md); Q1 [amplifier and loss ledger](../../astra-2026-10-23/qrh-digest/astra-proofs.md), especially lines 100–245 and 330–359; the supplied [11/12 text](../../astra-2026-10-23/qrh/sources/qrh-11-12-openai-2026-10-05.txt), §2, especially lines 214–236, 278–630, and theta-uniformity statements at 1519–1551. These source claims are treated as data, not as an independently certified number-field proof. The function-field framework references are Hoffstein, Invent. Math. 107 (1992), 61–86, and the two Patterson papers linked in §4. No theorem about the distribution of zeros is used in a numerical route.

## Numerical checks for the blind lane

All ν below are the Q2 cubic-conductor characters except in item 5.

1. **Every h for q=7,D=3:** for h=0,…,6,

       S = [1350, 12828, 78774, 641214, 4238010, 30135294, 210947058].

   Recompute with `python3 checks/shortrow_exact.py --poisson 7 3 0`; `--audit` checks the short values against direct rows.
2. **The missing cell:** S(13,5,5)=**1528527342888**, diagonal **1534850493696**, off-diagonal **−6323150808**. R=117579026376/137858491849 and c_D=**−0.012407033674**. Use the two independent commands in the reproduction section; the table builder prints the diagonal split.
3. **Growth at q=7,D=6,h=6:** S=**73319616510**, R=10474230930/13841287201, c_D=**−0.023873824828**. Recompute with `--poisson 7 6 6`; the degree-seven reconstruction run independently includes this cell.
4. **Extended critical cell:** S(7,7,7)=**3620356559274**, R=517193794182/678223072849, c_D=**−0.019899509456**. Use `shortrow_reconstruct.py --run 7 7 7` and `shortrow_extend.py`. The full six-target growth grids, including rounding, are printed in the table and extension outputs.
5. **Diagonal correction:** q=7, ν=(·/t)₂, D=2,h=0 gives **216**, not **1548/7**. `shortrow_certificates.py` recomputes the squarefree factors and totients with FLINT.
6. **Naive Poisson correction:** q=7,D=2,h=2 with Q2's ν has B_1=**−6+2ζ₆**, norm **28**; the proposed one-norm shortcut gives **8232**, while the actual mean square is **11844**. The same certificate script prints these exact integers.

## What this changes in the notebook

No record page or registry was edited. The following are candidate rows only; independent review is still required.

| candidate | status | scope and dependencies |
|---|---|---|
| `prop:ff-short-row-poisson` | PROVED | Equations (1)–(6), with exact diagonal for every h and all common-factor masks; finite Fourier analysis, reciprocity, Hasse–Davenport. |
| `prop:ff-weighted-diagonal-asymptotic` | PROVED | Equations (10)–(11); elementary Euler product, no RH. |
| `prop:ff-gauss-fe-reconstruction` | PROVED / NUMERICAL | Equations (7)–(9); lower-half character sums, exact mixed Gauss sums, functional equation, and omitted Euler factors. Implementation ranges and audits stated above. |
| `num:ff-short-row-tables` | NUMERICAL | All requested cells plus all h≤14 at q=7,D=7; 100 cells including D=0. The missing (13,5,5) cell agrees by two routes. |
| `cex:ff-naive-short-row-poisson` | REFUTED proposed shortcut | The explicitly defined single-Gauss-norm formula fails at (7,2,2); this is **not** a counterexample to H-MS. |
| `thm:ff-short-row-ms` | PROVED **only as a Weil-dependent comparison** | Equations (13)–(14) give H-MS for fixed q,ν and bounded h/D. Do **not** record this as a new independent metaplectic proof. |
| `prop:ff-quasi-rh-exponent` | PROVED-conditional on independent H-MS | Equation (12); 11/12 conditional, 4/3 from the established complete-row estimate, effective unconditional bound 1 after the trivial estimate. |

**No `cex:ff-short-row-ms` row is proposed.** The independent metaplectic proof remains OPEN in this lane. The comparison theorem must not be removed from the dependencies of the positive H-MS row.

Proposed annotation to [`data-ladder.md` §2](../../adelic-gkp/data-ladder.md), the family rung:

> Over F_q(t), the sextic Möbius family has an exact short-row Poisson identity with signed divisor-restricted discriminant norms. Complete finite tables, including (q,D,h)=(13,5,5), agree with the expected volume scale. The independent metaplectic short-row estimate has not been established in these lanes; conditional on it the sixth-power amplifier gives 11/12. Weil supplies a stronger, separately labelled comparison and implies this mean-square bound through uniform inverse-L estimates, but cannot be used to certify an independent transposition of the mechanism.

For Q1's loss ledger, add: “Exact Gauss evaluation and coefficient reconstruction remove computational cost, not the uniform theta/transfer estimate or the sparse-amplifier exponent loss.” For Q2, replace its missing-cell note with the value and two-route audit above, and qualify its OPEN H-MS label as referring to a proof avoiding Weil.

**Next step:** establish, with explicit fixed-character and common-factor uniformity, the function-field counterparts of source Proposition 6.2/Lemma 6.3 and Proposition 5.4; then close the cube-inversion recursion. The exact signed formula and the stored tables give regression tests for every local factor. The present work does not substitute a numerical pattern or a Weil comparison for that proof.
