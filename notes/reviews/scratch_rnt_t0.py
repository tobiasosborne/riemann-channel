# Reviewer claude:opus-5.  T0.1/T0.2: are all eigenvalues of E_g/sqrt(q) roots of unity?
import sys, numpy as np
sys.path.insert(0,'scripts')
from artin_schreier_mps import transfer
CASES = [(3,[0,1]),(3,[1,1]),(3,[0,1,1]),(3,[0,0,1]),(3,[1,0,1]),(3,[2,1]),
         (5,[0,1]),(5,[1,1]),(5,[0,1,1]),(5,[2,0,1]),(5,[1,2,1]),
         (7,[0,1]),(7,[1,1]),(7,[0,1,1]),(7,[3,1,1])]
worst=0.0
for q,a in CASES:
    E=transfer(q,a); U=E/np.sqrt(q)
    uni = np.max(np.abs(U@U.conj().T-np.eye(U.shape[0])))
    lam=np.linalg.eigvals(U)
    # order: smallest h<=4000 with U^h = 1
    h=None; Uk=np.eye(U.shape[0],dtype=complex)
    for k in range(1,4001):
        Uk=Uk@U
        if np.max(np.abs(Uk-np.eye(U.shape[0])))<1e-8: h=k; break
    modmax=np.max(np.abs(np.abs(lam)-1))
    # each eigenvalue a root of unity: lam^h = 1
    rootres = np.max(np.abs(lam**h-1)) if h else np.nan
    print(f"  q={q} a={a} J={len(a)-1} dim={U.shape[0]}: ||UU*-1||={uni:.1e}  order h={h}  max||lam|-1|={modmax:.1e}  max|lam^h-1|={rootres:.1e}")
    worst=max(worst,modmax, rootres if h else 1.0)
print("  worst deviation:", worst)
