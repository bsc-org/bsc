# Alarmregeln 
In den Alarmregeln kann eingestellt werden, welche Daten von welchen Devices überwacht werden sollen.  

## BMS
Die BMS Alarmregeln ermöglichen die Überwachung der konfigurierten Data-Devices. Es können verschiedene Parameter des Data-Device überwacht werden, um Alarme zu konfigurieren und automatische Aktionen auszulösen, wenn bestimmte Schwellenwerte erreicht werden.

Es stehen **10 BMS-Alarmregeln** zur Verfügung. Pro Alarmregel:

**Zu überwachendes Data-Device**  
Hier wird festgelegt, für welches Data-Device die Alarmregel gilt.

**Keine Daten vom BMS**  
Überwacht, ob vom zugeordneten Data-Device über einen definierten Zeitraum keine Daten empfangen werden.

- **Aktion bei Trigger**  
  Auswahl des Triggers (Trigger 1–27), der bei Auslösen der Bedingung aktiviert werden soll.
- **Trigger keine Daten (s)**  
  Zeit in Sekunden, nach deren Ablauf ohne eingehende Daten der Trigger aktiviert wird.

**Spannungsüberwachung Zelle Min/Max**  
Überwacht die minimalen und maximalen Spannungswerte der einzelnen Zellen.

- **Aktion bei Trigger**  
  Auswahl des Triggers (Trigger 1–27), der bei Auslösen der Bedingung aktiviert werden soll.
- **Anzahl Zellen Monitoring**  
  Anzahl der zu überwachenden Zellen.
- **Zellspannung Min (mV)**  
  Unterer Grenzwert der Zellspannung (Standard 2500 mV).  
  Wird dieser unterschritten, löst die Alarmregel aus.
- **Zellspannung Max (mV)**  
  Oberer Grenzwert der Zellspannung (Standard 3650 mV).  
  Wird dieser überschritten, löst die Alarmregel aus.
- **Hysterese Min/Max (mV)**  
  Definiert den Spannungsbereich, um den sich die Spannung bei aktivem Trigger mindestens verändern muss, damit der erkannte Fehler wieder zurückgesetzt wird.
  Beispiel: Wird der Trigger bei einer Zellspannung Max. von 3,65 V ausgelöst und die Hysterese ist auf 50 mV eingestellt, muss die Spannung unter 3,60 V fallen, damit der Trigger wieder deaktiviert wird.

**Spannungsüberwachung Gesamt Min/Max**  
Überwacht die minimalen und maximalen Spannungswerte des gesamten Systems.

- **Aktion bei Trigger**  
  Auswahl des Triggers (Trigger 1–27), der bei Auslösen der Bedingung aktiviert werden soll.
- **Spannung Min (V)**  
  Unterer Grenzwert der Gesamtspannung (Standard 48,00 V).
- **Spannung Max (V)**  
  Oberer Grenzwert der Gesamtspannung (Standard 54,00 V).
- **Hysterese Min/Max (V)**  
  Definiert den Spannungsbereich, um den sich die Spannung bei aktivem Trigger mindestens verändern muss, damit der erkannte Fehler wieder zurückgesetzt wird.  

```bsc-settings
version: v010
file: alarmBms.json
profile: off
index: 1
```


## Plausibility check
### Plausibility check

!!! note "Hinweis zur Supporter-Firmware"
    Der Plausibility Check ist auch Bestandteil der separat erhältlichen **Supporter-Firmware** (Classic WebUI). Weitere Informationen: [Supporter](supporter.md).

Der "Plausibility Check" ist eine wichtige Funktion, die kontinuierlich den Stromfluss sowie die Zellspannungen der an das System angeschlossenen Data-Devices überwacht.  

Wenn sich die Werte für Strom und Zellspannungen über einen längeren Zeitraum hinweg nicht mehr regelmäßig ändern, deutet dies darauf hin, dass das BMS keine gültigen Daten mehr sendet. In diesem Fall kann davon ausgegangen werden, dass ein Problem im BMS vorliegt.

Der "Plausibility Check" bietet so eine frühzeitige Warnung bei Unregelmäßigkeiten und unterstützt die zuverlässige Funktion und Sicherheit des gesamten Systems.  

**Funktionsweise des Plausibility checks**:

```mermaid
flowchart TD
	n1["Plausibility check"] --> n7["Ist Strom &lt; 'Strom Schwellwert'"]
	n7 --> n8["Zellspannungen ändern sich 'Zeit 2' nicht"]
	n8 --> n4["Trigger wird aktiv"]
	n1 --> n6["Ist Strom >= 'Strom Schwellwert'"]
	n6 --> n10["Zellspannungen ändern sich 'Zeit 1' nicht"]
	n10 --> n4
```

**Parameter:**

```bsc-settings
version: v010
file: plausibilityCheck.json
profile: off
section: UI_SECT_PLAUSIBILITYCHECK_PLAUSIBILITY_CHECK
```

