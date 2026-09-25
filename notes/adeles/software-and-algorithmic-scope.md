# Adeles: existing software and the algorithmic scope of a first-class implementation

Discussion record, 2026-09-25 (TJO with Fable). Status: **discussion, not established.** Package names, authors and
years below are from memory and were not byte-verified against sources; verify each before relying on it. No
claim here is registered in `db/`. TJO's stated intention at the end of the discussion: consider implementing
adeles on top of FLINT or a similar library.

TJO's questions: (1) what software exists to work with the adeles, in general; (2) if one wanted `A_K` as a first-class
citizen like `Q` or `R`, are the algorithms known in the literature and just not implemented?

## 1. Existing software

**Headline.** No mainstream system has an adele ring as a data type. The one implementation known to us is Mathé
Hertogh's Sage package `adeles` (2021, with a Leiden thesis "Computing with adeles and ideles"): an adele is stored
to finite precision, the finite part as a *profinite number* known modulo an ideal, the archimedean part as a real
or complex ball. It also has ideles, computes ray class groups and Hilbert class fields through them, and does
Shimura reciprocity. Research code, one author, not in core Sage.

Everything else reaches the adeles through one of the following finite reductions, each with mature software.

| What is computed | Why it is adelic | Software |
|---|---|---|
| Completions, local fields | one place of `A_K` at a time | Sage (`Qp`, `Zp`, completions, extensions), PARI/GP, Magma (`LocalField`), Hecke.jl / OSCAR, FLINT (`padic`, `qadic`, C level), LMFDB p-adic field database (Jones–Roberts) |
| Ray class groups, class field theory | `GL_1`: the idele class group modulo an open subgroup | PARI (`bnrinit`, `bnrclassfield`), Magma, Hecke.jl (Fieker), Sage via PARI |
| Hecke Grössencharacters | characters of `A_K^x / K^x`, Tate's thesis | PARI >= 2.15 (`gcharinit`, Molin–Page, with `lfun`), Magma (`Grossencharacter`), LMFDB |
| Genera of lattices, Kneser neighbours | classes in a genus = `O(V)(F) \ O(V)(A_f) / K` | Magma, Hecke.jl (Kirschmer), Sage genus symbols (local invariants only) |
| Algebraic modular forms, Hilbert modular forms, Brandt modules | Hecke operators on the finite double cosets `G(F) \ G(A_f) / K` | Magma (Greenberg–Voight, Dembélé–Voight), Sage `BrandtModule`, PARI `alg*` for quaternion orders (Page) |
| Bruhat–Tits tree quotients, p-adic uniformisation | `Gamma \ PGL_2(Q_p) / PGL_2(Z_p)` | Sage `BruhatTitsQuotient` (Franc–Masdeu), Masdeu's `darmonpoints` |
| Local components of an automorphic representation | the factor `pi_p` of the restricted tensor product | Sage `LocalComponent` (Loeffler): principal series / special / supercuspidal at `p` for a newform |

**Formalisation.** Mathlib has the finite adele ring of a Dedekind domain and the adele ring of a number field
(de Frutos-Fernández, Mercuri), built on a restricted-product construction. Buzzard's FLT project has been formalising
local compactness and the discrete-cocompact embedding of `K` in `A_K`. The definition itself is machine-checked there;
nothing is computed.

**Function fields.** Magma and Sage have function fields, divisor class groups and class field theory (Hess, Fieker,
Lee); Sage 10 has Drinfeld modules. The adeles of a curve over `F_q` appear only implicitly, as the double-coset
description of vector bundles; no package exposes them.

**Absent everywhere.** Harmonic analysis on `A_K` or `A_K / K` as a locally compact group (Fourier transforms, Haar
integrals, Poisson summation beyond one place at a time); any numerical treatment of the archimedean and finite places
together (automorphic-form numerics, Hejhal's method, Booker–Strömbergsson, `lcalc`, live on `Gamma \ H` and use strong
approximation on paper); adelic representation theory beyond the local-component classification.

**Practical reading.** "Computing with adeles" today always means one completion, or a finite quotient of the idele
class group, or a finite double-coset set. The part that never gets computed is how the places are glued.

## 2. Algorithmic scope of a first-class `A_K`

**Answer.** Essentially every needed algorithm is known, because `A_K` is glued from three computable pieces (`K` exact;
`R`/`C` ball arithmetic; profinite ball arithmetic) and the glue is the Chinese remainder theorem. What is missing is a
precision theory (started by Hertogh) and the will to build it, since every application collapses to a finite quotient
first.

