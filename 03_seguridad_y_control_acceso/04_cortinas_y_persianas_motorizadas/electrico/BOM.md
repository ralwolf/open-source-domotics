# Lista de Materiales (BOM) - Controlador Persianas con Interbloqueo Hardware

| Ref | Cantidad | Descripción | Encapsulado | Función Técnica | Proveedor / P/N | Coste Est. (EUR) |
|---|---|---|---|---|---|---|
| PS1 | 1 | Fuente AC/DC Conmutada 230VAC a 5VDC 3W HLK-PM01 | Módulo THT | Alimentación directa desde la red eléctrica | Hi-Link HLK-PM01 | 2.50 |
| U1 | 1 | Regulador Lineal LDO 3.3V 800mA AMS1117-3.3 | SOT-223 | Regulación 5V a 3.3V para ESP32 | Advanced Monolithic Systems | 0.35 |
| U2 | 1 | Microcontrolador SoC ESP32-WROOM-32E 8MB | SMD Module | Lógica de posición porcentual, ESPHome, Wi-Fi | Espressif ESP32-WROOM-32E | 3.50 |
| K1 | 1 | Relé de Potencia 10A 250VAC SPST Bobina 5V | THT | Corte y encendido general de energía motor | Omron G5Q-1 5VDC | 1.80 |
| K2 | 1 | Relé de Potencia 10A 250VAC SPDT Conmutado | THT | Conmutador de fase Subir / Bajar (Interlock) | Omron G5Q-1 5VDC | 1.80 |
| U3 | 1 | Sensor de Corriente Efecto Hall Aislado ACS712-05B | SOIC-8 | Detección de sobreesfuerzo y anti-atrapamiento | Allegro MicroSystems ACS712ELCTR-05B | 2.20 |
| U4-U5 | 2 | Optoacoplador Fototransistor Aislamiento 5kV PC817 | DIP-4 | Lectura de pulsadores mecánicos de pared 230V | Sharp PC817 | 0.60 |
| R_SNUB | 2 | Resistencia de Potencia 47Ω 2W Antiflama | THT Axial | Red amortiguadora RC snubber de contactos relé | Yageo FKN2WS | 0.50 |
| C_SNUB | 2 | Condensador Polipropileno X2 47nF 275VAC | THT Radial | Supresión de arco voltaico en desconexión motor | KEMET R46 | 0.80 |
| J1 | 1 | Bornero Tornillo 4P 5.08mm 16A | THT | Conexión cable motor (L_UP, L_DOWN, N, PE) | Phoenix Contact 1729144 | 1.40 |
| J2 | 1 | Bornero Tornillo 3P 5.08mm | THT | Conexión pulsador doble de pared (Subir/Bajar) | Phoenix Contact 1729131 | 1.10 |
| PCB | 1 | Placa de Circuito Impreso Doble Cara 2oz Cu | FR4 70x60mm | Pistas con aislamiento de 2.5 mm de fuga | JLCPCB / PCBWay | 2.00 |
| **TOTAL** | | | | | | **18.55 EUR** |
