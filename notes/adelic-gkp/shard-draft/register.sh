#!/bin/sh
# Registration of the adelic-GKP ladder shard (lane P draft). Run from the repository root.
# Idempotence is not attempted: run once on a clean tree.
set -e
D=notes/adelic-gkp/shard-draft
test -f report.tex && test -d db || { echo "run from the repository root"; exit 1; }
cp $D/04za_adelic_gkp_ladder.tex report/sections/04za_adelic_gkp_ladder.tex
# include order = sorted file names: 04za sorts after 04z_ and before 05_
grep -q '04za_adelic_gkp_ladder' report.tex || \
  sed -i 's#^\\include{report/sections/04z_cerednik_drinfeld}$#&\n\\include{report/sections/04za_adelic_gkp_ladder}#' report.tex
tail -n +2 $D/claims-rows.tsv      >> db/claims.tsv
tail -n +2 $D/definitions-rows.tsv >> db/definitions.tsv
tail -n +2 $D/provenance-rows.tsv  >> db/provenance.tsv
# SHARD-SCRIPTS parity: the gate wants outputs/<stem>*.txt for every script named in a header
for s in curve_bridge cone_bridge overlap_data no_lift zn_flux cm_lift gate_phases ff_dirichlet family_vacuum family_weil step_powers zeta_ingredients; do
  cp notes/adelic-gkp/checks/output_$s.txt outputs/check_$s.txt
done
python3 scripts/labbook_check.py --regen
python3 scripts/labbook_check.py
