"""Exact exponent algebra, O7's endpoint identity, and a certified Liu root interval.

Run from any directory: python3 path/to/checks/exponents.py
No L-function zeros or RH hypotheses are inputs.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
import sympy as s


def dec(x, digits=65):
    with localcontext() as c:
        c.prec = digits
        return str(Decimal(x.numerator) / Decimal(x.denominator))


def show(label, x):
    print(f"{label}: {x} = {dec(x)}")


show("O11 first squared exponent at H=D", 1 + F(5, 6))
show("O11 error squared exponent at H=D", 2 - F(1, 3))
show("O11 A exponent", (1 + F(5, 6)) / 2)
h = 1 / (F(5, 6) + F(1, 3))
show("Formal balancing H exponent (outside proved range)", h)
assert (1 + F(5, 6)*h)/2 == 1 - h/6 == F(6, 7)
show("Formal balanced A exponent", F(6, 7))
b, ell = F(1, 8), F(1, 6)
lx, ly = (1-b-ell)/2, (1+b-ell)/2
show("O7 lx", lx)
show("O7 ly", ly)
show("O7 low exponent", lx/2+b/12)
show("O7 zero-free boundary", lx/2+b/12+(4+b)/6)
assert lx/2+b/12+(4+b)/6 == F(11, 12)-ell/4 == F(7, 8)

d, y = s.symbols('d y')
v = 51+41*y
Dx, Px = (37+34*y)/18, (7+18*y+8*y*y)/9
J = (s.Rational(5, 6)-d)*Dx+d*Px
R = 1-d+(s.Rational(5, 6)-d)*d*Px/(2*J)
E = -s.Rational(1, 48)+2*d/3+(s.Rational(1, 2)-y)*d/6-s.Rational(13, 16)*(1-R)
certificate = (3+5*y)*((4*v*d-79)**2+49)+4*y*(4*v*d*((1+3*y)*(15+32*y)*d+9-13*y)+265+3485*y)
assert s.cancel(10368*v*J*(-E)-certificate) == 0
print("O7 (20.9) polynomial certificate residual: 0 (exact)")
show("O7 uniform endpoint margin", F(49, 440640))
assert F(49, 440640) > F(1, 10000)
show("Kintali central saving", F(47, 48)-F(29, 30))
show("Kintali surviving stated saving", F(1, 4800))


def cubic(x):
    return 1188*x**3-2160*x*x+171*x+190


lo, hi = F(38858, 100000), F(38859, 100000)
assert cubic(lo) > 0 > cubic(hi)
# On this bracket P'(x)=3564*x^2-4320*x+171 < 0.
assert 3564*hi**2-4320*lo+171 < 0
for _ in range(280):
    mid = (lo+hi)/2
    if cubic(mid) > 0:
        lo = mid
    else:
        hi = mid
assert cubic(lo) > 0 > cubic(hi)
print("Liu unique root interval (decimal display, exact rational endpoints in computation):")
print("  lo =", dec(lo, 100))
print("  hi =", dec(hi, 100))
print("  interval width =", dec(hi-lo, 12))


def boundary(x):
    return (18*x+7)/(18*x+9)


Blo, Bhi = boundary(lo), boundary(hi)  # strictly increasing
print("Liu Bnew =", dec((Blo+Bhi)/2, 66))
print("Liu certified Bnew interval width =", dec(Bhi-Blo, 12))
assert Bhi-Blo < F(1, 10**85)
x = s.symbols('x')
kappa = (18*x+5)/(18*x+9)
critical = (216*kappa-18)*x*x-(468*kappa-57)*x+150*kappa-20
num = s.factor(s.together(critical).as_numer_denom()[0])
print("Liu eliminated critical equation numerator =", num)
assert s.rem(num, 1188*x**3-2160*x*x+171*x+190, x) == 0
assert s.cancel(s.Rational(11, 12)-(5-6*x)/(9+18*x)/4-(18*x+7)/(18*x+9)) == 0
print("Liu B=11/12-ell/4 identity residual: 0 (exact)")
print("Liu improvement over 7/8 =", dec(F(7, 8)-(Blo+Bhi)/2))
print("All exact checks passed.")
