In diesem Kapitel können Sie neben der Definition des angeschlossenen Wechselrichters auch das Lade- und Entladehandling konfigurieren.  
Alle prozentualen Limitierungen beziehen sich auf die in der Kategorie "[Basisdaten](settings_inverter.md#basisdaten)" eingestellten Werte.

Beispiel eines Ladezyklus inkl. Balancing-, Float- und Absorption-Voltage mit Hilfe des BSC und einer Visualisierung über HomeAssistant/Grafana:  
![](img/settings/settings_inverter_charge_beispiel.png){  width="1300" }   


## Dynamischer Ladespannungsoffset

Mit dieser Funktion kann die Ladespannung dynamisch in Abhängigkeit vom aktuellen Ladestrom angepasst werden.  
Der Offset wird linear in Relation zum Ladestrom berechnet. Für die Berechnung wird stets der kleinste Ladestrom aller Batterypacks herangezogen.  
Durch die Funktion kann ein Spannungsabfall auf der Leitung kompensiert werden.  

```bsc-settings
version: v010
file: inverterCharge.json
profile: off
section: UI_SECT_INVERTERCHARGE_DYNAMISCHER_LADESPANNUNGSOFFSET
```

**Parameter**  
**Ein/Aus**: Aktiviert oder deaktiviert die Funktion.  
**Strom (A)**: Stromwert, bei dem der maximale Offset angewendet wird.  
**Min. Offset (mV)**: Minimaler Offset, der zur Ladespannung addiert wird. Dieser Wert wird bei einem Ladestrom von 0 A addiert.  
**Max. Offset (mV)**: Maximaler Offset, der zur Ladespannung addiert wird. Dieser Wert wird bei dem unter *Strom* eingestellten Wert addiert (Standard: 500 mV). 


## Ladestrom pro Pack zu groß

```bsc-settings
version: v010
file: inverterCharge.json
profile: off
section: UI_SECT_INVERTERCHARGE_LADESTROM_PRO_PACK_ZU_GROSS
```

Mit dieser Funktion wird der Ladestrom automatisch und dynamisch angepasst, um sicherzustellen, dass der maximale Ladewert eines jeden Batterie-Packs nicht überschritten wird. Diese intelligente Regelung schützt die Batterie vor Überstrom.

**Modus**  

