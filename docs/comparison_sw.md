# Software Version Comparison
A quick overview of what you get with the **Free Version** versus the **Sponsor Version**.  
The sponsored version offers you the latest features, advanced control functions, and a modern user interface – ideal for those who always want the newest features.

| Feature | Free Version | Sponsor Version |
|---------|:------------:|:---------------:|
| **<br>:material-alpha-a-box: Web Interface** |
| **Modern Web Application** <br> A fast, modern, feature-rich web app for configuring and managing the system |  | :material-check: |
| **Extended Dashbaord** [:material-information:](dashboard.md/#ubersicht) <br> Advanced dashboard with rich insights like live charging control data and data-device information |  | :material-check: |
| **Web Interface Dark Mode** |  | :material-check: |
| **Standart Webapplikation** <br> A simple but functional web app for the system configuration | :material-check: |  |
| **Standart Dashboard** <br> A lightweight dashboard showing the most important key metrics | :material-check: |  |
| **Login screen with Autologout** |  | :material-check: |
| **Basic Web Authentication** | :material-check: |  |
| **<br>:material-alpha-b-box: General** |
| **Wi-Fi Reconnect** <br> If the connection to the access point is lost, the system will periodically retry and restore it automatically |  | :material-check: |
| **MQTT** [:material-information:](mqtt.md) | :material-alert: | :material-check: |
| **REST-API** [:material-information:](restapi.md) | :material-alert: | :material-check: |
| **Settings Export & Import** |  | :material-check: |
| **Maintenance Mode** <br> Temporarily exclude individual battery packs from control and monitoring for service or troubleshooting |  | :material-check: |
| **<br>:material-alpha-c-box: Inverter / General** [:material-information:](settings_inverter.md) |
| **Data Sources** <br> Define which devices provide the data that is sent to the inverter | :material-check: | :material-check: |
| **Aggregation SoC** <br>  Advanced selection and weighting of devices for calculating state of charge | :material-check: | :material-check: |
| **Aggregation Total Voltage** <br> Advanced selection and weighting of devices for calculating overall voltage |  | :material-check: |
| **Aggregation Total Current** <br> Advanced selection and weighting of devices for calculating overall current |  | :material-check: |
| **Battery Temperature Sensors** <br> Manual selection of sensors used for battery temperature | :material-check: | :material-check: |
| **Cell Temperature Sensors** <br> Manual selection of sensors used for cell temperature |  | :material-check: |
| **Charging voltage ramp** <br> Define how quickly charging voltage changes (voltage/time ramp) when adjustments are needed |  | :material-check: |
| **<br>:material-alpha-d-box: Inverter / Charge Control** [:material-information:](settings_inverter_charge.md) |
| **Maximum device current** <br> Note: In the Sponsor Version the limit is defined by the inverter’s CAN protocol — not by the BSC | 320 A | 3200 A |
| **Dynamic charge voltage offset** |  | :material-check: |
| **Reduce charging current - temperature** |  | :material-check: |
| **Reduce charging current - temperature profile** |  | :material-check: |
| **Voltage regulation for current zero control** |  | :material-check: |
| **Charging current per pack too high** <br> Sponsor Version: can additionally use current calculated from C-rate and temperature as a control basis | :material-alert: | :material-check: |
| **Autobalance** <br> Sponsor Version includes additional advanced options | :material-alert: | :material-check: |
| **Throttle the charging current depending on the cell voltage** | :material-check: | :material-check: |
| **Reduce charging current in case of cell drift** | :material-check: | :material-check: |
| **Reduce charging current - SoC** | :material-check: | :material-check: |
| **Charging current Cut-Off** | :material-check: | :material-check: |
| **Set SoC when the cell voltage falls below** | :material-check: | :material-check: |
| **Discharging current per pack too high** |  | :material-check: |
| **Throttling the discharge current depending on the cell voltage** | :material-check: | :material-check: |
| **<br>:material-alpha-e-box: Alarm Rules / Plausibility Check** |
| **Plausibility check** |  | :material-check: |
| **Value comparison** |  | :material-check: |
| **<br>:material-alpha-f-box: Alarm Rules / BMS** |
| **No data from BMS** | :material-check: | :material-check: |
| **Voltage monitoring cell min/max** | :material-check: | :material-check: |
| **Voltage monitoring battery pack min/max** | :material-check: | :material-check: |
| **<br>:material-alpha-g-box: Alarm Rules / Temperature** |
| **Sensor error alarm (Onewire)** | :material-check: | :material-check: |
| **Temperature monitoring** | :material-check: | :material-check: |
| <br>**:material-alpha-h-box: Triggers** |
| **Trigger Übersicht** <br> Overview of all configured triggers currently in use |  | :material-check: |
| **Trigger Scheduler** <br> Activate triggers on a time schedule |  | :material-check: |
| **Trigger on SoC** <br> Activate a trigger when a defined SoC threshold is reached | :material-check: | :material-check: |

## Legend

| Symbol | Meaning |
|:------:|---------|
| :material-check: | Included |
| :material-alert: | Limited |
