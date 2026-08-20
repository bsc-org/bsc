# Wechselrichter
In diesem Abschnitt werden die Einstellungen für die Kommunikation mit dem Wechselrichter über den CAN-Bus sowie die Verarbeitung der bereitgestellten Messwerte konfiguriert. Über die CAN-Bus-Schnittstelle werden Betriebsdaten wie Ladezustand, Gesamtspannung, Strom und Temperatur an den Wechselrichter übertragen. Die Wahl der Datenquelle legt fest, welche Geräte als Referenz für einzelne Messgrößen dienen. Bei Bedarf können Werte aus mehreren Quellen zusammengefasst werden.  


## General

```bsc-settings
version: v010
file: bmsToInverter.json
profile: off
index: 1
```

**BMS Canbus enable**  
Aktiviert oder deaktiviert die generelle CAN-Bus-Kommunikation des BMS.  
Wenn deaktiviert, werden keine Daten über den CAN-Bus an Wechselrichter gesendet.

**Canbus protocol**  
Legt fest, welches Kommunikationsprotokoll für den angeschlossenen Wechselrichter verwendet wird (Standard: `nicht belegt`).  
Für die meisten Wechselrichter sollte das Protokoll **Pylontech** gewählt werden.  

**Send extended data**  
Steuert, ob erweiterte Datenpakete zusätzlich über den CAN-Bus gesendet werden.  

