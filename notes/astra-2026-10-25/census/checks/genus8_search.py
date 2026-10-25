#!/usr/bin/env python3
"""Exhaustive genus-eight trigonal search, exact arithmetic.

F_e divisor 3S+bF has genus 2b-3e-2. For genus 8, e=0,b=5
or e=2,b=8: all 2^24 equations in each family are searched, including
nonmonic and degenerate equations. Count all projective fibers, then certify
geometric smoothness of complete matches on all four bundle charts.
"""
import argparse
import json
from pathlib import Path
import subprocess
import sympy as S
from census_lookup import HERE, FLUX

def charts(mask,e,b):
    x,y=S.symbols('x y')
    mons=[(i,j,b-e*j) for j in range(4) for i in range(b-e*j+1)]
    for baserev in [False,True]:
        for fibrev in [False,True]:
            f=sum(x**(d-i if baserev else i)*y**(3-j if fibrev else j)
                  for n,(i,j,d) in enumerate(mons) if mask>>n&1)
            yield f,x,y

def smooth(mask,e,b):
    certificates=[]
    for f,x,y in charts(mask,e,b):
        gb=S.groebner([f,S.diff(f,x),S.diff(f,y)],x,y,modulus=2)
        certificates.append(list(map(str,gb)))
        if list(gb)!=[1]:
            return False,certificates
    return True,certificates

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--graph',default='cube',choices=['cube','Petersen','K33'])
    args=parser.parse_args()
    binary=HERE/'trigonal_search'
    subprocess.run(['g++','-O3','-std=c++17',str(HERE/'trigonal_search.cpp'),'-o',str(binary)],check=True)
    records=json.loads(FLUX.read_text())
    graphs={'cube':(8,[(0,5),(2,8)],[3,5]),'K33':(6,[(0,4),(2,7)],[1,6]),
            'Petersen':(10,[(0,6),(2,9),(4,12)],[6,10,22])}
    g,families,masks=graphs[args.graph]
    stem='genus8' if args.graph=='cube' else 'trigonal_'+args.graph
    outputs=[];hits=[]
    for e,b in families:
        for mask in masks:
            r=next(r for r in records if r['graph']==args.graph and r['mask']==mask)
            cmd=[str(binary),str(e),str(b),str(g)]+[str(r['a'][str(k)]) for k in range(1,g+1)]
            print(f'TARGET {args.graph}:{mask}',flush=True)
            proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,text=True)
            lines=[]
            for line in proc.stdout:
                print(line,end='',flush=True);lines.append(line.rstrip())
            assert proc.wait()==0
            matching=list(map(int,lines[-1].split()[1:]))
            n=0
            for eq in matching:
                ok,cert=smooth(eq,e,b)
                if ok:
                    n+=1
                    f,_,_=next(charts(eq,e,b))
                    hits.append(dict(graph=args.graph,mask=mask,e=e,b=b,equation_mask=eq,
                                     equation=str(f),smoothness=cert))
            print(f'SMOOTH MATCHES {n}',flush=True)
            outputs.append(dict(graph=args.graph,mask=mask,e=e,b=b,log=lines,
                                raw_matching_masks=matching,smooth_matches=n))
            (HERE/f'output_{stem}.json.txt').write_text(json.dumps(dict(searches=outputs,hits=hits),indent=2)+'\n')
    print('VERDICT: no smooth match in these trigonal families' if not hits else 'WITNESSES '+str(hits),flush=True)

if __name__=='__main__':
    main()
