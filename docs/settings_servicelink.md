# Fernwartung (T-Connect)

!!! note "Hinweis"
    Die Fernwartung (ServiceLink) ist ein Feature, das **ausschließlich auf T-Connect-Hardware** zur Verfügung steht.

Die Fernwartung baut vom Controller aus eine ausgehende, verschlüsselte Verbindung zu einem Vermittlungsserver auf. Dadurch kann eine unterstützende Person (Support/Servicetechniker) ohne Port-Freigabe im Router auf das Gerät zugreifen. Im Router muss **kein Port geöffnet** werden.

## Fernwartung

- **Fernwartung aktivieren** – Schaltet den Fernwartungszugang ein oder aus. Ist die Option deaktiviert, besteht kein Zugang; laufende Sitzungen werden sofort beendet.
- **Server** – Domain des Vermittlungsservers (ohne `https://` und ohne Schrägstrich am Ende).
- **Fernwartungs-ID** und **Fernwartungspasswort** – Werden automatisch erzeugt und müssen zusammen an die unterstützende Person weitergegeben werden. Das Fernwartungspasswort ist **nicht** das Passwort der WebApp. Über die Buttons **Anlernen starten**, **Neue Fernwartungs-ID** und **Neues Passwort** können die Zugangsdaten neu erzeugt bzw. ein Kopplungsfenster gestartet werden.

```bsc-settings
version: v010
file: serviceLink.json
profile: off
label: Fernwartung
```

!!! note "Kopplung"
    Die Kopplung mit dem Portal ist nur innerhalb eines **5-Minuten-Fensters** möglich, das über den Button **Anlernen starten** geöffnet wird.

## Log-Upload

Die Logs können alle 15 Minuten verschlüsselt auf den Vermittlungsserver hochgeladen werden. Der Server kann die Logs nicht lesen – die Entschlüsselung erfolgt ausschließlich im Browser der unterstützenden Person mit dem hier angezeigten **Log-Schlüssel**.

```bsc-settings
version: v010
file: serviceLink.json
profile: off
label: Log-Upload
```

## Statusbewertung

Legt fest, welche Trigger und Systemzustände in der Fernwartung als **Warnung**, **Fehler** oder **Alarm** angezeigt werden:

- **Trigger für Warn / Error / Alarm** – Auswahl der Trigger (1–27), die den jeweiligen Status auslösen.
- **Warn / Error / Alarm wirkt bei** – Auswahl der Systemquellen (z. B. Fehlerstatus, Trigger-Zustand), die zusätzlich berücksichtigt werden.

```bsc-settings
version: v010
file: serviceLink.json
profile: off
label: Statusbewertung
```

## Verbindungsstatus

Zeigt den aktuellen Status der Fernwartungs-Verbindung (verbunden/getrennt, Anlern-Status). Die Anzeige aktualisiert sich automatisch alle 3 Sekunden.
