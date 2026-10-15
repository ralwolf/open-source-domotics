# Lista de Materiales (BOM) - Central de Incendio, CO y Extinción por Aerosol

| Ref | Cantidad | Descripción | Encapsulado | Función Técnica | Proveedor / P/N | Coste Est. (EUR) |
|---|---|---|---|---|---|---|
| U1 | 1 | Regulador Buck Step-Down MP1584 | Módulo SMD | 24V a 3.3V / 1.5A para ESP32 | Monolithic Power MP1584EN | 1.80 |
| U2 | 1 | Microcontrolador ESP32-WROOM-32E 8MB | SMD Module | Lógica de lazo EN54, coincidencia cruzada, ESPHome | Espressif ESP32-WROOM-32E | 3.50 |
| C1 | 1 | Condensador Electrolítico Baja ESR 4700µF 35V | Radial D16mm | Almacenamiento de energía para disparo autónomo | Nichicon UHW1V472MHD | 2.20 |
| Q1 | 1 | P-MOSFET Potencia 40V 40A AOD403 | TO-252 | Conmutador High-Side de disparo seguro | Alpha & Omega AOD403 | 1.20 |
| Q2 | 1 | N-MOSFET Potencia 40V 50A AOD4184A | TO-252 | Conmutador Low-Side de disparo seguro | Alpha & Omega AOD4184A | 0.80 |
| R_SENSE | 1 | Resistencia Shunt Medición 10Ω 1% 1W | SMD 1206 | Supervisión de corriente en reposo iniciador (<5mA) | Vishay WSL1206 | 0.60 |
| R_EOL | 2 | Resistencia Fin de Línea 4.7kΩ 1% 0.5W | THT Axial | Terminación lazo supervisado detectores EN54 | Yageo MFR-50FTE52-4K7 | 0.20 |
| U3 | 1 | Sensor Electroquímico de CO Figaro TGS5042 | Módulo TO-5 | Medición precisa de CO (0 - 1000 ppm) vida útil 10 años | Figaro Engineering TGS5042 | 14.50 |
| K1 | 1 | Relé de Maniobra SPDT 10A 250VAC | THT | Enclavamiento de corte para gas y climatización VMC | Omron G5Q-1 24VDC | 1.80 |
| K2 | 1 | Relé de Potencia SPST 10A 24VDC | THT | Activación de sirena 110dB y estrobo exterior | Omron G5Q-1 24VDC | 1.80 |
| J1-J3 | 3 | Bornero de Tornillo 2P 5.08mm 16A | THT | Conexión iniciador aerosol, lazo humo y aborto | Phoenix Contact 1729128 | 2.40 |
| D1-D4 | 4 | Diodos TVS Bidireccionales SMBJ28CA | SMB | Protección de descargas en líneas perimetrales | Littelfuse SMBJ28CA | 1.20 |
| PCB | 1 | Placa de Circuito Impreso Doble Cara 2oz Cu | FR4 100x80mm | Pistas de potencia reforzadas para pulso de disparo | JLCPCB / PCBWay | 2.50 |
| **TOTAL** | | | | | | **34.50 EUR** |
