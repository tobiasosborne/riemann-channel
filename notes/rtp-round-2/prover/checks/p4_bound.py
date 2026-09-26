#!/usr/bin/env python3
"""Arithmetic of the explicitly conditional H-BPR/H-LOG2 bound; no QE run."""
import math
import mpmath as mp
mp.mp.dps=100
mp.iv.dps=80

def data(d):
    k=4*d**4+d*d+1
    degree=max(2*d*d,3)
    s=2**(2*d*d)+2**d+2*d*d
    tau=32*d**4
    q=2*s*degree
    # D = q ** (2 ** (k+1)); B = 10 ** (-200000*(tau+2)*D**4).
    # We store log10(-log10 B), never D or B themselves.
    E=mp.log10(200000*(tau+2))+mp.power(2,k+3)*mp.log10(q)
    EI=mp.iv.log(mp.iv.mpf(200000*(tau+2)),10)+mp.iv.mpf(2)**(k+3)*mp.iv.log(mp.iv.mpf(q),10)
    power=int(mp.floor(mp.log10(E)))
    mantissa=int(mp.ceil(E/mp.power(10,power-7)))
    upper_text=f'{mantissa}e{power-7}'
    assert EI < mp.iv.mpf(upper_text)
    # Verify the declared input coefficient bit bound with exact integers.
    M=2*d*d
    assert 2**M*math.factorial(M) < 2**tau
    assert 8*d*d+2 < 2**tau
    assert 64*d**5+5 < 2**tau
    return k,degree,s,tau,E,upper_text

print('H-BPR full CAD projection and H-LOG2 are hypotheses; the coefficient envelope is derived in the note, not tested here.')
print('Exact formula: B(d)=10^[-200000*(tau+2)*(2*s*degree)^(2^(k+3))].')
for d in (2,3,4,8):
    k,degree,s,tau,E,upper=data(d)
    print(f'd={d}; k={k}; degree={degree}; s={s}; tau={tau}')
    print('  E=log10(-log10 B)=',mp.nstr(E,18))
    print('  conservative decimal lower bound = 10^(-10^('+upper+'))')
    print('  log10(E)=',mp.nstr(mp.log10(E),18))
print('PASS: exact input-height inequalities; 80-digit interval verification of conservative rounded exponents.')
