# -*- coding: utf-8 -*-
"""
MkDocs-Hook: BSC-Settings-Rendering (components/bsc).

Rendert ```bsc-settings```-Fenced-Code-Bloecke in Markdown-Seiten zu statischem
HTML im WebApp-Layout (listview/flex-container/separation-card) direkt aus den
Firmware-JSONs unter <root>/bsc_settings/<version>/params/.

Zielauswahl pro Block (mehrere Zeilen moeglich):
- section: <section_id>  – Top-Level-Eintrag mit section_id (String-Vergleich,
  numerische section_ids funktionieren)
- index: <n>             – N-ter Top-Level-Eintrag in page (1-basiert)
- label: <text>          – Top-Level-Eintrag mit exaktem Label
- name: <name>           – globaler Eintrag mit exaktem name

- on_config: traegt vorhandene docs/css/bsc-settings-v*.css als docs-relative
  Pfade in config.extra_css ein.
- on_page_markdown: ersetzt ```bsc-settings```-Bloeke VOR der
  Markdown-Konvertierung durch generiertes HTML.

Fehler (unbekannte Version/Datei/Sektion/Name, unbekannter Feldtyp, defektes
JSON, fehlende Combos) erzeugen immer BEIDES: eine MkDocs-Warnung im Log und
eine sichtbare Fehlerbox (.bsc-settings-error) im generierten Output.

Nur Python-Stdlib. Spezifikation: Konzept docs-dev_konzept_bsc-settings-renderer.md.
"""

import html as html_mod
import json
import logging
import os
import re
from pathlib import Path

log = logging.getLogger("mkdocs")

# ---------------------------------------------------------------------------
# Marker- und Zeilen-Parsing
# ---------------------------------------------------------------------------
FENCE_RE = re.compile(r"^```bsc-settings[ \t]*\r?\n(.*?)^```[ \t]*\r?$",
                      re.MULTILINE | re.DOTALL)
# Eingerueckte Fences (z.B. innerhalb von Tabs/Admonitions/Listen) werden
# ebenfalls verarbeitet: Das generierte HTML wird mit derselben Einrueckung
# eingefuegt, damit der Block Teil des umgebenden Markdown-Blocks bleibt.
# Der Schliessfence muss die GLEICHE Einrueckung wie der Oeffnungsfence haben.
INDENTED_FENCE_RE = re.compile(
    r"^([ \t]+)```bsc-settings[ \t]*\r?\n(.*?)^\1```[ \t]*\r?$",
    re.MULTILINE | re.DOTALL)
# Fallback-Erkennung: eingerueckter Oeffnungsfence, dessen Block nicht
# ersetzt werden konnte (z.B. fehlender Schliessfence mit gleicher Einrueckung).
INDENTED_FENCE_OPEN_RE = re.compile(r"^[ \t]+```bsc-settings[ \t]*\r?$",
                                    re.MULTILINE)
KEY_VALUE_RE = re.compile(r"^(version|file|section|name|index|label|profile)\s*:\s*(.+?)\s*$")

# HTML-Entities im JSON-Text erhalten (Labels enthalten z.B. &uuml;).
_ENTITY_RE = re.compile(
    r"&(amp|lt|gt|quot|#\d+|#x[0-9a-fA-F]+|[a-zA-Z][a-zA-Z0-9]{1,30});")

# Profilfaehige Feldtypen (P1/P2-Controls, vgl. buildProfileControlByExistingRenderer)
PROFILE_TYPES = {0, 2, 3, 4, 7, 9, 10, 14, 16, 17, 18}
# Typen, fuer die das Paar-Format NICHT angewendet wird (WebApp-Bedingung)
PROFILE_NO_PAIR_TYPES = {12, 13, 15, 20, 21, 23}

# JSON-Cache: {(version, filename): obj}
_JSON_CACHE = {}
_TYPE_MAP_CACHE = {}
_GROUPSIZES_CACHE = {}


def escape_text(value):
    """Escaped Text fuer HTML-Textkontext. Bereits vorhandene HTML-Entities
    (z.B. &uuml; in Labels) bleiben erhalten – wie in der WebApp, die Labels
    als innerHTML einsetzt."""
    s = html_mod.escape(str(value if value is not None else ""), quote=True)
    return _ENTITY_RE.sub(lambda m: "&" + m.group(1) + ";", s)


def escape_attr(value):
    """Escaped Wert fuer HTML-Attribute (keine Entity-Erhaltung)."""
    return html_mod.escape(str(value if value is not None else ""), quote=True)


def help_html(data):
    """Help-Text: escaped, aber <br>-Tags werden bewusst durchgelassen und
    echte Zeilenumbrueche wie in der WebApp (utils.textToHtml) zu <br>."""
    h = data.get("help")
    if h is None or str(h).strip() == "":
        return ""
    s = html_mod.escape(str(h), quote=True)
    s = re.sub(r"&lt;br\s*/?&gt;", "<br>", s)
    s = s.replace("\n", "<br>")
    return _ENTITY_RE.sub(lambda m: "&" + m.group(1) + ";", s)


def fmt_default(value):
    """Default-Wert als String; Listen/Dicts (z.B. Profil-Defaults) ergeben ''."""
    if value is None:
        return ""
    if isinstance(value, (list, dict)):
        return ""
    return str(value)


def scale_value(value, precision):
    """Skaliert einen Rohwert um Faktor 1/10^precision (fl1/fl2/fl3) und
    formatiert ihn wie die WebApp (JS Number->String: bis zu precision
    Nachkommastellen, ohne unnoetige Nullen)."""
    try:
        num = float(value) / (10 ** precision)
    except (TypeError, ValueError):
        return fmt_default(value)
    r = round(num, precision)
    s = f"{r:.{precision}f}".rstrip("0").rstrip(".")
    if s in ("", "-0"):
        s = "0"
    return s


class RenderError(Exception):
    """Fehler, der als sichtbare Fehlerbox + MkDocs-Warnung ausgegeben wird."""


