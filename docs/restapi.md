# REST API Dokumentation

## Hinweise
- Alle Endpunkte liefern JSON-Daten zurück.
- **Authentifizierung:** Solange der [Passwortschutz](settings_bsc.md#benutzer) aktiviert ist, benötigen die meisten Endpunkte eine gültige Sitzung (Login über das Webinterface). Ausnahmen:
    - `/restapi` **ohne** URL-Parameter ist ohne Anmeldung abrufbar (nur Abfrage).
    - `/restapi/errors/active` und `/restapi/errors/all` sind ohne Anmeldung abrufbar.
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
  "data_device": [
    {"name": "Seplos 1", "en": 1, "valid": 1, "nr": 0, "totalVolt": 55.30, "totalCurr": 22.10, "soc": 85.00}
  ]
}
```

### 2. Alle Active-Errors [GET] 
> Hinweis: Dieser Endpunkt ist Bestandteil der separat erhältlichen [Supporter-Firmware](supporter.md).

Endpunkt: `/restapi/errors/all`

**Beschreibung:**
Dieser Endpunkt gibt alle möglichen Fehler des Systems zurück, inklusive einer Kennzeichnung, ob sie derzeit aktiv sind oder nicht. Dieser Endpunkt ist ohne Anmeldung abrufbar.

**Antwortformat:**
```json
{
  "errors": [
    {"id": 1, "state": false, "text": "Data Device 0 Error"},
    {"id": 2, "state": false, "text": "Data Device 1 Error"},
    {"id": 20, "state": false, "text": "CANBUS Error"}
  ]
}
```

### 3. Aktive Active-Errors [GET]
> Hinweis: Dieser Endpunkt ist Bestandteil der separat erhältlichen [Supporter-Firmware](supporter.md).

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
> Hinweis: Dieser Endpunkt ist Bestandteil der separat erhältlichen [Supporter-Firmware](supporter.md).

Endpunkt: `/restapi/io`

**Beschreibung:**
Dieser Endpunkt gibt den Zustand der digitalen Eingänge (DI) und Relais zurück.

**Antwortformat:**
```json
{
  "di": [0, 0, 0, 0],
  "relais": [0, 0, 0, 0, 0, 0]
}
```

### 5. vTrigger [POST]
> Hinweis: Dieser Endpunkt ist Bestandteil der separat erhältlichen [Supporter-Firmware](supporter.md).

Endpunkt: `/restapi/vTrigger`

**Beschreibung:**
Dieser Endpunkt erlaubt das Setzen der virtuellen Trigger. Dafür ist eine gültige Sitzung erforderlich (bzw. deaktivierter Passwortschutz).

**Erwartetes Eingabeformat:**
```json
{
  "id": [Trigger Nr],
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

## Derzeit aktive Inverter-Drosselung
Welche eingestellte Drosselung gerade aktiv ist, können Sie mit Hilfe der Restapi einsehen.  
Hierzu nach der IP-Adresse des BSC "/restapi" hinzufügen (z.B. 192.168.1.100/restapi).  

Die dargestellten "cc_"-Werte und "dcc_"-Werte stellen den durch die jeweilige Laderegelung limitierten Strom dar.

![](img/settings/settings_restapi_aktive_drosselung.png){ width="250" }  

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
