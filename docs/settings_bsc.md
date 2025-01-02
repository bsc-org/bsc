## Allgemeines
Es gibt zwei Version des WebUI's. Das Classic WebUI und das WebUI V2. <br>
Im folgenden ist das WebUI V2 abgebildet, welches so aktuell nicht zur Verfügung steht. 

### Allgemeine Informationen zur Bedienung
**Speichern der Einstellungen**<br>
Das Speichern unterscheidet sich in den WebUI's.<br>

Classic WebUI:<br>
Die geänderten Einstellungen können mit dem „S"-Button, der in jeder Zeile der Einstellungen ist, gespeichert werden.
Zu beachten ist, dass auch nur die Einstellung in der jeweiligen Zeile des „S"-Button gespeichert wird.<br>

WebUI V2<br>
Hier können alle Änderungen über den "Save"-Button in der Headline gespeichert werden. Es muss nicht jeder Änderung einzeln gespeichert werden.

### Funktionsprinzip der Überwachungsfunktionen
Für jeden zu überwachenden Wert, dies kann z.B. eine Temperatur, eine Spannung, ... sein, kann ein Trigger eingestellt werden, der im Gefahrenfall aktiv wird. Dieser Trigger löst erst einmal keine weitere Aktion aus. Es kann jetzt aber wiederum eingestellt werden, dass das Relais x schalten soll, wenn Trigger x aktiv wird, oder dass der Wechselrichter seinen Ladestrom auf 0 A einstellen soll, wenn Trigger x aktiv wird. Durch diese Logik lässt sich eine flexible Kombination von Trigger-Gebern und Trigger-Nehmern zu. Maximal stehen 10 interne Trigger zur Verfügung.<br>
<br>
Wenn mehrere Quellen auf einen Trigger wirken, wird dieser aktiv geschaltet (high) sobald eine einzelne der verbundenen Quellen aktiv wird.<br>
Deaktiv (low) wird dieser Trigger erst, wenn alle angeschlossenen Quellen wieder deaktiv sind.<br>
Dies ist vor allem bei Verwendung von vTriggern wichtig zu verstehen, da diese durch eine Automation wieder deaktiv geschaltet werden müssen, um die Trigger-Funktionalität wieder frei zu geben.<br>

Ein Beispiel hierzu:<br>
Wenn die Temperatursensoren 2 oder 3 eine Temperatur von 30 °C überschreiten, dann soll Trigger 1 aktiv werden. Für das Relais 1 wurde eingestellt, dass es schaltet, wenn Trigger 1 aktiv wird um einen Lüfter zu aktivieren. Gleichzeitig kann ich aber auch einstellen, dass bei Trigger 1 der Wechselrichter seinen Ladestrom reduziert, da er für die hohe Wärmebelastung verantwortlich ist.

## Dashboard
Nach dem Aufrufen der Webseite über das integrierte WLAN-Modul (IP oder bsc.info) kommt als Startseite das Dashboard mit ein paar grundlegenden Informationen.<br>
Über das seitliche Menü kann man zu den jeweiligen Funktionen navigieren.

<img src="../img/settings/settings_dashboard.png" width="950"><br><br>

| Kachel  | Beschreibung |
| ------------- | ------------- |
| System  | Solange auf der Kachel „running" steht, laufen die einzelnen Tasks fehlerfrei. <br>Sollte ein interner Task seine vorgegebene maximale Zykluszeit überschreiten <br>kommt hier ein Fehler mit der zugehörigen Tasknummer.  |
| MQTT  | Gibt an, ob eine Verbindung zu dem MQTT Broker besteht  |
| Free Heap  | Zeigt den freien Heap und den jemals niedrigsten freien Heap seit Systemstart an  |
| BT-Devices| Status der angeschlossenen BT-Geräte wie z.B. ein Neey Balancer; "c" bedeutet Connected|
| Trigger | Status der zehn möglichen Trigger; 0=kein Trigger, 1=Trigger |

