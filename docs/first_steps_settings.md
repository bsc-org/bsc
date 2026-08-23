# Einstellungen für den Betrieb des BSC
Dieses Kapitel gibt einen Überblick über die erforderlichen Einstellungen für den Betrieb des BSC.  
Abweichungen können je nach Firmware-Version auftreten. Die hier beschriebenen Einstellungen beziehen sich auf die aktuelle BSC-Firmware; daneben existiert eine separate **Supporter-Firmware** mit eigenem Funktionsumfang (siehe [Supporter](supporter.md)). Die **freie Firmware** nutzt das **Classic WebUI**.

!!! tip "Einrichtungsassistenten"
    Für die Erstkonfiguration bietet die WebApp [Einrichtungsassistenten](setup_assistant.md) für Netzwerk, MQTT, die seriellen Schnittstellen und den Wechselrichter an. Die Assistenten führen durch die wichtigsten Schritte und befüllen das Data-Device-Mapping automatisch.

## 1. Grundeinstellungen
Die Grundeinstellungen werden im Menü **System** vorgenommen.  
Hierzu zählen insbesondere:  

- WLAN-Zugangsdaten  
- Falls erforderlich: MQTT-Broker-Daten (bei Nutzung von MQTT)  

**Zugriff auf die Systemeinstellungen**:  
`Einstellungen → System` 

Weitere Informationen:  

