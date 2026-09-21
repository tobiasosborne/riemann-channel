#!/usr/bin/env bash
# Local CI/CD for the lab book. Run by `make ci` and by the pre-commit hook (`make hooks`).
# Fails loud on: stale generated files, any parity error from the gate, a failed or warning-laden
# LaTeX build, or whitespace errors. Bounded by timeouts; no detached processes.
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT"

step() { printf '\n== %s\n' "$*"; }

step "git diff --check"
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then git diff --check; fi

step "generated files are current"
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
cp report/macros.tex "$tmp/macros.tex" 2>/dev/null || true
cp report/generated/status.tex "$tmp/status.tex" 2>/dev/null || true
cp report/generated/notation_table.tex "$tmp/notation_table.tex" 2>/dev/null || true
cp report/README.md "$tmp/README.md" 2>/dev/null || true
cp report/SHARD_CATALOG.md "$tmp/SHARD_CATALOG.md" 2>/dev/null || true
timeout 60 python3 scripts/labbook_check.py --regen >/dev/null
if ! cmp -s report/macros.tex "$tmp/macros.tex" || ! cmp -s report/generated/status.tex "$tmp/status.tex" \
   || ! cmp -s report/generated/notation_table.tex "$tmp/notation_table.tex" \
   || ! cmp -s report/README.md "$tmp/README.md" || ! cmp -s report/SHARD_CATALOG.md "$tmp/SHARD_CATALOG.md"; then
  echo "ci: generated TeX was stale; regenerated. Re-run and commit the result." >&2; exit 1
fi

step "lab-book gate (parity) + fresh build + log scan"
timeout 900 python3 scripts/labbook_check.py --build

step "refs manifest"
if [ -d refs/src ]; then (cd refs && timeout 120 sha256sum -c --quiet manifest.sha256); else echo "refs/src absent (run refs/fetch_sources.sh); provenance quotes were checked only if present"; fi

step "evidence scripts smoke (fast ones)"
# Only scripts that finish in a few seconds run here (the pre-commit hook re-runs every one of them on
# every commit). weil_positivity.py (minutes) is deliberately NOT in this list; the slower scripts
# (graded_permutation, phase_side_lindbladian, graded_ramanujan, elliptic_cavity: 25-55 s each) run
# only with CI_FULL=1. Everything else is re-run by `make scripts-run`. Timed 2026-09-21.
FAST="scripts/qihara.py scripts/qihara_general.py scripts/bc_entropy.py scripts/bc_symmetry_generators.py scripts/cmps_parity_supertrace.py scripts/ring_norm_certificate.py scripts/zeta_conditions.py scripts/selberg_letters.py scripts/weil_window_extension.py scripts/rebound_state.py scripts/cusp_graph.py scripts/ihara_dirac.py scripts/ccm_tensor_network.py"
SLOW="scripts/graded_permutation.py scripts/phase_side_lindbladian.py scripts/graded_ramanujan.py scripts/elliptic_cavity.py"
LIST="$FAST"; if [ "${CI_FULL:-0}" = "1" ]; then LIST="$FAST $SLOW"; fi
for s in $LIST; do
  [ -f "$s" ] || continue
  n="$(basename "$s" .py)"
  timeout 120 python3 "$s" > "$tmp/$n.txt" 2>&1
  if ! diff -q <(grep -v '^\s*$' "outputs/$n.txt") <(grep -v '^\s*$' "$tmp/$n.txt") >/dev/null; then
    echo "ci: outputs/$n.txt differs from a fresh run of $s (seeded scripts must be reproducible)" >&2
    diff "outputs/$n.txt" "$tmp/$n.txt" | head -20 >&2; exit 1
  fi
done

step "report.pdf is in lockstep with sources"
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  if git diff --quiet -- report.tex report/ db/ && ! git diff --quiet -- report.pdf; then
    echo "ci: report.pdf changed with no source change (fine if fonts/date only)";
  fi
fi
printf '\nci: all green\n'
