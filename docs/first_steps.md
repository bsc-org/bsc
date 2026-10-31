# Erste Schritte und Inbetriebnahme

Diese Reihenfolge führt dich von der Prüfung deiner Geräte bis zur ersten Datenverbindung. Die Anleitung zum Flashen unterscheidet zwischen den Hardware-Varianten; wähle dort den Abschnitt, der zu deinem Board passt.

## Empfohlener Ablauf

1. **Kompatibilität und Hardware prüfen:** Prüfe, ob dein [BMS](devices/bms.md) und dein [Wechselrichter](devices/wechselrichter.md) unterstützt werden. Informationen zur aktuell empfohlenen Hardware findest du unter [Beschaffung der Hardware](#beschaffung-der-hardware).
2. **Firmware installieren und mit dem BSC verbinden:** Folge der [Flash- und Verbindungsanleitung](first_steps_programming.md). Achte darauf, den Abschnitt für deine Hardware zu verwenden.
3. **BMS anschließen:** Folge der [Anschlussanleitung](first_steps_hardware.md), um das BMS mit dem BSC zu verbinden.
4. **BSC konfigurieren und Messwerte prüfen:** Verbinde dich wieder mit der Weboberfläche. Richte Netzwerk und Grundeinstellungen ein, konfiguriere die BMS-Schnittstelle und Gerätezuordnung anhand der [Einstellungen für den Betrieb](first_steps_settings.md) und prüfe im [Dashboard](dashboard.md), ob Messwerte ankommen.
5. **Optional: Wechselrichter und weitere Funktionen einrichten:** Wenn die BMS-Daten korrekt angezeigt werden, kannst du den Wechselrichter anschließen und konfigurieren. MQTT, REST, Alarmregeln und Sensoren lassen sich danach je nach Bedarf ergänzen.

Die Konfiguration hängt von den angeschlossenen Geräten ab. Übernimm Beispielwerte nicht ungeprüft; die [Beispielkonfigurationen](beispiel_konfigurationen.md) sind ausdrücklich als Orientierung und nicht als allgemeingültige Vorgabe gedacht.

## Weitere Hilfe

- [Systemübersicht](system_overview.md)
- [Hardware-Details](hardware.md)
- [Test ohne Originalhardware](BSC_ohne_orig_hardware.md): nur als Testaufbau, nicht für den produktiven Einsatz empfohlen
- [Troubleshooting](troubleshooting.md)

## Info-Videos

[www.youtube.com/@shining-man](http://www.youtube.com/@shining-man)

!!! note "Bitte beachten"
     Aufgrund der Weiterentwicklung des BSC sind nicht mehr alle Inhalte der Videos aktuell.


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

In der freien Firmware wird das **Display** am T-CONNECT nicht unterstützt.

Die Belegung des Pin-Headers ist [hier](hardware.md/#belegung-des-pin-headers) zu finden.  
Weitere Informationen zur Hardware des Lilygo T-CONNECT finden Sie [hier](hardware.md/#lilygo-t-connect).  

### Originales BSC-Mainboard
Das ursprüngliche BSC-Mainboard wurde speziell für das Projekt entwickelt.  

Es kann über den [derzeitigen Platinenhersteller](https://de.aliexpress.com/item/1005007096164253.html) bezogen werden.  
**Die Verfügbarkeit dort war in der Vergangenheit allerdings unbeständig**.
