#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sync-Script fuer das BSC-Settings-Rendering der Doku (components/bsc).

Kopiert die Firmware-Settings-Daten (params/*.json inkl. combos/ und refs/)
in den versionspezifischen Ordner `bsc_settings/<version>/`, generiert die
Typ-Zuordnung `type_map.json` aus WebSettings.h, die Gruppen-Groessen
`groupsizes.json` aus defines.h/WebSettings.h (fuer symbolische
"groupsize"-Namen wie CNT_ALARMS) und extrahiert das CSS-Subset
der WebApp nach `docs/css/bsc-settings-<version>.css` (gescoped unter
`.bsc-settings-<version>`, Dark-Mode unter `html.dark .bsc-settings-<version>`).

Alle rem-Groessen des Subsets werden zu em konvertiert; der Scope-Root
`.bsc-settings-<version>` erhaelt die WebApp-Groessenbasis (font-size: 16px,
line-height: 1.4), damit die Darstellung unabhaengig von der erhoehten
Root-Schrift des MkDocs/Material-Themes (125-150%) der WebApp entspricht.

Aufruf:
    python3 scripts/sync_bsc_settings.py --version v010

Nur Python-Stdlib, kein Netzwerkzugriff. Ergebnis wird im Doku-Repo eingecheckt.
"""

import argparse
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

# Repo-Root der Doku (components/bsc) – Ort dieses Scripts ist scripts/
REPO_ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# CSS-Whitelist (Konzept Abschnitt 6.1). Alle Klassen, die aus der WebApp
# uebernommen werden (plus State-/Sub-Klassen, die in den zugehoerigen
# Selektoren auftauchen). W3.CSS-Klassen werden bewusst NICHT uebernommen.
# ---------------------------------------------------------------------------
CSS_WHITELIST = {
    # Grundgeruest / Flex / Texte
    "listview", "flex-container", "flex-item", "sub-item", "head", "subHead",
    "item4", "settings-row-warning", "dynamic-select-invalid",
    "dynamic-select-warning",
    # Gruppen
    "group-block",
    # Sektionen
    "separation-card", "separation-card-title", "section-toggle-btn",
    "section-toggle-title", "section-toggle-icon", "separation-list",
    "section-collapsed",
    # Collapsible
    "settings-collapsible-block", "settings-collapsible-list",
    # Multicheck
    "toggle", "lbl-toggle", "collapsible-content", "content-inner",
    "selected-summary", "tag",
    # Rows
    "settings-row", "settings-row-wrap", "settings-row-grid",
    "settings-row-grid-paired", "row-item-label", "row-item-value-wrap",
    "row-item-value", "row-item-unit", "settings-row-label-cell",
    "settings-row-value-cell",
    # Profile-Paare
    "profile-entry-flex", "profile-pair", "profile-slot", "profile-slot-label",
    "profile-slot-row", "profile-pair-row", "profile-single",
    # Profilgraph
    "profile-label", "profile-control", "chart-wrap", "profile-svg",
    "points-table",
    # Fehlerbox (eigene Regel wird weiter unten ergaenzt)
    "bsc-settings-error",
}

# Variablen, die aus :root (Light) bzw. .dark (Dark) der WebApp uebernommen
# werden (Konzept Abschnitt 6.2). Die Input-Variablen werden zusaetzlich
# gebraucht, weil die uebernommene Regel `.dark .listview input` sie referenziert.
LIGHT_VARS = [
    "--bg", "--text", "--muted", "--card-bg", "--surface-border",
    "--primary", "--primary-100", "--primary-500",
    "--listview-head-bg", "--listview-head-color", "--accent-danger",
    "--pf-curve", "--pf-point-fill", "--pf-point-stroke", "--pf-text",
    "--pf-grid",
    # Tag-Pills der Multicheck-Summary (.lbl-toggle .selected-summary .tag)
    "--lbl-toggle-tag-bg", "--lbl-toggle-tag-text",
]
DARK_VARS = LIGHT_VARS + ["--input-bg", "--input-border", "--input-focus-shadow"]

CLASS_RE = re.compile(r"\.([A-Za-z_][A-Za-z0-9_-]*)")
DARK_PREFIX_RE = re.compile(r"^(?:html\.dark|\.dark)\s+(.+)$", re.S)
VAR_RE = re.compile(r"(--[A-Za-z0-9_-]+)\s*:\s*([^;]+);")
# rem -> em: Die WebApp geht von der Browser-Basis 16px aus; MkDocs/Material
# erhoeht die Root-Schrift auf 125-150%. em-Werte beziehen sich auf die
# 16px-Basis, die auf dem Scope-Root gesetzt wird (siehe extract_css).
REM_RE = re.compile(r"(\d+(?:\.\d+)?)rem\b")


def rem_to_em(text):
    """Konvertiert alle rem-Groessen in em (WebApp-Groessenbasis 16px)."""
    return REM_RE.sub(r"\1em", text)


def log(msg):
    print(msg)


def warn(msg):
    print(f"WARNUNG: {msg}")


# ---------------------------------------------------------------------------
# 1. Params kopieren
# ---------------------------------------------------------------------------
def sync_params(firmware_path, version_dir):
    """Kopiert params/ KOMPLETT (inkl. combos/ und refs/) nach
    bsc_settings/<version>/params/. Idempotent: Ziel wird geleert."""
    src = firmware_path / "params"
    dst = version_dir / "params"
    if not src.is_dir():
        raise FileNotFoundError(f"Firmware-Params nicht gefunden: {src}")

    if dst.exists():
        warn(f"Zielverzeichnis existiert bereits und wird ueberschrieben: {dst}")
        shutil.rmtree(dst)
    shutil.copytree(src, dst)

    copied = sum(1 for p in dst.rglob("*") if p.is_file())
    log(f"Params kopiert: {src} -> {dst} ({copied} Dateien)")
    return copied


# ---------------------------------------------------------------------------
# 2. type_map.json generieren
# ---------------------------------------------------------------------------
def generate_type_map(firmware_path, version_dir):
    """Parst #define HTML_... <zahl> aus include/settings/WebSettings.h."""
    header = firmware_path / "include" / "settings" / "WebSettings.h"
    if not header.is_file():
        raise FileNotFoundError(f"WebSettings.h nicht gefunden: {header}")

    type_map = {}
    define_re = re.compile(r"^\s*#define\s+(HTML_[A-Za-z0-9_]+)\s+(\d+)\s*$")
    for line in header.read_text(encoding="utf-8", errors="replace").splitlines():
        m = define_re.match(line)
        if m:
            type_map[m.group(1)] = int(m.group(2))

    if not type_map:
        warn("Keine HTML_-Defines in WebSettings.h gefunden – type_map.json ist leer.")

    out = version_dir / "type_map.json"
    out.write_text(json.dumps(type_map, indent=2, sort_keys=True) + "\n",
                   encoding="utf-8")
    log(f"type_map.json generiert: {len(type_map)} Typen ({out})")

    # Warnung, wenn ein in den Params verwendeter Typname im Mapping fehlt
    used = set()
    for f in (version_dir / "params").glob("*.json"):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue

        def walk(node):
            if isinstance(node, dict):
                t = node.get("type")
                if isinstance(t, str) and t.startswith("HTML_"):
                    used.add(t)
                for v in node.values():
                    walk(v)
            elif isinstance(node, list):
                for v in node:
                    walk(v)
        walk(data)

    for name in sorted(used - set(type_map)):
        warn(f"Typname '{name}' wird in params verwendet, fehlt aber in WebSettings.h-Mapping")
    return type_map


# ---------------------------------------------------------------------------
# 3. groupsizes.json generieren
# ---------------------------------------------------------------------------
def generate_groupsizes(firmware_path, version_dir):
    """Parst numerische #define-Werte aus include/defines.h und
    include/settings/WebSettings.h (defines.h hat Vorrang) und schreibt sie
    nach bsc_settings/<version>/groupsizes.json. Damit kann der Renderer
    symbolische "groupsize"-Namen (z.B. CNT_ALARMS) aufloesen."""
    sources = [
        firmware_path / "include" / "defines.h",
        firmware_path / "include" / "settings" / "WebSettings.h",
    ]
    sizes = {}
    define_re = re.compile(r"^\s*#define\s+([A-Za-z_][A-Za-z0-9_]*)\s+"
                           r"((?:0[xX][0-9A-Fa-f]+)|(?:\d+))\s*$")
    for src in sources:
        if not src.is_file():
            warn(f"Defines-Quelle nicht gefunden: {src}")
            continue
        for line in src.read_text(encoding="utf-8", errors="replace").splitlines():
            m = define_re.match(line)
            if m:
                name, raw = m.group(1), m.group(2)
                try:
                    sizes[name] = int(raw, 0)
                except ValueError:
                    continue

    if not sizes:
        warn("Keine numerischen Defines gefunden – groupsizes.json ist leer.")

    out = version_dir / "groupsizes.json"
    out.write_text(json.dumps(sizes, indent=2, sort_keys=True) + "\n",
                   encoding="utf-8")
    log(f"groupsizes.json generiert: {len(sizes)} Defines ({out})")
    return sizes


# ---------------------------------------------------------------------------
# 4. CSS extrahieren
# ---------------------------------------------------------------------------
def split_css_rules(text):
    """Zerlegt CSS-Text in eine Liste von (prelude, body|None)-Tupeln.
    Kommentare werden entfernt; verschachtelte Bloeke (@media) bleiben als
    Tupel mit body erhalten (die inneren Regeln werden rekursiv geparst)."""
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    out = []
    i, n = 0, len(text)
    while i < n:
        # Whitespace ueberspringen
        ws = re.match(r"\s+", text[i:])
        if ws:
            i += ws.end()
        if i >= n:
            break
        start = i
        while i < n and text[i] not in "{;}":
            i += 1
        prelude = text[start:i].strip()
        if i >= n:
            break
        if text[i] == ";":  # At-Rule ohne Block (z.B. @import)
            i += 1
            continue
        # balanced braces
        depth, j = 0, i
        while j < n:
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        if depth != 0:
            warn("CSS-Parser: unbalancierte Klammern – Extraktion wird abgebrochen")
            break
        body = text[i + 1:j]
        i = j + 1
        if prelude:
            out.append((prelude, body))
    return out


def class_in_whitelist(cls):
    if cls in CSS_WHITELIST:
        return True
    for w in CSS_WHITELIST:
        if cls.startswith(w + "-"):
            return True
    return False


def scope_selector_part(part):
    """Prueft einen einzelnen (Komma-getrennten) Selektor-Teil gegen die
    Whitelist. Gibt (is_dark, bereinigter_teil) zurueck oder None, wenn der
    Teil nicht uebernommen wird."""
    p = part.strip()
    if not p:
        return None
    is_dark = False
    m = DARK_PREFIX_RE.match(p)
    if m:
        is_dark = True
        p = m.group(1).strip()
    classes = CLASS_RE.findall(p)
    if not classes:
        return None
    for c in classes:
        if not class_in_whitelist(c):
            return None
    return is_dark, p


def filter_and_scope_rules(rules, scope_prefix):
    """Filtert eine Liste von (prelude, body)-Tupeln auf Whitelist-Regeln und
    scoped die uebernommenen Selektoren. Gibt Liste von (prelude, body) zurueck."""
    result = []
    for prelude, body in rules:
        if prelude.startswith("@"):
            # @media/@supports: innere Regeln rekursiv verarbeiten
            if prelude.lower().startswith("@keyframes"):
                continue
            inner = split_css_rules(body)
            filtered = filter_and_scope_rules(inner, scope_prefix)
            if filtered:
                inner_text = "\n".join(f"{p}{{{b}}}" for p, b in filtered)
                result.append((prelude, inner_text))
            continue
        kept_parts = []
        for part in prelude.split(","):
            res = scope_selector_part(part)
            if res is None:
                continue
            is_dark, clean = res
            if is_dark:
                kept_parts.append(f"html.dark {scope_prefix} {clean}")
            else:
                kept_parts.append(f"{scope_prefix} {clean}")
        if kept_parts:
            result.append((", ".join(kept_parts), body.strip()))
    return result


def extract_var_block(css_text, selector_regex, var_list, scope_prefix,
                      is_dark, extra_lines=None, fallback_rules=None):
    """Extrahiert die gewuenschten Variablen aus einem Block (z.B. :root oder
    .dark) und erzeugt einen gescopten Variablen-Block. Fuer den Dark-Block
    werden Variablen, die die WebApp dort nicht ueberschreibt, explizit aus
    :root uebernommen (entspricht exakt dem Vererbungsverhalten der WebApp)."""
    rules = split_css_rules(css_text)
    values = {}
    for prelude, body in rules:
        if selector_regex.match(prelude):
            for var, val in VAR_RE.findall(body):
                if var in var_list:
                    values[var] = val.strip()
            break
    missing = [v for v in var_list if v not in values]
    if missing and fallback_rules is not None:
        # Fallback: Werte aus :root (WebApp-Vererbung nachbilden)
        for prelude, body in fallback_rules:
            if re.compile(r":root\s*$").match(prelude):
                root_vals = {v: val.strip() for v, val in VAR_RE.findall(body)}
                for v in missing:
                    if v in root_vals:
                        values[v] = root_vals[v]
                break
        missing = [v for v in missing if v not in values]
    if missing:
        warn(f"CSS: Variablen nicht gefunden (in '{selector_regex.pattern}'): "
             f"{', '.join(missing)}")
    if not values:
        return ""
    lines = [f"{scope_prefix} {{"]
    for v in var_list:
        if v in values:
            lines.append(f"  {v}: {values[v]};")
    if extra_lines:
        lines.extend(extra_lines)
    lines.append("}")
    return "\n".join(lines) + "\n"


def extract_css(webapp_path, version, version_dir):
    """Extrahiert das CSS-Subset nach docs/css/bsc-settings-<version>.css."""
    src = webapp_path / "css" / "style.css"
    if not src.is_file():
        raise FileNotFoundError(f"WebApp-CSS nicht gefunden: {src}")

    css_text = src.read_text(encoding="utf-8", errors="replace")
    scope = f".bsc-settings-{version}"

    rules = split_css_rules(css_text)
    filtered = filter_and_scope_rules(rules, scope)
    if not filtered:
        warn("CSS: keine Regeln aus der Whitelist extrahiert – bitte prüfen!")

    light_block = extract_var_block(css_text, re.compile(r":root\s*$"), LIGHT_VARS,
                                    scope, is_dark=False,
                                    extra_lines=[
                                        "  /* In der WebApp von .profile-slot referenziert, dort nicht definiert */",
                                        "  --line: var(--surface-border);",
                                        "  /* WebApp-Groessenbasis: Browser-Default 16px. MkDocs/Material",
                                        "     erhoeht die Root-Schrift (125-150%) – alle em-Groessen im",
                                        "     Subset beziehen sich auf diese 16px-Basis. */",
                                        "  font-size: 16px;",
                                        "  line-height: 1.4;",
                                    ])
    dark_block = extract_var_block(css_text, re.compile(r"\.dark\s*$"), DARK_VARS,
                                   f"html.dark {scope}", is_dark=True,
                                   fallback_rules=rules)

    error_rule = rem_to_em(
        f"{scope} .bsc-settings-error {{\n"
        f"  border: 2px solid var(--accent-danger);\n"
        f"  border-radius: 8px;\n"
        f"  padding: 10px 14px;\n"
        f"  margin: 8px 0;\n"
        f"  color: var(--accent-danger);\n"
        f"  background: var(--card-bg);\n"
        f"  font-weight: 600;\n"
        f"  font-size: 0.9rem;\n"
        f"}}\n"
    )
    # Eigene Ergaenzung: In der WebApp wird das SVG per JS gestylt; fuer die
    # statische Doku braucht es eine Breitenregel, damit es responsiv skaliert.
    svg_rule = (
        f"{scope} .profile-svg {{\n"
        f"  display: block;\n"
        f"  width: 100%;\n"
        f"  height: auto;\n"
        f"}}\n"
    )

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    parts = [
        "/* bsc-settings-" + version + ".css",
        " * Generiert von scripts/sync_bsc_settings.py am " + stamp,
        " * Quelle: " + str(src),
        " * Enthaelt das CSS-Subset der WebApp fuer die Settings-Darstellung,",
        " * gescoped unter .bsc-settings-" + version +
        " (Dark-Mode: html.dark .bsc-settings-" + version + ").",
        " * Nicht von Hand editieren.",
        " */",
        "",
        "/* --- Variablen (Light) --- */",
        light_block.rstrip("\n"),
        "",
        "/* --- Variablen (Dark) --- */",
        dark_block.rstrip("\n"),
        "",
        "/* --- Fehlerbox (eigene Regel des Renderers) --- */",
        error_rule.rstrip("\n"),
        "",
        "/* --- Profilgraph-SVG (eigene Ergaenzung, in der WebApp per JS gestylt) --- */",
        svg_rule.rstrip("\n"),
        "",
        "/* --- CSS-Subset der WebApp (gescoped) --- */",
    ]
    body_lines = []
    for prelude, body in filtered:
        body_lines.append(f"{prelude}{{{rem_to_em(body)}}}")
    parts.append("\n\n".join(body_lines).rstrip("\n"))
    css_out = "\n".join(parts) + "\n"

    out_path = REPO_ROOT / "docs" / "css" / f"bsc-settings-{version}.css"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(css_out, encoding="utf-8")
    log(f"CSS extrahiert: {len(filtered)} Regeln (+Variablen/Fehlerbox) -> {out_path}")
    return out_path, len(filtered)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Sync der BSC-Settings-Daten und des WebApp-CSS in die Doku")
    parser.add_argument("--version", required=True,
                        help="Zielversion, z.B. v010 (Pflicht)")
    parser.add_argument("--firmware-path", default=str(REPO_ROOT.parent / "bsc_fw_insider"),
                        help="Pfad zur Firmware (Default: ../bsc_fw_insider)")
    parser.add_argument("--webapp-path", default=str(REPO_ROOT.parent / "bsc_fw_insider_webapp"),
                        help="Pfad zur WebApp (Default: ../bsc_fw_insider_webapp)")
    args = parser.parse_args(argv)

    version = args.version
    if not re.fullmatch(r"[A-Za-z0-9._-]+", version):
        sys.exit(f"FEHLER: Ungueltiger Versionsname '{version}'")
    firmware_path = Path(args.firmware_path)
    webapp_path = Path(args.webapp_path)
    version_dir = REPO_ROOT / "bsc_settings" / version

    log(f"=== Sync bsc_settings/{version} ===")
    log(f"Firmware: {firmware_path}")
    log(f"WebApp:   {webapp_path}")

    version_dir.mkdir(parents=True, exist_ok=True)
    sync_params(firmware_path, version_dir)
    generate_type_map(firmware_path, version_dir)
    generate_groupsizes(firmware_path, version_dir)
    extract_css(webapp_path, version, version_dir)
    log(f"=== Fertig. Daten unter {version_dir}, CSS unter docs/css/ ===")


if __name__ == "__main__":
    main()
