#!/usr/bin/env python3
"""Fable: independent recomputation of lane U's comparison C9 (E1: y^2 + xy = x^3 + 1 over F_2, k = 6, N = 7).
Curve side by PARI (elltatepairing), lattice side by hand: t_N(P, Q) = exp(2 pi i Omega(P~, (M^k - 1) Q~)) up to Aut(mu_7)."""
import subprocess, itertools, sympy as sp
gpsrc = r"""
t=ffgen(2^6,'t); E=ellinit([1,0,0,0,1],t); print("card|",ellcard(E)); print("grp|",ellgroup(E));
g=0; until(ellorder(E,g)==56, g=random(E));
\\ 2-Frobenius acts on the cyclic group as multiplication by f: find f with f*g = frob(g)
fr=[g[1]^2,g[2]^2]; f=0; for(c=1,56, if(ellmul(E,g,c)==fr, f=c; break)); print("f|",f);
w=ffprimroot(t)^((2^6-1)/7);
P=ellmul(E,g,8); z=elltatepairing(E,P,g,7)^((2^6-1)/7); e=-1; for(j=0,6, if(w^j==z, e=j; break)); print("e|",e);
"""
out = subprocess.run(["gp","-q","-f"], input=gpsrc, capture_output=True, text=True).stdout
d = dict(l.split("|") for l in out.splitlines() if "|" in l)
card, f, e = int(d["card"]), int(d["f"]), int(d["e"])
print("curve: #E(F_64) =", card, " group", d["grp"].strip(), " Frobenius = mult by", f, " Tate exponent e =", e)
M = sp.Matrix([[0,-1],[2,-1]]); A = sp.eye(2) - M**6; h = int(A.det())
print("lattice: det(1 - M^6) =", h)
# 7-part of Fix(M^6): v in (Z/7)^2 with A v = 0 mod 7
line = [v for v in itertools.product(range(7), repeat=2) if any(v) and all(int(x) % 7 == 0 for x in A*sp.Matrix(v))]
print("7-torsion fixed points:", len(line))
def act(v): return tuple(int(x) % 7 for x in M*sp.Matrix(v))
fp = {v: next(c for c in range(1,7) if tuple((c*x) % 7 for x in v) == act(v)) for v in line}
print("M acts on the 7-part as multiplication by", set(fp.values()), " (curve Frobenius mod 7:", f % 7, ")")
assert set(fp.values()) == {f % 7}, "no equivariant isomorphism"
def Om(v, w): return v[0]*w[1] - v[1]*w[0]
scales = set()
for u in line:                      # equivariant isos g -> u/7; P = 8g -> 8u/7 = u/7 mod L
    Au = A*sp.Matrix(u); up = tuple(int(x)//7 for x in Au)     # (1 - M^6) u = 7 u'
    x = (-Om(u, up)) % 7            # Omega(P~, (M^6 - 1) Q~) = -Omega(u/7, A u/7)*49/7 ... = -Omega(u,u')  (mod 7, times 1/7 -> exponent)
    s = next(s for s in range(1,7) if (e - s*x) % 7 == 0) if x % 7 else None
    scales.add(s)
sq = {1,2,4}
print("scales over the six isomorphisms:", sorted(scales), " one coset of the squares:", scales in (sq, {3,5,6}))
