#!/usr/bin/env python3
"""X1: is the termwise criterion Re nu_l <= nu_0 equivalent to positive definiteness /
boundedness for a finite exponential sum?  And is Huang's h_k exactly nu_0 - nu_k?
Reviewer claude:opus, 2026-09-12."""
import numpy as np, itertools
rng = np.random.default_rng(2718)

print("=" * 78); print("X1(a)  does Re nu_l <= nu_0 for all l >= 1 force |z| <= 1 ?"); print("=" * 78)
print("  conjugate pair z = R e^{+-i theta}: nu_l = 2 R^l cos(l theta), nu_0 = 2.")
print("  (iii) would need cos(l theta) <= R^{-l} for EVERY l >= 1.")
worst = 0
for R in (1.001, 1.01, 1.1, 1.5):
    for th in (0.1, 1.0, np.pi / 2, 2.0, 3.0, np.pi - 1e-3, np.pi * (1 - 1e-4), np.sqrt(2), np.pi * 2 * 0.6180339887):
        first = None
        for l in range(1, 400001):
            if 2 * R ** l * np.cos(l * th) > 2 + 1e-12:
                first = l; break
        worst = max(worst, first if first else 10 ** 9)
        print(f"    R={R:<6} theta={th:.6f}: first l with Re nu_l > nu_0 = {first}")
print(f"  largest first-failure index seen: {worst}   (no counterexample: (iii) => (ii) holds)")

print()
print("  random multisets with max |z| = R > 1, three to six modes:")
bad = 0
for trial in range(400):
    d = int(rng.integers(2, 7)); Z = []
    for _ in range(d):
        if rng.random() < 0.5:
            z = rng.uniform(0.1, 0.99) * np.exp(2j * np.pi * rng.uniform()); Z += [z, np.conj(z)]
        else:
            z = rng.uniform(1.001, 1.3) * np.exp(2j * np.pi * rng.uniform()); Z += [z, np.conj(z)]
    if max(abs(z) for z in Z) <= 1: continue
    nu0 = len(Z); first = None
    for l in range(1, 20001):
        if sum(z ** l for z in Z).real > nu0 + 1e-9: first = l; break
    if first is None: bad += 1; print("    NO FAILURE within l<=20000 for", Z)
print(f"  multisets with a mode outside the circle for which Re nu_l <= nu_0 held up to l=20000: {bad}")
print("  reason: the closure of {(z_j/|z_j|)^l} is a compact group, so (z_j/R)^l returns arbitrarily")
print("  close to (1,...,1) for infinitely many l >= 1, giving Re nu_l ~ (sum m_j) R^l -> +infinity.")
# explicit recurrence demonstration
for th in (1.0, np.sqrt(2), np.pi * 2 * 0.6180339887):
    ls = [l for l in range(1, 5000) if np.cos(l * th) > 0.9]
    print(f"    theta={th:.6f}: #{{l<5000 : cos(l theta) > 0.9}} = {len(ls)}, first few {ls[:6]}")

print(); print("=" * 78); print("X1(b)  the termwise bound does NOT imply positive definiteness for a general sequence")
print("=" * 78)
for nu in ([1, 0.9, -1], [1, 1j, -1], [1, 0.5, 0.5, -1]):
    L = len(nu) - 1
    v = np.array([np.conj(nu[abs(k)]) if k < 0 else nu[k] for k in range(-L, L + 1)], dtype=complex)
    idx = np.arange(L + 1); K = idx[:, None] - idx[None, :]
    M = v[K + L]; ev = np.linalg.eigvalsh((M + M.conj().T) / 2)
    print(f"  nu = {nu}: |nu_l| <= nu_0 holds = {all(abs(x)<=abs(nu[0])+1e-12 for x in nu)};"
          f"  Toeplitz eigenvalues {np.round(ev,4)} -> PD = {ev.min() > -1e-12}")
print("  so (iii) <=> (i) uses the finite-exponential-sum structure, not just the sequence bound.")

print(); print("=" * 78); print("X1(c)  Huang 2019:  h_k  ==  nu_0 - nu_k  for (q+1)-regular graphs?"); print("=" * 78)
def hashimoto(adj):
    n = len(adj); edges = [(u, v) for u in range(n) for v in range(n) if adj[u][v]]
    idx = {e: i for i, e in enumerate(edges)}; E = len(edges)
    B = np.zeros((E, E))
    for (u, v) in edges:
        for (x, y) in edges:
            if v == x and y != u: B[idx[(x, y)], idx[(u, v)]] = 1
    return B, edges
