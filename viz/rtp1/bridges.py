"""Bridges to the committed code this package reuses, without re-deriving anything (lane V).

* `a2()`: the functions of `scripts/rtp1_prime_content.py` (lane A2).  That script runs its whole
  measurement at module level (~100 s), so it is not imported as a module: its source is parsed and
  only the top-level definitions and the cheap setup statements are executed (all `def`s, imports,
  constants, the admissible-delta table and the bump constants of its Sections 0, 2 and 3).  Skipped:
  every bare expression statement (prints, `check(...)` calls), the verification loops of its Sections 1
  and 4, and everything from its measurement loop on (Sections 5-7, including the only place where it
  touches zeros of zeta).  The functions are then called exactly as lane A2 calls them.
* `defs(path)`: the same, for a script whose functions only are wanted (`scripts/weil_window_extension.py`).
* `zst_ab(X, N, prec)`: `(a_n, b_n)` of the zst window form at `x = X` (prime powers `<= X`), from
  `zst_riemann_ab` in `zst/build/libzst.a`, through a small C printer compiled at run time in a temporary
  directory (the approach of lane A2's consistency check), printing enough digits for `prec` bits.  zst is
  not modified.  Returns decimal strings (midpoints) and the ball radii.
"""
import ast
import contextlib
import io
import os
import subprocess
import tempfile

from common import REPO

_A2 = None


def _exec_selected(path, keep):
    src = open(path).read()
    tree = ast.parse(src)
    body = [node for node in tree.body if keep(node, src)]
    ns = {"__name__": "rtp1_viz_bridge", "__file__": path}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(ast.Module(body=body, type_ignores=[]), path, "exec"), ns)
    return ns


def a2():
    """namespace with lane A2's functions (build, entry, min_eig, delta_grid, ADM, R1, ...)"""
    global _A2
    if _A2 is not None:
        return _A2
    path = os.path.join(REPO, "scripts", "rtp1_prime_content.py")
    lines = open(path).read().splitlines()

    def line_of(prefix):
        for i, ln in enumerate(lines, 1):
            if ln.startswith(prefix):
                return i
        raise RuntimeError("marker not found in lane A2 script: " + prefix)
    sec1 = line_of('head("1. CONSISTENCY')
    sec2 = line_of('head("2. TEST')
    sec4 = line_of('head("4. STRUCTURE')
    stop = line_of("print_gram((2,), 2")

    def keep(node, _src):
        if node.lineno >= stop or isinstance(node, ast.Expr):
            return False
        if isinstance(node, (ast.For, ast.While)) and (sec1 <= node.lineno < sec2 or node.lineno >= sec4):
            return False
        return True
    _A2 = _exec_selected(path, keep)
    return _A2


def defs(path):
    """only imports and function definitions of a script"""
    return _exec_selected(path, lambda node, _s: isinstance(node, (ast.FunctionDef, ast.Import, ast.ImportFrom)))


ZST_PRINTER = r"""
#include <stdio.h>
#include <stdlib.h>
#include "zst.h"
int main(int argc, char **argv)
{
    ulong X = strtoul(argv[1], 0, 10); slong N = atol(argv[2]); slong prec = atol(argv[3]);
    slong digits = atol(argv[4]);
    arb_t x; arb_ptr a = _arb_vec_init(N + 1), b = _arb_vec_init(N + 1); slong n;
    arb_init(x); arb_set_ui(x, X);
    zst_riemann_ab(a, b, N, x, X, prec);
    for (n = 0; n <= N; n++) {
        flint_printf("%wd ", n);
        arb_printn(a + n, digits, ARB_STR_NO_RADIUS); flint_printf(" "); mag_printd(arb_radref(a + n), 3); flint_printf(" ");
        arb_printn(b + n, digits, ARB_STR_NO_RADIUS); flint_printf(" "); mag_printd(arb_radref(b + n), 3); flint_printf("\n");
    }
    _arb_vec_clear(a, N + 1); _arb_vec_clear(b, N + 1); arb_clear(x);
    return 0;
}
"""
_EXE = None
_TMP = None


def _printer():
    global _EXE, _TMP
    if _EXE is not None:
        return _EXE
    zdir = os.path.join(REPO, "zst")
    lib = os.path.join(zdir, "build", "libzst.a")
    if not os.path.exists(lib):
        subprocess.run(["make", "-C", zdir], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    _TMP = tempfile.TemporaryDirectory()
    src = os.path.join(_TMP.name, "ab.c")
    exe = os.path.join(_TMP.name, "ab")
    with open(src, "w") as fh:
        fh.write(ZST_PRINTER)
    subprocess.run(["cc", "-O2", "-I" + os.path.join(zdir, "include"), src, lib, "-lflint", "-lmpfr", "-lgmp",
                    "-lm", "-o", exe], check=True, capture_output=True)
    _EXE = exe
    return exe


def zst_ab(X, N, prec):
    """(a, b, ra, rb): lists of decimal strings a_n, b_n (n = 0..N) and float radii, from zst at prec bits"""
    digits = int(prec * 0.30103) + 5
    out = subprocess.run([_printer(), str(X), str(N), str(prec), str(digits)], capture_output=True, text=True,
                         check=True).stdout
    a, b, ra, rb = [], [], [], []
    for line in out.strip().splitlines():
        t = line.split()
        a.append(t[1]); ra.append(float(t[2])); b.append(t[3]); rb.append(float(t[4]))
    return a, b, ra, rb
