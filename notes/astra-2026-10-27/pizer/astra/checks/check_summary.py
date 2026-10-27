"""Audit the saved numerical outputs without regenerating any data."""
from pathlib import Path
import hashlib
root=Path(__file__).resolve().parent
files=['output_pizer_graph.txt','output_pizer_quotient.txt','output_quaternion.txt','output_label_lattice.txt','output_curve37.txt']
out={}
for name in files:
    text=(root/name).read_text()
    assert text and 'Traceback' not in text and 'AssertionError' not in text
    assert 'model check failed' not in text
    out[name]=text
    print(name,'lines=',len(text.splitlines()),'sha256=',hashlib.sha256(text.encode()).hexdigest())
g=out[files[0]]; q=out[files[1]]; l=out[files[3]]; c=out[files[4]]
assert g.count('DETERMINANT MATCH PASS')==24
assert g.count('ACTUAL ISOGENY DUALITY halfloops=')==16
assert g.count('WEIGHTED EDGE-INDEXED QUOTIENT')==8
assert 'ALL P1 MATRIX / HECKE / POSITIVITY CHECKS PASS' in g
assert q.count('ACTUAL DUALITY p=')==16
assert q.count('BIPARTITE DOUBLE ordinary Bass')==4
assert q.count('MODULAR POLYNOMIAL MATCH PASS')==4
assert q.count('VELU DUALITY MATCH PASS')==4
assert 'ALL QUATERNION IDEAL / EXACT NORM-ENUMERATION CHECKS PASS' in q
assert l.count('#J via P=')==36
assert l.count('product invariant factors=')==12
assert 'ALL LABEL / SMITH / POINT-ORDER CHECKS PASS' in l
assert c.count('good model vs Brandt characteristic polynomial MATCH PASS')==4
assert c.count('good model direct point count')==8
assert 'GROUP=[48]' in c
print('CERTIFICATES: Brandt/Hecke cells=24; unweighted natural-reversal Bass cells=16; weighted cells=8')
print('CERTIFICATES: quaternion neighbour primes=4; bipartite-double Bass cells=4; Smith levels=36; elliptic-product comparisons=12')
print('CERTIFICATES: good model polynomials=4; independent point counts=8; full Mumford group enumeration at F5=48')
print('SAVED OUTPUT AUDIT PASS')