- [Details zu den Systemeinstellungen](settings_bsc.md#system)  

## 2. BMS-Einstellungen im BSC
Damit eine Kommunikation stattfinden kann, sind folgende Konfigurationen erforderlich:  

!!! note "Hinweis"  
    Der BSC greift **ausschließlich lesend** auf die Daten des BMS zu.  
    Es werden zu keinem Zeitpunkt Einstellungen, Konfigurationen oder sonstige Daten **auf das BMS geschrieben**.  
    Dadurch bleibt die weitere Sicherheits-Instanz "BMS" immer funktional unabhängig.  

        
### 2.1 Serielle Schnittstelle konfigurieren
Hier wird festgelegt, welcher **BMS-Typ** an welcher **Hardware-Schnittstelle** angeschlossen ist.  
  
Im folgenden Beispiel ist ein **JK Inverter BMS** mit *Serial 0* verbunden:

- Serial 0 → **JK Inverter BMS**
- Serial 1 → nicht belegt
- Serial 2 → nicht belegt

**Pfad:**  
`Einstellungen → Schnittstellen → Serial`

!!! note "Hinweis"  
    An einer Schnittstelle können mehrere BMS desselben Typs betrieben werden.  
    Die Unterscheidung erfolgt über unterschiedliche Adressen, deren Konfiguration im nächsten Schritt (Data-Device-Mapping) beschrieben wird.

Weitere Informationen: [Serielle Schnittstellen](settings_bsc_interfaces.md#serial)  

### 2.2 Data-Device-Mapping einrichten
Nachdem im vorherigen Schritt festgelegt wurde, welcher **BMS-Typ** an welcher **seriellen Schnittstelle** angeschlossen ist, erfolgt nun die Zuordnung der **einzelnen BMS** mit ihren spezifischen **Adressen**.  

Das **Data-Device** ist die interne Repräsentation eines physischen Geräts (BMS, Victron SmartShunt etc.) im BSC.  
  
Die korrekte Adresszuordnung ist notwendig, damit der BSC mit dem BMS kommunizieren kann.  
Besonders bei mehreren BMS desselben Typs (z.B. mehrere *JK Inverter BMS*) an einer Schnittstelle ist eine eindeutige Adresse erforderlich.

Die hier konfigurierten Data-Devices dienen als Grundlage für weitere Einstellungen, beispielsweise in der Wechselrichter-Konfiguration.

**Pfad:**  
`Einstellungen → Schnittstellen → Data devices`

**Konfiguration:**  

Für jedes Data-Device müssen folgende Einstellungen vorgenommen werden:

- **Schnittstelle**: Auswahl der Hardware-Schnittstelle (Serial 0, Serial 1, etc.)
- **Adresse**: BMS-spezifische Adresse (0–16)  
  
    !!! info "Adresskonfiguration beachten"  
        Die Adresse muss sowohl **am BMS selbst** als auch **im BSC Data-Device-Mapping** korrekt eingestellt werden.  
        Welche Adresse wo einzustellen ist, wird BMS-spezifisch hier erklärt:  
        [Unterstützte BMS – Adresskonfiguration](https://bsc-org.github.io/bsc/devices/bms/#serial-bms)  
        **Diese Dokumentation sollte sorgfältig gelesen werden**, da jeder BMS-Typ unterschiedliche Anforderungen hat.
        
- **Name** (optional): Anzeigename für bessere Übersicht in allen BSC-Menüs

**Beispiel:**  
An *Serial 0* sind zwei JK Inverter BMS angeschlossen:

- **Data-Device 0**: Serial 0, Adresse 1, Name "Batterie unten"
- **Data-Device 1**: Serial 0, Adresse 2, Name "Batterie oben"

Weitere Informationen:

- [Adresskonfiguration pro BMS-Typ](https://bsc-org.github.io/bsc/devices/bms/#unterstutzte-bms)
- [Data-Device-Mapping Details](settings_bsc_data_devices.md#data-devices)

## 3. Wechselrichter-Einstellungen
In diesem Abschnitt werden die grundlegenden Einstellungen beschrieben, die erforderlich sind, damit der BSC mit dem Wechselrichter kommunizieren kann.  

### 3.1 Allgemeine Einstellungen
**Pfad:**  
`Einstellungen → Wechselrichter & Laderegelung → Allgemein`

Folgende Parameter müssen für die Grundkommunikation konfiguriert werden:  

- **BMS CAN-Bus Enable:**  
  Aktiviert die Kommunikation mit dem Wechselrichter.  
- **CAN-Bus-Protokoll:**  
  Auswahl des Protokolls entsprechend dem Wechselrichter (z. B. *Victron* oder *Pylontech*).  
  **Hinweis**: Bei den meisten Wechselrichtern muss **Pylontech** als CAN-Bus-Protokoll ausgewählt werden.
- **Datenquelle**:  
  Hier wird ausgewählt, von welchen Data-Devices die Daten genommen werden, um sie dann – je nach weiteren Einstellungen – aufbereitet an den Wechselrichter zu senden.  
  Die Aufbereitung kann beispielsweise die Aggregation mehrerer Datenquellen oder die Anwendung von definierten Laderegelungen umfassen. 

    !!! note "Hinweis"  
        Welcher Wert von welchem Data-Device verwendet wird, lässt sich über die [Valuehandling-Einstellungen](settings_inverter.md#valuehandling-multi-bms) detailliert festlegen (Domain, Quelle und Aggregation je Messwert). Sind [Group Devices](settings_bsc_group-devices.md#group-devices-batterie-gruppen) aktiviert, können dort außerdem Battery-Packs als Quelle gewählt werden.

- **Kategorie Valuehandling:**  
  Festlegung, von welchen Data-Devices welche Werte übernommen und wie diese aggregiert werden.  
  Weitere Informationen: [Valuehandling Multi-BMS](settings_inverter.md#valuehandling-multi-bms)  
- **Kategorie Basisdaten:**  
  Konfiguration von Ladespannungen und maximalen Strömen für das gesamte System.  
  Unter *Batterypack settings* können zusätzlich pro Data-Device Kapazität und maximale Ströme definiert werden.  

Weitere Informationen: [Wechselrichter-Einstellungen](settings_inverter.md#wechselrichter)  

### 3.2 Einstellungen zur Laderegelung
Informationen zur Konfiguration der Laderegelung sind hier verfügbar:  
[Dokumentation Laderegelung](settings_inverter_charge.md)  

## 4. Alarmregeln
Alarmregeln dienen der Überwachung bestimmter Werte von Data-Devices und dem Auslösen von Triggern, wenn Grenzwerte erreicht werden.  
Dies ersetzt nicht die korrekt gesetzten Werte im BMS, ermöglicht jedoch eine frühzeitige Reaktion, z. B.:  

- Wechselrichter auf 0 A Ladestrom setzen  
- Relais schalten
- Benachrichtigung auslösen: Der Trigger, sofern MQTT aktiviert ist, wird per MQTT übertragen und kann in einer Automatisierungssoftware (z. B. ioBroker, Home Assistant) für weitere Aktionen wie Benachrichtigungen oder Steuerbefehle weiterverarbeitet werden.

Weitere Informationen zu den Triggern und ihrer Funktionsweise: [Funktionsprinzip der Trigger](settings_bsc_trigger.md#funktionsprinzip-der-trigger)  
