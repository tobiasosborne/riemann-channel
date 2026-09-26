#!/usr/bin/env python3
"""REFUTE review of RTP-2 lane G (claude:opus, 2026-09-26). G4/G6 (a): the eleven uniform-grid infeasibility
certificates re-verified with the reviewer's own (a_n, b_n) (scratch_rtp2_grid_common.py; no zst, no lane code).

Certificate = PSD matrix Z = sum_i y_i v_i v_i^T + y_c e_0 e_0^T (the lane's frozen vectors and weights, read from
checks/farkas_*.in as exact decimals, so Z is PSD by construction whatever the vectors are). Dual function
q_Z(t) = tr(Z T(t)) = co . phi(t), cost = tr(Z H0) = co . (a0, b0), with co = K^*(Z) computed here by the
reviewer's closed form for the adjoint of the block assembly (tested against direct block evaluation).
If q_Z(t_j) <= 0 on every grid point and tr(Z H0) < 0, then tr(Z H(w)) < 0 for every w >= 0 on the grid, so
H(w) is never PSD. Any positive residual found at 40 digits is repaired by adding rho = max q_j^+ /(2(1-t_j))
to the constant-test weight (A_0(t) = -2(1-t) < 0 on the interior), which raises the cost by rho * a0_0;
the certificate stands iff the repaired cost is still negative (a rigorous margin argument, not a tolerance).
"""
import sys, json, random
import mpmath as mp
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from scratch_rtp2_grid_common import ab0, phi, blocks, LANE

COUNT = [0, 0]
def check(c, m):
    COUNT[0] += 1; COUNT[1] += (not c); print(('PASS ' if c else 'FAIL ') + m, flush=True)

def co_even(c, N):
    """moment coefficients of c^T E(a,b) c: returns (coA[0..N], coB[1..N])."""
    s2 = mp.sqrt(2)
    A = [c[0] ** 2] + [c[k] ** 2 for k in range(1, N + 1)]
    B = [mp.mpf(0)] * (N + 1)
    for k in range(1, N + 1):
        s = 2 * s2 * c[0] * c[k] / k + c[k] ** 2 / k
        acc = mp.fsum(c[j] * (mp.mpf(1) / (k - j) + mp.mpf(1) / (k + j)) for j in range(1, N + 1) if j != k)
        B[k] = s + 2 * c[k] * acc
    return A, B

def co_odd(c, N):
    """c indexed 1..N as c[0..N-1]."""
    A = [mp.mpf(0)] + [c[k - 1] ** 2 for k in range(1, N + 1)]
    B = [mp.mpf(0)] * (N + 1)
    for k in range(1, N + 1):
        acc = mp.fsum(c[j - 1] * (mp.mpf(1) / (k - j) - mp.mpf(1) / (k + j)) for j in range(1, N + 1) if j != k)
        B[k] = -c[k - 1] ** 2 / k + 2 * c[k - 1] * acc
    return A, B

def selftest(N=6):
    random.seed(1)
    a = [mp.mpf(random.uniform(-1, 1)) for _ in range(N + 1)]; b = [mp.mpf(0)] + [mp.mpf(random.uniform(-1, 1)) for _ in range(N)]
    E, O = blocks(a, b, N)
    ce = [mp.mpf(random.uniform(-1, 1)) for _ in range(N + 1)]; co = [mp.mpf(random.uniform(-1, 1)) for _ in range(N)]
    direct_e = (mp.matrix(ce).T * E * mp.matrix(ce))[0]; direct_o = (mp.matrix(co).T * O * mp.matrix(co))[0]
    Ae, Be = co_even(ce, N); Ao, Bo = co_odd(co, N)
    fe = mp.fsum(Ae[k] * a[k] for k in range(N + 1)) + mp.fsum(Be[k] * b[k] for k in range(1, N + 1))
    fo = mp.fsum(Ao[k] * a[k] for k in range(N + 1)) + mp.fsum(Bo[k] * b[k] for k in range(1, N + 1))
    check(abs(fe - direct_e) < 1e-30 and abs(fo - direct_o) < 1e-30, f'adjoint of block assembly: even/odd closed forms = direct quadratic forms ({mp.nstr(abs(fe-direct_e),3)}, {mp.nstr(abs(fo-direct_o),3)})')

