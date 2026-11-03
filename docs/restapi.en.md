# REST API Documentation {#rest-api-dokumentation}

## Notes {#hinweise}

- All endpoints return JSON.
- With [password protection](settings_bsc.md#benutzer) enabled, most endpoints require a valid session established by logging in through the web interface. Exceptions: `/restapi` **without URL parameters**, `/restapi/errors/active`, `/restapi/errors/all` and `/names` can be read without login. For `/names`, this also applies to requests with filter parameters.
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

### 6. Device and Sensor Names [GET] {#6-gerate-und-sensornamen-get}

> Note: This endpoint is not available in every firmware version.

Endpoint: `/names`

**Description:**
This endpoint returns the names configured in the BSC for Data Devices, Group Devices, extended temperature sensors, Onewire sensors, relays and digital inputs. You can use these names to label measurements in your own visualization or home automation system.

The response contains **names, not measurements**. Current measurements remain available through `/restapi`. A request to `/names` does not change any settings.

**Authentication:** No login is required for `/names`, even with password protection enabled. This applies both to full requests and to requests with filter parameters such as `fields`, `dd` and `pd`.

**Open in a browser:**

```text
http://192.168.1.100/names
```

Replace `192.168.1.100` with your BSC's IP address. Without additional parameters, all available name fields and all devices are requested. For a smaller response, use the following parameters to restrict the selection.

**Query parameters:**

| Parameter | Meaning | Example |
| --- | --- | --- |
| `fields` | Requested name fields, separated by commas. If omitted, all name fields are returned. | `fields=dd.name,pd.name` |
| `dd` | Requested Data Device numbers, separated by commas. If omitted, all Data Devices are included. | `dd=0,3` |
| `pd` | Requested Group Device numbers, separated by commas. If omitted, all Group Devices are included. | `pd=1` |

Data Device and Group Device numbers **start at 0**; valid numbers range from **0 to 31**. The `dd` and `pd` parameters select only the devices. The `fields` parameter determines which names are returned.

The following values are available for `fields`:

| Value | Names returned | Response field |
| --- | --- | --- |
| `dd.name` | Data Device names | `data_devices[].name` |
| `dd.temp32` | Names of the Data Devices' extended temperature sensors | `data_devices[].temperature32` |
| `pd.name` | Group Device names | `group_devices[].name` |
| `pd.temp32` | Names of the Group Devices' selected extended temperature sensors | `group_devices[].temperature32` |
| `ow` | Onewire sensor names | `onewire` |
| `rel` | Relay names | `relays` |
| `di` | Digital input names | `digital_inputs` |

**Example: Retrieve the names of a Data Device and a group**

```text
http://192.168.1.100/names?fields=dd.name,pd.name&dd=0&pd=1
```

Example response, depending on the configured names:

```json
{
  "data_devices": [
    { "nr": 0, "name": "Left battery" }
  ],
  "group_devices": [
    { "nr": 1, "name": "Battery group" }
  ]
}
```

The device number is preserved in the `nr` field. Identify devices by this number, not by their position in the response. For example, if you request only Data Device 3, its entry appears first but still has `"nr": 3`.

**Example: Retrieve a group's temperature sensor names**

```text
http://192.168.1.100/names?fields=pd.temp32&pd=1
```

Example response for a group with two selected sensors:

```json
{
  "group_devices": [
    {
      "nr": 1,
      "temperature32": ["Flow", "Return"]
    }
  ]
}
```

The names appear in the same order as the group's extended temperature measurements. The first name belongs to group sensor 0, the second to group sensor 1, and so on. The [sensor selection in the Group Device](settings_bsc_group-devices.md#zuordnung-der-erweiterten-temperaturen) determines this order, not the original physical sensor number: for example, if Onewire sensors 7 and 63 are selected, they appear in the group as sensors 0 and 1. Names are taken from the respective source sensors.

**More examples:**

```text
http://192.168.1.100/names?fields=dd.temp32&dd=0,3
http://192.168.1.100/names?fields=ow
http://192.168.1.100/names?fields=rel,di
```

The first request returns the extended temperature sensor names for Data Devices 0 and 3. The second returns the Onewire names, and the third returns the relay and digital input names. Indices within these name lists also start at 0.

**Important notes for processing responses:**

- An unset name is returned as an empty string `""`. Do not remove these entries from the list, as this would shift the mapping to sensors or inputs/outputs.
- In filtered Data Device requests, `temperature32` contains only the channels supported by the configured device, currently 8, 16 or 32. Devices without extended temperature sensors return an empty list. A full request without query parameters still returns all 32 stored temperature sensor names per Data Device.
- Names can also be retrieved when the associated device is offline. A name being present does not mean that a valid measurement is currently available.
- You do not need to reload names with every measurement request. For example, retrieve them when your visualization starts and after changes to names or sensor selections.
- Successful requests return HTTP 200 with `application/json`. Unknown parameters or fields, duplicate parameters, empty or malformed selection lists, and device numbers outside 0 to 31 are rejected with HTTP 400. If this happens, check the spelling and selection values.

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