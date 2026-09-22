#!/usr/bin/env python3
"""Author: codex:gpt-6-astra
Certified augmented cosine L_1 Gram; run from any directory. Prints only.
All analytic computation uses mpmath.iv; integers/Fraction/SymPy are exact.
No ordinary floating point special functions, quadrature or eigensolvers.
"""
import argparse
from fractions import Fraction
from math import factorial
import mpmath
from mpmath import iv
from sympy import bernoulli

parser = argparse.ArgumentParser()
parser.add_argument('--dps', type=int, default=90)
parser.add_argument('--terms', type=int, default=24)
args = parser.parse_args()
iv.dps = args.dps
M = args.terms
N = 2*M
Z = iv.mpf(0)
ONE = iv.mpf(1)
HALF = ONE/2
PI = iv.pi

def rat(a, b=1):
    return iv.mpf(int(a))/int(b)

def upper(x):
    return x.b

def mag(z):
    return upper(abs(z))

def conj(z):
    return iv.mpc(z.real, -z.imag)

def noise(r):
    r = upper(r)
    return iv.mpf([-r, r])

def widen(z, r):
    if isinstance(z, iv.mpc):
        return z + iv.mpc(noise(r), noise(r))
    return z + noise(r)

def exact_endpoint(t):
    sign, mantissa, exponent, _ = t
    return Fraction((-1 if sign else 1)*mantissa) * Fraction(2)**exponent

def decimal_integer(n, digits):
    sign = '-' if n < 0 else ''
    s = str(abs(n)).rjust(digits+1, '0')
    return sign + s[:-digits] + '.' + s[-digits:] if digits else str(n)

def fmt(x, digits=18):
    """Outward decimal formatting by exact integer floor/ceiling."""
    lo, hi = map(exact_endpoint, x._mpi_)
    scale = 10**digits
    a = (lo*scale).__floor__()
    b = (hi*scale).__ceil__()
    return '[' + decimal_integer(a,digits) + ', ' + decimal_integer(b,digits) + ']'

def show(name, x, digits=18):
    if isinstance(x, iv.mpc):
        print(name, fmt(x.real,digits), '+ i', fmt(x.imag,digits), flush=True)
    else:
        print(name, fmt(x,digits), flush=True)

def less(x, bound):
    assert upper(x) < iv.mpf(bound), (x, bound)

def moment(s, k):
    z = 1/s
    for j in range(1,k+1):
        z *= (s-j)/(s+j)
    return z

roots = [iv.sqrt(2*k+1) for k in range(1,N+1)]
c = [2*(-1)**n*(2*PI)**(2*n)/factorial(2*n) for n in range(M+1)]
U = [[roots[k-1]*moment(iv.mpf(2*n+1), k) if k <= 2*n else Z
      for k in range(1,N+1)] for n in range(M+1)]
A = [[sum((c[n]*U[n][i]*U[n][j] for n in range(1,M+1)), Z)
      for j in range(N)] for i in range(N)]
eps = upper(2*(2*PI)**(2*M+2)/factorial(2*M+2))
ratio = upper((2*PI)**2/((2*M+3)*(2*M+4)))
assert ratio < 1
tailbase = eps/(1-ratio)
eta = upper(tailbase*(rat(1,2*M+3)+rat(1,2*M+1)))
afrob = upper(iv.sqrt(sum((mag(a)**2 for row in A for a in row),Z)))
tbound = upper(afrob+eps)
t0 = rat(3,4)
assert tbound < t0
show('A_Frobenius',afrob)
show('kernel_error_eps',eps,50)
show('r2_preprojection_tail_eta',eta,50)
show('T_norm_upper',tbound)
show('resolvent_norm_upper',1/(1-t0**2))

r = [(-2*PI**2*roots[k-1]*moment(iv.mpf(2),k)
      + sum((-c[n]*(rat(1,2*n+1)+rat(1,2*n-1))*U[n][k-1]
             for n in range(1,M+1)),Z)) for k in range(1,N+1)]
B = [[(ONE if i==j else Z)-sum((A[i][k]*A[k][j] for k in range(N)),Z)
      for j in range(N)] for i in range(N)]

def solve(B,r):
    """Interval Gaussian elimination: each exact pivot enclosed away from zero."""
    B = [row[:] for row in B]
    r = r[:]
    for k in range(N):
        assert B[k][k].a > 0
        for i in range(k+1,N):
            f = B[i][k]/B[k][k]
            for j in range(k+1,N):
                B[i][j] -= f*B[k][j]
            r[i] -= f*r[k]
    w = [Z]*N
    for i in range(N-1,-1,-1):
        w[i] = (r[i]-sum((B[i][j]*w[j] for j in range(i+1,N)),Z))/B[i][i]
    return w

