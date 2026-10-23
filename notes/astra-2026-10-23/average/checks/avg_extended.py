#!/usr/bin/env python3
"""Exact certificate extension beyond the requested brute-force table.

Uses A2 on the first half and the algebraic functional equation, not enumeration
of the exponentially larger H_d. No claim of an unrestricted genus theorem.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import time
from common import *
from avg_hyperelliptic import formula


def main():
    with Path(__file__).with_name('output_extended.txt').open('w') as f:
        def emit(s):print(s,flush=True);print(s,file=f,flush=True)
        emit('Exact A2 + algebraic FE. H-half and independent rational Sturm certificates; 80-digit root diagnostics.')
        for q,gmax in [(3,12),(5,8),(7,6)]:
            for g in range(1,gmax+1):
                t=time.monotonic();a,_=formula(q,g)
                half=[a[2*m]/q**m for m in range(g//2+1)]
                if g%2==0:half[-1]/=2
                good=all(half[i]>=half[i+1]>0 for i in range(len(half)-1)) and (len(half)<2 or half[0]>half[1])
                r,iv=sturm_curve_certificate(a,q)
                emit(f'q={q} g={g} average={expr(a)}')
                emit(f'  H-half={good} coefficients={half}; exact_Sturm_band=True; R(x)={r}')
                assert good
                root_report(a,q,f'q={q} g={g}',emit)
                emit(f'  seconds={time.monotonic()-t:.3f}')
        for q,gmax in [(3,6),(5,4),(7,4)]:
            for g in range(1,gmax+1):
                a,_=formula(q,g,even=True)
                r,iv=sturm_curve_certificate(a,q)
                emit(f'even q={q} g={g} completed_average={expr(a)} exact_Sturm_band=True R(x)={r}')
                root_report(a,q,f'even q={q} g={g}',emit)
        emit('ALL LISTED H-HALF AND STURM CERTIFICATES PASS. These finite parameter ranges are proved, not extrapolated.')


if __name__=='__main__':main()
