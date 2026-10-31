# Data Devices {#data-devices}

**Data-device mapping** assigns an interface (for example a serial port) to an internal *data device*. Other settings, including inverter configuration, rely on this mapping.

```bsc-settings
version: v010
file: dataDeviceMapping.json
profile: off
section: UI_SECT_DATADEVICEMAPPING_DATA_DEVICE_MAPPING
```

- **Interface:** Select the connected interface, e.g. `Serial 0` or `Bluetooth 0`. **Unused** disables the data device.
- **Address:** Unique device address (**0–16**), configured or fixed by the manufacturer. Read [BMS Address Configuration](devices/bms.md#unterstutzte-bms) carefully: the address **on the BMS** can differ from the address **in BSC mapping**.
- **Name** (optional): Custom display name, also used in the device's MQTT topic.

!!! note "Name Restrictions"
    Names must not contain `#` or `+`.

Other settings list only **configured** devices with an assigned interface. If several BMS units share a serial interface using a supported daisy chain, give each the correct address for unique mapping and reliable communication.

!!! note "Check Addressing Rules"
    Correct mapping is essential for reliable operation. Follow your BMS system's addressing rules.

## Value Adjustment {#value-adjustment}

```bsc-settings
version: v010
file: dataDeviceMapping.json
profile: off
section: UI_SECT_DATADEVICEMAPPING_VALUE_ADJUSTMENTS
```

Value adjustment modifies the SoC sent to the inverter based on cell voltage. Settings apply **per data device**.

=== "Firmware >= V0.9.x"
    - **SoC linearisation:** Calculates SoC linearly between *Cellvoltage for SoC 0%* and *Cellvoltage for SoC 100%*. Both must be set, and the 100 % voltage must exceed the 0 % voltage.
    - **SoC 100% trigger mode:** Either **one cell reaches the threshold** (highest cell voltage is sufficient), or **all configured cells reach the threshold**.
    - **Cellvoltage for SoC 100% [mV]:** SoC only becomes 100 % at this threshold. Below it, the data-device SoC is used, capped at **99 %**. **0** disables this feature.
    - **Cellvoltage for SoC 0% [mV]:** Corresponding lower threshold. SoC becomes 0 % when voltage reaches or falls below it. **0** disables the feature.

    Linearisation example: **3.5 V → 100 %**, **2.9 V → 0 %**; at or above 3.5 V use 100 %, at or below 2.9 V use 0 %, and calculate linearly between them. This is useful for BMS units without their own SoC value.

=== "Standard Firmware"
    **SoC linearisation** is not a separate option; it is performed automatically in mode 2.

    **Mode 1: Fixed SoC at a Defined Cell Voltage**

    At or above the configured upper threshold, SoC is set to **100 %**. Below it, the BMS SoC is used again. Leave *Cellvoltage for SoC 0%* **empty**, so only the upper threshold is considered. Example: with an upper threshold of **3.5 V**, SoC becomes 100 % at 3.5 V and above, and reverts to the BMS value below 3.5 V.

    **Mode 2: Linear SoC Between Two Cell Voltage Thresholds**

    Define an upper threshold for 100 % and a lower threshold for 0 %. At or above the upper threshold, use 100 %; at or below the lower threshold, use 0 %. Between them, calculate linearly. Example: **3.5 V → 100 %**, **2.9 V → 0 %**. Useful for BMS units without their own SoC calculation.

!!! danger "Important"
    Cell voltages must match the specifications of the battery system for correct and safe operation.