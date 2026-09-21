# MVP-3 review and corrections

2026-09-18. Review lane; only this file and `checks/` are mine. No changes to
`plan.md` or the C implementation. All numerical results here are mpmath/PARI
approximations, not interval certificates.

**Implement the corrected distribution below. Do not implement D1 as drafted.**
It omits a factor `p^(-m/2)`. D2, D4 and the algebraic signs in D5 are correct;
D3 is supplied explicitly below. D6 is correct about poles but overstates the
unconditional applicability of the downstream construction. The rank-one
construction requires the full matrix's minimum to be even and simple.

The corrected formula gives the first 11a1 zero with error `4.10e-4` at
`x=lambda^2=13, N=60`, and `2.13e-9` at `x=30, N=120`. For 37a1 the minimum is
odd at all three tested windows `x=8,13,20`. For 389a1 it is also odd at `x=13`,
although its root number is +1. These results change both G2 and the framing of Q1.

## Formula sheet for the workers

This section is self-contained for the data builder. Use `C_E` for the
conductor and `N` for Fourier truncation; the draft uses `N` for both. All logs
are natural. Input is an integral global minimal Weierstrass model and its
conductor. The formulas for kernels below assume real `d>0, mu>0`, multiplicity
one, and `P=1`; that is the complete scope needed here.

**F1 — analytic normalization and window.** Write `L_ar(E,s)` for the usual
arithmetic L-function, with centre 1. Then

```text
L_an(E,s) = L_ar(E,s+1/2),
Lambda_an(E,s) = C_E^(s/2) Gamma_C(s+1/2) L_an(E,s),
Gamma_C(v) = 2 (2*pi)^(-v) Gamma(v),
Lambda_an(E,s) = w Lambda_an(E,1-s),
L = log x = 2 log lambda > 0,  omega_n = 2*pi*n/L.                 (F1)
```

Multiplying the completed function by an s-independent constant changes
nothing here. The completion in F1 differs from the customary arithmetic
completion by such a constant.

**F2 — the distribution means a regularized functional.** Set
`U_n(t)=L^(-1/2) exp(2*pi*i*n*t/L)` on `[0,L]`. For a test function `q` on
`[0,L]`, use the one-sided evaluation convention `delta_0(q)=q(0)`:

```text
D_E(q) = sum_{p^m<=x} w_{p,m} q(m log p)
         - integral_0^L (q(y)-q(0))/(exp(y)-1) dy
         + (s_E(L)/2) q(0).                                     (F2)
```

Thus the matrix identity shift is `s_E`, and the literal coefficient of
`delta_0` is `s_E/2`. The expression `-rho(y)` on its own is not an integrable
distribution: its subtraction convention is part of the API contract.

**F3 — paper's Loewner convention.** With `D_E` as F2,

```text
b_n = -(1/pi) D_E(sin(omega_n y)),
a_n = 2 D_E((1-y/L) cos(omega_n y)),
tau_nm = (b_n-b_m)/(n-m) if n!=m;  tau_nn = a_n,
a_{-n}=a_n, b_{-n}=-b_n, b_0=0 exactly.                           (F3)
```

These are exactly `mc2arXiv.tex:817–833`, with the basis and convolutions at
lines 352–388. In particular no factor of two is to be added to a prime atom.

**F4 — local counting (D1, H-COUNT: confirmed for minimal models).**

```text
A_p = #{(u,v) in F_p^2:
        v^2+a1*u*v+a3*v = u^3+a2*u^2+a4*u+a6},
#E_tilde(F_p)=A_p+1,   a_p=p-A_p.                                 (F4)
```

Count the singular point too. At bad primes the nonsingular projective locus
has `p-1`, `p+1`, or `p` points for split multiplicative, nonsplit
multiplicative, or additive reduction; the unique rational singular point
adds one. Hence `a_p=1,-1,0`, respectively. This works also in characteristics
2 and 3 using the **general** Weierstrass equation. Do not substitute a short
Weierstrass equation by dividing by 2 or 3. Minimality is essential for reading
the local L-factor from this singular cubic.

**F5 — corrected prime-power weights (D1: corrected; H-LUCAS: confirmed).**
For a good prime, let `t_0=2, t_1=a_p` and use the integer recurrence below.
For a bad prime use the degree-one factor, or the trivial factor when `a_p=0`:

```text
good p: t_m = a_p*t_{m-1} - p*t_{m-2} = alpha_p^m+beta_p^m,
bad p:  t_m = a_p^m,                      m>=1,
w_{p,m} = -t_m log(p)/p^m.                                      (F5)
```

Equivalently, with the draft's `c_m=t_m p^(-m/2)`, the weight is
`-c_m log(p) p^(-m/2)`, not `-c_m log(p)`. At a bad prime it is
`-(a_p/p)^m log p`, not `-a_p^m p^(-m/2) log p`.
Good/bad status can be obtained from `p|C_E`, or from the minimal discriminant.
At `p^m=x` either inclusion convention gives the same `(a,b)`, since the
window test functions vanish there. Other test functions need the usual
explicit-formula convention at jumps.

