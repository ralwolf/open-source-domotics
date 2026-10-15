# Lista de Materiales y Componentes (BOM)
## Proyecto: Controlador Autónomo de Corte de Emergencia de Gas y Agua
**Directorio:** `03_seguridad_y_control_acceso/03_actuadores_valvulas_gas_agua/electrico/`  
**Diseño:** KiCad 10.0 | Código de Proyecto: `ESP32-SHUTOFF-V1`

---

### 1. Circuitos Integrados y Módulos
| Referencia | Componente | Encapsulado | Función | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **U3** | ESP32-WROOM-32E | Módulo SMD | MCU Dual-Core 240MHz con WiFi + BLE para telemetría | 1 |
| **U1** | Módulo UPS 18650 12V | PCB Through-Hole | Cargador Li-Ion + Elevador Step-Up 12V continuo de respaldo | 1 |
| **U2** | AMS1117-3.3 | SOT-223 | Regulador lineal de bajo voltaje (12V/5V -> 3.3V 800mA) | 1 |
| **U4** | LM393 | DIP-8 / SOIC-8 | Comparador dual de voltaje para sondas resistivas de agua | 1 |
| **OK1, OK2** | PC817 | DIP-4 | Optoacopladores de aislamiento galvánico | 2 |

---

### 2. Etapa de Potencia y Disparo de Válvulas
| Referencia | Componente | Encapsulado | Descripción | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **Q1, Q2** | IRLZ44N | TO-220 | MOSFET canal N Logic-Level (55V 47A) para electroválvulas | 2 |
| **D2, D3** | 1N5408 | DO-201AD | Diodos de supresión de picos inductivos (Flyback 3A 1000V) | 2 |
| **BZ1** | Zumbador Piezoeléctrico | 12V DC | Sirena acústica continua de 85 dB a 1 metro | 1 |
| **F1** | Fusible Rearmable Polyswitch | PPTC 16V 3A | Protección contra sobrecorriente en actuadores | 1 |

---

### 3. Válvulas y Actuadores Vinculados
- **1x Electroválvula de Gas con Rearme Manual:** 12V DC, cuerpo de latón DN20 (3/4") o DN25 (1"), cierre por pulso en <1 segundo.
- **1x Válvula Motorizada de Agua:** 12V DC, cuerpo de latón DN25 (1"), cierre por condensador de retorno automático en <3 segundos.
- **3x Sensores de Inundación de Cable Conductivo:** 2 metros de cable sensor trenzado para zócalos de cocina, lavandería y colector de calefacción.
