# REST API Dokumentation

## Hinweise
- Alle Endpunkte liefern JSON-Daten zurück.
- **Authentifizierung:** Solange der [Passwortschutz](settings_bsc.md#benutzer) aktiviert ist, benötigen die meisten Endpunkte eine gültige Sitzung (Login über das Webinterface). Ausnahmen:
    - `/restapi` **ohne** URL-Parameter ist ohne Anmeldung abrufbar (nur Abfrage).
    - `/restapi/errors/active` und `/restapi/errors/all` sind ohne Anmeldung abrufbar.
    - `/names` ist ohne Anmeldung abrufbar, auch mit Filterparametern.
- Ist der Passwortschutz **deaktiviert** (Parameter *Passwortschutz aktivieren* in den [System-Einstellungen](settings_bsc.md#benutzer)), ist die gesamte API ohne Anmeldung zugänglich.

## Endpunkte

### 1. Systemdaten [GET]
Endpunkt: `/restapi`

**Beschreibung:**
Dieser Endpunkt ermöglicht das Abrufen verschiedener Systemdaten vom Controller. Die Antwort enthält Informationen über den Systemzustand, Daten, die an den Wechselrichter gesendet werden, sowie Daten der verbundenen Data-Devices. Wird der Endpunkt mit URL-Parametern aufgerufen (z. B. `?args`), ist eine gültige Sitzung erforderlich.

**Antwortformat:**  
Dies ist nur ein Auszug aus der Antwort und nicht vollständig!
```json
{
  "system": {
    "fw_version": "V0.10.0",
    "fw_add": "",
    "hw_version": "1",
    "name": "bsc",
    "time": "2025-04-03 06:10:39",
    "boottime": "2025-04-01 21:01:46",
    "system": 0,
    "mqtt": 1,
    "rssi": 23,
    "profile": 0
  },
  "trigger": {
    "1": 0, "2": 1, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0,
    "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0,
    "19": 0, "20": 0, "21": 0, "22": 0, "23": 0, "24": 0, "25": 0, "26": 0, "27": 0
  },
  "inverter": {
    "current": 66.30,
    "voltage": 55.30,
    "soc": 14.00,
    "setpoint_cv": 57.60,
    "setpoint_cc": 200.00,
    "setpoint_dcc": 210.00,
    "cc_cellVoltage": 200.00,
    "cc_soc": 200.00,
    "cc_cellDrift": 200.00,
    "cc_cutOff": 200.00,
    "cc_packHigh": 200.00,
    "cc_temperature": 200.00,
    "cc_tempProfile": 200.00,
    "cc_zero": 200.00,
    "cc_triggerLimit": 0.00,
    "dcc_cellVoltage": 210.00,
    "dcc_temperature": 0.00,
    "dcc_tempProfile": 0.00,
    "dcc_packHigh": 210.00,
    "dcc_triggerLimit": 0.00,
    "autobal_state": 5
  },
  "data_device": [{
      "name": "Seplos 1", 
      "en": 1, 
      "valid": 1, 
      "nr": 0, 
      "totalVolt": 55.30, 
      "totalCurr": 22.10, 
      "soc": 85.00
    }]
}
```

### 2. Alle Active-Errors [GET] 
> Hinweis: Dieser Endpunkt ist nicht in allen Firmware-Versionen verfügbar.

Endpunkt: `/restapi/errors/all`

**Beschreibung:**
Dieser Endpunkt gibt alle möglichen Fehler des Systems zurück, inklusive einer Kennzeichnung, ob sie derzeit aktiv sind oder nicht. Dieser Endpunkt ist ohne Anmeldung abrufbar.

**Antwortformat:**
```json
{
  "errors": [
    {"id": 1,  "state": false, "text": "Data Device 0 Error"},
    {"id": 2,  "state": false, "text": "Data Device 1 Error"},
    {"id": 20, "state": false, "text": "CANBUS Error"}
  ]
}
```

### 3. Aktive Active-Errors [GET]
> Hinweis: Dieser Endpunkt ist nicht in allen Firmware-Versionen verfügbar.

Endpunkt: `/restapi/errors/active`

**Beschreibung:**
Dieser Endpunkt gibt nur die aktuell aktiven Active-Errors des Systems zurück. Das Format ist identisch mit `/restapi/errors/all`, enthält aber nur Einträge mit `"state": true`. Dieser Endpunkt ist ohne Anmeldung abrufbar.

**Antwortformat:**
```json
{
  "errors": [
    {"id": 20, "state": true, "text": "CANBUS Error"}
  ]
}
```

### 4. IO-Daten [GET]
> Hinweis: Dieser Endpunkt ist nicht in allen Firmware-Versionen verfügbar.

Endpunkt: `/restapi/io`

**Beschreibung:**
Dieser Endpunkt gibt den Zustand der digitalen Eingänge (DI) und Relais zurück.

**Antwortformat:**
```json
{
  "di":     [0, 0, 0, 0],
  "relais": [0, 0, 0, 0, 0, 0]
}
```

### 5. vTrigger [POST]
> Hinweis: Dieser Endpunkt ist nicht in allen Firmware-Versionen verfügbar.

Endpunkt: `/restapi/vTrigger`

**Beschreibung:**
Dieser Endpunkt erlaubt das Setzen der virtuellen Trigger. Dafür ist eine gültige Sitzung erforderlich (bzw. deaktivierter Passwortschutz).

**Erwartetes Eingabeformat:**
```json
{
  "id":    [Trigger Nr],
  "value": [0|1]
}
```

**Beispielaufruf mit `curl`**:  
Windows:  
```bash
curl -L -X POST "http://[BSC IP]/restapi/vTrigger" ^
-H "Content-Type: application/json" ^
-d "{\"id\":6,\"value\":0}"
```

Linux:  
```bash
curl -L -X POST "http://[BSC IP]/restapi/vTrigger" \
-H "Content-Type: application/json" \
-d "{\"id\":6,\"value\":0}"
```

### 6. Geräte- und Sensornamen [GET]
> Hinweis: Dieser Endpunkt ist nicht in allen Firmware-Versionen verfügbar.

Endpunkt: `/names`

**Beschreibung:**
Dieser Endpunkt liefert die im BSC vergebenen Namen von Data-Devices, Group Devices, erweiterten Temperatursensoren, Onewire-Sensoren, Relais und digitalen Eingängen. Damit können Sie Messwerte in einer eigenen Visualisierung oder Hausautomation mit den Namen aus dem BSC anzeigen.

Die Antwort enthält **Namen, keine Messwerte**. Aktuelle Messwerte können Sie weiterhin über `/restapi` abrufen. Eine Abfrage von `/names` verändert keine Einstellungen.

**Anmeldung:** Für `/names` ist kein Login erforderlich, auch bei aktiviertem Passwortschutz. Das gilt sowohl für den vollständigen Abruf als auch für Abfragen mit Filterparametern wie `fields`, `dd` und `pd`.

**Aufruf im Browser:**

```text
http://192.168.1.100/names
```

Ersetzen Sie `192.168.1.100` durch die IP-Adresse Ihres BSC. Ohne weitere Angaben werden alle verfügbaren Namensfelder und alle Geräte abgefragt. Für eine kleinere Antwort können Sie die Auswahl mit den folgenden Parametern einschränken.

**Abfrageparameter:**

| Parameter | Bedeutung | Beispiel |
| --- | --- | --- |
| `fields` | Gewünschte Namensfelder, durch Kommas getrennt. Ohne Angabe werden alle Namensfelder geliefert. | `fields=dd.name,pd.name` |
| `dd` | Nummern der gewünschten Data-Devices, durch Kommas getrennt. Ohne Angabe werden alle Data-Devices berücksichtigt. | `dd=0,3` |
| `pd` | Nummern der gewünschten Group Devices, durch Kommas getrennt. Ohne Angabe werden alle Group Devices berücksichtigt. | `pd=1` |

Data-Device- und Group-Device-Nummern werden **ab 0** gezählt; gültig sind die Nummern **0 bis 31**. Die Auswahl mit `dd` oder `pd` legt nur die Geräte fest. Welche Namen zurückgegeben werden, bestimmt `fields`.

Für `fields` stehen folgende Werte zur Verfügung:

| Wert | Gelieferte Namen | Feld in der Antwort |
| --- | --- | --- |
| `dd.name` | Namen der Data-Devices | `data_devices[].name` |
| `dd.temp32` | Namen der erweiterten Temperatursensoren der Data-Devices | `data_devices[].temperature32` |
| `pd.name` | Namen der Group Devices | `group_devices[].name` |
| `pd.temp32` | Namen der ausgewählten erweiterten Temperatursensoren der Group Devices | `group_devices[].temperature32` |
| `ow` | Namen der Onewire-Sensoren | `onewire` |
| `rel` | Namen der Relais | `relays` |
| `di` | Namen der digitalen Eingänge | `digital_inputs` |

**Beispiel: Namen eines Data-Devices und einer Gruppe abrufen**

```text
http://192.168.1.100/names?fields=dd.name,pd.name&dd=0&pd=1
```

Beispielantwort, abhängig von den vergebenen Namen:

```json
{
  "data_devices": [
    { "nr": 0, "name": "Batterie links" }
  ],
  "group_devices": [
    { "nr": 1, "name": "Batteriegruppe" }
  ]
}
```

Die Gerätenummer bleibt im Feld `nr` erhalten. Ordnen Sie Geräte anhand dieser Nummer zu, nicht anhand ihrer Position in der Antwort. Wenn Sie beispielsweise nur Data-Device 3 abfragen, steht dessen Eintrag an erster Stelle, hat aber weiterhin `"nr": 3`.

**Beispiel: Temperatursensornamen einer Gruppe abrufen**

```text
http://192.168.1.100/names?fields=pd.temp32&pd=1
```

Beispielantwort für eine Gruppe mit zwei ausgewählten Sensoren:

```json
{
  "group_devices": [
    {
      "nr": 1,
      "temperature32": ["Vorlauf", "Rücklauf"]
    }
  ]
}
```

Die Namen stehen in derselben Reihenfolge wie die erweiterten Temperaturmesswerte dieser Gruppe. Der erste Name gehört zum Gruppensensor 0, der zweite zum Gruppensensor 1 usw. Maßgeblich ist die [Sensorauswahl im Group Device](settings_bsc_group-devices.md#zuordnung-der-erweiterten-temperaturen), nicht die ursprüngliche physische Sensornummer: Werden beispielsweise die Onewire-Sensoren 7 und 63 ausgewählt, erscheinen sie in der Gruppe als Sensor 0 und 1. Die Namen werden von den jeweiligen Quellsensoren übernommen.

**Weitere Beispiele:**

```text
http://192.168.1.100/names?fields=dd.temp32&dd=0,3
http://192.168.1.100/names?fields=ow
http://192.168.1.100/names?fields=rel,di
```

Die erste Anfrage liefert die Namen der erweiterten Temperatursensoren von Data-Device 0 und 3. Die zweite liefert die Onewire-Namen, die dritte die Relais- und Eingangsnamen. Auch innerhalb dieser Namenslisten beginnt die Zählung bei 0.

**Wichtige Hinweise zur Auswertung:**

- Ein nicht vergebener Name wird als leere Zeichenkette `""` geliefert. Entfernen Sie solche Einträge nicht aus der Liste, da sich sonst die Zuordnung zu den Sensoren oder Ein-/Ausgängen verschiebt.
- Bei gefilterten Data-Device-Abfragen enthält `temperature32` nur die vom konfigurierten Gerät unterstützten Kanäle, derzeit 8, 16 oder 32. Geräte ohne erweiterte Temperatursensoren liefern eine leere Liste. Beim vollständigen Aufruf ohne Abfrageparameter werden weiterhin alle 32 gespeicherten Temperatursensornamen je Data-Device ausgegeben.
- Namen können auch abgerufen werden, wenn das zugehörige Gerät gerade offline ist. Ein vorhandener Name bedeutet daher nicht, dass aktuell ein gültiger Messwert vorliegt.
- Sie müssen die Namen nicht bei jeder Messwertabfrage erneut laden. Rufen Sie sie beispielsweise beim Start Ihrer Visualisierung und nach Änderungen an Namen oder der Sensorauswahl erneut ab.
- Erfolgreiche Anfragen liefern HTTP 200 mit `application/json`. Unbekannte Parameter oder Felder, mehrfach angegebene Parameter, leere oder fehlerhafte Auswahllisten sowie Gerätenummern außerhalb von 0 bis 31 werden mit HTTP 400 abgewiesen. Prüfen Sie in diesem Fall die Schreibweise und die Auswahlwerte.

## Derzeit aktive Inverter-Drosselung
Welche eingestellte Drosselung gerade aktiv ist, können Sie mit Hilfe der Restapi einsehen.  
Hierzu nach der IP-Adresse des BSC "/restapi" hinzufügen (z.B. 192.168.1.100/restapi).  

Die dargestellten "cc_"-Werte und "dcc_"-Werte stellen den durch die jeweilige Laderegelung limitierten Strom dar.

```json
"inverter":{
  "cc_cellVoltage":    0.00,
  "cc_soc":            0.00,
  "cc_cellDrift":      0.00,
  "cc_cutOff":         0.00,
  "cc_packHigh":     100.00,
  "cc_temperature":    0.00,
  "cc_tempProfile":    0.00,
  "cc_zero":           0.00,
  "cc_triggerLimit": 100.00,
  
  "dcc_cellVoltage":   0.00,
  "dcc_temperature": 100.00,
  "dcc_tempProfile": 100.00,
  "dcc_packHigh":    100.00,
  "dcc_triggerLimit":100.00
}
```

Falls es nicht möglich ist, die Daten während eines Drosselungs-Events direkt anzuzeigen, besteht die Möglichkeit, diese temporär über eine alternative Plattform wie Home Assistant aufzeichnen zu lassen. Dabei ist zu beachten, dass jede Abfrage der REST-API alle verfügbaren Daten umfasst.

Für die Übertragung der Daten kann mit einer Dauer von etwa 0,5 bis 1 Sekunde pro Paket gerechnet werden. Diese Zeitangabe dient als Orientierung.

Nachfolgend finden Sie ein Beispiel für einen YAML-Code, der für die Erstellung eines Sensors zur Anzeige des Werts von "setpoint_cc" in Home Assistant verwendet werden kann:

```yaml
platform: rest
name: bscapi_setpoint_cc
resource: http://192.x.x.x/restapi
value_template: "{{ value_json['inverter']['setpoint_cc'] }}"
unit_of_measurement: "A"
state_class: "measurement"
icon: "mdi:api"
```
