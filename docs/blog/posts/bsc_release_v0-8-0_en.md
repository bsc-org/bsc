---
date: 2025-04-06
authors: [shiningman]
categories:
  - Release Notes (Insider)
---

[img_dashboard]: release_v0-8-0_de/dashboard.png
[img_LadestrombegrenzungGrafana]: release_v0-8-0_de/LadestrombegrenzungGrafana.png
[img_LadestrombegrenzungVrm]: release_v0-8-0_de/LadestrombegrenzungVrm.png

# Version 0.8.0 (EN)
This version brings several improvements and enhancements, most notably the new **Dashboard**. Below is an overview of all changes since the last stable release:

## 🌐 Dashboard
One of the biggest changes is the new dashboard. It provides a quick overview of all system-relevant information and live data.

<!-- more -->

![img_dashboard]

## ✨ New Features

- **Plausibility check for text input fields in the WebUI**  
  This feature improves input reliability and reduces configuration errors.

- **Immediate start of the autobalancer via trigger**  
  The autobalancer can now also be started directly via a trigger, offering more flexibility in operation.

- **Additional options for the autobalancer**  
  The autobalancer now offers extra options to better adapt it to specific requirements.
    - **Send balance voltage as soon as start time is reached**  
      With this option, the balance voltage is sent as soon as the defined start time is reached.
    - **On start cell voltage drop → step 'Wait for start cell voltage'**  
      If the defined start cell voltage is not reached, this option returns the process to the step “Wait for start cell voltage.” All running timers will be reset in this case.
    - **Disable CutOff from step 'Wait for start cell voltage'**  
      This option disables the CutOff feature already in the “Wait for start cell voltage” step.

- **Dynamic voltage regulation to limit charging current**  
  This feature dynamically adjusts the charging voltage to keep the charging current within the configured range. If the charging current exceeds or falls below the defined limits, the voltage is automatically corrected.  <br><br>
  This function allows charging the battery only up to a specific SoC (State of Charge) to extend its lifespan.  <br><br>
  The diagrams show a Victron system with active voltage regulation. It is clearly visible that the charging current is limited and no energy flows into the battery. Instead, the excess energy is fed into the grid, while the SoC remains almost constant over time.<br>
  ![img_LadestrombegrenzungGrafana]
  ![img_LadestrombegrenzungVrm]<br>

- **Support for PACE PC200 via RS232**  
  The device can now also be read via the serial interface (RS232).

## 🔌 REST API Enhancements

- **New REST endpoint: `/restapi/io`**  
  Digital inputs and relay statuses can now be queried via this new REST endpoint.

- **Setting `vTrigger` via the REST API**  
  This extends control capabilities from external systems and allows for more flexible integration.

## 🛠️ Adjustments & Bugfixes

- **Adjustment of the temperature range for alarm rules**  
  The temperature range for alarm rules has been optimized.

- **Fix for data type issues in “reduce charging current – SoC”**  
  A data type issue related to SoC charge control has been resolved.

- **Bugfix when reading PIC data on SeplosV3**  
  An issue with reading PIC data on the SeplosV3 platform has been fixed.
