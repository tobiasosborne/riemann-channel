"""REFUTE scratch: the number max|J13-J17| = 0.61 of family-vacuum.md 2(a) is basis dependent; evaluate it in the vertex basis."""
import sys; sys.argv = ['x']
exec(open('scratch_gkp_ffm_lps.py').read().split('# per-plane facts')[0])
from scipy.linalg import sqrtm
PW = Uw@Uw.T
out = {}
for q, A in [(13, A13), (17, A17)]:
    Dm = Uw@np.diag(1/np.sqrt(4*q-np.diag(Uw.T@A@Uw)))@Uw.T   # (4q - A^2)^{-1/2} on W, 0 off W
    Dm = Uw@np.real(np.linalg.inv(sqrtm(4*q*np.eye(Uw.shape[1])-(Uw.T@A@Uw)@(Uw.T@A@Uw))))@Uw.T
    out[q] = (M(q, A)-Vq(q, A))@np.block([[Dm, Z], [Z, Dm]])
print('vertex basis, restricted to W (x) R^2: max entry |J13-J17| =', round(np.abs(out[13]-out[17]).max(), 4),
      '; operator norm', round(np.linalg.norm(out[13]-out[17], 2), 4))
