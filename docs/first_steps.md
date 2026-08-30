## Info-Videos
[www.youtube.com/@shining-man](http://www.youtube.com/@shining-man)  

!!! note "Bitte beachten"
    Aufgrund der Weiterentwicklung des BSC, ist nicht mehr alles im Video aktuell!  


## Weiterführende Informationen
Für erste Informationen und die Inbetriebnahme zuerst folgende weitere Kapitel lesen:  
[Programmieren des BSC](first_steps_programming.md)  
[Hardware anschließen](first_steps_hardware.md)  
[Einstellungen für den Betrieb des BSC](first_steps_settings.md)  

Weiterführende Informationen:   
[Hardware](hardware.md)   
[Konfiguration des BSC](settings_bsc.md)  

Wer die BSC Software ohne orginale Hardware testen möchte, sollte das Kapitel 
[Test ohne orig. Hardware](BSC_ohne_orig_hardware.md) lesen.  

Hochrüstungen oder häufige Probleme sind im Kapitel [Troubleshooting](troubleshooting.md) beschrieben.


## Beschaffung der Hardware
Kompatible Hardware - darunter Gehäuse, Erweiterungen und Zubehör - sind über den Webshop unter <a href="https://bsc-shop.com" target="_blank">www.BSC-Shop.com</a> erhältlich.  

Für den Betrieb des BSC-Systems wird aktuell das **LILYGO T-CONNECT Board** empfohlen.  
Das ursprüngliche BSC-Mainboard wurde speziell für das Projekt entwickelt, ist jedoch nicht mehr regulär verfügbar und wird daher nicht mehr als empfohlene Beschaffungsoption geführt.

### Empfohlene Hardware: LILYGO T-CONNECT
Das **LILYGO T-CONNECT Board** unterstützt die BSC-Firmware und ist die aktuell empfohlene Hardware für den Betrieb des BSC-Systems.  
Die RS485- und CAN-Bus-Anschlüsse sind galvanisch getrennt ausgeführt; fehlende Komponenten gegenüber dem ursprünglichen BSC-Mainboard können durch externe Module teilweise kompensiert werden (siehe unten).
  
Eine Bezugsquelle ist beispielsweise:  
🔗 [LILYGO T-CONNECT auf AliExpress](https://de.aliexpress.com/item/1005007619430455.html)

!!! danger "Wichtig!"
    Beim Kauf unbedingt darauf achten, dass die **Variante mit 3× RS485 und 1× CAN-Schnittstelle** gewählt wird!  

**Hinweise zur Funktionalität**  
Da das T-CONNECT Board **keine integrierten Relais, Digitaleingänge oder eine redundante Spannungsversorgung** besitzt, kommt es im Vergleich zur originalen BSC-Hardware zu funktionalen Einschränkungen.  

Die **Supporter-Version** ermöglicht den Anschluss des **Displays** über den Pin-Header.  
Die Belegung des Pin-Headers ist [hier](hardware.md/#belegung-des-pin-headers) zu finden.  
Weitere Informationen zur Hardware des Lilygo T-CONNECT finden Sie [hier](hardware.md/#lilygo-t-connect).  

### Originales BSC-Mainboard
Das ursprüngliche BSC-Mainboard wurde speziell für das Projekt entwickelt.  

Es kann über den [derzeitigen Platinenhersteller](https://de.aliexpress.com/item/1005007096164253.html) bezogen werden.  
**Die Verfügbarkeit dort war in der Vergangenheit allerdings unbeständig**.