- **Aus** – Funktion deaktiviert.
- **Ein** – Es gelten die unter [Basisdaten → Batterypack Settings](settings_inverter.md#basisdaten) eingestellten Ströme pro Pack.
- **C-Rate** – Der Ladestrom pro Pack wird aus der dort hinterlegten **Kapazität (Ah)** und einem Temperaturprofil berechnet (C-Rate = Strom/Kapazität). Die Regelung nutzt die Kapazität und das Temperaturprofil, um den maximalen Ladestrom des Packs zu bestimmen. Ist keine Kapazität hinterlegt, wird der Strom auf 0 A begrenzt.

Die folgende Grafik veranschaulicht die Ströme von drei Batteriepacks während eines Ladeprozesses:
![](img/settings/settings_inverter_current_per_pack_example_1.png){  width="600" }  
Grün zeigt den Stromverlauf für Pack 1, Gelb von Pack 2 und Blau von Pack 3.

In der Darstellung ist zu erkennen, dass der maximale Ladestrom für Pack 1 (grün) für eine kurze Zeit auf 50A reduziert wurde (dies ist in der Mitte des Diagramms sichtbar). Nachdem der Wert reduzierte wurde, regelt der BSC den Ladestrom dynamisch herunter und hält ihn auf den eingestellten Wert von 50A.


## Ladestrom Zell-Spannungsabhängig drosseln

Mit dieser Funktion wird der Ladestrom automatisch reduziert, sobald eine definierte Zellspannung überschritten wird.  
Dadurch lässt sich ein sanftes Erreichen der Zielspannung sicherstellen und eine Überladung einzelner Zellen vermeiden.  

```bsc-settings
version: v010
file: inverterCharge.json
profile: off
section: UI_SECT_INVERTERCHARGE_LADESTROM_ZELL_SPANNUNGSABHAENGIG_DROSSELN
```

**Ein/Aus**:  
Aktiviert oder deaktiviert die Funktion.  

**Starten bei Zellspannung größer (mV)**:  
Zellspannung, ab der die Drosselung beginnt. Sobald die höchste Zellspannung diesen Wert überschreitet, wird der Ladestrom schrittweise reduziert.  

**Maximale Zellspannung (mV)**:  
Zellspannung, ab der nur noch mit dem eingestellten Mindest-Ladestrom geladen wird. Dieser Wert muss größer sein als die Startspannung.

**Maximale Zellspannung (Float) (mV)**:  
Separater Maximalwert für die Float-Phase.  
Einstellung **0** = deaktiviert: Es wird dann auch bei Float die maximale Zellspannung genommen. 

**Mindest-Ladestrom (A)**:  
Untergrenze des Ladestroms, auf die bei Erreichen der maximalen Zellspannung reduziert wird.  
  
!!! warning "Achtung"
    Ist der **Autobalancer aktiviert** und erreicht den Zustand Aktiv, wird die maximale Zellspannung automatisch durch die *Maximale Zellspannung* aus dem [Autobalance-Abschnitt](#autobalance) ersetzt.


## Ladestrom reduzieren bei Zelldrift

Mit dieser Funktion wird der Ladestrom reduziert, sobald eine zu große Spannungsdifferenz (Drift) zwischen den Zellen festgestellt wird.  
Dies hilft, den Drift zu begrenzen. Ein verbauter Balancer kann so effektiv arbeiten, und die Funktion sorgt dafür, dass der Ladestrom so weit reduziert wird, dass die Spannungsabweichung nicht weiter zunimmt. 

```bsc-settings
version: v010
file: inverterCharge.json
profile: off
section: UI_SECT_INVERTERCHARGE_LADESTROM_REDUZIEREN_BEI_ZELLDRIFT
```

**Ein/Aus**:  
Aktiviert oder deaktiviert die Funktion.  

**Starten bei Zellspannung größer (mV)**:  
Zellspannung, ab der die Driftüberwachung und Stromreduzierung aktiviert wird.  

**Starten bei Drift größer (mV)**:  
Spannungsdifferenz zwischen der höchsten und niedrigsten Zelle eines Batteriepacks, ab der die Reduzierung beginnt.  

**Reduzierung pro weiterem mV-Abweichung um (A)**:  
Stromreduzierung pro zusätzlichem Millivolt Spannungsdifferenz gegenüber der gesetzten Startspannung.  
Die Berechnung erfolgt auf Basis des in den [Basissettings](settings_inverter.md#basisdaten) eingestellten Maximalstroms.  


## Ladestrom reduzieren - SoC

Mit dieser Funktion kann der Ladestrom in Abhängigkeit vom Ladezustand (State of Charge, SoC) der Batterie schrittweise reduziert werden.  
Sobald der eingestellte SoC-Wert erreicht oder überschritten wird, beginnt die Reduzierung. 

```bsc-settings
version: v010
file: inverterCharge.json
profile: off
section: UI_SECT_INVERTERCHARGE_LADESTROM_REDUZIEREN_SOC
```

**Ein/Aus**:  
Aktiviert oder deaktiviert die Funktion.  

**Reduzierung ab SoC (%)**:  
SoC-Wert, ab dem der Ladestrom reduziert wird.  

**Pro 1 % um x A reduzieren (A)**:  
Stromreduzierung pro zusätzlichem Prozentpunkt SoC oberhalb des eingestellten Startwerts. Die Berechnung erfolgt auf Basis des in den [Basissettings](settings_inverter.md#basisdaten) eingestellten Maximalstroms. 

**Mindest-Ladestrom (A)**:  
Unterer Grenzwert für den Ladestrom, der auch bei fortschreitender Reduzierung nicht unterschritten wird.  

!!! warning "Hinweis"
    Die Regel wird automatisch deaktiviert, sobald der Autobalancer auf das Erreichen der Start-Zellspannung wartet.


## Ladestrom reduzieren - Temperatur
Mit dieser Funktion kann der maximale Ladestrom abhängig von der gemessenen Temperatur schrittweise reduziert werden. Hierbei werden ausschließlich die unter *Datenquelle* ausgewählten Data Devices (bzw. Group Devices) berücksichtigt. Für die Regelung wird je nach Richtung stets der passende Grenzwert herangezogen: Von warm nach kalt gilt der Minimalwert, von kalt nach warm der Maximalwert.  

Die Temperaturreduzierung erfolgt anhand von bis zu vier konfigurierbaren **Temperaturregeln**. Jede Regel kann individuell aktiviert, deaktiviert und mit eigenen Sensoren sowie Start- und Endwerten konfiguriert werden. 

!!! note "Hinweis zur Supporter-Firmware"
    Die Temperatur-Reduzierung ist auch Bestandteil der **Supporter-Firmware**. Weitere Informationen: [Supporter](supporter.md).

```bsc-settings
version: v010
file: inverterCharge.json
profile: off
section: UI_SECT_INVERTERCHARGE_LADESTROM_REDUZIEREN_TEMPERATUR
```

!!! note "Hinweis"
    Die Regelung kann in beide Richtungen konfiguriert werden - sowohl für Drosselung bei steigenden Temperaturen als auch für Drosselung bei fallenden Temperaturen.

**Konfiguration**  
**Data-Device Sensoren**  
In diesem Bereich können die spezifischen Temperatursensoren (0–5) der Data Devices ausgewählt werden, die für die Regelung verwendet werden sollen.

**Erweiterte Sensorquellen / Erweiterte Sensoren 0-31**  
Zusätzlich können erweiterte Temperatursensoren (z. B. OneWire, Sensoren 0–31) als Quellen ausgewählt werden – die *Erweiterten Sensorquellen* bestimmen die zugehörigen Group Devices bzw. Data-Devices.

**Reduzieren Start**  
Hier wird die Temperatur definiert, ab der die Stromreduzierung beginnt (Standard: 20,00 °C). Diese kann sowohl höher als auch niedriger als die Endtemperatur sein.

**Reduzieren Ende**  
Diese Einstellung legt die Temperatur fest, bei der der Ladestrom vollständig auf 0 A reduziert wird (Standard: 0,00 °C). Liegt dieser Wert unter der Starttemperatur, wird bei fallenden Temperaturen gedrosselt.

---

**Funktionsweise**  
Die Regelung erfolgt linear zwischen den beiden konfigurierten Temperaturschwellen. Je nach Konfiguration wird der Ladestrom bei steigenden oder fallenden Temperaturen gedrosselt.

1. **Regelungsverhalten bei steigender Temperatur (Start < Ende)** (z.B. 20 °C → 40 °C)  
    - Unterhalb der Starttemperatur: Ladung mit maximalem Strom  
    - Zwischen Start- und Endtemperatur: Lineare Stromreduzierung bei steigender Temperatur  
    - Oberhalb der Endtemperatur: Ladestrom auf 0 A (Ladung gestoppt)  
  
    **Konfiguration:**  

    - Maximaler Ladestrom: 100 A  
    - Reduzieren Start: 20 °C  
    - Reduzieren Ende: 40 °C  

    **Regelungsverhalten:**  

    - Bei Temperaturen bis 20 °C: Ladung mit vollem Strom (100 A)  
    - Bei 30 °C (Mitte zwischen Start und Ende): Ladestrom auf 50 A reduziert  
    - Bei 40 °C und darüber: Ladestrom auf 0 A (Ladung gestoppt)  
<br>

2. **Regelungsverhalten bei fallender Temperatur (Start > Ende)** (z.B. 40 °C → 20 °C)

    - Oberhalb der Starttemperatur: Ladung mit maximalem Strom
    - Zwischen Start- und Endtemperatur: Lineare Stromreduzierung bei fallender Temperatur
    - Unterhalb der Endtemperatur: Ladestrom auf 0 A (Ladung gestoppt)

    **Konfiguration:**

    - Maximaler Ladestrom: 100 A
    - Reduzieren Start: 40 °C
    - Reduzieren Ende: 20 °C

    **Regelungsverhalten:**

    - Bei Temperaturen ab 40 °C: Ladung mit vollem Strom (100 A)
    - Bei 30 °C (Mitte zwischen Start und Ende): Ladestrom auf 50 A reduziert
    - Bei 20 °C und darunter: Ladestrom auf 0 A (Ladung gestoppt)

**Berechnung des aktuellen Ladestroms:**  
`
Aktueller Ladestrom = Maximaler Ladestrom × (Endtemperatur - Aktuelle Temperatur) / (Endtemperatur - Starttemperatur)
`

## Ladestrom reduzieren - Temperaturprofil

Mit dieser Funktion wird der maximale Ladestrom anhand eines frei definierbaren **Temperaturprofils** begrenzt. Das Profil besteht aus **10 Punkten**, die jeweils einer Temperatur eine maximale **C-Rate** zuordnen. Aus C-Rate und Batteriekapazität ergibt sich der zulässige Ladestrom – damit lässt sich das Laden z. B. bei tiefen Temperaturen oder bei Hitze gezielt begrenzen. Zwischen den Profilpunkten wird linear interpoliert; außerhalb des Profils gelten der erste bzw. letzte Punkt.

```bsc-settings
version: v010
file: inverterCharge.json
profile: off
section: UI_SECT_INVERTERCHARGE_LADESTROM_REDUZIEREN_TEMPERATURPROFIL
```

**Konfiguration**

**Ein/Aus**  
Aktiviert oder deaktiviert die Funktion (Standard: Aus).

**Sensorquellen**  
Es werden die Quellen der aktiven Datenquelle verwendet (Data-Devices oder Group Devices). Die Temperatur für die Regelung wird aus den folgenden Bereichen ermittelt:

- **Data-Device Sensoren** – Temperatursensoren (0–5) der Data Devices, deren Messwerte in die Regelung einfließen.
- **Erweiterte Sensorquellen** – bestimmt die Devices bzw. Group Devices, deren erweiterte Sensoren berücksichtigt werden.
- **Erweiterte Sensoren 0-31** – erweiterte Temperatursensoren (z. B. OneWire) der ausgewählten Quellen.

Sind keine Quellen ausgewählt, hat die Funktion keine Wirkung.

**Temperaturprofil**  
Das Profil besteht aus 10 Punkten mit je **Temperatur** (in °C, einstellbar in 0,1-°C-Schritten, Bereich 0–60 °C) und **C-Rate** (in C, einstellbar in 0,01-C-Schritten, Bereich 0–1 C). Im Standardprofil steigt die C-Rate von 0 °C bis 25 °C an und fällt ab 45 °C bis 60 °C wieder auf 0 C:

| Punkt | Temperatur | C-Rate |
|-------|-----------|--------|
| 1 | 0,0 °C | 0,00 C |
| 2 | 5,0 °C | 0,10 C |
| 3 | 10,0 °C | 0,20 C |
| 4 | 15,0 °C | 0,40 C |
| 5 | 20,0 °C | 0,60 C |
| 6 | 25,0 °C | 1,00 C |
| 7 | 45,0 °C | 0,50 C |
| 8 | 50,0 °C | 0,25 C |
| 9 | 55,0 °C | 0,20 C |
| 10 | 60,0 °C | 0,00 C |

**Funktionsweise**

**Temperaturwahl (Minimum oder Maximum)**  
Über alle ausgewählten Quellen und Sensoren werden die niedrigste und die höchste Temperatur ermittelt. Welcher der beiden Werte verwendet wird, entscheidet die Temperatur des Profilpunkts mit der höchsten C-Rate (im Standardprofil 25,0 °C mit 1,00 C):

- Liegt die niedrigste Temperatur **unter** dieser Referenztemperatur, gilt der **Minimalwert** – das kälteste Element bestimmt dann die Begrenzung.
- Andernfalls gilt der **Maximalwert**.

**Berechnung des Ladestroms**  
Für die verwendete Temperatur wird die C-Rate aus dem Profil bestimmt: Zwischen benachbarten Profilpunkten wird **linear interpoliert**. Unterhalb der Temperatur des ersten Punkts gilt dessen C-Rate, oberhalb der Temperatur des letzten Punkts dessen C-Rate. Bei mehreren Punkten mit identischer Temperatur zählt der erste Punkt.

Der zulässige Ladestrom berechnet sich aus **C-Rate × Kapazität (Ah)** – die Kapazität wird unter [Basisdaten → Batterypack Settings](settings_inverter.md#basisdaten) pro Pack hinterlegt. Verwendet wird die Summe der Kapazitäten der aktiven Packs (Daten nicht älter als 5 s). Ist keine Kapazität hinterlegt (0 Ah), wird der Ladestrom auf 0 A begrenzt. Der berechnete Wert wird außerdem auf den maximalen Ladestrom begrenzt und auf 0,1 A gerundet.

**Beispielrechnung (Standardprofil, Kapazität 100 Ah)**

- Sensoren melden **12 °C und 18 °C**: Die niedrigste Temperatur (12 °C) liegt unter der Referenz (25 °C), es gilt also der Minimalwert. Zwischen 10 °C (0,20 C) und 15 °C (0,40 C) ergibt die Interpolation 0,28 C → **28 A**.
- Sensoren melden **28 °C und 32 °C**: Die niedrigste Temperatur (28 °C) liegt über der Referenz, es gilt der Maximalwert. Zwischen 25 °C (1,00 C) und 45 °C (0,50 C) ergibt die Interpolation 0,825 C → **82,5 A**.
- Temperaturen unterhalb von 0 °C: Es gilt die C-Rate des ersten Punkts (0,00 C) → **0 A**.
- Temperaturen oberhalb von 60 °C: Es gilt die C-Rate des letzten Punkts (0,00 C) → **0 A**.

**Zusammenspiel mit anderen Laderegelungen**  
Das Temperaturprofil ist eine von mehreren Ladestrombegrenzungen. Der BSC berechnet alle aktiven Begrenzungen – u. a. die [zellspannungsabhängige Drosselung](#ladestrom-zell-spannungsabhangig-drosseln), die [SoC-Reduzierung](#ladestrom-reduzieren-soc), die [Zelldrift-Reduzierung](#ladestrom-reduzieren-bei-zelldrift), die [Temperaturregeln](#ladestrom-reduzieren-temperatur), den [Charge-Current Cut-Off](#charge-current-cut-off) und die Begrenzung pro Pack – und verwendet den kleinsten Wert. Das Temperaturprofil bleibt dabei auch während des Autobalancing aktiv.

Auch der Modus **C-Rate** der Funktion [Ladestrom pro Pack zu groß](#ladestrom-pro-pack-zu-gro) nutzt das Temperaturprofil – dort pro Batterie-Pack mit der jeweiligen Pack-Kapazität und dem Pack-Ladestrom als Obergrenze.


## Spannungsregelung zur Ladestrombegrenzung

Sobald die Funktion aktiviert ist, wird die Ladespannung dynamisch angepasst, um den Ladestrom innerhalb des konfigurierten Korridors zu halten. Sollte der Ladestrom den definierten Bereich überschreiten oder unterschreiten, greift die Spannungsregelung ein und korrigiert die Ladespannung entsprechend. Zusätzlich wird der an den Wechselrichter übermittelte Ladestrom auf 0 A gesetzt.  

Die Funktion ermöglicht es z.B., den Akku nur bis zu einem bestimmten SoC zu laden, um seine Lebensdauer zu verlängern.  

!!! note "Hinweis zur Supporter-Firmware"
    Die Spannungsregelung ist auch Bestandteil der **Supporter-Firmware**. Weitere Informationen: [Supporter](supporter.md).

```bsc-settings
version: v010
file: inverterCharge.json
profile: off
section: UI_SECT_INVERTERCHARGE_SPANNUNGSREGELUNG_ZUR_LADESTROMBEGRENZUNG
```

**Einstellmöglichkeiten:**  
**Ein/Aus:**  
Die Regelung kann entweder dauerhaft aktiviert oder deaktiviert werden.  
Alternativ ist es möglich, sie nur dann zu aktivieren, wenn eine definierte Triggerbedingung (Trigger 1–27) erfüllt ist. Dadurch lässt sich die Regelung beispielsweise in ein Home-Automation-System integrieren, sodass sie nur im Sommer aktiv ist und im Winter die volle Kapazität der Batterie zur Verfügung steht.

**Aktiv ab (SoC):**  
Hier kann festgelegt werden, ab welchem Ladezustand (State of Charge, SoC) die Regelung in Kraft tritt (Standard: 80 %). Dies ermöglicht eine gezielte Anpassung an verschiedene Anforderungen.

**Regelungskorridor (±):**  
Definiert den zulässigen Schwankungsbereich für den Ladestrom (Standard: 10,00 A). Innerhalb dieses Korridors erfolgt keine Regelung. Über- oder Unterschreitet der Ladestrom diesen Bereich, wird die Ladespannung automatisch angepasst.

!!! note "Hinweis"
    Die Regelung tritt ausschließlich in Kraft, wenn der Autobalancer nicht aktiv ist.  

---

Die Diagramme zeigen eine Victron-Anlage mit aktivierter Spannungsregelung. Deutlich erkennbar ist, dass der Ladestrom begrenzt wird und keine Energie in den Akku fließt. Stattdessen wird die überschüssige Energie ins Netz eingespeist, während der SoC (State of Charge) über die Zeit nahezu konstant bleibt.
![](img/settings/settings_inverter_SpgRegLadestrombegrenzungGrafana.png){ width="950" }  
![](img/settings/settings_inverter_SpgRegLadestrombegrenzungVrm.png){ width="950" }  


## Autobalance
Die Autobalance-Funktion automatisiert das regelmäßige Balancieren der Akkuzellen: Der BSC hebt dazu gezielt die Ladespannung an und bringt die Zellen in den Spannungsbereich, in dem die Balancer des BMS oder externe Balancer die Zellspannungen angleichen können.

!!! note "Wichtiger Hinweis: Der BSC balanciert nicht selbst"
    Der BSC besitzt **keine eigenen Balancing-Schaltungen** – weder ein Widerstands-Balancing (passiv) noch ein aktives Balancing auf Zellebene.
    Er hebt lediglich die Ladespannung auf die konfigurierte **Balance-Ladespannung** an, sodass die Zellen den Spannungsbereich erreichen, in dem die im BMS integrierten (passiven) Balancer oder externe aktive Balancer (z. B. Neey) aktiv werden und die Zellspannungen angleichen.

Während des Balancevorgangs setzt der BSC gezielt andere Laderegelungen aus oder koordiniert sie – Einzelheiten dazu finden Sie im Abschnitt [„Zusammenwirken mit anderen Laderegelungen“](#zusammenwirken-mit-anderen-laderegelungen).

=== "Version >= V0.10.0"

    !!! note "Neu in V0.10.0"
        * Neuer Parameter **Balance Zellspannung**: Bildet zusammen mit *Celldif. fertig* das Balanceziel (Finish-Kriterium).
        * Der Parameter **Maximale Zellspannung** (ehemals *Balance Zellspannung*) begrenzt die Zellspannung während des Autobalancing (Endspannung der Ladestrom-Reduzierung).
        * Der Parameter **Nachlaufzeit** ersetzt die bisherige *Balance Mindest-Zeit*.
        * Neue erweiterte Option **Step „Warte auf Lade-Spg.“ überspringen**.
        * Die Option *„Balance-Spg. senden, sobald Startzeitpunkt erreicht“* ist entfallen – das Verhalten ist jetzt Standard.

    ```bsc-settings
    version: v010
    file: inverterCharge.json
    profile: off
    section: UI_SECT_INVERTERCHARGE_AUTOBALANCE
    ```

    Im Folgenden werden die wichtigsten Einstellungen und Abläufe beschrieben:

    **Autobal. starten (Trigger)**
    Der hier konfigurierte Trigger ermöglicht es, den Autobalancer unmittelbar zu starten, wenn er sich aktuell in der Wartezeit bis zum nächsten Intervall befindet. Zu beachten ist, dass der Trigger nach dem Starten des Autobalancers manuell wieder auf „Low“ gesetzt werden muss.

    **Balance-Intervall**   
    Mit dem Parameter Balance-Intervall kann festgelegt werden, in welchen zeitlichen Abständen ein Balancing der Akkuzellen durchgeführt werden soll. Dieser Wert bestimmt, wie häufig die Balancierung aktiviert wird, um die Zellspannungen anzugleichen.

    **Startkriterien**   
    Der Balancierungsprozess beginnt automatisch, wenn der definierte Balance-Intervall abgelaufen ist und im zweiten Schritt die Start-Zellspannung erreicht wurde. Alternativ kann der Vorgang über den Start-Trigger unmittelbar gestartet werden.  
    Für die Start-Zellspannung wird die höchste Zellspannung der konfigurierten Data-Devices genommen.  
    Diese Startbedingungen stellen sicher, dass das Balancing unter optimalen Bedingungen durchgeführt wird.

    **Balance-Ladespannung**   
    Für den Balancierungsprozess wird die Ladespannung des Systems auf die vorab definierte Balance-Ladespannung angehoben. Diese Spannung sorgt dafür, dass der Balancierungsvorgang effektiv durchgeführt werden kann.  
    Die Balance-Ladespannung wird ab dem Step *„Warte auf Start-Zellspannung“* immer an den Wechselrichter gesendet.

    **Maximale Zellspannung**   
    Der Parameter Maximale Zellspannung gibt an, wie hoch die Spannung der einzelnen Zellen während des Balancing-Vorgangs maximal ansteigen darf. Bis zu dieser Spannung wird der Ladestrom während des Autobalancing reduziert (Endspannung der Ladestrom-Reduzierung). Dies verhindert eine Überladung der Zellen und schützt das Akkusystem vor Schäden.

    **Balance Zellspannung**   
    Die Balance Zellspannung definiert zusammen mit der Zelldifferenz (Celldif. fertig) das Balanceziel: Haben die höchste Zellspannung diesen Wert erreicht und die Zelldifferenz gleichzeitig den eingestellten Wert nicht überschritten, gilt das Balancing als fertig und der Autobalancer wechselt in den Step *„Warte auf Lade-Spg.“*.

    **Celldif. fertig**   
    Toleranz für die Zelldifferenz: Zusammen mit der Balance Zellspannung bildet dieser Wert das Finish-Kriterium. Das Balanceziel gilt als erreicht, sobald die größte Spannungsdifferenz zwischen den Zellen diesen Wert nicht überschreitet und die Balance Zellspannung erreicht ist.

    **Nachlaufzeit**   
    Nachdem die Balance-Ladespannung erreicht ist, läuft das Balancing noch die eingestellte Nachlaufzeit nach. Der Nachlaufzeit-Timer startet, sobald die Pack-Spannung 99 % der Balance-Ladespannung erreicht hat. Erst nach Ablauf der Nachlaufzeit wird der Vorgang beendet.

    **Beendigung des Balancierungsprozesses**   
    Das Balanceziel gilt als erreicht, sobald die Balance Zellspannung erreicht und die eingestellte Zelldifferenz nicht überschritten wird. Der Vorgang selbst wird beendet, sobald anschließend die Pack-Spannung 99 % der Balance-Ladespannung erreicht hat und die Nachlaufzeit abgelaufen ist. Danach wird die Ladespannung wieder auf das Floating-Niveau abgesenkt.

    **Timeout**   
    Mit dem Parameter Timeout wird festgelegt, nach welcher maximalen Zeit der Balancierungsprozess automatisch abgebrochen wird, falls das Balanceziel nicht innerhalb des vorgesehenen Zeitrahmens erreicht werden konnte. Nach einem Abbruch wechselt der Autobalancer in den Step *„Warte auf nächsten Tag“* und wartet 12 Stunden, bevor erneut versucht wird, das Balancing zu starten. Dies schützt das System vor endlosen Balancierungszyklen.

    **Erweiterte Optionen**  

    - **Bei Start-Zellspg.-Unterschreitung → Step 'Warte auf Start-Zellspg.'**  
    Ist diese Option aktiv, wird bei Unterschreiten der definierten Start-Zellspannung erneut in den Schritt *„Warte auf Start-Zellspg.“* gewechselt. Dadurch werden auch die laufenden Timer zurückgesetzt.  
    - **CutOff ab Step 'Warte auf Start-Zellspg.' deaktivieren**  
    Mit dieser Option wird die CutOff-Funktion bereits im Schritt *„Warte auf Start-Zellspg.“* deaktiviert. Ohne diese Option wird die CutOff-Funktion ab dem Schritt *„Warte auf Zellspannung/Differenz“* deaktiviert.  
    - **Step 'Warte auf Lade-Spg.' überspringen**  
    Mit dieser Option wechselt der Autobalancer beim Erreichen des Balanceziels (Balance Zellspannung und Zelldifferenz) direkt in die Nachlaufzeit. Der Nachlaufzeit-Timer startet in diesem Fall sofort. Der Rückfall auf die Pack-Spannung (99 % der Balance-Ladespannung) entfällt mit dieser Option.  

    !!! note "Nach dem Balancing"
        Nach Abschluss des Balancierungsprozesses wird die Ladespannung auf das Floating-Niveau abgesenkt, um den Akku im geladenen Zustand zu halten, ohne ihn weiter zu belasten.

    !!! note "Hinweise"
        * Nach einem Neustart des BSC ist keine Wartezeit bis zum ersten Balancing. Erst nach dem ersten Balancing startet der eingestellte Balance-Interval.
        * Wurde das BSC beispielsweise um 22:00 Uhr gestartet und ein Intervall von fünf Tagen eingestellt, erfolgt das nächste Balancing nicht am Morgen des fünften Tages, sondern erst am Abend des fünften Tages. Da zu diesem Zeitpunkt keine Sonnenenergie zur Verfügung steht, wird das Balancing erst am nächsten Tag gestartet, an dem die Sonne scheint.
        * Für verschiedene BMS, z.B. dem Seplos, kann die einstellbare Nachlaufzeit genutzt werden, um den SoC 100 zu setzen   

    Den genauen Ablauf des Balance-Vorgangs kann mit dem MQTT-Topic "/Inverter/autoBalState" visualisiert werden.  
    Funktion der sieben verfügbaren States:

    - 0: Autobalancing ist deaktiviert
    - 1: BSC wartet auf den Starttag (das Start-Intervall läuft)
    - 2: Balancing wurde nicht fertig und es wird am nächsten Tag wiederholt (Wartezeit 12 h)
    - 3: Startzeitpunkt erreicht; BSC wartet auf die Start-Zellspannung
    - 4: Start-Zellspannung erreicht; BSC wartet auf das Balanceziel (Balance Zellspannung und Zelldifferenz)
    - 5: Balanceziel erreicht; BSC wartet darauf, dass die Pack-Spannung 99 % der Balance-Ladespannung erreicht
    - 6: Balance-Ladespannung erreicht; Nachlaufzeit läuft

    Ablauf:

    1. **Warte auf Starttag**:  
      Bei Aktivierung des Autobalancers wechselt der Zustand in den Step *„Warte auf Starttag“*. Das Start-Intervall läuft ab diesem Zeitpunkt.
    2. **Warte auf Starttag → Warte auf Start-Zellspannung**:  
      Das Start-Intervall ist abgelaufen ODER der Start-Trigger ist aktiv.
    3. **Warte auf Start-Zellspannung → Warte auf Zellspannung/Differenz**:  
      Die höchste Zellspannung hat die eingestellte *Start Zellspannung* erreicht oder überschritten.
    4. **Warte auf Zellspannung/Differenz → Warte auf Lade-Spg.**:  
      Die höchste Zellspannung hat die *Balance Zellspannung* erreicht oder überschritten UND die größte Zelldifferenz ist nicht größer als *Celldif. fertig* (Balanceziel erreicht).
    5. **Warte auf Lade-Spg. → Nachlaufzeit**:  
      Die Pack-Spannung hat 99 % der *Balance-Ladespannung* erreicht. Der Nachlaufzeit-Timer startet.
    6. **Nachlaufzeit → Warte auf Starttag**:  
      Die *Nachlaufzeit* ist abgelaufen. Der Vorgang ist beendet.

    Weitere Übergänge:

    - **Timeout** (aus den Steps 4–6): Läuft der Autobalancer länger als die eingestellte *Timeout*-Zeit, wird der Vorgang abgebrochen und der Zustand wechselt auf *„Warte auf nächsten Tag“* (12 h Wartezeit).
    - **Rückfall (Option „Bei Start-Zellspg.-Unterschreitung…“)**: Unterschreitet die höchste Zellspannung die *Start Zellspannung*, wechselt der Autobalancer aus den Steps 4–6 zurück in den Step *„Warte auf Start-Zellspannung“*. Laufende Timer werden zurückgesetzt.
    - **Nachlaufzeit-Rückfall**: Fällt die Pack-Spannung während der Nachlaufzeit wieder unter 99 % der *Balance-Ladespannung*, wechselt der Autobalancer zurück in den Step *„Warte auf Lade-Spg.“*. Mit der Option *„Step 'Warte auf Lade-Spg.' überspringen“* entfällt dieser Rückfall.

    ??? info "Zustandsdiagramm"
        ``` mermaid
        stateDiagram-v2
            classDef movement font-style:italic;
            classDef colorOrange fill:#FFDE59
            classDef colorRed fill:#FF5757

            %% Texte
            s0: <b>Step 0</b> (Autobalancer Off)
            s1: <b>Step 1</b> (Warte auf Starttag)
            s2: <b>Step 2</b> (Warte auf nächsten Tag)
            s3: <b>Step 3</b> (Warte auf Start-Zellspannung)
            s4: <b>Step 4</b> (Warte auf Zellspannung/Differenz)
            s5: <b>Step 5</b> (Warte auf Lade-Spg.)
            s6: <b>Step 6</b> (Nachlaufzeit)
            n_setFloat: Float setzen
            n_setChargeVolt: Balance-Ladespannung setzen
            n_timeout: Timeout
            n_startNachlauf: Nachlaufzeit-Timer starten

            s0 --> s1 : Wenn Balancer Enabled
            s1 --> s3 : Wenn Start-Intervall abgelaufen oder Start-Trigger aktiv
            s2 --> s3 : Wenn 12 h abgelaufen oder Start-Trigger aktiv
            s3 --> n_setChargeVolt
            s3 --> s4 : Wenn Start-Zellspannung erreicht
            s4 --> n_setChargeVolt
            s4 --> s5 : Wenn Balance-Zellspannung erreicht und Zelldifferenz <= Celldif. fertig
            s4 --> n_startNachlauf : Option) Step 'Warte auf Lade-Spg.' überspringen
            s4 --> n_timeout
            s4 --> s3 : Option) Wenn Zellspannung wieder unter Start-Zellspannung
            s5 --> n_setChargeVolt
            s5 --> n_startNachlauf : Wenn Pack-Spannung >= 99% der Balance-Ladespannung
            s5 --> n_timeout
            s5 --> s3 : Option) Wenn Zellspannung wieder unter Start-Zellspannung
            s6 --> n_setChargeVolt
            s6 --> s5 : Wenn Pack-Spannung < 99% (nur ohne Option 'überspringen')
            s6 --> s3 : Option) Wenn Zellspannung wieder unter Start-Zellspannung
            s6 --> n_timeout
            s6 --> n_setFloat : Wenn Nachlaufzeit abgelaufen
            s6 --> s0 : Wenn Nachlaufzeit abgelaufen
            n_startNachlauf --> s6
            n_timeout --> s2 : Float setzen

            class n_setFloat colorOrange
            class n_setChargeVolt colorOrange
            class n_startNachlauf colorOrange
            class n_timeout colorRed
        ```

=== "Version < V0.10.0"
    <div class="bsc_content"><div class="content bsc_content_left"><form><table>
    <tr class='Ctr'><td class='sep' colspan='3'><b>Autobalance</b></td></tr>
    <tr class='Ctr'><td class='Ctd'><b>Ein/Aus</b></td><td class='Ctd'><input type='checkbox'  name='38654715712'></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s10048'></span></td></tr>
    <tr class='Ctr'><td class='Ctd'><b>Autobal. starten (Trigger)</b></td>
    <td class='Ctd'><select name='4294979328'>
    <option value='0' selected>Aus</option>
    <option value='1' >Trigger 1 (DI1)</option>
    <option value='2' >Trigger 2 (DI2)</option>
    <option value='3' >Trigger 3 (DI3)</option>
    <option value='4' >Trigger 4 (DI4)</option>
    <option value='5' >Trigger 5</option>
    <option value='6' >Trigger 6</option>
    <option value='7' >Trigger 7</option>
    <option value='8' >Trigger 8</option>
    <option value='9' >Trigger 9</option>
    <option value='10' >Trigger 10</option>
    </select></td><td class='t1'></td><td class='Ctd'><span class='secVal' id='s12032'></span></td></tr>
    <tr class='Ctr'><td class='Ctd'><b>Balance-Intervall</b></td>
    <td class='Ctd'><input type='number' min='1' max='30' value='5' name='4294976832'></td><td class='t1'>T</td><td class='Ctd'><span class='secVal' id='s9536'></span></td></tr>
    <tr><td colspan='3' class='td0'><div class='help'>Gibt die Tage an, nach denen wieder das Balancing gestartet werden soll.<br>Hinweis: Wenn der Autobalancer aktiv, dann ist in der Ballance-Zeit der Charge-Current Cut-Off deaktiviert!<br>Es muss die richtige Anzahl der Zellen in den Serial-Settings eingestellt sein!</div></td></tr><tr class='Ctr'><td class='Ctd'><b>Start Zellspannung</b></td>
    <td class='Ctd'><input type='number' min='2500' max='5000' value='3300' name='12884911488'></td><td class='t1'>mV</td><td class='Ctd'><span class='secVal' id='s9600'></span></td></tr>
    <tr><td colspan='3' class='td0'><div class='help'>Zellspannung die erreicht sein muss, damit der Vorgang beginnt.</div></td></tr><tr class='Ctr'><td class='Ctd'><b>Balance Mindest-Zeit</b></td>
    <td class='Ctd'><input type='number' min='0' max='600' value='0' name='12884912256'></td><td class='t1'>Min</td><td class='Ctd'><span class='secVal' id='s10368'></span></td></tr>
    <tr><td colspan='3' class='td0'><div class='help'>So lange läuft das Balancing mindestens</div></td></tr><tr class='Ctr'><td class='Ctd'><b>Balance-Ladespannung</b></td>
    <td class='Ctd'><input type='number' step='0.1' min='20' max='60' value='55.20' name='12884911552' class='fl1'></td><td class='t1'>V</td><td class='Ctd'><span class='secVal' id='s9664'></span></td></tr>
    <tr><td colspan='3' class='td0'><div class='help'>Die Max. Ladespannung wird während dem Autobalancing auf diese Spannung angehoben.</div></td></tr><tr class='Ctr'><td class='Ctd'><b>Balance-Zellspannung</b></td>
    <td class='Ctd'><input type='number' min='2500' max='5000' value='3450' name='12884911744'></td><td class='t1'>mV</td><td class='Ctd'><span class='secVal' id='s9856'></span></td></tr>
    <tr class='Ctr'><td class='Ctd'><b>Celldif. fertig</b></td>
    <td class='Ctd'><input type='number' min='0' max='50' value='5' name='4294977024'></td><td class='t1'>mV</td><td class='Ctd'><span class='secVal' id='s9728'></span></td></tr>
    <tr><td colspan='3' class='td0'><div class='help'>Balancing ist fertig, wenn die eingestellte Zelldifferenz erreicht ist.</div></td></tr><tr class='Ctr'><td class='Ctd'><b>Timeout</b></td>
    <td class='Ctd'><input type='number' min='0' max='600' value='60' name='12884911680'></td><td class='t1'>Min</td><td class='Ctd'><span class='secVal' id='s9792'></span></td></tr>
    <tr><td colspan='3' class='td0'><div class='help'>Ist in dieser Zeit das Balancing nicht fertig, wird der Vorgang abgebrochen.</div></td></tr><tr class='Ctr'><td class='Ctd'><b>Erweiterte Optionen</b></td>
    <td class='Ctd'>
    <input id='t389598300' class='toggle' type='checkbox'>
    <label for='t389598300' class='lbl-toggle'>Erweiterte Optionen</label>
    <div class='collapsible-content'>
    <div class='content-inner'>
    <fieldset style='text-align:left;'>
    <input type='checkbox' name='4294979072' value='0' >Balance-Spg. senden, sobald Startzeitpunkt erreicht<br>
    <input type='checkbox' name='4294979072' value='1' >Bei Start-Zellspg.-Unterschreitung → Step 'Warte auf Start-Zellspg.'<br>
    <input type='checkbox' name='4294979072' value='2' >CutOff ab Step 'Warte auf Start-Zellspg.' deaktivieren<br>
    </fieldset></div></div></td><td class='t1'></td></tr>
    </table></form></div></div>

    Im Folgenden werden die wichtigsten Einstellungen und Abläufe beschrieben:

    **Autobal. starten (Trigger)** *(Diese Option steht nur Supportern zur Verfügung)*  
    Der hier konfigurierte Trigger ermöglicht es, den Autobalancer unmittelbar zu starten, wenn er sich aktuell in der Wartezeit bis zum nächsten Intervall befindet. Zu beachten ist, dass der Trigger nach dem Starten des Autobalancers manuell wieder auf „Low“ gesetzt werden muss.

    **Balance-Intervall**   
    Mit dem Parameter Balance-Intervall kann festgelegt werden, in welchen zeitlichen Abständen ein Balancing der Akkuzellen durchgeführt werden soll. Dieser Wert bestimmt, wie häufig die Balancierung aktiviert wird, um die Zellspannungen anzugleichen.

    **Startkriterien**   
    Der Balancierungsprozess beginnt automatisch, wenn der definierte Balance-Intervall abgelaufen ist und im zweiten Schritt die Start-Zellspannung erreicht wurde.  
    Für die Start-Zellspannung wird die höchste Zellspannung der konfigurierten Data-Devices genommen.  
    Diese Startbedingungen stellen sicher, dass das Balancing unter optimalen Bedingungen durchgeführt wird.

    **Balance Mindest-Zeit**   
    Der Parameter Balance Mindest-Zeit gibt an, wie lange das Balancing mindestens durchgeführt werden soll, unabhängig davon, ob die Zellspannungen bereits ausgeglichen sind. Dies verhindert eine zu kurze Balancierungsdauer und sorgt für eine gründliche Anpassung der Zellspannungen.

    **Balance-Ladespannung**   
    Für den Balancierungsprozess wird die Ladespannung des Systems auf die vorab definierte Balance-Ladespannung angehoben. Diese Spannung sorgt dafür, dass der Balancierungsvorgang effektiv durchgeführt werden kann.

    **Balance-Zellspannung**   
    Der Parameter Balance-Zellspannung gibt an, wie hoch die Spannung der einzelnen Zellen während des Balancing-Vorgangs maximal ansteigen darf. Dies verhindert eine Überladung der Zellen und schützt das Akkusystem vor Schäden.

    **Beendigung des Balancierungsprozesses**   
    Der Vorgang wird automatisch beendet, sobald die Differenz zwischen den Zellspannungen den eingestellten Wert erreicht oder unterschreitet. Dadurch wird sichergestellt, dass alle Zellen gleichmäßig geladen sind und keine übermäßige Disparität besteht.

    **Timeout**   
    Mit dem Parameter Timeout wird festgelegt, nach welcher maximalen Zeit der Balancierungsprozess automatisch abgebrochen wird, falls die Zellspannungen nicht innerhalb des vorgesehenen Zeitrahmens ausgeglichen werden konnten. Dies schützt das System vor endlosen Balancierungszyklen.

    **Erweiterte Optionen**  

    - **Ballance-Spg. senden, sobald Startzeitpunkt erreicht**  
    Wenn diese Option aktiviert ist, wird die Balance-Spannung gesendet, sobald der festgelegte Startzeitpunkt erreicht ist.  
    - **Bei Start-Zellspg.-Unterschreitung → Step 'Warte auf Start-Zellspg.'**  
    Ist diese Option aktiv, wird bei Unterschreiten der definierten Start-Zellspannung erneut in den Schritt *„Warte auf Start-Zellspg.“* gewechselt. Dadurch werden auch die laufenden Timer zurückgesetzt.  
    - **CutOff ab Step 'Warte auf Start-Zellspg.' deaktivieren**  
    Mit dieser Option wird die CutOff-Funktion bereits im Schritt *„Warte auf Start-Zellspg.“* deaktiviert.  

        !!! note "Hinweis"
            Die erweiterten Optionen stehen nur in der **Sponsoren Version** zur Verfügung

    !!! note "Nach dem Balancing"
        Nach Abschluss des Balancierungsprozesses wird die Ladespannung auf das Floating-Niveau abgesenkt, um den Akku im geladenen Zustand zu halten, ohne ihn weiter zu belasten.

    !!! note "Hinweise"
        * Nach einem Neustart des BSC ist keine Wartezeit bis zum ersten Balancing. Erst nach dem ersten Balancing startet der eingestellte Balance-Interval.
        * Wurde das BSC beispielsweise um 22:00 Uhr gestartet und ein Intervall von fünf Tagen eingestellt, erfolgt das nächste Balancing nicht am Morgen des fünften Tages, sondern erst am Abend des fünften Tages. Da zu diesem Zeitpunkt keine Sonnenenergie zur Verfügung steht, wird das Balancing erst am nächsten Tag gestartet, an dem die Sonne scheint.
        * Für verschiedene BMS, z.B. dem Seplos, kann die einstellbare Mindestzeit genutzt werden, um den SoC 100 zu setzen   

    Den genauen Ablauf des Balance-Vorgangs kann mit dem MQTT-Topic "/Inverter/autoBalState" visualisiert werden.  
    Funktion der fünf verfügbaren States:

    - 0: Autobalancing ist deaktiviert
    - 1: BSC wartet auf den nächsten Startzeitpunkt
    - 2: Balancing wurde nicht fertig und es wird am nächsten Tag wiederholt
    - 3: Startzeitpunkt erreicht; BSC wartet auf die Start-Zellspannung
    - 4: Start-Zellspannung erreicht; Autoblancing ist jetzt aktiv
    - 5: Celldif. fertig wurde erreicht, aber die Balance-Ladespannung ist noch nicht erreicht
    - 6: Balance-Ladespannung erreicht; warten bis Mindestzeit abgelaufen


    ??? info "Zustandsdiagramm"
        ``` mermaid
        stateDiagram-v2
            classDef movement font-style:italic;
            classDef colorOrange fill:#FFDE59
            classDef colorRed fill:#FF5757

            %% Texte
            s0: <b>Step 0</b> (Autobalancer Off)
            s1: <b>Step 1</b> (Warte auf Starttag)
            s2: <b>Step 2</b> (Warte auf nächsten Tag)
            s3: <b>Step 3</b> (Warte auf Zellspannung)
            s4: <b>Step 4</b> (Autobalancer läuft)
            s5: <b>Step 5</b> (Warte auf erreichen der Ladespannung)
            s6: <b>Step 6</b> (Balance abschließen)
            n_setAbs: Abs. setzen
            n_setFloat: Float setzen
            n_setChargeVolt: Ladespannung setzen
            n_timeout: Timeout
            n_startBalMinTime: Balance-Mindest-Zeit starten
            
            s0 --> s1 : Wenn Balancer Enabled
            s0 --> s2 : Wenn Balancer Enabled und der Balance Vorgang nicht abgeschlossen werden konnte
            s1 --> s3 : Wenn Zeitpunkt erreicht
            s2 --> s3 : Wenn Zeitpunkt erreicht
            s3 --> s4 : Wenn Startzellspannung erreicht
            s4 --> n_setAbs
            s3 --> n_setAbs : Wenn Option aktiv
            s3 --> n_setChargeVolt : Wenn Option aktiv
            s4 --> n_timeout
            s4 --> s3 : Option) Wenn Zellspannung wieder unter Startzellspannung
            s4 --> n_startBalMinTime : Wenn Ladespannung (minus Toleranz) erreicht
            s4 --> s5 : Wenn MaxCellDiff unterschritten
            s5 --> s3 : Option) Wenn Zellspannung wieder unter Startzellspannung
            s5 --> n_startBalMinTime : Wenn Ladespannung (minus Toleranz) erreicht
            s5 --> n_setChargeVolt
            s5 --> s6 : Wenn Balance-Mindest-Zeit gestartet
            s5 --> n_timeout
            s6 --> n_setChargeVolt
            s6 --> s3 : Option) Wenn Zellspannung wieder unter Startzellspannung
            s6 --> n_setFloat : Wenn Mindestzeit abgelaufen
            s6 --> s0 : Wenn Mindestzeit abgelaufen

            class n_setAbs colorOrange
            class n_setFloat colorOrange
            class n_setChargeVolt colorOrange
            class n_startBalMinTime colorOrange
            class n_timeout colorRed
        ```

### Zusammenwirken mit anderen Laderegelungen

Während des Balancevorgangs setzt der BSC gezielt seine eigenen Laderegelungs-Funktionen aus oder stellt sie um – genau die Regelungen, die den Ladestrom im oberen Spannungsbereich sonst reduzieren oder abschalten und damit verhindern würden, dass die Zellen den Balance-Bereich überhaupt erreichen:

- Die [SoC-abhängige Ladestrom-Reduzierung](#ladestrom-reduzieren-soc) wird deaktiviert, sobald der Autobalancer auf die Start-Zellspannung wartet. Sie würde den Ladestrom bei hohem SoC drosseln, sodass die Zellen die Balance-Zellspannung unter Umständen nie erreichen.
- Der [Charge-Current Cut-Off](#charge-current-cut-off) wird ausgesetzt und sein Timer zurückgesetzt – mit der entsprechenden Option bereits im Step *„Warte auf Start-Zellspannung“*, sonst ab dem Step *„Warte auf Zellspannung/Differenz“*. Er würde das Laden nach Erreichen der Ladeschlussspannung vorzeitig beenden.
- Die [zellspannungsabhängige Ladestrom-Drosselung](#ladestrom-zell-spannungsabhangig-drosseln) läuft weiter, verwendet als End-Zellspannung aber die *Maximale Zellspannung* aus dem Autobalance-Abschnitt (in älteren Versionen die *Balance-Zellspannung*). Der Ladestrom bleibt dadurch hoch, bis die Zellen den Balance-Bereich erreicht haben.
- Die Zero-Charge-Current-Regelungen – spannungsgeführt in der [Spannungsregelung zur Ladestrombegrenzung](#spannungsregelung-zur-ladestrombegrenzung) sowie stromgeführt – werden übersprungen. Sie würden den Ladestrom auf 0 A zwingen.
- Die Ladespannung wird auf die *Balance-Ladespannung* angehoben und gehalten, bis die Pack-Spannung 99 % dieses Wertes erreicht hat.


## Charge-Current Cut-Off
Diese Funktion unterbricht den Ladestrom, wenn er für eine bestimmte Zeitspanne unterhalb einem eingestellten Strom-Wert liegt.  
Nach diesem Abbruch wird die bisher verwendete Soll-Lade-Spannung von der [Absorption-Spannung](settings_inverter.md#basisdaten) auf die [Float-Spannung](settings_inverter.md#basisdaten) gesetzt.  

```bsc-settings
version: v010
file: inverterCharge.json
profile: off
section: UI_SECT_INVERTERCHARGE_CHARGE_CURRENT_CUT_OFF
```

**Ein/Aus:**  
Aktivieren oder Deaktivieren der Funktion.

**Cut-Off Time:**  
Zeitspanne, in der der Ladestrom unter einem bestimmten Wert liegen muss, bevor er auf 0 A gesetzt wird.

**Cut-Off Strom:**  
Der Cut-Off-Strom ist der Gesamt-Ladestrom, unterhalb dessen die Cut-Off-Zeit beginnt. Der Gesamt-Ladestrom wird als Mittelwert berechnet, seit die eingestellte *Start-Zellspannung* (falls vorhanden) überschritten wurde.  
Überschreitet während des Prozesses der Mittelwert des Gesamt-Ladestroms erneut den Cut-Off-Strom, setzt sich sowohl der Timer als auch der Mittelwert zurück.

**Start-Zellspannung:**  
Die Start-Zellspannung ist die Spannung, ab der die Cut-Off-Regelung aktiv wird. Sobald diese überschritten wurde und der Cut-Off-Strom unterschritten ist, bleibt der Timer aktiv.  
Ein erneutes Unterschreiten der Start-Zellspannung führt nicht zum Abbruch des Timers. Der Timer wird ausschließlich zurückgesetzt, wenn der Cut-Off-Strom erneut überschritten wird.

!!! note "Hinweis"
    Der Wechsel zurück in die Absorption-Phase erfolgt durch den definierten [Float Ladespannung SoC-Wert](settings_inverter.md#basisdaten).  
    Bitte beachten Sie, dass ein zu hoch gewählter SoC-Wert unter Umständen das System sofort wieder in die Absorption-Phase zurückführen kann.  
    Auch ungenaue SoC-Werte der angeschlossenen BMS können diesen Phasenwechsel verfälschen. Für eine präzise SoC-Erfassung empfiehlt sich ein externer Shunt (siehe [hier](devices/externer_shunt.md)).

## SoC beim Unterschreiten der Zellspannung
Die Funktion ermöglicht, beim Unterschreiten einer definierten Zellspannung einen festgelegten Ladezustand (SoC) an den Wechselrichter zu übermitteln.

Die Funktion kann beispielsweise genutzt werden, um das Nachladen der Batterie automatisch zu veranlassen. Der Ladevorgang wird solange durchgeführt, bis die eingestellte Zellspannung für das Ladeende erreicht oder überschritten wird und wieder der normale SoC an den Wechselrichter übermittelt wird.

```bsc-settings
version: v010
file: inverterCharge.json
profile: off
section: UI_SECT_INVERTERCHARGE_SOC_BEIM_UNTERSCHREITEN_DER_ZELLSPANNUNG
```

**Einstellungen**
**Ein/Aus**:  
Aktiviert oder deaktiviert die Funktion.  

**Zellspannung Ladebeginn (mV)**:  
Zellspannung, bei deren Unterschreiten das Nachladen gestartet wird.  

**Zellspannung Ladeende (mV)**:  
Zellspannung, bei deren Erreichen das Nachladen beendet wird. Wird dieser Wert auf 0 gesetzt, erfolgt das Laden so lange, bis die Zellspannung wieder über die Ladebeginn-Spannung steigt.  

**SoC (%)**:  
Ladezustand, der beim Unterschreiten der Ladebeginn-Spannung an den Wechselrichter gesendet wird.  

**Sperrzeit zwischen zwei Nachladungen (s)**:  
Zeitspanne, die mindestens zwischen zwei Nachladevorgängen vergehen muss.
