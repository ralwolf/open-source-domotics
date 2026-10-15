# Lista de Materiales (BOM) - Contador IoT de Rayos y Telemetría DPS

**Placa:** `contador_rayos_iot.kicad_sch`  
**Función:** Detección y conteo de descargas atmosféricas (>500A) y supervisión de protectores de sobretensión transitoria  
**Alimentación:** Micro-panel solar 5V + Batería Li-Ion 18650 (Autonomía continua en exteriores)  
**Proyecto:** open-source-domotics  

---

### 1. Semiconductores y Circuitos Integrados
| Referencia | Componente | Encapsulado | Función / Descripción | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-WROOM-32E | SMD-38 | Microcontrolador central Wi-Fi/BLE con contador de pulsos por hardware (PCNT) | 1 |
| **U2** | TP4056 | SOIC-8 | Controlador de carga de batería Li-Ion 1A con protección térmica | 1 |
| **U3** | AMS1117-3.3 | SOT-223 | Regulador lineal LDO 3.3V 1A de bajo ruido | 1 |
| **U4** | LM393 | SOIC-8 | Comparador de tensión analógico de alta velocidad para detección de picos de rayo | 1 |
| **OK1, OK2** | PC817 | DIP-4 | Optoacopladores para lectura aislada de contactos auxiliares de cartuchos DPS | 2 |
| **TVS1** | SMAJ36A | SMA | Diodo supresor de transitorios TVS para protección de entrada de bobina captadora | 1 |
| **D1, D2** | BAT54S | SOT-23 | Diodos Schottky duales para rectificación ultrarrápida del pulso inducido | 1 |

---

### 2. Componentes de Protección Atmosférica en Campo
- **1x Bobina Rogowski / Captador Toroidal:** Bobina toroidal de núcleo de aire o ferrita para abrazo de conductor Cu 50 mm² sin interrumpir la bajante.
- **1x Descargador Combinado Tipo 1+2 (TGBT):** Dehn DG M TNC 275 / Schneider iPRD1 12.5r con contacto auxiliar inversor de disparo.
- **1x Vía de Chispas Equipotencial (Spark Gap):** Dehn TFS / OBO Bettermann 100 kA (10/350 µs) para unión de malla pararrayos con tierra de servicio.
- **3x Picas de Acero Cobrizado:** $\phi 16	ext{ mm} 	imes 2.0	ext{ m}$ con abrazaderas de bronce y arqueta de registro de $30 	imes 30	ext{ cm}$.
