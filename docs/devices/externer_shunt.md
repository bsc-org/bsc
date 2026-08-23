# Externe Shunts

Der BSC kann den Ladezustand (State of Charge, SoC) einer Batterie von einem externen Shunt übernehmen. Aktuell wird der **Victron SmartShunt** unterstützt, der über seine VE.Direct-Schnittstelle mit dem BSC verbunden wird. Der Shunt liefert dem BSC den SoC sowie Gesamtspannung und Strom der Batterie.

## Victron SmartShunt

### Vorteil des externen Shunts

Der SmartShunt misst den Batteriestrom fortlaufend direkt am Messpunkt und ermittelt daraus seinen Ladezustand per Stromzählung (Coulomb-Zählung). Dieser SoC-Wert ist damit unabhängig von der SoC-Berechnung des BMS, die bei vielen BMS-Systemen mit der Zeit vom tatsächlichen Ladezustand abweicht (Drift). Für eine präzise SoC-Erfassung ist der externe Shunt daher eine sinnvolle Ergänzung zum BMS: Der BSC liest den SoC zusammen mit Gesamtspannung und Strom aus dem Shunt aus und kann diese Werte für den Wechselrichter und die SoC-abhängigen Laderegelungen verwenden.

!!! note "Hinweis"
    Der Shunt-SoC ersetzt den SoC des BMS **nicht automatisch**. Damit der BSC den SoC des Shunts verwendet, musst du den Shunt unter **Valuehandling** als Quelle auswählen – siehe [Schritt 3](#3-shunt-als-quelle-wahlen-valuehandling).

!!! warning "Keine Zellspannungen vom Shunt"
    Der SmartShunt liefert keine Zellspannungen und keine Temperaturwerte. Laderegelungen, die Zellspannungen benötigen, können daher nicht allein mit dem Shunt als Datenquelle arbeiten und benötigen zusätzlich ein BMS (siehe [Datenquelle](../settings_inverter.md#general)).

### Hardwareverbindung

Der SmartShunt wird über seinen VE.Direct-Port an den BSC angeschlossen. Da die seriellen Schnittstellen des BSC auf RS485 basieren, ist dafür ein Adapter erforderlich: die **Single device extension (SDE)**. Sie ist im [BSC-Shop](https://bsc-shop.com/produkt/single-device-extension/) erhältlich und wird mit einem üblichen RJ45-Netzwerkkabel mit dem BSC verbunden.

Ein galvanisch getrennter Adapter ist nicht erforderlich, da die seriellen Eingänge des BSC bereits galvanisch getrennt sind (siehe [CAN/RS485](../hardware.md#canrs485)).

Über die SDE wird genau ein Gerät angeschlossen. Benötigst du weitere serielle Schnittstellen, kannst du sie mit der Serial-Extension erweitern (Serial 3 bis 10, siehe [Serial](../settings_bsc_interfaces.md#serial)).

### Einstellungen im BSC

Die Einrichtung erfolgt in drei Schritten: Gerätetyp an der seriellen Schnittstelle festlegen, die Schnittstelle einem Data-Device zuordnen und den Shunt als Quelle für die gewünschten Messwerte auswählen. Schritt 4 beschreibt die optionale Wertanpassung (Value Adjustment) für den Shunt.

#### 1. Gerätetyp an der Serial-Schnittstelle auswählen

Öffne `Einstellungen → Schnittstellen → Serial` und wähle an dem seriellen Port, an dem die SDE mit dem SmartShunt angeschlossen ist, den Gerätetyp **Victron SmartShunt**. Der BSC stellt die Schnittstelle anschließend automatisch auf die passende Baudrate ein (19200 Baud). Weitere Details zur Serial-Seite findest du unter [Serial](../settings_bsc_interfaces.md#serial).

#### 2. Schnittstelle im Data-Device-Mapping zuordnen

Öffne `Einstellungen → Schnittstellen → Data devices` und ordne die Schnittstelle einem Data-Device zu (siehe [Data-Devices](../settings_bsc_data_devices.md#data-devices)):

- **Schnittstelle:** der serielle Port aus Schritt 1.
- **Adresse:** `0`. Der SmartShunt besitzt keine Geräteadresse – das VE.Direct-Protokoll arbeitet ohne Adressierung, und die Firmware sieht für den Shunt nur die Adresse `0` vor.
- **Name** (optional): Der Name wird in den Auswahllisten der weiteren Einstellungen angezeigt und für den MQTT-Topic des Data-Devices verwendet.

#### 3. Shunt als Quelle wählen (Valuehandling)

Damit der BSC die Werte des Shunts an den Wechselrichter übermittelt, wähle ihn unter `Einstellungen → Wechselrichter & Laderegelung → Allgemein` im Abschnitt **Valuehandling** als Quelle aus (Details siehe [Valuehandling](../settings_inverter.md#valuehandling-multi-bms)):

- **Quelle SoC:** Wähle hier den Shunt aus, damit sein SoC an den Wechselrichter übermittelt wird.
- **Quelle Gesamtspannung** und **Quelle Gesamtstrom:** Optional kannst du auch für diese Werte den Shunt als Quelle wählen.

Der so ermittelte SoC wird an den Wechselrichter gesendet und steuert alle SoC-abhängigen Funktionen, zum Beispiel die SoC-abhängige Reduzierung des Ladestroms und den Charge-Current Cut-Off.

Wird der Shunt nicht als Quelle ausgewählt, nutzt der BSC weiterhin die Werte der konfigurierten Datenquellen – ein automatisches Ersetzen findet nicht statt.

#### 4. Value Adjustment für den Shunt

Der vom Shunt gelieferte SoC durchläuft denselben Anpassungsmechanismus wie der SoC jedes anderen Data-Devices (siehe [Value Adjustment](../settings_bsc_data_devices.md#value-adjustment)). Mit den Standardwerten – alle Funktionen deaktiviert – wird der SoC des Shunts unverändert übernommen.

!!! warning "Zellspannungsbasierte Korrekturen nicht für den Shunt verwenden"
    Die Korrekturen *Cellvoltage for SoC 100 %*, *Cellvoltage for SoC 0 %* und *SoC linearisieren* werten die Zellspannungen des jeweiligen Data-Devices aus. Da der SmartShunt keine Zellspannungen liefert, können diese Korrekturen für das Shunt-Data-Device nicht greifen – lass sie für den Shunt deaktiviert:

    - Ein gesetzter Wert für *Cellvoltage for SoC 0 %* würde den Shunt-SoC dauerhaft auf **0 %** setzen, da die Schwelle ohne Zellspannungen immer als unterschritten gilt.
    - Ein gesetzter Wert für *Cellvoltage for SoC 100 %* würde den Shunt-SoC dauerhaft bei maximal **99 %** festhalten, da die Schwelle nie erreicht wird.
    - Ein aktiviertes *SoC linearisieren* würde den Shunt-SoC bei gesetzten Zellspannungswerten dauerhaft auf **0 %** setzen.

### Werte des Shunts im BSC

Der BSC liest zyklisch folgende Werte aus dem SmartShunt aus:

- **SoC** mit einer Auflösung von 0,01 %
- **Gesamtspannung** der Batterie
- **Strom** mit einer Auflösung von 0,1 A

Zusätzlich werden regelmäßig weitere Statuswerte abgerufen und über MQTT veröffentlicht: Time-to-go (verbleibende Laufzeit), Zyklen, minimale und maximale Spannung, Zeit seit der letzten Vollladung, Anzahl der SoC-Synchronisierungen, Zähler für Unter- und Überspannungsalarme sowie die geladene und entladene Energie. In Home Assistant stehen diese Werte über die [Auto-Discovery](../mqtt.md#home-assistant-auto-discovery) automatisch zur Verfügung.