**Cellvoltage plausibility check**  
Hier kann eingestellt werden, **welcher Trigger aktiviert wird**, falls ein Fehler bei der Plausibilitätsprüfung der Zellspannungen erkannt wird.  
Der Trigger sorgt dafür, dass im Fehlerfall entsprechende Aktionen ausgelöst werden, z. B. Alarmmeldungen oder Schutzmaßnahmen.

**Zu überwachende Geräte**  
Hier werden die Data Devices ausgewählt, deren Zellspannungen geprüft werden sollen.  

**Strom-Schwellwert (A)**  
Definiert den Grenzwert für den Batteriestrom, ab dem unterschiedliche Prüfzeiten (*Zeit 1* oder *Zeit 2*) angewendet werden (Standard: 200 A).  

**Zeit 1 (s)**  
Wird verwendet, wenn der Strom im Batterypack **größer** als der eingestellte *Strom-Schwellwert* ist (Standard: 30 s).  
Diese Zeit legt fest, wie lange ein auffälliger Zellspannungswert bestehen muss, bevor er als fehlerhaft gewertet wird.  

**Zeit 2 (s)**  
Wird verwendet, wenn der Strom im Batterypack **kleiner oder gleich** dem eingestellten *Strom-Schwellwert* ist (Standard: 240 s).  
In der Regel wird hier eine längere Zeit eingestellt, um Fehlalarme bei geringen Lasten zu vermeiden.


### Wertevergleich

!!! note "Hinweis zur Supporter-Firmware"
    Der Wertevergleich ist auch Bestandteil der separat erhältlichen **Supporter-Firmware** (Classic WebUI). Weitere Informationen: [Supporter](supporter.md).

Mit dieser Funktion können die Werte ausgewählter Data Devices überwacht und miteinander verglichen werden. Bei Überschreiten der definierten Abweichungen wird der zugewiesene Trigger aktiviert.  
Es stehen **10 Wertevergleichs-Regeln** zur Verfügung.

```bsc-settings
version: v010
file: plausibilityCheck.json
profile: off
section: UI_SECT_PLAUSIBILITYCHECK_WERTEVERGLEICH
```

**Trigger**  
Hier kann ausgewählt werden, welcher Trigger (Trigger 1–27) ausgelöst werden soll, wenn eine Abweichung erkannt wird.  

**Vergleichen**  
Wählen Sie die Data Devices aus, deren Werte miteinander verglichen werden sollen.  

**Werte**  
Legt fest, welche Werte verglichen werden:  

- **Gesamtspannung**  
- **Zellspannung**  
- **Batteriestrom**  
  Zusätzlich wird überwacht, dass bei einem offenen Lade-FET nur ein Ladestrom von maximal **100 mA** fließen darf.  
  Die 100 mA dienen als Toleranz aufgrund von Messungenauigkeiten.  
  Das Gleiche gilt auch für den Entlade-FET, jedoch in umgekehrter Stromrichtung.

**Maximale Abweichung**  

- **Gesamtspannung (mV)**  
  Die maximal zulässige Abweichung der Gesamtspannung zwischen den ausgewählten Geräten (Standard: 50 mV).  
- **Zellspannung (mV)**  
  Die maximal zulässige Abweichung der einzelnen Zellspannungen (Standard: 5 mV).  
- **Batteriestrom (A)**  
  Die maximal zulässige Abweichung des Batteriestroms (Standard: 5 A).  

**Verzögerung (s)**  
Definiert die Zeitspanne, die die Abweichung bestehen muss, bevor der Trigger ausgelöst wird (Standard: 5 s). Dies verhindert Fehlalarme durch kurzzeitige Schwankungen.  

---

**Einsatzbeispiele:**  

- Prüfen, ob sich der Batteriestrom gleichmäßig zwischen den ausgewählten **Data Devices** aufteilt.  
- Prüfen, ob die Zellspannungen zwischen zwei in einem Batteriepack verbauten Geräten, z. B. einem **BMS** und einem **Balancer** gleich sind.

**Hinweis:**  
Der Wertevergleich prüft nicht, ob die **Data Devices** tatsächlich online sind. Diese Überwachung kann an anderer Stelle erfolgen und entsprechend darauf reagiert werden.  


### Zellspannung bei Ladestrom

Diese Überwachung erkennt **Zellspannungs-Einbrüche während des Ladens**: Bricht die Zellspannung eines überwachten Data-Devices unter Ladebedingungen ein (die Batterie nimmt Ladestrom auf, die Spannung sinkt aber dennoch), deutet das auf eine defekte Zelle oder ein Problem im Batteriepack hin.

```bsc-settings
version: v010
file: plausibilityCheck.json
profile: off
section: 2
```

- **Ein/Aus** – Aktiviert oder deaktiviert die Überwachung.
- **Zu überwachende Geräte** – Data-Devices, deren Zellspannungen überwacht werden.
- **Trigger** – Trigger (Trigger 1–27), der bei einem erkannten Zellspannungs-Einbruch aktiviert wird.
- **Fehler bis manuellem Reset halten** – Ist diese Option aktiviert, bleibt der Fehlerzustand auch dann bestehen, wenn sich die Zellspannungen wieder erholt haben. Der Fehler muss dann manuell zurückgesetzt werden.



