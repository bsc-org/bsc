#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

# Python-Venv anlegen und Abhaengigkeiten installieren, falls nicht vorhanden
if [ ! -d .venv ]; then
  python3 -m venv .venv
  .venv/bin/pip install --upgrade pip
  .venv/bin/pip install -r requirements.txt
fi

# Lokalen MkDocs-Server starten (Live-Reload auf Port 8000).
# Zusaetzliche mkdocs-Argumente werden durchgereicht, z.B.:
#   ./serve.sh -a 0.0.0.0:8080
exec .venv/bin/mkdocs serve "$@"
