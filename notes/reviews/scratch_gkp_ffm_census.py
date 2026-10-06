"""REFUTE scratch (ff-dirichlet.md 1.2, 3.2 B6, 3.5, and the scope of 'positive iff RH'):
census of power-residue characters chi mod irreducible f: RH, prod of page local phases = W, W=1 for N=2,
and a search for characters whose P_chi has a REPEATED root (non-reduced E)."""
from scratch_gkp_ffm_core import *
from scratch_gkp_ffm_phases import page_local, global_W
mp.mp.dps = 30
import sys
fams = [(5,4,3),(5,4,4),(7,3,3),(7,2,3),(3,2,4),(5,2,3),(3,2,5),(3,2,6),(5,2,5),(5,4,5)]
for (q,N,d) in fams:
    cnt=0; rhbad=0; prodbad=0; Ws=set(); rep=[]
    for f in irreducibles(d,q):
        ch=Char(q,N,[f]); Lam,even,n,W=global_W(ch)
        cnt+=1
        if n>0:
            r=mp.polyroots(Lam[::-1],maxsteps=300,extraprec=300)
            if max(abs(1/abs(x)-mp.sqrt(q)) for x in r)>1e-15: rhbad+=1
            mind=min([abs(r[i]-r[j]) for i in range(n) for j in range(i)]+[1])
            if mind<1e-8: rep.append((f,[mp.nstr(c,6) for c in Lam]))
        if abs(mp.fprod(page_local(ch))-W)>1e-20: prodbad+=1
        if N==2: Ws.add(round(float(W.real),6))
    print(f'(q,N,d)={(q,N,d)}: {cnt} chars, RH fails {rhbad}, prod(local) != W: {prodbad}', ('W values '+str(Ws)) if N==2 else '', f'; repeated roots in P_chi: {len(rep)}')
    for x in rep[:3]: print('    repeated:', x)
    sys.stdout.flush()
# X1 at infinity vs the quartic Dirichlet character mod 5 (chi_D(2)=i)
chiD={1:1,2:1j,4:-1,3:-1j}
tau=sum(chiD[c]*mp.exp(2j*mp.pi*c/5) for c in range(1,5))
WD=tau/(1j*mp.sqrt(5))
print('W(chi_D)=',mp.nstr(WD,6),' -i W(chi_D)=',mp.nstr(-1j*WD,6),' -tau/sqrt5=',mp.nstr(-tau/mp.sqrt(5),6))
