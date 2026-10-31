# REST API Documentation {#rest-api-dokumentation}

## Notes {#hinweise}

- All endpoints return JSON.
- With [password protection](settings_bsc.md#benutzer) enabled, most endpoints require a valid session established by logging in through the web interface. Exceptions: `/restapi` **without URL parameters**, `/restapi/errors/active` and `/restapi/errors/all` can be read without login.
- With password protection **disabled**, the entire API is accessible without login.

## Endpoints {#endpunkte}

### 1. System Data [GET] {#1-systemdaten-get}

Endpoint: `/restapi`. Returns system status, inverter data and connected data-device data. URL parameters, for example `?args`, require authentication when password protection is enabled.

**Partial response, not a complete response:**

```json
{
  "system": {
    "fw_version": "V0.10.0", "fw_add": "", "hw_version": "1",
    "name": "bsc", "time": "2025-04-03 06:10:39",
    "boottime": "2025-04-01 21:01:46", "system": 0,
    "mqtt": 1, "rssi": 23, "profile": 0
  },
  "trigger": {
    "1": 0, "2": 1, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0,
    "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0, "18": 0,
    "19": 0, "20": 0, "21": 0, "22": 0, "23": 0, "24": 0, "25": 0, "26": 0, "27": 0
  },
  "inverter": {
    "current": 66.30, "voltage": 55.30, "soc": 14.00,
    "setpoint_cv": 57.60, "setpoint_cc": 200.00, "setpoint_dcc": 210.00,
    "cc_cellVoltage": 200.00, "cc_soc": 200.00, "cc_cellDrift": 200.00,
    "cc_cutOff": 200.00, "cc_packHigh": 200.00, "cc_temperature": 200.00,
    "cc_tempProfile": 200.00, "cc_zero": 200.00, "cc_triggerLimit": 0.00,
    "dcc_cellVoltage": 210.00, "dcc_temperature": 0.00,
    "dcc_tempProfile": 0.00, "dcc_packHigh": 210.00,
    "dcc_triggerLimit": 0.00, "autobal_state": 5
  },
  "data_device": [{
    "name": "Seplos 1", "en": 1, "valid": 1, "nr": 0,
    "totalVolt": 55.30, "totalCurr": 22.10, "soc": 85.00
  }]
}
```

### 2. All Possible Active Errors [GET] {#2-alle-active-errors-get}

Not available in every firmware version. Endpoint: `/restapi/errors/all`. Returns all possible errors with their active states. No login required.

```json
{
  "errors": [
    {"id": 1, "state": false, "text": "Data Device 0 Error"},
    {"id": 2, "state": false, "text": "Data Device 1 Error"},
    {"id": 20, "state": false, "text": "CANBUS Error"}
  ]
}
```

### 3. Currently Active Errors [GET] {#3-aktive-active-errors-get}

Not available in every firmware version. Endpoint: `/restapi/errors/active`. Same structure, but only entries with `"state": true`. No login required.

```json
{"errors": [{"id": 20, "state": true, "text": "CANBUS Error"}]}
```

### 4. I/O Data [GET] {#4-io-daten-get}

Not available in every firmware version. Endpoint: `/restapi/io`. Returns digital input and relay states.

```json
{"di": [0, 0, 0, 0], "relais": [0, 0, 0, 0, 0, 0]}
```

### 5. vTrigger [POST] {#5-vtrigger-post}

Not available in every firmware version. Endpoint: `/restapi/vTrigger`. Sets a virtual trigger. A valid session is required unless password protection is disabled. JSON fields: **id** = trigger number, **value** = **0 or 1**.

```json
{"id": 6, "value": 0}
```

Example `curl` commands; with password protection enabled, use an authenticated session as noted above.

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

## Currently Applied Inverter Limits {#derzeit-aktive-inverter-drosselung}

Open `/restapi` after the BSC IP, e.g. `http://192.168.1.100/restapi`. Fields prefixed **cc_** and **dcc_** indicate the current allowed by each charging/discharging control.

Example excerpt from the inverter object:

```json
{
  "inverter": {
    "cc_cellVoltage": 0.00, "cc_soc": 0.00, "cc_cellDrift": 0.00,
    "cc_cutOff": 0.00, "cc_packHigh": 100.00, "cc_temperature": 0.00,
    "cc_tempProfile": 0.00, "cc_zero": 0.00, "cc_triggerLimit": 100.00,
    "dcc_cellVoltage": 0.00, "dcc_temperature": 100.00,
    "dcc_tempProfile": 100.00, "dcc_packHigh": 100.00,
    "dcc_triggerLimit": 100.00
  }
}
```

If you cannot inspect data during an event, record it temporarily in a platform such as Home Assistant. Each REST request retrieves all available data. Allow about **0.5–1 second per response** as a guide.

Example Home Assistant sensor for `setpoint_cc`:

```yaml
platform: rest
name: bscapi_setpoint_cc
resource: http://192.x.x.x/restapi
value_template: "{{ value_json['inverter']['setpoint_cc'] }}"
unit_of_measurement: "A"
state_class: "measurement"
icon: "mdi:api"
```