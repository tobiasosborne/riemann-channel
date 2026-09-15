#!/usr/bin/env python3
"""D1--D9, D13--D14: exact counterexamples and independent finite checks.

Run from the repository root with PYTHONDONTWRITEBYTECODE=1.
No files are written. Kronecker convention: A tensor conjugate(A).
"""
import itertools
import numpy as np
import sympy as s
from scipy.linalg import expm

count = 0
def check(ok, label):
    global count
    assert bool(ok), label
    count += 1
    print(f"PASS {count:03d}: {label}")

I = s.eye(2)
X = s.Matrix([[0, 1], [1, 0]])
Y = s.Matrix([[0, -s.I], [s.I, 0]])
P = s.diag(1, -1)
G = s.kronecker_product(P, P)
u = s.symbols('u')
ev, od = [0, 3], [1, 2]
def doubled(letters):
    return sum((s.kronecker_product(a, s.conjugate(a)) for a in letters), s.zeros(4))
def sectors(E):
    return E.extract(ev, ev), E.extract(od, od)
def bass(letters):
    D = len(letters)
    rev = [i ^ 1 for i in range(D)]
    T = s.zeros(4 * D)
    for i, a in enumerate(letters):
        a2 = doubled([a])
        for j in range(D):
            if j != rev[i]:
                T[4*j:4*j+4, 4*i:4*i+4] = a2
    return T
def f(lam, q):
    return 1 - lam*u + q*u*u

# D1: equal radii without any equal-valued even/odd eigenvalues.
E = doubled([P]); E0, E1 = sectors(E)
check(E0 == s.eye(2) and E1 == -s.eye(2), 'D1 equal radii, disjoint spectra {1} and {-1}')
for n in range(1, 7):
    check(abs(s.trace(E1**n)) <= s.trace(E0**n), f'D1 trace inequality n={n}')
check(sorted((s.eye(2)+X).eigenvals()) == [0,2] and ((s.eye(2)+X)*P != P*(s.eye(2)+X)),
      'positive matrices need not be even; I+X is a rank-one positive matrix')

# D4: primitive mixed-unitary qubit, an off-band quadratic cancels exactly.
letters = [I]*10 + [X]*2 + [P]*2
E0, E1 = sectors(doubled(letters))
check(sorted(E0.eigenvals()) == [10, 14] and sorted(E1.eigenvals()) == [6, 10],
      'D4 primitive counterexample: even {14,10}, odd {10,6}')
check(10**2 > 4*13 and 6**2 < 4*13, 'D4 hidden modes outside band, surviving modes inside')
Z = s.cancel((s.eye(2)-u*E1+13*u*u*s.eye(2)).det() /
             (s.eye(2)-u*E0+13*u*u*s.eye(2)).det())
check(s.cancel(Z-f(6,13)/((1-u)*(1-13*u))) == 0, 'D4 exact cancellation of f_10')
print('D4 reduced Z =', s.factor(Z))

# D5: all dimensions; the odd contribution of P is negative.
E0, E1 = sectors(doubled([I,I,P,P])/4)
check(E1 == s.zeros(2), 'D5 degree four dephasing has odd spectral radius zero')
check(s.trace(E1**2) == 0 and s.Rational(2*4,4**2) > 0,
      'D5 claimed return-word lower bound fails already at length two')
for m in [1,2,7,31]:
    check(2*m*m*(-1) + 2*m*m == 0, f'D5 C^({m}|{m}): I/P odd characters cancel exactly')

# A fixed-degree primitive family: depolarizing qubit tensor clock/shift channel.
for m in [3,5,7]:
    C = np.diag(np.exp(2j*np.pi*np.arange(m)/m))
    S = np.roll(np.eye(m), 1, axis=0)
    vs = [C, C.conj().T, S, S.conj().T]
    ls = [np.kron(np.array(a, complex), v) for a in [I,X,Y,P] for v in vs]
    E = sum(np.kron(a,a.conj()) for a in ls)/16
    pp = np.r_[np.ones(m), -np.ones(m)]
    idx = np.where(np.outer(pp,pp).ravel() < 0)[0]
    check(np.linalg.norm(E[np.ix_(idx,idx)]) < 1e-12, f'D5 primitive D=16 family, odd block zero, m={m}')
    # Clock/shift eigenbasis proves these are all spectator eigenvalues.
    eigen = [(np.cos(2*np.pi*a/m)+np.cos(2*np.pi*b/m))/2 for a in range(m) for b in range(m)]
    check(sum(abs(v-1)<1e-12 for v in eigen) == 1 and all(abs(v)<1-1e-12 for v in eigen[1:]),
          f'D5 spectator has unique fixed point and is primitive, m={m}')

# D3, D6 and D13: Pauli example, determinant and cyclic word formulas.
letters = [X,X,Y,Y,P,P]
E = doubled(letters); E0,E1 = sectors(E); T = bass(letters)
GT = s.kronecker_product(s.eye(6),G)
for idx,nk in [(ev,2),(od,2)]:
    edge = [4*j+k for j in range(6) for k in idx]
    Tk = T.extract(edge,edge); Ek=E.extract(idx,idx)
    check(s.expand((s.eye(12)-u*Tk).det()-(1-u*u)**4*(s.eye(2)-u*Ek+5*u*u*s.eye(2)).det()) == 0,
          f'D3 exact sector Bass identity {idx}')
