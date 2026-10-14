# Lista de Materiales y Componentes (BOM)
## Proyecto: Gateway ESP32 de Telemetría Energética y Control de Sobrecargas
**Directorio:** `04_telemetria_y_cargas_criticas/01_medicion_potencia_cuadro/electrico/`  
**Diseño:** KiCad 10.0 | Código de Proyecto: `ESP32-PWR-MON-V1`

---

### 1. Circuitos Integrados y Módulos Principales
| Referencia | Componente | Encapsulado / Módulo | Descripción / Función | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **U1** | AMS1117-3.3 | SOT-223 | Regulador lineal de bajo voltaje (LDO 5V -> 3.3V 800mA) | 1 |
| **U2** | ESP32-WROOM-32E | Módulo SMD 38-pin | MCU dual-core 240MHz, 4MB Flash, WiFi + BLE | 1 |
| **U3** | SP3485 / MAX485 | SOIC-8 / DIP-8 | Transceptor semidúplex RS-485 para Modbus RTU | 1 |
| **PSU1** | Hi-Link HLK-PM01 | Módulo PCB Through-Hole | Conversor AC/DC 100-240VAC a 5VDC 3W aislado | 1 |
| **DISP1** | SSD1306 | Cabezal 4-pin I2C | Pantalla OLED 0.96" 128x64 para lectura local directa | 1 |

---

### 2. Etapa de Relés y Aislamiento de Control
| Referencia | Componente | Encapsulado | Descripción | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **K1, K2** | Omron G5LE-1-5VDC | THT 5 pines | Relé electromecánico SPDT 5VDC bobina, 10A 250VAC contactos | 2 |
| **Q1, Q2** | 2N2222 / MMBT2222 | SOT-23 / TO-92 | Transistor bipolar NPN driver de bobina de relé | 2 |
| **OK1, OK2** | PC817 | DIP-4 / SOP-4 | Optoacoplador para aislamiento galvánico de señales de disparo | 2 |
| **D1, D2** | 1N4148 / 1N4007 | DO-35 / SMA | Diodo flyback antiparalelo de protección de bobina | 2 |

---

### 3. Protecciones y Filtrado
| Referencia | Componente | Especificación | Cantidad |
| :--- | :--- | :--- | :--- |
| **F1** | Fusible Cartucho 5x20mm | 1A / 250V Acción Lenta (T1A) con zócalo para carril | 1 |
| **MOV1** | Varistor de Óxido Metálico | 10D431K (275VAC / 350VDC, absorción 45J) | 1 |
| **TVS1, TVS2** | Diodos TVS Bidireccionales | SMBJ6.8CA en líneas A y B de RS-485 | 2 |
| **C1** | Condensador Electrolítico | 470 µF / 16V Low-ESR (filtro salida 5V) | 1 |
| **C2, C4, C5** | Condensador Cerámico Multicapa | 100 nF / 50V X7R (desacoplo de ICs) | 3 |
| **C3** | Condensador Tantalio / Electrolítico | 220 µF / 10V (filtro carril 3.3V ESP32) | 1 |

---

### 4. Conectores y Borneras de Tablero
| Referencia | Conector | Pines | Uso | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **J1** | Bornera Enchufable KF2EDG 5.08mm | 2 pines | Entrada de Alimentación AC 230V (Fase, Neutro) | 1 |
| **J2** | Bornera Enchufable KF2EDG 5.08mm | 6 pines | Salidas de Relés K1 y K2 (COM, NO, NC) para contactores | 1 |
| **J3** | Bornera Enchufable KF2EDG 3.81mm | 3 pines | Bus RS-485 Modbus (A+, B-, GND Pantalla) | 1 |
| **J4, J5, J6, J7** | Cabezal JST-XH 2.54mm | 4 pines | Conexión directa a módulos de corriente PZEM-004T v3 | 4 |
| **J8** | Cabezal Pin Header 2.54mm | 4 pines | Puerto de Programación y Debug (3V3, RX, TX, GND) | 1 |

---

### 5. Sensores Externos Vinculados (En Carril DIN)
- **1x Analizador de Redes Trifásico/Bifásico:** Eastron SDM630 Modbus V2 (en acometida principal).
- **4x Sensores Monofásicos:** PZEM-004T v3 con transformadores de núcleo abierto 100A / 50mA para sub-medición de circuitos críticos y prioritarios.
