## Funktionsprinzip der Trigger
In diesem Abschnitt wird erklärt, wie interne Trigger zur Überwachung und Steuerung verschiedener Werte (z. B. Temperatur, Spannung) verwendet werden können, um auf potenzielle Gefahrenzustände zu reagieren.  
  
**Trigger-Funktionalität**  
Für jeden zu überwachenden Wert kann ein Trigger konfiguriert werden, der bei Erreichen eines definierten Grenzwerts aktiv wird. Ein aktivierter Trigger löst selbst zunächst keine direkte Aktion aus. Es kann jedoch flexibel eingestellt werden, welche Aktionen durch den Trigger ausgelöst werden sollen. So kann beispielsweise:

  - ein Relais geschaltet werden (z. B. zum Aktivieren eines Lüfters),
  - der Wechselrichter angewiesen werden, seinen Ladestrom auf 0 A zu reduzieren.


Diese Logik ermöglicht es, Trigger (als Signalgeber) und verbundene Aktionen (als Signalnehmer) in flexibler Weise zu kombinieren. Es stehen bis zu 10 interne Trigger zur Verfügung.  
  
Ein Setzen dieser Trigger ist auch von einer externen Datenverbindung mit Hilfe der [vTrigger](mqtt.md#virtual-trigger) möglich.  

**Funktionsweise bei mehreren Quellen**  
Wenn mehrere Quellen mit einem Trigger verbunden sind, gilt folgende Regel:

  - Aktivierung (High): Der Trigger wird aktiv geschaltet, sobald mindestens eine der verbundenen Quellen den definierten Grenzwert überschreitet.
  - Deaktivierung (Low): Der Trigger wird erst deaktiviert, wenn alle verbundenen Quellen wieder in den Normalzustand zurückgekehrt sind.

!!! note "Hinweis"
    Insbesondere bei der Verwendung von [virtuellen Triggern (vTrigger)](mqtt.md#virtual-trigger) ist darauf zu achten, dass diese durch Automatisierungen gezielt deaktiviert werden müssen, um die Trigger-Funktionalität erneut nutzen zu können.

**Beispielanwendung**

  - Zwei Temperatursensoren (Sensor 2 und Sensor 3) überwachen eine Grenztemperatur von 30 °C. Sobald einer der beiden Sensoren diesen Wert überschreitet, wird Trigger 1 aktiv.
  - Auf Trigger 1 basierend, können zwei Aktionen konfiguriert werden:
      - Relais 1 wird geschaltet, um einen Lüfter zu aktivieren.
      - Der Wechselrichter reduziert automatisch seinen Ladestrom, um die Wärmeentwicklung zu minimieren.

**Zusammenfassung**  
Diese Kombination aus flexiblen Trigger-Quellen und konfigurierbaren Zielaktionen ermöglicht eine präzise und vielseitige Steuerung. Die Logik stellt sicher, dass Gefahren frühzeitig erkannt und geeignete Maßnahmen ergriffen werden können, während die Flexibilität zur Anpassung an individuelle Anforderungen erhalten bleibt.

## Triggername

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='sep' colspan='3'><b>Triggername</b></td></tr>
<tr><td class='Ctd2' colspan='3'><b>Trigger description</b></td></tr>
<tr><td colspan='3'><b>Trigger 1</b></td></tr><tr class='Ctr'><td class='Ctd'><b>Trigger</b></td>
<td class='Ctd'><input type='text' value='Beispieltrigger 1' name='1133871373632' pattern='^[^~]*$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s7488'></span></td></tr>
<tr><td colspan='3'><hr style='border:none; border-top:1px dashed black; height:1px; color:#000000; background:transparent'></td></tr><tr><td colspan='3'><b>Trigger 2</b></td></tr><tr class='Ctr'><td class='Ctd'><b>Trigger</b></td>
<td class='Ctd'><input type='text' value='' name='1133871373633' pattern='^[^~]*$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s7489'></span></td></tr>
<tr><td colspan='3'><hr style='border:none; border-top:1px dashed black; height:1px; color:#000000; background:transparent'></td></tr><tr><td colspan='3'><b>Trigger 3</b></td></tr><tr class='Ctr'><td class='Ctd'><b>Trigger</b></td>
<td class='Ctd'><input type='text' value='' name='1133871373634' pattern='^[^~]*$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s7490'></span></td></tr>
</table></form></div></div>

In diesem Menü können für die **10 verfügbaren Trigger** benutzerdefinierte Namen vergeben werden.  
Diese Namen werden im gesamten System verwendet, z. B. bei der Auswahl von Triggern in anderen Einstellungen oder Funktionen.


## Trigger Scheduler
!!! note "Hinweis"
    Diese Funktion steht nur in der Sponsoren Version zur Verfügung

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='sep' colspan='3'><b>Trigger Scheduler</b></td></tr>
<tr><td class='Ctd2' colspan='3'><b>Trigger Scheduler</b></td></tr>
<tr><td colspan='3'><b>Scheduler  0</b></td></tr><tr class='Ctr'><td class='Ctd'><b>Trigger</b></td>
<td class='Ctd'><select name='4294980032'>
<option value='0' selected>Aus</option>
<option value='1' >Trigger 1 </option>
<option value='2' >Trigger 2 </option>
<option value='3' >Trigger 3 </option>
<option value='4' >Trigger 4 </option>
<option value='5' >Trigger 5</option>
<option value='6' >Trigger 6</option>
<option value='7' >Trigger 7</option>
<option value='8' >Trigger 8</option>
<option value='9' >Trigger 9</option>
<option value='10' >Trigger 10</option>
</select></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s12736'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Monat</b></td>
<td class='Ctd'>
<input id='t46161146' class='toggle' type='checkbox'>
<label for='t46161146' class='lbl-toggle'>Monat</label>
<div class='collapsible-content'>
<div class='content-inner'>
<fieldset style='text-align:left;'>
<input type='checkbox' name='12884914688' value='0' >Januar<br>
<input type='checkbox' name='12884914688' value='1' >Februar<br>
<input type='checkbox' name='12884914688' value='2' >März<br>
<input type='checkbox' name='12884914688' value='3' >April<br>
<input type='checkbox' name='12884914688' value='4' >Mai<br>
<input type='checkbox' name='12884914688' value='5' >Juni<br>
<input type='checkbox' name='12884914688' value='6' >Juli<br>
<input type='checkbox' name='12884914688' value='7' >August<br>
<input type='checkbox' name='12884914688' value='8' >September<br>
<input type='checkbox' name='12884914688' value='9' >Oktober<br>
<input type='checkbox' name='12884914688' value='10' >November<br>
<input type='checkbox' name='12884914688' value='11' >Dezember<br>
</fieldset></div></div></td><td class='t1'></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Wochentag</b></td>
<td class='Ctd'>
<input id='t46161156' class='toggle' type='checkbox'>
<label for='t46161156' class='lbl-toggle'>Wochentag</label>
<div class='collapsible-content'>
<div class='content-inner'>
<fieldset style='text-align:left;'>
<input type='checkbox' name='12884914752' value='0' >Sonntag<br>
<input type='checkbox' name='12884914752' value='1' >Montag<br>
<input type='checkbox' name='12884914752' value='2' >Dienstag<br>
<input type='checkbox' name='12884914752' value='3' >Mittwoch<br>
<input type='checkbox' name='12884914752' value='4' >Donnerstag<br>
<input type='checkbox' name='12884914752' value='5' >Freitag<br>
<input type='checkbox' name='12884914752' value='6' >Samstag<br>
</fieldset></div></div></td><td class='t1'></td></tr>
<tr class='Ctr'><td class='Ctd'><b>von</b></td>
<td class='Ctd'><input type='time' value='0' name='34359751296' pattern='.*'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s12928'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>bis</b></td>
<td class='Ctd'><input type='time' value='0' name='34359751360' pattern='.*'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s12992'></span></td></tr>
</table></form></div></div>

Der Trigger Scheduler ermöglicht die zeitgesteuerte Ausführung von Triggern im BSC.  
Es stehen insgesamt **5 Scheduler** zur Verfügung, die unabhängig voneinander konfiguriert werden können.  

Folgende Parameter stehen zur Verfügung:  

- **Trigger**  
  Auswahl des auszuführenden Triggers.  

- **Monat**  
  Auswahl der Monate, in dem der Trigger aktiv sein soll.  

- **Wochentag**  
  Auswahl der Wochentage, an dem der Trigger ausgeführt werden soll.  

- **Von (Uhrzeit)**  
  Startzeitpunkt, ab dem der Trigger aktiv ist.  

- **Bis (Uhrzeit)**  
  Endzeitpunkt, bis zu dem der Trigger aktiv ist.  
