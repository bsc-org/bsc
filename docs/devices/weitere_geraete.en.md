# Other Devices {#weitere-gerate}

In addition to [BMS units](bms.md), [inverters](wechselrichter.md) and [external shunts](externer_shunt.md), the BSC supports other device classes documented here.

## Eletechsup NTC Temperature Boards (NT48x Series) {#eletechsup-ntc-temperatur-boards-nt48x-serie}

NT48x boards are **not BMS units**: they measure up to 32 NTC temperature sensors and send values to the BSC via RS485 (Modbus RTU).

| Type | Channels | Single pack<br>Board / BSC | Multi-pack<br>Board / BSC |
| --- | --- | --- | --- |
| NT48A08 | 8 | 1 / 1 | 1 / 1 |
| NT48B16 | 16 | 1 / 1 | 1 / 1 |
| NT48C32 | 32 | 1 / 1 | 1 / 1 |

### Connection {#anbindung}

- **Connection:** RS485 directly to a BSC serial interface. Select the device type under [Settings / Interfaces / Serial](../settings_bsc_interfaces.md#serial); the BSC automatically sets **9600 baud**.
- **Protocol:** Modbus RTU, function code **03**, holding registers.
- **Address:** Set the Modbus slave address with the board's DIP switches and enter it in [data-device mapping](../settings_bsc_data_devices.md#data-devices). It is used as the Modbus slave ID. The table uses **board / BSC** notation.

### Temperature Data in the BSC {#temperaturdaten-im-bsc}

Each channel supplies a 16-bit temperature value with **0.1 °C resolution**. The BSC stores it in the data device's extended temperature values.

### Using the Temperatures {#verwendung-der-temperaturwerte}

Extended temperatures are available for:

- [Group-device extended temperatures](../settings_bsc_group-devices.md#zuordnung-der-erweiterten-temperaturen).
- Temperature-dependent charge and discharge current control.
- REST, MQTT and Home Assistant.

See [Group Devices](../settings_bsc_group-devices.md#zuordnung-der-erweiterten-temperaturen) for bitmasks and slot ordering.