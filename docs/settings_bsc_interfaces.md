# Schnittstellen des BSC
In den Schnittstellen Einstellungen wird eingestellt was an welcher Schnittstelle angeschlossen ist. Hier wird **nicht** eingestellt was z.B. mit den Daten von einem BMS oder Balancer passieren soll, oder wann der Relais-Ausgang schalten soll. Dies wird dann bei den Einstellungen zu den Alarmregeln oder dem Wechselrichter gemacht.



## Relaisausgänge
Hier können die grundlegenden Einstellungen zu den Relaisausgängen vorgenommen werden.

```bsc-settings
version: v010
file: digitalOut.json
profile: off
index: 1
```

* **Auslösung bei**
  Hier wird angegeben bei welchem Trigger (Trigger 1–27) das Relais schalten soll
* **Auslöseverhalten**
    * Permanent: Das Relais bleibt angezogen, solange der Trigger ansteht
    * Impuls: Das Relais schaltet für eine Dauer von x ms. Die Impulsdauer wird unter "Impulsdauer" eingestellt.
* **Impulsdauer**
  Hier wird die Impulsdauer eingestellt, wenn bei dem Auslöseverhalten "Impuls" eingestellt wurde (100–10000 ms, Standard 500 ms).
* **Verzögerung**
  Gibt an um wie viel Sekunden das Schalten des Relais bei einem kommenden Trigger verzögert werden soll (0–254 s).
* **Invertieren**
  Die Option ermöglicht es, den Relaisausgang flexibel zwischen den Betriebsmodi NO (Normally Open) und NC (Normally Closed) umzuschalten. Durch Aktivieren dieser Option wird die Logik des Relaisausgangs umgekehrt, sodass bei der Ausführung des Schaltvorgangs der alternative Zustand genutzt wird. Diese Funktion ist besonders nützlich, um die Kompatibilität mit verschiedenen Steuerungsanforderungen oder Schaltungsdesigns sicherzustellen.



## Digitaleingänge
Hier können die grundlegenden Einstellungen zu den Digitaleingängen vorgenommen werden.

```bsc-settings
version: v010
file: digitalIn.json
profile: off
index: 1
```

- **Eingang invertieren**  
  Hier kann der Eingang invertiert werden

- **Weiterleiten an**  
  Mit dieser Option wird festgelegt, welcher Trigger (Trigger 1–27) durch einen bestimmten Eingang aktiviert wird.  
    - Wird der Eingang **High**, wird der hier ausgewählte Trigger aktiviert.  
    - Ist der Eingang **invertiert**, wird der Trigger bei einem **Low**-Signal am Eingang aktiviert. 