## Livedaten
<img src="../img/settings/settings_livedaten.png" width="950"><br><br>
"FET state" beschreibt den aktuellen FET Lade-/Entladezustand.<br>

<img src="../img/settings/settings_fet_state.png" width="300">

## System
<img src="../img/settings/settings_system.png" width="950">

Hier findet man alle System-Internen Einstellmöglichkeiten, wie z.B. Benutzernamen und Passwörter zu den WLAN und MQTT Logins.<br>
Bitte beachten Sie, dass das Tilde-Zeichen (~) derzeit als Passwort-Zeichen <u>nicht unterstützt</u> wird.<br>
<br>
Sobald MQTT aktiviert ist und die zugehörige IP-Adresse und der Port eingestellt ist, sendet der BSC zyklisch die Daten an den MQTT-Broker.<br>
<br>
Falls Sie einen externen NTP-Server verwenden und mit der Zeitsynchronisierung Probleme haben, können Sie auch den Router Ihres Netzwerkes hierzu verwenden - Dies funktioniert oft stabiler.<br>
Am Beispiel einer AVM FritzBox können Sie den Zeitserver im Menü unter Heimnetz/Netzwerk/Netzwerkeinstellungen aktivieren.<br>
Als Zeitserver können Sie beispielsweise folgendes definieren: "ntp1.t-online.de; 2.europe.pool.ntp.org".<br>
Im BSC muss dann dessen IP-Adresse angegeben werden.

## Schnittstellen
In den Schnittstellen Einstellungen wird eingestellt was an welcher Schnittstelle angeschlossen ist.<br>
Hier wird **nicht** eingestellt was z.B. mit den Daten von einem BMS oder Balancer passieren soll, oder wann der Relais-Ausgang 
schalten soll. Dies wird dann bei den Einstellungen zu den Alarmregeln oder dem Wechselrichter gemacht.

### Relaisausgänge
<img src="../img/settings/settings_relais.png" width="950"><br>
Hier können die grundlegenden Einstellungen zu den Relaisausgängen vorgenommen werden.

* **Auslösung bei**
<br>Hier wird angegeben bei welchem kommenden Trigger das Relais schalten soll
* **Auslöseverhalten**
    * Permanent: Das Relais bleibt angezogen, solange der Trigger ansteht
    * Impuls: Das Relais schaltet für eine Dauer von x ms. Die Impulsdauer wird unter "Impulsdauer" eingestellt.
* **Impulsdauer**
<br>Hier wird die Impulsdauer eingestellt, wenn bei dem Auslöseverhalten "Impuls" eingestellt wurde.
* **Verzögerung**
<br>Gibt an um wie viel Sekunden das Schalten des Relais bei einem kommenden Trigger verzögert werden soll.

Die Logik mit den Triggern zieht sich durch das gesamte System. Es gibt Trigger-Geber, z.B. die Digitaleingänge<br>und es gibt Trigger-Nehmer, z.B. die Relaisausgänge.

### Digitaleingänge
<img src="../img/settings/settings_di.png" width="950"><br>
Hier können die grundlegenden Einstellungen zu den Digitaleingängen vorgenommen werden.

* **Eingang invertieren**
<br>Hier kann der Eingang invertiert werden
* **Weiterleiten an**
<br>Hier kann der Trigger eingestellt werden, auf den der Eingang geht. <br>Wenn der Eingang High wird, dann wird der hier eingestellte Trigger aktiv.<br>Ist der Eingang invertiert, dann wird bei einem Low am Eingang der Trigger aktiv.
 
### Serial
<img src="../img/settings/settings_serial.png" width="950"><br>
Hier wird erst einmal nur eingestellt, was an welchem seriellen Port angeschlossen ist.<br>
Die Daten stehen dem System jetzt intern zur Verfügung und es kann z.B. bei den Alarmregeln darauf zugegriffen werden.<br>

**Zuordnung (Software => Hardware):**

* Serial 0 => U1
* Serial 1 => U2
* Serial 2 => U3