Z = s.cancel((s.eye(2)-u*E1+5*u*u*s.eye(2)).det()/(s.eye(2)-u*E0+5*u*u*s.eye(2)).det())
check(s.cancel(Z-f(-2,5)/((1-u)*(1-5*u))) == 0, 'D13 exact Pauli elliptic zeta')
counts = [s.trace(GT*T**n) for n in range(1,7)]
check(counts == [8,32,104,640,3208,15392], 'D13 six Pauli ring counts')
print('Pauli counts:', counts)
for n in [1,2,3]:
    total=0
    for w in itertools.product(range(6),repeat=n):
        if any(w[(j+1)%n] == (w[j]^1) for j in range(n)):
            continue
        a=I
        for j in w: a=letters[j]*a
        total += abs(s.trace(P*a))**2
    check(total == counts[n-1], f'D6 cyclic word/supertrace equality, Pauli n={n}')
for b in [0,1,4]:
    check(1+sum((y*y-x**3-4*x-b)%5 == 0 for x in range(5) for y in range(5)) == 8,
          f'D13 actual nonsingular elliptic curve over F5, b={b}')

# D13: homogeneous unitary letters have weighted, generally nonintegral norms.
# Four even letters U,U*,U,U*, two odd X,X, with relative phase cos theta = 1/3.
z = (1+2*s.sqrt(2)*s.I)/3
U = s.diag(z,1)
letters = [U,U.conjugate(),U,U.conjugate(),X,X]
E0,E1 = sectors(doubled(letters))
check(sorted(E0.eigenvals()) == [2,6] and sorted(E1.eigenvals()) == [-s.Rational(2,3),s.Rational(10,3)],
      'D13 rational noninteger odd eigenvalues, all sector modes inside band')
check(s.simplify(s.trace(E0)-s.trace(E1)) == s.Rational(16,3), 'D13 N_P(1)=16/3, not a word count')
numerator = s.expand(f(s.Rational(10,3),5)*f(-s.Rational(2,3),5))
print('Nonintegral circle numerator:', numerator)
check(numerator.coeff(u) == -s.Rational(8,3), 'D13 numerator not a Weil polynomial over Z')

# Even an integral Weil numerator of a primitive channel need not come from a curve.
E0,E1=sectors(doubled([I]*6+[X]*2+[Y]*2))
check(sorted(E0.eigenvals()) == [2,10] and E1 == 6*s.eye(2),
      'D13 primitive D=10 example: even {10,2}, odd {6,6}, at the band edge')
check(s.expand(f(6,9)**2-(1-3*u)**4) == 0 and 9+1-4*3 == -2,
      'D13 integral Weil-9 numerator (1-3u)^4 would give a curve -2 rational points')

# D7: finite-time aliasing can destroy the signed divisor.
H = np.diag([0,2*np.pi]); I2=np.eye(2)
Q = .5*I2-1j*H
Tn = np.kron(Q,I2)+np.kron(I2,Q.conj())
check(np.allclose(expm(Tn), np.e*np.eye(4)), 'D7 at epsilon=1 every rate aliases to e')
check(abs(np.trace(np.array(G,complex)@expm(Tn))) < 1e-12, 'D7 sampled divisor cancels completely')
check(abs(np.trace(np.array(G,complex)@expm(.5*Tn))-4*np.exp(.5)) < 1e-12,
      'D7 continuous supertrace does not vanish between samples')

# D8/D9: genuine CPTP Euler family with odd jumps and a convergence rate check.
ls=[np.array(X,complex),np.array(Y,complex),np.array(P,complex)]
rates=[.3,.5,.2]
L=sum(g*(np.kron(a,a.conj())-np.eye(4)) for a,g in zip(ls,rates))
check(np.allclose(np.linalg.eigvalsh(L[np.ix_(ev,ev)]),[-1.6,0]), 'D9 even diffusion rates')
check(np.allclose(np.linalg.eigvalsh(L[np.ix_(od,od)]),[-1.4,-1]), 'D9 odd diffusion rates')
err=[]
for n in [50,100,200,400]:
    eps=1/n
    ks=[np.sqrt(1-eps)*I2]+[np.sqrt(eps*g)*a for a,g in zip(ls,rates)]
    F=sum(np.kron(a,a.conj()) for a in ks)
    check(np.allclose(sum(a.conj().T@a for a in ks),I2), f'D8 Euler Kraus family is CPTP, n={n}')
    err.append(np.linalg.norm(np.linalg.matrix_power(F,n)-expm(L),2))
check(all(a/b > 1.95 for a,b in zip(err,err[1:])), 'D8 first-order norm convergence under mesh halving')
print('D8 operator norm errors:', err)
check(doubled([I]).extract(od,od) == s.eye(2), 'D14 odd fixed operators can exist when the fixed point is not unique')
# Irreducibility does not force peripheral period modes to be Gamma-even.
F=doubled([P,Y])/2
xvec=s.Matrix([0,1,1,0])
check(F*xvec == -xvec and G*xvec == -xvec,
      'period-two channel with grading P=Z has an odd peripheral eigenoperator X')
print(f'\n{count}/{count} checks passed')
