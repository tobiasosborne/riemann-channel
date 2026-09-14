"""Shared finite phase model. No zeta-zero data are imported here.

All bases are in increasing order; doubled coordinates use C-order vec(rho),
so A (x) conjugate(A) implements rho -> A rho A^dagger.
"""
from pathlib import Path
import itertools
import json
import math
import numpy as np
import scipy.sparse as ss
import sympy as sp

SEED = 20260914
HERE = Path(__file__).resolve().parent


class Checks:
    def __init__(self, name):
        self.name, self.count = name, 0
        self.rng = np.random.default_rng(SEED)
        print(f"{name}; seed={SEED}", flush=True)

    def __call__(self, condition, message):
        self.count += 1
        assert bool(condition), f"FAIL {self.count}: {message}"
        print(f"  ok {self.count:4d}  {message}", flush=True)

    def finish(self, results):
        results = dict(seed=SEED, checks=self.count, **results)
        (HERE / f"{self.name}.json").write_text(json.dumps(results, indent=2) + "\n")
        print(f"all {self.count} checks passed", flush=True)
        return results


def primes(P):
    """Inclusive cutoff, unlike scripts/bcmpo.py's exclusive helper."""
    return [int(p) for p in sp.primerange(2, P + 1)]


def phi(b):
    return int(sp.totient(int(b)))


def divisors(B):
    return [int(b) for b in sp.divisors(B)]


def shell_jump(basis, p):
    """Compression P_B V_p P_B using S2, independently checked by verify_phase.py."""
    ix = {b: j for j, b in enumerate(basis)}
    rows, cols, vals = [], [], []
    for j, b in enumerate(basis):
        if b % p:
            rows.append(j); cols.append(j); vals.append(p**-0.5)
        if p*b in ix:
            rows.append(ix[p*b]); cols.append(j)
            vals.append(math.sqrt((p - 1)/p) if b % p else 1.)
    return ss.csr_matrix((vals, (rows, cols)), shape=(len(basis), len(basis)))


def shell_fourier(b, N):
    assert N % b == 0
    v = np.zeros(N, complex)
    for a in range(b):
        if math.gcd(a, b) == 1:
            v[(a*(N//b)) % N] = phi(b)**-0.5
    return v


def position_jump(N, p):
    """J: normalized Euclidean coordinates of Haar L2(Z/(N/p)) -> L2(Z/N).

    In function values this is sqrt(p) f(x/p) 1_{p|x}; normalized
    coordinates absorb sqrt(p), leaving J[p*y,y]=1.
    """
    assert N % p == 0
    M = N//p
    return ss.csr_matrix((np.ones(M), (p*np.arange(M), np.arange(M))), shape=(N, M))


def fourier_jump(N, p):
    assert N % p == 0
    M = N//p
    return ss.csr_matrix((np.full(N, p**-0.5), (np.arange(N), np.arange(N) % M)), shape=(N, M))


def galois_fourier(N, a):
    ai = pow(a, -1, N)
    return ss.csr_matrix((np.ones(N), ((ai*np.arange(N)) % N, np.arange(N))), shape=(N, N))


def maxabs(A):
    data = A.data if ss.issparse(A) else np.asarray(A)
    return float(np.max(np.abs(data), initial=0.))


def characters(b):
    """All characters of (Z/b)^x, extended by zero; explicit local cyclic factors.

    At 2^k, k>=3 use -1 and 5; at odd prime powers use a primitive root.
    Return (label, values[0:b]); no floating eigenspace clustering is used.
    """
    if b == 1:
        return [((), np.ones(1, complex))]
    factors = []
    for p0, k in sp.factorint(b).items():
        p, k = int(p0), int(k)
        q = p**k
        if p == 2 and k == 1:
            factors.append((q, [], {1: ()}))
        elif p == 2 and k >= 3:
            orders = [2, 2**(k - 2)]
            logs = {(pow(-1, u, q)*pow(5, v, q)) % q: (u, v)
                    for u in range(2) for v in range(orders[1])}
            factors.append((q, orders, logs))
        else:
            order = phi(q); g = int(sp.primitive_root(q))
            factors.append((q, [order], {pow(g, v, q): (v,) for v in range(order)}))
    orders = [order for _, oo, _ in factors for order in oo]
    result = []
    for label in itertools.product(*(range(order) for order in orders)):
        values = np.zeros(b, complex)
        for a in range(b):
            if math.gcd(a, b) != 1:
                continue
            logs = [v for q, _, ll in factors for v in ll[a % q]]
            angle = sum(j*v/order for j, v, order in zip(label, logs, orders))
            values[a] = np.exp(2j*np.pi*angle)
        result.append((label, values))
    return result


def gauss_vector(values, N):
    b = len(values)
    assert N % b == 0
    v = np.zeros(N, complex)
    for a in range(b):
        v[(a*(N//b)) % N] = values[a]/math.sqrt(phi(b))
    return v


def dissipator(A, rho):
    A = A.toarray() if ss.issparse(A) else A
    D = A.conj().T @ A
    return A @ rho @ A.conj().T - (D @ rho + rho @ D)/2


def lindblad_matrix(jumps):
    n = jumps[0].shape[0]
    I = ss.eye(n, format="csr")
    out = ss.csr_matrix((n*n, n*n), dtype=complex)
    for A in jumps:
        A = ss.csr_matrix(A)
        D = A.conj().T @ A
        out += ss.kron(A, A.conj()) - (ss.kron(D, I) + ss.kron(I, D.T))/2
    return out.tocsr()
