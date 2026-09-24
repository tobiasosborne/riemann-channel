#!/usr/bin/env python3
"""REFUTE lane R, RTP-1 (claude:opus, 2026-09-24).  Reviewer's own ball LDL^T / inertia / inverse
iteration for the even and odd blocks of a Loewner window form, as a small C program on FLINT's arb
(written here from plan.md 1.3's block formulas; no zst code, no arb_mat_ldl: a plain unpivoted
LDL^T that allows negative pivots, so it also gives certified inertia of indefinite forms).
Imported by the other scratch_rtp1_* scripts; compiles into the scratchpad (or $RTP1_TMP)."""
import os, subprocess, hashlib
C_SRC = r'''
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <flint/arb.h>
#include <flint/arb_mat.h>
static char buf[1<<20];
static void build(arb_mat_t E, arb_mat_t O, arb_srcptr a, arb_srcptr b, slong M, slong prec) {
  /* E: size M+1, basis V_0, (V_j+V_-j)/sqrt2 ; O: size M, basis (V_j-V_-j)/sqrt2, j=1..M */
  arb_t t, u, s2; arb_init(t); arb_init(u); arb_init(s2); arb_sqrt_ui(s2, 2, prec);
  arb_set(arb_mat_entry(E,0,0), a+0);
  for (slong j=1;j<=M;j++){ arb_mul(t, s2, b+j, prec); arb_div_si(t,t,j,prec);
    arb_set(arb_mat_entry(E,0,j),t); arb_set(arb_mat_entry(E,j,0),t); }
  for (slong i=1;i<=M;i++) for (slong j=1;j<=M;j++){
    if (i==j){ arb_div_si(t,b+j,j,prec); arb_add(arb_mat_entry(E,j,j),a+j,t,prec); arb_sub(arb_mat_entry(O,j-1,j-1),a+j,t,prec); continue; }
    arb_sub(t,b+i,b+j,prec); arb_div_si(t,t,i-j,prec);
    arb_add(u,b+i,b+j,prec); arb_div_si(u,u,i+j,prec);
    arb_add(arb_mat_entry(E,i,j),t,u,prec); arb_sub(arb_mat_entry(O,i-1,j-1),t,u,prec); }
  arb_clear(t); arb_clear(u); arb_clear(s2);
}
/* in place unpivoted LDL^T on the leading n x n block; returns pivots in d; L below diag */
static void ldl(arb_mat_t A, slong n, arb_ptr d, slong prec){
  arb_t t; arb_init(t);
  for (slong k=0;k<n;k++){
    arb_set(d+k, arb_mat_entry(A,k,k));
    for (slong i=k+1;i<n;i++){ arb_div(arb_mat_entry(A,i,k), arb_mat_entry(A,i,k), d+k, prec); }
    for (slong i=k+1;i<n;i++){ arb_mul(t, arb_mat_entry(A,i,k), d+k, prec);
      for (slong j=k+1;j<=i;j++){ arb_submul(arb_mat_entry(A,i,j), t, arb_mat_entry(A,j,k), prec);
        arb_set(arb_mat_entry(A,j,i), arb_mat_entry(A,i,j)); } }
  }
  arb_clear(t);
}
static void solve(const arb_mat_t F, arb_srcptr d, slong n, arb_ptr x, slong prec){
  arb_t t; arb_init(t);
  for (slong i=0;i<n;i++) for (slong j=0;j<i;j++) arb_submul(x+i, arb_mat_entry(F,i,j), x+j, prec);
  for (slong i=0;i<n;i++) arb_div(x+i,x+i,d+i,prec);
  for (slong i=n-1;i>=0;i--) for (slong j=i+1;j<n;j++) arb_submul(x+i, arb_mat_entry(F,j,i), x+j, prec);
  arb_clear(t);
}
static void pr(const arb_t x, slong dig){ char *s = arb_get_str(x, dig, ARB_STR_NO_RADIUS); printf("%s", s); flint_free(s); }
static void prr(const arb_t x, slong dig){ char *s = arb_get_str(x, dig, 0); printf("%s", s); flint_free(s); }
int main(int argc, char **argv){
  slong prec, M; char mode[32];
  if (scanf("%ld %ld %31s", &prec, &M, mode)!=3) return 1;
  arb_ptr a=_arb_vec_init(M+1), b=_arb_vec_init(M+1);
  for (slong n=0;n<=M;n++){ if (scanf("%s",buf)!=1) return 2; arb_set_str(a+n,buf,prec);
                            if (scanf("%s",buf)!=1) return 2; arb_set_str(b+n,buf,prec); }
  arb_mat_t E,O; arb_mat_init(E,M+1,M+1); arb_mat_init(O,M,M); build(E,O,a,b,M,prec);
  if (!strcmp(mode,"ldl")){
    arb_ptr dE=_arb_vec_init(M+1), dO=_arb_vec_init(M); ldl(E,M+1,dE,prec); ldl(O,M,dO,prec);
    arb_t l; arb_init(l);
    for (slong j=0;j<=M;j++){ printf("E %ld ", j); int sg = arb_is_positive(dE+j)?1:(arb_is_negative(dE+j)?-1:0);
      arb_abs(l,dE+j); arb_log(l,l,prec); pr(l,25); printf(" %d %ld\n", sg, arb_rel_accuracy_bits(dE+j)); }
    for (slong j=0;j<M;j++){ printf("O %ld ", j+1); int sg = arb_is_positive(dO+j)?1:(arb_is_negative(dO+j)?-1:0);
      arb_abs(l,dO+j); arb_log(l,l,prec); pr(l,25); printf(" %d %ld\n", sg, arb_rel_accuracy_bits(dO+j)); }
  } else if (!strcmp(mode,"inertia")){
    /* reads: nshift then shifts; for each shift: negatives of E-s, O-s (leading full size); ? if undecided */
    slong ns; if (scanf("%ld",&ns)!=1) return 3;
    for (slong q=0;q<ns;q++){ arb_t s; arb_init(s); if (scanf("%s",buf)!=1) return 3; arb_set_str(s,buf,prec);
      arb_mat_t A,B; arb_mat_init(A,M+1,M+1); arb_mat_init(B,M,M); arb_mat_set(A,E); arb_mat_set(B,O);
      for (slong j=0;j<=M;j++) arb_sub(arb_mat_entry(A,j,j),arb_mat_entry(A,j,j),s,prec);
      for (slong j=0;j<M;j++) arb_sub(arb_mat_entry(B,j,j),arb_mat_entry(B,j,j),s,prec);
      arb_ptr dA=_arb_vec_init(M+1), dB=_arb_vec_init(M); ldl(A,M+1,dA,prec); ldl(B,M,dB,prec);
      slong nE=0,nO=0,uE=0,uO=0;
      for (slong j=0;j<=M;j++){ if (arb_is_negative(dA+j)) nE++; else if (!arb_is_positive(dA+j)) uE++; }
      for (slong j=0;j<M;j++){ if (arb_is_negative(dB+j)) nO++; else if (!arb_is_positive(dB+j)) uO++; }
      printf("shift %s negE %ld undE %ld negO %ld undO %ld\n", buf, nE, uE, nO, uO);
      _arb_vec_clear(dA,M+1); _arb_vec_clear(dB,M); arb_mat_clear(A); arb_mat_clear(B); arb_clear(s); }
  } else if (!strcmp(mode,"eig")){
    /* reads: sigma iters digits ; inverse iteration on E - sigma (E full size M+1), midpoints renormalised */
    slong it, dig; arb_t sg; arb_init(sg); if (scanf("%s %ld %ld",buf,&it,&dig)!=3) return 4; arb_set_str(sg,buf,prec);
    slong n=M+1; arb_mat_t A; arb_mat_init(A,n,n); arb_mat_set(A,E);
    for (slong j=0;j<n;j++) arb_sub(arb_mat_entry(A,j,j),arb_mat_entry(A,j,j),sg,prec);
    arb_ptr d=_arb_vec_init(n), x=_arb_vec_init(n), y=_arb_vec_init(n); ldl(A,n,d,prec);
    for (slong j=0;j<n;j++) arb_one(x+j);
    arb_t nr,t,num,den; arb_init(nr); arb_init(t); arb_init(num); arb_init(den);
    for (slong k=0;k<it;k++){ solve(A,d,n,x,prec); arb_zero(nr);
      for (slong j=0;j<n;j++){ arb_get_mid_arb(x+j,x+j); arb_addmul(nr,x+j,x+j,prec);} arb_sqrt(nr,nr,prec);
      for (slong j=0;j<n;j++){ arb_div(x+j,x+j,nr,prec); arb_get_mid_arb(x+j,x+j);} }
    /* Rayleigh quotient and residual with E (not shifted) */
    arb_zero(num); arb_zero(den);
    for (slong i=0;i<n;i++){ arb_zero(y+i); for (slong j=0;j<n;j++) arb_addmul(y+i, arb_mat_entry(E,i,j), x+j, prec);
      arb_addmul(num,x+i,y+i,prec); arb_addmul(den,x+i,x+i,prec);} arb_div(num,num,den,prec);
    arb_zero(nr); for (slong i=0;i<n;i++){ arb_submul(y+i,num,x+i,prec); arb_addmul(nr,y+i,y+i,prec);} arb_sqrt(nr,nr,prec);
    printf("rayleigh "); prr(num,40); printf("\nresidual "); pr(nr,5); printf("\n");
    for (slong j=0;j<n;j++){ printf("v %ld ",j); pr(x+j,dig); printf("\n"); }
  }
  return 0;
}
'''
_TMP = os.environ.get('RTP1_TMP', '/tmp/claude-0/-home-user-riemann-channel/17bd93f8-9a05-5f47-b828-4d972b66777c/scratchpad')
_BIN = None
def binary():
    global _BIN
    if _BIN: return _BIN
    h = hashlib.sha256(C_SRC.encode()).hexdigest()[:12]
    src = os.path.join(_TMP, f'rtp1_linalg_{h}.c'); exe = src[:-2]
    if not os.path.exists(exe):
        os.makedirs(_TMP, exist_ok=True)
        open(src, 'w').write(C_SRC)
        subprocess.check_call(['gcc', '-O2', '-o', exe, src, '-lflint', '-lmpfr', '-lgmp', '-lm'])
    _BIN = exe
    return exe

