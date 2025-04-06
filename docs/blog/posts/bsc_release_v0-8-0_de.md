---
date: 2025-04-06
authors: [shiningman]
categories:
  - Release Notes (Insider)
---

[img_dashboard]: release_v0-8-0_de/dashboard.png
[img_LadestrombegrenzungGrafana]: release_v0-8-0_de/LadestrombegrenzungGrafana.png
[img_LadestrombegrenzungVrm]: release_v0-8-0_de/LadestrombegrenzungVrm.png

# Version 0.8.0 (DE)
Diese Version bringt einige Verbesserungen und Erweiterungen mit sich, insbesondere das neue **Dashboard**. Nachfolgend eine Übersicht aller Änderungen seit der letzten stabilen Version:

## 🌐 Dashboard
Eine der größten Änderungen ist das neue Dashboard. Es zeigt auf einen Blick alle systemrelevanten Informationen und Livedaten an.

<!-- more -->

![img_dashboard]

## ✨ Neue Funktionen

- **Plausibilitätsprüfung für Texteingabefelder in der WebUI**  
  Diese Funktion erhöht die Eingabesicherheit und reduziert Konfigurationsfehler.

- **Sofortiger Start des Autobalancers per Trigger**  
  Der Autobalancer kann jetzt auch direkt über einen Trigger gestartet werden, was den Ablauf flexibler gestaltet.

- **Zusätzliche Optionen für den Autobalancer**  
  Der Autobalancer bietet nun zusätzliche Optionen, um ihn besser an spezifische Anforderungen anzupassen.
    - **Ballance-Spg. senden, sobald Startzeitpunkt erreicht**  
    Mit dieser Option wird die Balance-Spannung gesendet, sobald der festgelegte Startzeitpunkt erreicht ist.
    - **Bei Start-Zellspg.-Unterschreitung → Step 'Warte auf Start-Zellspg.'** 
    Mit dieser Option wird bei Unterschreiten der definierten Start-Zellspannung erneut in den Schritt „Warte auf Start-Zellspg.“ gewechselt. Dadurch werden auch die laufenden Timer zurückgesetzt.
    - **CutOff ab Step 'Warte auf Start-Zellspg.' deaktivieren**  
    Mit dieser Option wird die CutOff-Funktion bereits im Schritt „Warte auf Start-Zellspg.“ deaktiviert.


- **Dynamische Spannungsregelung zur Begrenzung des Ladestroms**  
  Mit dieser Funktion wird die Ladespannung dynamisch angepasst, um den Ladestrom innerhalb des konfigurierten Korridors zu halten. Sollte der Ladestrom den definierten Bereich überschreiten oder unterschreiten, wird die Spannung automatisch korrigiert.  <br><br>
  Diese Funktion ermöglicht es, den Akku nur bis zu einem bestimmten SoC (State of Charge) zu laden, um seine Lebensdauer zu verlängern.  <br><br>
  Die Diagramme zeigen eine Victron-Anlage mit aktivierter Spannungsregelung. Deutlich erkennbar ist, dass der Ladestrom begrenzt wird und keine Energie in den Akku fließt. Stattdessen wird die überschüssige Energie ins Netz eingespeist, während der SoC über die Zeit nahezu konstant bleibt.<br>
  ![img_LadestrombegrenzungGrafana]
  ![img_LadestrombegrenzungVrm]  <br>

- **Unterstützung des PACE PC200 über RS232**  
  Das Gerät kann nun auch über die serielle Schnittstelle (RS232) ausgelesen werden.

## 🔌 REST API-Erweiterungen

- **Neues REST-Endpoint: `/restapi/io`**  
  Ab sofort können digitale Eingänge und Relaisstatus über dieses neue REST-Endpoint abgefragt werden.

- **Setzen von `vTrigger` über die REST API**  
  Dies erweitert die Steuerungsmöglichkeiten über externe Systeme und ermöglicht eine flexiblere Integration.

## 🛠️ Anpassungen & Bugfixes

- **Anpassung des Temperaturbereichs für Alarmregeln**  
  Der Temperaturbereich für die Alarmregeln wurde optimiert.

- **Behebung von Datentypfehlern bei „Ladestrom reduzieren – SoC“**  
  Ein Problem mit den Datentypen im Zusammenhang mit der SoC-Laderegelung wurde behoben.

- **Fehlerbehebung beim Auslesen der PIC-Daten bei SeplosV3**  
  Ein Problem beim Auslesen der PIC-Daten wurde für die SeplosV3-Plattform behoben.
