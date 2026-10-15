# Ventilación Mecánica Controlada (VMC) de Doble Flujo con Recuperador Entálpico y Free-Cooling

Este subsistema comprende el diseño aeráulico, mecánico, electrónico y de control para la renovación continua de aire en la vivienda bioclimática (10x10 m), con recuperación pasiva de calor y humedad (>90% de eficiencia), filtración F7/HEPA y enfriamiento nocturno pasivo (*Free-Cooling*).

---

## 1. Alcance Técnico y Dimensionamiento

### 1.1 Red Aeráulica y Distribución
- **Caudales de Diseño Higrotécnico (Norma UNE-EN 13141-7 / RITE):**
  - Caudal base (modo reposo/noche): $60\text{ m}^3\text{/h}$ ($0.25\text{ ren/h}$).
  - Caudal de confort (ocupación estándar): $120\text{ m}^3\text{/h}$ ($0.5\text{ ren/h}$).
  - Caudal de sobreventilación (Boost CO2 / Humedad): $210\text{ m}^3\text{/h}$ ($0.875\text{ ren/h}$).
- **Segregación de Estancias:**
  - **Impulsión de Aire Nuevo Filtrado (Estancias Secas):** Dormitorio Principal ($45\text{ m}^3\text{/h}$), Dormitorio Infantil ($30\text{ m}^3\text{/h}$), Salón-Comedor ($60\text{ m}^3\text{/h}$) mediante conductos circulares semirrígidos de polietileno antibacteriano y antiestático DN90.
  - **Extracción de Aire Viciado (Estancias Húmedas):** Cocina ($60\text{ m}^3\text{/h}$), Baño Principal ($35\text{ m}^3\text{/h}$).
- **Atenuación Acústica:**
  - Silenciadores circulares flexibles de lana mineral en plenum de impulsión y retorno ($L = 600\text{ mm}$), garantizando nivel de presión sonora interior $L_p \le 24\text{ dB(A)}$.

### 1.2 Recuperación Térmica y Eficiencia Entálpica
- Intercambiador de flujo a contracorriente con membrana polimérica entálpica capaz de transferir tanto calor sensible como calor latente (humedad), evitando la resecación del aire en invierno.
- Eficiencia térmica real calculada continuamente por firmware:
  $$\eta_{term} = \frac{T_{imp} - T_{ext}}{T_{extrac} - T_{ext}} \times 100\% \ge 90\%$$

### 1.3 Modo Free-Cooling Nocturno de Verano
- Compuerta de bypass 100% motorizada mediante actuador rotativo de 24V DC / 35 s de carrera.
- Conmutación automática cuando la temperatura exterior cae por debajo de la interior y la vivienda requiere refrigeración ($T_{int} > 23.5\ ^\circ\text{C}$), introduciendo aire fresco nocturno directamente sin pasar por el intercambiador de calor.

---

## 2. Entregables Técnicos Generados

| Componente | Tipo de Archivo | Enlaces | Descripción Técnica |
| :--- | :--- | :--- | :--- |
| **Unidad VMC Recuperadora** | Modelo 3D CAD | [unidad_vmc_recuperador_entalpico.FCStd](mecanico/unidad_vmc_recuperador_entalpico.FCStd)<br>[unidad_vmc_recuperador_entalpico.step](mecanico/unidad_vmc_recuperador_entalpico.step) | Ensamble 3D FreeCAD de la unidad VMC ($720\times620\times280\text{ mm}$), toberas DN160, núcleo entálpico, servomotor de bypass y drenaje con sifón. |
| **Plano de Red de Conductos** | Plano 2D CAD | [plano_distribucion_conductos_vmc.svg](mecanico/plano_distribucion_conductos_vmc.svg)<br>[plano_distribucion_conductos_vmc.dxf](mecanico/plano_distribucion_conductos_vmc.dxf) | Trazado en planta 2D de conductos semirrígidos DN90 de impulsión y retorno, ubicación de bocas de impulsión/extracción, silenciadores y tomas exteriores. |
| **Placa Controladora VMC** | Esquema KiCad 10 | [controlador_vmc_recuperador.kicad_sch](electrico/controlador_vmc_recuperador.kicad_sch)<br>[controlador_vmc_recuperador.svg](electrico/esquema_svg/controlador_vmc_recuperador.svg) | Hardware KiCad 10 con ESP32-S3, doble salida analógica 0-10V con DAC y Op-Amp, puente H DRV8871 para bypass 24V, tacómetros optoaislados y 4 sondas de temperatura. |
| **Lista de Materiales** | Lista BOM | [BOM.md](electrico/BOM.md) | Componentes de la placa, sensores de calidad de aire (SCD41 NDIR, SDP810 presión diferencial), conectores y reguladores. |
| **Firmware de Control** | Firmware ESPHome | [controlador_vmc_recuperador.yaml](control/controlador_vmc_recuperador.yaml) | Firmware nativo Home Assistant con modulación por demanda de CO2, boost automático por humedad, algoritmo de free-cooling y alerta de filtros. |

---

## 3. Scripts de Generación Paramétrica

- `scripts/generar_vmc_recuperador_3d.py`: Genera el sólido 3D en FreeCAD 1.1+ y exporta en formato neutro STEP AP214.
- `scripts/generar_plano_vmc.py`: Dibuja el plano de trazado aeráulico en DXF R12 y SVG vectorial.
- `scripts/generar_kicad_vmc.py`: Genera el esquema KiCad 10 y exporta el SVG mediante `kicad-cli`.
