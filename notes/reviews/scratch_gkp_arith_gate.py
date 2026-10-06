"""REFUTE scratch (gate-phases.md), written from the statements only.
Conventions (Tate): psi_inf(x)=e^{-2 pi i x}, psi_p(x)=e^{2 pi i {x}_p}; on K the character psi o Tr; self-dual measures.
Local root number (Tate's integral form):  eps(chi,psi) at s=1/2 = int_{c^{-1} O^x} chi^{-1}(x) |x|^{-1/2} psi(x) dx,
with v(c) = a(chi) + d. Each value below is computed by explicit finite sums / quadrature, no PARI except for the final comparison."""
import cmath, math, numpy as np, subprocess
from sympy import legendre_symbol as _leg
leg = lambda a, p: int(_leg(a, p))
def gp(cmd):
    return subprocess.run(['gp', '-q', '-f'], input=cmd + '\n\\q\n', capture_output=True, text=True).stdout.strip()
e = lambda t: cmath.exp(2j*math.pi*t)
# ---------- place 7: K_7 = Q_7(pi), pi^2 = -7, x = a + b pi, Tr(x) = 2a, |pi| = 7^{-1}, vol(O) = 7^{-1/2}
eps7 = lambda a: 0 if a % 7 == 0 else leg(a % 7, 7)          # Legendre symbol of x mod pi
chi7_pi = 1j                                                  # the claim to be tested: chi_7(pi) = +i
# (i) the global consistency fixing chi_7(pi): prod_v chi_v(alpha) = 1 for alpha in O_K;
#     chi_inf(z) = |z|/z, chi_7 = eps on units, chi_p(varpi_p) = psi_u(p) = eps(beta) beta/|beta| for the generator beta of p.
def chi_inf(z): return abs(z)/z
def factor_check(nmax=60):
    import sympy
    worst = 0
    w = complex(0.5, math.sqrt(7)/2)
    for a in range(-nmax, nmax):
        for b in range(-nmax, nmax):
            al = a + b*w
            Nn = a*a + a*b + 2*b*b
            if Nn == 0 or Nn > 400: continue
            # unramified part: psi_u of the prime-to-7 part of (alpha); write alpha = pi^k * beta, beta prime to pi
            k = 0; be = al
            pi = complex(0, math.sqrt(7))
            while True:
                # beta divisible by pi iff its reduction a' + 4b' == 0 mod 7 (w == 4 mod pi)
                br = round(be.real - be.imag/math.sqrt(7)); bb = round(2*be.imag/math.sqrt(7))  # coordinates in 1,w
                if (br + 4*bb) % 7 != 0: break
                be = be/pi; k += 1
            br = round(be.real - be.imag/math.sqrt(7)); bb = round(2*be.imag/math.sqrt(7))
            psi_u = eps7(br + 4*bb)*be/abs(be)                     # = prod over unramified p of chi_p(alpha)
            # chi_7(alpha) = chi_7(pi)^k * eps(beta mod pi)
            c7 = chi7_pi**k*eps7(br + 4*bb)
            tot = chi_inf(al)*c7*psi_u
            worst = max(worst, abs(tot - 1))
    return worst
print('(i) max |prod_v chi_v(alpha) - 1| over alpha in O_K, N(alpha)<=400, with chi_7(pi)=+i:', f'{factor_check():.1e}')
chi7_pi = -1j
print('    same with chi_7(pi) = -i:', f'{factor_check():.1e}'); chi7_pi = 1j
# (ii) Fourier transform of Phi_7 = eps 1_{O^x} on y = (c + d pi)/7^s, compared with i D_7 Phi_7
def FPhi7(c, d, s):
    # sum over x = a + b pi, a,b mod 7^s, vol of each class = 7^{-1/2} 49^{-s}
    tot = 0
    for a in range(7**s):
        if a % 7 == 0: continue
        for b in range(7**s):
            # x y = (a + b pi)(c + d pi)/7^s = (ac - 7bd + (ad + bc) pi)/7^s ; Tr = 2(ac - 7bd)/7^s
            tot += eps7(a)*e(2*(a*c - 7*b*d)/7**s)
    return tot*7**-0.5*49.0**-s
def iD7Phi7(c, d, s):
    # D_7 f(y) = |7|^{1/2} f(7y), |7|_K = 49^{-1}; 7y = (c + d pi) 7^{1-s}
    if s != 1: return 0.0       # 7y in O^x only when s = 1 and c is a unit
    return 1j*(1/7)*eps7(c)
