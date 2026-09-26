# Sources and provenance of the curve data (lane ellcurve-conductors)

Author: `claude:opus`, 2026-09-26. Nothing below was typed from memory: every model comes from a fetched file and
is checked by at least one independent computation.

## What the driver needs

`zst_ell_ref` (`zst/src/ell_ref.c`) reads, per curve, one line `curve <label> <a1,a2,a3,a4,a6> <C> <w> <rank>`
and stops at `end`. The `ap` lines are not read by it (they serve Lane B's tests), and `zero` lines are read only
when `K > 0`, i.e. in the driver's COMPARISON STEP, which these runs skip (`--compare 0`). So the appended entries in
`ell_ref_ext.txt` carry the curve line only: no `ap`, no `zero`. The model and conductor are the only
inputs to the form (`zst_weil_ellcurve`: "both inputs ... never computed here"); `a_p` come from `zst_ell_ap`,
zst's own point count on the model. The root number and rank are printed in the header and used by the driver only
to decide whether a comparison is possible.

## Primary source (machine-readable, byte-exact)

| what | URL | fetched | sha256 |
|---|---|---|---|
| Cremona, `ecdata`, `allcurves/allcurves.00000-09999` (columns: conductor, isogeny class, number, a-invariants of the minimal model, rank, torsion order) | `https://raw.githubusercontent.com/JohnCremona/ecdata/master/allcurves/allcurves.00000-09999` | 2026-09-26, `curl` | `259f3846329395b371e8079c77a6f1097adaebc98a054974573e241416efa968` |

The 19 rows used are copied verbatim to `cremona_rows.txt`. Cremona's tables are the upstream of the LMFDB's
elliptic-curve data for these conductors; label `Na1` is the Gamma_0(N)-optimal curve of class `a`.

## Second source: LMFDB

The LMFDB API was reachable only intermittently: `curl` got a reCAPTCHA page at once; `WebFetch` (which returns a
model's summary of the page, not the raw bytes) got data for the first few requests and then the same reCAPTCHA
page. Fields used: `ainvs`, `conductor`, `rank`, `analytic_rank`, `optimality`. Because WebFetch output is a
paraphrase, LMFDB serves here as a cross-source only; the values entering `ell_ref_ext.txt` are Cremona's, checked
by PARI (next section). One WebFetch answer shows why: the page `https://www.lmfdb.org/EllipticCurve/Q/21/a/1` is
LMFDB `21.a1` = Cremona `21a5`, a different curve, and the summariser reported "Root number: -1" for 24a1, an
analytic-rank-0 curve (evidently a local root number from the local-data table). No root number was taken from
LMFDB.

| curve | URL (fetched 2026-09-26) | LMFDB label | ainvs | C | rank / analytic rank | optimal | agrees with Cremona row |
|---|---|---|---|---|---|---|---|
| 11a1 | `https://www.lmfdb.org/api/ec_curvedata/?Clabel=11a1&_format=json&_fields=Clabel,lmfdb_label,ainvs,conductor,rank,analytic_rank,optimality,absD,signD,bad_primes` | 11.a2 | [0,-1,1,-10,-20] | 11 | 0 / 0 | optimality 1 | yes (absD 161051, bad primes [11]) |
| 14a1 | same API, `Clabel=14a1` | 14.a6 | [1,0,1,4,-6] | 14 | 0 / 0 | 1 | yes (absD 21952, [2,7]) |
| 15a1 | same API, `Clabel=15a1`; also `https://www.lmfdb.org/api/ec_curvedata/?conductor=15&_format=json` (all 8 curves of conductor 15; 15a1 = 15.a5 is the one with `optimality: 1`) | 15.a5 | [1,1,1,-10,-10] | 15 | 0 / 0 | 1 | yes (absD 50625, [3,5]) |
| 17a1 | same API, `Clabel=17a1` | 17.a3 | [1,-1,1,-1,-14] | 17 | 0 / 0 | 1 | yes (absD 83521, [17]) |
| 19a1 | same API, `Clabel=19a1` | 19.a2 | [0,1,1,-9,-15] | 19 | 0 / 0 | 1 | yes (absD 6859, [19]) |
| 20a1 | same API, `Clabel=20a1` | 20.a4 | [0,1,0,4,4] | 20 | 0 / 0 | 1 | yes (absD 6400, [2,5]) |
| 21a1 | `https://www.lmfdb.org/EllipticCurve/Q/21a1/` | 21.a5 | [1,0,0,-4,-1] | 21 | 0 / 0 | "Gamma_0(N)-optimal: yes" | yes (discriminant 3969) |
| 24a1 | `https://www.lmfdb.org/EllipticCurve/Q/24a1/` | 24.a4 | [0,-1,0,-4,4] | 24 | 0 / 0 | yes | yes |
| 26a1 | `https://www.lmfdb.org/EllipticCurve/Q/26a1/` | 26.a2 | [1,0,1,-5,-8] | 26 | 0 / 0 | yes | yes |
| 27a1 | `https://www.lmfdb.org/EllipticCurve/Q/27a1/` | 27.a3 | [0,0,1,0,-7] | 27 | 0 / 0 | yes | yes |
| 30a1 | `https://www.lmfdb.org/EllipticCurve/Q/30a1/` | 30.a8 | [1,0,1,1,2] | 30 | 0 / 0 | yes | yes |
| 32a1 | same API, `Clabel=32a1` | 32.a4 | [0,0,0,4,0] | 32 | 0 / 0 | 1 | yes (absD 4096, [2]) |
| 33a1 | `https://www.lmfdb.org/EllipticCurve/Q/33a1/` | 33.a2 | [1,1,0,-11,0] | 33 | 0 / 0 | (summary quoted the isogeny sentence, not the optimality line) | yes (ainvs, C, rank) |
| 35a1 | `https://www.lmfdb.org/EllipticCurve/Q/35a1/` | 35.a3 | [0,1,1,9,1] | 35 | 0 / 0 | yes | yes (discriminant -42875) |
| 36a1 | `https://www.lmfdb.org/EllipticCurve/Q/36a1/` | 36.a4 | [0,0,0,0,1] | 36 | 0 / 0 | yes | yes (minimal discriminant -432) |
| 34a1 | `https://www.lmfdb.org/EllipticCurve/Q/34a1/` (third attempt) | 34.a4 | [1,0,0,-3,1] | 34 | 0 / 0 | yes | yes (discriminant 1088) |
| 50a1 | `https://www.lmfdb.org/EllipticCurve/Q/50a1/` (third attempt) | 50.a3 | [1,0,1,-1,-2] | 50 | 0 / 0 | yes | yes (discriminant -1250) |
| 67a1 | `https://www.lmfdb.org/EllipticCurve/Q/67a1/` | 67.a1 | [0,1,1,-12,-21] | 67 | 0 / 0 | yes | yes (minimal discriminant -67) |
| 109a1 | `https://www.lmfdb.org/EllipticCurve/Q/109a1/` | 109.a1 | [1,-1,0,-8,-7] | 109 | 0 / 0 | yes | yes |

The API requests for 21a1–30a1 by `Clabel` were refused (reCAPTCHA); the curve pages above were fetched instead, several
only after repeated attempts. In the end all 19 curves have an LMFDB record agreeing with the Cremona row in a-invariants,
conductor and rank (and analytic rank 0), and 18 of 19 state Gamma_0(N)-optimality explicitly (33a1: the summary did not quote it).

## Independent checks (all pass)

`checks/check_models.py` (run with PARI 2.17.2 through `cypari2` in a scratch venv; output `checks/check_models.out`,
`# checks: 152 run, 0 failed`):

1. Pure Python from the a-invariants: the prime support of the discriminant equals the prime support of the
   conductor for all 19 curves; the multiplicative primes (p | Delta, p not dividing c4, valid for a minimal model at
   every p including 2, 3) are exactly the primes with exponent 1 in the conductor. A sufficient minimality test
   (v_p(Delta) < 12 or v_p(c4) < 4) passes at every bad prime except p = 2 for 32a1 (v_2(Delta) = 12, v_2(c4) = 6:
   inconclusive), where PARI decides.
2. PARI: `ellglobalred` conductor = the table's conductor (Tate's algorithm, independent of the table);
   `ellminimalmodel` returns the model itself (minimal at every prime, 32a1 included); `ellrootno` = +1;
   `ellanalyticrank` = 0 (an L-value computation at s = 1; no zeros).
3. `checks/ap_check.c` + `checks/ap_compare.py`: `zst_ell_ap` (the point count the driver uses, read through
   `zst_ell_ref` from `ell_ref_ext.txt`) equals PARI `ellap` for all 46 primes below 200 on all 19 curves
   (`checks/ap_compare.out`: 19 run, 0 failed). This also checks that the extended file parses as intended.

Root numbers in `ell_ref_ext.txt` are +1 (PARI `ellrootno`; forced by analytic rank 0). Ranks are 0 (Cremona
table, LMFDB where fetched, PARI analytic rank).
