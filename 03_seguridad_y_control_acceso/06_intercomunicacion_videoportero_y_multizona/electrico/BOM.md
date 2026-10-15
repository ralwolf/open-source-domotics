# Lista de Materiales y Componentes (BOM)
## Proyecto: Videoportero Inteligente ESP32-S3 y Control de Acceso VoIP / WebRTC
**Directorio:** `03_seguridad_y_control_acceso/06_intercomunicacion_videoportero_y_multizona/electrico/`  
**Diseño:** KiCad 10.0 | Código de Proyecto: `ESP32S3-DOORBELL-V1`

---

### 1. Circuitos Integrados y Módulos Principales
| Referencia | Componente | Encapsulado | Función / Especificación | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **U4** | ESP32-S3-WROOM-1-N16R8 | SMD Módulo | MCU Dual-Core 240MHz, 16MB Flash, 8MB Octal PSRAM | 1 |
| **U5** | INMP441 / ICS-43434 | SMD QFN-14 | Micrófono MEMS Digital I2S (SNR 65 dBA) | 1 |
| **U6** | MAX98357A | SMD WLP / TQFN | Amplificador de Audio Digital I2S Clase D Mono 3.2W | 1 |
| **U1** | Silvertel Ag9905M | Módulo SIL Through-Hole | Extractor PoE IEEE 802.3af (Entrada 48V -> Salida 5V 1.8A Aislada) | 1 |
| **U2** | AMS1117-3.3 | SOT-223 | Regulador lineal de bajo voltaje (5V -> 3.3V 800mA) | 1 |
| **U7** | NXP PN532 | QFN-40 / Breakout | Controlador NFC/RFID 13.56MHz con soporte Mifare/NFC Forum | 1 |
| **CAM1** | Módulo Sensor OV2640 / OV5640 | FPC 24 pines | Sensor CMOS HD con lente M12 gran angular 160° y filtro IR-CUT | 1 |

---

### 2. Driver de Cerradura Eléctrica y Potencia
| Referencia | Componente | Encapsulado | Función | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **OK1** | PC817 | DIP-4 / SMD | Optoacoplador para aislamiento de la señal de apertura | 1 |
| **Q1** | IRLZ44N / IRLML0030 | TO-220 / SOT-23 | MOSFET canal N Logic-Level para accionar cerradura 12V 2A | 1 |
| **D4** | SB560 / 1N5408 | DO-201AD | Diodo Schottky de protección contra picos inductivos (Flyback) | 1 |
| **K1** | Omron G5V-1 (Opcional) | DIP-6 | Relé miniatura de contacto seco (contacto libre de potencial) | 1 |

---

### 3. Componentes de Interfaz Humana y Acústica
| Referencia | Componente | Tipo | Especificación | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **SW1** | Pulsador Piezoeléctrico Antivandálico | Diámetro 19mm | Acero inoxidable 316, anillo LED iluminado, IP68 | 1 |
| **SPK1** | Altavoz Cónico de Mylar | Diámetro 40mm | Impedancia 4 Ω, Potencia 3 W, membrana impermeable IP65 | 1 |
| **IR1, IR2** | LEDs Infrarrojos de Potencia | SMD 3535 | Longitud de onda 850nm / 940nm con lente de 120° | 2 |
| **PIR1** | Sensor PIR miniatura / LD2410 | Cabezal 5-pin | Sensor de presencia radar 24 GHz para pre-activación de vídeo | 1 |

---

### 4. Conectores y Borneras
| Referencia | Conector | Pines | Uso | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **J1** | Conector RJ45 blindado con imanes | 8 pines | Entrada Ethernet 10/100 con soporte PoE pasivo/activo | 1 |
| **J2** | Conector JST-PH 2.0mm | 2 pines | Salida hacia altavoz frontal impermeable | 1 |
| **J3** | Conector FPC 0.5mm paso | 24 pines | Conexión directa al módulo de cámara HD | 1 |
| **J4** | Bornera Enchufable KF2EDG 5.08mm | 4 pines | Conexión externa de electrocerradura (12V DC, GND, Contacto) | 1 |
