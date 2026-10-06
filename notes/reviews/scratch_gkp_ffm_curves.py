"""REFUTE scratch (ff-dirichlet.md 2.6, D1-D3, 3.5 D4): the curve y^N = c f(t), c from the reciprocity condition
c^{(q-1)/N} = (-1)^{(q-1)d/N}; my own point counts over F_{q^r} against prod_j Lambda(u, chi^j);
PARI hyperellcharpoly for N = 2; the twisted-c control; prod_j W(chi^j) = 1."""
from scratch_gkp_ffm_core import *
from scratch_gkp_ffm_phases import EX, global_W
import subprocess, math
mp.mp.dps = 30
class CharPow(Char):
    def __init__(self, q, N, Ps, j): super().__init__(q, N, Ps); self.j = j
    def sym(self, a, P):
        s = Char.sym(self, a, P); return None if s is None else (s*self.j) % self.N
def gp(cmd): return subprocess.run(['gp', '-q', '-f'], input=cmd+'\n\\q\n', capture_output=True, text=True).stdout.strip()
def ff_elements(q, r):
    """F_{q^r} = F_q[s]/(m(s)); returns (list of elements as tuples, mul function)"""
    if r == 1:
        m = [0, 1]
    else:
        m = next(f for f in monics(r, q) if is_irred(f, q))
    els = [tuple(c) for c in itertools.product(range(q), repeat=r)]
    def mul(a, b):
        return tuple((pmod(pmul(trim(list(a)), trim(list(b)), q), m, q) + [0]*r)[:r]) if r > 1 else ((a[0]*b[0]) % q,)
    return els, mul, m
def fpow(a, e, mul, r):
    res = tuple([1]+[0]*(r-1)); 
    while e:
        if e & 1: res = mul(res, a)
        a = mul(a, a); e >>= 1
    return res
def count(q, N, f, c, r):
    els, mul, m = ff_elements(q, r); Q = q**r; one = tuple([1]+[0]*(r-1)); zero = tuple([0]*r)
    tot = 0
    for t in els:
        # evaluate c f(t) by Horner
        v = zero
        for coef in reversed(f):
            v = mul(v, t); v = tuple((v[0]+coef) % q if i == 0 else v[i] for i in range(r))
        v = tuple((c*x) % q for x in v)
        if v == zero: tot += 1
        elif fpow(v, (Q-1)//N, mul, r) == one: tot += N
    d = len(f)-1; e = math.gcd(N, d)
    if e == 1: tot += 1
    elif e == N:
        cc = tuple([c % q]+[0]*(r-1)); tot += N if fpow(cc, (Q-1)//N, mul, r) == one else 0
    else: raise NotImplementedError
    return tot
def main():
  for name, (q, N, Ps) in EX.items():
      f = [1]
      for P in Ps: f = pmul(f, P, q)
      d = len(f)-1
      target = (-1)**(((q-1)*d//N) % 2)
      cs = [c for c in range(1, q) if pow(c, (q-1)//N, q) == target % q]
      c = q-1 if (q-1) in cs else cs[0]
      alphas = []; Ws = []; degs = []
      for j in range(1, N):
          ch = CharPow(q, N, Ps, j); Lam, even, n, W = global_W(ch); Ws.append(W); degs.append(n)
          if n: alphas += [1/r for r in mp.polyroots(Lam[::-1], maxsteps=300, extraprec=300)]
      g = sum(degs)//2
      rr = range(1, max(g, 2)+1)
      pred = [int(mp.nint(mp.re(q**r+1-sum(a**r for a in alphas)))) for r in rr]
      got = [count(q, N, f, c, r) for r in rr]
      gnon = primroot(q); ctw = (c*gnon) % q
      tw = [count(q, N, f, ctw, r) for r in rr]
      print(f'{name}: curve y^{N} = {c}*f, genus {g}; c allowed by reciprocity: {cs}; deg Lambda(chi^j) = {degs}')
      print(f'   counts r=1..{len(rr)}: mine {got}, predicted from prod Lambda(chi^j) {pred}, match {got == pred};  twisted c={ctw}: {tw}, match {tw == pred}')
      print(f'   prod_j W(chi^j) = {mp.nstr(mp.fprod(Ws), 10)}')
      if N == 2:
          fs = '+'.join(f'{a}*x^{i}' for i, a in enumerate(f))
          print('   PARI hyperellcharpoly(c f):', gp(f'hyperellcharpoly(Mod({c},{q})*({fs}))'))
      if N == 4:
          chq = CharPow(q, N, Ps, 2); Lam2, ev2, n2, W2 = global_W(chq)
          fs = '+'.join(f'{a}*x^{i}' for i, a in enumerate(f))
          print('   Lambda(chi^2) =', [mp.nstr(x, 5) for x in Lam2], '; PARI hyperellcharpoly(-f):', gp(f'hyperellcharpoly(Mod(-1,{q})*({fs}))'))

if __name__ == '__main__': main()
