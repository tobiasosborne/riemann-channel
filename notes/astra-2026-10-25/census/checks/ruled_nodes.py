#!/usr/bin/env python3
"""Tetragonal genus-eight normalizations of one-node genus-nine ruled curves."""
import json
import subprocess
import sympy as S
from census_lookup import HERE

def main():
    binary=HERE/'ruled_nodes'
    subprocess.run(['g++','-O3','-std=c++17',str(HERE/'ruled_nodes.cpp'),'-o',str(binary)],check=True)
    logs=[];hits=[]
    for e,b in [(0,4),(2,8)]:
        p=subprocess.run([str(binary),str(e),str(b)],check=True,capture_output=True,text=True)
        mons=[(i,j,b-e*j) for j in range(5) for i in range(b-e*j+1)]
        for line in p.stdout.splitlines():
            print(line,flush=True);logs.append(line)
            lhs,rhs=line.split(' MASKS');target=int(lhs.split()[1])
            for mask in map(int,rhs.split()):
                x,y=S.symbols('x y');ok=True;cert=[]
                for baserev in [False,True]:
                    for fibrev in [False,True]:
                        f=sum(x**(d-i if baserev else i)*y**(4-j if fibrev else j)
                              for n,(i,j,d) in enumerate(mons) if mask>>n&1)
                        gb=S.groebner([f,S.diff(f,x),S.diff(f,y)],x,y,modulus=2)
                        expect=[x,y] if not baserev and not fibrev else [1]
                        cert.append(list(map(str,gb)))
                        if list(gb)!=expect:ok=False;break
                    if not ok:break
                if ok:
                    f=sum(x**i*y**j for n,(i,j,d) in enumerate(mons) if mask>>n&1)
                    hit=dict(target=target,e=e,b=b,mask=mask,equation=str(f),cert=cert)
                    hits.append(hit);print('WITNESS',hit,flush=True)
    (HERE/'output_ruled_nodes.json.txt').write_text(json.dumps(dict(logs=logs,hits=hits),indent=2)+'\n')
    print('GOOD NORMALIZATIONS',len(hits),flush=True)

if __name__=='__main__':main()
