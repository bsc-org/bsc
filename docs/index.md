# Battery Safety Controller (BSC) – <br>Der flexible Controller für DIY-Batterien
<img src="img/bsc_display.png" width="600">

Der **Battery Safety Controller (BSC)** ist ein frei konfigurierbarer Controller, der für eine Vielzahl von Steuerungs- und Überwachungsaufgaben in DIY-Batteriesystemen eingesetzt werden kann. Der BSC übernimmt die zentrale Steuerung des Energy-Sorange-Systems und kann als zusätzliches Sicherheitslevel neben dem BMS fungieren.

## Der BSC besteht aus zwei Komponenten:
1. **BSC-Hardware** – Sie fungiert als Middleware zwischen dem BMS und dem Wechselrichter. Ein Vorteil der BSC-Hardware ist ihr sicherer Betrieb: Alle physischen Schnittstellen sind galvanisch isoliert.
2. **BSC-Software** – Diese macht die BSC-Hardware zu einem frei konfigurierbaren Controller, der für eine Vielzahl von Steuerungs- und Überwachungsaufgaben in DIY-Batteriesystemen verwendet werden kann.

## Einsatzmöglichkeiten des BSC

### 1. Überwachung von verbundenen Geräten (seriell, Bluetooth)
Der BSC kann die Daten von angeschlossenen Geräten (BMS, Balancer, Temperatursensoren) via MQTT an einen Broker senden, um sie grafisch darzustellen (z.B. in Grafana) oder weiter zu verarbeiten, z.B. in einem Automatisierungssystem wie **ioBroker**, **NodeRed** oder **Home Assistant**.

### 2. Lade-Steuerung
Der BSC nutzt die Daten der angeschlossenen Geräte, um den Wechselrichter (Victron, Solis, DEYE, etc.) zu steuern, der über den CAN-Bus verbunden ist. Hierbei stehen mehrere Funktionen zur Verfügung, um die Lade-Steuerung an das eigene DIY-Batteriesystem anzupassen:

- Zellspannungsabhängige Drosselung des Ladestroms
- Reduzierung des Ladestroms bei Zellabweichungen
- SoC-abhängige Reduktion des Ladestroms
- Ladeabschaltung: Verhindert kontinuierliches Nachladen, wenn die Batterie voll ist
- Zusammenführung der Daten aus den einzelnen physischen Batteriepaketen zu einem virtuellen Gesamtbatteriepaket unter Berücksichtigung zahlreicher Parameter, z.B. ob das Batteriepaket überhaupt lädt oder entlädt.
- Und noch einges mehr ...

### 3. Zweites Sicherheitslevel neben dem BMS
Der BSC kann verschiedene konfigurierbare Parameter auf den angeschlossenen Geräten überwachen, um ein zusätzliches Sicherheitslevel zu schaffen. Überwachte Parameter umfassen:

- Regelmäßige Antwort des angeschlossenen BMS
- Zellspannungen (min/max)
- Gesamte Spannung (min/max)
- Temperaturen

Diese Daten können verwendet werden, um beispielsweise Relaisausgänge zu steuern und einen Lasttrennschalter auszulösen.

### 4. Temperaturüberwachung
Es können bis zu **64 OneWire-Temperatursensoren** (DS18B20) angeschlossen und überwacht werden. Verschiedene Regelungen sind möglich:

- Überwachung des Maximalwerts
- Überwachung des Minimalwerts
- Überwachung des Maximalwerts mit einem Sensor als Referenzwert
- Überwachung der Differenzwerte

Alle Einstellungen können flexibel über eine Web-Oberfläche parametriert werden.

Der **Battery Safety Controller** bietet eine vielseitige und anpassbare Lösung für die Überwachung und Steuerung von DIY-Batteriesystemen. Ideal für anspruchsvolle Anwendungen, die eine zusätzliche Sicherheitsebene und umfangreiche Steuerungsmöglichkeiten benötigen.
