## Entladestrom Zell-Spannungsabhängig drosseln

Diese Funktion dient der Anpassung des Entladestroms basierend auf der Zellspannung, um die Lebensdauer der Batteriezellen zu verlängern und deren Sicherheit zu gewährleisten.

<div class="bsc_content"><div class="content bsc_content_left"><form><table>
<tr class='Ctr'><td class='sep' colspan='3'><b>Entladestrom Zell-Spannungsabhängig drosseln</b></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Ein/Aus</b></td><td class='Ctd'><input type='checkbox'  name='38654715840'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s10176'></span></td></tr>
<tr class='Ctr'><td class='Ctd'><b>Starten bei Zellspg. kleiner</b></td>
<td class='Ctd'><input type='number' min='0' max='5000' value='0' name='12884910720'></td><td class='t1'>mV</td><td class='Ctd'><span class='secVal' id='s8832'></span></td></tr>
<tr><td colspan='3' class='td0'><div class='help'>Sobald die niedrigste Zellspannung diesen Wert unterschreitet wird die Drosselung aktiv.</div></td></tr><tr class='Ctr'><td class='Ctd'><b>End Zellspannung</b></td>
<td class='Ctd'><input type='number' min='2500' max='5000' value='3300' name='12884910784'></td><td class='t1'>mV</td><td class='Ctd'><span class='secVal' id='s8896'></span></td></tr>
<tr><td colspan='3' class='td0'><div class='help'>Sobald die niedrigste Zellspannung diesen Wert unterschreitet wird maxmial noch mit dem Mindest-Entladestrom entladen.<br>Hinweis: Der Wert muss kleiner sein als die Zell-Startspannung.</div></td></tr><tr class='Ctr'><td class='Ctd'><b>Mindest Entladestrom</b></td>
<td class='Ctd'><input type='number' min='0' max='200' value='1' name='4294976256'></td><td class='t1'>A</td><td class='Ctd'><span class='secVal' id='s8960'></span></td></tr>
</table></form></div></div>

**Parameter:**  
**Ein/Aus** (Aktivierung der Drosselung)  
Diese Option ermöglicht es, die Zellspannungsabhängige Drosselung ein- oder auszuschalten.  
Wenn aktiviert, wird der Entladestrom in Abhängigkeit von der Zellspannung angepasst.

**Starten bei Zellspannung kleiner als**  
Hier wird ein Schwellenwert festgelegt, bei dessen Unterschreitung die Drosselung des Entladestroms aktiviert wird.  
Sobald die niedrigste Zellspannung diesen Wert unterschreitet, wird die Drosselung in Kraft gesetzt, um die Zellen nicht zu stark zu entladen.

**End Zellspannung**  
Dieser Wert legt die Zellspannung fest, bei deren Unterschreitung der Entladestrom auf den "Mindest-Entladestrom" reduziert wird.

!!! note "Hinweis"
    Der End Zellspannung-Wert muss immer kleiner als die Zell-Startspannung eingestellt werden!

**Mindest-Entladestrom**  
Dies ist der minimale Entladestrom, der bei Unterschreiten der End Zellspannung nicht unterschritten wird.
