# Wechselrichter
In dieser Sektion können Sie neben der Definierung des angeschlossenen Inverters, das Lade- und Entladehandling definieren.<br>
Alle prozentualen Limitierungen werden auf die in der Kategorie "Basisdaten" eingestellten Werte angewendet.<br>
<img src="../img/settings/settings_inverter_basisdaten.png" width="950"><br>

## General
### CANbus
Hier kann man das in Richtung Inverter zu nutzende Protokoll definieren.<br>
Das "Pylontech" genannte CAN-Bus-Protokoll wird bei vielen Invertern unterstützt und ist z.B. mit Deye, Growatt nutzbar.<br>
Die Einstellung "Send extended data" ist nur unter Umständen für eine angeschlossene Victron Anlage nutzbar. Weitere Informationen sind [hier](../devices/wechselrichter/#einstellungen-bsc) einsehbar.

### Basisdaten

#### Absorption Ladespannung
Bei der Absorption Ladespannung handelt es sich um die Spannung, mit der die Akkus einen (nahezu) voll geladenen Zustand erreichen können.<br>
Diese Spannung sollte nicht dauerhaft anliegen, da man sonst Gefahr läuft, die Zellen zu überladen.<br>
<br>
Der richtige Zeitpunkt zum Abbruch der Ladung wird bei LiFePo4-Zellen mit 0,05C definiert. Was bei 280Ah Zellen 14A Ladestrom wären.<br>
Danach muss die Soll-Spannung der Akkus auf die niedrigere Float-Spannung gesetzt werden.<br>
Für dieses Prozedere gibt es die nachfolgende beschriebene Funktion "Charge-Current Cut-Off".<br>
Ohne diese aktivierte Einstellung wird der Akku immer auf der Absorption-Spannung verbleiben.

#### Float Ladespannung
Dieser Wert definiert die Spannung des Akkus im "offenen Zustand" (Open-Circuit Voltage (OCV)).<br>
Hierauf würden sich die Zellen selbstständig angleichen, wenn diese ohne jegliche Ladung oder Belastung unkontaktiert stehen würden.<br>

#### Batterypack Settings
Einen Lade- oder Entlade-Überstrom bei einzeln weg geschalteten Battery-Packs kann mit dieser Funktion verhindern werden.<br>
<br>
Das BSC kann einen zuvor definierten maximalen Lade- und Entladestrom an die Inverter senden.<br>
Dieser Strom ist von Ihnen, je nach Anzahl parallel angebundener Packs, zu definieren.<br>
Wenn nun ein BMS oder Schütz des Packs anschlägt und diesen vom Netz nimmt, würden die anderen Packs dessen Strom aufgeteilt je nach verbleibender Pack Anzahl erhalten und so möglicherweise in einen Überstrombereich gelangen.<br>
Um dies zu verhindern, können Sie mit dieser Einstellung einen maximalen Strom pro Pack definieren.<br>
Das BSC kümmert sich bei Abfall eines Packs dann automatisch darum, den maximal Strom auf die Summen der noch vorhandenen Packs zu begrenzen.<br>
<br>
Beispiel:<br>
Sie haben einen generellen maximalen Ladestrom von 180A eingestellt und haben drei Packs mit jeweils max. 100A definiert.<br>
Wenn nun ein Pack ausfallen würde, wären Sie mit den zulässigen 200A noch in einem gültigen Bereich.<br>
Ein weiterer Ausfall würde den Ladecontroller automatisch auf 100A limitieren, um für den noch verbleibenden Pack keinen Überstrom auszulösen.<br>

### Trigger bei SoC
Mit dieser Funktion kann man beispielsweise externe Gerät je nach SoC-Wert schalten.<br>
<img src="../img/settings/settings_inverter_trigger_soc.png" width="950"><br><br>

**Zwei Beispiele hierzu:**<br><br>
<img src="../img/settings/settings_inverter_trigger_soc_beispiel.png" width="450"><br>


Hier triggert...<br>

* Rule0 ein Relais für einen MPPT-Ladecontroller<br>
  * <= 89% einschalten
  * &gt;= 90% ausschalten

* Rule1 ein Relais für ein Ladegerät eines Offgrid-Systems<br>
  * <= 10% einschalten
  * &gt;= 25% ausschalten

Das Ladegerät geht bei 0% an, bis die 25% erreicht sind und schaltet dann aus. Erst bei 10% und kleiner wird es wieder gestartet.<br>
Somit hat man eine Hysterese von 15%.

## Charge
Beispiel eines Ladezyklus inkl. Balancing-, Float- und Absorption-Voltage mit Hilfe des BSC und einer Visualisierung über HomeAssistant/Grafana:<br>
<img src="../img/settings/settings_inverter_charge_beispiel.png" width="1300"><br>

### Ladestrom Zell-Spannungsabhängig drosseln
Diese Einstellungen ermöglichen es, den Ladestrom zu drosseln, wenn bestimmte Zellspannungen überschritten werden. Dies hilft, die Zellen vor Überladung zu schützen.

* **Ein/Aus:** Aktivieren oder Deaktivieren der Funktion.
* **Starten bei Zellspannung größer:** Gibt die Zellspannung an, bei der die Drosselung des Ladestroms beginnt.
* **Maximale Zellspannung:** Ab dieser Zellspannung wird nur noch mit dem Mindest-Ladestrom geladen.
* **Mindest-Ladestrom:** Der niedrigste Strom, der beim Laden verwendet wird.

### Ladestrom reduzieren bei Zelldrift
Diese Funktion reduziert den Ladestrom basierend auf der Zellspannungsdifferenz (Drift), um eine gleichmäßige Ladung der Zellen sicherzustellen.

* **Ein/Aus:** Aktivieren oder Deaktivieren der Funktion.
* **Starten bei Zellspannung größer:** Zellspannung, ab der die Reduzierung des Ladestroms beginnt.
* **Starten bei Drift größer:** Die Spannungsdifferenz zwischen Zellen, bei der die Reduzierung startet.
* **Reduzierung pro weiterer mV-Abweichung um:** Stromreduktion für jede weitere mV-Abweichung an Zellspannungsunterschied gegenüber der gesetzten Startdefinition.

### Ladestrom reduzieren - SoC
Der Ladestrom wird reduziert, wenn der Ladezustand (State of Charge, SoC) einen bestimmten Wert überschreitet.

* **Ein/Aus:** Aktivieren oder Deaktivieren der Funktion.
* **Reduzierung ab SoC:** Der Ladezustand (SoC), ab dem der Ladestrom reduziert wird.
* **Pro 1% um x A reduzieren:** Gibt an, um wie viel der Strom pro 1% SoC reduziert werden soll.
* **Mindest-Ladestrom:** Der niedrigste Strom, der beim Laden verwendet wird.

### Dynamische Ladespannungsbegrenzung (Beta!) 
Diese experimentelle Funktion begrenzt die Ladespannung basierend auf der Zellspannung und dem Spannungsunterschied zwischen den Zellen.

* **Ein/Aus:** Aktivieren oder Deaktivieren der Funktion.
* **Start-Zellspannung:** Zellspannung, ab der die Begrenzung aktiv wird.
* **Spannungs-Delta Min/Max:** Der maximale Unterschied zwischen der niedrigsten und höchsten Zellspannung.

### Autobalance
Das Autobalance-Feature übernimmt die vollständige Balancierung Ihrer Akkuzellen, um eine optimale Leistung und Lebensdauer des Akkus sicherzustellen. Im Folgenden werden die wichtigsten Einstellungen und Abläufe beschrieben:
<img src="../img/settings/settings_inverter_charge_autobalance.png" width="950"><br><br>

**Balance-Intervall** <br>
Mit dem Parameter Balance-Intervall kann festgelegt werden, in welchen zeitlichen Abständen ein Balancing der Akkuzellen durchgeführt werden soll. Dieser Wert bestimmt, wie häufig die Balancierung aktiviert wird, um die Zellspannungen anzugleichen.

**Startkriterien** <br>
Der Balancierungsprozess beginnt automatisch, wenn der definierte Balance-Intervall abgelaufen ist und im zweiten Schritt die Start-Zellspannung erreicht wurde. Diese Startbedingungen stellen sicher, dass das Balancing unter optimalen Bedingungen durchgeführt wird.

**Balance Mindest-Zeit** <br>
Der Parameter Balance Mindest-Zeit gibt an, wie lange das Balancing mindestens durchgeführt werden soll, unabhängig davon, ob die Zellspannungen bereits ausgeglichen sind. Dies verhindert eine zu kurze Balancierungsdauer und sorgt für eine gründliche Anpassung der Zellspannungen.

**Balance-Ladespannung** <br>
Für den Balancierungsprozess wird die Ladespannung des Systems auf die vorab definierte Balance-Ladespannung angehoben. Diese Spannung sorgt dafür, dass der Balancierungsvorgang effektiv durchgeführt werden kann.

**Balance-Zellspannung** <br>
Der Parameter Balance-Zellspannung gibt an, wie hoch die Spannung der einzelnen Zellen während des Balancing-Vorgangs maximal ansteigen darf. Dies verhindert eine Überladung der Zellen und schützt das Akkusystem vor Schäden.

**Beendigung des Balancierungsprozesses** <br>
Der Vorgang wird automatisch beendet, sobald die Differenz zwischen den Zellspannungen den eingestellten Wert erreicht oder unterschreitet. Dadurch wird sichergestellt, dass alle Zellen gleichmäßig geladen sind und keine übermäßige Disparität besteht.

**Timeout** <br>
Mit dem Parameter Timeout wird festgelegt, nach welcher maximalen Zeit der Balancierungsprozess automatisch abgebrochen wird, falls die Zellspannungen nicht innerhalb des vorgesehenen Zeitrahmens ausgeglichen werden konnten. Dies schützt das System vor endlosen Balancierungszyklen.

**Nach dem Balancing** <br>
Nach Abschluss des Balancierungsprozesses wird die Ladespannung auf das Floating-Niveau abgesenkt, um den Akku im geladenen Zustand zu halten, ohne ihn weiter zu belasten.

Dieses Autobalance-Feature bietet eine automatisierte Lösung, um die Akkuzellen regelmäßig zu balancieren und damit die Effizienz und Lebensdauer des Akkus zu maximieren. <br><br>

**Hinweise**

* Nach einem Neustart des BSC ist keine Wartezeit bis zum ersten Balancing. Erst nach dem ersten Balancing startet der eingestellte Balance-Interval.
* Wenn das BSC Abends um 22:00Uhr gestartet wurde und ein Intervall von fünf Tagen eingestellt ist, wird es nicht am Morgen des fünften Tages balancieren, sondern erst am nächsten, wenn die Sonne wieder auf geht!<br>Denn das Balancen würde erst am Abend des fünften Tages scharf geschaltet werden
* Für verschiedene BMS, z.B. dem Seplos, kann die einstellbare Mindestzeit genutzt werden, um den SoC 100 zu setzen <br>

Den genauen Ablauf des Balance-Vorgangs kann mit dem MQTT-Topic "/Inverter/autoBalState" visualisiert werden.<br>
Funktion der fünf verfügbaren States:<br>

0) Autobalancing ist deaktiviert
1) BSC wartet auf den nächsten Startzeitpunkt
2) Startzeitpunkt erreicht; BSC wartet auf die Start-Zellspannung
3) Start-Zellspannung erreicht; Autoblancing ist jetzt aktiv
4) Celldif. fertig wurde erreicht, aber die Balance-Ladespannung ist noch nicht erreicht
5) Balance-Ladespannung erreicht; warten bis Mindestzeit abgelaufen

