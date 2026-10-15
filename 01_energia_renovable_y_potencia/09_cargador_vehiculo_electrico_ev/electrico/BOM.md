# Lista de Materiales (BOM) - Controlador EV Wallbox 32A

**Placa:** `controlador_ev_wallbox.kicad_sch`  
**Norma de Carga:** IEC 61851-1 / SAE J1772 Modo 3 Caso B/C  
**Potencia Soportada:** 7.4 kW (Monofásico 32A) / 22 kW (Trifásico 32A)  
**Proyecto:** open-source-domotics  

---

### 1. Circuitos Integrados y Módulos Principales
| Referencia | Componente | Encapsulado | Función / Descripción | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-WROOM-32E | SMD-38 | Microcontrolador central Wi-Fi/BLE dual-core, máquina de estados IEC 61851 | 1 |
| **U2** | AMS1117-3.3 | SOT-223 | Regulador lineal de baja caída 3.3V 1A para MCU y lógica | 1 |
| **U3** | MCP6002-I/P | SOIC-8 | Amplificador operacional doble Rail-to-Rail para driver PWM ±12V CP | 1 |
| **U4** | L9110S | SOP-8 | Driver puente H de corriente continua (12V 1.5A) para solenoide de bloqueo | 1 |
| **U5** | ISO3082DW | SOIC-16W | Transceptor RS-485 aislado galvánicamente 2.5 kV para Medidor Modbus RTU | 1 |
| **PS1** | HLK-PM12 | Módulo PCB | Fuente ACDC conmutada 230VAC a 12VDC 3W clase II | 1 |
| **DC1** | B1212S-1WR3 | SIP-4 | Convertidor DC-DC aislado 12V a -12V 1W para nivel negativo del CP (-12V) | 1 |

---

### 2. Elementos de Conmutación y Protecciones
| Referencia | Componente | Encapsulado | Función / Descripción | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **K1** | Omron G5LE-1 12VDC | THT | Relé SPDT 10A 250VAC para excitación de bobina de contactor principal 40A | 1 |
| **OK1, OK2** | PC817 | DIP-4 | Optoacopladores para feedback de contacto auxiliar y trigger RCMB 6mA DC | 2 |
| **D1, D2** | 1N4148 / 1N4007 | SOD-123 / DO-41 | Diodo flyback de protección de bobinas y rectificación en lazo CP | 2 |
| **ZD1** | BZX84C3V3 | SOT-23 | Diodo Zener 3.3V de protección de entrada ADC frente a sobretensiones | 1 |
| **F1** | PPTC 16V 1.5A | SMD 1812 | Fusible rearmable de protección línea de 12V y solenoide | 1 |

---

### 3. Equipamiento Eléctrico de Potencia en Carril DIN
- **1x Contactor Bipolar 40A AC-1 (230VAC Bobina):** Schneider Acti9 iCT / Finder 22.32 con contacto auxiliar 1NO para supervisión de soldadura de contactos.
- **1x Disyuntor Magnetotérmico 2P C40A (10kA):** Protección exclusiva de sobrecorriente.
- **1x Interruptor Diferencial Tipo B / RDC-DD (IEC 62955):** Sensibilidad 30mA AC y disparo instantáneo a 6mA DC continuos lisos.
- **1x Medidor de Energía Modbus RS-485:** Eastron SDM120 / Finder 7M.24 (bidireccional, MID).
- **1x Base Receptáculo Tipo 2 (IEC 62196-2):** Hembra con pestillo motorizado 12V.
- **1x Seta de Parada de Emergencia:** Contacto NC cableado en serie directo a la bobina del contactor (seguridad intrínseca por hardware).
