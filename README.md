# Battery Safety Controller

[Hier](https://bsc-org.github.io/bsc) gehts zur Dokumentation des Battery Safety Controllers.

## BSC-Settings-Rendering (Marker-System)

Settings-Darstellungen können seit Kurzem direkt aus den Firmware-JSONs gerendert
werden, statt sie als manuelles HTML zu pflegen. Dafür in einer Markdown-Seite
einen Fenced-Code-Block mit Sprache `bsc-settings` verwenden:

````markdown
```bsc-settings
version: v010
file: inverterCharge.json
name: ID_PARAM_INVERTER_AUTOBALANCE_ENABLE
section: UI_SECT_INVERTERCHARGE_AUTOBALANCE
name: ID_PARAM_INVERTER_AUTOBALANCE_NACHLAUFZEIT
```
````

- `version:` Versionsordner unter `bsc_settings/` (z.B. `v010`)
- `file:` JSON-Datei unter `bsc_settings/<version>/params/`
- `section:` rendert eine komplette Sektion (`section_id`), `name:` einen einzelnen Parameter (globale Namenssuche), `index:` den N-ten Top-Level-Eintrag (1-basiert), `label:` den Top-Level-Eintrag mit exaktem Label; Reihenfolge der Zeilen bestimmt die Anzeige
- `profile: off` (optional, Default `on`) rendert `enProfile`-Felder ohne P1/P2-Profile als normale Felder
- `groups: n` (optional, Default `2`) begrenzt die Anzahl der gerenderten
  Instanzen von Optiongruppen (Typ 12/15, `groupsize`-Iteration) auf die
  ersten n Instanzen – es werden bewusst nie alle Instanzen dargestellt,
  sondern nur Beispiele. Sollen mehr Instanzen erscheinen, `groups: n`
  entsprechend erhöhen.
- Fehler (unbekannte Version/Datei/Sektion/Name, nicht unterstützte Feldtypen) erzeugen eine MkDocs-Warnung und eine sichtbare rote Fehlerbox

**Einrückung:** Der Fenced-Code-Block kann in Spalte 0 stehen oder – z.B. innerhalb
von Tabs (`===`-Inhalt), Admonitions oder Listen – **eingerückt** sein. Die
Einrückung des generierten HTML-Blocks entspricht dann der Fence-Einrückung, damit
der Block Teil des umgebenden Markdown-Blocks bleibt. Öffnungs- und Schließfence
müssen dabei **dieselbe** Einrückung haben. Eingerückte Blöcke ohne passenden
Schließfence werden nicht verarbeitet (bleiben als Codeblock sichtbar) und erzeugen
eine MkDocs-Warnung mit Zeilennummer.

### Daten synchronisieren

Die Versionsdaten unter `bsc_settings/<version>/` und das CSS unter
`docs/css/bsc-settings-<version>.css` werden mit dem Sync-Script aus der
Firmware bzw. der WebApp erzeugt:

```bash
python3 scripts/sync_bsc_settings.py --version v010
```

Das Script kopiert `params/` komplett (inkl. `combos/`, `refs/`), generiert
`type_map.json` aus `WebSettings.h`, `groupsizes.json` (numerische Defines
aus `defines.h`/`WebSettings.h`, zur Auflösung symbolischer `groupsize`-Namen)
und extrahiert das gescopte CSS-Subset aus `css/style.css` der WebApp. Bei
Firmware-/WebApp-Änderungen erneut ausführen und das Ergebnis committen. Die
Daten liegen bewusst außerhalb von `docs/` und werden nicht Teil von `site/`.

### Dark Mode

`docs/js/theme-sync.js` synchronisiert das Material-Farbschema
(`data-md-color-scheme`) mit der `.dark`-Klasse am `<html>`-Element, sodass die
Dark-Overrides des WebApp-CSS (unter `html.dark .bsc-settings-<version>`)
funktionieren. Umgeschaltet wird über das Paletten-Toggle-Icon.

Bestehende `bsc_content`-HTML-Blöcke bleiben unverändert funktionsfähig. Stand
der Migration (2026-08-20): Alle Settings-Seiten sind auf Marker migriert; der
einzige verbliebene `bsc_content`-Block ist der bewusst unveränderte Alt-Tab
„Version < V0.10.0“ in `docs/settings_inverter_charge.md`.
