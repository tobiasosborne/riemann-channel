#!/usr/bin/env python3
"""One lattice, every prime: for 441d1 (CM by O_K = Z[(1+sqrt(-7))/2]) the step psi(p) acting on O_K in the basis (1, omega)
reproduces the group structure of E(F_{p^k}) and the Tate pairing of the reduction mod p, up to Aut(mu_N) (lane U's identities,
reused through its functions).  Fable, 2026-10-06; the epsilon-uniform identification of mu_N across primes is NOT attempted here."""
import re, sys, itertools
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
src = open(__file__.replace("check_cm_tower.py", "check_tower_pairing.py")).read()
exec(src[:src.index('print("== S.')])          # check(), GP_LIB, gp(), LatGroup, equivariant_isos, units, scales_for, Om2
from math import gcd

def snf(A):
    S = smith_normal_form(A, domain=sp.ZZ)
    return sorted(abs(int(S[i, i])) for i in range(S.shape[0]) if S[i, i] != 0 and abs(S[i, i]) != 1)

def step(u, v):                                   # multiplication by u + v*omega on O_K in the basis (1, omega), omega^2 = omega - 2
    return sp.Matrix([[u, -2 * v], [v, u + v]])

ap = {}
out = gp('E=ellinit("441d1"); print("ai|", vector(5,i,E[i])); forprime(p=2,40, if((-7)%p!=0 && kronecker(-7,p)==1, print("ap|", p, " ", ellap(E,p))));')
d = gp_lines(out)
ai = d["ai"][0]
for ln in d["ap"]:
    p, a = map(int, ln.split()); ap[p] = a
print("441d1 a-invariants", ai, " split primes and a_p:", ap)
check("P0 the split primes below 40 are 2, 11, 23, 29, 37 (kronecker(-7, p) = 1)", sorted(ap) == [2, 11, 23, 29, 37])

cases = [(2, 1), (2, 2), (2, 3), (2, 4), (11, 1), (11, 2), (23, 1), (29, 1), (37, 1)]
steps = {}
for p, a in ap.items():
    y = [y for y in range(1, 20) if 4 * p == a * a + 7 * y * y]
    check(f"P1 p={p}: 4p = a_p^2 + 7 y^2 has a solution (a_p = {a})", len(y) == 1)
    y = y[0]
    u = (a - y) // 2
    M = step(u, y); Mc = step(u + y, -y)         # psi(p) and its conjugate
    check(f"P2 p={p}: M = mult by (a_p + y sqrt(-7))/2 has det p and trace a_p; Omega-similitude M^T Omega M = p Omega", M.det() == p and M.trace() == a
          and Mc.det() == p and (M.T * sp.Matrix([[0, 1], [-1, 0]]) * M == p * sp.Matrix([[0, 1], [-1, 0]])))
    steps[p] = (M, Mc)
allM = [steps[p][0] for p in steps]
check("P3 all the steps psi(p) commute with each other (one lattice, one commuting family)", all(A * B == B * A for A in allM for B in allM))
JK = sp.Matrix([[-1, -4], [2, 1]])               # 2 omega - 1 = sqrt(-7): JK = mult by sqrt(-7) / sqrt 7 is not integral; use I = (2 omega - 1) with I^2 = -7
check("P4 the vacuum: I = mult by sqrt(-7) satisfies I^2 = -7 and commutes with every step (J_K = I/sqrt 7)", JK ** 2 == -7 * sp.eye(2) and all(JK * A == A * JK for A in allM))

print("\n== groups and pairings, reduction mod p against the lattice O_K with the step psi(p)")
for p, k in cases:
    M, Mc = steps[p]
    h = int((sp.eye(2) - M ** k).det())
    body = f'E=ellinit({ai}); t=ffgen({p}^{k},\'t); Et=ellinit(vector(5,i,E[i]),t); print("grp|", ellgroup(Et)); print("card|", ellcard(Et));'
    d = gp_lines(gp(body))
    card = int(d["card"][0]); grp = sorted(int(x) for x in re.findall(r"\d+", d["grp"][0]))
    lat = snf(sp.eye(2) - M ** k)
    check(f"G p={p} k={k}: #E(F_{{{p}^{k}}}) = det(1 - M^k) = {h}; group {grp} = Smith form of 1 - M^k {lat}", card == h and grp == lat)
    # pairings, l-primary parts
    for l in sorted({f for f, _ in sp.factorint(h).items()}):
        e = sp.multiplicity(l, h)
        N = l ** min(e, sp.multiplicity(l, p ** k - 1)) if sp.multiplicity(l, p ** k - 1) > 0 else 1
        if N < 2:
            continue
        out = gp(f'E=ellinit({ai}); r=cdata(vector(5,i,E[i]),{p},{k},{l},{N},0); print("c|", r);')
        r = eval(gp_lines(out)["c"][0].replace("~", ""))
        os, F, Tm, We = r[0], r[1], r[2], r[3]
        if Tm == -1:
            continue
        matched = None
        for which, Mm in (("psi", M), ("psi-bar", Mc)):
            G = LatGroup(Mm, k, l)
            phis = equivariant_isos(os, F, G)
            if not phis:
                continue
            per, union = scales_for(os, Tm, We, G, phis, N, "tate")
            if union:
                matched = (which, len(phis), sorted(union))
                break
        check(f"T p={p} k={k} l={l} N={N}: a Frobenius-equivariant isomorphism E(F_{{p^k}})_l -> O_K/(1-M^k) exists for the step {matched[0] if matched else '?'} "
              f"and the Tate pairing equals the code commutator c(P~,(M^k-1)Q~) up to Aut(mu_N) (scales {matched[2] if matched else None}; {matched[1] if matched else 0} isos)",
              matched is not None)
print(f"\n{npass} of {npass + nfail} pass   ({time.time() - T0:.1f} s)")
