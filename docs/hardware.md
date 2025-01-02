# Hardwarevoraussetzungen
Um alle Funktionen der Firmware nutzen zu können ist die zum BSC zugehörige Hardware erforderlich. Eine Beschreibung der Hardware ist auf einem weiteren [Github-Repo](https://github.com/shining-man/bsc_hw) inklusive [Stromlaufplan](https://github.com/shining-man/bsc_hw/blob/main/circuit.pdf?raw=true "Stromlaufplan") zu finden. 

Wir empfehlen, dass die originale BSC Hardware benutzt wird. Damit werden alle Funktionen getestet und Anschlüsse sind galvanisch getrennt, und somit ist ein stabilerer Betrieb möglich.
Alternativ zur BSC Hardware kann zum erstmaligen Testen auch ein ESP32-Dev-Kit genutzt werden.
Weitere Infos finden Sie über folgenden [Link](../BSC_ohne_orig_hardware).

# Anschlüsse
Ein Techtalk über die Anschlussmöglichkeiten kann auf [Youtube](https://youtu.be/zwu_jJifkF4?si=2ktcM57JjkR39Dph) angesehen werden.

**Korrektes Kontaktieren der Schraubklemmen:**
Alle Schraubklemmen haben eine Markierung mit der Ziffer "1", welche den Pin 1 der entsprechenden Klemme kennzeichnet.
Die daneben stehende Beschriftung repräsentiert die jeweiligen Funktionen der einzelnen Kontaktstellen.
Bitte achten Sie unbedingt auf richtiges Anschließen, da sonst der BSC oder extern angeschlossene Komponenten zu Schaden kommen können.
Die folgenden Bilder dienen nur der Illustration, bitte schauen Sie auf Ihrer Platine nach der jeweiligen Stecker-Markierung.

<img src="../img/hardware/hw_stecker_9pol.png" height="250">
<img src="../img/hardware/hw_stecker_6pol.png" height="250">


## Stromversorgung
Die jeweils zu nutzenden Pins finden Sie als "V IN1" für "+" und GND für "-" aufgedruckt auf Ihrer PCB. Der Betrieb der BSC-Hardware ist in der Standard-Auslieferung für 5V (>=1,5A) ausgelegt. Als stabile Lösung in Sachen Netzteile haben sich Hutschienen-Typen der Firma Meanwell bewährt (z.B. SDR- & DDR-Typen).

Die Spannungsversorgung sollte redundant erfolgen, d.h. eine Ausfallsicherheit der Versorgung hergestellt werden. In diesem Fall wird, falls ein Netzteil keine Spannung mehr liefert, das Zweite einschreiten und die Platine ohne Unterbrechnung weiterversorgen. Somit könnte die Platine an ein direkt aus dem Akku versorgten DC/DC Netzteil und ein an das EVU-Netz angeschlossenen AC/DC Netzteil angeschlossen werden. Hierfür bietet das BSC zwei separate Eingänge an. Um zu definieren welche Spannungsquelle die Primärspannungsquelle ist, sollte diese 0,1V/0,2V höher eingestellt werden. Dann übernimmt die Stromversorgung des BSCs das Netzteil mit der höher eingestellten Spannung.

**Erhöhung der Spannungsversorgung:** 

Bei Bedarf ist es möglich die Spannungsversorgung auf mehr als 5V zu erweitern (z.B. 12V / 24V). Dabei sind folgende Bedingungen zu beachten (Achtung, die Platinenkennzeichnung hat sich zwischen verschiedenen Hardwarerevisionen geändert. Angegeben sind diese wie folgt immer als HwRev < 2.5 / HwRev >= 2.5):

* JP28 / R61 (Versorgungsspannung für die BSC-Komponenten): ist im Normalfall gebrückt und muss für höhere Versorgungsspannungen größer 5V getrennt werden
* JP29 / R91 & JP25 (Relais-Spannungsversorgung):
  * Beim Einsatz von 5V Relais ist keine Änderung an diesen Jumpern notwendig
  * Wenn eine höhere Versorgungsspannung > 5V ohne Belastung von U19 für die Relais gewünscht ist
    * Hw-Rev < 2.5
      * Beim Einsatz von Relais höherer Spannung, die Verbindung 2-1 trennen und 3-2 mit dem Lötkolben überbrücken<br>
      Hinweis: Beim BSC V2.3 ist die Beschriftung der Jumper von JP29 falsch! Aufgedruckt ist 1 links, aber 1 ist auf der rechten Seite.
    * Hw-Rev >= 2.5
      * Beim Einsatz von Relais höherer Spannung, Widerstand R91 entfernen und Lötjumper JP25 setzen.
* U19 ist für eine **höhere Versorgungsspannung** größer 5V mit einem DC-DC Wandler zu bestücken 
  * bis 27V Eingangsspannung kann z.B. "LMO78_05-1.0" oder ein "Murata OKI-78SR-5/1.5-W36-C" verwendet werden. 
* ansonsten ist ein passender DC-DC Wandler abhängig von der Eingangsspannung zu verwenden
* Der viereckige Lötpunkt bei U19 ist der 5V Ausgang des DC/DC Wandlers. Auf Polarität achten!
  * Wenn 5V Relais verwendet werden, bitte beachten, dass diese durch den Spannungsregler U19 mitversorgt werden, daher >=1A DC-DC Wandler verwenden
  * Hier ein Beispiel der U19 Bestückung:<br>
_<img src="../img/hardware/hw_bestueckung_u19.png" width="600">



## CAN/RS485
Alle Schnittstellen sind galvanisch getrennt und können somit ohne jegliche Adapter direkt an ein BMS (RS485 -> Serial0-10) oder Inverter (CAN) angeschlossen werden.<br>
Die Spannungs-Pegel der genannten Schnittstellen sind "genormt".<br>
Ein Seplos-BMS kann direkt über die RJ45-Buchse kontaktiert werden.

## OneWire
An die OneWire-Schnittstelle können, ohne zusätzliche weitere Hardware, Temperatursensoren angeschlossen werden.<br>
Die dafür normalerweise notwendigen Pullup-Widerstände sind auf der BSC-Platine schon integriert.


# Temperaturmanagement
Das BSC benötigt eine leichte Thermik zur Kühlung der Platinen-Oberseite.<br>
Bitte packen Sie die Platine nicht unnötig ein und sorgen Sie für eine kontinuierliche Belüftung.


# Wie trennt man Lötjumper
Hierzu müssen teilweise die in der Auslieferung gesetzten Lötjumper mechanisch entfernt werden.<br>
Dies geschieht am Besten mit einem "Dremel", der nur an der Oberfläche die Kupferschicht entfernt.<br>
Vorsicht! Es gibt weitere Kupferschichten innerhalb der Platine, diese dürfen natürlich nicht verletzt werden.<br>
<img src="../img/hardware/hw_trennen_loetjumper.jpg" width="600">

# Jumper Konfiguration

## J6 für den regulären Betrieb
Das Öffnen von Jumper J6 wird zur Programmierung einer unprogrammierten Platine benötigt.<br>
Für den normalen Betrieb ist dieser zu setzen.<br>
<img src="../img/hardware/hw_jumper_j6.png" height="400">

## J4 zur Programmierung
Das setzen von Jumper J4 wird zur Programmierung einer unprogrammierten Platine benötigt.<br>
Für den normalen Betrieb bleibt dieser offen.<br>
<img src="../img/hardware/hw_jumper_j4.png" height="400">

## Mittelabgriffe der Relais mit Vin verbinden
Die Mittelabgriffe (COM) der Relais können durch setzen der jeweiligen Jumper mit dem Vin der Platine verbunden werden.<br>
<img src="../img/hardware/hw_relais_vin.png" width="600">

## J14-J16 Aktivieren der Ausgänge
Diese Relais haben weitere Funktionalitäten, die derzeit nicht mit der Firmware abgebildet sind.<br>
Daher müssen die Jumper auf die blau markierten Positionen gesetzt werden.<br>
<img src="../img/hardware/hw_relais_jumper_j14_j16.png" width="600">

# BSC Display
Das Display für den BSC wurde in ein [separates Projekt](https://github.com/shining-man/bsc_display) ausgegliedert in dem auch die Firmware zu finden ist.

## Unterstützes Display
Hardware-Version 3.3 des Displays wurde getestet.<br>
Erhältlich beispielweise über Aliexpress von verschiedenen Versendern.<br>
<img src="../img/hardware/hw_display.png" width="500">

## Anschluss an das BSC-Mainboard
Der Anschluss dessen erfolgt über den Extension-Port "J3":

* Die Datenverbindung über den hier kontaktierbaren I²C-Bus der Pins "SCL/SDA", welche 1:1 anzuschließen sind.
* Eine 5V Spannungsversorgung für das Display ist auch abgreifbar. Diese muss, zusammen mit GND, mit dem dazu passenden Anschluss Ihres Displays verbunden werden.
<img src="../img/hardware/hw_display_stecker_j3.png" height="400"> 
<img src="../img/hardware/hw_display_stecker_j3_2.png" height="400">

## Pinout des Displays "WT32-SC01"<br>
<img src="../img/hardware/hw_pinout_display_wt32sc01.png" width="700">