## Funktionsprinzip der Trigger
In diesem Abschnitt wird erklärt, wie interne Trigger zur Überwachung und Steuerung verschiedener Werte (z. B. Temperatur, Spannung) verwendet werden können, um auf potenzielle Gefahrenzustände zu reagieren.  

**Trigger-Funktionalität**  
Für jeden zu überwachenden Wert kann ein Trigger konfiguriert werden, der bei Erreichen eines definierten Grenzwerts aktiv wird. Ein aktivierter Trigger löst selbst zunächst keine direkte Aktion aus. Es kann jedoch flexibel eingestellt werden, welche Aktionen durch den Trigger ausgelöst werden sollen. So kann beispielsweise:

  - ein Relais geschaltet werden (z. B. zum Aktivieren eines Lüfters),
  - der Wechselrichter angewiesen werden, seinen Ladestrom auf 0 A zu reduzieren.


Diese Logik ermöglicht es, Trigger (als Signalgeber) und verbundene Aktionen (als Signalnehmer) in flexibler Weise zu kombinieren. Es stehen bis zu 27 interne Trigger zur Verfügung.  

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

```bsc-settings
version: v010
file: trigger.json
profile: off
section: UI_SECT_TRIGGER_TRIGGERNAME
```

In diesem Menü können für die **27 verfügbaren Trigger** benutzerdefinierte Namen vergeben werden (max. 16 Zeichen).  
Diese Namen werden im gesamten System verwendet, z. B. bei der Auswahl von Triggern in anderen Einstellungen oder Funktionen.


## Trigger Scheduler

```bsc-settings
version: v010
file: trigger.json
profile: off
section: UI_SECT_TRIGGER_TRIGGER_SCHEDULER
```

Der Trigger Scheduler ermöglicht die zeitgesteuerte Ausführung von Triggern im BSC.  
Es stehen insgesamt **5 Scheduler** zur Verfügung, die unabhängig voneinander konfiguriert werden können.  

!!! note "Hinweis zur Supporter-Firmware"
    Der Trigger Scheduler ist ein Feature der **Supporter-Firmware**. Weitere Informationen: [Supporter](supporter.md).

Folgende Parameter stehen zur Verfügung:  

- **Trigger**  
  Auswahl des auszuführenden Triggers (Trigger 1–27).  

- **Monat**  
  Auswahl der Monate, in dem der Trigger aktiv sein soll.  

- **Wochentag**  
  Auswahl der Wochentage, an dem der Trigger ausgeführt werden soll.  

- **Von (Uhrzeit)**  
  Startzeitpunkt, ab dem der Trigger aktiv ist.  

- **Bis (Uhrzeit)**  
  Endzeitpunkt, bis zu dem der Trigger aktiv ist.  
