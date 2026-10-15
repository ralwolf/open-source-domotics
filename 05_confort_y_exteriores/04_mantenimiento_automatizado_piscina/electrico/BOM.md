# Lista de Materiales (BOM) - Controlador Químico y Filtración Piscina

| Ref | Cantidad | Descripción | Encapsulado | Función Técnica | Proveedor / P/N | Coste Est. (EUR) |
|---|---|---|---|---|---|---|
| U1 | 1 | Regulador Buck Step-Down MP1584 | Módulo SMD | 24V a 5V/3.3V para ESP32 y periféricos | Monolithic Power MP1584EN | 1.80 |
| U2 | 1 | Convertidor DC-DC Aislado B0505S-1WR3 | SIP-4 | Aislamiento galvánico 1kV para sondas pH/ORP | Mornsun B0505S-1WR3 | 3.20 |
| U3 | 1 | Microcontrolador ESP32-WROOM-32E 8MB | SMD Module | Lógica de filtración, PID químico, ESPHome | Espressif ESP32-WROOM-32E | 3.50 |
| U4-U5 | 2 | Amp Op Ultra-Baja Corriente Polarización LMC6001 | SOIC-8 | Amplificador de electroteca para electrodos pH/ORP ($I_b < 25	ext{ fA}$) | Texas Instruments LMC6001AIN | 5.80 |
| U6 | 1 | Convertidor ADC 16-Bit I2C Aislado ADS1115 | MSOP-10 | Muestreo de alta resolución para lecturas mV | Texas Instruments ADS1115IDGST | 3.10 |
| J1-J2 | 2 | Conector BNC Hembra 50Ω Montaje PCB Chasis | BNC THT | Conexión blindada para electrodos de vidrio | Amphenol B6252HB | 3.60 |
| Q1-Q2 | 2 | MOSFET Canal N AOD4184A (40V, 50A, 8.5mΩ) | TO-252 | Driver PWM bombas peristálticas 24V 1.5A | Alpha & Omega AOD4184A | 1.40 |
| D1-D2 | 2 | Diodo Flyback Ultrarrápido 1N5408 | DO-201AD | Protección contra fuerza contraelectromotriz motor | Vishay 1N5408 | 0.60 |
| K1 | 1 | Relé de Potencia 16A 250VAC Bobina 12V/24V | THT | Maniobra contactor bobina bomba 1 CV 230V | Omron G5Q-1 24VDC | 2.20 |
| J3-J6 | 4 | Bornero Tornillo 2P 5.08mm 15A | THT | Conexión peristálticas, contactor y flow switch | Phoenix Contact 1729128 | 3.20 |
| J7 | 1 | Bornero Tornillo 3P 5.08mm | THT | Conexión sonda temperatura digital DS18B20 | Phoenix Contact 1729131 | 1.10 |
| R1-R6 | 6 | Resistencias SMD 0805 1% (10k, 4.7k, 1k) | SMD 0805 | Pull-ups 1-Wire e I2C y filtros pasivos | Yageo RC0805FR | 0.30 |
| C1-C8 | 8 | Condensadores Cerámicos 100nF y 10µF X7R | SMD 0805 | Desacoplo de ruido analógico y alimentación | Murata GRM21 | 0.80 |
| PCB | 1 | Placa de Circuito Impreso Doble Cara 2oz Cu | FR4 100x80mm | Plano de masa analógica aislada | JLCPCB / PCBWay | 2.50 |
| **TOTAL** | | | | | | **33.10 EUR** |
