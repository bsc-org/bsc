# Data Devices

Das **Data-Device-Mapping** dient der Zuordnung der Schnittstelle (z. B. einer seriellen Schnittstelle) zum im BSC verwendeten internen *Data-Device*. Diese Zuordnung ist Grundlage für weitere Konfigurationen, z. B. in den Wechselrichter-Einstellungen.

```bsc-settings
version: v010
file: dataDeviceMapping.json
profile: off
section: UI_SECT_DATADEVICEMAPPING_DATA_DEVICE_MAPPING
```

Hierbei müssen folgende Parameter eingestellt werden:

  - **Schnittstelle**: Auswahl der Schnittstelle, an der das Data-Device angeschlossen ist (z. B. `Serial 0` oder `Bluetooth 0`; `Nicht belegt` deaktiviert das Data-Device).
  - **Adresse**: Die eindeutige Adresse (0–16), die dem spezifischen Gerät zugewiesen wird oder vom Hersteller fest zugewiesen ist. Informationen, welche Adresse bei welchem BMS eingestellt werden muss, sind hier dokumentiert: [Unterstützte BMS – Adresskonfiguration](https://bsc-org.github.io/bsc/devices/bms/#unterstutzte-bms). Der dortige Text sollte sorgfältig gelesen werden, da er beschreibt, **welche Adresse am BMS selbst** und **welche hier im Data-Device-Mapping des BSC** eingestellt werden muss.
  - **Name** (optional): Ein benutzerdefinierter Name, der in den weiteren Einstellungen des Parameters angezeigt wird. Dieser Name wird außerdem für den MQTT-Topic des jeweiligen Devices verwendet.

    !!! Hinweis
        Der Name darf keine # und + Zeichen enthalten!

!!! note "Hinweis"
    In den Auswahllisten anderer Einstellungsseiten (z. B. Datenquelle, Alarmregeln) erscheinen nur die **konfigurierten** Data-Devices, also diejenigen mit zugewiesener Schnittstelle.

Falls mehrere Geräte an einer seriellen Schnittstelle angeschlossen sind und das BMS (Battery Management System) die Verbindung im Daisy-Chain-Modus unterstützt, ist es erforderlich, für jedes Gerät die korrekte Adresse zu definieren. Nur so kann eine eindeutige Zuordnung und eine fehlerfreie Kommunikation zwischen dem BMS und den Geräten sichergestellt werden.

!!! note "Hinweis"
    Die korrekte Konfiguration der Data Device Mappings ist essenziell, um eine störungsfreie Funktionalität zu gewährleisten. Beachten Sie die Adressierungsregeln Ihres BMS-Systems.

## Value Adjustment

```bsc-settings
version: v010
file: dataDeviceMapping.json
profile: off
section: UI_SECT_DATADEVICEMAPPING_VALUE_ADJUSTMENTS
```

Das "Value Adjustment" ermöglicht es, dem Wechselrichter abhängig von der Zellspannung einen angepassten State of Charge (SoC) zu übermitteln. Die Einstellungen werden **pro Data-Device** vorgenommen.

!!! note "Hinweis zur Supporter-Firmware"
    Das Value Adjustment ist ebenfalls Bestandteil der **Supporter-Firmware**. Weitere Informationen: [Supporter](supporter.md).

Folgende Optionen stehen zur Verfügung:

- **SoC linearisieren**: Ist diese Option aktiviert, wird der SoC linear zwischen den beiden Spannungswerten *Cellvoltage for SoC 0%* und *Cellvoltage for SoC 100%* berechnet. Dazu müssen beide Werte gesetzt sein und der 100-%-Wert größer als der 0-%-Wert sein.

- **SoC 100% trigger mode**: Legt fest, welche Zellen den Schwellwert erreichen müssen, damit der SoC auf 100 % gesetzt wird:
    - **Eine Zelle erreicht Schwellwert** – Es genügt, wenn die höchste Zellspannung den Wert *Cellvoltage for SoC 100%* erreicht.
    - **Alle Zellen erreichen Schwellwert** – Der SoC wird erst auf 100 % gesetzt, wenn alle konfigurierten Zellen den Wert *Cellvoltage for SoC 100%* erreicht haben.

- **Cellvoltage for SoC 100%** (in mV): Der SoC-Wert wird erst dann auf 100 % gesetzt, wenn die eingestellte Zellspannung erreicht ist. Bis dahin wird der SoC-Wert des zugeordneten Data-Devices übernommen und maximal mit 99 % angezeigt. Ein Wert von `0` deaktiviert die Funktion.

- **Cellvoltage for SoC 0%** (in mV): Funktioniert analog zu *Cellvoltage for SoC 100%*, jedoch für den unteren Grenzwert. Der SoC wird erst auf 0 % gesetzt, wenn die definierte Zellspannung erreicht oder unterschritten ist. Ein Wert von `0` deaktiviert die Funktion.

**Verhalten ohne aktiviertes „SoC linearisieren“:**

- Ist nur *Cellvoltage for SoC 100%* gesetzt, wird der SoC bei Erreichen der Schwelle auf 100 % gesetzt; fällt die Zellspannung wieder darunter, wird der SoC-Wert des BMS übernommen.
- Ist nur *Cellvoltage for SoC 0%* gesetzt, gilt das Verhalten entsprechend für die untere Schwelle.
- Sind beide Werte gesetzt, werden die beiden Schwellen unabhängig voneinander angewendet (fester 100-%- bzw. 0-%-Wert ab Schwelle).

**Beispiel (mit „SoC linearisieren“):**

- Cellvoltage für SoC 100%: 3,5 V
- Cellvoltage für SoC 0%: 2,9 V
- Bei ≥ 3,5 V → SoC = 100 %
- Bei ≤ 2,9 V → SoC = 0 %
- Zwischen 2,9 V und 3,5 V → SoC linear berechnet

Die lineare Berechnung ist besonders nützlich für BMS-Systeme, die keinen eigenen SoC-Wert bereitstellen, da der SoC in Abhängigkeit von den Zellspannungen automatisch ermittelt wird.

!!! danger "Wichtiger Hinweis"
    Stellen Sie sicher, dass die eingetragenen Zellspannungen den Spezifikationen des verwendeten Batteriesystems entsprechen, um eine optimale Funktion und Sicherheit zu gewährleisten.
