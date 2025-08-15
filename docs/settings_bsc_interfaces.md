# Schnittstellen des BSC
In den Schnittstellen Einstellungen wird eingestellt was an welcher Schnittstelle angeschlossen ist. Hier wird **nicht** eingestellt was z.B. mit den Daten von einem BMS oder Balancer passieren soll, oder wann der Relais-Ausgang schalten soll. Dies wird dann bei den Einstellungen zu den Alarmregeln oder dem Wechselrichter gemacht.



## Relaisausgänge
Hier können die grundlegenden Einstellungen zu den Relaisausgängen vorgenommen werden.

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='Ctd'><b>Ausl&#246;severhalten</b></td>
<td class='Ctd'><select name='4294969216'>
<option value='0' selected>Permanent</option>
<option value='1' >Impuls</option>
</select></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s1920'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Impulsdauer</b></td>
<td class='Ctd'><input type='number' min='100' max='10000' value='500' name='12884903872'></td><td class='t1'>ms</td><td class='Ctd'><span class='secVal' id='s1984'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Verz&ouml;gerung</b></td>
<td class='Ctd'><input type='number' min='0' max='254' value='0' name='4294969408'></td><td class='t1'>s</td><td class='Ctd'><span class='secVal' id='s2112'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Invertieren</b></td><td class='Ctd'><input type='checkbox'  name='38654716160'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s10496'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Auswahl Trigger</b></td>
<td class='Ctd'>
<input id='t129889691' class='toggle' type='checkbox'>
<label for='t129889691' class='lbl-toggle'>Auswahl Trigger</label>
<div class='collapsible-content'>
<div class='content-inner'>
<fieldset style='text-align:left;'>
<input type='checkbox' name='12884903936' value='0' checked>Trigger 1 <br>
<input type='checkbox' name='12884903936' value='1' >Trigger 2 <br>
<input type='checkbox' name='12884903936' value='2' >Trigger 3 <br>
<input type='checkbox' name='12884903936' value='3' >Trigger 4 <br>
<input type='checkbox' name='12884903936' value='4' >Trigger 5<br>
<input type='checkbox' name='12884903936' value='5' >Trigger 6<br>
<input type='checkbox' name='12884903936' value='6' >Trigger 7<br>
<input type='checkbox' name='12884903936' value='7' >Trigger 8<br>
<input type='checkbox' name='12884903936' value='8' >Trigger 9<br>
<input type='checkbox' name='12884903936' value='9' >Trigger 10<br>
</fieldset></div></div></td>
</table></form></div></div>

* **Auslösung bei**
  Hier wird angegeben bei welchem Trigger das Relais schalten soll
* **Auslöseverhalten**
    * Permanent: Das Relais bleibt angezogen, solange der Trigger ansteht
    * Impuls: Das Relais schaltet für eine Dauer von x ms. Die Impulsdauer wird unter "Impulsdauer" eingestellt.
* **Impulsdauer**
  Hier wird die Impulsdauer eingestellt, wenn bei dem Auslöseverhalten "Impuls" eingestellt wurde.
* **Verzögerung**
  Gibt an um wie viel Sekunden das Schalten des Relais bei einem kommenden Trigger verzögert werden soll.
* **Invertieren**
  Die Option ermöglicht es, den Relaisausgang flexibel zwischen den Betriebsmodi NO (Normally Open) und NC (Normally Closed) umzuschalten. Durch Aktivieren dieser Option wird die Logik des Relaisausgangs umgekehrt, sodass bei der Ausführung des Schaltvorgangs der alternative Zustand genutzt wird. Diese Funktion ist besonders nützlich, um die Kompatibilität mit verschiedenen Steuerungsanforderungen oder Schaltungsdesigns sicherzustellen.



## Digitaleingänge
Hier können die grundlegenden Einstellungen zu den Digitaleingängen vorgenommen werden.

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='Ctd'><b>Eingang invertieren</b></td><td class='Ctd'><input type='checkbox'  name='38654707840'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s2176'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Weiterleiten an</b></td>
<td class='Ctd'><select name='4294969536'>
<option value='0' >Aus</option>
<option value='1' selected>Trigger 1 </option>
<option value='2' >Trigger 2 </option>
<option value='3' >Trigger 3 </option>
<option value='4' >Trigger 4 </option>
<option value='5' >Trigger 5</option>
<option value='6' >Trigger 6</option>
<option value='7' >Trigger 7</option>
<option value='8' >Trigger 8</option>
<option value='9' >Trigger 9</option>
<option value='10' >Trigger 10</option>
</select></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s2240'></span></td></tr>
</table></form></div></div>