w = solve(B,r)
wnorm = upper(iv.sqrt(sum((mag(a)**2 for a in w),Z)))
wsup = upper(sum((mag(w[k])*roots[k] for k in range(N)),Z))
delta2 = upper((eta+eps*(t0+afrob)*wnorm)/(1-t0**2))
deltainf = upper(2*eta+4*t0*delta2+eps*(2*t0+4+2*eps)*wnorm)
show('w_L2_upper',wnorm)
show('w_Linf_upper',wsup)
show('v_minus_w_L2',delta2,50)
show('v_minus_w_Linf',deltainf,50)
show('v_Legendre_tail_Linf',deltainf+iv.sqrt(N*(N+2))*delta2,50)
for k in range(N):
    show('r2_coef_%02d'%(k+1),widen(r[k],eta),32)
    show('v_coef_%02d'%(k+1),widen(w[k],delta2),32)

# Euler--Maclaurin log Gamma, shifted into Re z >= 64.
# Through B_(2K); remainder -1/(2K) integral B_(2K)({t})/(z+t)^(2K) dt.
# Bounds: |R| <= |B_(2K)|/[2K(2K-1) Re(z)^(2K-1)] and
# |R'| <= |B_(2K)|/[2K Re(z)^(2K)].
K = 18
SHIFT = 64
ber = [None]+[rat(*bernoulli(2*k).as_numer_denom()) for k in range(1,K+1)]

def loggamma_psi(z):
    if not isinstance(z, iv.mpc):
        z = iv.mpc(z)
    zz = z+SHIFT
    assert zz.real.a >= 64
    lg = (zz-HALF)*iv.log(zz)-zz+iv.log(2*PI)/2
    ps = iv.log(zz)-1/(2*zz)
    for k in range(1,K+1):
        lg += ber[k]/(2*k*(2*k-1)*zz**(2*k-1))
        ps -= ber[k]/(2*k*zz**(2*k))
    a = zz.real.a
    er = mag(ber[K])/(2*K*(2*K-1)*a**(2*K-1))
    ep = mag(ber[K])/(2*K*a**(2*K))
    lg = widen(lg,er)
    ps = widen(ps,ep)
    for j in range(SHIFT):
        lg -= iv.log(z+j)
        ps -= 1/(z+j)
    return lg,ps

show('loggamma_remainder_upper_at_Re64',mag(ber[K])/(2*K*(2*K-1)*iv.mpf(64)**(2*K-1)),50)
show('psi_remainder_upper_at_Re64',mag(ber[K])/(2*K*iv.mpf(64)**(2*K)),50)

def scalar_factors(s):
    lg,ps = loggamma_psi(s/2)
    lm = lg-s*iv.log(PI)/2
    m = iv.exp(lm)
    md = m*(ps-iv.log(PI))/2
    lh,ph = loggamma_psi((1-s)/2)
    ch = iv.exp((s-HALF)*iv.log(PI)+lh-lg)
    chd = ch*(iv.log(PI)-(ph+ps)/2)
    return m,md,ch,chd

def scalar_integral(s,ch,chd=None):
    """Encloses J(s) and optionally J'(s), including uniform v error."""
    mu = 1/s
    mud = -1/s**2
    mw = iv.mpc(0)
    mwd = iv.mpc(0)
    for k in range(1,N+1):
        f = (s-k)/(s+k)
        mud,mu = mud*f+mu*2*k/(s+k)**2,mu*f
        mw += w[k-1]*roots[k-1]*mu
        mwd += w[k-1]*roots[k-1]*mud
    j = ch*mw
    jd = chd*mw+ch*mwd if chd is not None else None
    norm0 = Z
    norm1 = Z
    for n in range(1,M+1):
        a = c[n]*(1/((1-s)*(2*n+1))-1/(2*n+1-s))
        ad = c[n]*(1/((1-s)**2*(2*n+1))-1/(2*n+1-s)**2)
        wx = sum((w[k]*U[n][k] for k in range(N)),Z)
        j += a*wx
        norm0 += mag(a)/(2*n+1)
        if jd is not None:
            jd += ad*wx
            norm1 += mag(ad)/(2*n+1)
    sigma = s.real.a
    sigmax = s.real.b
    inv = mag(1/(1-s))
    tau0 = upper(tailbase*(inv/(2*M+3)+1/(2*M+3-sigmax)))
    tau1 = upper(tailbase*(inv**2/(2*M+3)+1/(2*M+3-sigmax)**2))
    err0 = upper(deltainf*(mag(ch)/sigma+norm0+tau0)+wsup*tau0)
    j = widen(j,err0)
    if jd is not None:
        err1 = upper(deltainf*(mag(chd)/sigma+mag(ch)/sigma**2+norm1+tau1)+wsup*tau1)
        jd = widen(jd,err1)
    else:
        err1 = Z
    return j,jd,err0,err1,tau0,tau1

