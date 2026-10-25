#!/usr/bin/env python3
"""Exact whole-curve products in Z[omega], all monic squarefree f.
Run with python3. The prior helpers are copied in reproduced/ (read-only input provenance).
Coefficients are formed separately for every member BEFORE averaging the product.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'reproduced'))
from avg_cubic import cubic
from common import expr,sturm_curve_certificate,root_report

def main():
    with Path(__file__).with_name('output_cubic_whole.txt').open('w') as log:
        def emit(s):print(s,flush=True);print(s,file=log,flush=True)
        for q,ds in [(7,[3,4,5]),(13,[3,4])]:
            for d in ds:
                count,raw,iso,p=cubic(q,d)
                emit(f'q={q} d={d} H={count} whole={expr(p)}')
                emit(f'raw_isotypic={expr(raw)} completed_isotypic={expr(iso)}')
                try:
                    r,iv=sturm_curve_certificate(p,q)
                    emit(f'exact_circle=True R(x)={r}; rational_isolating_intervals={iv}')
                except AssertionError:
                    emit('exact_circle=False; full rational root isolation follows')
                    raise
                root_report(p,q,f'q={q} d={d}',emit)
        emit('ALL FIVE WHOLE-CURVE AVERAGES HAVE EXACT CIRCLE CERTIFICATES.')
if __name__=='__main__':main()
