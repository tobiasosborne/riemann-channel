import mpmath as mp, numpy as np
from sympy import primerange
mp.mp.dps=20
def xi(s): return mp.mpf(1)/2*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def S(tau): return xi(1-2j*tau)/xi(1+2j*tau)          # Lax-Phillips scattering symbol in the Mellin variable tau
print('--- (a) unimodularity of S on the real line ---')
for tau in (0.3, 2.0, 7.5, 21.3): print(f'tau={tau}: |S|-1 = {float(abs(S(mp.mpf(tau)))-1):.1e}')
print('--- (b) zeros of S in the lower half plane vs gamma_n/2 - i/4 ---')
for n in range(1,7):
    g=mp.zetazero(n).imag; guess=g/2-0.25j+0.01+0.01j
    r=mp.findroot(S, mp.mpc(guess))
    print(f'n={n}: gamma_n/2 = {float(g)/2:.6f};  zero of S at {complex(r).real:.6f} {complex(r).imag:+.6f}i;  |S(root)|={float(abs(S(r))):.1e}')
print('--- (c) is S small inside the lower half plane? (inner-function check at a few points) ---')
for tau in (mp.mpc(3,-0.6), mp.mpc(10,-1.0), mp.mpc(0.5,-2.0), mp.mpc(30,-0.3)):
    print(f'tau={complex(tau)}: |S| = {float(abs(S(tau))):.4f}')
print('--- (d) phase of S from the critical (sigma=1) Bost-Connes Levy exponent ---')
P=np.array(list(primerange(2,3_000_000)),dtype=float); lp=np.log(P)
def prime_phase(tau,K=6):
    # -Im log zeta(1+2 i tau) = sum_{p,k} p^{-k} sin(2 k tau log p)/k  (conditionally convergent at k=1)
    tot=0.0
    for k in range(1,K+1): tot+=np.sum(P**(-k)*np.sin(2*k*tau*lp))/k
    return tot
for tau in (0.7, 1.9, 4.2):
    exact=-mp.im(mp.log(mp.zeta(1+2j*tau)))
    print(f'tau={tau}: -arg zeta(1+2i tau) exact={float(exact):.5f}   prime sum (p<3e6)={prime_phase(tau):.5f}')
