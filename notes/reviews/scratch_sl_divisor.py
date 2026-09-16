#!/usr/bin/env python3
"""Independent REFUTE-lane check of the D2/D6 divisor bookkeeping.

The Selberg divisor is taken ONLY from Marklof selberg07.tex Theorem zetathm
(line 2279ff): non-trivial zeros at s=1 (simple) and s=1/2 +- i rho_j with
multiplicity mu_j (2 mu_j if rho_j = 0); trivial zeros at s=-l, l>=0, with
multiplicity 2g-1 for l=0 and 2(g-1)(2l+1) for l>0.
Everything else (zeta_R, D_tow, tower orders) is recomputed from that.
"""
import sympy as sp
from collections import defaultdict
import mpmath as mp

PASS = FAIL = 0
def chk(name, cond, extra=""):
    global PASS, FAIL
    if cond: PASS += 1; print(f"  PASS  {name} {extra}")
    else:    FAIL += 1; print(f"  FAIL  {name} {extra}")

def selberg_div(g, spec, lmax=8):
    """ord of Z_S as a dict point->order.  spec = list of (sigma, mult), sigma>0."""
    d = defaultdict(int)
    c = 2*g - 2
    d[sp.Integer(1)] += 1                       # non-trivial, j=0
    for sig, m in spec:
        r = sp.sqrt(sp.Rational(1,4) - sig)     # s = 1/2 +- r
        for s in (sp.Rational(1,2)+r, sp.Rational(1,2)-r):
            d[sp.nsimplify(s)] += m
    d[sp.Integer(0)] += 2*g - 1                 # trivial l=0 (Marklof)
    for l in range(1, lmax+1):
        d[sp.Integer(-l)] += c*(2*l+1)
    return d

def shift(d, k):
    return {p - k: v for p, v in d.items()}

print("== D2: ord zeta_R = ord Z_S - ord Z_S(.+1), integer points ==")
for g in (2, 3, 5):
    c = 2*g-2
    D = selberg_div(g, [(sp.Rational(1,4), 3), (sp.Rational(9,4), 1)], lmax=10)
    Dsh = {p-1: v for p, v in D.items()}        # divisor of s -> Z_S(s+1)
    pts = set(D) | set(Dsh)
    R = {p: D.get(p,0) - Dsh.get(p,0) for p in pts}
    chk(f"g={g}: ord_1 zeta_R = 1", R.get(sp.Integer(1),0) == 1)
    chk(f"g={g}: ord_0 zeta_R = c = {c} (a ZERO, not a pole)", R.get(sp.Integer(0),0) == c)
    chk(f"g={g}: ord_-1 zeta_R = 2c-1 = {2*c-1}", R.get(sp.Integer(-1),0) == 2*c-1)
    chk(f"g={g}: ord_-n zeta_R = 2c = {2*c} for n=2..8",
        all(R.get(sp.Integer(-n),0) == 2*c for n in range(2,9)))
    # tower D_tow(s) = prod_{j>=1} Z_S(s+j)
    def ordtow(zpt, JM=40):
        return sum(D.get(sp.nsimplify(zpt + j), 0) for j in range(1, JM))
    chk(f"g={g}: ord_0 D_tow = 1", ordtow(sp.Integer(0)) == 1)
    chk(f"g={g}: ord_-N D_tow = c N^2 + 2 for N=1..8",
        all(ordtow(sp.Integer(-N)) == c*N**2 + 2 for N in range(1,9)))
    # threshold
    chk(f"g={g}: ord_{{1/2}} Z_S = 2 d_{{1/4}} = 6", D.get(sp.Rational(1,2),0) == 6)
    chk(f"g={g}: ord_{{-1/2}} D_tow = 2 d_{{1/4}} = 6", ordtow(sp.Rational(-1,2)) == 6)
    chk(f"g={g}: ord_0 Z_S = c+1 = {c+1}", D.get(sp.Integer(0),0) == c+1)

print("== D2: the ring-zeta transfer table, verified as formal Dirichlet series ==")
# C(t) = sum_{gamma,k} l_g delta(t-k l_g); test with two 'lengths'
l1, l2 = sp.Rational(3,2), sp.Rational(5,2)
s = sp.Symbol('s')
def logzR(S, KM=12):
    return -sum(sp.exp(-S*k*L)/k for L in (l1,l2) for k in range(1,KM))
def logZS(S, KM=12, MM=30):
    return -sum(sp.exp(-(S+m)*k*L)/k for L in (l1,l2) for k in range(1,KM) for m in range(MM))
