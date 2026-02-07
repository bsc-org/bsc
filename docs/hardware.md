## Hardwarevoraussetzungen
Um sämtliche Funktionen der Firmware nutzen zu können, wird die zum BSC-System gehörige Hardware benötigt. Eine detaillierte Beschreibung dieser Hardware, einschließlich des [Stromlaufplans](https://github.com/shining-man/bsc_hw/blob/main/circuit.pdf?raw=true), finden Sie in einem separaten [GitHub-Repository](https://github.com/shining-man/bsc_hw).

Wir empfehlen ausdrücklich die Verwendung der originalen BSC-Hardware. Diese wurde umfassend getestet und bietet galvanisch getrennte Anschlüsse, wodurch ein stabilerer Betrieb gewährleistet wird.  

Genauere Infos bezüglich der Hardware-Beschaffung haben wir für Sie [hier](first_steps.md/#beschaffung-der-hardware) zusammen gestellt.  
<br><br>
Für erste Tests kann alternativ ein ESP32-Dev-Kit verwenden. Beachten Sie jedoch, dass einige Funktionen eingeschränkt oder nicht getestet sind. Weitere Informationen finden Sie unter folgendem [Link](BSC_ohne_orig_hardware.md).

## Originales BSC-Mainboard
### Anschluss-Handling
Ein Techtalk über die Anschlussmöglichkeiten kann auf [Youtube](https://youtu.be/zwu_jJifkF4?si=2ktcM57JjkR39Dph) angesehen werden.

**Korrektes Kontaktieren der Schraubklemmen:**
Um eine fehlerfreie Installation zu gewährleisten, beachten Sie bitte folgende Hinweise zum Anschluss der Schraubklemmen:

  1. **Markierung von Pin 1:**  
  Jede Schraubklemme ist mit einer Ziffer "1" gekennzeichnet, die den Pin 1 der jeweiligen Klemme angibt. Diese Markierung dient als Referenz für den korrekten Anschluss.

  2. **Beschriftung der Funktionen:**  
  Neben der Markierung von Pin 1 befindet sich eine Beschriftung, die die jeweilige Funktion der einzelnen Kontaktstellen beschreibt. Lesen Sie diese sorgfältig, um die richtigen Verbindungen herzustellen.

  3. **Wichtige Sicherheitshinweise:**  
  Achten Sie unbedingt darauf, die Anschlüsse korrekt vorzunehmen!  
  Falsche Verbindungen können Schäden am BSC oder an extern angeschlossenen Komponenten verursachen.

  4. **Illustrationen und praktische Hinweise:**  
  Die in dieser Dokumentation enthaltenen Abbildungen dienen lediglich der Veranschaulichung. Überprüfen Sie daher immer die Markierungen und Beschriftungen auf Ihrer Platine, um die korrekten Anschlüsse sicherzustellen.

![](img/hardware/hw_stecker_9pol.png){ width="300" }
![](img/hardware/hw_stecker_6pol.png){ width="300" }

### Stromversorgung
Die jeweils zu nutzenden Pins finden Sie als "V IN1" für "+" und GND für "-" aufgedruckt auf Ihrer PCB. Der Betrieb der BSC-Hardware ist in der Standard-Auslieferung für 5V (>=1,5A) ausgelegt. Als stabile Lösung in Sachen Netzteile haben sich Hutschienen-Varianten der Firma Meanwell bewährt, welche man über den <a href="https://bsc-shop.com" target="_blank">BSC-Shop</a>
 erwerben kann.

Die Spannungsversorgung sollte redundant erfolgen, d.h. eine Ausfallsicherheit der Versorgung hergestellt werden. In diesem Fall wird, falls ein Netzteil keine Spannung mehr liefert, das Zweite einschreiten und die Platine ohne Unterbrechnung weiterversorgen. Somit könnte die Platine an ein direkt aus dem Akku versorgten DC/DC Netzteil und ein an das EVU-Netz angeschlossenen AC/DC Netzteil angeschlossen werden. Hierfür bietet das BSC zwei separate Eingänge an. Um zu definieren welche Spannungsquelle die Primärspannungsquelle ist, sollte diese ca. 0,2V höher eingestellt werden. Dann übernimmt die Stromversorgung des BSCs das Netzteil mit der höher eingestellten Spannung.

**Erhöhung der Spannungsversorgung:** 

Bei Bedarf ist es möglich die Spannungsversorgung auf mehr als 5V zu erweitern (z.B. 12V / 24V).  

Dabei sind folgende Bedingungen zu beachten:  
> Achtung, die Platinenkennzeichnung hat sich zwischen verschiedenen Hardwarerevisionen geändert. Angegeben sind diese folgend immer als HwRev < 2.5 / HwRev >= 2.5

* JP28 / R61 (Versorgungsspannung für die BSC-Komponenten):
    * Dieses ist im Normalfall gebrückt und muss für höhere Versorgungsspannungen größer 5V getrennt werden.  
      Das Bauteil ist durch seine Bedruckung auf der Rückseite der Platine, direkt neben den Lötanschlüssen von U19 zu finden.
* JP29 / R91 & JP25 (Relais-Spannungsversorgung):
    * Beim Einsatz von 5V Relais ist keine Änderung an diesen Jumpern notwendig
    * Wenn JP25 zur Schleiferkontaktierung der Relais genutzt wird, dürfen Spannungen nur bis 24V genutzt werden.
    * Wenn eine höhere Versorgungsspannung > 5V ohne Belastung von U19 für die Relais gewünscht ist
      * Hw-Rev < 2.5
         * Beim Einsatz von Relais höherer Spannung, die Verbindung 2-1 trennen und 3-2 mit dem Lötkolben überbrücken  
      Hinweis: Beim BSC V2.3 ist die Beschriftung der Jumper von JP29 falsch! Aufgedruckt ist 1 links, aber 1 ist auf der rechten Seite.
      * Hw-Rev >= 2.5
         * Beim Einsatz von Relais höherer Spannung, Widerstand R91 entfernen und Lötjumper JP25 setzen.
* Bei Versorgungsspannungen größer 19V können Bauteildefekte bei verpolten Anschliessen entstehen. Bitte achten Sie hier explizit die Anschlusspolarität um Probleme zu vermeiden.
* U19 ist für eine **höhere Versorgungsspannung** größer 5V mit einem DC-DC Wandler zu bestücken
    * Bis 34V Eingangsspannung werden im <a href="https://bsc-shop.com" target="_blank">BSC-Shop</a> passende DCDC-Module angeboten.
    * Zur rendundanten Spannungsversorgung, oder Spannungen über dem genannten Wert, werden getrennte 5V Netzteile im <a href="https://bsc-shop.com" target="_blank">BSC-Shop</a> angeboten.
    * Der viereckige Lötpunkt bei U19 ist der 5V Ausgang des DC/DC Wandlers. Hierbei unbedingt auf Polarität achten!
        * Wenn 5V Relais verwendet werden, bitte beachten, dass diese durch den Spannungsregler U19 mitversorgt werden, daher >=1A DC-DC Wandler verwenden
        * Hier ein Beispiel der U19 Bestückung:  
![](img/hardware/hw_bestueckung_u19.jpg){ width="400" }

### CAN/RS485
Alle Schnittstellen sind galvanisch getrennt und können somit ohne jegliche Adapter direkt an ein BMS (RS485 -> Serial0-10) oder Inverter (CAN) angeschlossen werden.  
Die Spannungs-Pegel der genannten Schnittstellen sind "genormt".  

### RS485 (BMS)
Einige übliche BMS-Typen können direkt über die RJ45-Buchse kontaktiert werden.  
Wenn Sie mehrere Geräte direkt mit RJ45 anschließen möchten, kann dies teilweise als DaisyChain, oder mit Hilfe des RJ45-Serial-Distributor aus dem <a href="https://bsc-shop.com" target="_blank">BSC-Shop</a> erfolgen.

### OneWire
An die OneWire-Schnittstelle können, ohne zusätzliche weitere Hardware, Temperatursensoren angeschlossen werden.  
Die dafür normalerweise notwendigen Pullup-Widerstände sind auf der BSC-Platine schon integriert.

### Temperaturmanagement
Das BSC benötigt eine leichte Thermik zur Kühlung der Platinen-Oberseite.  
Bitte packen Sie die Platine nicht unnötig ein und sorgen Sie für eine kontinuierliche Belüftung.

### Digitale Eingänge

#### Technische Spezifikation

- **Anzahl**: 4 Eingänge
- **Spannungsbereich**: 3-27VDC
- **Galvanische Trennung**: Ja, über Optokoppler
- **Triggerflanke**: Positiv (Low → High)
- **Invertierung**: Software-konfigurierbar

#### Elektrische Eigenschaften

**Galvanische Trennung**  

- Jeder Eingang ist galvanisch vom Rest der Schaltung getrennt  
- Eigener GND-Bezugspunkt für alle vier Eingänge  
- Gemeinsamer GND-Pin am Stecker für externes Netzteil oder Signalquelle  

**Versorgungsspannung**  

- Zu jedem Eingang steht eine getrennte 5V-Versorgung zur Verfügung  
- 5V-Ausgänge sind mit dem gemeinsamen GND verbunden  
- Direkte Speisung von Tastern möglich  

#### Software-Invertierung

- Positive Triggerflanke kann invertiert werden  
- Dann dient negative Flanke (High → Low) als Auslöser  
- Nützlich für inverse Logik oder NC-Kontakte  

#### Typische Anwendungen

**Taster abfragen**  

- 5V-Ausgang mit Taster verbinden  
- Tasterausgang mit DI-Eingang verbinden  
- Bei Tasterdruck: 5V am Eingang → Trigger  

**Relais-Kontakt abfragen**  

- 5V-Ausgang auf eine Seite des Relaiskontakts  
- Andere Seite mit DI-Eingang verbinden  
- Bei geschlossenem Kontakt: Trigger  

**Externe Spannung (z.B. 24VDC-Signale)**  

- Externes GND mit GND-Pin verbinden  
- Signalleitung direkt an DI-Eingang (3-27VDC)  

### Relais-Schaltausgänge

#### Übersicht

Der BSC verfügt über sechs elektromechanische Relais-Schaltausgänge (Rel1 bis Rel6), die für externe Schaltanwendungen genutzt werden können.  
Die Relais werden softwareseitig über konfigurierbare Trigger-Events gesteuert und bieten flexible Schalt- und Timing-Optionen.

#### Hardware-Spezifikation

##### Maximale Schaltwerte

- DC: 24 V / 3 A
- AC: 120 V / 3 A

##### Verfügbare Kontakte

**Relais 1-3 (alle Kontakte herausgeführt)**

- NO  (Normally Open / Schließer)
- NC  (Normally Closed / Öffner)
- COM (Common / Gemeinsamer Kontakt)

**Relais 4-6 (eingeschränkt herausgeführt)**

- NO  (Normally Open / Schließer)
- COM (Common / Gemeinsamer Kontakt)

Die NC-Kontakte der Relais 4-6 sind aus Gründen der externen Pin-Belegung nicht nach außen geführt.

#### Software-Konfiguration

Jedes Relais kann individuell über die BSC-Software konfiguriert werden.  
Die Ansteuerung erfolgt über ein oder mehrere wählbare Trigger-Events.

##### Konfigurierbare Parameter

**Impulsdauer [ms]**  
Definiert die Zeitdauer, für die das Relais nach einem Trigger-Event geschaltet bleibt.  
Bei einem Wert von 0 bleibt das Relais dauerhaft geschaltet, bis das Trigger-Event endet.

**Verzögerung nach Trigger-Event [s]**  
Ermöglicht eine zeitliche Verzögerung zwischen dem Auftreten des Trigger-Events und der tatsächlichen Relais-Schaltung.  
Dies kann für sequentielle Schaltabläufe oder zeitlich versetzte Aktionen genutzt werden.

**Invertierung**  
Kehrt die Schaltlogik um. Bei aktivierter Invertierung schaltet das Relais beim Trigger-Event ab statt ein (bzw. umgekehrt).

##### Trigger-Events

Die Relais können durch verschiedene System-Events ausgelöst werden, die in der Software konfiguriert werden.  
Mehrere Trigger können gleichzeitig einem Relais zugeordnet werden, wobei die Relais-Aktivierung erfolgt, wenn mindestens eines der konfigurierten Events eintritt.

#### Anwendungsbeispiele

**Lastabwurf bei kritischen Batterie-Zuständen**

- Trigger: Plausibility-Check (BMS-Daten außerhalb gültiger Bereiche)
- Verzögerung: 0 s
- Impulsdauer: 200 ms
- Invertierung: Ja
- Hinweis: Für das Schalten großer Akkupack-Ströme sollten externe DC-Schütze mit Steuereingang verwendet werden, die über das Relais angesteuert werden.

**Periodische Lüftersteuerung**

- Trigger: Temperatur-Schwelle
- Verzögerung: 0 s
- Impulsdauer: 60000 ms (1 min Nachlauf)
- Invertierung: Nein

**Alarm-Ausgabe mit Verzögerung**

- Trigger: Kritisches Batterie-Event
- Verzögerung: 10 s
- Impulsdauer: 500 ms (kurzer Impuls)
- Invertierung: Nein
- Hinweis: Bei einem kritischen Event sollte immer zuerst über Befehle der Inverter-Strombedarf heruntergefahren werden, bevor die harte Abschaltung über einen Schütz getriggert wird. Dies schont die Hardware im Fehlerfall.

#### Hinweise zur Verwendung

- Die Schaltkapazität der Relais ist durch verwendete Platinen-Layout begrenzt. Für höhere Spannungen/Leistungen sollten externe Schütze oder Halbleiter-Relais nachgeschaltet werden.
- Bei induktiven Lasten (Motoren, Spulen) wird der Einsatz von Freilaufdioden oder Snubber-Beschaltungen empfohlen.
- Die Relais 1-3 bieten durch die NC-Kontakte Fail-Safe-Möglichkeiten für sicherheitskritische Anwendungen.
- Bei Verwendung der Impulsdauer ist zu beachten, dass diese unabhängig von der Dauer des Trigger-Events abläuft.

### Wie trennt man Lötjumper
Hierzu müssen teilweise die in der Auslieferung gesetzten Lötjumper mechanisch entfernt werden.  
Dies geschieht am Besten mit einem "Dremel", der nur an der Oberfläche die Kupferschicht entfernt.  
Vorsicht! Es gibt weitere Kupferschichten innerhalb der Platine, diese dürfen natürlich nicht verletzt werden.  
![](img/hardware/hw_trennen_loetjumper.jpg){ width="600" }

### Jumper Konfiguration

#### J6 für den regulären Betrieb
Das Öffnen von Jumper J6 wird zur Programmierung einer unprogrammierten Platine benötigt.  
Für den normalen Betrieb ist dieser zu setzen.  
![](img/hardware/hw_jumper_j6.png){ width="400" }

#### J4 zur Programmierung
Das setzen von Jumper J4 wird zur Programmierung einer unprogrammierten Platine benötigt.  
Für den normalen Betrieb bleibt dieser offen.  
![](img/hardware/hw_jumper_j4.png){ width="400" }

#### Mittelabgriffe der Relais mit Vin verbinden
Die Mittelabgriffe (COM) der Relais können durch setzen der jeweiligen Jumper mit dem Vin der Platine verbunden werden.  
![](img/hardware/hw_relais_vin.png){ width="600" }

#### J14-J16 Aktivieren der Ausgänge
Diese Relais haben weitere Funktionalitäten, die derzeit nicht mit der Firmware abgebildet sind.  
Daher müssen die Jumper auf die blau markierten Positionen gesetzt werden.  
![](img/hardware/hw_relais_jumper_j14_j16.png){ width="600" }


## Lilygo T-CONNECT
![T-CONNECT](img/hardware/t-connect_connectors.jpg){ width="550" }

#### Steckerbelegung
**Serial 0-2 (RS485)**  
Pin 1: ---  
Pin 2: B  
Pin 3: A  
Pin 4: GND  

**CAN**   
Pin 1: ---  
Pin 2: H  
Pin 3: L  
Pin 4: GND  

#### Funktion der LEDs  
| LED            | Farbe          | Funktion                              |
|----------------|----------------|---------------------------------------|
|  System        | Blau           | System bootet                         |
|  System        | Grün - blinken | System ist fehlerfrei                 |
|  System        | Rot - blinken  | Einer der System-Task antwortet nicht |
|  Serial RX/TX  | Rot - blinken  | Kommunikation mit einem BMS           |
|  CAN RX/TX     | Rot - blinken  | Versenden einer CAN Nachricht         |

#### Belegung des Pin-Headers
Mit der Standard Firmware Version kann nur Onewire genutzt werden. Alle weiteren Funktionen (Relais, Digitaleingänge, I²C) können nur mit der Supporter Version genutzt werden.

| PIN | GPIO | Funktion         |
|-----|------|------------------|
|  1  |      | 5V               |
|  2  |      | 3.3V             |
|  3  |      | GND              |
|  4  |      | GND              |
|  5  |  46  | ---              |
|  6  |      | GND              |
|  7  |  12  | I²C SCL          |
|  8  |  11  | I²C SDA          |
|  9  |  14  | SE RX            |
| 10  |  13  | SE TX            |
| 11  |  47  | ---              |
| 12  |  21  | Onewire          |
| 13  |  45  | ---              |
| 14  |  48  | ---              |
| 15  |  36  | Digitaleingang 1 |
| 16  |  35  | Digitaleingang 2 |
| 17  |  38  | Digitaleingang 3 |
| 18  |  37  | Digitaleingang 4 |
| 19  |  40  | Relais 1         |
| 20  |  39  | Relais 2         |
| 21  |  42  | Relais 3         |
| 22  |  41  | Relais 4         |
| 23  |   1  | Relais 5         |
| 24  |   2  | Relais 6         |


## BSC Display
Das Display für den BSC wurde in ein [separates Projekt](https://github.com/shining-man/bsc_display) ausgegliedert in dem auch die Firmware zu finden ist.

### Unterstützes Display
Die Hardware-Version 3.3 des Displays wurde von uns getestet.  
Das Display ist über unseren Webshop unter <a href="https://bsc-shop.com" target="_blank">www.BSC-Shop.com</a> erhältlich.  
  
![](img/hardware/Display_SC01_3_5Zoll.png){ width="1000" }

### Anschluss an das BSC-Mainboard

**Empfohlene Methode: Mainboard-Display Connection Kit**

Für eine werkzeugfreie und sichere Montage ohne Löten und Verdrahtungsfehler empfehlen wir das <a href="https://bsc-shop.com/produkt/mainboard-display-connection-kit/" target="_blank">Mainboard-Display Connection Kit</a>.  
Das Kit enthält zwei Adapterplatinen und ein Flachbandkabel für die zuverlässige Verbindung zwischen Mainboard und Display.

**Vorteile:**

- Kein händisches Löten erforderlich
- Werkzeugfreie Montage durch Aufstecken
- Sichere Kontaktierung ohne Verdrahtungsfehler durch mechanische Kodierung
- Status-LED zur Funktionskontrolle
- Kompatibel mit allen Mainboard-Revisionen

---

**Alternative: Manueller Anschluss**

Der Anschluss kann alternativ manuell über den Extension-Port "J3" erfolgen:

* **Datenverbindung:** I²C-Bus über die Pins "SCL/SDA"
* **Spannungsversorgung:** 5V und GND am Extension-Port können für die Versorgung des Displays genutzt werden
![](img/hardware/hw_display_stecker_j3.png){ width="400" }
![](img/hardware/hw_display_stecker_j3_2.png){ width="200" }

### Pinout des Displays "WT32-SC01"
![](img/hardware/hw_pinout_display_wt32sc01.png){ width="700" }
