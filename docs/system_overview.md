## Systemüberblick
Der BSC ist ein frei konfigurierbarer Controller, welcher eine Schnittstelle zwischen den verschiedenen Komponenten eines DIY Batteriesystems realisiert. Er kann eine Vielzahl an Kontroll- und Überwachungsaufgaben übernehmen, unter anderem die zentrale Ladesteuerung des Speichersystems oder die Realisierung einer zweiten Sicherheitsebene neben des BMS.

```mermaid
%%{init: {
    'theme': 'base', 
    'themeVariables': { 'fontSize': '16px', 'fontFamily': 'Arial', 'edgeLabelBackground': 'white'}
}}%%


flowchart TD
    BMS[BMS] -- "RS485" --> BSC[Serial 0-2]
    TEMP_SENSOR[Temperature<br>Sensors] -- Onewire --> BSC
    NEEY[NEEY<br>Balancer] <-- Bluetooth --> BSC[Bluetooth]
    VICTRON_SHUNT[Victron<br>SmartShunt] --> VICTRON_SHUNT_CONV[RS485<br>Converter] -- RS485 --> BSC
    BSC -- CAN --> CAN[Inverter]
    BSC[MQTT] <-- MQTT --> MQTT_BROKER[MQTT Broker]
    BSC[REST API] -- REST --> REST[REST Client]

    BSC[Extension<br>Interface] -.- E1[<a href='hardware.md#bsc-display'>Display</a>]
    SE["Serial<br>Extension<br>(Serial 3-10)"] -.- BSC
    BMS -- RS485 --> SE

    BSC[Battery Safety Controller]:::wide
    
    subgraph Battery  
        BMS
        TEMP_SENSOR
        NEEY
        VICTRON_SHUNT
    end

classDef wide padding:200px
style BSC fill:#ffdbaa 
```

## Komponenten
* **BSC:** das Gerät besteht aus einer Platine und der darauf laufenden Software. Er besitzt verschiedenste Schnittstellen, um mit den externen Komponenten kommunizieren zu können (WLAN, Bluetooth, RS485, CAN-Bus, Onewire, digitale Ein- und Ausgänge, sowie einen Analogeingang)
* **Display:** optional kann an den BSC ein Display angeschlossen werden, welches über einen I2C-Bus mit dem BSC kommuniziert. Weitere Informationen finden sich [hier im Wiki](hardware.md#bsc-display). Es bietet sich an, BSC und Display in [diesem Gehäuse](https://bsc-shop.com/produkt-kategorie/gehaeuse/) zu betreiben. 
* **Serial Extension:** der BSC besitzt 3 RS485 Schnittstellen für den Anschluss von BMS. Falls weitere benötigt werden, kann das Serial Extension Board an den BSC angeschlossen werden um 8 weitere RS485 Schnittstellen zu erhalten. Siehe [das entsprechende Github-Repo](https://github.com/shining-man/bsc_extension_serial)
* **BMS:** Verschiedene BMS können über RS485, CAN, oder Bluetooth verbunden werden. Von diesen werden dann aktuelle Zustandsinformationen der Batterien, wie Zellspannungen, SOC oder Temperaturen abgerufen. Siehe [hier im Wiki](devices/bms.md)
* **Temperatursensoren:** Es können zusätzliche Temperatursensoren über Onewire oder Digital- bzw. Analogeingänge angeschlossen werden, welche die Informationen des angeschlossenen BMS ergänzen.
* **Balancer:** Balancer von NEEY können vom BSC angesteuert werden, inklusive Abruf der aktuellen Zustandsinformationen und Steuerung des Balancers.
* **Shunt:** Der BSC kann den SoC einer Batterie von einem externen Shunt abrufen. Derzeit wird ein Victron SmartShunt unterstützt. Da dieser nur über UART kommuniziert, wird ein zusätzlicher RS485/UART Konverter benötigt.  
Siehe [hier im Wiki](devices/externer_shunt.md)
* **Inverter:** Der BSC kommuniziert mit verschiedenen Wechselrichtern über CAN-Bus, wie z.B. Victron, Solis oder DEYE. Dabei kann der aktuelle Batteriezustand gemeldet werden, und auch Konfigurationsparameter, wie z.B. zur Ladesteuerung, gesetzt werden.  
Siehe [hier im Wiki](devices/wechselrichter.md)
* **MQTT Broker:** Alle Zustandsdaten können zusätzlich über WLAN an einen MQTT Broker gesendet werden, um diese langfristig zu speichern und zu visualisieren (z.B. über Grafana).  
Siehe [hier im Wiki](mqtt.md)
* **REST Client:** Zustandsdaten über die überwachten Batterien oder über den BSC können über eine HTTP REST API abgerufen werden.  
Siehe [hier im Wiki](settings_bsc.md#derzeit-aktive-inverter-drosselung)

## Verfügbare Schnittstellen
* **WLAN:** Zugriff auf das BSC-Webinterface, Übertragung von MQTT-Daten
* **Bluetooth:** ~~Kommunikation mit NEEY-Balancer~~
* **RS485:** Abruf von BMS-Daten
* **CAN Bus:** Abruf von BMS-Daten, Kommunikation mit Wechselrichtern
* **HTTP REST:** Abruf von Batterie- und BSC-Zustandsinformationen
* **Onewire:** Abruf von Sensordaten, wie z.B. Temperatursensoren
* **Digitale Eingänge:** Empfang von digitalen Sensordaten über einen galvanisch getrennten Eingang
* **Analoger Eingang:** Empfang von analogen Sensordaten  über einen galvanisch getrenten Eingang
* **Digitale Ausgänge:** Steuerung von externen Geräten über Relais
