# Lista de Materiales (BOM) - Controlador de Riego Multizona 24VAC

**Placa:** `controlador_riego_jardin.kicad_sch`  
**Canales de Salida:** 5 (4 Zonas de Riego + 1 Válvula Maestra de Seguridad)  
**Tensión de Operación:** 24V AC (Transformador 230V -> 24V AC 50VA)  
**Proyecto:** open-source-domotics  

---

### 1. Circuitos Integrados y Módulos
| Referencia | Componente | Encapsulado | Función / Descripción | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-WROOM-32E | SMD-38 | Microcontrolador central Wi-Fi/BLE dual-core con ESPHome | 1 |
| **U2** | LM2596HV-5.0 | TO-263-5 | Regulador Step-Down conmutado de alta tensión (60V -> 5V 1A) | 1 |
| **U3** | AMS1117-3.3 | SOT-223 | Regulador lineal 3.3V 1A para ESP32 y sensores analógicos | 1 |
| **OK1 a OK5** | MOC3041M | DIP-6 | Optoacopladores disparadores de triac con detección de Cruce por Cero (Zero-Cross) | 5 |
| **BR1** | MB6S | SOIC-4 | Puente rectificador de onda completa 600V 1A para alimentación interna | 1 |

---

### 2. Dispositivos de Potencia y Protección
| Referencia | Componente | Encapsulado | Función / Descripción | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **Q1 a Q5** | BT136-600E | TO-220 | Triacs de compuerta sensible 4A 600V para electroválvulas solenoides 24VAC | 5 |
| **MOV1 a MOV5** | S10K275 | Radial 10mm | Varistores de óxido metálico 275V AC para absorción de picos transitorios inductivos | 5 |
| **R_snub (1-5)** | Resistencia Cerámica 39 Ω / 1W | Axial | Red amortiguadora snubber RC contra dV/dt espurio | 5 |
| **C_snub (1-5)** | Condensador Poliéster 10 nF / 400V | Paso 10mm | Red amortiguadora snubber RC | 5 |
| **F1** | Fusible Cerámico 2A 250V (5x20mm) | Portafusible PCB | Protección contra cortocircuito en bobinas de solenoides | 1 |

---

### 3. Conectores y Sensores
| Referencia | Componente | Tipo / Paso | Conexión | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **J1** | Bornero de tornillo 8 pines | Paso 5.08 mm | 24VAC In, Común, Válvula Maestra, Zonas 1 a 4, Tierra PE | 1 |
| **J2** | Bornero de tornillo 6 pines | Paso 3.81 mm | Entradas analógicas sondas S1-S4, entrada de pulsos caudalímetro, 3.3V | 1 |
| **S1 a S4** | Sondas Capacitivas de Suelo v2.0 | Sensor analógico | Inmunes a corrosión galvánica, cable apantallado hacia arquetas/macetas | 4 |
| **FL1** | Caudalímetro de Turbina Hall | 1" BSP Macho | Salida de impulsos NPN colector abierto (1 pulso / litro) | 1 |
