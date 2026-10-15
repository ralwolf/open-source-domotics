# Lista de Materiales (BOM) - Controlador de Acceso para Cerraduras Biométricas

**Placa:** `controlador_acceso_cerraduras.kicad_sch`  
**Alimentación:** 12V DC (Batería de respaldo 12V 7Ah con cargador flotante)  
**Carga Máxima de Salida:** 12V DC / 3A (Soporta cerradura electromagnética o cerradura motorizada de perno)  
**Proyecto:** open-source-domotics  

---

### 1. Semiconductores y Circuitos Integrados
| Referencia | Componente | Encapsulado | Función / Descripción | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-WROOM-32E | SMD-38 | Microcontrolador central Wi-Fi/BLE con base de datos de huellas local | 1 |
| **U2** | MP1584EN | SOIC-8 | Convertidor reductor síncrono 12V a 3.3V 2A de alta eficiencia | 1 |
| **Q1** | IRLZ44N | TO-220 | MOSFET canal N Logic-Level (55V 47A) para disparo de cerradura | 1 |
| **D1** | 1N5408 | DO-201AD | Diodo rectificador 3A 1000V de supresión de picos flyback | 1 |
| **K1** | Omron G5LE-1 12VDC | THT | Relé SPDT 10A conmutador (Configuración Fail-Safe / Fail-Secure) | 1 |
| **OK1** | PC817 | DIP-4 | Optoacoplador para aislamiento de entrada de sensor de puerta y pulsador REX | 1 |
| **BZ1** | Zumbador 12V | THT | Buzzer piezoeléctrico continuo para aviso de apertura y alarma de sabotaje | 1 |

---

### 2. Dispositivos Periféricos Vinculados
- **1x Sensor de Huella Dactilar Capacitivo R503:** Resolución 508 DPI, sensor circular con anillo LED RGB bicolor, capacidad para 200 huellas, interfaz UART TTL.
- **1x Sensor Magnético de Puerta (Reed Switch):** Grado 2 de seguridad, contacto NC empotrado en marco de puerta para supervisión de puerta abierta.
- **1x Pulsador Interior de Salida (REX):** Tipo contacto seco capacitivo No-Touch (sensor infrarrojo de aproximación sin contacto físico).
- **1x Microswitch Tamper:** Contacto NC situado en el respaldo del panel para disparo de alarma si se intenta desprender de la pared.