**F6 — archimedean kernel (D2: confirmed).** A gamma factor
`Q^s Gamma((s+kappa)/d)` has `mu=kappa+1/2` in these centred conventions:

```text
rho_{d,mu}(y) = exp(-mu*y)/(1-exp(-d*y))
             = sum_{k>=0} exp(-(d*k+mu)*y),
D_kernel(q) = -integral_0^L (q(y)-q(0)) rho_{d,mu}(y) dy.
E/Q: d=1, mu=1, Q=(2*pi)^(-1), coefficient -1;
zeta: d=2, mu=1/2, Q=pi^(-1/2), coefficient -1.                  (F6)
```

The coefficient is **-1, not -2**, for `Gamma_C(s+1/2)`. In particular

```text
rho_{1,1} = rho_{2,1}+rho_{2,2},
Gamma_C(s+1/2) = Gamma_R(s+1/2) Gamma_R(s+3/2),
Gamma_R(v)=pi^(-v/2) Gamma(v/2).                                 (F7)
```

The identity holds for both kernels and the complete regularized functional,
provided the constants are also combined according to F8.

**F8 — general identity shift (D3: derived).** Define the convergent tail and
the contribution of a gamma factor by

```text
T_{d,mu}(L) = integral_L^infinity rho_{d,mu}(y) dy
            = exp(-mu L)/d * sum_{k>=0} exp(-d L k)/(k+mu/d),
s_gamma(L) = 2 log Q + (2/d) psi(mu/d) + 2 T_{d,mu}(L),
s_total(L) = log C_E + sum_gamma s_gamma(L).                      (F8)
```

Here `psi=Gamma'/Gamma` and Euler's constant is `gamma_Euler=-psi(1)`.
Gamma multiplicities multiply their entire contribution. Pole terms, if
present, are separate. Conductor contributes **+log C_E** to every `a_n`.

**F9 — closed elliptic shift, ready to implement.**

```text
T_{1,1}(L) = -log(1-exp(-L)),
s_E(L) = log C_E - 2 log(2*pi) - 2 gamma_Euler
         - 2 log(1-exp(-L)).                                    (F9)
```

Use a stable `log1p`/`expm1` implementation near zero. There is no extra
root-number or rank constant.

**F10 — window-edge constants, with the same convention as zeta.** To display
the paper's regularization rather than the compact F8, use the common
reference exponent 1 and put

```text
K_{d,Q} = -log Q - psi(1/d)/d,
w_{d,Q}(L) = K_{d,Q} - T_{d,1}(L),
C_{d,mu}(L) = integral_0^L (rho_{d,mu}(y)-rho_{d,1}(y)) dy
            = [psi(1/d)-psi(mu/d)]/d - T_{d,mu}(L)+T_{d,1}(L),
s_gamma(L) = -2 [w_{d,Q}(L)+C_{d,mu}(L)].                        (F10)
```

For the elliptic factor this gives

```text
w_E(L)=gamma_Euler+log(2*pi)+log(1-exp(-L)),
C_E_window(L)=0,   s_E(L)=log C_E-2 w_E(L).                       (F11)
```

The notation `C_E_window` in F11 is a window constant, not the conductor.
For zeta F10 gives **the constants implemented in `riemann_ab.c`**:

```text
w_zeta(L) = (gamma_Euler+log(4*pi))/2
            - (1/2) log((exp(L)+1)/(exp(L)-1)),
C_zeta(L) = integral_0^L (1-exp(-y/2)) rho_{2,1/2}(y) dy
          = -log(t+1)+(1/2)log(t^2+1)+atan(t)+(1/2)log 2-pi/4,
t=exp(L/2),   s_zeta(L)=-2(w_zeta(L)+C_zeta(L)).                  (F12)
```

**F13 — general window integrals (D4: confirmed).** For integer `n>=0`, set

```text
A_n=(mu-i*omega_n)/d,  a=mu/d,  z=exp(-d L),  e=exp(-mu L),
S_r(n)=sum_{k>=0} z^k/(k+A_n)^r,  r=1,2,
S_1(0)=sum_{k>=0} z^k/(k+a).                                     (F13)
```

Then

```text
I1(n)=integral_0^L sin(omega_n y) rho(y) dy
     = -Im psi(A_n)/d - (e/d) Im S_1(n),
I2(n)=integral_0^L y cos(omega_n y) rho(y) dy
     = Re psi'(A_n)/d^2 - (e/d^2) Re S_2(n)
       - (e L/d) Re S_1(n),
I3(n)=integral_0^L (cos(omega_n y)-1) rho(y) dy
     = [psi(a)-Re psi(A_n)]/d
       - (e/d) Re S_1(n) + (e/d) S_1(0).                         (F14)
```

These use `exp(i omega_n L)=1`; they are not formulas for arbitrary real
frequencies without modified tail terms. A rigorous series remainder for
`K>=1` and real `a>0` is

