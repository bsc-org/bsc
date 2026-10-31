# Group Devices

This page describes virtual battery groups beyond the general [interface settings](settings_bsc_interfaces.md).

## Group Devices (Battery Groups) {#group-devices-batterie-gruppen}

Combine data devices, such as BMS units or shunts, into a virtual **battery group**. Each group provides aggregated voltage, current and SoC and can replace individual data devices as a source in inverter settings, alarm rules or MQTT filters.

```bsc-settings
version: v010
file: groupDeviceMapping.json
profile: off
groups: 1
section: UI_SECT_GROUPDEVICEMAPPING_BATTERY_PACKS
```

!!! note "Enable Group Devices"
    Group devices appear only when **Group Devices active** is enabled. Many other source selectors then switch to **Battery Packs** (group devices), including inverter sources, temperature alarms and MQTT filters.

Up to **32** group devices are available, all with the same structure:

- **Name:** Up to **16 characters**, without `#` or `+`.
- **Master Device:** Primary data device, providing cell voltages and temperatures, for example.
- **Second Device:** Currently has no function.
- **Voltage / Current / SoC:** Select source devices and aggregation: average, maximum, minimum; current also supports sum.
- **Extended temperatures:** Source is unused, OneWire, or a data device with extended sensors. Select **Sensors 0–31** and, for OneWire only, **Sensors 32–63**.
- **Extended temperature names:** Names for **32** slots, up to **16 characters** each.

### Mapping Extended Temperatures {#zuordnung-der-erweiterten-temperaturen}

Each group has up to **32 temperature slots**, populated by the selected source and sensor masks.

**Source**

- **Unused:** Disabled; all slots empty.
- **OneWire:** Uses the [OneWire address list](settings_bsc_interfaces.md#onewire-onewire-adressen).
- **Data device:** Only the serial temperature acquisition devices **NT48A08** (8 channels), **NT48B16** (16) and **NT48C32** (32) provide these extended sensors.

**Sensor Selection (Bitmasks)**

Each checkbox is one bit of a 32-bit mask. Its number identifies the **physical sensor**, not the output slot:

- **Data device:** Number `n` is extended channel `n`, starting at **0**. Sensors 32–63 are neither shown nor used.
- **OneWire:** Number `n` is entry `n` in the address list, starting at **0**. The second mask selects sensors **32–63**.

**Slot Order**

Selected sensors fill slots in **ascending sensor-number order**, first selected sensors 0–31, then (OneWire only) selected sensors 32–63. Only the first **32** selected sensors are used. Names **Sensor 0–31** label the **slots**, not the physical sensors. Changing the selection changes which sensor each existing name describes.

Example: select **5, 10, 15, 16, 17, 18, 19, 20**:

| Slot | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8–31 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sensor | 5 | 10 | 15 | 16 | 17 | 18 | 19 | 20 | empty |

For a data-device source, slot 0 receives channel 5 and slot 1 channel 10. For OneWire, they receive OneWire sensors 5 and 10. Names Sensor 0–7 label those eight slots; slots 8–31 remain empty.

Use these temperatures wherever group devices can be selected, e.g. charge/discharge temperature reduction under **Extended sensor sources / Extended sensors 0–31**. They are also available through [REST](restapi.md) and [MQTT](mqtt.md).

!!! tip "Using Groups"
    Configured groups can be selected wherever **Group Device** or **Battery-Pack** is offered: inverter domain “Group devices”, temperature alarms, maintenance and MQTT filters.