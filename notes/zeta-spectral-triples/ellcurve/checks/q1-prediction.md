# Prediction recorded before spectral runs

2026-09-18, before running `ell_check.py` or computing either block's spectrum.

No H-a/H-b/H-c is forced just by the root number. Under even-simple the quotient
has dimension 2N and equal parity dimensions N,N, so its characteristic
polynomial is even. A zero at the centre has even multiplicity. It cannot
represent a single central zero with its true multiplicity. A disappearing
residue at zero does not change the 2N count: use det(D-s)g(s), including
cancelled poles. The normalisation sum xi_j=1 can make coefficients very large;
vanishing of xi_0 in that normalisation is not automatic.

Working prediction for 37a1: H-a (an odd simple minimum) is plausible because
the central spectral mass penalises only the even block. I predict it in at
least part of the scan, with low confidence; this is not a theorem. Even-simple
with a small pair remains possible and would be a numerical H-b-type outcome,
without proving multiplicity recovery. Neither outcome follows from w=-1.

For an odd simple radical xi, B=<beta,xi> is nonzero: T D xi=B eta and
D xi cannot lie in the one-dimensional odd radical. Thus replacing eta by
beta/B gives D'=D-|D xi><beta|/B, self-adjoint for T on the quotient. Its
quotient parity dimensions are N+1,N-1 and it has at least two zero modes.
This finite-dimensional variant does not solve odd central multiplicity and
does not preserve the original Fourier-transform determinant formula.