Diese Option kann **nur** in Verbindung mit einer **Victron-Anlage** genutzt werden und erfordert dort einen entsprechenden Treiber, der [hier](https://github.com/shining-man/dbus-bsc-can) verfügbar ist.  
**Nicht** empfohlen für den Einsatz in Verbindung mit einem **CerboGX**, da dies zu Kommunikationsproblemen führen kann.

**Datenquelle**  
Hier werden die **Data-Devices** ausgewählt, deren Messwerte als Grundlage für **alle Laderegelungen** dienen. Diese Daten werden vom BSC **aufbereitet** und anschließend an den **Wechselrichter** übermittelt.

Wichtig: Je nach **aktiver Laderegelung** müssen die ausgewählten Datenquellen **Zellspannungen liefern** – sonst kann die Regelung nicht korrekt arbeiten.

An dieser Stelle werden **nicht** die Datenquellen ausgewählt, die **nur** für **Gesamtspannung**, **Gesamtstrom** oder den **SoC** verwendet werden sollen (z. B. ein **Shunt**) – das erfolgt unter [Valuehandling](#valuehandling-multi-bms).

!!! note "Hinweis"
    Sind [Group Devices](settings_bsc_devices.md#group-devices-batterie-gruppen) aktiviert, kann hier anstelle der Data-Devices eine **Battery-Pack-Auswahl** (Group Devices) getroffen werden.


## Valuehandling {: #valuehandling-multi-bms }
In diesem Abschnitt werden die Quellen und Methoden zur Verarbeitung zentraler Batteriewerte festgelegt. Dabei kann für jeden Messwerttyp – Ladezustand (SoC), Gesamtspannung und Gesamtstrom – eine spezifische Datenquelle ausgewählt werden. Die verfügbaren Datenquellen stammen aus den angeschlossenen Data Devices und liefern die Rohwerte für die weitere Verarbeitung.  

Zusätzlich kann eingestellt werden, wie die Werte bei der Auswahl von mehreren Data Devices aggregiert werden sollen.  

```bsc-settings
version: v010
file: bmsToInverter.json
profile: off
section: UI_SECT_BMSTOINVERTER_VALUEHANDLING
```

**Domain**  
Mit der Domain wird festgelegt, aus welchem Bereich die Quellen stammen:

- **Auto** – Automatische Auswahl (Data Devices; bei aktivierten Group Devices: Battery-Packs).
- **Data devices** – Es werden die konfigurierten Data-Devices angeboten.
- **Group devices** – Es werden die konfigurierten Group Devices (Battery-Packs) angeboten. Nur verfügbar, wenn [Group Devices](settings_bsc_devices.md#group-devices-batterie-gruppen) aktiviert sind.

**Quelle SoC**  
Legt fest, von welchem angeschlossenen Gerät (Data Device bzw. Group Device) der Ladezustand der Batterie (State of Charge, SoC) übernommen wird.  
Wird nur ein Gerät als Quelle verwendet, bestimmt ausschließlich dessen Wert den SoC im System.

**Aggregation SoC**  
Definiert die Methode, mit der der SoC berechnet wird, wenn mehrere Datenquellen gleichzeitig ausgewählt wurden.  
Mögliche Aggregationsmethoden sind **Mittelwert**, **höchster Wert**, **niedrigster Wert**, **BMS** oder **Kapazitätsgewichtet**. Bei der Auswahl **BMS** wird der SoC des ersten ausgewählten Data-Device an den Wechselrichter übermittelt. Bei **Kapazitätsgewichtet** fließen die SoC-Werte entsprechend der in den [Basisdaten](#basisdaten) hinterlegten Pack-Kapazitäten gewichtet ein.

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

```bsc-settings
version: v010
file: bmsToInverter.json
profile: off
section: UI_SECT_BMSTOINVERTER_BASISDATEN
```

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

**Float Ladespannung SoC**  
Legt den Ladezustand (State of Charge) fest, bei dessen Unterschreiten von der Float-Ladespannung zurück auf die Absorptionsladespannung gewechselt wird.  
Diese Funktion sorgt dafür, dass bei sinkendem Ladezustand erneut eine vollständige Ladung initiiert wird.

!!! note "Hinweis"
    Bitte beachten Sie, dass ein zu hoch gewählter SoC-Wert unter Umständen das System sofort wieder in die Absorption-Phase zurückführen kann.  
    Auch ungenaue SoC-Werte der angeschlossenen BMS können diesen Phasenwechsel verfälschen. Für eine präzise SoC-Erfassung empfiehlt sich ein externer Shunt (siehe [hier](devices/externer_shunt.md)).

!!! note "Profilumschaltung"
    Absorption Ladespannung, Float Ladespannung und Float Ladespannung SoC sind **profilfähig** (P1/P2). Bei aktivierter [Profilumschaltung](settings_bsc.md#system) gelten die Werte des aktiven Profils.

**Max. Ladestrom**  
Dies ist der **maximale Strom**, der an den Wechselrichter übermittelt wird und den dieser als **Begrenzung für den Ladevorgang** verwendet.  
Damit wird sichergestellt, dass die Ladeleistung nicht über die zulässigen Werte hinausgeht und Batterie sowie Ladegeräte vor Überlastung geschützt werden.

**Max. Entladestrom**  
Dies ist der **maximale Strom**, der an den Wechselrichter übermittelt wird und den dieser als **Begrenzung für den Entladevorgang** verwendet.  
So wird verhindert, dass die Batterie mit zu hohen Strömen belastet werden.

**SoC auf 100**  
Setzt den Ladezustand im System auf 100 %, wenn einer der definierten Trigger aktiviert wird.  

**SoC auf 0**  
Setzt den Ladezustand im System auf 0 %, wenn einer der definierten Trigger aktiviert wird.  

**Batterypack Settings**  
Mit dieser Funktion können Sie einen Lade- oder Entlade-Überstrom vermeiden, wenn einzelne Battery-Packs im System abgeschaltet werden. 

Das Battery Safety Controller (BSC) sorgt dafür, dass der zuvor definierte maximale Lade- und Entladestrom an den Inverter übermittelt wird. Je nach Anzahl der parallel geschalteten Packs müssen Sie diesen Stromwert individuell festlegen. Sollte nun ein Battery Management System (BMS) eines Packs eingreifen und das Pack vom Netz nehmen, besteht die Möglichkeit, dass die verbleibenden Packs den vollen Strom des ausgefallenen Packs übernehmen. Dies könnte zu einem Überstrom führen.

Um dies zu verhindern, können Sie mit dieser Funktion einen maximalen Strom pro Pack definieren. Das BSC reagiert automatisch auf den Ausfall eines Packs und passt den maximalen Strom an die verbleibenden Packs an.

Beispiel: Angenommen, Sie haben einen maximalen Ladestrom von 180A definiert und drei Packs, bei denen jeweils ein maximaler Strom von 100A festgelegt ist. Sollte nun ein Pack ausfallen, würde der verbleibende Strom von 200A noch innerhalb des zulässigen Rahmens liegen. Fällt ein weiteres Pack aus, würde der Ladecontroller den Strom automatisch auf 100A begrenzen, um das verbleibende Pack vor einem Überstrom zu schützen.


## Triggerbasierte Begrenzungen

```bsc-settings
version: v010
file: bmsToInverter.json
profile: off
section: UI_SECT_BMSTOINVERTER_TRIGGER_BEGRENZUNGEN
```

**Ladeleistung auf 0**  
Setzt den Ladestrom auf 0 A, wenn einer der zugeordneten Trigger (Trigger 1–27) aktiviert wird.  

**Entladeleistung auf 0**  
Setzt den Entladestrom auf 0 A, wenn einer der zugeordneten Trigger (Trigger 1–27) aktiviert wird.  

**Triggerbasierte Strombegrenzung**  
Es stehen **3 Regeln** zur Verfügung. Pro Regel:

- **Trigger** – Trigger (Trigger 1–27), bei denen die Begrenzung aktiv wird.
- **Laden max.** / **Entladen max.** – Maximaler Lade- bzw. Entladestrom (0–1000 A), der bei aktivem Trigger als Obergrenze an den Wechselrichter übermittelt wird.

Bei aktivem Trigger gelten die Werte als Obergrenze. Sie übersteuern die festgelegten Maximalwerte nicht – es wirkt immer der kleinere Wert.


## Ladespannungsrampe

Die Funktion **Ladespannungsrampe** sorgt dafür, dass Änderungen der Ladespannung – beispielsweise beim Übergang von Float auf Absorption – nicht sprunghaft, sondern in langsamen, definierten Schritten erfolgen. Damit werden abrupte Spannungsänderungen vermieden und Belastungsspitzen an Batterie und System reduziert.

!!! note "Hinweis zur Supporter-Firmware"
    Die Ladespannungsrampe ist auch Bestandteil der separat erhältlichen **Supporter-Firmware** (Classic WebUI). Weitere Informationen: [Supporter](supporter.md).

```bsc-settings
version: v010
file: bmsToInverter.json
profile: off
section: UI_SECT_BMSTOINVERTER_LADESPANNUNGSRAMPE
```

**Modus**  

- **Aus** – Die Ladespannung wird direkt auf den Zielwert gesetzt.
- **Zeitrampe** – Die Ladespannung wird in festen Schritten von **100 mV** angepasst. Die Zeitdauer pro Schritt wird über *Zeit pro Spannungsschritt* eingestellt (Standard: 15 s). Die Anpassung erfolgt kontinuierlich, bis die eingestellte Zielspannung erreicht ist – sowohl bei Erhöhung als auch bei Absenkung der Ladespannung.
- **Auto** – Erhöhungen erfolgen wie bei der Zeitrampe; Absenkungen erfolgen **spannungsgeführt** über die aktuelle Batteriespannung. Dabei wird der Ladestrom kurzzeitig auf 0 A gesetzt, bis die Zielspannung erreicht ist.

**Zeit pro Spannungsschritt (s)**  
Bestimmt, in welchem Intervall die Ladespannung in 100 mV-Schritten angepasst wird (1–240 s, Standard 15 s).

**Hinweis**:   
Die Ladespannungsrampe wird bei jeder Änderung der Sollspannung aktiv, sofern diese Funktion aktiviert ist.


## Batterietemperatur

Hier wird festgelegt, von welchem Data Device die Batterietemperatur übernommen und an den Wechselrichter übermittelt werden soll.  

```bsc-settings
version: v010
file: bmsToInverter.json
profile: off
section: UI_SECT_BMSTOINVERTER_BATTERIETEMPERATUR
```

**Quelle**  
Das Data-Device, dessen Temperatur übertragen wird (`nicht belegt` = 255 deaktiviert die Temperaturübertragung). Sind [Group Devices](settings_bsc_devices.md#group-devices-batterie-gruppen) aktiviert, wird hier stattdessen ein **Battery-Pack** (Group Device) ausgewählt.

**Sensortyp** (nur bei aktivierten Group Devices)  
Legt fest, ob die **Data-Device Sensoren** (0–5) oder die **Erweiterten Sensoren** (0–31) der Gruppe verwendet werden.

**Sensornummer**  
Nummer des Temperatursensors der gewählten Quelle: Data-Device Sensoren 0–5, Erweiterte Sensoren 0–31.


## Zelltemperatur

Hier wird festgelegt, von welchen Sensoren der als Datenquelle ausgewählten Data Devices die minimale und maximale Zelltemperatur ermittelt und an den Wechselrichter übermittelt wird.  

```bsc-settings
version: v010
file: bmsToInverter.json
profile: off
section: UI_SECT_BMSTOINVERTER_ZELLTEMPERATUR
```

!!! note "Hinweis zur Supporter-Firmware"
    Die Zelltemperatur-Auswahl ist auch Bestandteil der separat erhältlichen **Supporter-Firmware** (Classic WebUI). Weitere Informationen: [Supporter](supporter.md).


## Alarme (Inverter)

Über diese Einstellungen können Alarme im Wechselrichter über Trigger ausgelöst werden.  

```bsc-settings
version: v010
file: bmsToInverter.json
profile: off
section: UI_SECT_BMSTOINVERTER_ALARME_INVERTER
```

Die vier Alarme (**High battery voltage**, **Low battery voltage**, **High Temperature**, **Low Temperature**) werden an den Wechselrichter gemeldet, wenn mindestens einer der jeweils zugeordneten Trigger (Trigger 1–27) aktiv ist.


## Trigger bei SoC
Mit dieser Funktion kann ein Trigger ausgelöst werden, wenn ein bestimmter Ladezustand (SoC) der Batterie über- oder unterschritten wird.  
Dadurch lassen sich beispielsweise externe Geräte abhängig vom SoC-Wert schalten.  
Es stehen **4 Regeln** zur Verfügung.

```bsc-settings
version: v010
file: bmsToInverter.json
profile: off
section: UI_SECT_BMSTOINVERTER_TRIGGER_BEI_SOC
```

**Parameter:**  
**SoC - Trigger ein**: Definiert den SoC-Wert, bei dem der Trigger aktiviert wird (Standard: 95 %).  
**SoC - Trigger aus**: Definiert den SoC-Wert, bei dem der Trigger wieder deaktiviert wird (Standard: 80 %).  

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
