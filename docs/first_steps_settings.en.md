# Operating Settings for the BSC {#einstellungen-fur-den-betrieb-des-bsc}

This chapter introduces the settings required to operate the BSC. Available settings may vary by firmware version.

!!! tip "Setup Assistant"
    The web app provides [setup assistants](setup_assistant.md) for networking, MQTT, serial interfaces and the inverter. They guide you through the main steps and populate data-device mapping automatically.

## 1. Basic Settings {#1-grundeinstellungen}

Basic settings are in the **System** menu, including Wi-Fi credentials and, if MQTT is used, MQTT broker details. Open **Settings / System**.

Further information: [System Settings](settings_bsc.md#system).

## 2. BMS Settings in the BSC {#2-bms-einstellungen-im-bsc}

The following configuration is necessary for communication.

!!! note "Read-Only Access"
    The BSC accesses BMS data **only for reading**. It never writes settings, configuration or other data **to the BMS**. The BMS therefore remains a functionally independent safety layer.

### 2.1 Configure the Serial Interface {#21-serielle-schnittstelle-konfigurieren}

Specify which **BMS type** is connected to which **hardware interface**. Example: a **JK Inverter BMS** connected to *Serial 0*:

- Serial 0: **JK Inverter BMS**
- Serial 1: unused
- Serial 2: unused

Menu: **Settings / Interfaces / Serial**.

!!! note "Multiple BMS Units"
    Several BMS units of the same type can share one interface. They are distinguished by addresses, configured in the next step (data-device mapping).

Further information: [Serial Interfaces](settings_bsc_interfaces.md#serial).

### 2.2 Set Up Data-Device Mapping {#22-data-device-mapping-einrichten}

After assigning a **BMS type** to each **serial interface**, map each **individual BMS** and its specific **address**.

A **data device** is the BSC's internal representation of a physical device (BMS, Victron SmartShunt, etc.). Correct address mapping is necessary for communication. Each BMS needs a unique address, particularly when several units of the same type share an interface.

Menu: **Settings / Interfaces / Data devices**.

Configure the following for each data device:

- **Interface:** Select the hardware interface (Serial 0, Serial 1, etc.).
- **Address:** BMS-specific address (0–16).

    !!! info "Check Address Configuration"
        Addresses must be correct both **on the BMS itself** and **in BSC data-device mapping**. Read the [BMS-specific address instructions](devices/bms.md#serial-bms) carefully: requirements differ between BMS types.

- **Name** (optional): A display name to identify the device throughout the BSC menus.

Example: two JK Inverter BMS units on *Serial 0*:

- **Data device 0:** Serial 0, address 1, name "Lower battery"
- **Data device 1:** Serial 0, address 2, name "Upper battery"

Further information:

- [Address Configuration by BMS Type](devices/bms.md#unterstutzte-bms)
- [Data-Device Mapping Details](settings_bsc_data_devices.md#data-devices)

## 3. Inverter Settings {#3-wechselrichter-einstellungen}

These are the basic settings needed for communication between the BSC and inverter.

### 3.1 General Settings {#31-allgemeine-einstellungen}

Menu: **Settings / Inverter & Charge Control / General**.

- **BMS CAN-Bus Enable:** Enables inverter communication.
- **CAN bus protocol:** Select the protocol for your inverter, such as *Victron* or *Pylontech*. Most inverters require **Pylontech**.
- **Data source:** Select the data devices whose data is processed and sent to the inverter. Processing can include aggregation of several sources or application of charge control rules.

    !!! note "Value Sources"
        [Valuehandling settings](settings_inverter.md#valuehandling-multi-bms) specify the domain, source and aggregation for each measurement. If [group devices](settings_bsc_group-devices.md#group-devices-batterie-gruppen) are enabled, they can also be selected as sources.

- **Valuehandling category:** Select which values come from which data devices and how they are aggregated. See [Multi-BMS Valuehandling](settings_inverter.md#valuehandling-multi-bms).
- **Basic data category:** Set charging voltages and maximum currents for the entire system. Under *Batterypack settings*, capacity and maximum currents can also be set per data device.

Further information: [Inverter Settings](settings_inverter.md#wechselrichter).

### 3.2 Charge Control Settings {#32-einstellungen-zur-laderegelung}

See [Charge Control](settings_inverter_charge.md).

## 4. Alarm Rules {#4-alarmregeln}

Alarm rules monitor selected data-device values and activate triggers when limits are reached. They do not replace correct BMS settings, but allow an earlier response, for example:

- Set inverter charging current to 0 A.
- Switch a relay.
- Send a notification: when MQTT is enabled, trigger states are published via MQTT and can be processed by automation software such as ioBroker or Home Assistant for notifications or control commands.

Further information: [How Triggers Work](settings_bsc_trigger.md#funktionsprinzip-der-trigger).