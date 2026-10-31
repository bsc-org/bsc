# External Shunts {#externe-shunts}

The BSC can obtain a battery's state of charge (SoC) from an external shunt. Currently, **Victron SmartShunt** is supported through its VE.Direct interface. It provides SoC, total battery voltage and current.

## Victron SmartShunt {#victron-smartshunt}

### Why Use an External Shunt? {#vorteil-des-externen-shunts}

The SmartShunt continuously measures current at its measurement point and calculates SoC by coulomb counting. This SoC is independent of the BMS calculation, which can drift over time on many BMS systems. An external shunt is therefore a useful addition for accurate SoC measurement. The BSC can use its SoC, voltage and current for inverter communication and SoC-dependent charge control.

!!! note "Select the Source Explicitly"
    Shunt SoC does **not automatically replace BMS SoC**. Select the shunt as the source under **Valuehandling**: see [step 3](#3-shunt-als-quelle-wahlen-valuehandling).

!!! warning "No Cell Voltages from the Shunt"
    The SmartShunt supplies neither cell voltages nor temperature values. Charge control requiring cell voltages cannot operate with the shunt alone: an additional BMS is required (see [Data Source](../settings_inverter.md#general)).

### Hardware Connection {#hardwareverbindung}

Connect the VE.Direct port through the **Single device extension (SDE)**, since BSC serial interfaces use RS485. The adapter is available from the [BSC Shop](https://bsc-shop.com/produkt/single-device-extension/) and connects to the BSC using a standard RJ45 network cable.

A galvanically isolated adapter is unnecessary because the BSC serial inputs are already isolated ([CAN/RS485](../hardware.md#canrs485)). Each SDE connects exactly one device. For more serial ports, use the Serial Extension (Serial 3–10; see [Serial](../settings_bsc_interfaces.md#serial)).

### BSC Settings {#einstellungen-im-bsc}

Setup consists of selecting the serial device type, mapping the interface to a data device and choosing the shunt as the source of the required values. Step 4 covers optional value adjustment.

#### 1. Select the Serial Device Type {#1-geratetyp-an-der-serial-schnittstelle-auswahlen}

Open **Settings / Interfaces / Serial**. Select **Victron SmartShunt** on the port connected to its SDE. The BSC automatically sets **19200 baud**. See [Serial](../settings_bsc_interfaces.md#serial).

#### 2. Assign Data-Device Mapping {#2-schnittstelle-im-data-device-mapping-zuordnen}

Open **Settings / Interfaces / Data devices** ([details](../settings_bsc_data_devices.md#data-devices)):

- **Interface:** Port from step 1.
- **Address:** **0**. VE.Direct has no addressing; firmware permits only address 0 for the shunt.
- **Name** (optional): Shown in source lists and used for the data device's MQTT topic.

#### 3. Select the Shunt as a Valuehandling Source {#3-shunt-als-quelle-wahlen-valuehandling}

Under **Settings / Inverter & Charge Control / General / Valuehandling**, select the shunt ([Valuehandling](../settings_inverter.md#valuehandling-multi-bms)):

- **SoC source:** Select the shunt to transmit its SoC to the inverter.
- **Total voltage source** and **total current source:** Optionally select the shunt for these values too.

The resulting SoC is sent to the inverter and controls all SoC-dependent functions, including SoC-based charging-current reduction and Charge-Current Cut-Off. Without explicit selection, configured sources continue to be used; there is no automatic replacement.

#### 4. Value Adjustment for the Shunt {#4-value-adjustment-fur-den-shunt}

Shunt SoC passes through the same [value adjustment](../settings_bsc_data_devices.md#value-adjustment) as every other data device. With defaults (all functions disabled), it passes through unchanged.

!!! warning "Do Not Use Cell-Voltage-Based Corrections for the Shunt"
    *Cellvoltage for SoC 100 %*, *Cellvoltage for SoC 0 %* and *SoC linearisation* evaluate that data device's cell voltages. Since the SmartShunt has none, keep these corrections disabled:

    - Setting *Cellvoltage for SoC 0 %* would keep shunt SoC at **0 %**, as the threshold is always treated as undershot without cell voltage data.
    - Setting *Cellvoltage for SoC 100 %* would cap SoC permanently at **99 %**, as that threshold is never reached.
    - Enabling *SoC linearisation* with cell voltage values configured would hold SoC permanently at **0 %**.

### Shunt Values in the BSC {#werte-des-shunts-im-bsc}

The BSC regularly reads **SoC (0.01 % resolution)**, **total battery voltage** and **current (0.1 A resolution)**. Additional regularly retrieved MQTT values include time-to-go, cycles, minimum and maximum voltage, time since full charge, SoC synchronisation count, under-/overvoltage alarm counts, and charged/discharged energy. These are automatically available in Home Assistant through [auto-discovery](../mqtt.md#home-assistant-auto-discovery).