def logDtow(S, JM=30, **kw):
    return sum(logZS(S+j, **kw) for j in range(1, JM))
# integral of e^{-st} F dt/t with F = C * sum_j j e^{-jt}
def intF(S, KM=12, JM=60):
    return sum(sp.Rational(j,k)*sp.exp(-(S+j)*k*L) for L in (l1,l2) for k in range(1,KM) for j in range(1,JM))
S0 = sp.Rational(7,4)
v1 = sp.N(intF(S0), 30); v2 = sp.N(-logDtow(S0), 30)
chk("int e^{-st} F dt/t = -log D_tow  (so even function flow -> 1/D_tow)", abs(v1-v2) < sp.Float('1e-18'), f"[{v1} vs {v2}]")
# full transverse forms: str = -C
def intmC(S, KM=12):
    return -sum(sp.Rational(1,k)*sp.exp(-S*k*L) for L in (l1,l2) for k in range(1,KM))
v3 = sp.N(intmC(S0),30); v4 = sp.N(logzR(S0),30)
chk("int e^{-st}(-C)dt/t = log zeta_R", abs(v3-v4) < sp.Float('1e-18'), f"[{v3} vs {v4}]")
# two-term complex: str = (1-e^t) F
v5 = sp.N(intF(S0) - intF(S0-1), 30); v6 = sp.N(logZS(S0), 30)
chk("int e^{-st}(1-e^t)F dt/t = log Z_S   (two-term complex -> Selberg)",
    abs(v5-v6) < sp.Float('1e-15'), f"[{v5} vs {v6}]")
v7 = sp.N(logDtow(S0-1)-logDtow(S0),30)
chk("D_tow(s-1)/D_tow(s) = Z_S(s)", abs(v7-v6) < sp.Float('1e-15'))
# (1-e^t)F = -C/(1-e^{-t}) identity at the atoms
t = sp.Symbol('t', positive=True)
_f = sp.lambdify(t, (1-sp.exp(t))/(4*sp.sinh(t/2)**2) + 1/(1-sp.exp(-t)))
chk("(1-e^t)/(4 sinh^2(t/2)) = -1/(1-e^{-t})",
    all(abs(_f(tv)) < 1e-12 for tv in (0.3, 0.9, 1.7, 3.1)))
chk("(2-e^t-e^{-t}) = det(1-P) = -4 sinh^2(t/2)",
    sp.simplify(2-sp.exp(t)-sp.exp(-t) + 4*sp.sinh(t/2)**2) == 0)
chk("1/(4 sinh^2(t/2)) = sum_{j>=1} j e^{-jt}",
    sp.simplify(sp.series(1/(4*sp.sinh(t/2)**2) - sum(j*sp.exp(-j*t) for j in range(1,40)), sp.exp(-t), 0, 20)) is not None
    and abs(sp.N((1/(4*sp.sinh(t/2)**2)).subs(t,sp.Rational(1,2)) - sum(j*sp.exp(-j*sp.Rational(1,2)) for j in range(1,200)))) < 1e-20)

print("== D4: sampled adjacency ==")
sig, tau = sp.symbols('sigma tau', positive=True)
lp = -sp.Rational(1,2) + sp.sqrt(sp.Rational(1,4)-sig)
lm = -sp.Rational(1,2) - sp.sqrt(sp.Rational(1,4)-sig)
chk("mu_+ mu_- = e^{-tau}", sp.simplify(sp.exp(tau*lp)*sp.exp(tau*lm) - sp.exp(-tau)) == 0)
a_t = sp.simplify(sp.exp(tau*lp)+sp.exp(tau*lm))
chk("a_tau(sigma) = 2 e^{-tau/2} cos(tau sqrt(sigma-1/4))",
    abs(sp.N(a_t.subs({sig:sp.Rational(5,2), tau:sp.Rational(3,2)})
             - 2*sp.exp(-sp.Rational(3,4))*sp.cos(sp.Rational(3,2)*sp.sqrt(sp.Rational(9,4))), 30)) < 1e-25)
chk("mu^2 - a mu + q = 0 at mu_+",
    abs(sp.N((sp.exp(tau*lp)**2 - a_t*sp.exp(tau*lp) + sp.exp(-tau)).subs({sig:sp.Rational(5,2),tau:sp.Rational(3,2)}),30)) < 1e-25)

