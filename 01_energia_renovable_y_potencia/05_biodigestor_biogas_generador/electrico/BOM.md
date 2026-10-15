# Lista de Materiales (BOM) - Controlador de Biogás y Generador Dual (ATS)

**Placa:** `controlador_biogas_generador.kicad_sch`  
**Potencia Generador Soportada:** 5 kW (Motor 4T 389cc gasolina/biogás)  
**Tensión de Operación:** 12V DC (Batería de arranque del grupo con cargador flotante)  
**Proyecto:** open-source-domotics  

---

### 1. Circuitos Integrados y Módulos
| Referencia | Componente | Encapsulado | Función / Descripción | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-WROOM-32E | SMD-38 | Microcontrolador central Wi-Fi/BLE con ESPHome | 1 |
| **U2** | AMS1117-3.3 | SOT-223 | Regulador lineal 3.3V 1A para ESP32 | 1 |
| **S1** | MQ-4 | Módulo Sensor | Sensor catalítico/semiconductor de gas Metano (CH4) | 1 |
| **T1** | ZMPT101B | Módulo PCB | Transformador de tensión de precisión para verificación 230VAC generador | 1 |
| **K1 a K4** | Omron G5LE-1 12VDC | THT | Relés SPDT 10A (Ignición, Arranque motor, Choke y Válvula ATEX) | 4 |
| **Q1 a Q4** | 2N7002 / IRLML2502 | SOT-23 | Transistores MOSFET canal N para excitación de bobinas de relé | 4 |
| **D1 a D4** | 1N4007 | DO-41 | Diodos de rueda libre flyback de supresión inductiva | 4 |

---

### 2. Equipamiento de Campo e Instalación de Biogás
- **1x Transmisor de Presión Piezorresistivo:** 0 a 50 mbar con salida analógica 4-20mA / 0.5-4.5V y conexión 1/4" NPT inox.
- **1x Electroválvula de Biogás Certificada ATEX (Zona 1/2):** 12V DC normalmente cerrada (NC), cuerpo de latón/aluminio DN20 (3/4").
- **1x Arrestador de Llama (Parallamas):** Malla de acero inoxidable AISI 316 certificada EN ISO 16852.
- **1x Actuador Lineal 12V para Choke:** Solenoide/servomotor para cierre y apertura gradual del cebador de aire en arranque frío.
- **1x Conmutador ATS (Automatic Transfer Switch):** 63A 2P conmutación mecánica motorizada con interbloqueo eléctrico.
