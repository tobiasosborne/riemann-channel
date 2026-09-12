REPORT_TEX := report.tex
REPORT_SHARDS := $(shell find report/sections -type f -name '*.tex' 2>/dev/null | sort)
REPORT_PDF := report.pdf
PY := python3

.PHONY: report regen check ci hooks clean-report clobber-report scripts-run refs

report: $(REPORT_PDF)

# Fresh build every time (a stale PDF is never reused); the gate parses report.log afterwards.
$(REPORT_PDF): $(REPORT_TEX) $(REPORT_SHARDS) report/references.bib report/macros.tex report/generated/status.tex
	timeout 600 latexmk -pdf -interaction=nonstopmode -halt-on-error $(REPORT_TEX)

# Regenerate the two generated TeX files from the databases.
regen:
	$(PY) scripts/labbook_check.py --regen

# The gate: parity of shards/notes/scripts/claims/definitions/notation/provenance, no build.
check:
	$(PY) scripts/labbook_check.py

# Local CI/CD: gate + fresh build + log scan + git diff --check. Installed as pre-commit by `make hooks`.
ci:
	scripts/ci_local.sh

hooks:
	scripts/install_hooks.sh

# Re-run every evidence script and refresh outputs/ (slow: weil_lps p=29 is minutes).
scripts-run:
	for s in scripts/qihara.py scripts/bcmpo.py scripts/scat.py scripts/ringnorm.py scripts/artin_schreier_mps.py scripts/qihara_general.py scripts/weil_positivity.py; do \
	  n=$$(basename $$s .py); timeout 1800 $(PY) $$s > outputs/$$n.txt 2>&1 || exit 1; done

refs:
	refs/fetch_sources.sh

clean-report:
	latexmk -c $(REPORT_TEX)

clobber-report:
	latexmk -C $(REPORT_TEX)
	rm -f $(REPORT_PDF)
