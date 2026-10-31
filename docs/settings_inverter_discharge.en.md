Configure discharge-current limits based on cell voltage, temperature, temperature profiles and per-pack current. Set pack currents under [Inverter / Basic Data / Batterypack Settings](settings_inverter.md#basisdaten). Temperature rules work like their [charging equivalents](settings_inverter_charge.md).

## Excessive Discharge Current per Pack {#entladestrom-pro-pack-zu-gro}

Automatically and dynamically adjusts discharge current to keep each battery pack within its configured [per-pack discharge limit](settings_inverter.md#basisdaten), protecting against overcurrent.

```bsc-settings
version: v010
file: inverterDischarge.json
profile: off
section: UI_SECT_INVERTERDISCHARGE_ENTLADESTROM_PRO_PACK_ZU_GROSS
```

## Cell-Voltage-Dependent Discharge Reduction {#entladestrom-zell-spannungsabhangig-drosseln}

Adjusts discharge current based on cell voltage to protect cells and their service life.

```bsc-settings
version: v010
file: inverterDischarge.json
profile: off
section: UI_SECT_INVERTERDISCHARGE_ENTLADESTROM_ZELL_SPANNUNGSABHAENGIG_DROSSELN
```

- **On/Off:** Enables cell-voltage-dependent reduction.
- **Start below cell voltage:** Reduction starts when the lowest cell falls below this threshold.
- **End cell voltage:** At or below this voltage, current is reduced to the configured minimum.
- **Minimum discharge current:** Lower bound used below the end voltage.

!!! note "Threshold Order"
    End cell voltage must always be **lower** than start cell voltage.

## Temperature-Dependent Discharge Reduction {#entladestrom-reduzieren-temperatur}

Up to **4** individually configurable temperature rules use active data or group sources. Cold-side reduction uses the minimum temperature; hot-side reduction uses the maximum.

```bsc-settings
version: v010
file: inverterDischarge.json
profile: off
groups: 1
section: UI_SECT_INVERTERDISCHARGE_ENTLADESTROM_REDUZIEREN_TEMPERATUR
```

- **Data-device sensors:** Sensors **0–5**.
- **Extended sources / sensors 0–31:** Additional sensors, e.g. OneWire.
- **Reduction start:** Temperature where reduction starts, default **20.00 °C**.
- **Reduction end:** Temperature where current reaches **0 A**, default **0.00 °C**.

Reduction is linear between thresholds and can work for rising or falling temperatures. See the [charging examples](settings_inverter_charge.md#ladestrom-reduzieren-temperatur), which apply analogously.

## Temperature-Profile Discharge Reduction {#entladestrom-reduzieren-temperaturprofil}

A freely defined **10-point** temperature profile assigns a maximum **C-rate** to each temperature. Interpolate linearly between points; below/above the profile, use its first/last point.

```bsc-settings
version: v010
file: inverterDischarge.json
profile: off
section: UI_SECT_INVERTERDISCHARGE_ENTLADESTROM_REDUZIEREN_TEMPERATURPROFIL
```

- **Data-device sensors:** Sensors **0–5** used in control.
- **Extended sources / sensors 0–31:** Additional sources such as OneWire.
- **Temperature profile:** **10** temperature/C-rate pairs. Temperature range **−30 to 60 °C**, step **0.1 °C**; C-rate step **0.01 C**.

Discharge current is **C-rate × capacity (Ah)** using capacities from [Batterypack Settings](settings_inverter.md#basisdaten), capped by the maximum discharge current. With no configured capacity, discharge current is limited to **0 A**.