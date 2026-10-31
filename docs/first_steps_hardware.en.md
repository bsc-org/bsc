This chapter introduces the hardware connections, including the BMS and inverter, required to operate the BSC.

## 1. Connecting the BMS to the BSC {#1-verbindung-des-bms-mit-dem-bsc}

The BSC must be switched off before connecting the BMS. This example uses a **LILYGO T-CONNECT** with three RS485 interfaces. Each interface can be assigned one BMS type. If the BMS supports *daisy chaining*, several BMS units of the same type can share one RS485 port.

Further information:

- [Supported BMS Units](devices/bms.md#serial-bms)
- [BMS Connection Examples](devices/bms.md#anbindungs-beispiele)
- [RS485 Port Assignment on the LILYGO T-CONNECT](hardware.md#lilygo-t-connect)
- [RS485 Connector Pinout on the LILYGO T-CONNECT](hardware.md#steckerbelegung)

To request support for another BMS, open an issue in the repository: [BSC Firmware Issues](https://github.com/shining-man/bsc_fw/issues).

## 2. Connecting the Inverter to the BSC {#2-verbindung-des-wechselrichters-mit-dem-bsc}

The inverter connects to the BSC via the **CAN interface**. The BSC must be switched off before making this connection.

Further information:

- [CAN Bus Connector on the LILYGO T-CONNECT](hardware.md#lilygo-t-connect)
- [CAN Connector Pinout on the LILYGO T-CONNECT](hardware.md#steckerbelegung)
- [Inverter Connection Notes](devices/wechselrichter.md)