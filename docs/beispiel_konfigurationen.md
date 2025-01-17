## Wichtiger Hinweis! Zuerst lesen!
Die hier aufgeführten Einstellungen und Konfigurationsvorschläge basieren auf Erfahrungswerten von Anwendern und sind speziell für LiFePo4-basierte Zellen entwickelt. Sie dienen lediglich als Orientierungshilfe und stellen einen **Erstentwurf** für eine mögliche Konfiguration mit den beschriebenen Geräten dar.  

Bitte beachten Sie, dass wir keine Gewährleistung oder Garantie für die Richtigkeit, Vollständigkeit oder Anwendbarkeit der bereitgestellten Informationen übernehmen können. Die korrekte Anpassung dieser Einstellungen an Ihr spezifisches System erfordert fundiertes technisches Fachwissen. Es liegt in Ihrer Verantwortung, die bereitgestellten Informationen sorgfältig zu überprüfen, zu verstehen und gegebenenfalls anzupassen, bevor Sie diese in Ihrem System implementieren.  

Wir raten dringend davon ab, die dargestellten Einstellungen unreflektiert zu übernehmen. Nehmen Sie sich die notwendige Zeit, die vorgeschlagenen Konfigurationen in ihrer Gesamtheit zu verstehen und sicherzustellen, dass sie für Ihre individuellen Anforderungen und Systeme geeignet sind. Eine unsachgemäße Anwendung kann zu Schäden an den Geräten, den Batterien oder sogar zur Gefährdung Ihrer Sicherheit führen.  

**Hinweis:** Die Nutzung der hier aufgeführten Informationen erfolgt auf eigenes Risiko. Wir übernehmen keine Haftung für direkte oder indirekte Schäden, die aus der Anwendung der bereitgestellten Einstellungen entstehen könnten.  

## Konfigurations-Beispiele
### 5x JK-InverterBMS 200A (16S); 2x Victron Multiplus 5000

#### BSC - Einstellungen Serielle Schnittstelle

![](img/beispielconfig/beispielcfg_serial.png){ width="450" }


#### BSC - Einstellungen Inverter
##### Allgemein
Serial 6 wurde hier als Datenquelle (Master) BMS gesetzt, da hier durch die höchste Position im Stack, die höchsten Temperaturen auftreten.  
Diese Temperatur wird genutzt für die Übertragung der "Batterie Temperatur" an Venus OS. Sensor Nummer 1 hatte in dieser Umgebung in der Regel die höchste Temperatur.  
![](img/beispielconfig/beispielcfg_inverter_general_1.png){ width="450" }
  
![](img/beispielconfig/beispielcfg_inverter_general_2.png){ width="450" }

##### Laden
![](img/beispielconfig/beispielcfg_inverter_charge_1.png){ width="450" }
![](img/beispielconfig/beispielcfg_inverter_charge_2.png){ width="450" }

##### Entladen
![](img/beispielconfig/beispielcfg_inverter_discharge_1.png){ width="450" }

#### BMS
##### Settings
![](img/beispielconfig/beispielcfg_bms_settings_jk_1.png){ width="350" }
![](img/beispielconfig/beispielcfg_bms_settings_jk_2.png){ width="350" }
![](img/beispielconfig/beispielcfg_bms_settings_jk_3.png){ width="350" }
![](img/beispielconfig/beispielcfg_bms_settings_jk_4.png){ width="350" }

##### Control
![](img/beispielconfig/beispielcfg_bms_settings_jk_5.png){ width="350" }


### 1x Seplos 10E 200A (16S); 3x Growatt SPF5000ES

#### BSC - Einstellungen Inverter
##### Allgemein
![](img/beispielconfig/beispielcfg_inverter_general_seplos.png){ width="1050" }

##### Laden
![](img/beispielconfig/beispielcfg_inverter_charge_seplos.png){ width="1050" }

##### Entladen
![](img/beispielconfig/beispielcfg_inverter_discharge_seplos.png){ width="350" }

#### BMS
##### Parameter
![](img/beispielconfig/beispielcfg_bms_seplos_parameter.png){ width="1050" }

##### Switches
![](img/beispielconfig/beispielcfg_bms_switches.png){ width="1050" }