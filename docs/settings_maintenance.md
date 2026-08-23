# Wartung

Der **Wartungsmodus** nimmt einzelne Geräte vorübergehend aus dem laufenden Betrieb – zum Beispiel, wenn du an einem Batteriepack arbeitest und ihn dafür abklemmen oder abschalten möchtest. Das markierte Gerät wird nicht mehr abgefragt und löst keine Alarme mehr aus; der Rest der Anlage (andere Geräte, Wechselrichter-Anbindung, MQTT, Display) arbeitet unverändert weiter.

## Einstellungen

Pro Kategorie gibt es zwei Einstellungen:

- **Wartung aktiv** – Die markierten Geräte werden nicht mehr abgefragt: Es werden keine Daten mehr von ihnen gelesen und es kommen keine Daten mehr vom Gerät. Außerdem werden sie von der Überwachung und Regelung ausgenommen – sie fließen nicht mehr in Alarme, Laderegelung oder Wechselrichter-Steuerung ein.
- **MQTT senden** – Für Geräte mit „Wartung aktiv“ legst du hier fest, dass sie **weiterhin abgefragt** werden und ihre Daten **per MQTT gesendet** werden.

Die Einstellungen gibt es getrennt für **Data Devices** und **Group Devices**:

```bsc-settings
version: v010
file: maintenance.json
profile: off
section: UI_SECT_MAINTENANCE_WARTUNGSMODUS
```

!!! note "Hinweis"
    Die Auswahl „Group Devices“ ist nur relevant, wenn [Group Devices](settings_bsc_group-devices.md#group-devices-batterie-gruppen) aktiviert sind.

## Was passiert bei „Wartung aktiv“?

- **Keine Abfragen mehr:** Der BSC schickt keine Leseabfragen mehr an das markierte Gerät. Die zuletzt gelesenen Werte werden nicht mehr aktualisiert und gelten nach wenigen Sekunden als ungültig. Du kannst das Gerät daher gefahrlos abschalten oder abklemmen – ohne dass Kommunikations- oder Zellspannungsalarme ausgelöst werden.
- **Keine Alarme:** Das Gerät wird aus allen Alarmregeln (Zellspannung, Temperatur, Plausibilität, Zellspannungs-Einbruch) ausgeschlossen.
- **Keine Regelung:** Laderegelung, Entladeregelung und Wechselrichter-Steuerung verwenden das Gerät nicht mehr als Datenquelle.
- **Der Rest läuft weiter:** Alle anderen Geräte, die Wechselrichter-Kommunikation, OneWire-Temperatursensoren, das Display und MQTT (für die übrigen Geräte) funktionieren unverändert.
- **Sichtbarkeit:** Der Wartungsstatus wird in der Web-App angezeigt und per MQTT als `maintenance`-Flag veröffentlicht.

!!! note "Wartung eines Data Devices bei aktivierten Group Devices"
    Setzt du ein Data Device in Wartung, gelten auch die [Batteriegruppen](settings_bsc_group-devices.md#group-devices-batterie-gruppen), die dieses Gerät verwenden, automatisch als in Wartung: Die Regelung nimmt die betroffenen Gruppen aus. Das Gerät wird nur noch abgefragt, wenn es eine nicht gewartete Gruppe oder die Einstellung „MQTT senden“ benötigt.

## „MQTT senden“ im Wartungsmodus

Standardmäßig sendet der BSC für Geräte mit „Wartung aktiv“ keine Daten mehr per MQTT. Aktivierst du für ein solches Gerät zusätzlich **MQTT senden**, gilt:

- Das Gerät wird **weiterhin abgefragt** – es kommen also weiterhin Daten vom Gerät.
- Die gelesenen Daten werden **per MQTT gesendet** (alle Werte wie im Normalbetrieb).
- Das `maintenance`-Flag bleibt gesetzt, damit Empfänger (z. B. Home Assistant) erkennen, dass sich das Gerät in Wartung befindet.

!!! note "Hinweis"
    „MQTT senden“ wirkt nur zusammen mit „Wartung aktiv“ – Geräte ohne Wartungsmarkierung werden ohnehin abgefragt und per MQTT gesendet.