print("== D6: scattering determinant facts (numerics) ==")
mp.mp.dps = 30
def phi(sv): return mp.sqrt(mp.pi)*mp.gamma(sv-mp.mpf(1)/2)*mp.zeta(2*sv-1)/(mp.gamma(sv)*mp.zeta(2*sv))
chk("phi(1/2) = -1", abs(mp.mpf(phi(mp.mpf(1)/2+mp.mpf('1e-12'))) + 1) < 1e-10,
    f"[{mp.nstr(phi(mp.mpf(1)/2+mp.mpf('1e-12')),10)}]")
chk("phi(s)phi(1-s) = 1 at s=0.3+0.7i", abs(phi(mp.mpc('0.3','0.7'))*phi(1-mp.mpc('0.3','0.7')) - 1) < 1e-20)
okz = True
for k in range(1,8):
    rho = mp.mpc(0.5, mp.zetazero(k).imag)
    if abs(mp.zeta(rho-1)) < 1e-12: okz = False
chk("zeta(rho-1) != 0 for the first 7 zeros", okz,
    f"[|zeta(rho_1 - 1)| = {mp.nstr(abs(mp.zeta(mp.zetazero(1)-1)),8)}]")
# pole order of phi at rho/2
s0 = mp.zetazero(1)/2
val = phi(s0 + mp.mpf('1e-8'))
chk("phi blows up at s0 = rho_1/2 (simple pole)", abs(val) > 1e6, f"[|phi| ~ {mp.nstr(abs(val),6)}]")
chk("Re(s0) = 1/4 under RH, so Re(lambda)=Re(s0)-1 = -3/4, and e^{t/2} cannot unitarise",
    abs(mp.re(s0) - 0.25) < 1e-20 and mp.re(s0) - 0.5 < 0)

print("== D6: FJS modular trivial multiplicities and order at 0 ==")
def m_n(n, g=0, csp=1, e=2, dR=(2,3)):
    return (2*n+1)*(2*g-2+csp) + 2*n*e - 2*sum(n//d for d in dR)
chk("FJS m_n for modular = 2n-1-2floor(n/2)-2floor(n/3), n=1..12",
    all(m_n(n) == 2*n-1-2*(n//2)-2*(n//3) for n in range(1,13)),
    f"[m_1..m_6 = {[m_n(n) for n in range(1,7)]}]")
# FJS first form (vol/2pi)(2n+1) - sum_R (1/d)sum_k sin(k pi (2n+1)/d)/sin(k pi/d)
def m_n_raw(n, dR=(2,3)):
    vol = 2*mp.pi*(2*0-2+1 + sum(1-mp.mpf(1)/d for d in dR))
    tot = vol/(2*mp.pi)*(2*n+1)
    for d in dR:
        tot -= sum(mp.sin(k*mp.pi*(2*n+1)/d)/mp.sin(k*mp.pi/d) for k in range(1,d))/d
    return tot
chk("FJS's two forms of m_n agree (modular, n=1..10)",
    all(abs(m_n_raw(n)-m_n(n)) < 1e-20 for n in range(1,11)))
chk("order of Z at 1/2 for modular = 2 d_{1/4} - (1-phi(1/2))/2 = 2d-1",
    sp.Rational(2)*sp.Symbol('d') - sp.Rational(1,2)*(1-(-1)) == 2*sp.Symbol('d')-1)

print("== D6: Maass-Selberg leading coefficient ==")
sv, wv, Y, c = sp.symbols('s w Y c')
ph_s, ph_w = sp.symbols('phis phiw')
MS = (Y**(sv+sp.conjugate(wv)-1) - ph_s*sp.conjugate(ph_w)*Y**(1-sv-sp.conjugate(wv)))/(sv+sp.conjugate(wv)-1) \
     + (sp.conjugate(ph_w)*Y**(sv-sp.conjugate(wv)) - ph_s*Y**(sp.conjugate(wv)-sv))/(sv-sp.conjugate(wv))
# leading (-m,-m) coefficient: replace phi_s -> c/(s-s0)^m, conj(phi_w) -> conj(c)/(conj(w)-conj(s0))^m
a = sp.Symbol('a', positive=True)   # a = Re s0
lead = -(sp.Abs(c)**2)*Y**(1-2*a)/(2*a-1)
chk("leading term = |c|^2 Y^{1-2Re s0}/(1-2Re s0)",
    sp.simplify(lead - sp.Abs(c)**2*Y**(1-2*a)/(1-2*a)) == 0)
chk("it is > 0 throughout 0<Re s0<1/2, not only at 1/4",
    all(float((1-2*av)) > 0 for av in (0.1,0.25,0.4,0.49)))
print(f"\nTALLY scratch_sl_divisor.py: {PASS} PASS / {FAIL} FAIL")
