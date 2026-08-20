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
In diesem Abschnitt legen Sie fest, welche Hardware an welchem seriellen Port angeschlossen ist. Darüber hinaus ist es erforderlich, im Abschnitt ["Data devices"](#data-devices) zu konfigurieren, welche serielle Port welchem internen Daten-Device zugeordnet wird.

Detaillierte Informationen zur Einrichtung der Data Devices finden sie im Kapitel [Data devices](#data-devices).  

Diese Konfiguration stellt sicher, dass die angeschlossene Hardware korrekt erkannt wird und mit den entsprechenden internen Daten-Devices verknüpft werden kann.

```bsc-settings
version: v010
file: serial.json
profile: off
index: 1
section: UI_SECT_SERIAL_ALLGEMEIN
section: UI_SECT_SERIAL_FILTER
```

**Zuordnung bei der orginal BSC Hardware (Software => Hardware):**

* Serial 0 => U1
* Serial 1 => U2
* Serial 2 => U3

Serial 3 bis 10 sind nur mit angeschlossener Serial-Extension nutzbar.  

**Unterstützte Hardware (Serielle Schnittstellen)**  
In der Auswahl stehen aktuell folgende Gerätetypen zur Verfügung: nicht belegt, BPN (not use), JBD BMS, JK BMS, JK BMS V1.3 (only monitoring), JK Inverter BMS, Seplos BMS, Seplos V3 BMS, DALY BMS, Sylcin BMS, PACE RN150 BMS (Test), PACE PC200 BMS (RS485B), PACE PC200 V1 BMS (RS232), PACE PC200 V2 BMS (RS232), Pylontech, Felicity LUX-Y Serie, Daren BMS, Victron SmartShunt, NEEY RS485, Eletechsup NT4A08, Eletechsup NT48B16 und Eletechsup NT48C32.  
Eine Liste der unterstützten Hardware mit Details zur Adressierung ist unter folgendem Link verfügbar: [Unterstützte BMS](devices/bms.md#unterstutzte-bms)  
Die Liste der verfügbaren Hardware wird kontinuierlich erweitert, um den Anforderungen und Bedürfnissen unserer Nutzer gerecht zu werden.

**Anzahl Zellen**  
Gibt die Anzahl der in einer Batterie verbauten Einzelzellen an.  
Diese Einstellung ist z.B. wichtig, um die Werte im Dashboard korrekt darzustellen.  

### Filter

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

```bsc-settings
version: v010
file: bluetooth.json
profile: off
index: 1
```

Hier können bis zu 5 Bluetooth Devices festgelegt werden, von denen der Controller Daten holt.  
Dazu muss der Device-Typ und die MAC-Adresse (in Kleinbuchstaben) eingestellt werden.  

Der Controller scannt, sobald diese Konfigurationsseite aufgerufen ist, zyklisch nach neuen BT-Devices   
und zeigt die letzten 5 gefundenen am unteren Ende der Seite an.  

**Unterstützte Hardware**  
Eine Liste der unterstützten Hardware ist unter folgendem Link verfügbar: [Unterstützte Bluetooth Devices](devices/bms.md#bluetooth-devices)



## Data devices
Das **Data-Device-Mapping** dient der Zuordnung der Schnittstelle (z. B. einer seriellen Schnittstelle) zum im BSC verwendeten internen *Data-Device*.
Diese Zuordnung ist Grundlage für weitere Konfigurationen, z. B. in den Wechselrichter-Einstellungen.

```bsc-settings
version: v010
file: dataDeviceMapping.json
profile: off
section: UI_SECT_DATADEVICEMAPPING_DATA_DEVICE_MAPPING
```

Hierbei müssen folgende Parameter eingestellt werden:

  - **Schnittstelle**: Auswahl der Schnittstelle, an der das Data-Device angeschlossen ist (z. B. `Serial 0` oder `Bluetooth 0`; `Nicht belegt` deaktiviert das Data-Device). 
  - **Adresse**: Die eindeutige Adresse (0–16), die dem spezifischen Gerät zugewiesen wird oder vom Hersteller fest zugewiesen ist.
    Informationen, welche Adresse bei welchem BMS eingestellt werden muss, sind hier dokumentiert: [Unterstützte BMS – Adresskonfiguration](https://bsc-org.github.io/bsc/devices/bms/#unterstutzte-bms)  
    Der dortige Text sollte sorgfältig gelesen werden, da er beschreibt, **welche Adresse am BMS selbst** und **welche hier im Data-Device-Mapping des BSC** eingestellt werden muss.  
  - **Name** (optional): Ein benutzerdefinierter Name, der in den weiteren Einstellungen des Parameters angezeigt wird. Dieser Name wird außerdem für den MQTT-Topic des jeweiligen Devices verwendet.

    !!! Hinweis
        Der Name darf keine # und + Zeichen enthalten!

!!! note "Hinweis"
    In den Auswahllisten anderer Einstellungsseiten (z. B. Datenquelle, Alarmregeln) erscheinen nur die **konfigurierten** Data-Devices, also diejenigen mit zugewiesener Schnittstelle.

Falls mehrere Geräte an einer seriellen Schnittstelle angeschlossen sind und das BMS (Battery Management System) die Verbindung im Daisy-Chain-Modus unterstützt, ist es erforderlich, für jedes Gerät die korrekte Adresse zu definieren. Nur so kann eine eindeutige Zuordnung und eine fehlerfreie Kommunikation zwischen dem BMS und den Geräten sichergestellt werden.

!!! note "Hinweis"
    Die korrekte Konfiguration der Data Device Mappings ist essenziell, um eine störungsfreie Funktionalität zu gewährleisten. Beachten Sie die Adressierungsregeln Ihres BMS-Systems.


### Value Adjustment

```bsc-settings
version: v010
file: dataDeviceMapping.json
profile: off
section: UI_SECT_DATADEVICEMAPPING_VALUE_ADJUSTMENTS
```

Das "Value Adjustment" ermöglicht es, dem Wechselrichter abhängig von der Zellspannung einen angepassten State of Charge (SoC) zu übermitteln. Die Einstellungen werden **pro Data-Device** vorgenommen.

!!! note "Hinweis zur Supporter-Firmware"
    Das Value Adjustment ist ebenfalls Bestandteil der **Supporter-Firmware**. Weitere Informationen: [Supporter](supporter.md).

Folgende Optionen stehen zur Verfügung:

- **SoC linearisieren**  
  Ist diese Option aktiviert, wird der SoC linear zwischen den beiden Spannungswerten *Cellvoltage for SoC 0%* und *Cellvoltage for SoC 100%* berechnet. Dazu müssen beide Werte gesetzt sein und der 100-%-Wert größer als der 0-%-Wert sein.

- **SoC 100% trigger mode**  
  Legt fest, welche Zellen den Schwellwert erreichen müssen, damit der SoC auf 100 % gesetzt wird:
    - **Eine Zelle erreicht Schwellwert** – Es genügt, wenn die höchste Zellspannung den Wert *Cellvoltage for SoC 100%* erreicht.
    - **Alle Zellen erreichen Schwellwert** – Der SoC wird erst auf 100 % gesetzt, wenn alle konfigurierten Zellen den Wert *Cellvoltage for SoC 100%* erreicht haben.

- **Cellvoltage for SoC 100%** (in mV)  
  Der SoC-Wert wird erst dann auf 100 % gesetzt, wenn die eingestellte Zellspannung erreicht ist.  
  Bis dahin wird der SoC-Wert des zugeordneten Data-Devices übernommen und maximal mit 99 % angezeigt.  
  Ein Wert von `0` deaktiviert die Funktion.  

- **Cellvoltage for SoC 0%** (in mV)  
  Funktioniert analog zu *Cellvoltage for SoC 100%*, jedoch für den unteren Grenzwert.  
  Der SoC wird erst auf 0 % gesetzt, wenn die definierte Zellspannung erreicht oder unterschritten ist.  
  Ein Wert von `0` deaktiviert die Funktion.  

**Verhalten ohne aktiviertes „SoC linearisieren“:**  

- Ist nur *Cellvoltage for SoC 100%* gesetzt, wird der SoC bei Erreichen der Schwelle auf 100 % gesetzt; fällt die Zellspannung wieder darunter, wird der SoC-Wert des BMS übernommen.
- Ist nur *Cellvoltage for SoC 0%* gesetzt, gilt das Verhalten entsprechend für die untere Schwelle.
- Sind beide Werte gesetzt, werden die beiden Schwellen unabhängig voneinander angewendet (fester 100-%- bzw. 0-%-Wert ab Schwelle).

**Beispiel (mit „SoC linearisieren“):**  

- Cellvoltage für SoC 100%: 3,5 V  
- Cellvoltage für SoC 0%: 2,9 V  
- Bei ≥ 3,5 V → SoC = 100 %  
- Bei ≤ 2,9 V → SoC = 0 %  
- Zwischen 2,9 V und 3,5 V → SoC linear berechnet  

Die lineare Berechnung ist besonders nützlich für BMS-Systeme, die keinen eigenen SoC-Wert bereitstellen, da der SoC in Abhängigkeit von den Zellspannungen automatisch ermittelt wird.

!!! danger "Wichtiger Hinweis"
    Stellen Sie sicher, dass die eingetragenen Zellspannungen den Spezifikationen des verwendeten Batteriesystems entsprechen, um eine optimale Funktion und Sicherheit zu gewährleisten.
