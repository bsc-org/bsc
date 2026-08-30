In diesem Kapitel kannst du das Entladehandling des BSC konfigurieren. Dazu gehören alle Regelungen, die den Entladestrom begrenzen – abhängig von der Zellspannung, der Temperatur oder einem Temperaturprofil – sowie die Begrenzung des Entladestroms pro Batterie-Pack.  
Die Entladeströme pro Pack werden im Kapitel [Wechselrichter](settings_inverter.md) unter [Basisdaten → Batterypack Settings](settings_inverter.md#basisdaten) hinterlegt. Die Temperaturregeln arbeiten analog zu den Laderegelungen im Kapitel [Laden](settings_inverter_charge.md).

## Entladestrom pro Pack zu groß

Mit dieser Funktion wird der Entladestrom automatisch und dynamisch angepasst, um sicherzustellen, dass der maximale Entladewert eines jeden Batterie-Packs nicht überschritten wird. Die Regelung schützt die Batterie vor Überstrom – es gelten die unter [Basisdaten → Batterypack Settings](settings_inverter.md#basisdaten) eingestellten Entladeströme pro Pack.

```bsc-settings
version: v010
file: inverterDischarge.json
profile: off
section: UI_SECT_INVERTERDISCHARGE_ENTLADESTROM_PRO_PACK_ZU_GROSS
```


## Entladestrom Zell-Spannungsabhängig drosseln

Diese Funktion dient der Anpassung des Entladestroms basierend auf der Zellspannung, um die Lebensdauer der Batteriezellen zu verlängern und deren Sicherheit zu gewährleisten.

```bsc-settings
version: v010
file: inverterDischarge.json
profile: off
section: UI_SECT_INVERTERDISCHARGE_ENTLADESTROM_ZELL_SPANNUNGSABHAENGIG_DROSSELN
```

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


## Entladestrom reduzieren - Temperatur

Mit dieser Funktion kann der maximale Entladestrom abhängig von der gemessenen Temperatur schrittweise reduziert werden. Es werden die Quellen aus der aktiven Datenquelle verwendet (Data-Devices oder Group Devices). Für die Regelung wird je nach Richtung stets der passende Grenzwert herangezogen: Von warm nach kalt gilt der Minimalwert, von kalt nach warm der Maximalwert.

Die Temperaturreduzierung erfolgt anhand von bis zu **vier konfigurierbaren Temperaturregeln**. Jede Regel kann individuell aktiviert, deaktiviert und mit eigenen Sensoren sowie Start- und Endwerten konfiguriert werden.

```bsc-settings
version: v010
file: inverterDischarge.json
profile: off
groups: 1
section: UI_SECT_INVERTERDISCHARGE_ENTLADESTROM_REDUZIEREN_TEMPERATUR
```

**Konfiguration**  

- **Data-Device Sensoren** – Temperatursensoren (0–5) der Data Devices, die für die Regelung verwendet werden.
- **Erweiterte Sensorquellen / Erweiterte Sensoren 0-31** – Zusätzliche erweiterte Temperatursensoren (z. B. OneWire) als Quelle.
- **Reduzieren Start** – Temperatur, ab der die Stromreduzierung beginnt (Standard: 20,00 °C).
- **Reduzieren Ende** – Temperatur, bei der der Entladestrom vollständig auf 0 A reduziert wird (Standard: 0,00 °C).

Die Regelung erfolgt linear zwischen den beiden Temperaturschwellen – sie kann sowohl für Drosselung bei steigenden als auch bei fallenden Temperaturen konfiguriert werden (siehe dazu die Beispiele bei [Ladestrom reduzieren – Temperatur](settings_inverter_charge.md#ladestrom-reduzieren-temperatur), die für das Entladen analog gelten).


## Entladestrom reduzieren - Temperaturprofil

Mit dieser Funktion kann der maximale Entladestrom anhand eines frei definierbaren **Temperaturprofils** begrenzt werden. Das Profil besteht aus **10 Punkten**, die jeweils einer Temperatur eine maximale **C-Rate** zuordnen. Zwischen den Punkten wird linear interpoliert; außerhalb des Profils gelten der erste bzw. letzte Punkt.

```bsc-settings
version: v010
file: inverterDischarge.json
profile: off
section: UI_SECT_INVERTERDISCHARGE_ENTLADESTROM_REDUZIEREN_TEMPERATURPROFIL
```

**Konfiguration**  

- **Data-Device Sensoren** – Temperatursensoren (0–5) der Data Devices, deren Messwerte in die Regelung einfließen.
- **Erweiterte Sensorquellen / Erweiterte Sensoren 0-31** – Zusätzliche erweiterte Sensoren (z. B. OneWire) als Quelle.
- **Temperaturprofil** – 10 Punkte mit je **Temperatur** (in °C, Schritt 0,1 °C, Bereich −30 bis 60 °C) und **C-Rate** (in C, Schritt 0,01 C).

**Funktionsweise**  
Der Entladestrom berechnet sich aus **C-Rate × Kapazität (Ah)** – die Kapazität wird unter [Basisdaten → Batterypack Settings](settings_inverter.md#basisdaten) pro Pack hinterlegt. Der berechnete Wert wird durch den maximalen Entladestrom begrenzt. Ist keine Kapazität hinterlegt, wird der Entladestrom auf 0 A begrenzt.
