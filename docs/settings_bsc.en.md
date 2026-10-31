## System {#system}

System settings include usernames and passwords for Wi-Fi and MQTT access.

```bsc-settings
version: v010
file: system.json
profile: off
index: 1
```

- **Device Name:** Custom name (default `BSC`), also shown on the dashboard.
- **Display Timeout:** Time before the connected display turns off automatically.
- **Profile switching:** P1/P2 store two sets of profile-capable parameters, e.g. summer/winter. **Off** uses P1; **P1** or **P2** permanently selects that profile; **Trigger** uses P1 when the selected profile trigger is inactive and P2 when active. The **Profile trigger** field appears only in Trigger mode. Profile-capable settings have P1/P2 fields.
- **Traceback trigger:** Activates selected triggers if a traceback (crash report) exists. Displayed **only on T-CONNECT hardware**.

### Users {#benutzer}

```bsc-settings
version: v010
file: system.json
profile: off
section: UI_SECT_SYSTEM_BENUTZER
```

- **Enable password protection:** Enables or disables web login. When disabled, the web interface **and [REST API](restapi.md)** are accessible without authentication.
- **Automatic logout:** Inactivity timeout, **0–240 minutes**. **0** disables automatic logout.
- **Users:** Up to **2** accounts, each with a username, password and role: **Admin** (full access) or **ReadOnly** (read-only settings access). Passwords are stored as hashes, not plaintext.

## Network Settings {#netzwerkeinstellungen}

```bsc-settings
version: v010
file: system.json
profile: off
section: UI_SECT_SYSTEM_WLAN
```

- **Wi-Fi SSID:** Network name to connect to.
- **Wi-Fi password:** Password for that network.
- **Wi-Fi Connect Timeout:** Maximum connection attempt time in seconds. If no connection is established, the BSC starts its own access point. **0** disables the timeout and retries indefinitely. After losing Wi-Fi and starting an AP, the BSC retries the original network every **5 minutes**.
- **Ethernet:** Available only on T-CONNECT hardware with Ethernet. Enabling it disables Wi-Fi and uses LAN.

```bsc-settings
version: v010
file: system.json
profile: off
section: UI_SECT_SYSTEM_STATIC_IP
```

- **IP address:** Static IPv4 address. Leave empty to use DHCP.
- **Gateway:** Default gateway IPv4 address.
- **Subnet:** Local subnet mask, e.g. `255.255.255.0`.
- **DNS (optional):** DNS server IPv4 address. If empty, the DHCP-provided server is used.

## MQTT Settings {#mqtt}

```bsc-settings
version: v010
file: mqtt.json
profile: off
label: MQTT Allgemein
```

- **MQTT Enable:** Enables MQTT. With broker IP and port configured, the BSC sends data cyclically.
- **MQTT Device Name:** Unique name identifying the BSC to the broker.
- **MQTT Server IP:** Broker IPv4 address.
- **MQTT Server Port:** Broker port (default **1883**, unencrypted).
- **Username / Password:** Broker credentials if required.
- **MQTT Topic Name:** Base publishing topic; individual-value subtopics are created automatically.
- **MQTT send interval:** **1–120 s**, default **60 s**. Data Devices, Group Devices, OneWire and Inverter categories are sent successively, one category per cycle. Inverter values are additionally published only every **15th inverter cycle**.
- **Persistent vTriggers:** Select virtual triggers whose states should be restored automatically after reboot or power loss. See [Virtual Triggers](mqtt.md#virtual-trigger).

See [MQTT](mqtt.md) for MQTT filtering and Home Assistant auto-discovery.

## Time Server (NTP) {#zeitserver-ntp}

```bsc-settings
version: v010
file: system.json
profile: off
section: UI_SECT_SYSTEM_NTP
```

!!! note "Restart Required"
    Restart the BSC to apply NTP settings.

- **Server Name/IP:** NTP server hostname or IPv4 address.
- **Time offset:** Local timezone offset from UTC in hours (**−12 to +14**, default **+1** for Central Europe). The BSC synchronises over NTP and applies this offset.

If an external NTP server is unreliable, the local router can be a more stable alternative. On an AVM FritzBox, enable its time server under **Home Network / Network / Network Settings**. Example upstream servers: `ntp1.t-online.de; 2.europe.pool.ntp.org`. In the BSC, enter the router's **IP address** as NTP server; using a hostname instead can cause connection problems.