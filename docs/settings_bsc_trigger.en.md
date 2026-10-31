## How Triggers Work {#funktionsprinzip-der-trigger}

Internal triggers monitor values such as temperature or voltage and enable responses to potentially dangerous conditions.

**Trigger Function**

A source activates a trigger when its configured limit is reached. A trigger does **not itself perform an action**. Configure consumers separately, for example to switch a fan relay or tell the inverter to reduce charging current to **0 A**. Up to **27** internal triggers can combine sources and actions flexibly. External systems can also activate them through [virtual triggers](mqtt.md#virtual-trigger).

**Multiple Sources**

- **Activation (high):** Active when **at least one** connected source exceeds its limit.
- **Deactivation (low):** Inactive only when **all** connected sources return to normal.

!!! note "Reset Virtual Triggers"
    Automations using [vTriggers](mqtt.md#virtual-trigger) must explicitly deactivate them too.

**Example**

Sensors **2 and 3** monitor a **30 °C** threshold. If either exceeds it, trigger **1** activates. Relay **1** can then start a fan while the inverter reduces charging current to limit heat generation.

This separation of flexible sources and configurable actions permits early detection and tailored responses.

## Trigger Names {#triggername}

```bsc-settings
version: v010
file: trigger.json
profile: off
section: UI_SECT_TRIGGER_TRIGGERNAME
```

Assign names of up to **16 characters** to the **27** triggers. Names appear throughout the system, including trigger selectors.

## Trigger Scheduler {#trigger-scheduler}

```bsc-settings
version: v010
file: trigger.json
profile: off
section: UI_SECT_TRIGGER_TRIGGER_SCHEDULER
```

Five independently configurable schedulers activate triggers by time.

!!! note "Firmware Availability"
    The scheduler is not available in every firmware version.

- **Trigger:** Select trigger **1–27**.
- **Month:** Select active months.
- **Weekday:** Select active weekdays.
- **From:** Start time.
- **Until:** End time.