#!/usr/bin/env python3
"""Compile and run independent direct character sums with exact affine reuse.
Every squarefree D is visited, with no functional-equation reconstruction.
For D_b,c=b^-d D(b*x+c), substituting monic test polynomials proves
S_n(D_b,c)=eta(b)^(d*n) S_n(D). All n=0,...,d-1 are directly summed.
"""
from pathlib import Path
import subprocess,os
H=Path(__file__).resolve().parent
subprocess.run(['g++','-std=c++17','-O3','-fopenmp',str(H/'direct_average.cpp'),'-o',str(H/'direct_average.bin')],check=True)
os.environ['OMP_NUM_THREADS']='4'
with (H/'output_direct_average.txt').open('w') as out:
 for q,d in [(3,5),(7,7)]:
  p=subprocess.run([str(H/'direct_average.bin'),str(q),str(d)],text=True,stdout=subprocess.PIPE,check=True)
  print(p.stdout,end='',flush=True);out.write(p.stdout);out.flush()
