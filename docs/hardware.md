## Hardwarevoraussetzungen
Um sämtliche Funktionen der Firmware nutzen zu können, wird die zum BSC-System gehörige Hardware benötigt. Eine detaillierte Beschreibung dieser Hardware, einschließlich des [Stromlaufplans](https://github.com/shining-man/bsc_hw/blob/main/circuit.pdf?raw=true), finden Sie in einem separaten [GitHub-Repository](https://github.com/shining-man/bsc_hw).

Wir empfehlen ausdrücklich die Verwendung der originalen BSC-Hardware. Diese wurde umfassend getestet und bietet galvanisch getrennte Anschlüsse, wodurch ein stabilerer Betrieb gewährleistet wird.

Falls die originale BSC-Hardware nicht verfügbar ist, können Sie für erste Tests alternativ ein ESP32-Dev-Kit verwenden. Beachten Sie jedoch, dass einige Funktionen möglicherweise eingeschränkt oder nicht getestet sind. Weitere Informationen finden Sie unter folgendem [Link](BSC_ohne_orig_hardware.md).

## Anschlüsse
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

## Stromversorgung
Die jeweils zu nutzenden Pins finden Sie als "V IN1" für "+" und GND für "-" aufgedruckt auf Ihrer PCB. Der Betrieb der BSC-Hardware ist in der Standard-Auslieferung für 5V (>=1,5A) ausgelegt. Als stabile Lösung in Sachen Netzteile haben sich Hutschienen-Varianten der Firma Meanwell bewährt, welche man über den BSC-Shop erwerben kann.

Die Spannungsversorgung sollte redundant erfolgen, d.h. eine Ausfallsicherheit der Versorgung hergestellt werden. In diesem Fall wird, falls ein Netzteil keine Spannung mehr liefert, das Zweite einschreiten und die Platine ohne Unterbrechnung weiterversorgen. Somit könnte die Platine an ein direkt aus dem Akku versorgten DC/DC Netzteil und ein an das EVU-Netz angeschlossenen AC/DC Netzteil angeschlossen werden. Hierfür bietet das BSC zwei separate Eingänge an. Um zu definieren welche Spannungsquelle die Primärspannungsquelle ist, sollte diese ca. 0,2V höher eingestellt werden. Dann übernimmt die Stromversorgung des BSCs das Netzteil mit der höher eingestellten Spannung.

**Erhöhung der Spannungsversorgung:** 

Bei Bedarf ist es möglich die Spannungsversorgung auf mehr als 5V zu erweitern (z.B. 12V / 24V). Dabei sind folgende Bedingungen zu beachten (Achtung, die Platinenkennzeichnung hat sich zwischen verschiedenen Hardwarerevisionen geändert. Angegeben sind diese wie folgt immer als HwRev < 2.5 / HwRev >= 2.5):

* JP28 / R61 (Versorgungsspannung für die BSC-Komponenten): ist im Normalfall gebrückt und muss für höhere Versorgungsspannungen größer 5V getrennt werden.  
Das Bauteil ist durch seine Bedruckung auf der Rückseite der Platine, direkt neben den Lötanschlüssen von U19 zu finden.
* JP29 / R91 & JP25 (Relais-Spannungsversorgung):
  * Beim Einsatz von 5V Relais ist keine Änderung an diesen Jumpern notwendig
  * Wenn eine höhere Versorgungsspannung > 5V ohne Belastung von U19 für die Relais gewünscht ist
    * Hw-Rev < 2.5
      * Beim Einsatz von Relais höherer Spannung, die Verbindung 2-1 trennen und 3-2 mit dem Lötkolben überbrücken  
      Hinweis: Beim BSC V2.3 ist die Beschriftung der Jumper von JP29 falsch! Aufgedruckt ist 1 links, aber 1 ist auf der rechten Seite.
    * Hw-Rev >= 2.5
      * Beim Einsatz von Relais höherer Spannung, Widerstand R91 entfernen und Lötjumper JP25 setzen.
* U19 ist für eine **höhere Versorgungsspannung** größer 5V mit einem DC-DC Wandler zu bestücken 
  * bis 27V Eingangsspannung werden im BSC-Shop passende DCDC-Module angeboten.
* ansonsten ist ein passender DC-DC Wandler abhängig von der Eingangsspannung zu verwenden
* Der viereckige Lötpunkt bei U19 ist der 5V Ausgang des DC/DC Wandlers. Hierbei unbedingt auf Polarität achten!
  * Wenn 5V Relais verwendet werden, bitte beachten, dass diese durch den Spannungsregler U19 mitversorgt werden, daher >=1A DC-DC Wandler verwenden
  * Hier ein Beispiel der U19 Bestückung:  
![](img/hardware/hw_bestueckung_u19.jpg){ width="400" }

## CAN/RS485
Alle Schnittstellen sind galvanisch getrennt und können somit ohne jegliche Adapter direkt an ein BMS (RS485 -> Serial0-10) oder Inverter (CAN) angeschlossen werden.  
Die Spannungs-Pegel der genannten Schnittstellen sind "genormt".  
Ein Seplos-BMS kann direkt über die RJ45-Buchse kontaktiert werden.

## OneWire
An die OneWire-Schnittstelle können, ohne zusätzliche weitere Hardware, Temperatursensoren angeschlossen werden.  
Die dafür normalerweise notwendigen Pullup-Widerstände sind auf der BSC-Platine schon integriert.


# Temperaturmanagement
Das BSC benötigt eine leichte Thermik zur Kühlung der Platinen-Oberseite.  
Bitte packen Sie die Platine nicht unnötig ein und sorgen Sie für eine kontinuierliche Belüftung.


# Wie trennt man Lötjumper
Hierzu müssen teilweise die in der Auslieferung gesetzten Lötjumper mechanisch entfernt werden.  
Dies geschieht am Besten mit einem "Dremel", der nur an der Oberfläche die Kupferschicht entfernt.  
Vorsicht! Es gibt weitere Kupferschichten innerhalb der Platine, diese dürfen natürlich nicht verletzt werden.  
![](img/hardware/hw_trennen_loetjumper.jpg){ width="600" }

# Jumper Konfiguration

## J6 für den regulären Betrieb
Das Öffnen von Jumper J6 wird zur Programmierung einer unprogrammierten Platine benötigt.  
Für den normalen Betrieb ist dieser zu setzen.  
![](img/hardware/hw_jumper_j6.png){ width="400" }

## J4 zur Programmierung
Das setzen von Jumper J4 wird zur Programmierung einer unprogrammierten Platine benötigt.  
Für den normalen Betrieb bleibt dieser offen.  
![](img/hardware/hw_jumper_j4.png){ width="400" }

## Mittelabgriffe der Relais mit Vin verbinden
Die Mittelabgriffe (COM) der Relais können durch setzen der jeweiligen Jumper mit dem Vin der Platine verbunden werden.  
![](img/hardware/hw_relais_vin.png){ width="600" }

## J14-J16 Aktivieren der Ausgänge
Diese Relais haben weitere Funktionalitäten, die derzeit nicht mit der Firmware abgebildet sind.  
Daher müssen die Jumper auf die blau markierten Positionen gesetzt werden.  
![](img/hardware/hw_relais_jumper_j14_j16.png){ width="600" }

# BSC Display
Das Display für den BSC wurde in ein [separates Projekt](https://github.com/shining-man/bsc_display) ausgegliedert in dem auch die Firmware zu finden ist.

## Unterstützes Display
Hardware-Version 3.3 des Displays wurde getestet.  
Erhältlich beispielweise über Aliexpress von verschiedenen Versendern.  
![](img/hardware/hw_display.png){ width="500" }

## Anschluss an das BSC-Mainboard
Der Anschluss dessen erfolgt über den Extension-Port "J3":

* Die Datenverbindung über den hier kontaktierbaren I²C-Bus der Pins "SCL/SDA", welche 1:1 anzuschließen sind.
* Eine 5V Spannungsversorgung für das Display ist auch abgreifbar. Diese muss, zusammen mit GND, mit dem dazu passenden Anschluss Ihres Displays verbunden werden.
![](img/hardware/hw_display_stecker_j3.png){ width="400" }
![](img/hardware/hw_display_stecker_j3_2.png){ width="200" }

## Pinout des Displays "WT32-SC01"
![](img/hardware/hw_pinout_display_wt32sc01.png){ width="700" }
