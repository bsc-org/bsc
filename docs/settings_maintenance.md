# Wartung

Der **Wartungsmodus** dient dazu, einzelne Geräte vorübergehend aus der Überwachung und Steuerung auszuschließen – z. B. während Wartungs- oder Servicearbeiten an einem Batteriepack.

## Wartungsmodus

Pro Kategorie gibt es zwei Einstellungen:

- **Wartung aktiv** – Die markierten Geräte werden von der Regelung und Überwachung ausgenommen (sie liefern weiterhin Daten, fließen aber nicht mehr in Alarme, Laderegelungen etc. ein).
- **MQTT senden** – Legt fest, welche Geräte im Wartungsmodus weiterhin per MQTT gesendet werden sollen.

Die Einstellungen gibt es getrennt für **Data Devices** und **Group Devices**:

```bsc-settings
version: v010
file: maintenance.json
profile: off
section: UI_SECT_MAINTENANCE_WARTUNGSMODUS
```

!!! note "Hinweis"
    Die Auswahl „Group Devices“ ist nur relevant, wenn [Group Devices](settings_bsc_group-devices.md#group-devices-batterie-gruppen) aktiviert sind.
