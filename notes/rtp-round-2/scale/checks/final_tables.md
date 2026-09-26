## S2–S4. Consolidated certified tables

**NUMERICAL.** All short decimal entries below are rounded identically at both endpoints of their source balls (`checks/render_tables.py`). Full enclosures remain in the outputs. `N_conv` is the lower member of the first passing pair on the stated 40-mode grid; the reported epsilon and comparison use the upper member.

| x | N_conv | final N | precision (bits) | eps_final | eps_Nconv / eps_final | N_conv / (x ln x) |
|---|---|---|---|---|---|---|
| 13 | 400 | 440 | 1000 | 2.54625083997e-59 | 1.00374654794 | 11.9960383154 |
| 25 | 500 | 540 | 1800 | 1.9406109046e-123 | 1.00455692105 | 6.2133493456 |
| 50 | 900 | 940 | 4200 | 1.50598703959e-258 | 1.00763277544 | 4.60119993544 |

**NUMERICAL — COMPARISON STEP (zeros used here only).** All first roots have an interval-Newton enclosure and a certificate that the preceding positive range is root-free. The final column is an independent, prime-free control (pole plus archimedean terms), certified at 512 bits.

| x | first-zero error | error / eps | eps / P(x) | control negative inertia (even, odd) |
|---|---|---|---|---|
| 13 | 1.78192540377e-55 | 6998.23197229 | 9.27178716508 | (2,2) |
| 25 | 1.80189109021e-119 | 9285.17450838 | 11.5154460954 | (3,3) |
| 50 | 1.62704426106e-254 | 10803.8397296 | 10.8184224773 | (3,4) |

**NUMERICAL (certified slopes of the finite-N endpoints).**

| consecutive x | digits per unit x |
|---|---|
| 13 → 25 | 5.34316355982 |
| 25 → 50 | 5.40440468932 |
