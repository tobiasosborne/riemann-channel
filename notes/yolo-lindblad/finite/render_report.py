#!/usr/bin/env python3
"""Render the authored report with numeric tables taken only from checked results."""
import json
import re
from finite_common import HERE, SEED


def table(headers, rows):
    return "\n".join(["| " + " | ".join(headers) + " |",
                      "| " + " | ".join("---" for _ in headers) + " |"] +
                     ["| " + " | ".join(map(str, row)) + " |" for row in rows])


def main():
    names = ("verify_phase", "verify_characters", "verify_ramanujan", "hunt", "spectrum", "balance")
    R = {name: json.loads((HERE/f"{name}.json").read_text()) for name in names}
    manifest = json.loads((HERE/"manifest.json").read_text())
    assert all(r["seed"] == SEED and r["checks"] == manifest["tallies"][name] for name, r in R.items())
    p, c, a, h, s, b = (R[name] for name in names)
    content = {}
    purposes = ("N1: direct quotient and shell checks", "N2: characters, coherence counterexample, BC transfer",
                "N3: exact Ramanujan and Gibbs identities", "N4: doubled model, truncation, pole/zero hunt",
                "N5: spectrum, parity leakage, Galois shifts", "N6: exact counterexample and stationary states")
    content["TALLIES"] = table(["Script", "Scope", "Passed / failed"],
                                [[f"[{name}.py](finite/{name}.py)", purpose, f"{R[name]['checks']} / 0"]
                                 for name, purpose in zip(names, purposes)] +
                                [["**Total**", "Scientific assertions", f"**{manifest['total']} / 0**"]])
    content["VERSIONS"] = "Recorded environment: " + "; ".join(f"{k} `{v}`" for k, v in manifest["versions"].items()) + "."
    content["TRUNCATION"] = table(["P", "Bmax = shell states", "Doubled dimension", "Max norm² loss", "Rate-weighted mean loss"],
                                      [[r["P"], r["Bmax"], r["doubled_dimension"], r["max_loss"], f"{r['weighted_mean_loss']:.6f}"] for r in h["truncation"]])
    content["PHASE_ERRORS"] = table(["Direct check", "Maximum absolute error"],
                                        [[k.replace("_", " "), f"{v:.3e}"] for k, v in p["errors"].items()])
    content["CHARACTERS"] = table(["β", "Re αχ", "Im αχ", "Orthogonal residual", "Re aχ draft", "Re ΔP", "Re C≥2"],
                                      [[r["beta"], *[f"{r[k]:.6f}" for k in ("projected_real", "projected_imag", "nonscalar_residual",
                                                                           "proposed_real", "log_difference_real", "prime_power_correction_real")]]
                                       for r in c["rows"] if r["chi"] == [1]])
    content["CHARACTER_ERRORS"] = (f"All {c['characters']} characters were included. Maximum errors: adjoint scalar "
                                  f"`{c['adjoint_error']:.3e}`, Galois diagonalization `{c['galois_error']:.3e}`, "
                                  f"BC units-block eigenvalue `{c['bc_error']:.3e}`.")
    content["RAMANUJAN"] = table(["P", "n", "nP", "s", "Nonzero-support terms enumerated", "Exact series value"],
                                    [[r[k] for k in ("P", "n", "nP", "s", "terms", "value")]
                                     for r in a["rows"] if r["P"] == 5 and r["n"] in (1, 6, 29)])
    content["HUNT_ERROR"] = f"Maximum doubled-solve/formula discrepancy: `{h['operator_error']:.3e}` (`hunt.py`)."
    content["HUNT_POLES"] = table(["P", "Bmax", "Ordered real pole", "Euler factor pole Re s", "Rectangle poles", "Tested overlap zeros"],
                                      [[r["P"], r["Bmax"], f"{r['ordered_real_pole']:.9f}", f"{r['euler_pole_real']:.2f}",
                                        r["rectangle_poles"], r["rectangle_overlap_zeros"]] for r in h["cases"] if r["beta"] == 1.])
    content["HUNT_BETA"] = table(["P", "Bmax", "β", "Ordered real pole", "Euler factor pole Re s"],
                                     [[r["P"], r["Bmax"], r["beta"], f"{r['ordered_real_pole']:.9f}", f"{r['euler_pole_real']:.2f}"]
                                      for r in h["cases"] if r["P"] == 47])
    content["AT_ONE"] = table(["P", "F(1)", "FE(1)"], [[r["P"], f"{r['F']:.9f}", f"{r['E']:.9f}"] for r in h["regular_at_one"]])
    content["ZERO_COMPARISON"] = table(["n", "γn (comparison only)", "abs F", "abs FE", "abs(1 − SP)"],
                                           [[r["n"], f"{r['gamma']:.9f}", f"{r['abs_F']:.9f}", f"{r['abs_E']:.9f}",
                                             f"{r['abs_ordered_denominator']:.9f}"]
                                            for r in h["zero_comparisons"] if r["P"] == 47 and r["n"] <= 3])
    content["RATIOS"] = table(["P", "abs(F / (1/ζP)) at 1/2+iγ1"],
                                  [[r["P"], f"{r['abs']:.9f}"] for r in h["ratios"] if r["n"] == 1])
    content["PARITY_ERROR"] = (f"For the explicit `Bmax=30, P=5` test, the largest odd-to-even matrix element is "
                               f"`{s['parity_leakage_max']:.9f}`, the largest grading commutator entry is "
                               f"`{s['parity_commutator_max']:.9f}`, and the largest trace defect entry is "
                               f"`{s['trace_defect_max']:.9f}`.")
    def spectral_rows(beta_filter):
        return [[r["P"], r["beta"], f"{r['min_real']:.9f}", f"{r['max_real']:.9f}", r["distinct_real"], "0 (exact)"]
                for r in s["rows"] if r["Bmax"] == 3072 and beta_filter(r)]
    headers = ["P", "β", "Min Re τ", "Max Re τ", "Distinct real values", "Max abs Im τ"]
    content["SPECTRUM"] = table(headers, spectral_rows(lambda r: r["beta"] == 1.))
    content["SPECTRUM_BETA"] = table(headers, spectral_rows(lambda r: r["beta"] != 1.))
    content["DEPHASING"] = (f"With `γ={s['gamma']}`, the maximum dephasing coefficient error is "
                            f"`{s['galois_error']:.3e}`. The test includes {s['character_within_pairs']} same-character "
                            f"and {s['character_cross_pairs']} cross-character Gauss-basis coherences, and "
                            f"{s['trivial_shells']} trivial shell vectors. Maximum character-sector leakage of the "
                            f"compressed phase jumps is `{s['covariance_error']:.3e}`; seeded direct unitary-average "
                            "checks agree with the coefficient calculation.")
    content["BALANCE_LOCAL"] = table(["β", "Gibbs residual, stated rates", "Gibbs residual, swapped rates", "Actual vacuum population", "Actual top population"],
                                          [[r["beta"], *[f"{r[k]:.9f}" for k in ("gibbs_residual", "corrected_rate_gibbs_residual", "stationary_vacuum", "stationary_top")]]
                                           for r in b["local_rows"] if r["p"] == 2])
    content["BALANCE_PRODUCT"] = table(["B", "Shell states", "β", "Proposed Gibbs residual", "Actual vacuum", "Actual top"],
                                            [[r["B"], r["states"], r["beta"], *[f"{r[k]:.9f}" for k in ("gibbs_residual", "vacuum", "top")]] for r in b["product_rows"]])
    content["CRITICAL"] = table(["β", "ZB(β)", "Captured infinite Gibbs mass", "Finite Gibbs vacuum weight"],
                                    [[r["beta"], f"{r['Z']:.9f}", f"{r['captured_mass']:.9f}" if r["captured_mass"] is not None else "—",
                                      f"{r['vacuum']:.9f}"] for r in b["critical"] if r["Bmax"] == 3072])
    template = (HERE/"report_template.md").read_text()
    assert not any(ord(c) < 32 and c not in "\n\t" for c in template)
    assert set(re.findall(r"@@([A-Z_]+)@@", template)) == set(content)
    for key, value in content.items():
        template = template.replace(f"@@{key}@@", value)
    assert "@@" not in template
    (HERE.parent/"astra-finite-model.md").write_text(template)
    print(f"render_report.py: {len(content)} generated sections; 4 integrity checks passed")


if __name__ == "__main__":
    main()
