# Setup Assistants {#einrichtungsassistenten}

The web app provides **four setup assistants** for initial configuration. Open them from the web app menu. They write directly to the corresponding settings pages.

## Network {#netzwerk}

Configures basic Wi-Fi: **SSID** (network name) and **password**.

## MQTT {#mqtt}

Four steps, followed by a summary:

1. **Activation:** Enable or disable MQTT globally.
2. **Connection:** Broker IP, port and MQTT device name.
3. **Login and topic:** Optional username/password and MQTT topic name.
4. **Publishing:** Send interval in seconds.

## Serial Interfaces {#serielle-schnittstellen}

Configure device type and chain length on **Serial 0–2**. The assistant then **automatically fills data-device mapping**, creating a device for each specified unit with the appropriate interface and consecutive address.

## Inverter {#wechselrichter}

Four steps for inverter and basic charge control, followed by a summary:

1. **Enable CAN and select protocol:** Enables *BMS CANbus enable*, selects the CAN protocol and uses active data devices as sources.
2. **Basic values:** Requests cell count and maximum cell voltage. Calculates **absorption voltage** (maximum cell voltage × cell count, rounded **up to 0.1 V**), **float voltage** (**3.37 V × cell count**) and **float voltage SoC** (**90 %**).
3. **Cell voltage reduction:** Enables charge reduction and sets start cell voltage, float maximum cell voltage and minimum current to established values (**3370 mV / 0 A**).
4. **Cell voltage difference reduction:** Enables it with start voltage **3400 mV**, start difference **20 mV** and reduction **2 A per mV**.

!!! note "Only Listed Parameters Are Changed"
    All other settings remain unchanged and can be adjusted afterwards on their settings pages.