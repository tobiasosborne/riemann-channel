# Reviewer claude:opus-5.  T0.4: the cut rank of psi(Tr x^3) is BOUNDED in a self-dual normal basis.
# In a normal basis {b^{2^i}}, Tr(x^3)=Tr(x x^2)=sum_{i,j} x_i x_j c_{j+1-i}, c_k = Tr(b^{1+2^k}).
# Self-dual means Tr(b^{2^i} b^{2^j}) = delta_ij, i.e. c_k = delta_{k,0}, so Tr(x^3)= sum_i x_i x_{i-1}:
# a cyclic nearest-neighbour form, whose contiguous-cut polar block has F_2-rank <= 2, hence cut rank <= 4.
import sys, itertools
sys.path.insert(0,'scripts')
from artin_schreier_mps import irreducible, polypow, polymulmod, trace
def rank2(rows):
    a=[list(r) for r in rows]; r=0
    for j in range(len(a[0]) if a else 0):
        p=next((i for i in range(r,len(a)) if a[i][j]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        for i in range(len(a)):
            if i!=r and a[i][j]: a[i]=[x^y for x,y in zip(a[i],a[r])]
        r+=1
    return r
for n in range(3,12):
    f=irreducible(2,n)
    found=None
    for beta in itertools.product(range(2),repeat=n):
        if not any(beta): continue
        basis=[polypow(list(beta),2**j,f,2) for j in range(n)]
        if rank2(list(zip(*basis)))!=n: continue
        # self-dual?  Tr(b^{2^i} b^{2^j}) = delta_ij
        G=[[trace(polymulmod(basis[i],basis[j],f,2),f,2,n) for j in range(n)] for i in range(n)]
        if all(G[i][j]==(i==j) for i in range(n) for j in range(n)): found=(beta,basis); break
    if found is None:
        print(f"n={n}: no self-dual normal basis over F_2 (expected for n even, n%4!=2)"); continue
    beta,basis=found
    def Q(bits):
        x=[sum(bits[j]*basis[j][i] for j in range(n))%2 for i in range(n)]
        return trace(polypow(x,3,f,2),f,2,n)
    e=[[int(i==j) for i in range(n)] for j in range(n)]
    ranks=[]
    for k in range(1,n):
        B=[[Q([a^b for a,b in zip(e[i],e[j])])^Q(e[i])^Q(e[j]) for j in range(k,n)] for i in range(k)]
        ranks.append(2**rank2(B))
    print(f"n={n}: self-dual normal basis beta={beta}; cut ranks {ranks}")
