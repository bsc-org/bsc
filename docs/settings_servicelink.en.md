# Remote Support (T-CONNECT) {#fernwartung-t-connect}

!!! note "Hardware Availability"
    ServiceLink is available **only on T-CONNECT hardware**.

The controller establishes an outgoing encrypted connection to a relay server. A support technician can then access the device without router port forwarding. **No router port needs to be opened.**

## Remote Support {#fernwartung}

- **Enable remote support:** Enables/disables access. Disabling immediately terminates ongoing sessions.
- **Server:** Relay server domain, without `https://` or a trailing slash.
- **Remote support ID and password:** Generated automatically. Share both with the supporting person. This password is **not the web app password**. **Start pairing**, **New remote support ID** and **New password** create a pairing window or regenerate credentials.

```bsc-settings
version: v010
file: serviceLink.json
profile: off
label: Fernwartung
```

!!! note "Pairing Window"
    Portal pairing is possible only during the **5-minute** window opened by **Start pairing**.

## Log Upload {#log-upload}

Logs can be uploaded encrypted every **15 minutes**. The server cannot read them; decryption takes place in the support person's browser using the displayed **log key**.

```bsc-settings
version: v010
file: serviceLink.json
profile: off
label: Log-Upload
```

## Status Classification {#statusbewertung}

Select triggers (**1–27**) for **Warning / Error / Alarm** and additional system sources (e.g. error state or trigger state) that contribute to each classification.

```bsc-settings
version: v010
file: serviceLink.json
profile: off
label: Statusbewertung
```

## Connection Status {#verbindungsstatus}

Shows connected/disconnected and pairing status. Updates automatically every **3 seconds**.