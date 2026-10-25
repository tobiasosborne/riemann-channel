#!/usr/bin/env python3
"""Exact limiting square densities; explicitly NOT full finite-genus averages."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from math import comb
from flint import fmpq_poly,fmpq
from exact_core import prime_count

def main():
    with Path(__file__).with_name('output_square_density.txt').open('w') as log:
        def emit(s):print(s);print(s,file=log)
        for q,M in [(3,30),(5,15),(7,15),(9,15),(11,6),(13,6)]:
            Q=fmpq_poly([1])
            for r in range(1,M+1):
                N=prime_count(q,r);pol=[fmpq(0)]*(M+1)
                for k in range(min(N,M//r)+1):pol[k*r]=fmpq((-1)**k*comb(N,k),(q**r*(q**r+1))**k)
                Q=(Q*fmpq_poly(pol)).truncate(M+1)
            c=fmpq(0)
            for m in range(M+1):
                c+=Q[m]
                emit(f'LIMIT_ONLY q={q} m={m} C_m={c} gap={-Q[m] if m else "NA"}')
            emit(f'limit_first_half_diagnostic q={q} through_m={M} all_differences_negative={all(Q[m]<0 for m in range(1,M+1))}; NOT a finite-g certificate')
        emit('Universal square-density lower bounds: finite c_(d,m)>=1-q/(q-1)^2>=1/4; limit C_(q,m)>=1-1/(q-1)>=1/2.')
if __name__=='__main__':main()