```text
|sum_{k>=K} z^k/(k+A_n)^r| <= z^K / [(1-z)(K+a)^r].              (F15)
```

**F16 — assemble `(a_n,b_n)` (D5: confirmed with the specified shift).**

```text
a_n^(p) = 2 sum_{p^m<=x} w_{p,m}(1-m log(p)/L) cos(omega_n m log p),
b_n^(p) = -(1/pi) sum_{p^m<=x} w_{p,m} sin(omega_n m log p),
a_n^(R,bare) = -2 [I3(n)-I2(n)/L],
b_n^(R) = I1(n)/pi,
a_n = a_n^(p)+a_n^(R,bare)+s_E(L),
b_n = b_n^(p)+b_n^(R).                                         (F16)
```

For `n>0`, `b_n^(R)>0`; `b_0^(R)=0`. The **bare**, subtracted diagonal
`a_n^(R,bare)>0` for all `n>=0`, since it is the integral of
`2[1-(1-y/L)cos(omega_n y)]rho(y)`. Including its gamma identity shift, the
archimedean diagonal has no fixed sign: low modes can be negative and large
modes grow positively. The `-2` in F16 is essential. Individual prime weights
and the prime contribution to `b_n` need not be positive.

**F17 — no poles for E/Q (D6: confirmed).**

```text
D_E = atoms + regularized gamma kernel + (s_E/2) delta_0;
number of pole terms = 0.                                      (F17)
```

The nontrivial zeros, including the central zero with its multiplicity, are
on the spectral side. They must not be added as a new input term. Trivial
zeros cancel the gamma poles in the completion and are already accounted for
by the gamma functional. The zeta comparison uses conductor 1, F12, atoms
`-log(p)p^(-m/2)`, and additionally its rank-two pole contribution:

```text
K=32 L sinh^2(L/4),
b_n^(02)=K*n/(L^2+16*pi^2*n^2),
a_n^(02)=K*(L^2-16*pi^2*n^2)/(L^2+16*pi^2*n^2)^2.                (F18)
```

This is the sign `W_02-W_R-sum W_p` in `mc2arXiv.tex:465–492`; the pole
matrix is `w02`, lines 684–686, and the prime matrix is `bomp`, lines 693–694.

## Derivation and source audit

The paper's current line numbers differ from some old parent-plan citations.
The relevant anchors are `bombtest` 465–470, `bomp` 693–694, `w02` 684–686,
`computearch` 720–771, `bigmatrix` 794–799, `basicexpli` 817–833, `basics`
837–848, `even-simple` 850–862, and `key` 863–936, all in
[`mc2arXiv.tex`](../../../refs/src/2511.22755/mc2arXiv.tex).
The implementation anchor is `zst/src/riemann_ab.c:103–116` for `w,C`,
lines 178–196 for archimedean/prime signs, and `zst/include/zst.h:48–61` for
the even-simple and root-count contracts. Those downstream preconditions
matter here.

Here is the derivation, separate from what the paper proves. If `F(y)` is
the log-coordinate convolution test function and `q(y)=F(y)+F(-y)`, then
`q(0)=2F(0)`. Let `h(t)=integral F(y) exp(-ity)dy`. The centred explicit
formula has archimedean/conductor contribution

```text
integral_R h(t)/(2*pi) *
  [log C_E + 2 Re (G'/G)(1/2+it)] dt,
```

and arithmetic contribution
`-sum c_m(p) log(p) p^(-m/2) [F(m log p)+F(-m log p)]`.
Indeed `-L_an'/L_an(s)=sum c_m log(p) p^(-ms)`; substituting the centre
`s=1/2+it` supplies the missing factor in D1. The draft's `c_m=1` comparison
with zeta itself exposes the omission. In arithmetic notation this is just
`t_m p^(-m)` at `s_ar=1+it`. This derivation also corrects Q5, not merely D1.

For a single `G(s)=Q^s Gamma((s+kappa)/d)`, put `a=(kappa+1/2)/d`.
The absolutely convergent digamma difference identity gives

```text
Re psi(a+it/d)
  = psi(a) + integral_0^infinity
       exp(-a u)(1-cos(tu/d))/(1-exp(-u)) du.
```

Changing variable `u=d y`, multiplying by `2/d`, and Fourier-inverting gives

```text
[log Q+psi(a)/d] q(0)
   + integral_0^infinity [q(0)-q(y)] rho_{d,mu}(y) dy.
```

This is why the one-sided kernel coefficient is -1 even for `Gamma_C`.
Splitting at `L`, where `q` has support, proves F8 and F2. This repeats the
paper's passage from the gamma spectral symbol (`thetaprime`, 449–459) to the
one-sided distribution (490, note the half at 495), and its window-tail
separation (698–709). It is not a gamma-factor analogy.

For a general subtraction exponent `nu>0`, insert
`exp(-(nu-mu)y) q(0)` instead of `q(0)` and use

```text
integral_0^infinity (rho_{d,mu}-rho_{d,nu})dy
       = [psi(nu/d)-psi(mu/d)]/d.
```

