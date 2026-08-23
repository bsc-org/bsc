# Group Devices
Auf dieser Seite werden die gerätespezifischen Einstellungen dokumentiert, die über die allgemeinen [Schnittstellen-Einstellungen](settings_bsc_interfaces.md) hinausgehen: **Group Devices** (virtuelle Batterie-Gruppen).

## Group Devices (Batterie-Gruppen)

Mit **Group Devices** können mehrere Data-Devices (z. B. einzelne BMS oder Shunts) zu einer virtuellen **Batterie-Gruppe** zusammengefasst werden. Jede Gruppe liefert einen aggregierten Wert für Spannung, Strom und SoC und kann anstelle der einzelnen Data-Devices als Datenquelle verwendet werden – z. B. in den Wechselrichter-Einstellungen, bei den Alarmregeln oder im MQTT-Filter.

!!! note "Hinweis"
    Group Devices werden erst sichtbar, wenn der Parameter **Group Devices aktiv** eingeschaltet ist. Bei aktivierten Group Devices stellen zahlreiche andere Einstellungen (Wechselrichter-Datenquellen, Temperatur-Alarmregeln, MQTT-Filter) auf die Auswahl der **Battery-Packs** (Group Devices) um.

Es stehen bis zu **32 Group Devices** zur Verfügung. Pro Group Device können folgende Parameter konfiguriert werden (im Einstellungsblock unten sind exemplarisch die ersten beiden Group Devices abgebildet – alle Group Devices sind identisch aufgebaut):

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

### Zuordnung der erweiterten Temperaturen

Die **Erweiterten Temperaturen** stellen pro Group Device bis zu **32 Temperatur-Slots** bereit. Welche Sensoren die Slots belegen, wird über die **Quelle** und die beiden Sensorauswahlen **Sensoren 0-31** und **Sensoren 32-63** festgelegt.

**Quelle**

- **Nicht belegt** – Die erweiterten Temperaturen sind deaktiviert (alle Slots leer).
- **Onewire** – Als Quelle dienen die Sensoren der [Onewire-Adressliste](settings_bsc_interfaces.md#onewire-onewire-adressen).
- **Data-Device** – Als Quelle dient ein Data-Device mit erweiterten Temperatursensoren. Dies sind ausschließlich die seriellen Temperatur-Erfassungsgeräte **NT48A08** (8 Sensoren), **NT48B16** (16 Sensoren) und **NT48C32** (32 Sensoren).

**Sensorauswahl (Bitmasken)**

Jedes Häkchen in **Sensoren 0-31** bzw. **Sensoren 32-63** entspricht einem Bit in einer 32-Bit-Maske – die angezeigte Nummer ist die **physische Sensornummer**:

- **Data-Device-Quelle:** Nummer `n` = der `n`-te erweiterte Temperaturkanal des ausgewählten Devices (Zählung ab 0 – Nummer 0 ist der erste Messkanal des NT48-Geräts). Die Auswahl **Sensoren 32-63** wird bei dieser Quelle nicht angezeigt und hat keine Wirkung.
- **Onewire-Quelle:** Nummer `n` = der Onewire-Sensor mit der laufenden Nummer `n` aus der Onewire-Adressliste (der erste Eintrag der Liste ist Nummer 0). **Sensoren 32-63** adressiert die Sensoren 32–63.

**Belegung der 32 Slots**

Die ausgewählten Sensoren werden **aufsteigend nach ihrer Nummer** auf die Slots verteilt – zuerst die ausgewählten Sensoren 0–31, danach (nur bei Quelle Onewire) die ausgewählten Sensoren 32–63. Es zählen höchstens die ersten **32** ausgewählten Sensoren. Die Namensfelder **Erweiterte Temperaturen - Namen** („Sensor 0“ bis „Sensor 31“) beschriften die Slots in genau dieser Reihenfolge – die Namen hängen also am **Slot**, nicht an der Sensornummer. Wird die Auswahl geändert, beschriften die bestehenden Namen die Slots in der neuen Reihenfolge.

**Beispiel:** Häkchen bei **5, 10, 15, 16, 17, 18, 19, 20** (acht ausgewählte Sensoren):

| Slot | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8–31 |
|---|---|---|---|---|---|---|---|---|---|
| Sensor | 5 | 10 | 15 | 16 | 17 | 18 | 19 | 20 | leer |

- Bei Quelle **Data-Device** liefert Slot 0 den Kanal 5, Slot 1 den Kanal 10 usw. des ausgewählten Devices.
- Bei Quelle **Onewire** liefert Slot 0 den Onewire-Sensor 5, Slot 1 den Sensor 10 usw.
- Die Namensfelder „Sensor 0“ bis „Sensor 7“ beschriften diese acht Slots; Slots 8–31 bleiben leer.

Die erweiterten Temperaturen können anschließend überall dort verwendet werden, wo Group Devices als Quelle wählbar sind – z. B. in den Wechselrichter-Einstellungen zur Temperatur-Reduzierung des Lade-/Entladestroms (dort unter **Erweiterte Sensorquellen** und **Erweiterte Sensoren 0-31**). Zudem werden sie über die [REST-API](restapi.md) und [MQTT](mqtt.md) bereitgestellt.

!!! tip "Verwendung der Group Devices"
    Nach der Einrichtung einer Gruppe kann diese überall dort als Quelle ausgewählt werden, wo bisher Data-Devices auswählbar waren – erkennbar an den Optionen `Group Device` bzw. `Battery-Pack`. Das betrifft u. a. die Wechselrichter-Einstellungen (Domain „Group devices“), die Temperatur-Überwachung der Alarmregeln, die Wartungsfunktionen und den MQTT-Filter.
