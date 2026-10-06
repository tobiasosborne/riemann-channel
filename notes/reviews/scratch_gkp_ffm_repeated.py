"""REFUTE scratch (scope of ff-dirichlet.md 2.3 'positive iff RH'): search squarefree moduli f for a
power-residue character whose P_chi has a repeated root (then E = Q(zeta)[x]/(P_chi) is not reduced and the
trace form Tr(x sigma y) is degenerate although RH holds)."""
from scratch_gkp_ffm_core import *
from scratch_gkp_ffm_phases import global_W
import sys
mp.mp.dps = 30
def factor(f, p):
    out = []; k = 1
    while len(f) > 1:
        found = False
        for k in range(1, len(f)):
            for g in irreducibles(k, p):
                qq, r = pdivmod(f, g, p)
                if not r:
                    out.append(g); f = qq; found = True; break
            if found: break
    return out
for (q, N, d) in ([] if "deg" in sys.argv else [(3, 2, 5), (3, 2, 6), (5, 4, 4), (5, 4, 5), (7, 3, 4), (7, 3, 5)]):
    hits = []; tot = 0
    for f in monics(d, q):
        fs = factor(f, q)
        if len(set(map(tuple, fs))) != len(fs): continue
        ch = Char(q, N, fs); Lam, even, n, W = global_W(ch); tot += 1
        if n < 2: continue
        r = mp.polyroots(Lam[::-1], maxsteps=300, extraprec=300)
        if min(abs(r[i]-r[j]) for i in range(n) for j in range(i)) < 1e-10:
            hits.append((f, fs, [mp.nstr(c, 5) for c in Lam]))
            if len(hits) >= 3: break
    print((q, N, d), 'squarefree moduli scanned', tot, 'repeated-root P_chi found:', len(hits))
    for h in hits: print('   f =', h[0], 'factors', h[1], 'Lambda', h[2])
    sys.stdout.flush()

# degree check on squarefree (possibly reducible) moduli: n = d-1 (odd) or d-2 (even)
if 'deg' in sys.argv:
    for (q, N, d) in [(5, 4, 3), (5, 4, 4), (7, 3, 3), (7, 3, 4), (3, 2, 5), (5, 2, 4)]:
        bad = 0; tot = 0
        for f in monics(d, q):
            fs = factor(f, q)
            if len(set(map(tuple, fs))) != len(fs): continue
            ch = Char(q, N, fs); Lam, even, n, W = global_W(ch); tot += 1
            bad += n != (d-2 if even else d-1)
        print('degree check', (q, N, d), 'squarefree moduli', tot, 'wrong degree', bad); sys.stdout.flush()
