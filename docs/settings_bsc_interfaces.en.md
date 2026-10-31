# BSC Interfaces {#schnittstellen-des-bsc}

Interface settings specify **what is connected where**. They do **not** decide how BMS/balancer data is used or when relays switch; configure those actions in alarm rules or inverter settings.

## Relay Outputs {#relaisausgange}

```bsc-settings
version: v010
file: digitalOut.json
profile: off
index: 1
```

- **Trigger on:** Select the trigger (**1–27**) that switches the relay.
- **Trigger behaviour:** **Permanent** stays energised while the trigger is active; **Pulse** switches for the configured pulse duration.
- **Pulse duration:** **100–10000 ms**, default **500 ms**, used in Pulse mode.
- **Delay:** **0–254 s** between trigger activation and relay switching.
- **Invert:** Reverses the output switching logic to suit normally open/normally closed control requirements. It changes which relay state is used during an event.

## Digital Inputs {#digitaleingange}

```bsc-settings
version: v010
file: digitalIn.json
profile: off
index: 1
```

- **Invert input:** Reverses input logic.
- **Forward to:** Select trigger **1–27**. A high input activates it; with inversion enabled, a low input activates it.

## Serial {#serial}

Select the hardware connected to each serial port. Also assign the serial port to an internal data device under [Data Devices](settings_bsc_data_devices.md#data-devices). Both steps are needed for correct detection and mapping.

```bsc-settings
version: v010
file: serial.json
profile: off
index: 1
```

Original BSC software-to-hardware mapping: **Serial 0 → U1**, **Serial 1 → U2**, **Serial 2 → U3**. Serial **3–10** require the Serial Extension.

See [Supported BMS Units](devices/bms.md#unterstutzte-bms) for supported hardware and addressing details. Support is expanded continuously.

### Cell Count {#anzahl-zellen}

```bsc-settings
version: v010
file: serial.json
profile: off
section: UI_SECT_SERIAL_ALLGEMEIN
```

Number of individual cells in the battery. Needed, for example, for correct dashboard display.

### Filter {#filter}

```bsc-settings
version: v010
file: serial.json
profile: off
section: UI_SECT_SERIAL_FILTER
```

The filter detects and suppresses sudden cell voltage jumps, preventing transient erroneous data packets from being used. Its threshold is a percentage relative to the previous valid value. Values beyond that deviation are discarded; the configured reception-error count determines when the state is treated as an error.

- **RX error count:** Number of consecutive faulty packets tolerated before the state is considered an error. Once exceeded, the timestamp of the last valid packet is no longer updated.
- **Cell voltage deviation:** Maximum permitted percentage deviation. **0** disables filtering.

## OneWire (Sensor Addresses) {#onewire-onewire-adressen}

Enable OneWire and set addresses for up to **64 DS18B20** temperature sensors.

```bsc-settings
version: v010
file: onewireAdr.json
profile: off
index: 1
```

Opening the firmware's OneWire configuration page starts periodic bus scans. Detected devices appear at the bottom. **Bold** addresses identify newly found sensors not yet saved. In the firmware, **Copy** copies an address to the clipboard.

| Example sensor address | Status |
| --- | --- |
| `28:93:e3:95:f0:1:3c:56` | Previously configured |
| **`28:93:e3:95:f0:1:3c:57`** | New sensor |
| `28:93:e3:95:f0:1:3c:58` | Previously configured |

## OneWire II (Temperature Offset) {#onewire-ii-temperatur-offset}

Set a correction offset for each of the **64** OneWire temperature sensors.

```bsc-settings
version: v010
file: onewire2.json
profile: off
index: 1
```

## Bluetooth {#bluetooth}

!!! warning "Not Supported in Current Firmware"
    Bluetooth is not supported by the current firmware.

```bsc-settings
version: v010
file: bluetooth.json
profile: off
index: 1
```

~~Earlier firmware allowed up to five Bluetooth devices, configured by type and lowercase MAC address. Opening that page scanned periodically and displayed the last five detected devices. See the historical [Bluetooth device list](devices/bms.md#bluetooth-devices).~~