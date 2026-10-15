# Generador Eléctrico a Gasolina (Respaldo Terciario ATS)

Este subsistema comprende la infraestructura electromecánica, aislamiento acústico, conmutación automática de potencia y automatización para el grupo electrógeno de respaldo terciario de la vivienda (10x10 m), diseñado para garantizar la continuidad del suministro esencial ante cortes prolongados de la red y agotamiento del banco solar de baterías LiFePO4.

---

## 1. Alcance y Especificaciones Técnicas

### 1.1 Cabina Exterior Insonorizada y Emplazamiento
- **Dimensiones y Materiales:** Cabina de chapa de acero galvanizado de $950 \times 650 \times 700\text{ mm}$ con recubrimiento de pintura epoxi electrostática para intemperie e interior revestido con espuma de poliuretano fonoabsorbente ignífuga clase M1 de 30 mm de espesor.
- **Atenuación Acústica:** Conductos de ventilación en laberinto y silenciador de escape exterior de alta pérdida de inserción con parallamas integrado, manteniendo el nivel sonoro por debajo de $65\text{ dBA}$ a 7 metros de distancia.
- **Desacoplo de Vibraciones:** 4 amortiguadores elásticos de caucho vulcanizado (*silentblocks*) en la base del bastidor para evitar la propagación de ondas mecánicas hacia la cimentación.

### 1.2 Grupo Electrógeno y Sistema de Alimentación
- **Motor y Alternador:** Motor térmico de 4 tiempos OHV de $389\text{ cc}$, alternador síncrono monofásico de $6.5\text{ kVA}$ ($5.2\text{ kW}$ continuo) a 230V 50Hz con regulación automática de voltaje AVR ($\pm 1.5\%$).
- **Arranque Eléctrico y Mantenimiento:** Motor de arranque de 12V con batería de arranque de plomo-calcio / LiFePO4 mantenida permanentemente a flote ($13.6\text{ V}$) mediante cargador electrónico conectado a las cargas esenciales del inversor.
- **Depósito de Combustible:** Tanque de gasolina de 25 litros con sensor analógico de nivel por boya resistiva (autonomía aproximada de 14 horas al 50% de carga).

### 1.3 Tablero de Transferencia Automática (ATS) con Enclavamiento Mecánico
- Conmutador motorizado de 63A y 2 polos con **enclavamiento mecánico y eléctrico simultáneo**, haciendo físicamente imposible el cortocircuito o retroalimentación accidental entre la red de compañía/inversor ESS y el generador.
- Tiempo de transferencia programable: retardo de 45 segundos tras el arranque para estabilización térmica y de régimen de revoluciones antes de acoplar la carga.

### 1.4 Lógicas de Automatización y Respaldo
- **Arranque por SoC Crítico:** Si el banco de baterías LiFePO4 cae por debajo del $18\%\text{ SoC}$ en ausencia de radiación solar y fallo de red, Home Assistant o el inversor híbrido activan la secuencia de arranque automático por contacto seco.
- **Secuencia de 3 Intentos:** Secuencia temporizada de 3 ciclos de intento (4 s estárter / 10 s reposo) con detección de tensión generada por optoacoplador para desacople inmediato del solenoide de arranque.
- **Test Mensual de Mantenimiento:** Rutina automatizada que arranca el generador el primer domingo de cada mes durante 10 minutos en vacío para garantizar la lubricación del motor y verificación operativa de la batería.

---

## 2. Entregables Técnicos Generados

| Componente | Tipo de Archivo | Enlaces | Descripción Técnica |
| :--- | :--- | :--- | :--- |
| **Cabina Insonorizada 3D** | Modelo CAD 3D | [cabina_insonorizada_generador_gasolina.FCStd](mecanico/cabina_insonorizada_generador_gasolina.FCStd)<br>[cabina_insonorizada_generador_gasolina.step](mecanico/cabina_insonorizada_generador_gasolina.step) | Ensamble 3D FreeCAD de la cabina de intemperie ($950\times650\times700\text{ mm}$), laberintos de ventilación, tubo de escape con silenciador y silentblocks. |
| **Plano de Instalación y ATS** | Plano 2D CAD | [plano_generador_respaldo_ats.svg](mecanico/plano_generador_respaldo_ats.svg)<br>[plano_generador_respaldo_ats.dxf](mecanico/plano_generador_respaldo_ats.dxf) | Distribución 2D en patio exterior, esquema unifilar de tablero ATS con enclavamiento mecánico, cableado de potencia 3x6 mm² y control de arranque. |
| **Placa PCB Control ATS** | Esquema KiCad 10 | [controlador_generador_respaldo_ats.kicad_sch](electrico/controlador_generador_respaldo_ats.kicad_sch)<br>[controlador_generador_respaldo_ats.svg](electrico/esquema_svg/controlador_generador_respaldo_ats.svg) | Hardware KiCad 10 con ESP32-C3, relés de arranque e ignición, detector de 230VAC de generador por optoacoplador, monitor de batería 12V y comando ATS. |
| **Lista de Materiales** | Lista BOM | [BOM.md](electrico/BOM.md) | Componentes de la placa, relés Finder/Hongfa 16A, optoacoplador EL814, regulador buck MP1584 y borneros de conexión. |
| **Firmware de Control** | Firmware ESPHome | [controlador_generador_ats.yaml](control/controlador_generador_ats.yaml) | Firmware nativo Home Assistant con secuencia de 3 intentos de arranque, retardo de calentamiento 45s, rutina de lubricación mensual y alerta de combustible. |

---

## 3. Scripts de Generación Paramétrica

- `scripts/generar_generador_cabina_3d.py`: Genera el sólido 3D en FreeCAD 1.1+ y exporta en formato neutro STEP AP214.
- `scripts/generar_plano_generador_ats.py`: Dibuja el plano de distribución y esquema unifilar en DXF R12 y SVG vectorial.
- `scripts/generar_kicad_generador_ats.py`: Genera el esquema KiCad 10 y exporta el SVG mediante `kicad-cli`.
