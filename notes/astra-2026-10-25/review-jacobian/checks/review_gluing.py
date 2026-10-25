#!/usr/bin/env python3
"""Independent PARI integer-kernel calculation of the three glued lattices."""
import sys,subprocess,json
from pathlib import Path
try:from cypari2 import Pari
except ImportError:
    raise SystemExit(subprocess.call(['/tmp/claude-1000/-home-tobias-Projects-riemann-channel/venv-astra/bin/python',__file__]))
HERE=Path(__file__).resolve().parent

def main():
    p=Pari();data=json.loads((HERE.parents[2]/'astra-2026-10-23/jacobian/checks/output_fluxes.json.txt').read_text())
    for name,mask in [('K4',1),('Petersen',22),('K5',13)]:
        r=next(r for r in data if r['graph']==name and r['mask']==mask);n=r['n'];q=r['p'];A=r['A']
        F=p.matrix(2*n,2*n,[A[i][j] if i<n and j<n else (-q if i<n and j==i+n else (1 if i>=n and j==i-n else 0)) for i in range(2*n) for j in range(2*n)])
        Om=p.matrix(2*n,2*n,[(1 if i<n and j==i+n else (-1 if i>=n and j==i-n else 0)) for i in range(2*n) for j in range(2*n)])
        I=p.matid(2*n)
        ops=[F**2-F+2*I,F**2+F+2*I,F**4-F**2+4*I] if name=='K4' else [F**2+q*I,F**4+(2*q-5)*F**2+q*q*I]
        bases=[p.matkerint(op) for op in ops]
        assert all(op*b==0*op*b for op,b in zip(ops,bases))
        combined=bases[0]
        for b in bases[1:]:combined=p.matconcat([combined,b])
        idx=abs(int(p.matdet(combined)));ranks=[int(b.ncols()) for b in bases];dets=[int(p.matdet(b.mattranspose()*Om*b)) for b in bases]
        print(f'{name}:{mask} PARI integer-kernel ranks={ranks}; splitting index={idx}; restricted Omega determinants={dets}')
        assert idx=={'K4':16,'Petersen':15625,'K5':25}[name]

if __name__=='__main__':main()
