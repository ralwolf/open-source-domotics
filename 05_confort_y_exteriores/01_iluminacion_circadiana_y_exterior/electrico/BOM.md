# Lista de Materiales (BOM) - Controlador Dimmer Circadiano 4x 24V

| Ref | Cantidad | Descripción | Encapsulado | Función Técnica | Proveedor / P/N | Coste Est. (EUR) |
|---|---|---|---|---|---|---|
| U1 | 1 | Regulador Buck Step-Down MP1584 | Módulo SMD | 24V a 3.3V / 1.5A para lógica ESP32 | Monolithic Power MP1584EN | 1.80 |
| U2 | 1 | Microcontrolador ESP32-WROOM-32E 8MB | SMD Module | Lógica de control solar, ESPHome, Wi-Fi | Espressif ESP32-WROOM-32E | 3.50 |
| U3 | 2 | Driver de Puerta Dual MOSFET TC4427 | SOIC-8 | Conmutación ultrarrápida 20 kHz sin ringing | Microchip TC4427EOA | 2.20 |
| Q1-Q4 | 4 | MOSFET Canal N AOD4184A (40V, 50A, 8.5mΩ) | TO-252 (DPAK) | Conmutación PWM canales LED WW/CW/Ext | Alpha & Omega AOD4184A | 2.80 |
| D1-D4 | 4 | Diodo Schottky SS34 (40V, 3A) | SMC | Diodo de marcha libre contra inductancia de cable | Vishay SS34 | 0.80 |
| TVS1-4| 4 | Supresor TVS SMBJ28A | SMB | Protección contra transitorios y descargas | Littelfuse SMBJ28A | 1.20 |
| U4 | 1 | Sensor Digital de Luz Ambiental BH1750 | SOIC-8 / Módulo | Medición de lux ambiental (1 - 65535 lx) | ROHM BH1750FVI | 1.50 |
| U5 | 1 | Sensor Radar Micro-ondas mmWave 24 GHz | Módulo 5-pin | Detección de presencia estática micrométrica | Hi-Link HLK-LD2410B | 4.50 |
| U6 | 1 | Transceptor RS-485 Auto-Dirección MAX13487 | SOIC-8 | Interfaz DMX512 / Modbus RTU cableada | Analog Devices MAX13487EESA | 2.40 |
| J1-J4 | 4 | Bloque de Terminales Tornillo 2P 5.08mm 15A | THT | Salidas de potencia a tiras LED 24V | Phoenix Contact 1729128 | 3.20 |
| J5 | 1 | Bloque de Terminales Tornillo 2P 5.08mm 20A | THT | Entrada alimentación 24VDC desde fuente | Phoenix Contact 1729128 | 1.00 |
| C1-C6 | 6 | Condensador Cerámico 10µF 50V X7R | SMD 1206 | Filtrado desacoplo de rizado PWM 20kHz | Murata GRM31CR71H106KA12L | 1.10 |
| R1-R8 | 8 | Resistencias 10Ω (Gate) + 10kΩ (Pull-down) | SMD 0805 | Control de gate y estado seguro apagado | Yageo RC0805FR | 0.40 |
| PCB | 1 | Placa de Circuito Impreso 2 Caras 2oz Cu | FR4 100x80mm | Conducción pistas alta corriente 10A | JLCPCB / PCBWay | 2.50 |
| **TOTAL** | | | | | | **28.40 EUR** |