Taking `nu=1` proves F10. For zeta `psi(1/2)=-gamma_Euler-2 log 2` and
`T_{2,1}=log((exp(L)+1)/(exp(L)-1))/2`, giving the required
`(gamma_Euler+log(4*pi))/2`, `w(L)`, and the exact implemented `C(L)`.
For E, `mu=nu=1`, so the analogous `C` vanishes; F9 follows immediately.
Changing regularization without also changing the shift is a bug.

F7 follows by splitting the exponential series into even and odd indices.
For the constants, digamma duplication supplies
`psi(1/2)+psi(1) = 2 psi(1)-2 log 2`; the different powers of pi then give
the same F9. Thus the kernel identity alone is a necessary but insufficient
normalization test. All three integrals and the full shift were tested.

For F14 integrate `exp(-(dk+mu)y)` against the three trigonometric weights
first, exactly as in `computearch:728–743`. The constant pieces sum to
digamma/trigamma differences, and the endpoint pieces are `S_1,S_2`.
For example each I1 summand is
`omega_n (1-exp(-(dk+mu)L))/((dk+mu)^2+omega_n^2)`, proving its sign.
The sign reversal from `W_R` to the Weil matrix is fixed by `bombtest`,
not by the signs of the special-function components.

The parent's correction to the paper is necessary: at lines 773–777 the
displayed `c(L)` lacks the factor `exp(y/2)` required by `corectc`, while
line 791 also combines two different subtraction conventions. Use the
unambiguous integral at 709 and F12; do not transcribe that display.

An entire completed L-function adds no missing `W_02` constant. The contour
explicit formula sums residues of the logarithmic derivative; E has no
completion poles. The zeta `W_02` is a genuine rank-two pole functional,
not a receptacle for an arbitrary regularization constant. The root number
disappears on logarithmic differentiation; a multiplicative normalization
constant also disappears. All remaining identity terms are F8. No GRH is
needed to derive the explicit formula; GRH enters its interpretation as a
positive sum of squares over real ordinates.

## Numerical checks and run records

