# Control de Acceso Biométrico por Huella Dactilar y Cerradura Electrónica

Este subsistema implementa un nodo de control de acceso autónomo de alta seguridad para puertas exteriores y accesos restringidos. Su arquitectura garantiza funcionamiento ininterrumpido 24/7 incluso ante cortes totales de energía de red o caída de la conectividad LAN/Wi-Fi, almacenando la base de datos biométrica y las reglas de validación en la memoria flash no volátil local.

---

## 1. Arquitectura del Sistema

```
+---------------------------------------------------------------------------------+
|                       PANEL EXTERIOR (Antivandálico IP65)                       |
|  +------------------------+  +--------------------+  +-----------------------+  |
|  | Sensor Huella R503     |  | Tamper Óptico/Mec  |  | Timbre / Pulsador     |  |
|  | Anillo LED RGB 360°    |  | Microswitch NA     |  | Retroiluminado 12V    |  |
|  +-----------+------------+  +---------+----------+  +-----------+-----------+  |
+--------------|-------------------------|-------------------------|--------------+
               | UART (57600 baud)       | GPIO33                  | GPIO32
+--------------v-------------------------v-------------------------v--------------+
|                     CONTROLADOR AUTÓNOMO (Lado Seguro Interior)                  |
|  ESP32-WROOM-32E (Criptografía local + WDT 15s + Almacenamiento Flash NVS)      |
|                                                                                 |
|  +--------------------------------+       +----------------------------------+  |
|  | Driver MOSFET AOD4184A + Flyback| ----> | Cerradura Fail-Secure 12V 2.5A   |  |
|  | Diodo 1N5408 + Snubber RC      |       | (Pestillo motorizado / cerradura)|  |
|  +--------------------------------+       +----------------------------------+  |
|  +--------------------------------+       +----------------------------------+  |
|  | Sensor Magnético Puerta (Reed) | <---- | Contacto NA/NC en marco/hoja     |  |
|  +--------------------------------+       +----------------------------------+  |
|  +--------------------------------+       +----------------------------------+  |
|  | UPS 12V Plomo-Gel / LiFePO4    | ----> | Monitor ADC Divisor Resistivo    |  |
|  +--------------------------------+       +----------------------------------+  |
+---------------------------------------+-----------------------------------------+
                                        | Wi-Fi WPA3 Enterprise / VLAN 30 IoT (Sin WAN)
                                        v
                       +---------------------------------+
                       | Home Assistant (Eventos/Auditor)|
                       +---------------------------------+
```

---

## 2. Entregables y Modelos del Subsistema

### 2.1 Diseño Mecánico 3D (`mecanico/`)
- **Modelo CAD FreeCAD 1.1+**: [panel_acceso_biometrico.FCStd](mecanico/panel_acceso_biometrico.FCStd)
- **Modelo de Intercambio STEP**: [panel_acceso_biometrico.step](mecanico/panel_acceso_biometrico.step)
- **Script Generador Paramétrico**: [generar_cerradura_biometrica_3d.py](../../scripts/generar_cerradura_biometrica_3d.py)
- **Especificaciones**:
  - Mecanizado en bloque de aluminio anodizado 6061-T6 ($160 \times 80 \times 32\text{ mm}$, espesor de pared $4.0\text{ mm}$).
  - Alojamiento frontal estanco para sensor capacitivo circular R503 ($\varnothing 25\text{ mm}$).
  - Ranura para junta tórica de estanqueidad de silicona (perfil tórico $2.0\text{ mm}$, grado IP65).
  - Vaina para pasamuros roscado M16 posterior con sellador ignífugo.
  - Soporte para microswitch antimanipulación (tamper) que se activa al separar el chasis de la pared.

### 2.2 Diseño Eléctrico y Esquemático KiCad 10 (`electrico/`)
- **Proyecto KiCad 10**: [controlador_acceso_cerraduras.kicad_pro](electrico/controlador_acceso_cerraduras.kicad_pro)
- **Esquema Electrónico**: [controlador_acceso_cerraduras.kicad_sch](electrico/controlador_acceso_cerraduras.kicad_sch)
- **Vectorial SVG**: [controlador_acceso_cerraduras.svg](electrico/esquema_svg/controlador_acceso_cerraduras.svg)
- **Lista de Materiales y Costes (BOM)**: [BOM.md](electrico/BOM.md)
- **Script Generador KiCad**: [generar_kicad_cerraduras.py](../../scripts/generar_kicad_cerraduras.py)
- **Características Eléctricas**:
  - Regulador reductor síncrono DC-DC MP1584 (12V a 3.3V, eficiencia $>91\%$).
  - Aislamiento galvánico por optoacoplador para la señal de disparo del pestillo.
  - Driver de potencia MOSFET canal N AOD4184A ($40\text{V}$, $50\text{A}$, $R_{DS(on)} < 8.5\text{ m}\Omega$).
  - Diodo flyback ultrarrápido 1N5408 en antiparalelo contra transitorios inductivos de solenoide ($L \cdot di/dt$).
  - Resistencia de pull-down activa en el gate del MOSFET para evitar aperturas espurias durante arranques.

### 2.3 Firmware y Automatización ESPHome (`control/`)
- **Firmware ESPHome**: [control_acceso_biometrico.yaml](control/control_acceso_biometrico.yaml)
- **Capacidades Autónomas**:
  - Capacidad para 200 plantillas dactilares almacenadas en chip biométrico R503.
  - Matching dactilar ultrarrápido local ($< 300\text{ ms}$) independiente del estado del servidor.
  - Notificaciones en tiempo real a Home Assistant mediante eventos cifrados (`api.encryption`).
  - Servicios remotos de Home Assistant para enrolar y revocar huellas desde la interfaz gráfica.
  - Retroalimentación audiovisual: Anillo LED RGB (Verde = Autorizado, Rojo = Denegado/Sabotaje, Púrpura = Modo enrolamiento) y zumbador piezoeléctrico de $2.7\text{ kHz}$.
  - Alarma inmediata por sabotaje mecánico (apertura del panel exterior).