def graph_check(name, adj):
    n = len(adj); A = np.array(adj, float); deg = int(A.sum(1)[0]); q = deg - 1
    m = int(A.sum() // 2); B, _ = hashimoto(adj)
    lam = np.sort(np.linalg.eigvalsh(A))[::-1]
    bip = abs(lam[-1] + deg) < 1e-9
    spB = np.linalg.eigvals(B)
    # trivial multiset: +-1 with multiplicity m-n, and the pair {q,1} from lambda = q+1
    triv = [1.0] * (m - n) + [-1.0] * (m - n) + [float(q), 1.0]
    rem = list(spB)
    for s in triv:
        j = int(np.argmin([abs(s - y) for y in rem])); rem.pop(j)
    nu0 = len(rem); r = np.sqrt(q)
    print(f"  {name}: n={n} deg={deg} q={q} m={m} bipartite={bip}; |spec B|={len(spB)}; retained {nu0} (2(n-1)={2*(n-1)})")
    nontriv = [l for l in lam if abs(abs(l) - deg) > 1e-9]
    ram = max(abs(np.array(nontriv))) <= 2 * np.sqrt(q) + 1e-9
    print(f"     nontrivial adjacency eigenvalues in [{min(nontriv):.4f},{max(nontriv):.4f}], 2 sqrt q = {2*np.sqrt(q):.4f} -> Ramanujan={ram}")
    ok = True
    for k in range(1, 13):
        Nk = np.trace(np.linalg.matrix_power(B, k)).real
        if k % 2 == 1: hk = 2 * (n - 1) + q ** (k / 2) + q ** (-k / 2) - q ** (-k / 2) * Nk
        else:          hk = 2 * (n - 1) + q ** (k / 2) + q ** (-k / 2) - q ** (-k / 2) * (Nk - n * (q - 1))
        nuk = sum((z / r) ** k for z in rem).real
        if abs(hk - (nu0 - nuk)) > 1e-6 * max(1, abs(hk)): ok = False
        if k <= 6:
            print(f"     k={k}: N_k={Nk:12.2f}  h_k={hk:+12.6f}   nu_0-nu_k={nu0-nuk:+12.6f}   diff={hk-(nu0-nuk):+.2e}")
    hks = []
    for k in range(1, 25):
        Nk = np.trace(np.linalg.matrix_power(B, k)).real
        hks.append(2*(n-1) + q**(k/2) + q**(-k/2) - q**(-k/2)*(Nk if k % 2 else Nk - n*(q-1)))
    print(f"     h_k = nu_0 - nu_k for k=1..12: {ok};  min_k h_k (k<=24) = {min(hks):+.6f};  "
          f"max retained |mu| = {max(abs(z) for z in rem):.6f} vs sqrt q = {r:.6f}")
K4 = [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]
graph_check("K_4", K4)
pet = np.zeros((10,10),int)
outer=[(0,1),(1,2),(2,3),(3,4),(4,0)]; inner=[(5,7),(7,9),(9,6),(6,8),(8,5)]; spokes=[(i,i+5) for i in range(5)]
for u,v in outer+inner+spokes: pet[u][v]=pet[v][u]=1
graph_check("Petersen", pet.tolist())
K5 = [[1 if i!=j else 0 for j in range(5)] for i in range(5)]
graph_check("K_5 (4-regular)", K5)
# a cubic non-Ramanujan graph: two copies of K_4 minus an edge, joined by two bridges
g = np.zeros((8,8),int)
for u,v in [(0,2),(0,3),(1,2),(1,3),(2,3)]: g[u][v]=g[v][u]=1
for u,v in [(4,6),(4,7),(5,6),(5,7),(6,7)]: g[u][v]=g[v][u]=1
for u,v in [(0,4),(1,5)]: g[u][v]=g[v][u]=1
graph_check("2x(K4-e) joined", g.tolist())

# a genuinely NON-Ramanujan cubic graph: the circular ladder CL_21 = C_21 x K_2
# (non-bipartite since 21 is odd; lambda_2 = 2 cos(2 pi/21) + 1 = 2.911 > 2 sqrt 2)
nn = 21; g = np.zeros((2 * nn, 2 * nn), int)
for i in range(nn):
    for s_ in (0, 1):
        j = (i + 1) % nn
        g[i + s_ * nn][j + s_ * nn] = g[j + s_ * nn][i + s_ * nn] = 1
    g[i][i + nn] = g[i + nn][i] = 1
graph_check("circular ladder CL_21", g.tolist())
print()
print("  and the Toeplitz form of the SAME nu (r = sqrt q, trivial removed) for CL_21:")
A_ = np.array(g, float); n_ = 42; q_ = 2; m_ = 63
B_, _ = hashimoto(g.tolist()); spB_ = np.linalg.eigvals(B_)
triv_ = [1.0] * (m_ - n_) + [-1.0] * (m_ - n_) + [float(q_), 1.0]
rem_ = list(spB_)
for s_ in triv_:
    j_ = int(np.argmin([abs(s_ - y) for y in rem_])); rem_.pop(j_)
for L in (20, 60, 200):
    nul = np.array([sum((z / np.sqrt(q_)) ** l for z in rem_) if l else complex(len(rem_)) for l in range(L + 1)])
    v = np.concatenate([np.conj(nul[:0:-1]), nul]); idx = np.arange(L + 1); Kk = idx[:, None] - idx[None, :]
    M = v[Kk + L]
    print(f"    L={L}: min Toeplitz eigenvalue = {np.linalg.eigvalsh((M+M.conj().T)/2).min():+.4e}")
