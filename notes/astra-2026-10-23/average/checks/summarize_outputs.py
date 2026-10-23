#!/usr/bin/env python3
"""Print the quoted numerical summary and audit the saved exact certificates."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import re
import ast
import sympy as sp


def main():
    here=Path(__file__).parent
    logs={name:(here/f'output_{name}.txt').read_text() for name in ['hyperelliptic','cubic','level','extended','audit']}
    assert all('ALL ' in text.splitlines()[-1] for text in logs.values())
    for path in here.glob('*.py'):ast.parse(path.read_text(),filename=str(path))
    ordinary=[line for line in logs['hyperelliptic'].splitlines() if 'even=False max_radial_deviation=' in line]
    assert len(ordinary)==9
    def val(line,key):return float(re.search(key+r'=([^ ]+)',line).group(1))
    extended=[line for line in logs['extended'].splitlines() if 'H-half=True' in line]
    assert len(extended)==26
    even=[line for line in logs['extended'].splitlines() if line.startswith('even q=') and 'exact_Sturm_band=True' in line]
    assert len(even)==14
    u=sp.Symbol('u')
    for line in logs['extended'].splitlines():
        m=re.match(r'q=(\d+) g=(\d+) average=(.*)',line)
        if m:
            q,g=int(m[1]),int(m[2]);p=sp.Poly(sp.sympify(m[3]),u)
            b=[p.nth(2*j)/q**j for j in range(g//2+1)]
            assert all(b[j]>=b[j+1]>0 for j in range(len(b)-1))
    all_diag=[line for text in logs.values() for line in text.splitlines() if 'max_relative_residual=' in line]
    assert max(val(line,'max_relative_residual') for line in all_diag)<1e-60
    assert all(val(line,'max_np_to_80d')<1e-10*max(1,val(line,'max_kappa')) for line in all_diag)
    with (here/'output_summary.txt').open('w') as f:
        def emit(s):print(s);print(s,file=f)
        emit('All five computation outputs end in success; all Python sources parse.')
        emit('Requested odd-degree grid: 9 exact brute-force/A2 agreements; total squarefree D enumerated = '+str(sum(int(x) for x in re.findall(r'd=(?:3|5|7) H=(\d+) completed_average=',logs['hyperelliptic']))))
        for key in ['max_radial_deviation','numpy_radial_deviation','max_kappa','max_np_to_80d','max_relative_residual']:
            emit(f'requested_odd_grid_{key}={max(val(line,key) for line in ordinary):.16g}')
        emit('Exact odd-degree certificates: q=3 g=1..12; q=5 g=1..8; q=7 g=1..6 (26 cases).')
        emit('All 26 also have unhalved b_0 >= ... >= b_floor(g/2) > 0, checked as exact rational inequalities.')
        emit('Exact even-degree Sturm certificates: q=3 g=1..6; q=5,7 g=1..4 (14 cases).')
        for line in ordinary:
            if line.startswith('q=3 g=1 ') or line.startswith('q=5 g=2 '):emit('blind_check '+line)
        emit('blind_exact Lbar_3_1=1+3u^2; Lbar_5_2=1+(524/125)u^2+25u^4; exact maximum radial deviation = 0 for both.')
        emit('blind_counterexample cubic q=7 d=3 completed average=1+u; root=-1; normalized radius=sqrt(7)=2.645751311065.')
        emit('blind_counterexample cubic q=7 d=4 average=1+7u^3; normalized radius=7^(1/6)=1.383087554268.')
        emit('blind_counterexample level q=3 d=2 raw sum=7-3u; root=7/3; normalized radius=4.041451884327.')
        emit('ALL SUMMARY AND SAVED-CERTIFICATE AUDITS PASS.')


if __name__=='__main__':main()
