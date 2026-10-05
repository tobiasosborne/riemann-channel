# The theta state as a GKP qunaught, and the functional equation as a gate

Author: `claude:fable-5.1`, 2026-10-05, answering TJO ("the Theta state ... could be thought of as a 'GKP' state on the rationals. It is a 'qunaught' because there is no way to find an index 2 subgroup of the rationals ... The functional equation then becomes an 'S' gate(?)"). Status: **a record, not a round.** Nothing registered; no REFUTE review. Companion to `adelic-gkp.md` §§1–3, 8; it corrects the gate name used there (the Fourier gate is the modular $S$ and the GKP Hadamard, not the GKP phase gate).

Your picture is right on all three points, with one sharpening and one naming trap.

- **Sharpening.** $\Theta$ is a qunaught because the lattice $\mathbb Q^2$ is its own symplectic complement. The absence of an index-2 subgroup is a second fact: it is why you cannot turn the qunaught into a qubit.
- **Naming trap.** The functional equation is the **Fourier gate**. That is $S$ in modular-group notation, but in GKP gate notation it is the **Hadamard**, not the phase gate $S$.

Conventions are those of `notes/adelic-gkp/adelic-gkp.md`: $W(u,v)f(x)=\psi(vx)f(x+u)$, squeeze $D_af(x)=|a|^{1/2}f(ax)$, Fourier transform $\hat f(y)=\int f(x)\psi(xy)\,dx$.

## 1. The rationals in the adeles

Yes: $\mathbb Q\subset\mathbb A$ behaves like $\mathbb Z\subset\mathbb R$ in the three ways that matter for a GKP code.

| | $\mathbb Z\subset\mathbb R$ | $\mathbb Q\subset\mathbb A$ |
|---|---|---|
| discrete | yes | yes |
| quotient compact | circle $\mathbb R/\mathbb Z$ | solenoid $\mathbb A/\mathbb Q$ |
| self-dual under the character | $\mathbb Z^\perp=\mathbb Z$ | $\mathbb Q^\perp=\mathbb Q$ |

So $\Theta=\sum_{q\in\mathbb Q}\delta_q$ is the joint $+1$ eigenvector of all $W(u,v)$ with $(u,v)\in\mathbb Q^2$, exactly as the comb $\sum_n\delta_n$ is for $\mathbb Z^2$. Like the ideal real comb it is a distribution, not a normalisable state.

## 2. Why it is a qunaught: two separate facts

**Fact 1: the code is one-dimensional because the lattice is Lagrangian.** A GKP code with stabiliser lattice $L$ has dimension $\sqrt{[L^\perp:L]}$. Here $L=\mathbb Q^2$ and $L^\perp=\mathbb Q^2$, so the dimension is one. The real square lattice $\mathbb Z^2$ is a qunaught for the same reason.

**Fact 2: you cannot repair this, because $\mathbb Q$ is divisible.** Over $\mathbb R$ one gets a qubit from the qunaught by thinning the lattice:

$$
L=\mathbb Z\times 2\mathbb Z,\qquad L^\perp=\tfrac12\mathbb Z\times\mathbb Z,\qquad [L^\perp:L]=4,\qquad \dim=2 .
$$

Over $\mathbb A$ this move does not exist. A divisible group has no proper subgroup of finite index, so $\mathbb Q^2$ has no index-2 (or index-$n$) sublattice. There is no finite superlattice either, because $\mathbb A^2/\mathbb Q^2$ is torsion-free. This is your statement, and it is Proposition 3 of the note.

A related difference: $\mathbb Z\subset\mathbb R$ has a spacing you can tune, while rescaling $\mathbb Q$ by a rational gives back $\mathbb Q$. The only deformations are squeezes by ideles that are not rational, and those lattices are again Lagrangian.

**Where the qudits went.** They reappear when you look at only some of the places. At level $N$, $\Theta$ restricts to a maximally entangled state between a real GKP qudit of dimension $N^2$ (lattice $N\mathbb Z^2$) and a qudit $\mathbb Z/N^2$ living at the finite places (Theorem 4 of the note). A Bell pair has no free logical parameter, which is the physical reason the global code is a qunaught.

