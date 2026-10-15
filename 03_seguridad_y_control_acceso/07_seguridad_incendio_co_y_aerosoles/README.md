# Seguridad Contra Incendios, Monóxido de Carbono (CO) y Extinción por Aerosol

Este subsistema implementa la protección contra incendios de grado industrial conforme a las normas EN 54 y NFPA 72: detección óptica y térmica de humo, detección electroquímica de monóxido de carbono ($\text{CO}$), enclavamiento inmediato para el corte de gas combustible y parada de la ventilación mecánica, junto con un sistema autónomo de extinción química por aerosol condensado de carbonato de potasio ($K_2CO_3$, tecnología Stat-X / FirePro) para recintos críticos (Rack IT 19" y Banco de Baterías LiFePO4).

---

## 1. Arquitectura de Detección, Enclavamientos y Extinción

```
           [ DETECCIÓN HUMO EN 54 ]                [ SENSOR CO FIGARO ]
          Lazo Supervisado EOL 4.7kΩ               Electroquímico 0-1000 ppm
                      \                                  /
                       \                                /
                        v                              v
           +------------------------------------------------+
           |     CENTRAL DE INCENDIO AUTÓNOMA (ESP32)       |
           |     Respaldo 24V UPS + Supercondensador 4700µF |
           +-----------------------+------------------------+
                                   |
             +---------------------+---------------------+
             | Disparo Inmediato (<2s)                   | Alarma Confirmada Coincidencia
             v                                           v
+-----------------------------+           +-----------------------------+
| ENCLAVAMIENTOS DE SEGURIDAD |           | SECUENCIA DE EXTINCIÓN IT   |
| 1. Corte Electroválvulas Gas|           | 1. Cuenta atrás 30s sonora  |
| 2. Parada VMC y Climatizac. |           | 2. Pulsador de aborto       |
| 3. Apertura 100% Persianas  |           | 3. Pulso Dual-MOSFET 24V 2A |
| 4. Luces 100% Blanco Escape |           | 4. Descarga Stat-X K2CO3    |
| 5. Sirena 110dB + Strobe 24V|           |    (Inundación 10s sin agua)|
+-----------------------------+           +-----------------------------+
```

### Principio de Extinción por Aerosol Condensado (Stat-X)
A diferencia de los rociadores de agua que dañan la electrónica o de los gases de inundación (CO2/Inergen) que asfixian y requieren botellas a alta presión ($200\text{ bar}$):
- El aerosol condensado permanece como un compuesto sólido estable a presión ambiente.
- Al activarse eléctricamente mediante el puente iniciador ($24\text{V}$, $1.5\text{A}$), se genera una micro-niebla de partículas de $K_2CO_3$ ultra-finas ($1\text{ - }2\ \mu\text{m}$).
- Estas partículas se combinan catalíticamente con los radicales libres de la combustión ($OH^\bullet$ y $H^\bullet$), rompiendo la reacción en cadena de la llama a nivel molecular en menos de $10\text{ segundos}$ sin desplazar el oxígeno respirable y sin dejar residuos conductores.

---

## 2. Entregables y Modelos del Subsistema

### 2.1 Diseño Mecánico y Cápsula Extintora 3D (`mecanico/`)
- **Modelo CAD FreeCAD 1.1+**: [capsula_extincion_aerosol_soporte.FCStd](mecanico/capsula_extincion_aerosol_soporte.FCStd)
- **Modelo de Intercambio STEP**: [capsula_extincion_aerosol_soporte.step](mecanico/capsula_extincion_aerosol_soporte.step)
- **Script Generador 3D**: [generar_aerosol_incendio_3d.py](../../scripts/generar_aerosol_incendio_3d.py)
- **Plano 2D CAD (DXF)**: [plano_seguridad_incendio_aerosoles.dxf](mecanico/plano_seguridad_incendio_aerosoles.dxf)
- **Plano Vectorial SVG**: [plano_seguridad_incendio_aerosoles.svg](mecanico/plano_seguridad_incendio_aerosoles.svg)
- **Script Generador Plano 2D**: [generar_plano_incendio.py](../../scripts/generar_plano_incendio.py)
- **Especificaciones**:
  - Cápsula cilíndrica de acero inoxidable AISI 304 $\varnothing 75\text{ mm}$, altura $160\text{ mm}$ con boquilla radial de dispersión 360°.
  - Abrazadera de fijación con disipación térmica para montaje en bastidor de rack 19" o carcasa de celdas LiFePO4.
  - Detector óptico de humo con laberinto fotométrico y rejilla anti-insectos.
  - Plano de implantación con zonificación EN 54 y radios de cobertura de $7.5\text{ m}$.

### 2.2 Diseño Eléctrico y Esquemático KiCad 10 (`electrico/`)
- **Proyecto KiCad 10**: [controlador_incendio_aerosoles.kicad_pro](electrico/controlador_incendio_aerosoles.kicad_pro)
- **Esquema Electrónico**: [controlador_incendio_aerosoles.kicad_sch](electrico/controlador_incendio_aerosoles.kicad_sch)
- **Vectorial SVG**: [controlador_incendio_aerosoles.svg](electrico/esquema_svg/controlador_incendio_aerosoles.svg)
- **Lista de Materiales y Costes (BOM)**: [BOM.md](electrico/BOM.md)
- **Script Generador KiCad**: [generar_kicad_incendio.py](../../scripts/generar_kicad_incendio.py)
- **Topología de Alta Seguridad**:
  - Lazo supervisado Clase B con resistencia EOL de $4.7\text{ k}\Omega$ (discriminación de Estado Normal, Fuego, y Avería por cable cortado o en corto).
  - Sensor electroquímico de monóxido de carbono Figaro TGS5042 con vida útil garantizada de 10 años.
  - Banco de energía autónomo con condensador de baja ESR de $4700\ \mu\text{F}\ 35\text{V}$, garantizando la energía de ignición de las cápsulas incluso con la alimentación principal cortada.
  - Conmutación en serie de doble MOSFET (High-Side P-MOSFET + Low-Side N-MOSFET) para impedir disparos accidentales ante un fallo único de componente.
  - Supervisión pasiva de línea de iniciador ($I_{test} < 5\text{ mA}$) para verificación continua de continuidad del cartucho pirotécnico.

### 2.3 Firmware y Automatización ESPHome (`control/`)
- **Firmware ESPHome**: [sistema_incendio_co_aerosoles.yaml](control/sistema_incendio_co_aerosoles.yaml)
- **Lógica Integrada**:
  - Evaluación analógica continua del lazo EN54 y detección de anomalías.
  - Monitorización en tiempo real de PPM de CO con umbrales de ventilación ($30\text{ ppm}$) y alarma crítica ($70\text{ ppm}$).
  - Secuencia de extinción por aerosol con aviso acústico de 30 segundos y pulsador físico de aborto.
  - Enclavamiento físico y eventos automáticos de Home Assistant: parada de clima y VMC, corte de electroválvulas de gas y apertura de persianas para evacuación.