## Serial
In diesem Abschnitt legen Sie fest, welche Hardware an welchem seriellen Port angeschlossen ist. Darüber hinaus ist es erforderlich, im Abschnitt ["Data devices"](settings_bsc_data_devices.md#data-devices) zu konfigurieren, welche serielle Port welchem internen Daten-Device zugeordnet wird.

Detaillierte Informationen zur Einrichtung der Data Devices finden sie im Kapitel [Data devices](settings_bsc_data_devices.md#data-devices).

Diese Konfiguration stellt sicher, dass die angeschlossene Hardware korrekt erkannt wird und mit den entsprechenden internen Daten-Devices verknüpft werden kann.

```bsc-settings
version: v010
file: serial.json
profile: off
index: 1
```

**Zuordnung bei der orginal BSC Hardware (Software => Hardware):**

* Serial 0 => U1
* Serial 1 => U2
* Serial 2 => U3

Serial 3 bis 10 sind nur mit angeschlossener Serial-Extension nutzbar.  

**Unterstützte Hardware (Serielle Schnittstellen)**  
Eine Liste der unterstützten Hardware mit Details zur Adressierung ist unter folgendem Link verfügbar: [Unterstützte BMS](devices/bms.md#unterstutzte-bms)  
Die Liste der verfügbaren Hardware wird kontinuierlich erweitert, um den Anforderungen und Bedürfnissen unserer Nutzer gerecht zu werden.

### Anzahl Zellen

```bsc-settings
version: v010
file: serial.json
profile: off
section: UI_SECT_SERIAL_ALLGEMEIN
```

Gibt die Anzahl der in einer Batterie verbauten Einzelzellen an.  
Diese Einstellung ist z.B. wichtig, um die Werte im Dashboard korrekt darzustellen.  

### Filter

```bsc-settings
version: v010
file: serial.json
profile: off
section: UI_SECT_SERIAL_FILTER
```

Dieser Filter dient dazu, plötzliche Sprünge in den Zellspannungen zu erkennen und zu unterdrücken.  
Er sorgt für eine präzisere und stabilere Datenverarbeitung, indem temporäre Spannungssprünge herausgefiltert und die Verwertung fehlerhafter Datenpakete verhindert werden.

Die Ansprechschwelle des Filters wird als Prozentsatz im Vergleich zum vorherigen gültigen Wert festgelegt.  
Überschreitet die Zellspannung den eingestellten Prozentsatz, wird der neue Wert verworfen. Der Wert wird jedoch nicht als Fehler gewertet, solange er die eingestellte Grenze nicht überschreitet.

**Anzahl RX-Fehler**  
Gibt die Anzahl aufeinanderfolgender fehlerhaft empfangener Datenpakete an, nach deren Erreichen der Zustand als Fehler bewertet wird.  
Wird die eingestellte Anzahl überschritten, erfolgt keine Aktualisierung des Zeitstempels für das letzte gültige Paket mehr im System.

**Abweichung Zellspannung**  
Legt die maximal zulässige prozentuale Abweichung der Zellspannungen fest.  
Ein Wert von `0` deaktiviert die Filterfunktion.



## Onewire (Onewire Adressen)
In diesem Menü kann die OneWire-Funktion aktiviert und die Adressen der angeschlossenen OneWire-Temperatursensoren festgelegt werden.  
Unterstützt werden Temperatursensoren vom Typ **DS18B20**.  
Es können bis zu **64 Sensoren** konfiguriert werden.

```bsc-settings
version: v010
file: onewireAdr.json
profile: off
index: 1
```

Sobald die OneWire-Konfigurationsseite aufgerufen wird, scannt der Controller zyklisch den OneWire-Bus nach angeschlossenen Devices.  
Gefundene Devices werden am unteren Ende der Seite angezeigt.  

Fett dargestellte Devices kennzeichnen neue Sensoren, die noch nicht in der OneWire-Konfiguration gespeichert sind.  
Diese Hervorhebung erleichtert das Identifizieren und Hinzufügen neu angeschlossener Sensoren.  

<table>
<tr><td>28:93:e3:95:f0:1:3c:56</td><td><button onclick='copyStringToClipboard("28:93:e3:95:f0:1:3c:56")'>Copy</button></td></tr>
<tr><td><b>28:93:e3:95:f0:1:3c:57</b></td><td><button onclick='copyStringToClipboard("28:93:e3:95:f0:1:3c:57")'>Copy</button></td></tr>
<tr><td>28:93:e3:95:f0:1:3c:58</td><td><button onclick='copyStringToClipboard("28:93:e3:95:f0:1:3c:58")'>Copy</button></td></tr>
</table>
 
Über die **Copy**-Schaltfläche kann die jeweilige Sensoradresse in die Zwischenablage kopiert werden.  



## Onewire II (Temperatur-Offset)

Hier kann für jeden der bis zu **64 OneWire-Temperatursensoren** ein Offset eingestellt werden, um die gemessene Temperatur zu korrigieren.

```bsc-settings
version: v010
file: onewire2.json
profile: off
index: 1
```



## Bluetooth
!!! warning
    Bluetooth wird in der aktuell Firmware nicht unterstützt

```bsc-settings
version: v010
file: bluetooth.json
profile: off
index: 1
```

~~ Hier können bis zu 5 Bluetooth Devices festgelegt werden, von denen der Controller Daten holt.~~  
~~Dazu muss der Device-Typ und die MAC-Adresse (in Kleinbuchstaben) eingestellt werden.~~  

~~Der Controller scannt, sobald diese Konfigurationsseite aufgerufen ist, zyklisch nach neuen BT-Devices und zeigt die letzten 5 gefundenen am unteren Ende der Seite an.~~  

~~**Unterstützte Hardware**~~  
~~Eine Liste der unterstützten Hardware ist unter folgendem Link verfügbar: [Unterstützte Bluetooth Devices](devices/bms.md#bluetooth-devices)~~