Alle weiteren dargestellten Schnittstellen sind nur mit angeschlossener Serial-Extension nutzbar.<br>

**Unterstütze Hardware<br>**
<img src="../img/settings/settings_unterstuetze_bms.png" width="400"><br>

#### Value Adjustment für SoC-Übermittlung an den Wechselrichter
<img src="../img/settings/settings_value_adjustment_soc.png" width="500"><br>
Der "Value Adjustment" ermöglicht es, dem Wechselrichter abhängig von der Zellspannung einen angepassten State of Charge (SoC) zu übermitteln. Dabei stehen zwei Betriebsmodi zur Verfügung, die unterschiedliche Anforderungen und Verhaltensweisen abdecken.<br>

##### Betriebsmodus 1: Feste SoC-Übermittlung bei definierter Zellspannung
In diesem Modus wird die Zellspannung definiert, bei der der Wechselrichter einen SoC von 100% erhalten soll. Wenn die Zellspannung den eingestellten Wert erreicht oder überschreitet, wird der SoC von 100% an den Wechselrichter übermittelt. Sobald die Zellspannung unter den eingestellten Wert fällt, wird der SoC wieder vom Batterie-Management-System (BMS) an den Wechselrichter gesendet.<br>

**Hinweis:** Für diesen Modus muss das Feld "Cellvoltage for SoC 0%" leer bleiben. Dies stellt sicher, dass nur die obere Schwelle (für 100% SoC) berücksichtigt wird und die Berechnung des SoC allein durch das BMS erfolgt, wenn die Zellspannung unter die festgelegte Schwelle sinkt.<br>

**Beispiel:**<br>
- Cellvoltage für SoC 100%: 3,5 V
  - Bei einer Zellspannung von 3,5 V oder höher wird dem Wechselrichter ein SoC von 100% übermittelt.
  - Fällt die Zellspannung unter 3,5 V, erfolgt die SoC-Übermittlung wieder regulär durch das BMS.

##### Betriebsmodus 2: Lineare SoC-Berechnung zwischen zwei Zellspannungsschwellen
In diesem Modus werden zwei Zellspannungsschwellen definiert: Eine obere Schwelle für 100% SoC und eine untere Schwelle für 0% SoC. Wenn die Zellspannung die obere Schwelle erreicht oder überschreitet, wird dem Wechselrichter ein SoC von 100% übermittelt. Erreicht oder unterschreitet die Zellspannung die untere Schwelle, wird ein SoC von 0% übermittelt. Für Zellspannungen zwischen diesen beiden Werten wird der SoC linear berechnet und entsprechend an den Wechselrichter gesendet.<br>

**Beispiel:**
- Cellvoltage für SoC 100%: 3,5 V
- Cellvoltage für SoC 0%: 2,9 V
  - Bei einer Zellspannung von 3,5 V oder höher wird dem Wechselrichter ein SoC von 100% übermittelt.
  - Bei einer Zellspannung von 2,9 V oder niedriger wird dem Wechselrichter ein SoC von 0% übermittelt.
  - Bei Zellspannungen zwischen 2,9 V und 3,5 V wird der SoC linear berechnet und an den Wechselrichter übermittelt.

Dieser Modus ist besonders nützlich für BMS-Systeme, die keinen eigenen SoC melden, da der SoC in Abhängigkeit von den Zellspannungen automatisch ermittelt wird.<br>

**Wichtiger Hinweis:** Stellen Sie sicher, dass die eingetragenen Zellspannungen den Spezifikationen des verwendeten Batteriesystems entsprechen, um eine optimale Funktion und Sicherheit zu gewährleisten.

### Onewire
<img src="../img/settings/settings_onewire1_1.png" width="950"><br>
Hier werden die Adressen der Onewire Temperatursensoren festgelegt.<br><br>

