"""Entropy of the Bost--Connes Gibbs state and its response to cutoffs.

The Gibbs state at inverse temperature beta > 1 is rho_beta = N^{-beta}/zeta(beta) on l^2(N),
N|n> = n|n>; it is a product over primes of geometric distributions with ratio p^{-beta}.  If the
Phantasm's bond fixed point is this state, then (cMPS canonical form) it is the reduced density
matrix of the half-line in dilation time, -log rho_beta = beta log N + log zeta(beta) is the
entanglement Hamiltonian, {log n} the entanglement spectrum, and S(rho_beta) the entanglement
entropy.  Checks:
  (1) S(beta) = log zeta(beta) - beta zeta'(beta)/zeta(beta) for beta > 1, diverging like
      1/(beta-1) + log(1/(beta-1)) as beta -> 1+;
  (2) prime cutoff p <= P at beta = 1: S_P = log P + log log P + o(1) (Mertens);
      beta < 1: S_P ~ beta P^{1-beta}/(1-beta) (power law); beta > 1: O(1);
  (3) bond (energy) cutoff n <= N: S_N/log N -> 1 (beta<1), 1/2 (beta=1; from int log n/n = (1/2) log^2 N), 0 (beta>1);
      at beta = 1, S_N = (1/2) log N + log log N + O(1);
  (4) the density of entanglement levels below E is floor(e^E): Hagedorn growth, beta_H = 1.
Run from the repo root.  No RH input; nothing here concerns the zeros."""
import numpy as np, mpmath as mp
from sympy import primerange

def S_geom(x):
    """entropy of the geometric distribution (1-x) x^k, k >= 0"""
    x = np.asarray(x, float)
    return -np.log(1 - x) - x * np.log(x) / (1 - x)

print("(1) uncut Gibbs state: S(beta) = log zeta - beta zeta'/zeta   vs  1/(beta-1) + log(1/(beta-1))")
for b in [3, 2, 1.5, 1.2, 1.1, 1.05, 1.01, 1.001]:
    z = mp.zeta(b); zp = mp.zeta(b, derivative=1)
    S = mp.log(z) - b * zp / z
    # cross-check: sum over primes of geometric entropies (primes < 2e6, remainder negligible for beta >= 1.2)
    print(f"  beta={b:<6} S={float(S):10.4f}   leading={1/(b-1)+np.log(1/(b-1)):10.4f}   S-leading={float(S)-1/(b-1)-np.log(1/(b-1)):+.4f}")
ps = np.array(list(primerange(2, 2_000_001)), float)
b = 1.5
print(f"  cross-check beta=1.5: sum_p S_p over p<2e6 = {S_geom(ps**-b).sum():.4f}  vs closed form {float(mp.log(mp.zeta(b)) - b*mp.zeta(b,derivative=1)/mp.zeta(b)):.4f}")

print("\n(2) prime cutoff p <= P, beta = 1:  S_P = sum_{p<=P} S_p   vs  log P + log log P")
for P in [10, 100, 10**3, 10**4, 10**5, 10**6, 2 * 10**6]:
    s = S_geom(1 / ps[ps <= P]).sum(); pred = np.log(P) + np.log(np.log(P))
    print(f"  P={P:<8} S_P={s:9.4f}   pred={pred:9.4f}   diff={s-pred:+.4f}")
print("    beta < 1 (power law): S_P / [beta P^(1-beta)/(1-beta)]")
for b in [0.5, 0.8]:
    for P in [10**4, 10**5, 10**6]:
        s = S_geom(ps[ps <= P] ** (-b)).sum(); lead = b * P ** (1 - b) / (1 - b)
        print(f"  beta={b} P={P:<8} S_P={s:10.2f}   ratio={s/lead:.4f}")
print("    beta > 1 (saturation): S_P for beta=2")
for P in [10, 100, 10**4, 10**6]:
    print(f"  P={P:<8} S_P={S_geom(ps[ps <= P] ** -2.0).sum():.6f}")

print("\n(3) bond cutoff n <= N:  S_N/log N  (beta = 0.5, 1, 2); at beta=1 also vs (1/2)log N + log log N")
for N in [10**3, 10**4, 10**5, 10**6, 10**7]:
    n = np.arange(1, N + 1, dtype=float)
    row = []
    for b in [0.5, 1.0, 2.0]:
        w = n ** (-b); p = w / w.sum(); S = -(p * np.log(p)).sum(); row.append(S)
    print(f"  N={N:<8} S/logN: beta=0.5 {row[0]/np.log(N):.4f}  beta=1 {row[1]/np.log(N):.4f}  beta=2 {row[2]/np.log(N):.4f}"
          f"   | beta=1: S_N={row[1]:.4f}  (1/2)logN+loglogN={0.5*np.log(N)+np.log(np.log(N)):.4f}")

print("\n(4) entanglement-level counting: #{n : log n <= E} = floor(e^E)  (Hagedorn density e^E, beta_H = 1)")
for E in [2.0, 5.0, 10.0]:
    print(f"  E={E}: count={int(np.floor(np.exp(E)))}   Cardy growth for a CFT would be exp(2 pi sqrt(c E/6)), i.e. sub-exponential")
