Dieses Kapitel gibt einen Überblick über das Anschließen der Hardware, wie zum Beispiel dem BMS oder Wechselrichter, für den Betrieb des BSC.

## 1. Verbindung des BMS mit dem BSC
Für die Verbindung des BMS mit dem BSC muss der BSC ausgeschaltet sein.  
Im folgenden Beispiel wird ein **Lilygo T-CONNECT** verwendet, das über drei RS485-Schnittstellen verfügt. An jede Schnittstelle kann ein BMS-Typ angeschlossen werden. Falls das BMS *Daisy Chain* unterstützt, können mehrere BMS desselben Typs an einem RS485-Port betrieben werden.  

Weitere Informationen:  

- [Unterstützte BMS](devices/bms.md#serial-bms)  
- [BMS-Anschlussbeispiele](devices/bms.md#anbindungs-beispiele)  
- [RS485-Port-Zuordnung am Lilygo T-CONNECT](hardware.md#lilygo-t-connect)  
- [RS485 Steckerbelegung am Lilygo T-CONNECT](hardware.md#steckerbelegung)  

Für die Unterstützung weiterer BMS kann ein Issue im Repository erstellt werden: [BSC Firmware Issues](https://github.com/shining-man/bsc_fw/issues)  

## 2. Verbindung des Wechselrichters mit dem BSC
Der Wechselrichter wird über die **CAN-Schnittstelle** mit dem BSC verbunden. Der BSC muss hierfür ausgeschaltet sein.  

Weitere Informationen:  

- [CAN-Bus-Stecker am Lilygo T-CONNECT](hardware.md#lilygo-t-connect)  
- [CAN Steckerbelegung am Lilygo T-CONNECT](hardware.md#steckerbelegung)  
- [Hinweise zur Verbindung von Wechselrichtern](devices/wechselrichter.md)  
