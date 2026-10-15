# Infraestructura Eléctrica, Filtrado EMI y Monitorización de Oficina Técnica

Este subsistema comprende la infraestructura eléctrica de precisión, calidad de suministro y automatización para el puesto de trabajo técnico de la vivienda (10x10 m), con PDU de escritorio filtrada contra ruidos EMI/RFI, respaldo senoidal ininterrumpido (UPS 1000VA), eliminación de consumos vampiro y señalización luminosa exterior "ON AIR".

---

## 1. Alcance y Especificaciones Técnicas

### 1.1 Filtrado de Ruido Eléctrico EMI/RFI para Equipos de Audio y Medición
- **Atenuación de Interferencias de Red:**
  - Filtro LC pasivo de doble etapa integrado en la PDU con bobina de choque toroidal de modo común ($2 \times 4.7\text{ mH}$, $10\text{ A}$) y condensadores de seguridad grado X2 ($0.47\ \mu\text{F}$) e Y2 ($4.7\text{ nF}$ con derivación limpia a tierra BEP).
  - Atenuación superior a $45\text{ dB}$ en el rango de frecuencias críticas ($150\text{ kHz} - 30\text{ MHz}$), eliminando zumbidos de 50 Hz (*ground hum*) y ruidos de fuentes conmutadas en interfaces de audio USB, preamplificadores de micrófonos capacitivos de estudio y monitores de audio activos.

### 1.2 Respaldo de Energía Ininterrumpida (UPS Senoidal)
- Sistema UPS interactivo con salida de **onda senoidal pura** de 1000VA / 700W para la estación de trabajo (PC Workstation), evitando la distorsión armónica en fuentes con PFC activo y garantizando un tiempo de autonomía de 20 minutos ante cortes de suministro.

### 1.3 Automatización Maestro-Esclavo (Cero Consumos Vampiro)
- **Monitoreo de Potencia en Toma Maestra:**
  - El chip de metrología BL0942 lee en tiempo real el consumo del PC:
    - **Encendido de PC ($P > 45\text{ W}$):** Activa inmediatamente el relé de potencia de las tomas esclavas, encendiendo monitores 4K, monitores de estudio e iluminación de escritorio.
    - **Apagado o Suspensión ($P < 18\text{ W}$ durante 30 s):** Desconecta físicamente las tomas esclavas mediante relé, ahorrando anualmente más de $180\text{ kWh}$ en consumos fantasma (*vampire loads*).

### 1.4 Señalización Exterior "ON AIR / EN LLAMADA"
- Letrero luminoso LED rojo de alta visibilidad instalado en el dintel exterior de la puerta de la oficina.
- Activación automática mediante eventos MQTT sincronizados con el estado de la cámara web o micrófono en el sistema operativo, o conmutación manual desde Home Assistant para garantizar privacidad en grabaciones y videoconferencias.

---

## 2. Entregables Técnicos Generados

| Componente | Tipo de Archivo | Enlaces | Descripción Técnica |
| :--- | :--- | :--- | :--- |
| **PDU de Escritorio y Mordaza** | Modelo 3D CAD | [pdu_escritorio_oficina_con_senalizador.FCStd](mecanico/pdu_escritorio_oficina_con_senalizador.FCStd)<br>[pdu_escritorio_oficina_con_senalizador.step](mecanico/pdu_escritorio_oficina_con_senalizador.step) | Ensamble 3D FreeCAD de la PDU de aluminio extruido ($240\times70\times45\text{ mm}$), mordaza de sujeción al tablero, tomas Schuko y difusor ON-AIR. |
| **Plano Eléctrico de Oficina** | Plano 2D CAD | [plano_oficina_electrico_telemetria.svg](mecanico/plano_oficina_electrico_telemetria.svg)<br>[plano_oficina_electrico_telemetria.dxf](mecanico/plano_oficina_electrico_telemetria.dxf) | Distribución 2D de puesto de trabajo técnico, esquema unifilar de UPS senoidal 1000VA, filtro LC y lógica de tomas maestro-esclavo. |
| **Placa PCB Control PDU** | Esquema KiCad 10 | [controlador_pdu_oficina.kicad_sch](electrico/controlador_pdu_oficina.kicad_sch)<br>[controlador_pdu_oficina.svg](electrico/esquema_svg/controlador_pdu_oficina.svg) | Hardware KiCad 10 con ESP32-C3, metrología BL0942, filtro de red EMI toroidal, relé de 16A para cargas esclavas y driver MOSFET 12V ON-AIR. |
| **Lista de Materiales** | Lista BOM | [BOM.md](electrico/BOM.md) | Componentes de la placa, choque toroidal 2x4.7mH, condensadores X2/Y2, relé Hongfa 16A y varistores SPD Clase III. |
| **Firmware de Control** | Firmware ESPHome | [controlador_pdu_oficina.yaml](control/controlador_pdu_oficina.yaml) | Firmware nativo Home Assistant con desconexión automática de consumos vampiro por potencia residual (<18W) y control de señalizador ON-AIR. |

---

## 3. Scripts de Generación Paramétrica

- `scripts/generar_oficina_pdu_3d.py`: Genera el sólido 3D en FreeCAD 1.1+ y exporta en formato neutro STEP AP214.
- `scripts/generar_plano_oficina.py`: Dibuja el plano de distribución y esquema unifilar en DXF R12 y SVG vectorial.
- `scripts/generar_kicad_oficina.py`: Genera el esquema KiCad 10 y exporta el SVG mediante `kicad-cli`.
