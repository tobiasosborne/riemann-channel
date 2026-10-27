#!/usr/bin/env python3
"""All MUB vectors, Gram matrices, and cross probabilities for p=3,5,7."""
import numpy as np

np.set_printoptions(precision=9, suppress=True, linewidth=160)


def run(p):
    zeta = np.exp(2j*np.pi/p)
    inv2 = pow(2, -1, p)
    bases = [('infinity/computational', np.eye(p, dtype=complex))]
    print(f'\np={p}; M=p Z_p x Z_p, C_M=L2(Z_p/p Z_p), Haar-normalised basis sqrt(p)*1_(x+pZ_p)')
    print('Basis infinity: coefficient matrix I_p (columns are states)')
    print(bases[0][1].real)
    for t in range(p):
        exponents = np.array([[(-inv2*t*x*x+b*x) % p for b in range(p)] for x in range(p)])
        basis = zeta ** exponents / np.sqrt(p)
        bases.append((f'slope {t}', basis))
        print(f'Basis slope {t}: coefficients zeta_p^E/sqrt(p), exponent matrix E=')
        print(exponents)
        # W_sym(1,t)f(x)=zeta^(t*x+t/2) f(x+1).
        T = np.zeros((p,p), complex)
        for x in range(p):
            T[x,(x+1)%p] = zeta ** ((t*x+inv2*t)%p)
        err = np.max(np.abs(T@basis-basis@np.diag(zeta**np.arange(p))))
        assert err < 1e-12
    orth = cross = 0.0
    for name, U in bases:
        gram = U.conj().T@U
        orth = max(orth,float(np.max(np.abs(gram-np.eye(p)))))
        print(f'Within-basis Gram, {name}, real part:')
        print(gram.real)
        print('imaginary part:')
        print(gram.imag)
    for i,(name,U) in enumerate(bases):
        for name2,V in bases[i+1:]:
            probabilities = np.abs(U.conj().T@V)**2
            cross = max(cross,float(np.max(np.abs(probabilities-1/p))))
            print(f'All cross-basis probabilities, {name} versus {name2}:')
            print(probabilities)
    assert orth < 1e-12 and cross < 1e-12
    print(f'SUMMARY p={p}: bases={len(bases)}, cross pairs={p*(p+1)//2}, expected probability={1/p:.17g}')
    print(f'max within Gram error={orth:.18g}; max cross probability error={cross:.18g}')


if __name__ == '__main__':
    print('NUMERICAL complex128, error tolerance 1e-12; exact proofs are in astra-proofs.md')
    for p in (3,5,7):
        run(p)