## Temperatur
### Alarm bei Sensorfehler
In diesem Abschnitt können Alarme für Sensorfehler an den Temperatursensoren konfiguriert werden.

```bsc-settings
version: v010
file: alarmTemp.json
profile: off
section: UI_SECT_ALARMTEMP_ALARM_BEI_SENSORFEHLER
```

**Trigger**  
Auswahl des Triggers (Trigger 1–27), der bei einem erkannten Sensorfehler aktiviert werden soll.  

**Timeout (s)**  
Zeit in Sekunden, nach deren Ablauf ohne gültige Sensordaten der Alarm ausgelöst wird (5–240 s, Standard 5 s).  
Dies dient dazu, kurzzeitige Aussetzer zu tolerieren und Fehlalarme zu vermeiden.


### Temperatur Überwachung
Die Temperatur-Überwachung dient dazu, definierte Sensoren kontinuierlich zu kontrollieren und bei Überschreiten oder Unterschreiten bestimmter Grenzwerte Alarme bzw. Trigger auszulösen. Dies kann sowohl für Data-Device-integrierte Sensoren als auch für erweiterte Sensoren (z. B. OneWire) erfolgen.  
Es stehen **10 Temperaturregeln** zur Verfügung.

```bsc-settings
version: v010
file: alarmTemp.json
profile: off
section: UI_SECT_ALARMTEMP_TEMPERATUR_220_BERWACHUNG
```

**Quelle**  
Legt fest, von welchem Sensortyp die Messwerte stammen:

- **Data Device** – Auswahl von 0–5 internen BMS-Sensoren.
- **Data Device – Erweiterte Sensoren** – Auswahl von 0–31 erweiterten Sensoren (z. B. OneWire).
- **Group Device** / **Group Device – Erweiterte Sensoren** – nur verfügbar, wenn [Group Devices](settings_bsc_devices.md#group-devices-batterie-gruppen) aktiviert sind.

**Zu überwachende Quellen**  
Hier kann festgelegt werden, von welchem **Data-Device** (bzw. Group Device) die Temperaturdaten stammen sollen.  

**Sensoren**  
Hier können die Sensoren gewählt werden, deren Werte für die Überwachung relevant sind.  
Welche Sensoren angeboten werden, hängt von der gewählten Quelle ab (BMS-Sensoren 0–5 bzw. erweiterte Sensoren 0–31).

**Überwachungstyp**  
Bestimmt die Logik, nach der die Temperaturwerte überwacht werden:

- **Maximalwert-Überschreitung:** Alarm bei Überschreiten von Wert 1.
- **Minimalwert-Unterschreitung:** Alarm bei Unterschreiten von Wert 1.
- **Maximalwert-Überschreitung (Referenz):**  
  Überwacht, dass keine der Temperaturen der Ausgewählten *Sensoren*  mehr als den zulässigen Temperaturoffset (*Wert 1)* von dem unter *Referenzsensor* definierten Sensor abweicht.  
  Der *Referenzsensor* ist die Sensornummer des Temperatursensors, gegen den Verglichen wird.  
  Wert 1 definiert den zulässigen Temperatur-Offset.
- **Differenzwert-Überwachung:**  
  Überwacht die maximale Differenz zwischen den unter *Sensoren* ausgewählten Temperatursensoren. Ist die Differenz zwischen dem niedrigsten und höchsten Wert zu groß, wird der Trigger ausgelöst.  
  *Wert 1* ist die maximal erlaubte Differenz.

**Referenzsensor**  
Gibt an, welcher Sensor als Referenzsensor verwendet wird (0–255).  
Nur relevant bei *Maximalwert-Überschreitung (Referenz)*.

**Wert 1**  
Numerischer Wert (−20 °C bis +100 °C) für den gewählten Überwachungstyp:

**Hysterese**  
Numerischer Wert (−20 °C bis +100 °C), der definiert, um wie viel der Messwert nach Unterschreiten des Schwellwerts fallen bzw. nach Überschreiten steigen muss, bevor die Überwachung wieder deaktiviert wird.  
Dies verhindert ständiges Ein- und Ausschalten bei Werten nahe am Grenzbereich.

**Auslösung**  
Bestimmt, welcher **Trigger** (Trigger 1–27) bei Eintreten der Überwachungsbedingung aktiviert wird.

---

**Beispiel**  

- Quelle: **Data Device – Erweiterte Sensoren**
- Sensor: **Nr. 12**
- Überwachung: **Maximalwert-Überschreitung**
- Wert 1: **60,00 °C**
- Hysterese: **2,00 °C**
- Auslösung: **Trigger 2**

**Ergebnis**  
Wenn der Sensor Nr. 12 eine Temperatur von 60,00 °C überschreitet, wird **Trigger 2** aktiviert. Erst wenn die Temperatur wieder unter 58,00 °C fällt (Wert 1 − Hysterese), wird der Trigger zurückgesetzt.
