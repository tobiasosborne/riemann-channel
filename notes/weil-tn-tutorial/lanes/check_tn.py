"""check_tn.py -- independent numpy check of the numeric part of movieCircle (tn.js).

Mode set (r = 1): conjugate pairs exp(+-i a), a in {0.7, 1.9, 2.6}, a movable pair R exp(+-1.3 i),
and optionally its reflected partners J(mu) = r^2/conj(mu) = (1/R) exp(+-1.3 i) with weight w.
t_l = sum_mu w_mu mu^l (complex sum; imaginary part must vanish), T_K[j][k] = t_{k-j},
lambda_min(T_K) for K = 1..14 by numpy.linalg.eigvalsh.  Then run tn.js under node with a stub
window/document and compare WT.tn.circleData(t) at the matching movie times.
"""
import json, os, subprocess
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
K = 14
CONFIGS = [  # (name, movie time t, R, partner weight)
    ("start: pair on the circle", 0.0, 1.0, 0.0),
    ("inside: R = 0.55", 0.3, 0.55, 0.0),
    ("outside: R = 1.35", 0.6, 1.35, 0.0),
    ("outside + partners 1/1.35", 0.8, 1.35, 1.0),
    ("merged on circle (double)", 1.0, 1.0, 1.0),
]

def modes(R, w):
    m = []
    for a in (0.7, 1.9, 2.6):
        m += [(np.exp(1j*a), 1.0), (np.exp(-1j*a), 1.0)]
    m += [(R*np.exp(1.3j), 1.0), (R*np.exp(-1.3j), 1.0)]
    if w > 0:
        J = lambda z: 1.0/np.conj(z)
        m += [(J(R*np.exp(1.3j)), w), (J(R*np.exp(-1.3j)), w)]
    return m

def numbers(R, w):
    ms = modes(R, w)
    t = np.array([sum(wt*z**l for z, wt in ms) for l in range(K)])
    assert np.max(np.abs(t.imag)) < 1e-9, "t_l not real"
    t = t.real
    mins = [np.linalg.eigvalsh(np.array([[t[abs(j-k)] for k in range(n)] for j in range(n)]))[0] for n in range(1, K+1)]
    return t, np.array(mins)

JS = r"""
global.window={matchMedia:()=>({matches:false})}; global.document={getElementById:()=>null};
require(process.argv[1]+'/core.js'); require(process.argv[1]+'/tn.js');
const ts = JSON.parse(process.argv[2]); const out = ts.map(t => { const d = window.WT.tn.circleData(t); return {R: d.R, pw: d.pw, tl: d.tl, mins: d.mins}; });
console.log(JSON.stringify(out));
"""

def main():
    js = json.loads(subprocess.check_output(["node", "-e", JS, ROOT, json.dumps([c[1] for c in CONFIGS])]))
    worst = 0.0
    for (name, t, R, w), d in zip(CONFIGS, js):
        tp, mp = numbers(R, w)
        assert abs(d["R"] - R) < 1e-12 and abs(d["pw"] - w) < 1e-12, (name, d["R"], d["pw"])
        et = np.max(np.abs(tp - np.array(d["tl"]))); em = np.max(np.abs(mp - np.array(d["mins"])))
        worst = max(worst, et, em)
        neg = [k+1 for k, v in enumerate(mp) if v < -1e-9*max(1, tp[0])]
        print(f"## {name}  (movie t = {t}, R = {R}, partner weight = {w})")
        print("t_l, l=0..13     :", " ".join(f"{v:.4f}" for v in tp))
        print("lambda_min K=1..14:", " ".join(f"{v:.4f}" for v in mp))
        print(f"first negative K : {neg[0] if neg else 'none'};  lambda_min(T_14) = {mp[-1]:.4f}  (demo computes {float(d['mins'][-1]):.4f})")
        print(f"max |python - js| : t {et:.2e}, mins {em:.2e}\n")
    print(f"worst discrepancy {worst:.2e}")
    assert worst < 1e-9

if __name__ == "__main__":
    main()
