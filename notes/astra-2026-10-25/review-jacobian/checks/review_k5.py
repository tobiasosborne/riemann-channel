#!/usr/bin/env python3
"""PARI witnesses and a different exhaustive F3 search via f mod (x^9-x).
Run with python3; relaunches with the already-installed cypari2 interpreter.
N2=20 forces every fiber above P1(F9) to split. Enumerate allowed residues,
then all degree-3 quotients, and compute each smooth survivor's PARI charpoly.
"""
import sys, subprocess, json, itertools
from pathlib import Path
try:
    from cypari2 import Pari
except ImportError:
    raise SystemExit(subprocess.call(['/tmp/claude-1000/-home-tobias-Projects-riemann-channel/venv-astra/bin/python',__file__]+sys.argv[1:]))

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parents[2]/'astra-2026-10-23'/'jacobian'/'checks'

def main():
    pari=Pari();pari.allocatemem(128000000,silent=True)
    data=json.loads((SOURCE/'output_fluxes.json.txt').read_text())
    tar={r['mask']:tuple(r['weil_coefficients']) for r in data if r['graph']=='K5' and r['ramanujan']}
    witness={1:[1,0,2,0,0,0,2,0,0,0,2,0,1],3:[1,0,0,0,2,0,2,0,2,0,0,0,1],11:[1,0,1,0,0,0,1,0,0,0,1,0,1],12:[2,2,0,2,2,1,0,0,1,0,0,0,1],13:[2,2,1,0,2,0,2,1,1,1,0,1,1]}
    def pol(c):return pari.Polrev(c)*pari.Mod(1,3)
    def cp(f):
        W=pari.hyperellcharpoly(f)
        return W,tuple(int(W.polcoef(i)) for i in range(10,-1,-1))
    for mask,c in witness.items():
        f=pol(c);assert f.gcd(f.deriv()).poldegree()==0
        W,w=cp(f);assert w==tar[mask]
        print(f'K5:{mask} PARI W(x)={W}; P(u) low-to-high={list(w)}; MATCH',flush=True)
    # Independent F9 arithmetic, encoding a+3b with z²=-1.
    add=[[((a%3+b%3)%3)+3*((a//3+b//3)%3) for b in range(9)] for a in range(9)]
    mul=[[((a%3*(b%3)-a//3*(b//3))%3)+3*((a%3*(b//3)+a//3*(b%3))%3) for b in range(9)] for a in range(9)]
    squares={mul[y][y] for y in range(1,9)}
    def ev(c,x):
        r=0
        for a in reversed(c):r=add[mul[r][x]][a]
        return r
    residues=[]
    for r in itertools.product(range(3),repeat=9):
        vals=[ev(r,x) for x in range(9)]
        if all(v in squares for v in vals):residues.append((r,vals[:3]))
    print('degree<9 residues with every F9 value a nonzero square='+str(len(residues)),flush=True)
    hits={m:[] for m in tar};singular=survivors=0
    for r,base in residues:
        for lo in itertools.product(range(3),repeat=3):
            for lead in (1,2):
                if 2*(sum(v==1 for v in base)+(lead==1))!=4:continue
                survivors+=1;g=lo+(lead,);c=list(r)+[0]*4
                for j,a in enumerate(g):c[j+9]=(c[j+9]+a)%3;c[j+1]=(c[j+1]-a)%3
                f=pol(c)
                if f.gcd(f.deriv()).poldegree()>0:singular+=1;continue
                W,w=cp(f)
                for mask,target in tar.items():
                    if w==target:hits[mask].append(c)
    print(f'N1=4,N2=20 equations={survivors}; singular={singular}; smooth PARI computations={survivors-singular}')
    old=json.loads((SOURCE/'output_hyperelliptic_f3.json.txt').read_text())
    for m,hh in hits.items():
        assert sorted(hh)==sorted(old['hits'][str(m)])
        print(f'K5:{m} independent matching equations={len(hh)}; complete set matches original',flush=True)
    print('Search covers all 2*3^12=1062882 degree-12 equations by unique quotient/remainder; degree 11 cannot have N2=20.')
    (HERE/'output_independent_k5.json.txt').write_text(json.dumps(dict(residues=len(residues),N1N2_survivors=survivors,singular=singular,hits=hits),indent=2)+'\n')

if __name__=='__main__':main()
