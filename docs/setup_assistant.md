# Einrichtungsassistenten

Die WebApp bietet **vier Einrichtungsassistenten**, die die Erstkonfiguration Schritt für Schritt begleiten. Die Assistenten sind über das Menü der WebApp erreichbar und schreiben direkt die zugehörigen Einstellungsseiten.

## Netzwerk

Konfiguriert die WLAN-Grundverbindung:

- **WLAN SSID** – Name des WLAN-Netzwerks.
- **WLAN Passwort** – Passwort des WLAN-Netzwerks.

## MQTT

Geführte MQTT-Einrichtung in vier Schritten (mit Zusammenfassung am Ende):

1. **Aktivierung** – MQTT global ein- oder ausschalten.
2. **Verbindung** – MQTT-Server (Broker-IP), MQTT-Port und MQTT Device Name.
3. **Login und Topic** – Optionale Zugangsdaten (Username/Passwort) und der MQTT Topic Name.
4. **Sendeverhalten** – Sendeintervall in Sekunden.

## Serielle Schnittstellen

Konfiguriert die an **Serial 0–2** angeschlossenen Geräte (Gerätetyp und Anzahl der Geräte in der Kette) und **befüllt anschließend automatisch das Data-Device-Mapping**: Für jedes angegebene Gerät wird ein Data-Device mit der passenden Schnittstelle und fortlaufender Adresse angelegt.

## Wechselrichter

Konfiguration des Wechselrichters und der Basis-Laderegelung in vier Schritten (mit Zusammenfassung am Ende):

1. **CAN aktivieren und Protokoll auswählen** – Der Assistent setzt *BMS Canbus enable* automatisch, wählt das CANBUS-Protokoll und übernimmt die aktiven Data-Devices als Datenquelle.
2. **Basisdaten** – Anzahl Zellen und maximale Zellspannung werden abgefragt; daraus berechnet der Assistent **Absorption Ladespannung** (max. Zellspannung × Zellanzahl, auf 0,1 V aufgerundet), **Float Ladespannung** (3,37 V × Zellanzahl) und **Float Ladespannung SoC** (90 %).
3. **Zellspannungsabhängige Drosselung** – Aktiviert die Ladestrom-Drosselung und setzt Start-Zellspannung, Maximale Zellspannung (Float) und Mindest-Ladestrom auf bewährte Werte (3370 mV / 0 A).
4. **Zelldrift-Drosselung** – Aktiviert die Zelldrift-Drosselung mit Start-Zellspannung 3400 mV, Start-Drift 20 mV und 2 A Reduzierung pro mV.

!!! note "Hinweis"
    Die Assistenten setzen ausschließlich die aufgelisteten Parameter. Alle übrigen Einstellungen bleiben unverändert und können anschließend in den jeweiligen Einstellungsseiten angepasst werden.
