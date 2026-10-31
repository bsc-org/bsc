## System Overview {#systemuberblick}

The BSC is a freely configurable controller linking components of a DIY battery system. It can handle monitoring and control tasks, including central charge control.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'fontSize': '16px', 'fontFamily': 'Arial', 'edgeLabelBackground': 'white'}}}%%
flowchart TD
    BMS[BMS] -- "RS485<br>(Serial 0-2)" --> BSC
    BMS -- UART/RS232 --> SDE["Single<br>device<br>extension"] --> BSC
    TEMP_SENSOR["Temperature<br>sensors"] -- OneWire --> BSC
    VICTRON_SHUNT["Victron<br>SmartShunt"] --> VICTRON_SHUNT_CONV["Single<br>device<br>extension"] --> BSC
    BSC -- CAN --> CAN[Inverter]
    BSC <-- MQTT --> MQTT_BROKER[MQTT broker]
    BSC -- REST --> REST[REST client]
    DigitalIn --> BSC
    BSC --> RelayOut
    BSC -.- Display[Display]
    SE["Serial Extension<br>(Serial 3-10)"] -.- BSC
    BMS -- RS485 --> SE
    BSC[Battery Safety Controller]
    subgraph Battery
        BMS
        TEMP_SENSOR
        VICTRON_SHUNT
    end
    subgraph Outputs[Data output]
        CAN
        MQTT_BROKER
        REST
        Display
    end
    subgraph Signals[External signals]
        DigitalIn[4 digital inputs]
        RelayOut[6 relay outputs]
    end
    style BSC fill:#ffdbaa
```

## Components {#komponenten}

- **BSC:** PCB and software with Wi-Fi, Bluetooth, RS485, CAN, OneWire and digital inputs/outputs. Available support depends on hardware and firmware.
- **Display:** Optional I²C display. See [Hardware](hardware.md#bsc-display) and a [suitable enclosure](https://bsc-shop.com/produkt-kategorie/gehaeuse/).
- **Single device extension:** Connects a non-RS485 device to the BSC.
- **Serial Extension:** Adds **8** RS485 ports to the BSC's **3**. See the [extension repository](https://github.com/shining-man/bsc_extension_serial).
- **BMS:** Provides battery state including cell voltages, SoC and temperatures. Connections can include RS485, CAN or Bluetooth where supported; see [Supported BMS Units](devices/bms.md) and current [interface limitations](settings_bsc_interfaces.md#bluetooth).
- **Temperature sensors:** Additional sensors via OneWire or digital/analogue inputs can supplement BMS data.
- **Shunt:** Provides external SoC. Currently Victron SmartShunt is supported through the Single device extension. See [External Shunts](devices/externer_shunt.md).
- **Inverter:** CAN communication with devices such as Victron, Solis or Deye reports battery state and control values such as charging limits. See [Inverters](devices/wechselrichter.md).

## Available Interfaces {#verfugbare-schnittstellen}

- **Wi-Fi:** Web interface access and MQTT transmission.
- [**RS485**](hardware.md#rs485-bms): BMS data.
- [**CAN bus**](hardware.md#canrs485): Inverter communication.
- [**OneWire**](hardware.md#onewire): Sensor data, e.g. temperature.
- [**Digital inputs**](hardware.md#digitale-eingange): Galvanically isolated digital signals.
- **Digital outputs:** External device control through relays.
- [**MQTT broker**](mqtt.md): Battery/system state for home automation, long-term storage and visualisation, e.g. Grafana.
- [**REST client**](restapi.md): HTTP API access to battery and BSC state.