### Charge-Current Cut-Off
Diese Funktion unterbricht den Ladestrom, wenn er für eine bestimmte Zeitspanne unterhalb einem eingestellten Strom-Wert liegt.<br>
Nach diesem Abbruch wird die bisher verwendete Soll-Lade-Spannung von der Absorption-Spannung auf die Float-Spannung gesetzt.<br>

* **Ein/Aus:** Aktivieren oder Deaktivieren der Funktion.
* **Cut-Off Time:** Zeitspanne, in der der Ladestrom unter einem bestimmten Wert liegen muss, bevor er auf 0 A gesetzt wird.
* **Cut-Off Strom:** Der Gesamt-Ladestrom, unterhalb dessen die Cut-Off-Zeit zu zählen beginnt.
* **Start-Zellspannung:** Zellspannung, ab der die Cut-Off-Regelung aktiv wird.

### SoC beim Unterschreiten der Zellspannung
Diese Funktion steuert das Nachladen der Zellen basierend auf der Zellspannung.

* **Ein/Aus:** Aktivieren oder Deaktivieren der Funktion.
* **Zellspannung Ladebeginn:** Zellspannung, bei der das Nachladen startet.
* **Zellspannung Ladeende:** Zellspannung, bei der das Nachladen endet.
* **SoC:** Ladezustand, der während des Nachladens an den Wechselrichter gesendet wird.
* **Sperrzeit zwischen zwei Nachladungen:** Zeit, die zwischen zwei Nachladungen vergehen muss.