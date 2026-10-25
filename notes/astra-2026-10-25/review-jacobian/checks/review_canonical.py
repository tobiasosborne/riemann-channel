#!/usr/bin/env python3
"""Direct targeted count on all three quadrics in a different quotient basis.
No Walsh transform; independently row-reduced cubic quotient with low pivots.
"""
import itertools,json
from pathlib import Path
import numpy as np
import sympy as s
from review_k4 import field
from review_genus6 import projective,powers,evaluations,parity

HERE=Path(__file__).resolve().parent
vs=s.symbols('X Y Z T')
mons=[e for e in itertools.product(range(4),repeat=4) if sum(e)==3]
qs=[[(1,1,0,0),(0,0,1,1)],[(1,1,0,0),(0,0,2,0),(0,0,1,1),(0,0,0,2)],[(1,1,0,0),(0,0,2,0)]]

def expression(ms):return sum(s.prod(v**e for v,e in zip(vs,m)) for m in ms)

def basis(Q):
    rows={}
    for i in range(4):
        r=sum(1<<mons.index(tuple(e+(i==j) for j,e in enumerate(m))) for m in Q)
        while r:
            pivot=(r&-r).bit_length()-1
            if pivot in rows:r^=rows[pivot]
            else:rows[pivot]=r;break
    assert len(rows)==4
    return [m for i,m in enumerate(mons) if i not in rows],rows

def main():
    all_hits=[]
    for qi,Q in enumerate(qs,1):
        B,rows=basis(Q);masks=np.arange(1<<16,dtype=np.uint32)
        for k,tar in enumerate((3,9,9,29),1):
            m=field(k)[1];pw=powers(m);counts=np.zeros(len(masks),dtype=np.int32)
            for pt in projective(len(m),4):
                value=0
                for v in evaluations(pt,Q,m,pw):value^=v
                if value:continue
                vals=evaluations(pt,B,m,pw)
                constraints={sum(1<<i for i,v in enumerate(vals) if v>>j&1) for j in range(k)}-{0}
                ok=np.ones(len(masks),dtype=bool)
                for row in constraints:
                    v=masks&row;v=v^(v>>16);v=v^(v>>8);ok&=parity[v&255]==0
                counts+=ok
            masks=masks[counts==tar]
            print(f'Q{qi} k={k} direct surviving cubic classes={len(masks)}',flush=True)
        QE=expression(Q);smooth=[]
        for mask in masks:
            C=expression([mon for j,mon in enumerate(B) if int(mask)>>j&1]);good=True
            for i in range(4):
                av=[v for j,v in enumerate(vs) if i!=j];q=QE.subs(vs[i],1);c=C.subs(vs[i],1)
                minors=[s.diff(q,a)*s.diff(c,b)-s.diff(q,b)*s.diff(c,a) for a,b in itertools.combinations(av,2)]
                if list(s.groebner([q,c]+minors,*av,modulus=2))!=[1]:good=False;break
            if good:smooth.append(dict(quadric=qi,mask=int(mask),C=str(C)))
        print(f'Q{qi}: smooth matches={len(smooth)}',flush=True)
        all_hits.extend(smooth)
        # Convert all source hits to this different quotient basis and compare.
        old=json.loads((HERE.parents[2]/'astra-2026-10-23/jacobian/checks/output_trigonal.json.txt').read_text())
        old_masks=[]
        for r in old:
            if r['quadric']!=qi:continue
            poly=s.Poly(s.sympify(r['C'],locals=dict(zip(('X','Y','Z','T'),vs))),*vs,modulus=2)
            v=sum(1<<mons.index(mon) for mon,c in poly.terms() if int(c)%2)
            for pivot,row in sorted(rows.items()):
                if v>>pivot&1:v^=row
            old_masks.append(sum(1<<j for j,mon in enumerate(B) if v>>mons.index(mon)&1))
        assert sorted(old_masks)==sorted(r['mask'] for r in smooth)
    print('TOTAL independent smooth matching cubic quotient classes='+str(len(all_hits)),flush=True)
    (HERE/'output_independent_canonical.json.txt').write_text(json.dumps(all_hits,indent=2)+'\n')

if __name__=='__main__':main()
