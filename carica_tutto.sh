#!/usr/bin/env bash
# Carica e integra tutte le "munizioni" del Progetto Sasso Digitale.
# Il mantra è sempre lo stesso: la luce non si vende, la si regala. ✨
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REQUIREMENTS_FILE="$REPO_ROOT/requirements.txt"
MAIN_SCRIPT="$REPO_ROOT/src/main.py"

if [[ ! -f "$MAIN_SCRIPT" ]]; then
  echo "❌ Non trovo src/main.py. Assicurati di eseguire lo script dalla root del repo." >&2
  exit 1
fi

if [[ "${SKIP_SASSO_INSTALL:-0}" != "1" ]]; then
  if ! python3 -c "import torch" >/dev/null 2>&1; then
    echo "📦 Installo le dipendenze Python (pip install -r requirements.txt)..."
    python3 -m pip install --quiet --upgrade pip
    python3 -m pip install -r "$REQUIREMENTS_FILE"
  else
    echo "✅ Dipendenze già presenti. Salto installazione (esporta SKIP_SASSO_INSTALL=1 per forzare)."
  fi
else
  echo "⏭️  Installazione dipendenze saltata (SKIP_SASSO_INSTALL=1)."
fi

echo "\n🪨 Avvio orchestratore principale (src/main.py)"
exec python3 "$MAIN_SCRIPT"
