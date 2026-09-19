#!/usr/bin/env python3
"""Offline, synthetic decay-mode diagnostics; no Riemann zero input or RH evidence."""
import json
from pathlib import Path
import numpy as np


def pair_case(name, omega, g=0.5, frequency=1.0):
    H = np.array([[-frequency, omega], [omega, -frequency]], dtype=complex)
    jump = np.array([[np.sqrt(2*g), 0]], dtype=complex)
    B = -1j*H - 0.5*jump.conj().T@jump
    centered = B + 0.25*np.eye(2) - 1j*frequency*np.eye(2)
    expected_square = (g*g/4-omega*omega)*np.eye(2)
    assert np.linalg.norm(centered@centered-expected_square)<1e-13
    assert np.linalg.norm(B+B.conj().T+jump.conj().T@jump)<1e-13
    eigenvalues = np.linalg.eigvals(B)
    fe_error = max(min(abs(-0.5-np.conj(z)-eigenvalues)) for z in eigenvalues)
    assert fe_error<1e-7  # defective threshold eigensolver splits by roundoff
    result = {
        'case':name, 'coupling':omega,
        'eigenvalues':[[float(z.real),float(z.imag)] for z in eigenvalues],
        'amplitude_widths':[-float(z.real) for z in eigenvalues],
        'decay_gauge_residual':float(np.linalg.norm(B+B.conj().T+jump.conj().T@jump)),
        'functional_equation_pair_residual':float(fe_error),
        'nonnormality':float(np.linalg.norm(B.conj().T@B-B@B.conj().T)),
        'centered_matrix_rank':int(np.linalg.matrix_rank(centered)),
        'centered_square_norm':float(np.linalg.norm(centered@centered)),
        'all_widths_quarter':bool(np.allclose(eigenvalues.real,-.25,atol=1e-7)),
    }
    Q=np.zeros((3,3),complex);Q[1:,1:]=B
    L=np.zeros((3,3),complex);L[0,1:]=jump
    assert np.linalg.norm(Q+Q.conj().T+L.conj().T@L)<1e-13
    result['cmps_gauge_residual']=float(np.linalg.norm(Q+Q.conj().T+L.conj().T@L))
    return result


def main():
    rows=[pair_case('underdamped_equal_widths',.5),
          pair_case('overdamped_FE_paired_unequal_widths',.125),
          pair_case('threshold_Jordan',.25)]
    assert rows[0]['all_widths_quarter']
    assert not rows[1]['all_widths_quarter']
    assert rows[2]['centered_matrix_rank']==1
    assert rows[2]['centered_square_norm']<1e-13
    # Scalar wave-geodesic intertwiner for each branch, including complex s.
    errors=[]
    for s in [.5+2j,.25+2j,.1+2j,.75]:
        mu=s*(1-s); lam=s-1; q=lam+.5
        W=np.array([[0,1],[.25-mu,0]],complex)
        v=np.array([1,q],complex)
        errors.append(float(np.linalg.norm(W@v-q*v)))
    assert max(errors)<1e-12
    result={'status':'all synthetic diagnostics passed',
            'interpretation':'CP, one exit, stability and FE do not force common width; wave shift is exact algebra',
            'two_level_cases':rows,'wave_intertwiner_residuals':errors}
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