# ---------------------------------------------------------------------------
# Daten laden
# ---------------------------------------------------------------------------
def load_json_file(root, version, filename):
    key = (version, filename)
    if key in _JSON_CACHE:
        return _JSON_CACHE[key]
    path = os.path.join(root, "bsc_settings", version, "params", filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise RenderError(f"Datei '{filename}' nicht gefunden (Version '{version}')")
    except json.JSONDecodeError as exc:
        raise RenderError(f"JSON defekt in '{filename}' (Version '{version}'): {exc}")
    _JSON_CACHE[key] = data
    return data


def load_type_map(root, version):
    if version in _TYPE_MAP_CACHE:
        return _TYPE_MAP_CACHE[version]
    path = os.path.join(root, "bsc_settings", version, "type_map.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            type_map = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        raise RenderError(f"type_map.json fuer Version '{version}' fehlt oder ist defekt: {exc}")
    _TYPE_MAP_CACHE[version] = type_map
    return type_map


def load_groupsizes(root, version):
    """Laedt bsc_settings/<version>/groupsizes.json (optional). Enthaelt
    numerische Defines (z.B. CNT_ALARMS=27) zur Aufloesung symbolischer
    groupsize-Namen."""
    if version in _GROUPSIZES_CACHE:
        return _GROUPSIZES_CACHE[version]
    path = os.path.join(root, "bsc_settings", version, "groupsizes.json")
    sizes = {}
    if os.path.isfile(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                sizes = json.load(f)
        except json.JSONDecodeError:
            sizes = {}
    _GROUPSIZES_CACHE[version] = sizes
    return sizes


def find_by_name(node, name):
    """Rekursive Suche (page/items/group) nach Eintrag mit exakt passendem name."""
    if isinstance(node, dict):
        if node.get("name") == name:
            yield node
        for value in node.values():
            yield from find_by_name(value, name)
    elif isinstance(node, list):
        for value in node:
            yield from find_by_name(value, name)


def find_section(data, section_id):
    """Sektion: Top-Level-Eintrag in page mit passender section_id
    (Vergleich als String, damit auch numerische section_ids funktionieren)."""
    page = data.get("page")
    if not isinstance(page, list):
        return None
    for entry in page:
        if isinstance(entry, dict) and str(entry.get("section_id")) == str(section_id):
            return entry
    return None


def find_page_entry(data, index=None, label=None):
    """Top-Level-Eintrag in page per 1-basiertem Index oder exaktem Label."""
    page = data.get("page")
    if not isinstance(page, list):
        return None
    if index is not None:
        if 1 <= index <= len(page):
            return page[index - 1]
        return None
    if label is not None:
        for entry in page:
            if isinstance(entry, dict) and str(entry.get("label")) == str(label):
                return entry
    return None


# ---------------------------------------------------------------------------
# Renderer
# ---------------------------------------------------------------------------
class RenderContext:
    def __init__(self, root, version, data, type_map, page_path,
                 profiles_enabled=True):
        self.root = root
        self.version = version
        self.data = data
        self.type_map = type_map
        self.groupsizes = load_groupsizes(root, version)
        self.page_path = page_path
        # Marker-Parameter 'profile: off' deaktiviert das P1/P2-Rendering
        # (enProfile-Felder werden dann wie normale Felder gerendert).
        self.profiles_enabled = profiles_enabled
        self._id_counter = 0

    def next_id(self, prefix):
        self._id_counter += 1
        return f"bsc-settings-{prefix}-{self._id_counter}"

    def warn(self, msg):
        log.warning(f"[bsc-settings] {msg} (Seite: {self.page_path})")

    def load_combo(self, ref):
        """Loest $ref gegen combos/<ref>.json (Fallback refs/<ref>.json) auf."""
        for sub in ("combos", "refs"):
            path = os.path.join(self.root, "bsc_settings", self.version,
                                "params", sub, ref + ".json")
            if not os.path.isfile(path):
                continue
            try:
                with open(path, "r", encoding="utf-8") as f:
                    combo = json.load(f)
            except json.JSONDecodeError as exc:
                raise RenderError(f"Combo '{ref}' defekt ({sub}/{ref}.json): {exc}")
            if isinstance(combo, list):
                return combo
            raise RenderError(f"Combo '{ref}' ist keine Liste ({sub}/{ref}.json)")
        return None

    def type_num(self, data):
        """Symbolischen/numerischen Typ in die Zahl aufloesen.
        Gibt None zurueck, wenn der Typ unbekannt ist."""
        t = data.get("type")
        if t is None:
            return None
        if isinstance(t, (int, float)):
            return int(t)
        if isinstance(t, str) and t in self.type_map:
            return int(self.type_map[t])
        return None

    def resolve_options(self, options):
        """Optionen-Liste mit aufgeloesten $ref-Eintraegen."""
        out = []
        for opt in options or []:
            if isinstance(opt, dict) and "$ref" in opt:
                ref = str(opt["$ref"])
                combo = self.load_combo(ref)
                if combo is None:
                    # Die MkDocs-Warnung erfolgt einmalig in render_entry/
                    # _render_row mit Namenskontext.
                    raise RenderError(f"Combo '{ref}' nicht gefunden")
                out.extend(combo)
            else:
                out.append(opt)
        return out

    # ---- Fehlerbox ----
    def error_box(self, msg, wrap_li=True):
        box = (f'<div class="bsc-settings-error">'
               f"BSC-Settings-Renderer: {escape_text(msg)}</div>")
        return f"<li>{box}</li>" if wrap_li else box

    # ---- Einstiegsfunktion fuer einen Eintrag ----
    def render_entry(self, data, is_group=False, in_row=False):
        if not isinstance(data, dict):
            return ""
        name = data.get("name")
        if data.get("ui_section_state"):
            return f"<!-- bsc-settings: ui_section_state uebersprungen ({escape_text(name)}) -->"
        if data.get("ui_hidden"):
            return f"<!-- bsc-settings: ui_hidden uebersprungen ({escape_text(name)}) -->"

        type_num = self.type_num(data)
        if type_num is None:
            t = data.get("type")
            msg = (f"Feldtyp '{t}' wird nicht unterstuetzt" if t is not None
                   else "Eintrag ohne Feldtyp wird nicht unterstuetzt")
            self.warn(f"{msg} ({name})")
            return self.error_box(msg)

        try:
            if (data.get("enProfile") is True and self.profiles_enabled
                    and (not is_group or in_row)):
                if type_num in PROFILE_NO_PAIR_TYPES:
                    return self._dispatch(data, type_num, is_group=is_group,
                                          in_row=in_row)
                if type_num == 11:
                    self.warn(f"Feldtyp 11 (HTML_INPUTMULTICHECK) wird nicht "
                              f"unterstuetzt ({name})")
                    return self.error_box(
                        "Feldtyp 11 (HTML_INPUTMULTICHECK) wird nicht unterstuetzt")
                if in_row:
                    return self._render_row_item_profiled(data)
                return self._render_profiled(data)
            return self._dispatch(data, type_num, is_group=is_group, in_row=in_row)
        except RenderError as exc:
            self.warn(f"{exc} ({name})")
            return self.error_box(str(exc))

    def _dispatch(self, data, type_num, is_group=False, in_row=False):
        if type_num == 0:
            return self._entry(data, self._control_text(data, fmt_default(data.get("default"))))
        if type_num == 2:
            # WebApp: buildEntry_text(..., "password") – mit Text-Attributen
            return self._entry(data, self._control_text(data, fmt_default(data.get("default")),
                                                        input_type="password"))
        if type_num == 3:
            return self._entry(data, self._control_number(data, fmt_default(data.get("default"))))
        if type_num == 4:
            return self._entry(data, self._control_float(data, fmt_default(data.get("default"))))
        if type_num == 7:
            # WebApp: buildEntry_text(..., "time") – mit Text-Attributen
            return self._entry(data, self._control_text(data, fmt_default(data.get("default")),
                                                        input_type="time"))
        if type_num == 9:
            return self._entry(data, self._control_select(data, fmt_default(data.get("default"))))
        if type_num == 10:
            # WebApp buildEntry_checkbox: dritte Flex-Zelle ist LEER (kein &nbsp;)
            return self._entry(data, self._control_checkbox(data, fmt_default(data.get("default"))),
                               unit_html="")
        if type_num == 11:
            self.warn(f"Feldtyp 11 (HTML_INPUTMULTICHECK) wird nicht unterstuetzt "
                      f"({data.get('name')})")
            return self.error_box(
                "Feldtyp 11 (HTML_INPUTMULTICHECK) wird nicht unterstuetzt")
        if type_num == 12:
            return self._render_option_group(data, collapsible=False)
        if type_num == 13:
            return self._render_separation(data)
        if type_num == 14:
            return self._entry(data, self._control_multicheck_collapsible(data))
        if type_num == 15:
            return self._render_option_group(data, collapsible=True)
        if type_num == 16:
            return self._entry(data, self._control_floatx(data, fmt_default(data.get("default")), 1))
        if type_num == 17:
            return self._entry(data, self._control_floatx(data, fmt_default(data.get("default")), 2))
        if type_num == 18:
            return self._entry(data, self._control_floatx(data, fmt_default(data.get("default")), 3))
        if type_num == 20:
            return self._render_profile(data)
        if type_num == 21:
            return self._render_row(data)
        if type_num == 22:
            label = data.get("label") or ""
            return f"<!-- bsc-settings: infoBox uebersprungen ({escape_text(label)}) -->"
        if type_num == 23:
            return self._render_collapsible(data)
        self.warn(f"Feldtyp {type_num} wird nicht unterstuetzt ({data.get('name')})")
        return self.error_box(f"Feldtyp {type_num} wird nicht unterstuetzt")

    # ---- Grundgeruest eines Eintrags ----
    def _entry(self, data, control_html, extra_class="", unit_html=None):
        label = escape_text(data.get("label") or "")
        if unit_html is None:
            unit = data.get("unit")
            unit_html = f"&nbsp;{escape_text(unit)}" if unit not in (None, "") else "&nbsp;"
        return (
            f"<li>\n"
            f"  <div class='flex-container{extra_class}'>\n"
            f"    <div class='flex-item'>{label}</div>\n"
            f"    <div class='flex-item'>{control_html}</div>\n"
            f"    <div class='flex-item'>{unit_html}</div>\n"
            f"  </div>\n"
            f"  <div class='sub-item'>{help_html(data)}</div>\n"
            f"</li>"
        )

    # ---- Einzelne Controls ----
    def _control_text(self, data, value, input_type="text"):
        attrs = f" value='{escape_attr(value)}'"
        if data.get("pattern") is not None:
            attrs += f" pattern='{escape_attr(data['pattern'])}'"
        if data.get("minlen") is not None:
            attrs += f" minlength='{escape_attr(data['minlen'])}'"
        if data.get("maxlen") is not None:
            attrs += f" data-max-bytes='{escape_attr(data['maxlen'])}'"
        return f"<input type='{input_type}'{attrs}>"

    def _control_number(self, data, value):
        attrs = ""
        if data.get("min") is not None:
            attrs += f" min='{escape_attr(data['min'])}'"
        if data.get("max") is not None:
            attrs += f" max='{escape_attr(data['max'])}'"
        return f"<input type='number'{attrs} value='{escape_attr(value)}'>"

    def _control_float(self, data, value):
        # Typ 4 (HTML_INPUTFLOAT): wie fl1, aber ohne fl1-Klasse,
        # step aus data.step (Default 0.1) – Entscheidung F3
        step = data.get("step")
        if step in (None, "", 0):
            step = 0.1
        attrs = ""
        if data.get("min") is not None:
            attrs += f" min='{escape_attr(data['min'])}'"
        if data.get("max") is not None:
            attrs += f" max='{escape_attr(data['max'])}'"
        return (f"<input type='number' step='{escape_attr(step)}'{attrs} "
                f"value='{escape_attr(scale_value(value, 1))}'>")

    def _control_floatx(self, data, value, precision):
        step = {1: "0.1", 2: "0.01", 3: "0.001"}[precision]
        attrs = ""
        if data.get("min") is not None:
            attrs += f" min='{escape_attr(data['min'])}'"
        if data.get("max") is not None:
            attrs += f" max='{escape_attr(data['max'])}'"
        return (f"<input type='number' step='{step}'{attrs} "
                f"value='{escape_attr(scale_value(value, precision))}' class='fl{precision}'>")

    def _control_checkbox(self, data, value):
        checked = " checked" if str(value) == "1" else ""
        return f"<input type='checkbox'{checked}>"

    def _control_select(self, data, value):
        options = self.resolve_options(data.get("options"))
        default_str = fmt_default(value)
        parts = ["<select>"]
        for i, opt in enumerate(options):
            if not isinstance(opt, dict):
                continue
            v = opt.get("v")
            v = i if v is None else v
            l = opt.get("l")
            if l is None or str(l).strip() == "":
                l = v
            selected = " selected" if str(v) == default_str else ""
            parts.append(f"<option value='{escape_attr(v)}'{selected}>{escape_text(l)}</option>")
        parts.append("</select>")
        return "".join(parts)

    def _control_multicheck_collapsible(self, data):
        """WebApp-Referenz: buildEntry_multiCheckCollapsible + renderMultiCheckSummary.
        Der Toggle ist initial immer zugeklappt (die WebApp setzt kein checked);
        die selected-summary zeigt Tag-Pills der per Default gesetzten Optionen
        und bleibt LEER, wenn keine Option gesetzt ist (keine Zaehlung)."""
        options = self.resolve_options(data.get("options"))
        default_str = fmt_default(data.get("default"))
        default_bits = int(default_str) if default_str.lstrip("-").isdigit() else 0

        parts = []
        tags = []
        for i, opt in enumerate(options):
            if not isinstance(opt, dict):
                continue
            v = opt.get("v")
            v = i if v is None else v
            l = opt.get("l")
            if l is None or str(l).strip() == "":
                l = v
            bit = int(v) if str(v).isdigit() and 0 <= int(v) <= 31 else i
            checked = bool(default_bits >= 0 and ((default_bits >> bit) & 1))
            checked_attr = " checked" if checked else ""
            parts.append(
                f"<label><input type='checkbox' value='{escape_attr(v)}'{checked_attr}>"
                f"<span>{escape_text(l)}</span></label>")
            if checked:
                tags.append(f"<span class='tag'>{escape_text(l)}</span>")

        toggle_id = self.next_id("mc")
        return (
            f"<input id='{toggle_id}' class='toggle' type='checkbox'>"
            f"<label for='{toggle_id}' class='lbl-toggle'>"
            f"<span class='selected-summary'>{''.join(tags)}</span></label>"
            f"<div class='collapsible-content'><div class='content-inner'>"
            f"<fieldset style='text-align:left;'>{''.join(parts)}</fieldset>"
            f"</div></div>"
        )

    # ---- Typ 12/15 Optiongruppen ----
    def _group_count(self, data):
        groupsize = data.get("groupsize")
        try:
            n = int(groupsize)
        except (TypeError, ValueError):
            # Symbolischer groupsize-Name (z.B. CNT_ALARMS): ueber die
            # generierte groupsizes.json aufloesen. Fallback: Anzahl der
            # group-Felder (nur Notloesung – deckt keine Optiongruppen ab).
            n = self.groupsizes.get(str(groupsize)) if isinstance(groupsize, str) else None
            if n is None:
                self.warn(f"groupsize '{groupsize}' nicht aufloesbar "
                          f"(fehlt in groupsizes.json) – Fallback: Feldanzahl")
                group = data.get("group")
                n = len(group) if isinstance(group, list) else 1
        return max(int(n), 1)

    def _render_option_group(self, data, collapsible=False):
        n = self._group_count(data)
        label_entry = data.get("label_entry") or "Eintrag"
        try:
            label_offset = int(data.get("label_offset") or 0)
        except (TypeError, ValueError):
            label_offset = 0
        # WebApp-Formel: Gruppennummer = idx + label_offset (label_offset > 0).
        # Ohne label_offset bleibt die Nummerierung 1-basiert (Konzept 5.3).
        if label_offset <= 0:
            label_offset = 1
        group = data.get("group")
        if not isinstance(group, list):
            group = []

        blocks = []
        for idx in range(n):
            inner = ""
            for item in group:
                inner += self.render_entry(item, is_group=True)
            blocks.append(
                f"<div class='group-block'>"
                f"<li class='subHead' style='margin-top:10px'>"
                f"<b>{escape_text(label_entry)} {idx + label_offset}</b></li>"
                f"{inner}</div>")
        body = "".join(blocks)

        if collapsible:
            label = escape_text(data.get("label") or "")
            return (
                f"<li class='settings-collapsible-block'>"
                f"<details><summary><b>{label}</b></summary>{body}</details>"
                f"<div class='sub-item'>{help_html(data)}</div></li>"
            )
        label = data.get("label")
        head = ""
        if label:
            head = (f"<li class='subHead'><div><b>{escape_text(label)}</b></div>"
                    f"<div class='sub-item'>{help_html(data)}</div></li>")
        return head + body

    # ---- Typ 13 Sektion ----
    def _render_separation(self, data):
        items = data.get("items")
        if not isinstance(items, list) or len(items) == 0:
            return (f"<li class='head'><div><b>{escape_text(data.get('label') or '')}</b></div>"
                    f"<div class='sub-item'>{help_html(data)}</div></li>")
        label = data.get("label") or ""
        inner = "".join(self.render_entry(item) for item in items)
        headline = ""
        if str(label).strip():
            headline = (
                f"<div class='separation-card-title'>"
                f"<button type='button' class='section-toggle-btn' aria-expanded='true'>"
                f"<span class='section-toggle-title'><b>{escape_text(label)}</b></span>"
                f"<span class='section-toggle-icon'>▾</span></button></div>"
                f"<div class='sub-item'>{help_html(data)}</div>"
            )
        return (f"<li class='separation-card'>{headline}"
                f"<ul class='separation-list'>{inner}</ul></li>")

    # ---- Typ 21 Row ----
    def _row_span(self, layout, index, default_span):
        try:
            span = int(layout[index])
        except (IndexError, TypeError, ValueError):
            return default_span
        return span if 1 <= span <= 12 else default_span

    def _render_row(self, data):
        items = data.get("items")
        if not isinstance(items, list) or len(items) == 0:
            return ""
        row_label = escape_text(data.get("label") or "")
        layout = data.get("layout")
        if isinstance(layout, dict):
            layout = layout.get("desktop")
        if not isinstance(layout, list):
            layout = []
        default_span = max(1, 12 // len(items))

        cells = []
        col_start = 1
        for i, item in enumerate(items):
            span = self._row_span(layout, i, default_span)
            if col_start > 12:
                col_start = 1
            base = f"--col-start:{col_start};--span-d:{span};--row-idx:{i};"
            unit = escape_text(item.get("unit") or "") if item.get("unit") else "&nbsp;"
            label = escape_text(item.get("label") or "")
            try:
                if item.get("enProfile") is True and self.profiles_enabled:
                    cells.append(self._render_row_item_profiled(item, base, label, unit))
                else:
                    control = self._control_for_item(item)
                    cells.append(
                        f"<div class='settings-row-label-cell' style='{base}'>"
                        f"<div class='row-item-label'>{label}</div></div>"
                        f"<div class='settings-row-value-cell' style='{base}'>"
                        f"<div class='row-item-value-wrap'>"
                        f"<div class='row-item-value'>{control}</div>"
                        f"<div class='row-item-unit'>{unit}</div></div></div>")
            except RenderError as exc:
                self.warn(f"{exc} ({item.get('name')})")
                cells.append(f"<div class='settings-row-value-cell' style='{base}'>"
                             f"{self.error_box(str(exc), wrap_li=False)}</div>")
            col_start += span

        return (
            f"<li class='settings-row'>"
            f"<div class='flex-container settings-row-wrap'>"
            f"<div class='flex-item'>{row_label}</div>"
            f"<div class='flex-item'>"
            f"<div class='settings-row-grid settings-row-grid-paired'>{''.join(cells)}</div>"
            f"</div>"
            f"<div class='flex-item'>&nbsp;</div></div>"
            f"<div class='sub-item'>{help_html(data)}</div></li>"
        )

    def _control_for_item(self, item):
        """Control eines Row-Items (ohne Profil), inkl. Fehlerbehandlung."""
        type_num = self.type_num(item)
        if type_num is None:
            raise RenderError(f"Feldtyp '{item.get('type')}' wird nicht unterstuetzt")
        if type_num == 11:
            raise RenderError("Feldtyp 11 (HTML_INPUTMULTICHECK) wird nicht unterstuetzt")
        default = fmt_default(item.get("default"))
        if type_num == 0:
            return self._control_text(item, default)
        if type_num == 2:
            return self._control_text(item, default, input_type="password")
        if type_num == 3:
            return self._control_number(item, default)
        if type_num == 4:
            return self._control_float(item, default)
        if type_num == 7:
            return self._control_text(item, default, input_type="time")
        if type_num == 9:
            return self._control_select(item, default)
        if type_num == 10:
            return self._control_checkbox(item, default)
        if type_num == 14:
            return self._control_multicheck_collapsible(item)
        if type_num == 16:
            return self._control_floatx(item, default, 1)
        if type_num == 17:
            return self._control_floatx(item, default, 2)
        if type_num == 18:
            return self._control_floatx(item, default, 3)
        raise RenderError(f"Feldtyp {type_num} wird nicht unterstuetzt")

    def _render_row_item_profiled(self, item, base=None, label=None, unit=None):
        """P1/P2-Zellen fuer enProfile-Items innerhalb einer Typ-21-Row."""
        if base is None or label is None:
            # Einstieg ueber render_entry mit in_row=True
            base = "--row-idx:0;"
            label = escape_text(item.get("label") or "")
            unit = escape_text(item.get("unit") or "") if item.get("unit") else "&nbsp;"
        p1, p2 = self._profile_defaults(item.get("default"))
        c1 = self._profile_control(item, p1)
        c2 = self._profile_control(item, p2)
        cells = [f"<div class='settings-row-label-cell' style='{base}'>"
                 f"<div class='row-item-label'>{label}</div></div>"]
        for slot_class, c in (("profile-slot-row-p1", c1), ("profile-slot-row-p2", c2)):
            cells.append(
                f"<div class='settings-row-value-cell settings-row-value-cell-profile "
                f"settings-row-value-cell-profile-{slot_class[-2:]}' style='{base}'>"
                f"<div class='row-item-value-wrap row-item-value-wrap-profile'>"
                f"<div class='profile-slot profile-slot-row {slot_class}'>"
                f"<span class='profile-slot-label'>{slot_class[-2:].upper()}</span>{c}</div>"
                f"<div class='row-item-unit'>{unit}</div></div></div>")
        return "".join(cells)

    # ---- P1/P2-Profil-Controls ----
    @staticmethod
    def _profile_defaults(default):
        if isinstance(default, list):
            p1 = str(default[0]) if len(default) > 0 and default[0] is not None else "0"
            p2 = str(default[1]) if len(default) > 1 and default[1] is not None else p1
            return p1, p2
        if default is not None:
            return str(default), str(default)
        return "0", "0"

    def _profile_control(self, data, value):
        """Control fuer einen P1-/P2-Slot (profilfaehige Typen)."""
        type_num = self.type_num(data)
        if type_num is None:
            raise RenderError(f"Feldtyp '{data.get('type')}' wird nicht unterstuetzt")
        if type_num == 11:
            raise RenderError("Feldtyp 11 (HTML_INPUTMULTICHECK) wird nicht unterstuetzt")
        if type_num == 0:
            return self._control_text(data, value)
        if type_num == 2:
            return self._control_text(data, value, input_type="password")
        if type_num == 3:
            return self._control_number(data, value)
        if type_num == 4:
            return self._control_float(data, value)
        if type_num == 7:
            return self._control_text(data, value, input_type="time")
        if type_num == 9:
            return self._control_select(data, value)
        if type_num == 10:
            return self._control_checkbox(data, value)
        if type_num == 14:
            return self._control_multicheck_collapsible(data)
        if type_num == 16:
            return self._control_floatx(data, value, 1)
        if type_num == 17:
            return self._control_floatx(data, value, 2)
        if type_num == 18:
            return self._control_floatx(data, value, 3)
        raise RenderError(f"Feldtyp {type_num} ist nicht profilfaehig")

    def _render_profiled(self, data):
        p1, p2 = self._profile_defaults(data.get("default"))
        c1 = self._profile_control(data, p1)
        c2 = self._profile_control(data, p2)
        label = escape_text(data.get("label") or "")
        unit = data.get("unit")
        unit_html = f"&nbsp;{escape_text(unit)}" if unit not in (None, "") else "&nbsp;"
        return (
            f"<li>\n"
            f"  <div class='flex-container profile-entry-flex'>\n"
            f"    <div class='flex-item'>{label}</div>\n"
            f"    <div class='flex-item'>\n"
            f"      <div class='profile-pair'>\n"
            f"        <div class='profile-slot'><span class='profile-slot-label'>P1</span>{c1}</div>\n"
            f"        <div class='profile-slot'><span class='profile-slot-label'>P2</span>{c2}</div>\n"
            f"      </div>\n"
            f"    </div>\n"
            f"    <div class='flex-item'>{unit_html}</div>\n"
            f"  </div>\n"
            f"  <div class='sub-item'>{help_html(data)}</div>\n"
            f"</li>"
        )

    # ---- Typ 23 Collapsible ----
    def _render_collapsible(self, data):
        items = data.get("items")
        if not isinstance(items, list):
            items = []
        open_attr = " open" if data.get("default_open") is True else ""
        label = escape_text(data.get("label") or "")
        inner = "".join(self.render_entry(item) for item in items)
        return (
            f"<li class='settings-collapsible-block'>"
            f"<details{open_attr}><summary><b>{label}</b></summary>"
            f"<ul class='settings-collapsible-list'>{inner}</ul></details>"
            f"<div class='sub-item'>{help_html(data)}</div></li>"
        )

    # ---- Typ 20 Profilgraph (statisches SVG) ----
    @staticmethod
    def _precision_from_type(type_num):
        if type_num == 16:
            return 1
        if type_num == 17:
            return 2
        if type_num == 18:
            return 3
        return 0

    def _render_profile(self, data):
        group = data.get("group")
        if not isinstance(group, list) or len(group) < 2:
            raise RenderError("Profilgraph ohne gueltige group-Eintraege")
        x_spec = group[0] if isinstance(group[0], dict) else {}
        y_spec = group[1] if isinstance(group[1], dict) else {}

        x_defaults = x_spec.get("default") if isinstance(x_spec.get("default"), list) else []
        y_defaults = y_spec.get("default") if isinstance(y_spec.get("default"), list) else []
        n = min(len(x_defaults), len(y_defaults))
        if n == 0:
            raise RenderError("Profilgraph ohne Default-Punkte")

        x_p = self._precision_from_type(self.type_num(x_spec) or 0)
        y_p = self._precision_from_type(self.type_num(y_spec) or 0)
        try:
            pts = [(float(x_defaults[i]) / (10 ** x_p),
                    float(y_defaults[i]) / (10 ** y_p)) for i in range(n)]
        except (TypeError, ValueError):
            raise RenderError("Profilgraph: Default-Werte sind nicht numerisch")

        x_unit = x_spec.get("unit") or ""
        y_unit = y_spec.get("unit") or ""

        def _axis_min_max(spec, fallback_max):
            try:
                lo = float(spec.get("min") if spec.get("min") is not None else 0)
            except (TypeError, ValueError):
                lo = 0.0
            try:
                hi = float(spec.get("max") if spec.get("max") is not None else fallback_max)
            except (TypeError, ValueError):
                hi = fallback_max
            if hi <= lo:
                hi = lo + 1.0
            return lo, hi

        x_min, x_max = _axis_min_max(x_spec, 60)
        y_min, y_max = _axis_min_max(y_spec, 1)

        W, H = 800, 320
        M = {"l": 48, "t": 12, "r": 16, "b": 28}
        inner_w = W - M["l"] - M["r"]
        inner_h = H - M["t"] - M["b"]

        def x2px(v):
            return M["l"] + (v - x_min) / (x_max - x_min) * inner_w

        def y2px(v):
            return M["t"] + (1 - (v - y_min) / (y_max - y_min)) * inner_h

        svg = []
        x_ticks, y_ticks = 6, 5
        for i in range(x_ticks + 1):
            t = x_min + i * (x_max - x_min) / x_ticks
            px = round(x2px(t), 2)
            svg.append(f"<line x1='{px}' y1='{M['t']}' x2='{px}' y2='{H - M['b']}' "
                       f"stroke='var(--pf-grid)'/>")
            label = f"{t:.{x_p}f}".rstrip("0").rstrip(".")
            svg.append(f"<text x='{px}' y='{H - 6}' text-anchor='middle' "
                       f"font-size='12' fill='var(--pf-text)'>{label}"
                       f"{escape_text(x_unit)}</text>")
        for i in range(y_ticks + 1):
            c = y_min + i * (y_max - y_min) / y_ticks
            py = round(y2px(c), 2)
            svg.append(f"<line x1='{M['l']}' y1='{py}' x2='{W - M['r']}' y2='{py}' "
                       f"stroke='var(--pf-grid)'/>")
            label = f"{c:.{y_p}f}".rstrip("0").rstrip(".")
            svg.append(f"<text x='{M['l'] - 8}' y='{py + 4}' text-anchor='end' "
                       f"font-size='12' fill='var(--pf-text)'>{label}</text>")
        # Achsen
        svg.append(f"<line x1='{M['l']}' y1='{H - M['b']}' x2='{W - M['r']}' "
                   f"y2='{H - M['b']}' stroke='var(--pf-grid)'/>")
        svg.append(f"<line x1='{M['l']}' y1='{M['t']}' x2='{M['l']}' "
                   f"y2='{H - M['b']}' stroke='var(--pf-grid)'/>")
        # Y-Achsenbeschriftung mit Unit
        if y_unit:
            svg.append(f"<text x='6' y='{M['t'] + 12}' font-size='11' "
                       f"fill='var(--pf-text)'>{escape_text(y_unit)}</text>")

        # Punktwolke (sortiert nach X, wie WebApp)
        sorted_pts = sorted(pts, key=lambda p: p[0])
        points_str = " ".join(f"{round(x2px(px), 2)},{round(y2px(py), 2)}"
                              for px, py in sorted_pts)
        svg.append(f"<polyline fill='none' stroke='var(--pf-curve)' stroke-width='2' "
                   f"points='{points_str}'/>")
        for px, py in sorted_pts:
            svg.append(f"<circle cx='{round(x2px(px), 2)}' cy='{round(y2px(py), 2)}' "
                       f"r='4' fill='var(--pf-point-fill)' "
                       f"stroke='var(--pf-point-stroke)' stroke-width='2'/>")

        # X/Y-Wertetabelle
        rows = []
        for i in range(n):
            xv = f"{pts[i][0]:.{x_p}f}".rstrip("0").rstrip(".")
            yv = f"{pts[i][1]:.{y_p}f}".rstrip("0").rstrip(".")
            rows.append(f"<tr><td>{xv}</td><td>{yv}</td></tr>")
        x_head = f"X ({escape_text(x_unit)})" if x_unit else "X"
        y_head = f"Y ({escape_text(y_unit)})" if y_unit else "Y"
        table = (f"<table class='points-table'><thead><tr><th>{x_head}</th>"
                 f"<th>{y_head}</th></tr></thead><tbody>{''.join(rows)}</tbody></table>")

        label = escape_text(data.get("label") or "")
        return (
            f"<li>\n"
            f"  <div class='profile-label'><b>{label}</b></div>\n"
            f"  <div class='profile-control'>\n"
            f"    <div class='chart-wrap'>\n"
            f"      <svg class='profile-svg' viewBox='0 0 800 320' "
            f"preserveAspectRatio='xMidYMid meet'>{''.join(svg)}</svg>\n"
            f"    </div>\n"
            f"    {table}\n"
            f"  </div>\n"
            f"  <div class='sub-item'>{help_html(data)}</div>\n"
            f"</li>"
        )


# ---------------------------------------------------------------------------
# Marker-Block-Verarbeitung
# ---------------------------------------------------------------------------
def parse_marker_body(body):
    """Parst Marker-Zeilen. Gibt (version, filename, entries, errors,
    profile_value) zurueck.
    entries: Liste von ('section', id), ('name', name), ('index', n) bzw.
    ('label', label).
    profile_value: 'off' deaktiviert das P1/P2-Profiling (Default: None = an)."""
    version = None
    filename = None
    entries = []
    errors = []
    profile_value = None
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        m = KEY_VALUE_RE.match(line)
        if not m:
            errors.append(f"Unbekannte Marker-Zeile: '{line}'")
            continue
        key, value = m.group(1), m.group(2).strip()
        if key == "version":
            version = value
        elif key == "file":
            filename = value
        elif key == "section":
            entries.append(("section", value))
        elif key == "name":
            entries.append(("name", value))
        elif key == "index":
            try:
                entries.append(("index", int(value)))
            except ValueError:
                errors.append(f"index:-Wert ist keine Zahl: '{value}'")
        elif key == "label":
            entries.append(("label", value))
        elif key == "profile":
            profile_value = value.lower()
            if profile_value not in ("on", "off"):
                errors.append(f"Unbekannter profile:-Wert '{value}' "
                              f"(erlaubt: on, off; Default: on)")
                profile_value = None
    return version, filename, entries, errors, profile_value


def replace_fence(match, root, page_path):
    """Ersetzt einen ```bsc-settings```-Block in Spalte 0. Das Ergebnis endet
    immer mit einem Zeilenumbruch: Python-Markdown beendet einen HTML-Block
    erst bei einer Leerzeile – ohne sie wuerde direkt folgendes Markdown
    (z.B. eine Liste) Teil des HTML-Blocks werden und nicht mehr geparst."""
    html = _replace_fence_body(match.group(1), root, page_path)
    if not html.endswith("\n"):
        html += "\n"
    return html


def replace_indented_fence(match, root, page_path):
    """Ersetzt einen EINGERUECKTEN ```bsc-settings```-Block (z.B. innerhalb
    von Tabs/Admonitions/Listen). Das generierte HTML wird mit derselben
    Einrueckung eingefuegt, damit der Block Teil des umgebenden Markdown-
    Blocks bleibt."""
    indent = match.group(1)
    html = _replace_fence_body(match.group(2), root, page_path)
    if not html.endswith("\n"):
        html += "\n"
    lines = []
    for line in html.rstrip("\n").split("\n"):
        lines.append(indent + line if line.strip() else "")
    return "\n".join(lines) + "\n"


def _replace_fence_body(body, root, page_path):
    version, filename, entries, errors, profile_value = parse_marker_body(body)
    if errors:
        for err in errors:
            log.warning(f"[bsc-settings] {err} (Seite: {page_path})")
    if not version:
        log.warning(f"[bsc-settings] Marker ohne version: (Seite: {page_path})")
        return ('<div class="bsc-settings-error">BSC-Settings-Renderer: '
                'Marker ohne version:-Angabe</div>')
    if not filename:
        log.warning(f"[bsc-settings] Marker ohne file: (Version {version}, "
                    f"Seite: {page_path})")
        return ('<div class="bsc-settings-error">BSC-Settings-Renderer: '
                'Marker ohne file:-Angabe</div>')

    if not re.fullmatch(r"[A-Za-z0-9._-]+", version):
        log.warning(f"[bsc-settings] Unbekannte Version '{version}' (Seite: {page_path})")
        return (f'<div class="bsc-settings-error">BSC-Settings-Renderer: '
                f"Unbekannte Version '{escape_text(version)}'</div>")
    if not os.path.isdir(os.path.join(root, "bsc_settings", version)):
        log.warning(f"[bsc-settings] Unbekannte Version '{version}' (Seite: {page_path})")
        return (f'<div class="bsc-settings-error">BSC-Settings-Renderer: '
                f"Unbekannte Version '{escape_text(version)}'</div>")

    # Pfad-Traversal verhindern: nur Dateiname zulassen
    safe_file = os.path.basename(filename)
    if safe_file != filename:
        log.warning(f"[bsc-settings] Unzulaessiger Dateiname '{filename}' "
                    f"(Seite: {page_path})")
        return (f'<div class="bsc-settings-error">BSC-Settings-Renderer: '
                f"Unzulaessiger Dateiname '{escape_text(filename)}'</div>")

    try:
        data = load_json_file(root, version, safe_file)
        type_map = load_type_map(root, version)
    except RenderError as exc:
        log.warning(f"[bsc-settings] {exc} (Seite: {page_path})")
        return f'<div class="bsc-settings-error">BSC-Settings-Renderer: {escape_text(str(exc))}</div>'

    profiles_enabled = profile_value != "off"
    ctx = RenderContext(root, version, data, type_map, page_path,
                        profiles_enabled=profiles_enabled)

    html_parts = []
    for kind, value in entries:
        if kind == "section":
            section = find_section(data, value)
            if section is None:
                log.warning(f"[bsc-settings] section_id '{value}' nicht gefunden "
                            f"in {safe_file} ({version}) (Seite: {page_path})")
                html_parts.append(
                    f"<li><div class=\"bsc-settings-error\">BSC-Settings-Renderer: "
                    f"section_id '{escape_text(value)}' nicht gefunden</div></li>")
                continue
            try:
                html_parts.append(ctx.render_entry(section))
            except RenderError as exc:
                log.warning(f"[bsc-settings] {exc} ({value}) (Seite: {page_path})")
                html_parts.append(
                    f"<li><div class=\"bsc-settings-error\">BSC-Settings-Renderer: "
                    f"{escape_text(str(exc))}</div></li>")
        elif kind in ("index", "label"):
            section = find_page_entry(data, index=value if kind == "index" else None,
                                      label=value if kind == "label" else None)
            if section is None:
                log.warning(f"[bsc-settings] {kind} '{value}' nicht gefunden "
                            f"in {safe_file} ({version}) (Seite: {page_path})")
                html_parts.append(
                    f"<li><div class=\"bsc-settings-error\">BSC-Settings-Renderer: "
                    f"{kind} '{escape_text(value)}' nicht gefunden</div></li>")
                continue
            try:
                html_parts.append(ctx.render_entry(section))
            except RenderError as exc:
                log.warning(f"[bsc-settings] {exc} ({kind} {value}) (Seite: {page_path})")
                html_parts.append(
                    f"<li><div class=\"bsc-settings-error\">BSC-Settings-Renderer: "
                    f"{escape_text(str(exc))}</div></li>")
        else:
            found = next(find_by_name(data, value), None)
            if found is None:
                log.warning(f"[bsc-settings] name '{value}' nicht gefunden "
                            f"in {safe_file} ({version}) (Seite: {page_path})")
                html_parts.append(
                    f"<li><div class=\"bsc-settings-error\">BSC-Settings-Renderer: "
                    f"name '{escape_text(value)}' nicht gefunden</div></li>")
                continue
            html_parts.append(ctx.render_entry(found))

    return (f"<div class=\"bsc-settings-{escape_attr(version)}\">\n"
            f"  <div class=\"listview\">\n"
            f"    <ul>\n"
            f"{''.join(html_parts)}"
            f"    </ul>\n"
            f"  </div>\n"
            f"</div>")


# ---------------------------------------------------------------------------
# MkDocs-Hook-Funktionen
# ---------------------------------------------------------------------------
def on_config(config):
    """Traegt vorhandene docs/css/bsc-settings-v*.css als docs-relative
    Pfade in config.extra_css ein (sortiert, deterministisch)."""
    config_root = os.path.dirname(config.config_file_path)
    docs_dir = config.get("docs_dir") or "docs"
    if not os.path.isabs(docs_dir):
        docs_dir = os.path.join(config_root, docs_dir)
    css_dir = os.path.join(docs_dir, "css")
    existing = set(config.get("extra_css") or [])
    if os.path.isdir(css_dir):
        for css_file in sorted(os.listdir(css_dir)):
            if re.fullmatch(r"bsc-settings-v[A-Za-z0-9._-]+\.css", css_file):
                rel = os.path.join("css", css_file)
                if rel not in existing:
                    config["extra_css"].append(rel)
    return config


def on_page_markdown(markdown, page, config, files):
    """Ersetzt ```bsc-settings```-Bloeke durch gerendertes HTML.

    Sowohl Bloeke in Spalte 0 als auch eingerueckte Bloeke (in Tabs,
    Admonitions oder Listen) werden ersetzt; bei eingerueckten Bloeken wird
    die Einrueckung im generierten HTML beibehalten. Eingerueckte Bloeke,
    die nicht ersetzt werden konnten (z.B. fehlender Schliessfence mit
    gleicher Einrueckung), ergeben eine MkDocs-Warnung mit Zeilennummer und
    bleiben als Codeblock sichtbar."""
    root = os.path.dirname(config.config_file_path)
    page_path = getattr(page, "file", None)
    page_path = getattr(page_path, "src_path", None) or getattr(page, "src_path", "?")

    markdown = FENCE_RE.sub(lambda m: replace_fence(m, root, page_path), markdown)
    markdown = INDENTED_FENCE_RE.sub(
        lambda m: replace_indented_fence(m, root, page_path), markdown)

    for m in INDENTED_FENCE_OPEN_RE.finditer(markdown):
        line_no = markdown[:m.start()].count("\n") + 1
        log.warning(
            f"[bsc-settings] Eingerueckter ```bsc-settings```-Block wird NICHT "
            f"verarbeitet (Zeile {line_no}, Seite: {page_path}) – fehlender "
            f"Schliessfence mit gleicher Einrueckung?")

    return markdown
