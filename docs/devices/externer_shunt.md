# Externe Shunts

## Victron SmartShunt

### Hardwareverbindung

Damit die Verbindung vom SmartShunt zum BSC hergestellt werden kann, muss zwischen dem VE.Direct Port (UART 3,3V) und dem BSC (RS485) ein entsprechender 3,3V kompatibler Konverter verwendet werden.  
Ein galvanisch getrennter Typ ist hierbei nicht notwendig, da diese Trennung am BSC ohnehin vorliegt. Der Anschluss erfolgt über A/B/GND.

#### Der zu verwendende Stecker
Hersteller: JST  
Serie: PH  
Pol-Anzahl: 4  
Rastermaß: 2.0mm  
Bestellnr.: JST PHR-4  

![](../img/devices/devices_shunt_smartshunt_vedirect_stecker.png){  width="550" }

#### Aderfarben eines original VE.Direct Kabels. (Ohne Gewähr der Information auf Ihr verwendetes Kabel)

|  PinNr | Aderfarbe  |
| :------------ | :------------ |
| 1  | rot  |
| 2  |  grün |
|  3 |  weiß |
|  4 | schwarz  |

#### Beispiel eines einzusetzenden UART/RS485 Konverters
![](../img/devices/devices_shunt_smartshunt_rs485_converter.png){  width="300" }

Es hat sich herausgestellt, dass der SmartShunt nicht alle Typen der UART/RS485 Wandler mit Strom versorgen kann.  
Der Konverter sollte nicht mehr wie 10mA (Puls max. 20mA/5ms) aufnehmen.  
Ansonsten muss eine externe Spannungsversorgung für den Konverter verwendet werden!

#### Anschlusstabelle

| SmartShunt | Adapter UART Seite | Adapter RS485 Seite | BSC (Serial 0) |
| ------------ | ------------ | ------------ | ------------ |
| Pin1(GND) | GND | GND | S0 GND |
| Pin2(Rx) | TxD | A+ | S0 Rx/A |
| Pin3(Tx) | RxD | B- | S0 Tx/B |
| Pin4(3V3) | VCC |  |  |

Verschiedene, vorzugsweise chinesische Konverter, haben eine falsche TxD/RxD-Bedruckung. Bei diesen müssen die beiden Signale dann invertiert angeschlossen werden.

### Einstellungen BSC

#### Definition der seriellen Schnittstelle
Einstellungen -> Schnittstellen -> Serial -> Auswahl des Victron SmartShunt

#### Benötigtes Valuehandling
![](../img/devices/devices_shunt_smartshunt_bsc_settings.png){  width="400" }

Einstellungen sind zu finden wie folgt
- Einstellungen -> Wechselrichter & Laderegelung -> Allgemein -> Valuehandling Multi-BMS -> SoC  
Selektion: BMS  

- Einstellungen -> Wechselrichter & Laderegelung -> Allgemein -> Valuehandling Multi-BMS -> BMS für SOC  
Selektion: Auswahl der Schnittstelle, wo der Smartshunt angeschlossen ist.  

Hierdurch wird nur noch der SoC des SmartShunt genutzt und an den Wechselrichter weiter geleitet.