def verify(x, N, M):
    lines = (LANE / f'farkas_x{x}_N{N}_M{M}.in').read_text().split('\n')
    hx, hN, hM = map(int, lines[0].split()); assert (hx, hN, hM) == (x, N, M)
    coA = [mp.mpf(0)] * (N + 1); coB = [mp.mpf(0)] * (N + 1); nneg = True
    for k in range(2 * N + 1):
        s = lines[1 + k].split(); par = int(s[0]); y = mp.mpf(s[1]); c = [mp.mpf(v) for v in s[2:]]
        nneg &= (y >= 0)
        assert len(c) == (N + 1 if par == 0 else N)
        A, B = (co_even if par == 0 else co_odd)(c, N)
        for n in range(N + 1):
            coA[n] += y * A[n]; coB[n] += y * B[n]
    yc = mp.mpf(lines[1 + 2 * N + 1].strip()); nneg &= (yc >= 0)
    coA[0] += yc                        # e_0 e_0^T contributes a_0 only
    a0, b0 = ab0(x, N)
    cost = mp.fsum(coA[n] * a0[n] for n in range(N + 1)) + mp.fsum(coB[n] * b0[n] for n in range(1, N + 1))
    ts = [mp.mpf(j) / M for j in range(1, M)]
    qs = []
    for t in ts:
        f = phi(N, t)
        qs.append(mp.fsum(coA[n] * f[n] for n in range(N + 1)) + mp.fsum(coB[n] * f[N + n] for n in range(1, N + 1)))
    err = mp.mpf(10) ** (-mp.mp.dps + 8)
    rho = max([mp.mpf(0)] + [(q + err) / (2 * (1 - t)) for q, t in zip(qs, ts)])
    repaired = cost + rho * a0[0] + err
    qmax = max(qs)
    # a crude 'where is the certificate positive' diagnostic: q_Z at the true atoms (tr(Z H_true) = cost - sum w q)
    L = mp.log(x)
    check(nneg and repaired < 0,
          f'x={x} N={N} M={M}: lane certificate valid with reviewer H0: weights>=0, max_j q_Z(t_j)={mp.nstr(qmax,3)}, '
          f'cost tr(ZH0)={mp.nstr(cost,12)}, repair rho={mp.nstr(rho,3)}, repaired cost={mp.nstr(repaired,12)}')
    return cost

if __name__ == '__main__':
    mp.mp.dps = 40
    selftest()
    table = {}
    for x, N, M in [(13, 20, 64), (13, 20, 128), (13, 20, 256), (13, 40, 64), (13, 40, 128), (13, 40, 256),
                    (13, 60, 64), (13, 60, 128), (13, 60, 256), (25, 60, 128), (25, 134, 128)]:
        table[(x, N, M)] = verify(x, N, M)
    lane = {(13,20,64):'-1.77218006360e-4',(13,20,128):'-5.22841053980e-5',(13,20,256):'-8.15313837417e-6',
            (13,40,64):'-1.76874875812e-4',(13,40,128):'-5.19936149409e-5',(13,40,256):'-7.99157226501e-6',
            (13,60,64):'-1.77041384553e-4',(13,60,128):'-5.15631496452e-5',(13,60,256):'-8.00093935025e-6',
            (25,60,128):'-8.49321221948e-5',(25,134,128):'-8.47189232157e-5'}
    bad = [k for k in lane if abs(table[k] / mp.mpf(lane[k]) - 1) > 1e-10]
    check(not bad, f'all eleven certificate costs agree with the report table to 1e-10 relative (mismatches: {bad})')
    print(f'# checks: {COUNT[0]} run, {COUNT[1]} failed')