def _input(prec, a, b, mode, extra=''):
    M = len(a) - 1
    digs = int(prec * 0.30103) + 10
    lines = [f'{prec} {M} {mode}']
    for n in range(M + 1):
        lines.append(a[n].mid().str(digs, radius=False) + ' ' + b[n].mid().str(digs, radius=False))
    lines.append(extra)
    return '\n'.join(lines) + '\n'

def run(prec, a, b, mode, extra=''):
    r = subprocess.run([binary()], input=_input(prec, a, b, mode, extra), capture_output=True, text=True, check=True)
    return r.stdout

def ldl_pivots(prec, a, b):
    """returns (E, O): lists of (logabs float, sign, accbits) ; E index 0..M, O index 1..M"""
    E, O = [], []
    for line in run(prec, a, b, 'ldl').splitlines():
        t = line.split()
        rec = (float(t[2]), int(t[3]), int(t[4]))
        (E if t[0] == 'E' else O).append(rec)
    return E, O

def inertia(prec, a, b, shifts):
    out = run(prec, a, b, 'inertia', f'{len(shifts)} ' + ' '.join(shifts))
    res = []
    for line in out.splitlines():
        t = line.split()
        res.append(dict(shift=t[1], negE=int(t[3]), undE=int(t[5]), negO=int(t[7]), undO=int(t[9])))
    return res

def eig_even(prec, a, b, sigma='0', iters=4, digits=60):
    out = run(prec, a, b, 'eig', f'{sigma} {iters} {digits}')
    lam = None; res = None; v = []
    for line in out.splitlines():
        t = line.split(None, 2)
        if t[0] == 'rayleigh': lam = line.split(None, 1)[1]
        elif t[0] == 'residual': res = line.split(None, 1)[1]
        elif t[0] == 'v': v.append(t[2])
    return lam, res, v
