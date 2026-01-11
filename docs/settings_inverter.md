# Wechselrichter
In diesem Abschnitt werden die Einstellungen für die Kommunikation mit dem Wechselrichter über den CAN-Bus sowie die Verarbeitung der bereitgestellten Messwerte konfiguriert. Über die CAN-Bus-Schnittstelle werden Betriebsdaten wie Ladezustand, Gesamtspannung, Strom und Temperatur an den Wechselrichter übertragen. Die Wahl der Datenquelle legt fest, welche Geräte als Referenz für einzelne Messgrößen dienen. Bei Bedarf können Werte aus mehreren Quellen zusammengefasst werden.  


## General

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='Ctd'><b>BMS Canbus enable</b></td><td class='Ctd'><input type='checkbox' checked name='38654709504'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s3840'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Canbus protocol</b></td>
<td class='Ctd'><select name='4294967424'>
<option value='0' >nicht belegt</option>
<option value='1' >Solis RHI</option>
<option value='2' >Pylontech</option>
<option value='3' selected>VICTRON</option>
<option value='4' >VICTRON 250k</option>
<option value='5' >BYD</option>
</select></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s128'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Send extended data</b></td><td class='Ctd'><input type='checkbox'  name='38654713664'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s8000'></span></td></tr>
<tr><td colspan='3' class='td0'><div class='help'>Nicht in Verbindung mit einem CerboGX aktivieren!</div></td></tr><tr class='Ctr'><td class='Ctd'><b>Datenquelle</b></td>
<td class='Ctd'>
<input id='t360168061' class='toggle' type='checkbox'>
<label for='t360168061' class='lbl-toggle'>Datenquelle</label>
<div class='collapsible-content'>
<div class='content-inner'>
<fieldset style='text-align:left;'>
<input type='checkbox' name='21474841792' value='0' checked>Data device 0<br>
<input type='checkbox' name='21474841792' value='1' checked>Data device 1<br>
<input type='checkbox' name='21474841792' value='2' checked>Data device 2<br>
<input type='checkbox' name='21474841792' value='3' >Data device 3<br>
<input type='checkbox' name='21474841792' value='4' >Data device 4<br>
<input type='checkbox' name='21474841792' value='5' >Data device 5<br>
<input type='checkbox' name='21474841792' value='6' >Data device 6<br>
<input type='checkbox' name='21474841792' value='7' >Data device 7<br>
<input type='checkbox' name='21474841792' value='8' >Data device 8<br>
<input type='checkbox' name='21474841792' value='9' >Data device 9<br>
<input type='checkbox' name='21474841792' value='10' >Data device 10<br>
<input type='checkbox' name='21474841792' value='11' >Data device 11<br>
<input type='checkbox' name='21474841792' value='12' >Data device 12<br>
<input type='checkbox' name='21474841792' value='13' >Data device 13<br>
<input type='checkbox' name='21474841792' value='14' >Data device 14<br>
<input type='checkbox' name='21474841792' value='15' >Data device 15<br>
<input type='checkbox' name='21474841792' value='16' >Data device 16<br>
<input type='checkbox' name='21474841792' value='17' >Data device 17<br>
</fieldset></div></div></td><td class='t1'></td></tr>
</table></form></div></div>

**BMS Canbus enable**  
Aktiviert oder deaktiviert die generelle CAN-Bus-Kommunikation des BMS.  
Wenn deaktiviert, werden keine Daten über den CAN-Bus an Wechselrichter gesendet.

**Canbus protocol**  
Legt fest, welches Kommunikationsprotokoll für den angeschlossenen Wechselrichter verwendet wird.  
Für die meisten Wechselrichter sollte das Protokoll **Pylontech** gewählt werden.  

**Send extended data**  
Steuert, ob erweiterte Datenpakete zusätzlich über den CAN-Bus gesendet werden.  

