# Maintenance {#wartung}

**Maintenance mode** temporarily removes selected devices from operation, for example before working on and disconnecting a battery pack. The marked device is no longer polled and raises no alarms. Other devices, inverter communication, MQTT and the display continue operating.

## Settings {#einstellungen}

Each category has two settings:

- **Maintenance active:** Stops polling marked devices and excludes them from monitoring, alarms, charge control and inverter control.
- **Send MQTT:** For devices in maintenance, enables **continued polling** and MQTT publication.

Settings are separate for **Data Devices** and **Group Devices**.

```bsc-settings
version: v010
file: maintenance.json
profile: off
section: UI_SECT_MAINTENANCE_WARTUNGSMODUS
```

!!! note "Group Devices"
    Group-device selection is relevant only when [group devices](settings_bsc_group-devices.md#group-devices-batterie-gruppen) are enabled.

## What Happens During Maintenance? {#was-passiert-bei-wartung-aktiv}

- **No polling:** No more read requests are sent. Last values stop updating and become invalid after a few seconds. Switching off or disconnecting the device will not produce communication or cell voltage alarms; this does not remove electrical hazards or replace safe isolation procedures.
- **No alarms:** Excluded from cell voltage, temperature, plausibility and cell voltage drop rules.
- **No control:** Excluded as a source for charging, discharging and inverter control.
- **Other functions continue:** Other devices, CAN communication, OneWire sensors, the display and MQTT for other devices work normally.
- **Visibility:** Maintenance status appears in the web app and as an MQTT `maintenance` flag.

!!! note "Data-Device Maintenance with Groups Enabled"
    Groups using a maintained data device are also treated as in maintenance and excluded from control. The device is polled only if required by a non-maintained group or **Send MQTT**.

## Send MQTT During Maintenance {#mqtt-senden-im-wartungsmodus}

Normally, no MQTT data is sent for maintained devices. Enabling **Send MQTT** keeps polling them and sends all normal values. The `maintenance` flag stays set so receivers such as Home Assistant recognise their status.

!!! note "Only Relevant in Maintenance"
    Devices not marked for maintenance are already polled and published normally.