**What "first class" can mean.** `Q` is exact (equality decidable). `R` is not; the usable object is the computable real,
an approximation with an error bound (Arb's ball arithmetic). `A_K` will be like `R`, not `Q`, since a single p-adic
number already carries infinite information. Target: ball arithmetic on `A_K` plus an exact dense subring.

**Level 1, the ring.** `A_K = K + (K_infty x O-hat_K)` (constructive: CRT). An element of the profinite completion
`O-hat_K` to finite precision is a residue class `a + a O-hat_K` for an ideal `a`: a ball whose radius is an ideal.
Addition and multiplication of such balls lose precision as intervals do, with gcd (sum) of ideals in place of max of
radii: `(a + N)(b + M) = ab + (aM + bN + NM)`. Archimedean part: ordinary real/complex balls. This is what Hertogh's
package implements, with the precision-loss rules worked out in his thesis.

**The exact dense subring (the `Q` inside `A_K`).** Eventually constant adeles: a finite set of places `T`, an element
of `K` at each place of `T`, and one fixed `alpha in K` at every other place. Closed under `+` and `x`, contains `K`
diagonally and every finitely supported adele, dense in `A_K`, equality decidable (finitely many elements of `K`). We
know no name for it in the literature; it is the natural exact type, everything else being limits of it.

**Level 2, ideles and `C_K`.** An idele: finitely many arbitrary components, units elsewhere. `C_K = A_K^x / K^x` sits
in an exact sequence with the class group on one side and `(K_infty^x x O-hat_K^x) / O_K^x` on the other, so
computing in `C_K` reduces to Buchmann's class-group-and-units algorithm (subexponential, certified only under GRH).
Molin–Page's Grössencharacter code is a logarithm on `C_K` modulo its connected component. Known and implemented; the
class group is the one expensive input.

**Level 3, quotients by `K`.** Reduction into a fundamental domain for `A_K / K`: CRT on the finite part, closest-vector
reduction in the lattice `O_K subset K_infty` on the archimedean part. For `GL_n`: reduction theory, Siegel sets,
LLL over number fields (Fieker–Stehlé). Enumerating `GL_n(K) \ GL_n(A) / K_f` for open compact `K_f` is finite via
Hermite normal form and class groups. Known; implemented in the special cases of section 1.

**Level 4, harmonic analysis.** Tate's test functions are products of Schwartz functions at infinity with locally
constant compactly supported functions at the finite places. The latter are functions on a finite ring `O_K / a`, so
their Fourier transform is a finite Fourier transform, exact. At infinity, the Gaussian-times-polynomial class is
closed under Fourier transform exactly. Poisson summation over `K` becomes a theta function of the lattice `O_K`
twisted by finite data (standard numerics). Local zeta integrals: Euler factors at unramified places, Gauss-sum-type
finite computations at ramified ones; the global integral is an `L`-function (Dokchitser's method). Tate's thesis is
therefore fully algorithmic, every piece implemented somewhere, never assembled behind one type.

**Level 5, foundations nobody wrote down.** Computable analysis (Weihrauch, type-two effectivity) covers computable
metric spaces and computable locally compact groups; `A_K` is one (`Z-hat` is a computable compact metric space; Haar
measure and the Fourier transform on computable Schwartz–Bruhat functions come out computable). We know of no paper
doing this for the adeles specifically. Routine to write; the one missing piece of theory.

**Hard or impossible, and why it does not matter.**
- Equality of two computable adeles is undecidable, as for reals; so is membership in `K`.
- The connected component of `C_K` (a line, circles, solenoids) has elements that are limits of roots of units:
  computable, never exact. It carries no arithmetic information for `L`-functions, which is why Grössencharacter code
  quotients it out.
- Anything through class groups inherits GRH-conditional certification.

**Scope summary.** Ring, ideles, reduction modulo `K`, Schwartz–Bruhat Fourier analysis and Tate integrals: known,
elementary, a few thousand lines on top of an existing number-field library (Hertogh's package is the proof of concept
for the ring and idele part). Class-group-dependent parts: known, subexponential. Computable-analysis foundations:
known in general, unwritten for `A_K`. Nothing about the adeles is algorithmically mysterious; the whole object has
simply never been worth building because every application collapses to a finite quotient first.

## 3. If building on FLINT (notes for TJO's next step)

FLINT already supplies: `fmpz`/`fmpq` (exact `Z`, `Q`), `arb`/`acb` (real/complex balls), `padic`/`qadic` (one place,
capped precision), `fmpz_mod` and CRT (`fmpz_multi_CRT`), `fmpz_poly`/`fq` for residue fields, and `nf`/`nf_elem`
(number field elements, via ANTIC). Missing for `A_K`: ideals of `O_K` and their HNF arithmetic (needed for the
"ideal radius" of a profinite ball; over `Q` the radius is just an integer modulus, which makes `A_Q` a natural first
target), class groups and units (PARI or Hecke.jl territory), and the precision-loss bookkeeping of section 2 Level 1.
A minimal `A_Q` type is: `(arb x_infty, fmpz a, fmpz N)` meaning `x_infty` at infinity and the class `a + N Z-hat` at
the finite places, plus a finite list of exceptional places with `padic` components of their own precision.