Diese Option kann **nur** in Verbindung mit einer **Victron-Anlage** genutzt werden und erfordert dort einen entsprechenden Treiber, der [hier](https://github.com/shining-man/dbus-bsc-can) verfügbar ist.  
**Nicht** empfohlen für den Einsatz in Verbindung mit einem **CerboGX**, da dies zu Kommunikationsproblemen führen kann.

**Datenquelle**  
Hier werden die Date-Devices ausgewählt von denen die Daten genommen und aufbereitet werden, um sie an den Wechselrichter zu übermitteln. 

Bei der **Standard-Firmware** muss hier **zusätzlich** eine **Master-Datenquelle** festgelegt werden.  
Von dieser wird die **Batteriespannung** übernommen, die anschließend an den Wechselrichter übermittelt wird.


## Valuehandling
In diesem Abschnitt werden die Quellen und Methoden zur Verarbeitung zentraler Batteriewerte festgelegt. Dabei kann für jeden Messwerttyp – Ladezustand (SoC), Gesamtspannung und Gesamtstrom – eine spezifische Datenquelle ausgewählt werden. Die verfügbaren Datenquellen stammen aus den angeschlossenen Data Devices und liefern die Rohwerte für die weitere Verarbeitung.  

Zusätzlich kann eingestellt werden, wie die Werte bei der Auswahl von mehreren Data Devices aggregiert werden sollen.  

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='sep' colspan='3'><b>Valuehandling</b></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Quelle SoC</b></td>
<td class='Ctd'>
<input id='t388335136' class='toggle' type='checkbox'>
<label for='t388335136' class='lbl-toggle'>Quelle SoC</label>
<div class='collapsible-content'>
<div class='content-inner'>
<fieldset style='text-align:left;'>
<input type='checkbox' name='21474845568' value='0' >Data device 0<br>
<input type='checkbox' name='21474845568' value='1' checked>Data device 1<br>
<input type='checkbox' name='21474845568' value='2' >Data device 2<br>
<input type='checkbox' name='21474845568' value='3' >...<br>
</fieldset></div></div></td><td class='t1'></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Aggregation SoC</b></td>
<td class='Ctd'><select name='4294974720'>
<option value='1' selected>Mittelwert</option>
<option value='4' >Minimalwert</option>
<option value='2' >Maximalwert</option>
<option value='3' >BMS</option>
</select></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s7424'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Quelle Gesamtspannung</b></td>
<td class='Ctd'>
<input id='t388335278' class='toggle' type='checkbox'>
<label for='t388335278' class='lbl-toggle'>Quelle Gesamtspannung</label>
<div class='collapsible-content'>
<div class='content-inner'>
<fieldset style='text-align:left;'>
<input type='checkbox' name='21474847552' value='0' checked>Data device 0<br>
<input type='checkbox' name='21474847552' value='1' checked>Data device 1<br>
<input type='checkbox' name='21474847552' value='2' checked>Data device 2<br>
<input type='checkbox' name='21474847552' value='3' >...<br>
</fieldset></div></div></td><td class='t1'></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Aggregation Spannung</b></td>
<td class='Ctd'><select name='4294978496'>
<option value='1' >Mittelwert</option>
<option value='4' >Minimalwert</option>
<option value='2' selected>Maximalwert</option>
</select></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s11200'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Quelle Gesamtstrom</b></td>
<td class='Ctd'>
<input id='t388335397' class='toggle' type='checkbox'>
<label for='t388335397' class='lbl-toggle'>Quelle Gesamtstrom</label>
<div class='collapsible-content'>
<div class='content-inner'>
<fieldset style='text-align:left;'>
<input type='checkbox' name='21474847616' value='0' checked>Data device 0<br>
<input type='checkbox' name='21474847616' value='1' checked>Data device 1<br>
<input type='checkbox' name='21474847616' value='2' checked>Data device 2<br>
<input type='checkbox' name='21474847616' value='3' >...<br>
</fieldset></div></div></td><td class='t1'></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Aggregation Strom</b></td>
<td class='Ctd'><select name='4294978560'>
<option value='1' >Mittelwert</option>
<option value='4' >Minimalwert</option>
<option value='2' >Maximalwert</option>
<option value='5' selected>Summe</option>
</select></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s11264'></span></td></tr>
</table></form></div></div>

!!! note "Hinweis"
    Bei der **Standard-Firmware** kann hier nur für den **SoC** die Aggregation eingestellt werden.

**Quelle SoC**  
Legt fest, von welchem angeschlossenen Gerät (Data Device) der Ladezustand der Batterie (State of Charge, SoC) übernommen wird.  
Wird nur ein Gerät als Quelle verwendet, bestimmt ausschließlich dessen Wert den SoC im System.

**Aggregation SoC**  
Definiert die Methode, mit der der SoC berechnet wird, wenn mehrere Datenquellen gleichzeitig ausgewählt wurden.  
Mögliche Aggregationsmethoden können z. B. **Mittelwert**, **höchster Wert**, **niedrigster Wert** oder **BMS** sein. Bei der Auswahl **BMS** wird der SoC des ersten ausgewählte Data-Device an den Wechselrichter übermittelt.   

**Quelle Gesamtspannung**  
Bestimmt, von welchem Data Device der Wert für die Gesamtbatteriespannung übernommen wird.  
Bei nur einer Quelle wird der angezeigte Spannungswert direkt von diesem Gerät übernommen.

**Aggregation Spannung**  
Legt die Berechnungsart fest, wenn mehrere Spannungsquellen ausgewählt wurden.  
Mögliche Auswahloptionen sind der **Mittelwert** oder die Auswahl des **höchsten** bzw. **niedrigsten** Wertes.  
Der so ermittelte Wert wird anschließend an den Wechselrichter übermittelt.

**Quelle Gesamtstrom**  
Gibt an, von welchem Data Device der aktuelle Gesamtstromwert der Batterie übernommen wird.  
Bei einer einzigen Quelle wird deren Wert direkt übernommen.

**Aggregation Strom**  
Definiert, wie der Gesamtstrom berechnet wird, wenn mehrere Stromquellen ausgewählt wurden.  
Mögliche Auswahloptionen sind **Summierung**, **Mittelwert** oder die Auswahl des **höchsten** bzw. **niedrigsten** Wertes.  
Der so ermittelte Wert wird anschließend an den Wechselrichter übermittelt.


## Basisdaten

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='sep' colspan='3'><b>Basisdaten</b></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Absorption Ladespannung</b></td>
<td class='Ctd'><input type='number' step='0.1' min='12' max='66' value='54.40' name='12884905856' class='fl1'></td><td class='t1'>V</td><td class='Ctd'><span class='secVal' id='s3968'></span></td></tr>
<tr><td colspan='3' class='td0'><div class='help'>Die Absorption Ladespannung entspricht einer erhöhten Spannung zum Erreichen des Voll-Zustandes.</div></td></tr><tr class='Ctr'><td class='Ctd'><b>Float Ladespannung</b></td>
<td class='Ctd'><input type='number' step='0.1' min='12' max='66' value='54.40' name='12884911872' class='fl1'></td><td class='t1'>V</td><td class='Ctd'><span class='secVal' id='s9984'></span></td></tr>
<tr><td colspan='3' class='td0'><div class='help'>Die Floatspannung wird nach Erreichen der einstellbaren Cutoff-Funktion angewendet.</div></td></tr><tr class='Ctr'><td class='Ctd'><b>Float Ladespannung SoC</b></td>
<td class='Ctd'><input type='number' min='1' max='100' value='95' name='4294972736'></td><td class='t1'>%</td><td class='Ctd'><span class='secVal' id='s5440'></span></td></tr>
<tr><td colspan='3' class='td0'><div class='help'>Beim Unterschreiten des eingestellten SoC wird von der Float in die Absorption Ladespannung gewechselt.</div></td></tr><tr class='Ctr'><td class='Ctd'><b>Max. Ladestrom</b></td>
<td class='Ctd'><input type='number' min='0' max='1000' value='100' name='12884905984'></td><td class='t1'>A</td><td class='Ctd'><span class='secVal' id='s4096'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Max. Entladestrom</b></td>
<td class='Ctd'><input type='number' min='0' max='1000' value='100' name='12884906048'></td><td class='t1'>A</td><td class='Ctd'><span class='secVal' id='s4160'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Ladeleistung auf 0</b></td>
<td class='Ctd'>
<input id='t388335673' class='toggle' type='checkbox'>
<label for='t388335673' class='lbl-toggle'>Ladeleistung auf 0</label>
<div class='collapsible-content'>
<div class='content-inner'>
<fieldset style='text-align:left;'>
<input type='checkbox' name='12884906112' value='0' >Trigger 1 <br>
<input type='checkbox' name='12884906112' value='1' >Trigger 2 <br>
<input type='checkbox' name='12884906112' value='2' >Trigger 3 <br>
<input type='checkbox' name='12884906112' value='3' >Trigger 4 <br>
<input type='checkbox' name='12884906112' value='4' >Trigger 5<br>
<input type='checkbox' name='12884906112' value='5' >Trigger 6<br>
<input type='checkbox' name='12884906112' value='6' >Trigger 7<br>
<input type='checkbox' name='12884906112' value='7' >Trigger 8<br>
<input type='checkbox' name='12884906112' value='8' >Trigger 9<br>
<input type='checkbox' name='12884906112' value='9' >Trigger 10<br>
</fieldset></div></div></td><td class='t1'></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Entladeleistung auf 0</b></td>
<td class='Ctd'>
<input id='t388335747' class='toggle' type='checkbox'>
<label for='t388335747' class='lbl-toggle'>Entladeleistung auf 0</label>
<div class='collapsible-content'>
<div class='content-inner'>
<fieldset style='text-align:left;'>
<input type='checkbox' name='12884906176' value='0' >Trigger 1 <br>
<input type='checkbox' name='12884906176' value='1' >Trigger 2 <br>
<input type='checkbox' name='12884906176' value='2' >Trigger 3 <br>
<input type='checkbox' name='12884906176' value='3' >Trigger 4 <br>
<input type='checkbox' name='12884906176' value='4' >Trigger 5<br>
<input type='checkbox' name='12884906176' value='5' >Trigger 6<br>
<input type='checkbox' name='12884906176' value='6' >Trigger 7<br>
<input type='checkbox' name='12884906176' value='7' >Trigger 8<br>
<input type='checkbox' name='12884906176' value='8' >Trigger 9<br>
<input type='checkbox' name='12884906176' value='9' >Trigger 10<br>
</fieldset></div></div></td><td class='t1'></td></tr>
<tr class='Ctr'><td class='Ctd'><b>SOC auf 100</b></td>
<td class='Ctd'>
<input id='t388335835' class='toggle' type='checkbox'>
<label for='t388335835' class='lbl-toggle'>SOC auf 100</label>
<div class='collapsible-content'>
<div class='content-inner'>
<fieldset style='text-align:left;'>
<input type='checkbox' name='12884906816' value='0' >Trigger 1 <br>
<input type='checkbox' name='12884906816' value='1' >Trigger 2 <br>
<input type='checkbox' name='12884906816' value='2' >Trigger 3 <br>
<input type='checkbox' name='12884906816' value='3' >Trigger 4 <br>
<input type='checkbox' name='12884906816' value='4' >Trigger 5<br>
<input type='checkbox' name='12884906816' value='5' >Trigger 6<br>
<input type='checkbox' name='12884906816' value='6' >Trigger 7<br>
<input type='checkbox' name='12884906816' value='7' >Trigger 8<br>
<input type='checkbox' name='12884906816' value='8' >Trigger 9<br>
<input type='checkbox' name='12884906816' value='9' >Trigger 10<br>
</fieldset></div></div></td><td class='t1'></td></tr>
</table><details><summary><b>Batterypack settings</b></summary><table>
<tr><td colspan='3'><b>Data device 0</b></td></tr><tr class='Ctr'><td class='Ctd'><b>Charge current per pack</b></td>
<td class='Ctd'><input type='number' min='0' max='500' value='280' name='12884909440'></td><td class='t1'>A</td><td class='Ctd'><span class='secVal' id='s7552'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Discharge current per pack</b></td>
<td class='Ctd'><input type='number' min='0' max='500' value='280' name='12884909504'></td><td class='t1'>A</td><td class='Ctd'><span class='secVal' id='s7616'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Kapazität</b></td>
<td class='Ctd'><input type='number' min='1' max='1000' value='280' name='12884912320'></td><td class='t1'>Ah</td><td class='Ctd'><span class='secVal' id='s10432'></span></td></tr>
<tr><td colspan='3'><hr style='border:none; border-top:1px dashed black; height:1px; color:#000000; background:transparent'></td></tr><tr><td colspan='3'><b>Data device 1</b></td></tr><tr class='Ctr'><td class='Ctd'><b>Charge current per pack</b></td>
<td class='Ctd'><input type='number' min='0' max='500' value='280' name='12884909441'></td><td class='t1'>A</td><td class='Ctd'><span class='secVal' id='s7553'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Discharge current per pack</b></td>
<td class='Ctd'><input type='number' min='0' max='500' value='280' name='12884909505'></td><td class='t1'>A</td><td class='Ctd'><span class='secVal' id='s7617'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Kapazität</b></td>
<td class='Ctd'><input type='number' min='1' max='1000' value='280' name='12884912321'></td><td class='t1'>Ah</td><td class='Ctd'><span class='secVal' id='s10433'></span></td></tr>
</table></details><table>
</table></form></div></div>

**Absorption Ladespannung**  
Die **Absorption Ladespannung** bezeichnet die Spannung, die erforderlich ist, um Akkus in einen (nahezu) vollständig geladenen Zustand zu bringen. Dabei ist zu beachten, dass diese Spannung nicht dauerhaft anliegen sollte, da dies die Lebensdauer und Leistung des Akkus negativ beeinflussen kann.

Ein geeigneter Zeitpunkt, um von der **Absorptionsladespannung** zur **Float-Spannung** zu wechseln, liegt vor, wenn der Strom bei LiFePo4-Zellen über einen längeren Zeitraum hinweg sehr niedrig bleibt.

Um diesen Übergang automatisch zu steuern, steht die Funktion "**Charge-Current Cut-Off**" zur Verfügung, die [hier](settings_inverter_charge.md#charge-current-cut-off) beschrieben wird. Ohne diese Funktion bleibt der Akku dauerhaft auf der Absorptions-Spannung, was langfristig zu Schäden führen kann.

Diese Einstellung ist daher essenziell, um den Ladeprozess korrekt zu beenden und den Akku optimal zu schützen.

**Float Ladespannung**  
Die Float Ladespannung gibt die Open-Circuit Voltage (OCV) an, also die Spannung, die eine Batterie erreicht, wenn sie sich im unbelasteten Zustand befindet und nicht geladen wird. 

Im Wesentlichen entspricht die Float Ladespannung dem Spannungswert, bei dem die Batterie in einem stabilen, ungenutzten Zustand verweilt, ohne zu entladen oder weiter aufgeladen zu werden. Dieser Zustand tritt auf, wenn keine Last auf der Batterie liegt und keine Energie in oder aus der Zelle fließt. 

!!! note "Hinweis"
    Der Wechsel in die Float-Phase erfolgt nur durch den [Charge-Current Cut-Off](settings_inverter_charge.md#charge-current-cut-off) oder den [Autobalancer](settings_inverter_charge.md#autobalance).  
    Bitte beachten Sie, dass ein zu hoch gewählter SoC-Wert unter Umständen das System sofort wieder in die Absorption-Phase zurückführen kann.  
    Auch ungenaue SoC-Werte der angeschlossenen BMS können diesen Phasenwechsel verfälschen. Für eine präzise SoC-Erfassung empfiehlt sich ein externer Shunt (siehe [hier](devices/externer_shunt.md)).

**Float Ladespannung SoC**  
Legt den Ladezustand (State of Charge) fest, bei dessen Unterschreiten von der Float-Ladespannung zurück auf die Absorptionsladespannung gewechselt wird.  
Diese Funktion sorgt dafür, dass bei sinkendem Ladezustand erneut eine vollständige Ladung initiiert wird.

**Max. Ladestrom**  
Dies ist der **maximale Strom**, der an den Wechselrichter übermittelt wird und den dieser als **Begrenzung für den Ladevorgang** verwendet.  
Damit wird sichergestellt, dass die Ladeleistung nicht über die zulässigen Werte hinausgeht und Batterie sowie Ladegeräte vor Überlastung geschützt werden.

**Max. Entladestrom**  
Dies ist der **maximale Strom**, der an den Wechselrichter übermittelt wird und den dieser als **Begrenzung für den Entladevorgang** verwendet.  
So wird verhindert, dass die Batterie mit zu hohen Strömen belastet werden.

**Ladeleistung auf 0**  
Setzt den Ladestrom auf 0 A, wenn einer der zugeordneten Trigger aktiviert wird.  

**Entladeleistung auf 0**  
Setzt den Entladestrom auf 0 A, wenn einer der zugeordneten Trigger aktiviert wird.  

**SOC auf 100**  
Setzt den Ladezustand im System auf 100 %, wenn einer der definierten Trigger aktiviert wird.  

**Batterypack Settings**  
Mit dieser Funktion können Sie einen Lade- oder Entlade-Überstrom vermeiden, wenn einzelne Battery-Packs im System abgeschaltet werden. 

Das Battery Safety Controller (BSC) sorgt dafür, dass der zuvor definierte maximale Lade- und Entladestrom an den Inverter übermittelt wird. Je nach Anzahl der parallel geschalteten Packs müssen Sie diesen Stromwert individuell festlegen. Sollte nun ein Battery Management System (BMS) eines Packs eingreifen und das Pack vom Netz nehmen, besteht die Möglichkeit, dass die verbleibenden Packs den vollen Strom des ausgefallenen Packs übernehmen. Dies könnte zu einem Überstrom führen.

Um dies zu verhindern, können Sie mit dieser Funktion einen maximalen Strom pro Pack definieren. Das BSC reagiert automatisch auf den Ausfall eines Packs und passt den maximalen Strom an die verbleibenden Packs an.

Beispiel: Angenommen, Sie haben einen maximalen Ladestrom von 180A definiert und drei Packs, bei denen jeweils ein maximaler Strom von 100A festgelegt ist. Sollte nun ein Pack ausfallen, würde der verbleibende Strom von 200A noch innerhalb des zulässigen Rahmens liegen. Fällt ein weiteres Pack aus, würde der Ladecontroller den Strom automatisch auf 100A begrenzen, um das verbleibende Pack vor einem Überstrom zu schützen.


<span id="a_ladespannungsrampe"></span>
## Ladespannungsrampe

Die Funktion **Ladespannungsrampe** sorgt dafür, dass Änderungen der Ladespannung – beispielsweise beim Übergang von Float auf Absorption – nicht sprunghaft, sondern in langsamen, definierten Schritten erfolgen. Damit werden abrupte Spannungsänderungen vermieden und Belastungsspitzen an Batterie und System reduziert.

!!! note "Hinweis"
    Diese Funktion steht nur in der **Sponsoren Version** zur Verfügung

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='sep' colspan='3'><b>Ladespannungsrampe</b></td></tr>
<tr><td colspan='3' class='td0'><div class='help'>Mit der Funktion wird Ladespannung langsam auf den neuen Wert geändert. Die Ladespannung wird pro Schritt um 100 mV geändert.</div></td></tr><tr class='Ctr'><td class='Ctd'><b>Ein/Aus</b></td><td class='Ctd'><input type='checkbox' checked name='38654717824'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s12160'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Zeit pro Spannungsschritt</b></td>
<td class='Ctd'><input type='number' min='1' max='240' value='5' name='4294979520'></td><td class='t1'>s</td><td class='Ctd'><span class='secVal' id='s12224'></span></td></tr>
</table></form></div></div>

**Funktionsweise**:  
Die Ladespannung wird in festen Schritten von 100 mV angepasst.  
Die Zeitdauer pro 100 mV-Schritt ist konfigurierbar und bestimmt damit die Geschwindigkeit der Spannungsänderung.  
Die Anpassung erfolgt kontinuierlich, bis die eingestellte Zielspannung erreicht ist.

**Parameter**:  
**Zeit pro Spannungsschritt**: Bestimmt, in welchem Intervall die Ladespannung in 100 mV-Schritten angepasst wird. Alle x Sekunden wird die Spannung um 100 mV erhöht oder verringert, bis die Zielspannung erreicht ist.

**Hinweis**:   
Die Ladespannungsrampe wird bei jeder Änderung der Sollspannung aktiv, sofern diese Funktion aktiviert ist.


## Batterietemperatur

Hier wird festgelegt, von welchem Data Device oder Onewire-Sensor die Batterietemperatur übernommen und an den Wechselrichter übermittelt werden soll.  

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='sep' colspan='3'><b>Batterietemperatur</b></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Quelle</b></td>
<td class='Ctd'><select name='4294973504'>
<option value='0' >Data device 0</option>
<option value='1' selected>Data device 1</option>
<option value='2' >Data device 2</option>
<option value='3' >Data device 3</option>
<option value='4' >Data device 4</option>
<option value='5' >Data device 5</option>
<option value='6' >Data device 6</option>
<option value='7' >Data device 7</option>
<option value='8' >Data device 8</option>
<option value='9' >Data device 9</option>
<option value='10' >Data device 10</option>
<option value='11' >Data device 11</option>
<option value='12' >Data device 12</option>
<option value='13' >Data device 13</option>
<option value='14' >Data device 14</option>
<option value='15' >Data device 15</option>
<option value='16' >Data device 16</option>
<option value='17' >Data device 17</option>
<option value='128' >Onewire</option>
</select></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s6208'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Sensornummer</b></td>
<td class='Ctd'><input type='number' min='0' max='64' value='0' name='4294973568'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s6272'></span></td></tr>
<tr><td colspan='3' class='td0'><div class='help'>Mögliche Werte:<br>Data device:0-2<br>Onewire:0-63</div></td></tr>
</table></form></div></div>


**Hinweis:** Bei der Standard-Firmware wird die Temperatur stets von der Masterquelle übernommen.


## Zelltemperatur

Hier wird festgelegt, von welchen Sensoren der als Datenquelle ausgewählten Data Devices die minimale und maximale Zelltemperatur ermittelt und an den Wechselrichter übermittelt wird.  

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='sep' colspan='3'><b>Zelltemperatur</b></td></tr>
<tr><td colspan='3' class='td0'><div class='help'>Es werden die Data Devices genommen, die unter 'Datenquelle' ausgewählt sind.</div></td></tr><tr class='Ctr'><td class='Ctd'><b>Sensoren</b></td>
<td class='Ctd'>
<input id='t388336656' class='toggle' type='checkbox'>
<label for='t388336656' class='lbl-toggle'>Sensoren</label>
<div class='collapsible-content'>
<div class='content-inner'>
<fieldset style='text-align:left;'>
<input type='checkbox' name='21474848192' value='0' >0<br>
<input type='checkbox' name='21474848192' value='1' >1<br>
<input type='checkbox' name='21474848192' value='2' >2<br>
<input type='checkbox' name='21474848192' value='3' >3<br>
<input type='checkbox' name='21474848192' value='4' >4<br>
<input type='checkbox' name='21474848192' value='5' >5<br>
</fieldset></div></div></td><td class='t1'></td></tr>
</table></form></div></div>

!!! note "Hinweis"
    Diese Funktion steht nur in der **Sponsoren Version** zur Verfügung


## Alarme (Inverter)

Über diese Einstellungen können Alarme im Wechselrichter über Trigger ausgelöst werden.  

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='sep' colspan='3'><b>Alarme (Inverter)</b></td></tr>
<tr class='Ctr'><td class='Ctd'><b>High battery voltage</b></td>
<td class='Ctd'>
<input id='t388336727' class='toggle' type='checkbox'>
<label for='t388336727' class='lbl-toggle'>High battery voltage</label>
<div class='collapsible-content'>
<div class='content-inner'>
<fieldset style='text-align:left;'>
<input type='checkbox' name='21474843648' value='0' >Trigger 1 <br>
<input type='checkbox' name='21474843648' value='1' >Trigger 2 <br>
<input type='checkbox' name='21474843648' value='2' >Trigger 3 <br>
<input type='checkbox' name='21474843648' value='3' >Trigger 4 <br>
<input type='checkbox' name='21474843648' value='4' >Trigger 5<br>
<input type='checkbox' name='21474843648' value='5' >Trigger 6<br>
<input type='checkbox' name='21474843648' value='6' >Trigger 7<br>
<input type='checkbox' name='21474843648' value='7' >Trigger 8<br>
<input type='checkbox' name='21474843648' value='8' >Trigger 9<br>
<input type='checkbox' name='21474843648' value='9' >Trigger 10<br>
</fieldset></div></div></td><td class='t1'></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Low battery voltage</b></td>
<td class='Ctd'>
<input id='t388336817' class='toggle' type='checkbox'>
<label for='t388336817' class='lbl-toggle'>Low battery voltage</label>
<div class='collapsible-content'>
<div class='content-inner'>
<fieldset style='text-align:left;'>
<input type='checkbox' name='21474843712' value='0' >Trigger 1 <br>
<input type='checkbox' name='21474843712' value='1' >Trigger 2 <br>
<input type='checkbox' name='21474843712' value='2' >Trigger 3 <br>
<input type='checkbox' name='21474843712' value='3' >... <br>
</fieldset></div></div></td><td class='t1'></td></tr>
<tr class='Ctr'><td class='Ctd'><b>High Temperature</b></td>
<td class='Ctd'>
<input id='t388336903' class='toggle' type='checkbox'>
<label for='t388336903' class='lbl-toggle'>High Temperature</label>
<div class='collapsible-content'>
<div class='content-inner'>
<fieldset style='text-align:left;'>
<input type='checkbox' name='21474843712' value='0' >Trigger 1 <br>
<input type='checkbox' name='21474843712' value='1' >Trigger 2 <br>
<input type='checkbox' name='21474843712' value='2' >Trigger 3 <br>
<input type='checkbox' name='21474843712' value='3' >... <br>
</fieldset></div></div></td><td class='t1'></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Low Temperature</b></td>
<td class='Ctd'>
<input id='t388337005' class='toggle' type='checkbox'>
<label for='t388337005' class='lbl-toggle'>Low Temperature</label>
<div class='collapsible-content'>
<div class='content-inner'>
<fieldset style='text-align:left;'>
<input type='checkbox' name='21474843712' value='0' >Trigger 1 <br>
<input type='checkbox' name='21474843712' value='1' >Trigger 2 <br>
<input type='checkbox' name='21474843712' value='2' >Trigger 3 <br>
<input type='checkbox' name='21474843712' value='3' >... <br>
</fieldset></div></div></td><td class='t1'></td></tr>
</table></form></div></div>


## Trigger bei SoC
Mit dieser Funktion kann ein Trigger ausgelöst werden, wenn ein bestimmter Ladezustand (SoC) der Batterie über- oder unterschritten wird.  
Dadurch lassen sich beispielsweise externe Geräte abhängig vom SoC-Wert schalten.  

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='sep' colspan='3'><b>Trigger bei SoC</b></td></tr>
<tr><td colspan='3' class='td0'><div class='help'>Auslösen eines Triggers, wenn ein bestimmter SoC über- oder unterschritten wird.</div></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Trigger</b></td>
<td class='Ctd'><select name='4294975872'>
<option value='0' selected>Aus</option>
<option value='1' >Trigger 1</option>
<option value='2' >Trigger 2 </option>
<option value='3' >Trigger 3 </option>
<option value='4' >Trigger 4 </option>
<option value='5' >Trigger 5</option>
<option value='6' >Trigger 6</option>
<option value='7' >Trigger 7</option>
<option value='8' >Trigger 8</option>
<option value='9' >Trigger 9</option>
<option value='10' >Trigger 10</option>
</select></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s8576'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>SoC - Trigger ein</b></td>
<td class='Ctd'><input type='number' min='1' max='100' value='95' name='4294975936'></td><td class='t1'>%</td><td class='Ctd'><span class='secVal' id='s8640'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>SoC - Trigger aus</b></td>
<td class='Ctd'><input type='number' min='1' max='100' value='80' name='4294976000'></td><td class='t1'>%</td><td class='Ctd'><span class='secVal' id='s8704'></span></td></tr>
</table></form></div></div>

**Parameter:**  
**SoC - Trigger ein**: Definiert den SoC-Wert, bei dem der Trigger aktiviert wird.  
**SoC - Trigger aus**: Definiert den SoC-Wert, bei dem der Trigger wieder deaktiviert wird.  

**Zwei Beispiele hierzu:**  
![](img/settings/settings_inverter_trigger_soc_beispiel.png){  width="450" }  


Hier triggert...  

* Rule0 ein Relais für einen MPPT-Ladecontroller  
  * <= 89% einschalten
  * &gt;= 90% ausschalten

* Rule1 ein Relais für ein Ladegerät eines Offgrid-Systems  
  * <= 10% einschalten
  * &gt;= 25% ausschalten

Das Ladegerät geht bei 0% an, bis die 25% erreicht sind und schaltet dann aus. Erst bei 10% und kleiner wird es wieder gestartet.  
Somit hat man eine Hysterese von 15%.
