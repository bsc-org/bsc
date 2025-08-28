## System

Hier findet man alle System-Internen Einstellmöglichkeiten, wie z.B. Benutzernamen und Passwörter zu den WLAN und MQTT Logins.

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='Ctd'><b>BSC Benutzer</b></td>
<td class='Ctd'><input type='text' value='bsc' name='1133871376384' pattern='^[^~]*$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s10240'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>BSC Passwort</b></td>
<td class='Ctd'><input type='password' value='admin' name='1133871376448' pattern='^[^~]*$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s10304'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Device Name</b></td>
<td class='Ctd'><input type='text' value='bsc-s3' name='34359750464' pattern='^[^#~+]*$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s12096'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Display timeout</b></td>
<td class='Ctd'><input type='number' min='1' max='120' value='5' name='4294976512'></td><td class='t1'>min</td><td class='Ctd'><span class='secVal' id='s9216'></span></td></tr>
</table></form></div></div>

- **BSC-Benutzername**  
  Benutzername für die Anmeldung am BSC-Webinterface.  

- **BSC-Passwort**  
  Passwort für die Anmeldung am BSC-Webinterface.

- **Device Name**  
  Benutzerdefinierter Gerätename. Dieser Name wird auch auf dem Dashboard angezeigt.  

- **Display Timeout**  
  Zeitspanne bis zur automatischen Deaktivierung des angeschlossenen Displays (Timeout).  


## Netzwerkeinstellungen

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='sep' colspan='3'><b>WLAN</b></td></tr>
<tr class='Ctr'><td class='Ctd'><b>WLAN SSID</b></td>
<td class='Ctd'><input type='text' value='SSID' name='34359740928' pattern='^[^~]*$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s2560'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>WLAN Passwort</b></td>
<td class='Ctd'><input type='password' value='123456' name='34359740992' pattern='^[^~]*$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s2624'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>WLAN connect Timeout</b></td>
<td class='Ctd'><input type='number' min='0' max='3600' value='30' name='12884908032'></td><td class='t1'>s</td><td class='Ctd'><span class='secVal' id='s6144'></span></td></tr>
<tr><td colspan='3' class='td0'></td></tr>

<tr class='Ctr'><td class='sep' colspan='3'><b>Static IP</b></td></tr>
<tr class='Ctr'><td class='Ctd'><b>IP-Adresse</b></td>
<td class='Ctd'><input type='text' value='' name='1133871368448' pattern='^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s2304'></span></td></tr>
<tr><td colspan='3' class='td0'><div class='help'>Wenn die IP-Adresse leer ist, dann ist DHCP aktiv</div></td></tr><tr class='Ctr'><td class='Ctd'><b>Gateway</b></td>
<td class='Ctd'><input type='text' value='' name='1133871368512' pattern='^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s2368'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Subnet</b></td>
<td class='Ctd'><input type='text' value='255.255.255.0' name='1133871368576' pattern='^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s2432'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>DNS</b></td>
<td class='Ctd'><input type='text' value='' name='1133871368640' pattern='^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s2496'></span></td></tr>
<tr><td colspan='3' class='td0'><div class='help'>Optional</div></td></tr>
</table></form></div></div>

!!! info "Hinweis"
    Bitte beachten Sie, dass das Tilde-Zeichen (~) derzeit als Passwort-Zeichen **nicht unterstützt** wird.  

- **WLAN SSID**  
  Name des WLAN-Netzwerks, mit dem sich der BSC verbinden soll.  

- **WLAN Passwort**  
  Passwort für die Anmeldung am angegebenen WLAN-Netzwerk.  

- **WLAN Connect Timeout**  
  Maximale Zeit (in Sekunden), die der BSC auf eine erfolgreiche WLAN-Verbindung wartet, bevor der Verbindungsversuch abgebrochen wird. Wird innerhalb dieser Zeit keine Verbindung hergestellt, erstellt das Gerät automatisch einen eigenen Access Point (AP).  
  Wird der Wert auf **0** gesetzt, ist der Timeout deaktiviert und der Verbindungsversuch wird unbegrenzt fortgesetzt.
  <br />
  **Zusatzfunktion in der [Insider Version](insider.md):**  
  Verliert der BSC die WLAN-Verbindung und erstellt nach dem eingestellten Timeout einen Access Point, versucht er alle **5 Minuten**, die Verbindung mit dem ursprünglichen WLAN-Netzwerk erneut herzustellen.

- **IP-Adresse**  
  Statische IPv4-Adresse des BSC.  
  Wenn dieses Feld leer bleibt, wird die IP-Adresse automatisch über DHCP bezogen.  

- **Gateway**  
  IPv4-Adresse des Standard-Gateways, das für die Netzwerkverbindung genutzt wird.  

- **Subnet**  
  Subnetzmaske für das lokale Netzwerk (z. B. `255.255.255.0`).  

- **DNS (Optional)**  
  IPv4-Adresse eines DNS-Servers zur Namensauflösung. Falls leer, wird der vom DHCP-Server bereitgestellte DNS-Server verwendet.  


