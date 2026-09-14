# Author: codex:gpt-6-astra
# Run with PYTHONDONTWRITEBYTECODE=1 timeout 35s python3, from the repo root.
import sys, itertools
sys.path.insert(0, 'scripts')
from artin_schreier_mps import irreducible, polypow, trace

def rank2(rows):
    a = [list(r) for r in rows]
    r = 0
    for j in range(len(a[0]) if a else 0):
        p = next((i for i in range(r, len(a)) if a[i][j]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        for i in range(len(a)):
            if i != r and a[i][j]:
                a[i] = [x ^ y for x, y in zip(a[i], a[r])]
        r += 1
    return r

for n in range(1, 9):
    f = irreducible(2, n)
    for beta in itertools.product(range(2), repeat=n):
        basis = [polypow(list(beta), 2**j, f, 2) for j in range(n)]
        if rank2(list(zip(*basis))) == n:
            break
    def Q(bits):
        x = [sum(bits[j]*basis[j][i] for j in range(n)) % 2
             for i in range(n)]
        return trace(polypow(x, 3, f, 2), f, 2, n)
    e = [[int(i == j) for i in range(n)] for j in range(n)]
    ranks = []
    for k in range(1, n):
        B = [[Q([x ^ y for x, y in zip(e[i], e[j])]) ^ Q(e[i]) ^ Q(e[j])
              for j in range(k, n)] for i in range(k)]
        ranks.append(2**rank2(B))
    print(n, f, beta, ranks)