- **Eingang invertieren**  
  Hier kann der Eingang invertiert werden

- **Weiterleiten an**  
  Mit dieser Option wird festgelegt, welcher Trigger durch einen bestimmten Eingang aktiviert wird.  
    - Wird der Eingang **High**, wird der hier ausgewählte Trigger aktiviert.  
    - Ist der Eingang **invertiert**, wird der Trigger bei einem **Low**-Signal am Eingang aktiviert. 



## Serial
In diesem Abschnitt legen Sie fest, welche Hardware an welchem seriellen Port angeschlossen ist. Darüber hinaus ist es erforderlich, im Abschnitt ["Data devices"](#data-devices) zu konfigurieren, welche serielle Port welchem internen Daten-Device zugeordnet wird.

Detaillierte Informationen zur Einrichtung der Data Devices finden sie im Kapitel [Data devices](#data-devices).  

Diese Konfiguration stellt sicher, dass die angeschlossene Hardware korrekt erkannt wird und mit den entsprechenden internen Daten-Devices verknüpft werden kann.

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr><td class='Ctd2' colspan='3'><b>Serielle Schnittstellen</b></td></tr>
<tr><td colspan='3'><b>Serial 0</b></td></tr><tr class='Ctr'><td class='Ctd'><b>Serial</b></td>
<td class='Ctd'><select name='4294967360'>
<option value='0' >nicht belegt</option>
<option value='1' >JBD BMS</option>
<option value='2' >JK BMS</option>
<option value='14' >JK Inverter BMS</option>
<option value='3' selected>Seplos BMS</option>
<option value='12' >Seplos V3 BMS</option>
<option value='4' >DALY BMS</option>
<option value='5' >Sylcin BMS</option>
<option value='11' >PACE PC200 BMS (RS485B)</option>
<option value='10' >Victron SmartShunt</option>
</select></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s64'></span></td></tr>
<tr><td colspan='3'><hr style='border:none; border-top:1px dashed black; height:1px; color:#000000; background:transparent'></td></tr>

<tr><td colspan='3'><b>Serial 1</b></td></tr><tr class='Ctr'><td class='Ctd'><b>Serial</b></td>
<td class='Ctd'><select name='4294967360'>
<option value='0' >nicht belegt</option>
</select></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s64'></span></td></tr>
<tr><td colspan='3'><hr style='border:none; border-top:1px dashed black; height:1px; color:#000000; background:transparent'></td></tr>

<tr><td colspan='3'><b>Serial 2</b></td></tr><tr class='Ctr'><td class='Ctd'><b>Serial</b></td>
<td class='Ctd'><select name='4294967360'>
<option value='0' >nicht belegt</option>
</select></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s64'></span></td></tr>
<tr><td colspan='3'><hr style='border:none; border-top:1px dashed black; height:1px; color:#000000; background:transparent'></td></tr>

<tr class='Ctr'><td class='sep' colspan='3'><b>Allgemein</b></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Anzahl Zellen</b></td>
<td class='Ctd'><input type='number' min='4' max='24' value='16' name='4294976320'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s9024'></span></td></tr>
</table></form></div></div>

**Zuordnung bei der orginal BSC Hardware (Software => Hardware):**

* Serial 0 => U1
* Serial 1 => U2
* Serial 2 => U3

Serial 3 bis 10 sind nur mit angeschlossener Serial-Extension nutzbar.  

**Unterstütze Hardware**  
Eine Liste der unterstützten Hardware ist unter folgendem Link verfügbar: [Unterstützte BMS](devices/bms.md#unterstutzte-bms)  
Die Liste der verfügbaren Hardware wird kontinuierlich erweitert, um den Anforderungen und Bedürfnissen unserer Nutzer gerecht zu werden.

**Anzahl Zellen**  
Gibt die Anzahl der in einer Batterie verbauten Einzelzellen an.  
Diese Einstellung ist z.B. wichtig, um die Werte im Dashboard korrekt darzustellen.  

### Filter

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='sep' colspan='3'><a href='https://bsc-org.github.io/bsc/settings_bsc/#filter' target='_blank'><b>Filter</b></a></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Anzahl RX Fehler</b></td>
<td class='Ctd'><input type='number' min='1' max='125' value='2' name='1103806602816'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s7744'></span></td></tr>
<tr><td colspan='3' class='td0'><div class='help'>Gibt an, nach wievielen fehlerhaften Paketen es als Fehler bewertet wird.</div></td></tr><tr class='Ctr'><td class='Ctd'><b>Abweichung Zellspannung</b></td>
<td class='Ctd'><input type='number' min='0' max='100' value='0' name='1103806602752'></td><td class='t1'>%</td><td class='Ctd'><span class='secVal' id='s7680'></span></td></tr>
<tr><td colspan='3' class='td0'><div class='help'>0=Filter deaktiviert</div></td></tr>
</table></form></div></div>

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


<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='Ctd'><b>Onewire enable</b></td><td class='Ctd'><input type='checkbox' checked name='38654708864'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s3200'></span></td></tr>
<tr><td class='Ctd2' colspan='3'><b>OW Adressen</b></td></tr>
<tr><td colspan='3'><b>OW Adr. 0</b></td></tr><tr class='Ctr'><td class='Ctd'><b>OW Adr.</b></td>
<td class='Ctd'><input type='text' value='28:93:e3:95:f0:1:3c:56' name='1133871369408' pattern='^([0-9a-f]{1,2}:){7}[0-9a-f]{1,2}$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s3264'></span></td></tr>
<tr><td colspan='3'><hr style='border:none; border-top:1px dashed black; height:1px; color:#000000; background:transparent'></td></tr><tr><td colspan='3'><b>OW Adr. 1</b></td></tr><tr class='Ctr'><td class='Ctd'><b>OW Adr.</b></td>
<td class='Ctd'><input type='text' value='28:93:e3:95:f0:1:3c:58' name='1133871369409' pattern='^([0-9a-f]{1,2}:){7}[0-9a-f]{1,2}$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s3265'></span></td></tr>
<tr><td colspan='3'><hr style='border:none; border-top:1px dashed black; height:1px; color:#000000; background:transparent'></td></tr><tr><td colspan='3'><b>OW Adr. 2</b></td></tr><tr class='Ctr'><td class='Ctd'><b>OW Adr.</b></td>
<td class='Ctd'><input type='text' value='' name='1133871369410' pattern='^([0-9a-f]{1,2}:){7}[0-9a-f]{1,2}$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s3266'></span></td></tr>
<tr><td colspan='3'><hr style='border:none; border-top:1px dashed black; height:1px; color:#000000; background:transparent'></td></tr><tr><td colspan='3'><b>OW Adr. 3</b></td></tr><tr class='Ctr'><td class='Ctd'><b>OW Adr.</b></td>
<td class='Ctd'><input type='text' value='' name='1133871369411' pattern='^([0-9a-f]{1,2}:){7}[0-9a-f]{1,2}$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s3267'></span></td></tr>
</table></form></div></div>

Sobald die OneWire-Konfigurationsseite aufgerufen wird, scannt der Controller zyklisch den OneWire-Bus nach angeschlossenen Devices.  
Gefundene Devices werden am unteren Ende der Seite angezeigt.  

Fett dargestellte Devices kennzeichnen neue Sensoren, die noch nicht in der OneWire-Konfiguration gespeichert sind.  
Diese Hervorhebung erleichtert das Identifizieren und Hinzufügen neu angeschlossener Sensoren.  

<table>
<tr><td>28:93:e3:95:f0:1:3c:56</td><td><button onclick='copyStringToClipboard("28:93:e3:95:f0:1:3c:56")'>Copy</button></td></tr>
<tr><td><b>28:93:e3:95:f0:1:3c:57</b></td><td><button onclick='copyStringToClipboard("28:93:e3:95:f0:1:3c:56")'>Copy</button></td></tr>
<tr><td>28:93:e3:95:f0:1:3c:58</td><td><button onclick='copyStringToClipboard("28:93:e3:95:f0:1:3c:56")'>Copy</button></td></tr>
</table>
 
Über die **Copy**-Schaltfläche kann die jeweilige Sensoradresse in die Zwischenablage kopiert werden.  



## Onewire II (Temperatur-Offset)

Hier kann für jeden OneWire-Temperatursensor ein Offset eingestellt werden, um die gemessene Temperatur zu korrigieren.

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr><td class='Ctd2' colspan='3'><b>Onewire Sensoren</b></td></tr>
<tr><td colspan='3'><b>Sensor 0</b></td></tr><tr class='Ctr'><td class='Ctd'><b>Offset</b></td>
<td class='Ctd'><input type='number' step='0.01' min='-10' max='10' value='0.20' name='30064774400'></td><td class='t1'>&deg;C</td><td class='Ctd'><span class='secVal' id='s3328'></span></td></tr>
<tr><td colspan='3'><hr style='border:none; border-top:1px dashed black; height:1px; color:#000000; background:transparent'></td></tr><tr><td colspan='3'><b>Sensor 1</b></td></tr><tr class='Ctr'><td class='Ctd'><b>Offset</b></td>
<td class='Ctd'><input type='number' step='0.01' min='-10' max='10' value='0.00' name='30064774401'></td><td class='t1'>&deg;C</td><td class='Ctd'><span class='secVal' id='s3329'></span></td></tr>
<tr><td colspan='3'><hr style='border:none; border-top:1px dashed black; height:1px; color:#000000; background:transparent'></td></tr><tr><td colspan='3'><b>Sensor 2</b></td></tr><tr class='Ctr'><td class='Ctd'><b>Offset</b></td>
<td class='Ctd'><input type='number' step='0.01' min='-10' max='10' value='0.00' name='30064774402'></td><td class='t1'>&deg;C</td><td class='Ctd'><span class='secVal' id='s3330'></span></td></tr>
<tr><td colspan='3'><hr style='border:none; border-top:1px dashed black; height:1px; color:#000000; background:transparent'></td></tr><tr><td colspan='3'><b>Sensor 3</b></td></tr><tr class='Ctr'><td class='Ctd'><b>Offset</b></td>
<td class='Ctd'><input type='number' step='0.01' min='-10' max='10' value='0.00' name='30064774403'></td><td class='t1'>&deg;C</td><td class='Ctd'><span class='secVal' id='s3331'></span></td></tr>
</table></form></div></div>




## Bluetooth
!!! Warning "Hinweis"
    **Bluetooth steht aktuell nicht zu Verfügung!**

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='Ctd'><b>Bluetooth</b></td>
<td class='Ctd'><select name='4294967552'>
<option value='0' selected>nicht belegt</option>
<option value='1' >NEEY GW-24S4EB</option>
<option value='4' >NEEY EK-24S4EB, EK-24S10EB</option>
</select></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s256'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>MAC-Adresse</b></td>
<td class='Ctd'><input type='text' value='' name='34359738688' pattern='^([0-9a-f]{2}:){5}[0-9a-f]{2}$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s320'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Deactivate</b></td>
<td class='Ctd'><select name='4294975360'>
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
</select></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s8064'></span></td></tr>
</table></form></div></div>

Hier können bis zu 5 Bluetooth Devices festgelegt werden, von denen der Controller Daten holt.  
Dazu muss der Device-Typ und die MAC-Adresse (in Kleinbuchstaben) eingestellt werden.  

Der Controller scannt, sobald diese Konfigurationsseite aufgerufen ist, zyklisch nach neuen BT-Devices   
und zeigt die letzten 5 gefundenen am unteren Ende der Seite an.  

**Unterstützte Hardware**  
Eine Liste der unterstützten Hardware ist unter folgendem Link verfügbar: [Unterstützte Bluetooth Devices](devices/bms.md#bluetooth-devices)



## Data devices
Das **Data-Device-Mapping** dient der Zuordnung der seriellen Schnittstelle zum im BSC verwendeten internen *Data-Device*.
Diese Zuordnung ist Grundlage für weitere Konfigurationen, z. B. in den Wechselrichter-Einstellungen.

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='Ctd'><b>Schnittstelle</b></td>
<td class='Ctd'><select name='4294977728'>
<option value='255' >Nicht belegt</option>
<option value='0' >Bluetooth 0</option>
<option value='1' >Bluetooth 1</option>
<option value='2' >Bluetooth 2</option>
<option value='3' >Bluetooth 3</option>
<option value='4' >Bluetooth 4</option>
<option value='5' >Bluetooth 5</option>
<option value='6' >Bluetooth 6</option>
<option value='7' selected>Serial 0</option>
<option value='8' >Serial 1</option>
<option value='9' >Serial 2</option>
<option value='10' >Serial 3</option>
<option value='11' >Serial 4</option>
<option value='12' >Serial 5</option>
<option value='13' >Serial 6</option>
<option value='14' >Serial 7</option>
<option value='15' >Serial 8</option>
<option value='16' >Serial 9</option>
<option value='17' >Serial 10</option>
</select></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s10432'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Adresse</b></td>
<td class='Ctd'><input type='number' min='0' max='18' value='1' name='4294977792'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s10496'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Name</b></td>
<td class='Ctd'><input type='text' value='' name='1133871376704' pattern='^[^#~+]*$'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s10560'></span></td></tr>
</table></form></div></div>

Hierbei müssen folgende Parameter eingestellt werden:

  - **Schnittstelle**: Auswahl der seriellen Schnittstelle, an der das Data-Device angeschlossen ist (z.B. das BMS oder der Victron Smart Shunt) 
  - **Adresse**: Die eindeutige Adresse, die dem spezifischen Gerät zugewiesen wird oder vom Hersteller fest zugewiesen ist.
    Informationen, welche Adresse bei welchem BMS eingestellt werden muss, sind hier dokumentiert: [Unterstützte BMS – Adresskonfiguration](https://bsc-org.github.io/bsc/devices/bms/#unterstutzte-bms)  
    Der dortige Text sollte sorgfältig gelesen werden, da er beschreibt, **welche Adresse am BMS selbst** und **welche hier im Data-Device-Mapping des BSC** eingestellt werden muss.  
  - **Name** (optional): Ein benutzerdefinierter Name, der in den weiteren Einstellungen des Parameters angezeigt wird. Dieser Name wird außerdem für den MQTT-Topic des jeweiligen Devices verwendet.

    !!! Hinweis
        Der Name darf keine # und + Zeichen enthalten!

Falls mehrere Geräte an einer seriellen Schnittstelle angeschlossen sind und das BMS (Battery Management System) die Verbindung im Daisy-Chain-Modus unterstützt, ist es erforderlich, für jedes Gerät die korrekte Adresse zu definieren. Nur so kann eine eindeutige Zuordnung und eine fehlerfreie Kommunikation zwischen dem BMS und den Geräten sichergestellt werden.

!!! note "Hinweis"
    Die korrekte Konfiguration der Data Device Mappings ist essenziell, um eine störungsfreie Funktionalität zu gewährleisten. Beachten Sie die Adressierungsregeln Ihres BMS-Systems.


### Value Adjustment

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='Ctd'><b>SoC linearisieren</b></td><td class='Ctd'><input type='checkbox'  name='38654717952'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s12288'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Cellvoltage for SoC 100%</b></td>
<td class='Ctd'><input type='number' min='0' max='5000' value='0' name='12884910016'></td><td class='t1'>mV</td><td class='Ctd'><span class='secVal' id='s8128'></span></td></tr>
<tr><td colspan='3' class='td0'><div class='help'>0=deaktiviert</div></td></tr><tr class='Ctr'><td class='Ctd'><b>Cellvoltage for SoC 0%</b></td>
<td class='Ctd'><input type='number' min='0' max='5000' value='0' name='12884910208'></td><td class='t1'>mV</td><td class='Ctd'><span class='secVal' id='s8320'></span></td></tr>
<tr><td colspan='3' class='td0'><div class='help'>0=deaktiviert</div></td></tr>
</table></form></div></div>

Der "Value Adjustment" ermöglicht es, dem Wechselrichter abhängig von der Zellspannung einen angepassten State of Charge (SoC) zu übermitteln. Dabei stehen zwei Betriebsmodi zur Verfügung, die unterschiedliche Anforderungen und Verhaltensweisen abdecken.  

=== "Sponsor Firmware"
    Es stehen folgende Optionen zur Verfügung:

    - **SoC linearisieren**  
    - **Cellvoltage for SoC 100%** (in mV)
    - **Cellvoltage for SoC 0%** (in mV)

    **Cellvoltage for SoC 100%**  
    Der SoC-Wert wird erst dann auf 100 % gesetzt, wenn die eingestellte Zellspannung erreicht ist.  
    Bis dahin wird der SoC-Wert des zugeordneten Data-Devices übernommen und maximal mit 99 % angezeigt.  
    Ein Wert von `0` deaktiviert die Funktion.  

    **Cellvoltage for SoC 0%**  
    Funktioniert analog zu *Cellvoltage for SoC 100%*, jedoch für den unteren Grenzwert.  
    Der SoC wird erst auf 0 % gesetzt, wenn die definierte Zellspannung erreicht oder unterschritten ist.  
    Ein Wert von `0` deaktiviert die Funktion.  

    **SoC linearisieren**  
    Ist diese Option aktiviert, erfolgt eine lineare Berechnung des SoC-Werts zwischen den eingestellten Spannungswerten für 0% und 100%.
    

=== "Standard Firmware"
    **Hinweis:** In der Standard-Firmware steht die Option **"SoC linearisieren"** nicht zur Verfügung, da diese Funktion automatisch durch den Betriebsmodus 2 ausgeführt wird.

    ---

    **Betriebsmodus 1: Feste SoC-Setzung bei definierter Zellspannung**  
    In diesem Modus wird die Zellspannung definiert, bei der intern ein SoC von 100 % gesetzt wird.  
    Wenn die Zellspannung den eingestellten Wert erreicht oder überschreitet, wird der SoC auf 100 % gesetzt.  
    Sobald die Zellspannung unter den eingestellten Wert fällt, wird der SoC wieder vom Batterie-Management-System (BMS) übernommen.  

    **Hinweis:** Für diesen Modus muss das Feld *Cellvoltage for SoC 0%* leer bleiben.  
    Dies stellt sicher, dass nur die obere Schwelle (für 100 % SoC) berücksichtigt wird und die Berechnung des SoC allein durch das BMS erfolgt, wenn die Zellspannung unter die festgelegte Schwelle sinkt.

    **Beispiel:**  

    - Cellvoltage für SoC 100%: 3,5 V  
    - Bei einer Zellspannung von 3,5 V oder höher wird der SoC auf 100 % gesetzt.  
    - Fällt die Zellspannung unter 3,5 V, wird der SoC-Wert wieder vom BMS übernommen.

    ---

    **Betriebsmodus 2: Lineare SoC-Berechnung zwischen zwei Zellspannungsschwellen**  
    In diesem Modus werden zwei Zellspannungsschwellen definiert: Eine obere Schwelle für 100 % SoC und eine untere Schwelle für 0 % SoC.  
    Wenn die Zellspannung die obere Schwelle erreicht oder überschreitet, wird der SoC auf 100 % gesetzt.  
    Erreicht oder unterschreitet die Zellspannung die untere Schwelle, wird der SoC auf 0 % gesetzt.  
    Für Zellspannungen zwischen diesen beiden Werten wird der SoC linear berechnet.  

    **Beispiel:**  

    - Cellvoltage für SoC 100%: 3,5 V  
    - Cellvoltage für SoC 0%: 2,9 V  
    - Bei ≥ 3,5 V → SoC = 100 %  
    - Bei ≤ 2,9 V → SoC = 0 %  
    - Zwischen 2,9 V und 3,5 V → SoC linear berechnet  

    Dieser Modus ist besonders nützlich für BMS-Systeme, die keinen eigenen SoC-Wert bereitstellen, da der SoC in Abhängigkeit von den Zellspannungen automatisch ermittelt wird.


!!! danger "Wichtiger Hinweis"
    Stellen Sie sicher, dass die eingetragenen Zellspannungen den Spezifikationen des verwendeten Batteriesystems entsprechen, um eine optimale Funktion und Sicherheit zu gewährleisten.