## MQTT-Einstellungen

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='sep' colspan='3'><b>MQTT</b></td></tr>
<tr><td colspan='3' class='td0'><div class='help'>Zum Übernehmen der Settings, muss der BSC neu gestartet werden!</div></td></tr><tr class='Ctr'><td class='Ctd'><b>MQTT enable</b></td><td class='Ctd'><input type='checkbox'  name='38654708480'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s2816'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>MQTT Device Name</b></td>
<td class='Ctd'><input type='text' value='bsc' name='34359741248' pattern='^[^#~+]*$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s2880'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>MQTT Server IP</b></td>
<td class='Ctd'><input type='text' value='' name='34359741056' pattern='^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s2688'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>MQTT Server Port</b></td>
<td class='Ctd'><input type='number' min='1' max='49151' value='1883' name='12884904640'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s2752'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Username</b></td>
<td class='Ctd'><input type='text' value='' name='34359743872' pattern='^[^#~+]*$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s5504'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Passwort</b></td>
<td class='Ctd'><input type='password' value='' name='34359743936' pattern='^[^~]*$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s5568'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>MQTT Topic Name</b></td>
<td class='Ctd'><input type='text' value='bsc' name='34359741312' pattern='^[^#~+]*$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s2944'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>MQTT Sendeintervall</b></td>
<td class='Ctd'><input type='number' min='30' max='120' value='60' name='4294975808'></td><td class='t1'>s</td><td class='Ctd'><span class='secVal' id='s8512'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Remanenz vTrigger</b></td>
<td class='Ctd'>
<input id='t42348100' class='toggle' type='checkbox'>
<label for='t42348100' class='lbl-toggle'>Remanenz vTrigger</label>
<div class='collapsible-content'>
<div class='content-inner'>
<fieldset style='text-align:left;'>
<input type='checkbox' name='21474847232' value='0' >vTrigger 1<br>
<input type='checkbox' name='21474847232' value='1' >vTrigger 2<br>
<input type='checkbox' name='21474847232' value='2' >vTrigger 3<br>
<input type='checkbox' name='21474847232' value='3' >vTrigger 4<br>
<input type='checkbox' name='21474847232' value='4' >vTrigger 5<br>
<input type='checkbox' name='21474847232' value='5' >vTrigger 6<br>
<input type='checkbox' name='21474847232' value='6' >vTrigger 7<br>
<input type='checkbox' name='21474847232' value='7' >vTrigger 8<br>
<input type='checkbox' name='21474847232' value='8' >vTrigger 9<br>
<input type='checkbox' name='21474847232' value='9' >vTrigger 10<br>
</fieldset></div></div></td><td class='t1'></td></tr>
<tr><td colspan='3' class='td0'><div class='help'>V-Trigger behalten dadurch ihren Zustand, auch wenn Spannung unterbrochen wurde.</div></td></tr>
</table></form></div></div>

- **MQTT Enable**  
  Aktiviert oder deaktiviert die MQTT-Funktionalität im BSC.  
  Sobald MQTT aktiviert ist und die zugehörige IP-Adresse und der Port eingestellt ist, sendet der BSC zyklisch die Daten an den MQTT-Broker.

- **MQTT Device Name**  
  Eindeutiger Gerätename, unter dem der BSC im MQTT-Broker identifiziert wird.  

- **MQTT Server IP**  
  IPv4-Adresse des MQTT-Brokers, zu dem sich der BSC verbinden soll.  

- **MQTT Server Port**  
  Portnummer des MQTT-Brokers (Standard: `1883` für unverschlüsselte Verbindungen).  

- **Username**  
  Benutzername für die Anmeldung am MQTT-Broker (falls erforderlich).  

- **Passwort**  
  Passwort für die Anmeldung am MQTT-Broker (falls erforderlich).  

- **MQTT Topic Name**  
  Basis-Topic, unter dem der BSC seine Daten veröffentlicht. Untertopics werden automatisch für einzelne Werte angelegt.  

- **MQTT Sendeintervall (in Sekunden)**  
  Zeitintervall in Sekunden, in dem der BSC Daten an den MQTT-Broker sendet.  
  <br>
  Durch die Vielzahl der zu übertragenen Daten, gibt es im BSC zwei unterschiedlich priorisierte Nachrichtenintervalle.  
  Die wichtigsten Nachrichten, wie z.B. Gesamtspannung (totalVoltage) und Gesamtstrom (totalCurrent) werden sekündlich via MQTT übertragen.  Andere, niedriger priorisierte Daten werden in einem vom Benutzer einstellbaren Intervall übertragen.

- **Remanenz vTrigger**  
  Mit "Remanenz vTrigger" kann festgelegt werden, welcher vTrigger als speichernd definiert werden soll.  
  Ein speichernder vTrigger stellt sicher, dass seine Werte auch nach einem Neustart (Reboot) oder einem Spannungsausfall automatisch wiederhergestellt werden.  
  Mehr zum Thema vTrigger unter [MQTT](mqtt.md#virtual-trigger).


## Zeitserver (NTP)

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='sep' colspan='3'><b>NTP</b></td></tr>
<tr><td colspan='3' class='td0'><div class='help'>Zum Übernehmen der Settings, muss der BSC neu gestartet werden!</div></td></tr><tr class='Ctr'><td class='Ctd'><b>Server Name/IP</b></td>
<td class='Ctd'><input type='text' value='pool.ntp.org' name='1133871373952' pattern='^[^~]*$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s7808'></span></td></tr>
</table></form></div></div>

- **Server Name/IP**  
  Name oder IPv4-Adresse des NTP Servers.  
  
Falls bei der Verwendung eines externen NTP-Servers Probleme mit der Zeitsynchronisierung auftreten, kann alternativ der Router des lokalen Netzwerks als Zeitserver genutzt werden. Diese Methode ist in vielen Fällen stabiler.  

**Beispiel (AVM FritzBox):**  
In der FritzBox kann der Zeitserver im Menü  
`Heimnetz → Netzwerk → Netzwerkeinstellungen`  
aktiviert werden.  

Als Zeitserver können beispielsweise folgende Adressen definiert werden:  
`ntp1.t-online.de; 2.europe.pool.ntp.org`  

Im BSC ist anschließend die **IP-Adresse** des Routers als NTP-Server anzugeben.  
**Hinweis:** Die Verwendung eines Hostnamens anstelle der IP-Adresse kann zu Verbindungsproblemen führen.