## 3. The functional equation as a gate

### Which gate

| operation on phase space | modular-group name | GKP / qubit gate name |
|---|---|---|
| rotation by a quarter turn, $(u,v)\mapsto(v,-u)$: the Fourier transform | $S$ | Hadamard $H$ |
| shear, multiplication by $\psi(x^2/2)$ | $T$ | phase gate $S$ |

The functional equation is the first row. The note calls it "the S-gate" in the modular sense; read as a qubit gate that would mean the shear, which is the wrong one.

### Three facts

**(a) The code is Fourier-invariant.** Conjugating a Weyl operator by the Fourier transform $F$ gives

$$
F\,W(u,v)\,F^{-1}=\psi(-uv)\,W(v,-u).
$$

For $(u,v)\in\mathbb Q^2$ the phase is $1$ and $(v,-u)$ is again in $\mathbb Q^2$. So $F$ maps the stabiliser group to itself, and since the code is one-dimensional $F\Theta$ is a multiple of $\Theta$. The multiple is $1$: this is Poisson summation,

$$
\sum_{q\in\mathbb Q}\hat f(q)=\sum_{q\in\mathbb Q}f(q).
$$

**(b) Fourier turns a squeeze into the opposite squeeze.**

$$
F\,D_a\,F^{-1}=D_{a^{-1}} .
$$

Squeezing position by $a$ is squeezing momentum by $1/a$.

**(c) Zeta is the Mellin transform of an overlap.** Probe the code with a squeezed test state $f$ and record the overlap as a function of the squeeze, with the $q=0$ term removed:

$$
Ef(a)=|a|^{1/2}\sum_{q\ne0}f(aq),\qquad Z(f,s)=\int Ef(a)\,|a|^{s-1/2}\,d^\times a .
$$

For the product vacuum $f_0=e^{-\pi x^2}\otimes1_{\hat{\mathbb Z}}$ this is $\xi(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$.

### Putting them together

By (a) and then (b),

$$
\langle\Theta,D_af\rangle=\langle\Theta,\widehat{D_af}\rangle=\langle\Theta,D_{a^{-1}}\hat f\rangle .
$$

The overlap of $f$ at squeeze $a$ equals the overlap of $\hat f$ at squeeze $1/a$. Under the Mellin transform $a\mapsto1/a$ sends $s-\tfrac12$ to $-(s-\tfrac12)$, so

$$
Z(f,s)=Z(\hat f,1-s).
$$

The two terms dropped along the way are the zero modes, $f(0)|a|^{1/2}$ and $\hat f(0)|a|^{-1/2}$; they produce the poles at $s=0$ and $s=1$.

If the probe is itself Fourier-invariant, $\hat f_0=f_0$, the two sides are the same function and one gets $\xi(s)=\xi(1-s)$. So the functional equation of $\xi$ needs three things: the code is $H$-invariant, $H$ inverts the squeeze, and the vacuum is $H$-invariant.

### Two consistency checks from the note

- **A vacuum that is not $H$-invariant leaves a visible factor.** For $\mathbb Q(\sqrt2)$ the vacuum at the ramified prime is mapped by Fourier to a squeezed copy of itself, and that leftover squeeze is the factor $|d_K|^{s/2}$ in the completed functional equation (§14.3).
- **The phase gate is a different story.** The shear by $1$ fixes the code, since $\psi(x^2/2)=1$ on $\mathbb Q$, but it does not fix the vacuum: at the 2-adic place it multiplies $1_{\mathbb Z_2}$ by $(-1)^x$. That is why $\vartheta(\tau+1)\ne\vartheta(\tau)$ while $\vartheta(\tau+2)=\vartheta(\tau)$ (§5).

## 4. What the gate does not give

The symmetry says the squeeze spectrum is symmetric under $s\mapsto1-s$: a zero at $\rho$ comes with one at $1-\rho$. It does not say the zeros sit on the fixed line $\mathrm{Re}\,s=\tfrac12$. In the gate language the functional equation is a Clifford symmetry of code and vacuum, and RH is a positivity statement about the squeeze correlations, which no symmetry of this kind supplies.
