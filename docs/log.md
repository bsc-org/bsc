## Beispiellog
Nachfolgend ist ein typisches Beispiel einer vom System erzeugten Logausgabe dargestellt. Diese Informationen können bei der Analyse, Diagnose und Fehlersuche wertvolle Hinweise liefern.

```
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

## Aufbau einer Logzeile
Ein typischer Eintrag im Log sieht wie folgt aus:

```
A   B  C                    D     E
IMP I (1970-01-01 00:00:03) MAIN: Verbindung zu ******
```

Die einzelnen Bestandteile im Detail:

**A – Statuskennung**  
Gibt den Typ des Logeintrags an:  
- `IMP`: Einmalige Meldung  
- `SET`: Ein Fehler ist aufgetreten und besteht aktuell  
- `RES`: Ein zuvor gemeldeter Fehler (via `SET`) wurde behoben und ist nicht mehr aktiv

Die aktuell aktiven Fehler (SET) können über die REST-API abgefragt werden. Zusätzlich werden sie im Dashboard im Bereich „Active Errors“ übersichtlich dargestellt.

> Hinweis: Der Status ist nur in der [Insider Version](insider.md) verfügbar  

**B – Schweregrad**  
Kennzeichnet die Einstufung des Logeintrags:  
- `I`: Information  
- `W`: Warnung  
- `E`: Fehler (Error)  
- `D`: Debug-Eintrag  
- `V`: Ausführliche Ausgabe (Verbose)

**C – Zeitstempel**  
Der Zeitpunkt, zu dem der Logeintrag erzeugt wurde (im Format `YYYY-MM-DD HH:MM:SS`).

**D – Quelle/Klasse**  
Bezeichnet die Komponente oder Klasse, die den Eintrag generiert hat.

**E – Lognachricht**  
Die eigentliche Nachricht bzw. Beschreibung des Ereignisses.