Der Controller scannt, sobald diese Onewire- Konfigurationsseite aufgerufen ist, zyklisch den Bus nach Onewire-Devices und zeigt diese am  unteren Ende der Seite an.<br>
Die Fett dargestellten Devices am unteren Rand sind neue Devices, die noch nicht in der Onewire-Konfigurationsseite gespeichert sind.<br>
Dadurch lassen sich neu angeschlossene Sensoren leichter identifizieren.<br>

<img src="../img/settings/settings_onewire1_2.png" width="950"><br>

### Onewire II
<img src="../img/settings/settings_onewire2_1.png" width="950"><br>
Hier kann ein Offset zu den jeweiligen Onewire-Temperatursensoren eingestellt werden.

### Bluetooth
<img src="../img/settings/settings_onewire2_2.png" width="950"><br>
Hier können bis zu 7 Bluetooth Devices festgelegt werden, von denen der Controller Daten holt.<br>
Dazu muss der Device-Typ und die MAC-Adresse (in Kleinbuchstaben) eingestellt werden.<br>

Der Controller scannt, sobald diese Konfigurationsseite aufgerufen ist, zyklisch nach neuen BT-Devices <br>
und zeigt die letzten 5 gefundenen am unteren Ende der Seite an.<br>

**Unterstützte Hardware<br>**
<img src="../img/settings/settings_unterstuetze_bms_bt.png" width="400"><br>

## Alarmregeln 
In den Alarmregeln kann eingestellt werden, welche Daten von welchen Devices überwacht werden sollen.<br>

**Allgemeine Informationen**<br>
Bluetooth 0 bis 6 sind die sieben Bluetooth-Devices.<br>
Serial 0 bis 10 sind die Seriellen-Devices. 0 bis 2 können direkt am BSC angeschlossen werden.<br>
Für Serial 3 bis 10 ist das Extension-Board notwendig.<br>

### BMS
<img src="../img/settings/settings_alarmrules_bms.png" width="950"><br><br>
Hier können die Daten von den Bluetooth und Serial BMS/Balancer überwacht werden.<br>
Wenn an einem seriellen Anschluss mehrere DaisyChain-Geräte angeschlossen sind, so gelten die getätigten Einstellungen für den kompletten Verbund.<br>
<br>
Der jeweilige Spannungs-Trigger wird aktiv, wenn die Spannung unterhalb "Min", oder oberhalb "Max" ist. Eine zusätzlich einstellbare Hysterese um den Trigger "zu beruhigen" ist bei Bedarf definierbar.<br>
Folgende Überwachungsfunktionen sind vorhanden:<br><br>

| Überwachungsfunktion | Option | Beschreibung |
| :------------ | :------------ | :------------ |
| **Keine Daten vom BMS** |  |  |
|  | Trigger keine Daten | Aktivieren/Deaktivieren der Überwachungsfunktion |
|  | Aktion bei Trigger | Gibt an welcher Trigger ausgelöst werden soll |
|  | Trigger keine Daten | Wenn x Sekunden keine Daten kommen, dann wird Trigger ausgelöst  |
| **Spannungsüberwachung Zelle Min/Max** |  |  |
|  | Spg.-Überwachung | Aktivieren/Deaktivieren der Überwachungsfunktion |
|  | Aktion bei Trigger | Gibt an welcher Trigger ausgelöst werden soll |
|  | Anzahl Zellen Monitoring | Anzahl der Zellen die Überwacht werden sollen.<br>Es wird immer bei der ersten Zelle begonnen. |
|  | Zellspannung Min | Überwachungs-Untergrenze |
|  | Zellspannung Max | Überwachungs-Obergrenze |
| **Spannungsüberwachung Gesamt Min/Max** |  |  |
|  | Aktion bei Trigger | Gibt an welcher Trigger ausgelöst werden soll |
|  | Spannung Min | Überwachungs-Untergrenze |
|  | Spannung Max | Überwachungs-Obergrenze |

### Temperatur
<img src="../img/settings/settings_alarmrules_temperatur.png" width="950"><br>
Hier können die Einstellungen für die Temperaturüberwachung der Onewire Temperatursensoren vorgenommen werden.<br>