worst = 0
for s in [1, 2]:
    for c in range(7**s):
        for d in range(0, 7**s, 7**(s-1) if s > 1 else 1):
            val = FPhi7(c, d, s)
            ref = iD7Phi7(c, d, s) if (s == 1 or c % 7 == 0 and False) else (iD7Phi7(c, d, 1) if False else 0)
            if s == 2:
                # y = (c + d pi)/49 lies in pi^{-4}O; it is in pi^{-2}O^x... only if c == 0 mod 7; reduce: y = (c/7 + (d/7)pi)/7
                ref = iD7Phi7(c//7, d//7, 1) if (c % 7 == 0 and d % 7 == 0) else 0
            worst = max(worst, abs(val - ref))
print('(ii) max |F Phi_7 - i D_7 Phi_7| on y in 7^{-1}O and 49^{-1}O sample classes:', f'{worst:.1e}')
# (iii) epsilon_7 by Tate's integral: c = pi^2 (v(c) = a + d = 1 + 1): x = pi^{-2} u, u in O^x mod pi
#    chi^{-1}(pi^{-2} u) = chi(pi)^2 eps(u);  |x|^{-1/2} = 49^{-1/2};  dx-volume of pi^{-2}(u + pi O) = 49 * 7^{-3/2}
tot = 0
for u in range(1, 7):
    x_tr = 2*u/(-7)                      # Tr(pi^{-2} u) = Tr(-u/7) = -2u/7
    tot += (chi7_pi**2*eps7(u)) * e(x_tr)
eps_7 = tot*49**-0.5*49*7**-1.5
print('(iii) eps_7 =', np.round(eps_7, 15), '  (Gauss sum g_7 =', np.round(sum(eps7(u)*e(u/7) for u in range(1, 7)), 12), ')')
# ---------- place 3: K_3 = Q_9, F_9 = F_3[i]/(i^2+1), eta(u) = (N u | 3)
F9 = [(a, b) for a in range(3) for b in range(3) if (a, b) != (0, 0)]
Nm = lambda a, b: (a*a + b*b) % 3
eta = lambda a, b: leg(Nm(a, b), 3)
Tr9 = lambda a, b: (2*a) % 3
g9 = sum(eta(a, b)*e(Tr9(a, b)/3) for a, b in F9)
g3 = sum(leg(u, 3)*e(u/3) for u in [1, 2])
print('(iv) g_9 =', np.round(g9, 12), '  -g_3^2 =', np.round(-g3**2, 12), '  eta quadratic & nontrivial:', sorted(set(eta(*u) for u in F9)))
# eps_3 for psi' : chi(3) = psi'_3(3) = psi_u((3)) * chi_{-3,3}(N 3) = (3|7) * 1 ; c = 3 (a=1, d=0)
chi3_3 = leg(3, 7)
for label, val in [('psi\'_3(3) = (3|7)', chi3_3), ('control psi\'_3(3)=+1', 1)]:
    tot = sum(val*eta(a, b)*e(Tr9(a, b)/3) for a, b in F9)   # chi^{-1}(u/3) = chi(3) eta(u)
    eps3 = tot*9**-0.5*1.0                                       # |x|^{-1/2} = 9^{-1/2}, vol(3^{-1}(u+3O)) = 1
    print(f'(v) eps_3(psi\') with {label}: {np.round(eps3, 15)}')
# ---------- infinity: Phi(z) = z e^{-2 pi |z|^2}, F with kernel e^{-2 pi i Tr(zw)} = e^{-4 pi i Re(zw)}, measure 2 dx dy
h = 0.02; xs = np.arange(-4, 4, h) + h/2
X, Y = np.meshgrid(xs, xs, indexing='ij'); Zg = X + 1j*Y
Phi = Zg*np.exp(-2*np.pi*np.abs(Zg)**2)
for w in [0.3 + 0.2j, -0.5 + 0.7j]:
    FPhi = np.sum(Phi*np.exp(-4j*np.pi*np.real(Zg*w)))*2*h*h
    print(f'(vi) F Phi(w={w}) = {FPhi:.12f};  -i conj(w) e^(-2pi|w|^2) = {-1j*np.conj(w)*np.exp(-2*np.pi*abs(w)**2):.12f}')
# zeta integrals at s=1/2 with chi_inf(z) = |z|/z: Z(Phi,chi,1/2) = int z e^{-2pi|z|^2} (|z|/z) |z|_C^{1/2} d^x z ;
# Z(F Phi, chi^{-1}, 1/2) with F Phi = -i conj(z) e^{-2 pi |z|^2}; ratio = eps_inf (L_inf factors equal at the centre)
r = np.sqrt(X**2 + Y**2) + 1e-300
Z1 = np.sum(Phi*(r/Zg)*r/(r**2))*h*h
Z2 = np.sum((-1j*np.conj(Zg)*np.exp(-2*np.pi*r**2))*(Zg/r)*r/(r**2))*h*h
print('(vii) eps_inf = Z(F Phi, chi^-1, 1/2)/Z(Phi, chi, 1/2) =', np.round(Z2/Z1, 10))
W1 = (-1j)*eps_7; W2 = (-1j)*eps_7*(-1)
print('(viii) products: 49a1', np.round(W1, 12), ' 441d1', np.round(W2, 12), '  PARI ellrootno:', gp('print([ellrootno(ellinit("49a1")),ellrootno(ellinit("441d1"))])'))
