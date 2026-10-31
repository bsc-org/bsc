# Getting Started and Commissioning {#erste-schritte-und-inbetriebnahme}

This sequence takes you from checking your devices to establishing the first data connection. The flashing guide distinguishes between hardware variants; choose the section for your board.

## Recommended Sequence {#empfohlener-ablauf}

1. **Check compatibility and hardware:** Check whether your [BMS](devices/bms.md) and [inverter](devices/wechselrichter.md) are supported. See [Obtaining Hardware](#beschaffung-der-hardware) for the currently recommended hardware.
2. **Install firmware and connect to the BSC:** Follow the [flashing and connection guide](first_steps_programming.md). Use the section for your hardware.
3. **Connect the BMS:** Follow the [connection guide](first_steps_hardware.md) to connect the BMS to the BSC.
4. **Configure the BSC and check measurements:** Reconnect to the web interface. Set up networking and basic settings, then configure the BMS interface and device mapping using [Operating Settings](first_steps_settings.md). Check the [Dashboard](dashboard.md) for incoming measurements.
5. **Optional: Set up the inverter and other functions:** Once BMS data is displayed correctly, connect and configure the inverter. Add MQTT, REST, alarm rules and sensors as needed.

Configuration depends on the connected devices. Do not copy example values without checking them; the [example configurations](beispiel_konfigurationen.md) are guidance, not universally applicable settings.

## Further Help {#weitere-hilfe}

- [System Overview](system_overview.md)
- [Hardware Details](hardware.md)
- [Testing Without Original Hardware](BSC_ohne_orig_hardware.md): for testing only, not recommended for production use
- [Troubleshooting](troubleshooting.md)

## Information Videos {#info-videos}

[www.youtube.com/@shining-man](http://www.youtube.com/@shining-man)

!!! note "Please Note"
    Due to ongoing BSC development, some video content is no longer up to date.

## Obtaining Hardware {#beschaffung-der-hardware}

Compatible hardware, including enclosures, extensions and accessories, is available from <a href="https://bsc-shop.com" target="_blank">www.BSC-Shop.com</a>.

The **LILYGO T-CONNECT board** is currently recommended for operating the BSC system. The original BSC mainboard was designed specifically for the project, but is no longer regularly available and is therefore no longer a recommended purchasing option.

### Recommended Hardware: LILYGO T-CONNECT {#empfohlene-hardware-lilygo-t-connect}

The **LILYGO T-CONNECT board** supports BSC firmware and is the currently recommended hardware. Its RS485 and CAN bus connections are galvanically isolated. Some components missing compared with the original BSC mainboard can be partly replaced by external modules (see below).

One possible supplier is [LILYGO T-CONNECT on AliExpress](https://de.aliexpress.com/item/1005007619430455.html).

!!! danger "Important"
    Make sure you buy the **variant with 3 RS485 interfaces and 1 CAN interface**!

**Functional Limitations**

The T-CONNECT board has **no built-in relays, digital inputs or redundant power supply**, so there are functional limitations compared with the original BSC hardware.

The free firmware does **not support the display** on the T-CONNECT.

See the [pin header assignment](hardware.md#belegung-des-pin-headers) and [LILYGO T-CONNECT hardware information](hardware.md#lilygo-t-connect).

### Original BSC Mainboard {#originales-bsc-mainboard}

The original BSC mainboard was developed specifically for the project. It can be obtained from the [current PCB manufacturer](https://de.aliexpress.com/item/1005007096164253.html), but **availability there has been inconsistent in the past**.