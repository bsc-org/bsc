Dieses Kapitel gibt einen Überblick über das Anschließen der Hardware, wie zum Beispiel dem BMS oder Wechselrichter, für den Betrieb des BSC.

## 1. Verbindung des BMS mit dem BSC
Für die Verbindung des BMS mit dem BSC muss der BSC ausgeschaltet sein.  
Im folgenden Beispiel wird ein **Lilygo T-CONNECT** verwendet, das über drei RS485-Schnittstellen verfügt. An jede Schnittstelle kann ein BMS-Typ angeschlossen werden. Falls das BMS *Daisy Chain* unterstützt, können mehrere BMS desselben Typs an einem RS485-Port betrieben werden.  

Weitere Informationen:  

- [Unterstützte BMS](https://bsc-org.github.io/bsc/devices/bms/#serial-bms)  
- [BMS-Anschlussbeispiele](https://bsc-org.github.io/bsc/devices/bms/#anbindungs-beispiele)  
- [RS485-Port-Zuordnung am Lilygo T-CONNECT](https://bsc-org.github.io/bsc/hardware/#lilygo-t-connect)  

Für die Unterstützung weiterer BMS kann ein Issue im Repository erstellt werden: [BSC Firmware Issues](https://github.com/shining-man/bsc_fw/issues)  

## 2. Verbindung des Wechselrichters mit dem BSC
Der Wechselrichter wird über die **CAN-Schnittstelle** mit dem BSC verbunden. Der BSC muss hierfür ausgeschaltet sein.  

Weitere Informationen:  

- [CAN-Bus-Stecker am Lilygo T-CONNECT](https://bsc-org.github.io/bsc/hardware/#lilygo-t-connect)  
- [Hinweise zur Verbindung von Wechselrichtern](https://bsc-org.github.io/bsc/devices/wechselrichter/)  
