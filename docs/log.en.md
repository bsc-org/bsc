## Example Log {#beispiellog}

Typical firmware output, useful for analysis, diagnosis and troubleshooting. Log messages are reproduced as emitted, including German firmware text.

```text
IMP I (1970-01-01 00:00:00) MAIN: BSC V0.x.x
IMP I (1970-01-01 00:00:00) MAIN: bootCounter=1
IMP I (1970-01-01 00:00:00) MAIN: HW: 2
IMP I (1970-01-01 00:00:00) MAIN: Free Heap: 264308
IMP I (1970-01-01 00:00:00) WEB_SETTINGS: Free flash entries: 161
IMP I (1970-01-01 00:00:00) WEB_SETTINGS: Settings ok
IMP I (1970-01-01 00:00:03) MAIN: Free Heap: 255936
IMP I (1970-01-01 00:00:03) MAIN: Hostname: bsc
IMP I (1970-01-01 00:00:03) MAIN: Init WLAN...
IMP I (1970-01-01 00:00:03) MAIN: Init BLE...
IMP I (1970-01-01 00:00:03) MAIN: Init BLE...ok
IMP I (1970-01-01 00:00:03) MAIN: Verbindung zu ######
IMP I (1970-01-01 00:00:03) BSC_SERIAL: initSerial SerialNr=0, funktionsTyp=0
IMP I (1970-01-01 00:00:03) Inverter: Load inverter settings(): dataSrcAdd=0
IMP I (1970-01-01 00:00:03) Canbus: TWAI START: ESP_OK
IMP I (1970-01-01 00:00:03) EXT_SERIAL: Serial Ext. found
IMP I (1970-01-01 00:00:03) EXT_DISPLAY: Display found
IMP I (1970-01-01 00:00:03) MAIN: Free Heap: 205244
IMP I (1970-01-01 00:00:03) BSC_SERIAL: initSerial SerialNr=1, funktionsTyp=0
IMP I (1970-01-01 00:00:03) BSC_SERIAL: initSerial SerialNr=2, funktionsTyp=9
IMP I (1970-01-01 00:00:03) BSC_SERIAL: initSerial SerialNr=3, funktionsTyp=0
IMP I (1970-01-01 00:00:03) MAIN: WIFI ready (0)
IMP I (1970-01-01 00:00:03) BSC_SERIAL: initSerial SerialNr=4, funktionsTyp=0
IMP I (1970-01-01 00:00:03) BSC_SERIAL: initSerial SerialNr=5, funktionsTyp=0
IMP I (1970-01-01 00:00:03) BSC_SERIAL: initSerial SerialNr=6, funktionsTyp=0
IMP I (1970-01-01 00:00:03) BSC_SERIAL: initSerial SerialNr=7, funktionsTyp=0
IMP I (1970-01-01 00:00:03) BSC_SERIAL: initSerial SerialNr=8, funktionsTyp=0
IMP I (1970-01-01 00:00:03) BSC_SERIAL: initSerial SerialNr=9, funktionsTyp=0
IMP I (1970-01-01 00:00:03) BSC_SERIAL: initSerial SerialNr=10, funktionsTyp=0
IMP I (1970-01-01 00:00:03) MAIN: WIFI STA start (2)
SET E (1970-01-01 00:00:04) BSC_SERIAL: ERROR: device=2, reason=Checksum wrong
```

## Structure of a Log Line {#aufbau-einer-logzeile}

```text
A   B  C                    D     E
IMP I (1970-01-01 00:00:03) MAIN: Verbindung zu ******
```

- **A — Status:** `IMP` = one-off message; `SET` = fault occurred and remains active; `RES` = previously set fault resolved. Active SET errors are available through REST and the dashboard's **Active Errors** tile. SET/RES is not available in every firmware version.
- **B — Severity:** `I` information, `W` warning, `E` error, `D` debug, `V` verbose.
- **C — Timestamp:** `YYYY-MM-DD HH:MM:SS`.
- **D — Source/class:** Component producing the entry.
- **E — Message:** Event description.