`checks/ell_check.py` imports only the parent's matrix/block helpers and
zeta regression functions. It builds elliptic atoms and gamma data from this
sheet. `checks/pari_check.py` counts points independently and compares to
PARI 2.17.2. It calls `lfunzeros(..., precision=288)` explicitly: setting
PARI's decimal display precision alone leaves cypari2's function argument
at 64 bits. The committed reference strings have 85 displayed digits.
PARI's `ellap` handles bad reduction; see the
[official ellap documentation](https://pari.math.u-bordeaux.fr/dochtml/ref-stable/Elliptic_curves.html#ellap).
These reference values are not certified zero balls.

Reproduce with Python having mpmath, and a Python having cypari2:

```sh
# In notes/zeta-spectral-triples/ellcurve/checks/:
python-with-cypari2 -u pari_check.py > pari_check.out 2>&1
python3 -u ell_check.py checks > formula_check.out 2>&1
python3 -u ell_check.py spectrum 11a1 13 60 90 > 11a1_x13_N60.out 2>&1
python3 -u ell_check.py spectrum 11a1 30 120 90 > 11a1_x30_N120.out 2>&1
python3 -u ell_check.py spectrum 37a1 8 60 90 > 37a1_x8_N60.out 2>&1
# Repeat the last command with x=13 and x=20.
```

The available `python-with-cypari2` in this session was
`/tmp/claude-1000/-home-tobias-Projects-riemann-channel/d28359ce-69e4-418f-93c1-0dfdf6562319/scratchpad/venv/bin/python`.

`formula_check.out` records `(d,mu)=(1,1),(2,1/2)`, `n=1,3`, and
`L=log 8,log 13`: maximum I1/I2/I3 quadrature discrepancy `7.25e-71` at
70 dps. It also checks duplication at `n=0,1,3`, the gamma shifts, the
generic zeta `(a,b)` against `ccm_proto.py` for `n=0..4`, and six complete
elliptic matrix entries against direct regularized quadrature at both
windows. All pass the `1e-60` threshold. These are independent integral
checks of formulas, not a C/arb regression certificate.

`algebra_check.out` additionally checks the derived odd-radical identities,
its determinant formula at two nonintegral arguments, and a conductor-only
shift `log(389/11)`, at 80 dps. All pass `1e-65` residual thresholds.
The 37a1 x=13 run repeated at 110 dps agrees with the 90-dps run through
every displayed spectral digit; the next odd eigenvalue is `2.0266706031`,
well separated from `0.01247513401`.

Counting agrees with PARI for every prime <=100 on all four curves, and
also at 389. In particular:

| curve | #reduction at 2 | a_2 | #reduction at 3 | a_3 | bad-prime coefficients |
|---|---:|---:|---:|---:|---|
| 11a1 | 5 | -2 | 5 | -1 | a_11=1 |
| 14a1 | 4 | -1 | 6 | -2 | a_2=-1, a_7=1 |
| 37a1 | 5 | -2 | 7 | -3 | **a_37=-1** |
| 389a1 | 5 | -2 | 6 | -2 | a_389=1 |

The four selected curves have no additive bad prime and all are good at 3.
They cannot by themselves verify singular reduction in characteristic 3.
The supplemental minimal models `[0,0,0,-1,0]` (conductor 32) and
`[0,0,0,0,1]` (conductor 36) also pass at 2 and 3, covering additive
reduction at both small characteristics. Exact `elllocalred` outputs are
in `pari_check.out`.

For 11a1 the PARI first ordinate is
`6.36261389471308870138602900887870118712378883...`.

| curve | x | N | min E | min O | first recovered ordinate | first error |
|---|---:|---:|---:|---:|---:|---:|
| 11a1 | 13 | 60 | 7.67659737e-7 | 1.52285566e-4 | 6.363023471933060838 | 4.09577220e-4 |
| 11a1 | 13 | 120 | 7.61818824e-7 | 1.47550303e-4 | 6.363020786245678585 | 4.06891533e-4 |
| 11a1 | 30 | 120 | 1.35809060e-12 | 5.66964529e-10 | 6.362613896840406426 | 2.12731772e-9 |
| 14a1 | 13 | 60 | 5.50067278e-6 | 9.12240942e-4 | 5.580140388745325234 | 8.53571316e-4 |

At `x=13,N=60`, 11a1's first three diagonal pins are
`0.263475564589420221342554782444504628760643903576657278212798`,
`0.323518941231498047943448000320372342608549117298086397437678`,
`0.982818159686707729510521723894484890553618819654431483767631`.
The records contain corresponding `b_n` and a fourth pair to 60 digits.

The root finder searches a mesh independently of the PARI ordinates, then
refines sign changes. It searches only ordinates below 20 and makes **no
complete 2N-root claim**. Records print the nearest PARI ordinate as an error
diagnostic, not as a proof of a bijective match. For example, at `x=13,N=120`
the second and higher errors are already appreciable. G2's demand that every
zero below 20 match inside its root ball is untenable: a tight numerical ball
around an approximate spectral value does not contain the true L-zero merely
because both are accurately computed.

Two mutation records make the normalization failures concrete.
`11a1_wrong_atoms.out` uses D1 exactly as drafted: the even/odd minima become
`-0.5966540824` and `-1.0471197884`, and the first forced-even positive
ordinate is `0.9974255200`. `14a1_drop_bad.out` drops the nonzero bad-prime
atoms: even-simple still holds numerically, but the first ordinate changes
from `5.5801403887` to `4.2546661431`. A negative minimum of the unshifted
form does not by itself prevent the finite construction: subtracting the
true simple even minimum still gives the positive form required by `key`.

## Q1: what the structure says, and what the runs say

The low-confidence pre-run prediction was **H-a** for at least part of the
37a1 scan; it is recorded separately in `checks/q1-prediction.md` before
any spectral calculation. The prediction explicitly did not assert a
root-number theorem. The observations support it in all three cases.

There is a stronger structural obstruction than the draft states. Apply the
paper's Lemma `key` to `T=tau-epsilon I` only when its radical is one even
dimension and T is positive. On the quotient, the even and odd dimensions
are both N; `D''` exchanges them and is self-adjoint. Its characteristic
polynomial is even. In fact **zero is impossible at finite N under these
hypotheses**, not merely required to have even multiplicity.

To see the latter without reproving the lemma, normalize `<eta,xi>=1` as
the paper proves at lines 852–862. For an even vector v, `D'v` is odd. If
its quotient class is zero, `D'v` must be both odd and a multiple of the
even xi, hence zero. Now `D(v-xi<eta,v>)=0` says
`v-xi<eta,v>=c V_0`; pairing with eta forces c=0. The map from the even
quotient to the odd quotient is thus injective. The two spaces have the
same dimension, and self-adjointness makes the reverse map its adjoint,
also invertible. Therefore `D''` is invertible. By the determinant formula
at lines 866–869,

```text
xi_0 = product_{k=1}^N s_k^2 / (N!)^2 > 0
```

in the parent's sum normalization. This supplies a cheap necessary
even-simple consistency check. An arbitrary even vector with `xi_0=0`
has an even polynomial `det(D-s)g(s)` with a centre zero of even order, but
it cannot be the simple global minimum under the paper's hypotheses.
Do not confuse this formal cancelled-pole case with an admissible instance.
More generally, count zeros of the characteristic polynomial, including
cancelled poles, rather than raw zeros of g. The admissible example `xi=V_0`
has `g=-1/s`, yet the quotient spectrum is the 2N integers `+-1,...,+-N`.

Consequences: none of H-a/H-b/H-c is forced merely by `w=-1`. The explicit
formula supplies a real Loewner matrix regardless of root number. The
conditional even-simple theorem does not select its ground-state parity.
If even-simple persists and central zeros are approached, pairs can tend
to zero, but this cannot preserve an odd divisor multiplicity. Exact zero,
a changed 2N count, or division by `<eta,xi_odd>=0` is not an alternative
allowed by the original theorem. The normalisation also matters: decay of
the L2-normalized central coefficient does not imply the same decay after
dividing by a very small endpoint sum.

The central spectral term of multiplicity r is exactly
`r L |V_0><V_0|`, because the integral of `V_n` is zero unless n=0.
It penalizes only the even block. This explains why an odd minimum is
plausible, but gives no theorem equating its parity to w or to r modulo 2.
It also exposes a multiplicity problem in the draft: a quadratic form term
`r |fhat(0)|^2` demands vanishing of the value, not vanishing of the first
r derivatives. Rank two at the centre does not automatically create a
double zero in the minimizing transform.

For 37a1, the following are **forced-even diagnostics**, not spectra justified
by Lemma `key`. `xi_0` is from the lowest even vector, normalized to sum 1;
`s_1` is its first positive real secular root. All rows use `N=60`, 90 dps.

| x | lambda | min E | min O | xi_0 of even candidate | s_1 of even candidate |
|---:|---:|---:|---:|---:|---:|
| 8 | 2.828427 | 0.9328919852 | 0.1591847976 | -0.8103249694 | 2.083501947 |
| 13 | 3.605551 | 0.2035253240 | 0.01247513401 | -0.1179268774 | 2.152066941 |
| 20 | 4.472136 | 0.02540719415 | 0.0007792425293 | -0.02868414523 | 2.411641959 |

The true minimal eigenvector is odd, so its `xi_0=0` exactly and its sum
normalization is undefined. The paper's `s_1` is therefore **not defined**
for these global minima. The even candidate has an imaginary central pair;
the updated run records solve for it explicitly. Its first positive real
root is not a shrinking pair about zero. Reporting these roots as certified
CCM spectral values would be wrong even if the scalar root solver certified
them perfectly.
The imaginary pairs are `s=+-0.6773050738 i`, `+-0.2142662393 i`, and
`+-0.07535626507 i`, respectively, with residuals below `4e-91` at 90 dps.

For 389a1 at `x=13,N=60`, `min E=3.1638473921` and
`min O=1.6401401182`; the even candidate has `xi_0=-0.8279366893` and
first positive real `s_1=2.0181107069`. Thus the same failure occurs for a
root-number +1 example. This is preliminary finite-window evidence, not an
asymptotic classification of either curve.

There **is** a natural odd-radical analogue of the finite-dimensional lemma.
This is a derivation here, not a theorem quoted from the paper. If T is
positive with one-dimensional odd radical xi, set `B=<beta,xi>`. The
commutator in `basics:837–848` gives `T D xi=B eta`. Since `D xi` is a
nonzero even vector and cannot lie in the odd radical, `B!=0`. Then

```text
ell = beta/B,
D'_odd = D - |D xi><ell|,
T D'_odd = T D - |eta><beta| = (D'_odd)^* T,
det(D''_odd-s) = det(D-s) sum_j [beta_j xi_j/B]/(j-s).
```

Thus beta/B replaces eta. However its spectral polynomial uses the products
`beta_j xi_j`, not the Fourier coefficients `xi_j`. It loses the original
Fourier-transform determinant interpretation. Its quotient parity dimensions
are `N+1,N-1`, so it has two zero modes: solving `D'_odd v` in the radical
shows its kernel on the quotient is exactly spanned by the classes of
`V_0` and `D^(-1)xi` (inverse on the nonzero modes). Self-adjointness excludes
larger algebraic multiplicity. This does **not** fix an odd central zero.
The optional Connes–van Suijlekom source contains related commented-out
algebra at `Araki-final-oct25.tex:1304–1310`; that is not a proved odd-case
theorem and should not be cited as one.

A potentially useful next experiment is a half-integer Fourier grid
(antiperiodic boundary conditions): its starting space has even dimension,
and removing one radical gives odd dimension, allowing a single central
mode. The basis, boundary functional, gamma-window integrals and Fourier
determinant must all be rederived; F14 uses integer frequencies. This is a
separate follow-up, not a one-line switch in Lane C.

## Q2–Q5

**Q2.** The zeta accuracy law is empirical and object-specific until shown
otherwise. The cited report measures zeta, not a universal prolate problem;
the original `chi_4` heuristic uses zeta's particular theta/Hermite model.
Do not transfer `exp(-4*pi*x)`, `N>7.5x`, or `10^(0.37 gamma)` unchanged.
Here `x=13 -> 30` improves 11a1's first error by only about 5.28 decimal
digits, not the roughly 92 digits the zeta slope would predict. Increasing
N from 60 to 120 at x=13 changes the first value by only `2.69e-6`, while
its error is `4.07e-4`. This is strong evidence against using the zeta rate
as a planning assumption, although not an asymptotic falsification theorem.
There is a different natural scale: the weight-two modular Mellin kernel
has leading exponential `exp(-2*pi*u/sqrt(C_E))`, so its window tails involve
`lambda/sqrt(C_E)`, whereas the theta kernel for zeta involves `lambda^2`.
This suggests testing exponential rates in `sqrt(x/C_E)` as well as x;
neither the coefficient in that exponent nor transfer from kernel tails to
CCM spectral error is established here. Use two N values at several x before
fitting any law, and distinguish conductor from truncation in every plot.

**Q3.** This is an exact algebraic invariance test, not an open empirical
question: adding `c I` preserves eigenvectors, parity gaps and the resulting
secular polynomial while translating all form eigenvalues by c. A fake
conductor replacement translates them by `log(C_new/C_old)`. It should be a
unit test with this predicted shift, not evidence that conductors are
irrelevant to actual L-functions. Across genuine curves the conductor is
tied to the arithmetic data and to a natural Mellin length scale. An
arbitrary shifted form need not be the explicit formula of an L-function.

**Q4.** GRH gives nonnegative quadratic forms via the zero sum. Strict
positivity additionally requires that no nonzero test vector vanish at every
zero ordinate; do not treat the word “positive” as a strict eigenvalue bound
without that argument or a certificate for the particular matrix. This
concerns the true minimum over both blocks and gives neither even-simple nor
a universal decay law. For 37a1 use `min O`, not `min E`, as epsilon. Multiplicity
r contributes a positive central rank-one term and never a negative term.
The positive values recorded here are numerical, not certificates. A wrong
constant shifts both blocks equally, so Q4 is a strong test of D3 but its
sign alone cannot validate D3. The zeta `2*upper(eps)` certification threshold
also needs to be decoupled from positivity when testing artificial shifts:
a threshold between the first eigenvalue and the next global eigenvalue is
the invariant concept.

**Q5.** Use the F5 bad weights, including powers. The draft's Q5 repeats
the missing normalization. The prescribed 14a1 has nonzero bad atoms at 2
and 7 already at x=13; 37a1 has none in the requested x=8,13,20 windows, so
that scan does not test its bad prime. Add a window above 37 and an additive
example. Dropping nonzero bad atoms generally changes the matrix and low
spectrum, but “shifts every zero” is too absolute, and an atom exactly on
the window edge has no effect. Compare complete spectra only when both
modified and unmodified forms meet the construction's hypotheses; a changed
minimum parity is itself a useful mutation outcome.

## Correction ledger

| claimed | true / correction | why | where it matters |
|---|---|---|---|
| D1: `w=-c_m log p` | `w=-c_m p^(-m/2) log p` | log derivative evaluated at centre | all `(a,b)` and zeros |
| Bad weight `-a_p^m p^(-m/2) log p` | `-a_p^m p^(-m) log p` | arithmetic centre is 1 | D1, Q5, bad-prime tests |
| All bad Euler factors have degree one | additive primes have the trivial, degree-zero factor | a_p=0 | model documentation and tests |
| D3 unspecified | F9, with conductor `+log C_E` | Gauss/digamma and tail derivation | epsilon and data model |
| Kernel is ordinary `-rho` | subtracted functional in F2/F6 | logarithmic divergence at zero | constructor/API contract |
| `shift` as delta coefficient | literal delta coefficient is shift/2 | `q(0)=2` on the diagonal | factor-two regression |
| Kernel determines all constants | must also retain `Q^s`, conductor and subtraction convention | scalar factors `exp(cs)` leave the kernel unchanged | generic gamma constructor |
| a_37 for 37a1 is +1 | **-1** | count=39; PARI ellap | Section 3 and windows x>=37 |
| Four curves test additive p=2,3 | none is additive, all good at 3 | actual reduction data | add conductor 32/36 cases |
| Any real D gives all downstream theorems | real D gives Loewner form; full even-simple is an additional hypothesis | `key:863`, `even-simple:850` | D6, Lane C gating |
| A cancelled pole at 0 may give a valid exact central root | even-simple forces xi_0>0 and invertibility | quotient parity plus Lemma key | Q1 and root-count semantics |
| H-a detects root-number -1 | also occurs at x=13 for 389a1, w=+1 | numerical block minima | Q1 interpretation |
| H-a/H-b/H-c are a complete forced classification | hypotheses may vary with window; none follows from w alone | conditional theorem | scientific question design |
| Central rank-two divisor naturally gives a double zero | its quadratic-form contribution only tests the value, with weight 2 | central rank-one projector | 389a1 acceptance |
| beta can replace eta without further consequences | yes for a different operator, with exactly two central zero modes | derived odd analogue | odd-block follow-up |
| Q2 same zeta rate predicted | unsupported; observed elliptic errors far larger | object-specific gamma/Mellin scale and runs | budget/accuracy map |
| G2 every true zero lies within recovered root balls | compare with explicit approximation-error bounds | root enclosure is not a bound on model error | end-to-end acceptance |
| 2N roots means N positive scalar g roots unconditionally | multiplicities and removable poles require characteristic polynomial bookkeeping; even-simple must hold | determinant formula | generic API, central cases |
| 50-digit pins can use PARI display precision alone | pass cypari2 `precision` explicitly | default lfunzeros precision is 64 bits | reference generator |
| N means both conductor and truncation | use C_E and N | otherwise Q2 and Section 6 are ambiguous | all parameters/reports |

## Hypothesis status ledger

| label | status |
|---|---|
| H-COUNT | Confirmed for minimal general Weierstrass models; all four curves pass against PARI, supplemented by additive small-characteristic examples. |
| H-LUCAS | Confirmed by the quadratic Euler factor; the recurrence was correct, its use in D1 was not. |
| H-FE | Established input from modularity for E/Q; completion convention F1 is correct, up to an irrelevant constant. |
| H-a | Supported for 37a1 at x=8,13,20, N=60; also seen for 389a1 at x=13; not a universal theorem about root numbers. |
| H-b | Not observed in the tested rank-one cases; remains a possible asymptotic scenario in other regimes, but cannot recover odd multiplicity faithfully. |
| H-c | Not needed for these runs; exact central root or changed 2N count is incompatible with the original even-simple finite construction. |
| H-RATE | New, open: test a conductor-scaled sqrt(x) rate for elliptic data; neither its constant nor universality is derived. |
| H-ODD-VARIANT | Finite-dimensional beta/B variant derived above; it has two centre modes and does not preserve the original Fourier determinant. |
| H-HALF-GRID | New, open follow-up: antiperiodic truncation may allow an odd-dimensional quotient and a single central mode. |

## Changes I recommend to the plan

1. **Put the real primitive Dirichlet character first as the implementation
   control, then E/Q as the scientific test.** A real character is strictly
   simpler for testing a generic archimedean builder and removing the zeta
   pole term: degree one, no point counter or reduction classifier, and an
   existing FLINT reference route. It does not replace the curve experiment:
   a quadratic character does not supply the forced odd central zero that
   makes this test valuable. Promote G4 from optional to a small mandatory
   constructor regression; retain 11a1/37a1 as the principal research outcome.

2. **Freeze the regularization contract before freezing the header.** Store
   the subtracted kernel and final matrix shift as in F2/F8, or store enough
   gamma metadata (`Q,d,mu,multiplicity,conductor`) to derive them. A `d,mu`
   pair alone cannot determine the exponential constant. Define whether a
   public constructor accepts a certified conductor or computes it. Counting
   `a_p` does not compute conductor exponents or establish minimality for an
   arbitrary model; the proposed `--curve a1,...,a6` is otherwise underspecified.

3. **Keep A/B/C disjoint, but add a shared preflight gate.** Lane A should
   deliver the F5 atom pin, F9 shift, kernel quadrature pins and one modest
   11a1 anchor before Lane B freezes formulas. Lane C must implement a clear
   “odd minimum / construction inapplicable” result before calling the
   existing root finder. Do not make it invent an odd construction during
   integration. The standalone checks here already establish a usable
   reference; spending the entire first lane repeating them is unnecessary.

4. **Rewrite G2 around measured tolerances.** At x=13,N=120 use the actual
   first-zero error near `4.06892e-4`, with a modest outward margin, alongside
   certified even-simple and complete root accounting if the latter is in
   budget. For a convincing higher-accuracy anchor use x=30 with first error
   near `2.13e-9`. Compare selected ordered low zeros, report unmatched ones,
   and state approximation-error bounds separately from ball radii. Do not
   promise every zero below 20 at x=13. G1 should cover both non-scalar data
   and the exact shift; spectra alone cannot detect D3 mistakes.

5. **Rewrite G3 as parity diagnosis with an allowed stop.** Require certified
   minima of both blocks, the parity decision, and L2-normalized coefficients.
   Print sum-normalized xi and CCM roots only when normalization and
   even-simple apply. A certificate of odd minimum is a successful research
   result. Scan 389a1 too, but do not describe its rank-two centre as already
   compatible with the existing algorithm. State that these scans cannot
   settle an asymptotic alternative with finitely many windows.

6. **Do not confuse larger conductor with a need only for more N.** Increasing
   N resolves the same window. It cannot provide missing prime data or fix
   the parity obstruction. The high-conductor case may need larger x, a
   different truncation parity, or a different construction. The proposed
   x=8..40 range is a reconnaissance grid, not an accuracy guarantee.

7. **Strengthen the risk list.** The most serious concrete omission was the
   prime normalization, not the gamma coefficient. Add loss of even-simple
   also at w=+1; reference precision accidentally stuck at 64 bits; singular
   roots/removable poles and multiplicity accounting; normalization-dependent
   xi_0 claims; and conflation of interval precision with approximation error.
   Keep a shift-invariance check, but a wrong shift is not acceptable for a
   purported Weil-form implementation even when G2's roots look right.

The bounded next deliverable is a correct generic distribution builder and
certified parity/first-zero examples. A universal accuracy law, faithful
central multiplicity recovery, and an odd Fourier-determinant construction
remain separate research questions.
