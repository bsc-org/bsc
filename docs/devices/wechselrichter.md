

## Victron MP2 48/5000/70 
**Andere Typen des Wechselrichters sind vermutlich im gleichen Stil anzubinden.**

### Physische Verbindung der Komponenten

* Victron Intern<br>
MP2 <-> MK3-USB-Adapter <-> VenusOS (z.B. RaspberryPi+CAN,RS485-Shild) <br>

* BSC<br>
BSC (CAN) <-> RaspberryPi+CAN-Shild <br> <br>

### CAN-Verbindung
* H auf H
* L auf L
* GND auf GND <br>

|CAN|[Victron VE.Can Port](https://www.victronenergy.com/live/battery_compatibility:can-bus_bms-cable)|
|---|---|
|CAN-GND|Pin 3|
|CAN-L|Pin 8|
|CAN-H|Pin 7|<br>

### Einstellungen BSC
Einstellungen -> Wechselrichter & Laderegelung (Inverter) -> Allgemein<br>
![image](../../img/devices/devices_inverter_canbus.png)
<br>
Die Option "Send extended data" hat nur in Verbindung mit dem [dbus-bsc-can](https://github.com/shining-man/dbus-bsc-can) eine Funktion.<br>
<br>
In Verbindung mit einem CerboGX ist die Option **nicht zu empfehlen**, da diese Hardware zu wenig Performance hat und es dadurch zu Problemen kommen kann.<br>
Die Probleme können sein, dass bei gesetzter Funktion in seltenen Fällen ein SOC von 0% für ca. 30s übermittelt wird!

### Einstellungen VenusOs
Menü -> Settings -> Services -> can[0,1,2,3,...] -> Can Bus-Profile<br>
![image](../../img/devices/devices_inverter_venus_canbus.png)
<br><br>
Network status wenn alles klappt<br>
![image](../../img/devices/devices_inverter_venus_canbus2.png)
<br><br>
Alles wird erkannt<br>
![image](../../img/devices/devices_inverter_venus_canbus_devicelist.png)

### BSC Log-Ausgabe wenn Inverter erkannt wurde
![image](../../img/devices/devices_inverter_can_log.png)

### Bekannte Besonderheiten
#### Akku wird in das Netz entladen
Der SoC erreicht 100% und wird beim Wechsel auf die Float-Voltage wieder entladen.<br>
Grund: Dies ist ein vom **BSC unabhängiges Verhalten**. Wenn in den Victron Einstellungen die Option „Gleichstromgekoppelte PV-Einspeisung von Überschuss“ mit ESS aktiviert ist, versucht das Victron System die Spannung durch Entladen auf die Float-Voltage abzusenken.<br>
~~Abhilfe: z.B. Die Spannungsdifferenz zwischen Float- & Absorptionvoltage auf 0.4V absenken. Um ein ständiges Laden und Entladen über den Tag zu verhindern, sollte die Einstellung für "Float Ladespannung SoC" im BSC nicht zu hoch eingestellt werden, da sonst auf die Absorption Spannung gewechselt wird und der Vorgang von vorne beginnt.~~

#### Die Ladestrombegrenzung (CCL) wird ignoriert
Wenn der BSC von Absorption- auf Float-Voltage wechselt, wird die Ladestrombegrenzung auf 0A gesetzt. Das Victron System ignoriert diese Einstellung unter bestimmten Umständen.<br>
Grund: Wenn die Option „Gleichstromgekoppelte PV-Einspeisung von Überschuss“ mit ESS aktiviert ist, wendet das DVCC-System die DVCC-Ladestrombegrenzung von der PV-Anlage zur Batterie nicht an. Dieses Verhalten ist notwendig, um den Export zu ermöglichen. Es gelten weiterhin Grenzwerte für die Ladespannung.<br>
Quelle: [Victron](https://www.victronenergy.com/media/pg/CCGX/de/dvcc---distributed-voltage-and-current-control.html#UUID-0cda63b2-c80b-e81b-e174-f6a91ca5f848)


## Growatt SPF5000ES
Anbindung erfolgt über CAN-Bus.<br>
Als CAN-Protokoll im BSC muss das Pylontech-Protokoll definiert werden (Deye...).<br>
Die Checkbox "Send extendet data" muss nicht aktiviert werden.<br>

Protokolleinstellung am Inverter über Prg 005: "LI".<br>
Dann bestätigen und im darauf folgenden PRG 36: "L52" definieren.<br>

Nun sollte der SOC usw. abrufbar sein.

![Growatt](../../img/devices/devices_inverter_growatt_spf5000es.jpg)


##  Goodwe GW5048ES
Anbindung BSC <> Wechselrichter über CAN-Bus<br><br>
CANbus Inverter-Protokoll im BSC: "Deye"<br>

Akku Einstellung am Wechselrichter: "Goodwe 3x Secu-A5.4L"<br> 
Eine Protokolleinstellung am Wechselrichter ist nicht nötig.

BMS:<br>
2x Seplos V2 konfiguriert auf Pylontech Protokoll.<br>
Angeschlossen an BSC über Serial2 Schnittstelle.


## Solis S5-EH1P & RHI 5G

#### CAN-Verbindung
* H auf H
* L auf L
* GND gibt es beim Solis nicht

Belegung CAN Anschluss Solis<br>

| Signal  | Anschluss | Aderfarbe RJ45 |
| ------------- | ------------- | ------------- |
| CAN-L  | Pin 5  | Blau/Weiß |
| CAN-H  | Pin 4  | Blau |
| CAN-GND  | ?  | ? |

#### Einstellungen BSC
Einstellungen -> Wechselrichter & Laderegelung (Inverter) -> Allgemein<br>
Canbus -> Solis RHI auswählen -> Save<br>
BMS Canbus enable -> aktiveren -> Save<br>

#### Einstellungen Solis
Advanced Settings -> Storage Energy Set -> Battery Select -> Battery Module -> Pylon auswählen<br>

## Deye SUN-12K-SG04LP3-EU

Die Anbindung BSC <> Wechselrichter (CAN-Bus) erfolgt über den "BMS Port" des Wechselrichters (siehe Manual Seite 10).<br>
Dieser Port wird mit einem handelsüblichen Netzwerkkabel mit der RJ45 Buchse (Serial2) des BSC verbunden.<br>
<br>
<img src="../../img/devices/devices_inverter_deye_sun_12k_sg04lp3-eu.png" width="450">

#### Einstellung am Wechselrichter
"Bat Set 1: Batt Mode "Lithium", Bat Set 3: "Lithium Mode 00"<br> 
![SystemSetup](../../img/devices/devices_inverter_deye_sun_12k_sg04lp3-eu_settings1.png)
![BatterySettings](../../img/devices/devices_inverter_deye_sun_12k_sg04lp3-eu_settings2.png)
![BatterySettings3](../../img/devices/devices_inverter_deye_sun_12k_sg04lp3-eu_settings3.png)

#### Einstellungen im BSC
Einstellungen -> Wechselrichter & Laderegelung -> Allgemein<br>
BMS CANbus enable<br>
CANbus-Protocol: "Pylontech"<br>
Datenquelle (Master): "Serial 2"