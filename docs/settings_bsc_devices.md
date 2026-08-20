# Devices (Geräte-Einstellungen)
Auf dieser Seite werden die gerätespezifischen Einstellungen dokumentiert, die über die allgemeinen [Schnittstellen-Einstellungen](settings_bsc_interfaces.md) hinausgehen: **Group Devices** (virtuelle Batterie-Gruppen), **BPN** (Battery Protection Node) und **JBD BMS**.

## Group Devices (Batterie-Gruppen)

Mit **Group Devices** können mehrere Data-Devices (z. B. einzelne BMS oder Shunts) zu einer virtuellen **Batterie-Gruppe** zusammengefasst werden. Jede Gruppe liefert einen aggregierten Wert für Spannung, Strom und SoC und kann anstelle der einzelnen Data-Devices als Datenquelle verwendet werden – z. B. in den Wechselrichter-Einstellungen, bei den Alarmregeln oder im MQTT-Filter.

!!! note "Hinweis"
    Group Devices werden erst sichtbar, wenn der Parameter **Group Devices aktiv** eingeschaltet ist. Bei aktivierten Group Devices stellen zahlreiche andere Einstellungen (Wechselrichter-Datenquellen, Temperatur-Alarmregeln, MQTT-Filter) auf die Auswahl der **Battery-Packs** (Group Devices) um.

Es stehen bis zu **32 Group Devices** zur Verfügung. Pro Group Device können folgende Parameter konfiguriert werden:

- **Name** – Frei wählbarer Name der Gruppe (max. 16 Zeichen; keine `#`- und `+`-Zeichen).
- **Master Device** / **Second Device** – Primäres bzw. sekundäres Data-Device der Gruppe. Das Master-Device liefert z. B. Zellspannungen und Temperaturen; das Second Device dient als Ergänzung/Redundanz. `Nicht belegt` (255) deaktiviert die Zuweisung.
- **Spannung / Strom / SoC** – Jeweils mit **Quell-Devices** (welche Data-Devices in die Berechnung einfließen) und **Aggregation** (Mittelwert, Maximum, Minimum; beim Strom zusätzlich Summe).
- **Erweiterte Temperaturen** – Quelle für zusätzliche Temperatursensoren: `Nicht belegt`, `Onewire` oder Data-Devices mit erweiterten Sensoren. Darunter die Sensorauswahl **Sensoren 0-31** bzw. (nur bei Quelle Onewire) **Sensoren 32-63**.
- **Erweiterte Temperaturen – Namen** – Frei wählbare Namen für die 32 erweiterten Sensoren (max. 16 Zeichen je Sensor).

```bsc-settings
version: v010
file: groupDeviceMapping.json
profile: off
section: UI_SECT_GROUPDEVICEMAPPING_BATTERY_PACKS
```

!!! tip "Verwendung der Group Devices"
    Nach der Einrichtung einer Gruppe kann diese überall dort als Quelle ausgewählt werden, wo bisher Data-Devices auswählbar waren – erkennbar an den Optionen `Group Device` bzw. `Battery-Pack`. Das betrifft u. a. die Wechselrichter-Einstellungen (Domain „Group devices“), die Temperatur-Überwachung der Alarmregeln, die Wartungsfunktionen und den MQTT-Filter.

## BPN (Battery Protection Node)

!!! note "Hinweis"
    Die BPN-Funktion (Battery Protection Node, ein eigenständiges Sicherheitsmodul) ist in der aktuellen Firmware **nicht aktiv** – in der seriellen Geräteauswahl wird sie als „BPN (not use)“ geführt. Die zugehörige Einstellungsseite ist dennoch in der Firmware vorhanden und wird hier der Vollständigkeit halber dokumentiert.

Die BPN-Einstellungen umfassen:

- **General** – Anzahl Zellen des BPN.
- **Shunt** – Nennkapazität der Batterie (Ah) für die BPN-interne SoC-Berechnung.
- **Ausgänge** – Schaltlogik der Relais 1 und 2 (Arbeitsstrom/Ruhestrom).
- **Alarm – Cell voltage** – Zellspannungs-Grenzwerte (Low/High), Alarm-Verzögerung und Alarm-Ausgang.
- **Alarm – Battery voltage** – Gesamtspannungs-Grenzwerte, Alarm-Verzögerung und Alarm-Ausgang.
- **Alarm – Charge current** – Maximaler Ladestrom, Alarm-Verzögerung und Alarm-Ausgang.
- **Alarm – Discharge current** – Maximaler Entladestrom, Alarm-Verzögerung und Alarm-Ausgang.

```bsc-settings
version: v010
file: deviceBpn.json
profile: off
section: UI_SECT_DEVICEBPN_GENERAL
section: UI_SECT_DEVICEBPN_SHUNT
section: UI_SECT_DEVICEBPN_AUSGAENGE
section: UI_SECT_DEVICEBPN_ALARM_CELL_COLTAGE
section: UI_SECT_DEVICEBPN_ALARM_BATTERY_VOLTAGE
section: UI_SECT_DEVICEBPN_ALARM_CHARGE_CURRENT
section: UI_SECT_DEVICEBPN_ALARM_DISCHARGE_CURRENT
```

## JBD BMS

Für jeden seriellen Anschluss, an dem ein **JBD BMS** ausgewählt ist, kann eine **Cellvoltage 100%** hinterlegt werden. Sobald diese Zellspannung erreicht wird, wird der SoC des JBD-Data-Devices auf 100 % gesetzt.

```bsc-settings
version: v010
file: deviceJbdBms.json
profile: off
index: 1
```

!!! note "Hinweis"
    Die JBD-Einstellungen erscheinen nur, wenn am jeweiligen seriellen Anschluss (Serial 0–10) als Gerät „JBD BMS“ ausgewählt ist. Weitere Hinweise zum Anschluss des JBD finden Sie unter [Unterstützte BMS](devices/bms.md#serial-bms).
