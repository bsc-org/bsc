## Info-Videos

[www.youtube.com/@shining-man](http://www.youtube.com/@shining-man)  

!!! note "Bitte beachten"
    Aufgrund der kontinuierlichen Weiterentwicklung des BSC können die Informationen der Videos nicht mehr aktuell sein!  

## Weiterführende Informationen

Für erste Informationen und die Inbetriebnahme zuerst folgende weitere Kapitel lesen:  

- [Programmieren des BSC](first_steps_programming.md)  
- [Hardware anschließen](first_steps_hardware.md)  
- [Einstellungen für den Betrieb des BSC](first_steps_settings.md)  

Weiterführende Informationen:

- [Hardware](hardware.md)
- [Konfiguration des BSC](settings_bsc.md)  

Wer die BSC Software ohne originale Hardware testen möchte, sollte das Kapitel [Test ohne originale Hardware](BSC_ohne_orig_hardware.md) lesen.  

Hochrüstungen oder häufige Probleme sind im Kapitel [Troubleshooting](troubleshooting.md) beschrieben.

## Beschaffung der Hardware

Kompatible Hardware – darunter Gehäuse, Erweiterungen und Zubehör – sind über unseren Webshop unter <a href="https://bsc-shop.com" target="_blank">www.BSC-Shop.com</a> erhältlich.  

Für den Betrieb des BSC-Systems kann entweder die **originale BSC-Hardware** oder alternativ ein **kompatibles Drittanbieter-Board** verwendet werden.

### Originale BSC-Hardware

Die ursprüngliche BSC-Hardware wurde speziell für das Projekt entwickelt. Aktuell ist diese jedoch **nicht als fertig montierte Hardware im Handel verfügbar**. Der Selbstbau ist zwar grundsätzlich möglich, jedoch mit höherem Aufwand verbunden.

### Alternative: LILYGO T-CONNECT

Als empfohlene Alternative kann das **LILYGO T-CONNECT Board** verwendet werden. Dieses ist kompatibel mit der Firmware und den Funktionen des BSC-Systems.  

Eine Bezugsquelle ist beispielsweise:  
🔗 [LILYGO T-CONNECT auf AliExpress](https://de.aliexpress.com/item/1005007619430455.html)

!!! danger "Wichtig!"
    Beim Kauf unbedingt darauf achten, dass die **Variante mit 3× RS485 und 1× CAN-Schnittstelle** gewählt wird!  

**Hinweise zur Funktionalität**  
Da das T-CONNECT Board **keine integrierten Relais oder Digitaleingänge** besitzt, kommt es im Vergleich zur originalen BSC-Hardware zu funktionalen Einschränkungen.

Mit der **Insider-Firmware** lassen sich diese Einschränkungen jedoch teilweise kompensieren:

- Die Signale für **Relaisausgänge**, **Digitaleingänge** sowie **I²C-Kommunikation** werden auf den **Pin-Header** zur direkten Ansteuerung von externen Modulen oder Relais herausgeführt. Die Belegung des Pin-Headers ist [hier](hardware.md/#belegung-des-pin-headers) zu finden.
- Anschluss des **Displays** über den Header.

Damit bietet die Insider-Firmware eine flexible Erweiterungsmöglichkeit, um das T-CONNECT Board näher an den Funktionsumfang der originalen BSC-Hardware heranzuführen.