| Option | Beschreibung |
| :------------ | :------------ |
| Sensornummer von<br>Sensornummer bis  | Hier kann der Bereich (von/bis) der Onewire-Sensoren eingegeben werden, die Überwacht werden sollen.<br>Die Sensornummern beziehen sich auf die Nummern der Onewire-Sensoren.  |
| Überwachung | Hier kann eine Überwachungsfunktion eingestellt werden.<br>Je nach Überwachungsfunktion haben die Felder Wert 1+2 eine andere Funktion |
| Referenzsensor <br>Wert 1<br>Wert 2 | Spezifische Funktion, je nach eingestellter Überwachung |
| Auslösung | Gibt an welcher Trigger ausgelöst werden soll.<br>Foraussetzung ist, dass eine Überwachungsfunktion ausgewählt wurde |

**Überwachungsfunktionen:**

  * **nicht belegt**
  Die Überwachung ist deaktiviert

  * **Maximalwert-Überschreitung**
  Es wird überwacht ob einer der Sensoren den maximal erlaubten Temperaturwert überschreitet.<br>
  Die maximale erlaubte Temperatur wird mit dem "Wert 1" festgelegt.
    * Referenzsensor: -
    * Wert 1: Maximal erlaubte Temperatur
    * Wert 2: -
<br><br>
  * **Maximalwert-Überschreitung (Referenz)**
  Es wird überwacht ob einer der Sensoren den maximal erlaubten Temperaturwert überschreitet.<br>
  Die maximale erlaubte Temperatur gibt der unter "Referenzsensor" festgelegte Sensor vor.
    * Referenzsensor:  Sensornummer des Onewire-Temperatursensors
    * Wert 1: Maximal erlaubte Temperaturdifferenz
    * Wert 2: -
<br><br>
  * **Differenzwert-Überwachung**
  Es wird die maximale Temperaturabweichung der Sensoren untereinander überwacht. <br>
  Ist die Differenz zwischen dem Niedrigsten und höchsten Wert zu groß, wird der Trigger ausgelöst.
    * Referenzsensor: -
    * Wert 1: Maximal erlaubte Temperaturdifferenz
    * Wert 2: -

### Derzeit aktive Inverter-Drosselung
Welche eingestellte Drosselung gerade aktiv ist, können Sie mit Hilfe der Restapi einsehen.<br>
Hierzu nach der IP-Adresse des BSC "/restapi" hinzufügen (z.B. 192.168.1.100/restapi).<br>

Die dargestellten "cc_"-Werte und "dcc_"-Werte stellen den durch die jeweilige Laderegelung limitierten Strom dar.

<img src="../img/settings/settings_restapi_aktive_drosselung.png" width="250"><br>

Falls es nicht möglich ist, bei dem Drosselungs-Event sich die Daten anzuschauen, kann man diese auch **temporär** mit z.B. HomeAssistant aufzeichnen lassen.<br>
Hierbei ist zu beachten, dass jede Abfrage *alle* verfügbaren Daten der RestAPI beinhaltet, was sehr viel Traffic und eine hohe Belastung für den BSC bedeutet.<br>
Für die Übertragung kann man mit 0,5 bis 1s pro Paket rechnen.<br>
Folgender YAML-Code ist für solch einen Sensor nutzbar - Hier als Beispiel für eine Anzeige von "setpoint_cc":

```yaml
platform: rest
name: bscapi_setpoint_cc
resource: http://192.x.x.x/restapi
value_template: "{{ value_json['inverter']['setpoint_cc'] }}"
unit_of_measurement: "A"
state_class: "measurement"
icon: "mdi:api"
```

## Firmware-Update
Ein Firmware-Update kann direkt über das Menü angestoßen werden.<br>
Informationen zum aktuellen Release-Stand, wie auch die dazu passende Beschreibung der Änderungen wird live angezeigt.<br>
Korrekt gesetztes Netzwerk-Gateway ist für die Live-Infos vorausgesetzt.

<img src="../img/settings/settings_ota_update.png" width="400"><br>