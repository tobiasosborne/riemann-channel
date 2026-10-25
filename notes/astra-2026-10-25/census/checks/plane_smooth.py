#!/usr/bin/env python3
"""Exhaustive smooth plane sextic comparison for the open Petersen targets."""
import json
import subprocess
import sympy as S
from census_lookup import HERE,FLUX
from plane_nodes import expression

def main():
    binary=HERE/'plane_nodes'
    subprocess.run(['g++','-O3','-std=c++17',str(HERE/'plane_nodes.cpp'),'-o',str(binary)],check=True)
    rows=json.loads(FLUX.read_text());data=['2 10']
    for mask in [6,10]:
        r=next(r for r in rows if r['graph']=='Petersen' and r['mask']==mask)
        data.append(' '.join(map(str,[mask,28,0]+[1<<i for i in range(28)]+[r['a'][str(k)] for k in range(1,11)])))
    inp=HERE/'plane_smooth_input.txt';inp.write_text('\n'.join(data)+'\n')
    proc=subprocess.Popen([str(binary),str(inp)],stdout=subprocess.PIPE,text=True)
    logs=[];hits=[]
    for line in proc.stdout:
        print(line,end='',flush=True);logs.append(line.rstrip())
        lhs,rhs=line.split(' MASKS');target=int(lhs.split()[1]);raw=list(map(int,rhs.split()))
        for mask in raw:
            f,X=expression(mask);ok=True
            for j in range(3):
                vs=[v for i,v in enumerate(X) if i!=j];ff=f.subs(X[j],1)
                gb=S.groebner([ff]+[S.diff(ff,v) for v in vs],*vs,modulus=2)
                if list(gb)!=[1]:ok=False;break
            if ok:
                hit=dict(target=target,mask=mask,equation=str(f));hits.append(hit);print('WITNESS',hit,flush=True)
        print('TARGET',target,'raw matches',len(raw),'smooth matches',sum(h['target']==target for h in hits),flush=True)
    assert proc.wait()==0
    (HERE/'output_plane_smooth.json.txt').write_text(json.dumps(dict(logs=logs,hits=hits),indent=2)+'\n')

if __name__=='__main__':main()
