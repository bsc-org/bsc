## System
Hier findet man alle System-Internen Einstellmöglichkeiten, wie z.B. Benutzernamen und Passwörter zu den WLAN und MQTT Logins.

```bsc-settings
version: v010
file: system.json
profile: off
index: 1
```

- **Device Name**  
  Benutzerdefinierter Gerätename (Standard: `BSC`). Dieser Name wird auch auf dem Dashboard angezeigt.  

- **Display Timeout**  
  Zeitspanne bis zur automatischen Deaktivierung des angeschlossenen Displays (Timeout).  

- **Profilumschaltung**  
  Mit den Profilen P1/P2 lassen sich profilfähige Parameter in zwei Varianten pflegen (z. B. Sommer-/Winterbetrieb). Mögliche Modi:
    - **Aus** – Es wird das Profil P1 verwendet.
    - **P1** / **P2** – Es wird dauerhaft das gewählte Profil verwendet.
    - **Trigger** – Der unter *Profil-Trigger* ausgewählte Trigger entscheidet: Trigger inaktiv → P1, Trigger aktiv → P2.
  
  Das Feld **Profil-Trigger** wird nur angezeigt, wenn als Modus `Trigger` gewählt ist.  
  Profilfähige Parameter sind in den Einstellungsseiten an den P1/P2-Feldern erkennbar.

- **Traceback-Trigger**  
  Setzt die ausgewählten Trigger, wenn ein Traceback (Absturzbericht) vorhanden ist.  
  Diese Option wird **nur auf T-Connect-Hardware** angezeigt.

### Benutzer

```bsc-settings
version: v010
file: system.json
profile: off
section: UI_SECT_SYSTEM_BENUTZER
```

- **Passwortschutz aktivieren**  
  Schaltet die Anmeldung am Webinterface ein oder aus. Ist der Passwortschutz **deaktiviert**, ist das Webinterface ohne Anmeldung zugänglich – auch die [REST-API](restapi.md) kann dann ohne Anmeldung genutzt werden.

- **Automatisch abmelden**  
  Zeitspanne (0–240 Minuten), nach der eine inaktive Sitzung automatisch beendet wird. Der Wert **0** deaktiviert den automatischen Logout.

- **Benutzer**  
  Es können bis zu **2 Benutzer** angelegt werden. Pro Benutzer:
    - **Benutzername** / **Passwort** – Zugangsdaten für das Webinterface. Das Passwort wird nicht im Klartext, sondern gehasht gespeichert.
    - **Rolle** – `Admin` (vollständiger Zugriff) oder `ReadOnly` (nur lesender Zugriff auf die Einstellungen).

## Netzwerkeinstellungen

```bsc-settings
version: v010
file: system.json
profile: off
section: UI_SECT_SYSTEM_WLAN
```

- **WLAN SSID**  
  Name des WLAN-Netzwerks, mit dem sich der BSC verbinden soll.  

- **WLAN Passwort**  
  Passwort für die Anmeldung am angegebenen WLAN-Netzwerk.  

- **WLAN Connect Timeout**  
  Maximale Zeit (in Sekunden), die der BSC auf eine erfolgreiche WLAN-Verbindung wartet, bevor der Verbindungsversuch abgebrochen wird. Wird innerhalb dieser Zeit keine Verbindung hergestellt, erstellt das Gerät automatisch einen eigenen Access Point (AP).  
  Wird der Wert auf **0** gesetzt, ist der Timeout deaktiviert und der Verbindungsversuch wird unbegrenzt fortgesetzt.  
  <br> 
  Verliert der BSC die WLAN-Verbindung und erstellt nach dem eingestellten Timeout einen Access Point, versucht er alle **5 Minuten**, die Verbindung mit dem ursprünglichen WLAN-Netzwerk erneut herzustellen. 

- **Ethernet**  
  Bei aktiviertem Ethernet (nur auf T-Connect-Hardware mit Ethernet-Anschluss verfügbar) wird WLAN deaktiviert und die Verbindung über den LAN-Anschluss aufgebaut.

```bsc-settings
version: v010
file: system.json
profile: off
section: UI_SECT_SYSTEM_STATIC_IP
```

- **IP-Adresse**  
  Statische IPv4-Adresse des BSC.  
  Wenn dieses Feld leer bleibt, wird die IP-Adresse automatisch über DHCP bezogen.  

- **Gateway**  
  IPv4-Adresse des Standard-Gateways, das für die Netzwerkverbindung genutzt wird.  

- **Subnet**  
  Subnetzmaske für das lokale Netzwerk (z. B. `255.255.255.0`).  

- **DNS (Optional)**  
  IPv4-Adresse eines DNS-Servers zur Namensauflösung. Falls leer, wird der vom DHCP-Server bereitgestellte DNS-Server verwendet.  


## MQTT-Einstellungen {: #mqtt }

```bsc-settings
version: v010
file: mqtt.json
profile: off
label: MQTT Allgemein
```

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
  Zeitintervall in Sekunden, in dem der BSC Daten an den MQTT-Broker sendet (einstellbar von 1–120 s, Standard 60 s).  
  <br>
  Die Datenkategorien (Data Devices, Group Devices, OneWire, Inverter) werden aufeinanderfolgend in je einem Sendezyklus übertragen. Die Inverter-Werte werden zusätzlich nur in jedem 15. Inverter-Zyklus veröffentlicht.

- **Remanenz vTrigger**  
  Mit "Remanenz vTrigger" kann festgelegt werden, welcher vTrigger als speichernd definiert werden soll.  
  Ein speichernder vTrigger stellt sicher, dass seine Werte auch nach einem Neustart (Reboot) oder einem Spannungsausfall automatisch wiederhergestellt werden.  
  Mehr zum Thema vTrigger unter [MQTT](mqtt.md#virtual-trigger).

Die weiteren MQTT-Einstellungen (MQTT-Filter, Home-Assistant-Auto-Discovery) sind auf der Seite [MQTT](mqtt.md) dokumentiert.


## Zeitserver (NTP)

```bsc-settings
version: v010
file: system.json
profile: off
section: UI_SECT_SYSTEM_NTP
```

!!! note "Hinweis"
    Zum Übernehmen der NTP-Settings muss der BSC neu gestartet werden!

- **Server Name/IP**  
  Name oder IPv4-Adresse des NTP Servers.  

- **Zeit-Offset**  
  Abweichung der lokalen Zeitzone von UTC in Stunden (−12 bis +14, Standard: +1 für Mitteleuropa). Der BSC gleicht die Systemzeit über NTP aus und wendet diesen Offset für die lokale Zeit an.
  
Falls bei der Verwendung eines externen NTP-Servers Probleme mit der Zeitsynchronisierung auftreten, kann alternativ der Router des lokalen Netzwerks als Zeitserver genutzt werden. Diese Methode ist in vielen Fällen stabiler.  

**Beispiel (AVM FritzBox):**  
In der FritzBox kann der Zeitserver im Menü  
`Heimnetz → Netzwerk → Netzwerkeinstellungen`  
aktiviert werden.  

Als Zeitserver können beispielsweise folgende Adressen definiert werden:  
`ntp1.t-online.de; 2.europe.pool.ntp.org`  

Im BSC ist anschließend die **IP-Adresse** des Routers als NTP-Server anzugeben.  
**Hinweis:** Die Verwendung eines Hostnamens anstelle der IP-Adresse kann zu Verbindungsproblemen führen.