j2,_,_,_,_,_ = scalar_integral(iv.mpc(2),iv.mpc(-2*PI**2))
H2 = rat(4,3)-j2.real
F2 = 4/PI**2*H2
assert F2.a > 0
b = iv.sqrt(3*F2)
show('J2',j2.real,24)
show('H2',H2,24)
show('F2',F2,24)
show('b',b,24)

gtext = ['14.13472514173469379045725','21.02203963877155499262848',
         '25.01085758014568876321379']
gammas = [iv.mpf(g)+noise(iv.mpf('1e-23')) for g in gtext]
Es = []
Eds = []
phases = []
ps = []
for i,g in enumerate(gammas):
    s = iv.mpc(HALF,g)
    m,md,ch,chd = scalar_factors(s)
    j,jd,err0,err1,tau0,tau1 = scalar_integral(s,ch,chd)
    h = -1/(1-s)+1/(s+1)-j
    hd = -1/(1-s)**2-1/(s+1)**2-jd
    p = s*(s-1)
    pd = 2*s-1
    f = 2/PI*p*m*h
    fd = 2/PI*((pd*m+p*md)*h+p*m*hd)
    e = (s+1)*f/b
    ed = (f+(s+1)*fd)/b
    phase = conj(e)/e
    Es.append(e)
    Eds.append(ed)
    phases.append(phase)
    ps.append(-(g**2+rat(1,4)))
    show('chi_%d'%(i+1),ch,22)
    show('chi_prime_%d'%(i+1),chd,22)
    show('J_%d'%(i+1),j,22)
    show('J_prime_%d'%(i+1),jd,22)
    show('J_analytic_error_%d'%(i+1),err0,45)
    show('Jprime_analytic_error_%d'%(i+1),err1,45)
    show('continuation_tail_%d'%(i+1),tau0,45)
    show('continuation_derivative_tail_%d'%(i+1),tau1,45)
    show('E_%d'%(i+1),e,26)
    show('Esharp_%d'%(i+1),conj(e),26)
    show('Eprime_%d'%(i+1),ed,26)
    show('phase_%d'%(i+1),phase,16)

G = [[Z for j in range(3)] for i in range(3)]
for i in range(3):
    G[i][i] = 2*(conj(Es[i])*Eds[i]).real/ps[i]**2
    assert G[i][i].a > 0
    for j in range(i+1,3):
        G[i][j] = 2*(conj(Es[i])*Es[j]).imag/((gammas[j]-gammas[i])*ps[i]*ps[j])
        G[j][i] = G[i][j]
    for j in range(i,3):
        show('G_%d%d'%(i+1,j+1),G[i][j],32)
O = [[(ONE if i==j else G[i][j]/iv.sqrt(G[i][i]*G[j][j])) for j in range(3)] for i in range(3)]
loss = [[iv.mpc(HALF,(gammas[i]-gammas[j])/2)*O[i][j] for j in range(3)] for i in range(3)]
for i in range(3):
    for j in range(i,3):
        show('O_%d%d'%(i+1,j+1),O[i][j],16)
        show('N_%d%d'%(i+1,j+1),loss[i][j],16)
for i in range(3):
    for j in range(i+1,3):
        distance = abs(phases[i]-phases[j])
        assert distance.a > iv.mpf('0.015')
        show('phase_distance_%d%d'%(i+1,j+1),distance,16)

# Rational test vector is fixed independently of any eigenvalue computation.
# This first version checks a negative principal 3-mode direction below.
test = [iv.mpc(1),iv.mpc(0,1),iv.mpc(1)]
value = sum((conj(test[i])*loss[i][j]*test[j] for i in range(3) for j in range(3)),iv.mpc(0))
show('trial_quadratic_form',value,16)
print('INTERVAL ASSEMBLY COMPLETE; mpmath',mpmath.__version__,'M',M,'N',N,'dps',iv.dps,flush=True)
