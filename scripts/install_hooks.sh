#!/usr/bin/env bash
# Install the local CI as a git pre-commit hook (lockstep: no commit with a red gate or stale PDF).
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
HOOK="$ROOT/.git/hooks/pre-commit"
cat > "$HOOK" <<'EOF'
#!/usr/bin/env bash
# riemann-channel pre-commit: run the lab-book CI when report/db/notes/scripts are staged.
if git diff --cached --name-only | grep -Eq '^(report\.tex|report/|db/|notes/|scripts/|outputs/|refs/manifest\.sha256)'; then
  exec scripts/ci_local.sh
fi
EOF
chmod +x "$HOOK"
echo "installed $HOOK"
