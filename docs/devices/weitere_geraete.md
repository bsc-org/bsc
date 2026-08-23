# Weitere Geräte

Neben [BMS](bms.md), [Wechselrichtern](wechselrichter.md) und
[externen Shunts](externer_shunt.md) unterstützt der BSC weitere Geräteklassen.
Diese Seite dokumentiert Geräte, die in keine der anderen Kategorien fallen.

## Eletechsup NTC-Temperatur-Boards (NT48x-Serie)

Die Eletechsup-Boards der NT48x-Serie sind **keine BMS**, sondern
Temperaturerfassungs-Boards für NTC-Temperatursensoren. Sie erfassen die
Temperaturen von bis zu 32 angeschlossenen NTC-Sensoren und übergeben die
Werte über RS485 (Modbus RTU) an den BSC.

| Typ | Kanäle | Adresse Singlepack<br>Board / BSC | Adresse Multipack<br>Board / BSC |
| ------------ | ------------ | ------------ | ------------ |
| NT48A08 | 8 | 1 / 1 | 1 / 1 |
| NT48B16 | 16 | 1 / 1 | 1 / 1 |
| NT48C32 | 32 | 1 / 1 | 1 / 1 |

### Anbindung

- **Anschluss:** RS485, direkt an eine der seriellen Schnittstellen des BSC.
  Den Gerätetyp wählst du unter
  [Einstellungen → Schnittstellen → Serial](../settings_bsc_interfaces.md#serial)
  aus – der BSC stellt die Schnittstelle dabei automatisch auf 9600 Baud ein.
- **Protokoll:** Modbus RTU (Funktionscode 03, Holding-Register).
- **Adresse:** Die Modbus-Slave-Adresse wird am Board über DIP-Schalter
  eingestellt. Im BSC wird die Adresse im
  [Data-Device-Mapping](../settings_bsc_interfaces.md#data-devices)
  hinterlegt – sie wird als Modbus-Slave-ID verwendet. Die Adressen in der
  Tabelle oben sind nach dem Schema „Board / BSC" angegeben.

### Temperaturdaten im BSC

Jeder Kanal liefert die Temperatur als 16-Bit-Wert mit einer Auflösung von
0,1 °C. Der BSC übernimmt die Werte in die erweiterten
Temperaturwerte des Daten-Devices.

### Verwendung der Temperaturwerte

Die erweiterten Temperaturwerte stehen im BSC anschließend zur Verfügung für:

- die "Erweiterten Temperaturen" der
  [Group Devices](../settings_bsc_devices.md#zuordnung-der-erweiterten-temperaturen)
- temperaturgeführte Laderegelungen (Lade-/Entladestrom in Abhängigkeit der
  Temperatur)
- REST, MQTT und Home Assistant

Details zur Zuordnung der erweiterten Temperaturen (Bitmasken,
Slot-Reihenfolge) sind unter
[Devices (Geräte-Einstellungen)](../settings_bsc_devices.md#zuordnung-der-erweiterten-temperaturen)
beschrieben.
