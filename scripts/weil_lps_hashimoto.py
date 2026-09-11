"""Direct quantum Hashimoto (non-backtracking edge) operator for a Weil–LPS
channel block, and the Ihara–Bass factorisation checked on the actual operator.
Usage: python3 scripts/weil_lps_hashimoto.py p q [even|odd]"""
import sys, numpy as np, collections
sys.path.insert(0,'scripts')
from weil_lps import *
p=int(sys.argv[1]); q=int(sys.argv[2]); blk=sys.argv[3] if len(sys.argv)>3 else 'odd'
I,J=split_matrices(p); table,X,Z=weil_rep_table(p)
Q,S,Ws,err=build(p,q,table,X,Z,I,J)
Be,Bo=parity_blocks(p); B=Be if blk=='even' else Bo
Wb=[B.T@W@B for W in Ws]; n=B.shape[1]; D=q+1
# inverse pairing: generator a <-> conj(a)
inv=[Q.index(conj(a)) for a in Q]
N=n*n; T=np.zeros((N*D,N*D),complex)
for i in range(D):
    for j in range(D):
        if j!=inv[i]: T[j*N:(j+1)*N, i*N:(i+1)*N]=np.kron(Wb[i].conj(),Wb[i])
Phi=superop(Wb)
print(f'p={p}, q={q}, block={blk}: n={n}, edge operator dim {N*D}')
for u in (0.11, 0.2+0.07j, -0.23):
    lhs=np.linalg.det(np.eye(N*D)-u*T); rhs=(1-u*u)**(N*(D-2)/2)*np.linalg.det(np.eye(N)-u*D*Phi+q*u*u*np.eye(N))
    print(f'  Ihara-Bass at u={u}: |lhs/rhs - 1| = {abs(lhs/rhs-1):.1e}')
mu=np.linalg.eigvals(T); mods=collections.Counter(np.round(abs(mu),5))
print('  |mu| spectrum of the edge operator with multiplicities:', sorted(mods.items(),key=lambda t:-t[0]))
print(f'  sqrt(q) = {np.sqrt(q):.5f};  RH for the quantum Ihara zeta: {set(mods)<= {round(q,5),1.0,round(np.sqrt(q),5)}}')
