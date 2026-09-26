#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane L (claude:opus, 2026-09-26).  Shared helpers, written independently of
scripts/rtp2_lattice_box.py.  (a_n, b_n) are read from zst exactly as scripts/rtp1_commutant.py does (a C printer
compiled at run time against zst/build/libzst.a; zst unchanged), with the prime cutoff X = x (true form) and X = 1
(pole + archimedean only, H0).  Loewner blocks follow plan.md section 1.3; the atom at y = log n is the Loewner form of
-delta(y - log n): a_j = -2 (1 - t) cos(2 pi j t), b_j = +(1/pi) sin(2 pi j t), t = log n / L.  No zeros are used."""
import os, subprocess, tempfile, functools
import mpmath as mp

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
C_SRC = r'''
#include <stdio.h>
#include <stdlib.h>
#include "zst.h"
int main(int argc, char **argv) {
    ulong X = strtoul(argv[1], 0, 10); slong N = atol(argv[2]); slong prec = atol(argv[3]); ulong XP = strtoul(argv[4], 0, 10);
    slong dig = atol(argv[5]);
    arb_t x; arb_ptr a = _arb_vec_init(N + 1), b = _arb_vec_init(N + 1); slong n;
    arb_init(x); arb_set_ui(x, X);
    zst_riemann_ab(a, b, N, x, XP, prec);
    for (n = 0; n <= N; n++) {
        flint_printf("%wd ", n);
        arb_printn(a + n, dig, ARB_STR_NO_RADIUS); flint_printf(" "); mag_printd(arb_radref(a + n), 3); flint_printf(" ");
        arb_printn(b + n, dig, ARB_STR_NO_RADIUS); flint_printf(" "); mag_printd(arb_radref(b + n), 3); flint_printf("\n");
    }
    return 0;
}
'''
_TD = tempfile.TemporaryDirectory()
_EXE = os.path.join(_TD.name, 'abprint')

def _build():
    z = os.path.join(REPO, 'zst'); src = os.path.join(_TD.name, 'p.c')
    open(src, 'w').write(C_SRC)
    cp = subprocess.run(['cc', '-O2', '-I' + os.path.join(z, 'include'), src, os.path.join(z, 'build', 'libzst.a'),
                         '-lflint', '-lmpfr', '-lgmp', '-lm', '-o', _EXE], capture_output=True, text=True)
    if cp.returncode: raise RuntimeError(cp.stderr)
_build()

@functools.lru_cache(None)
def zst_ab(X, N, XP, bits=1000, dig=220):
    out = subprocess.run([_EXE, str(X), str(N), str(bits), str(XP), str(dig)], capture_output=True, text=True).stdout
    a, b, rad = [], [], 0.0
    for line in out.strip().splitlines():
        t = line.split(); a.append(t[1]); b.append(t[3]); rad = max(rad, float(t[2]), float(t[4]))
    return tuple(a), tuple(b), rad

def blocks(a, b, N):
    """even (N+1) and odd (N) blocks, plan.md 1.3; a, b lists of mpf"""
    E = mp.matrix(N + 1, N + 1); O = mp.matrix(N, N); s2 = mp.sqrt(2)
    E[0, 0] = a[0]
    for j in range(1, N + 1):
        E[0, j] = E[j, 0] = s2 * b[j] / j
        E[j, j] = a[j] + b[j] / j; O[j - 1, j - 1] = a[j] - b[j] / j
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j:
                t = (b[i] - b[j]) / (i - j); u = (b[i] + b[j]) / (i + j)
                E[i, j] = t + u; O[i - 1, j - 1] = t - u
    return E, O

def atom_ab(N, t):
    return ([-2 * (1 - t) * mp.cos(2 * mp.pi * j * t) for j in range(N + 1)],
            [mp.sin(2 * mp.pi * j * t) / mp.pi for j in range(N + 1)])

def vonmangoldt(n):
    for p in range(2, n + 1):
        if n % p == 0:
            k = n
            while k % p == 0: k //= p
            return mp.log(p) if k == 1 else mp.mpf(0)
    return mp.mpf(0)

def setup(x, N):
    """returns H0 blocks, list of atom blocks for n = 2..x-1, w* list, true blocks from zst (X = x)"""
    L = mp.log(x)
    aT, bT, r1 = zst_ab(x, N, x); a0, b0, r0 = zst_ab(x, N, 1)
    H0 = blocks([mp.mpf(s) for s in a0], [mp.mpf(s) for s in b0], N)
    HT = blocks([mp.mpf(s) for s in aT], [mp.mpf(s) for s in bT], N)
    ns = list(range(2, x))
    T = [blocks(*atom_ab(N, mp.log(n) / L), N) for n in ns]
    w = [vonmangoldt(n) / mp.sqrt(n) for n in ns]
    return H0, T, w, HT, ns, max(r0, r1)

def combine(H0, T, w):
    E = H0[0].copy(); O = H0[1].copy()
    for wk, Tk in zip(w, T):
        if wk != 0: E += wk * Tk[0]; O += wk * Tk[1]
    return E, O
