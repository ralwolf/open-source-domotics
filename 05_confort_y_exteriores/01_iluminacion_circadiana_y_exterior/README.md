# Iluminación Modulada Circadiana y Control Exterior Inteligente

Este subsistema gestiona la iluminación biológica adaptativa en interiores para sincronizar los ritmos circadianos humanos (producción de melatonina y cortisol) según la posición solar astronómica local, junto con la modulación dinámica de la iluminación perimetral y exterior para seguridad y cortesía visual.

---

## 1. Arquitectura y Curva Circadiana Solar

La temperatura de color correlacionada (CCT) de las tiras LED interiores duales (2200K cálido ambarino a 6500K blanco frío luz día) se modula matemáticamente en función de la elevación solar ($\theta_{elev}$):

$$\text{CCT}(\theta_{elev}) = \begin{cases} 
2200\text{ K} & \text{si } \theta_{elev} < 0^\circ \text{ (Noche y Crepúsculo Civil)} \\
2200\text{ K} + \left(\frac{\theta_{elev}}{20^\circ}\right) \cdot (4000\text{ K} - 2200\text{ K}) & \text{si } 0^\circ \le \theta_{elev} < 20^\circ \text{ (Amanecer / Mañana temprana)} \\
4000\text{ K} + \left(\frac{\theta_{elev} - 20^\circ}{30^\circ}\right) \cdot (6500\text{ K} - 4000\text{ K}) & \text{si } 20^\circ \le \theta_{elev} < 50^\circ \text{ (Ascenso al mediodía)} \\
6500\text{ K} & \text{si } \theta_{elev} \ge 50^\circ \text{ (Cenit solar)}
\end{cases}$$

```
Temperatura CCT
  6500 K |                        /-------------------\
         |                       /                     \
  4000 K |               /------/                       \------\
         |              /                                       \
  2200 K | ------------/                                         \------------
         +-------------------------------------------------------------------->
          Noche (-10°)   Amanecer (0°)     Mediodía (60°)   Atardecer (0°) Noche
```

### Eliminación Total de Parpadeo (Flicker-Free 19.5 kHz)
Para evitar el estrés visual y el artefacto de bandas negras rodantes en cámaras de videovigilancia CCTV de alta velocidad, las salidas PWM se conmutan a **$19.531\text{ kHz}$**, muy por encima del umbral de percepción humana ($100\text{ Hz}$) y de los sensores CMOS de las cámaras PoE.

---

## 2. Entregables y Modelos del Subsistema

### 2.1 Diseño Mecánico y Perfilería 3D (`mecanico/`)
- **Modelo CAD FreeCAD 1.1+**: [perfil_aluminio_disipador_led.FCStd](mecanico/perfil_aluminio_disipador_led.FCStd)
- **Modelo de Intercambio STEP**: [perfil_aluminio_disipador_led.step](mecanico/perfil_aluminio_disipador_led.step)
- **Script Generador 3D**: [generar_perfil_led_3d.py](../../scripts/generar_perfil_led_3d.py)
- **Plano 2D CAD (AutoCAD R12 DXF)**: [plano_corte_perfil_led.dxf](mecanico/plano_corte_perfil_led.dxf)
- **Plano Vectorial SVG**: [plano_corte_perfil_led.svg](mecanico/plano_corte_perfil_led.svg)
- **Script Generador Plano 2D**: [generar_plano_perfil_led.py](../../scripts/generar_plano_perfil_led.py)
- **Especificaciones**:
  - Perfil extruido de aluminio arquitectónico 6063-T5 ($25 \times 15\text{ mm}$, longitud representativa $300\text{ mm}$, extensible).
  - Difusor curvo de policarbonato opalino Makrolon con protección anti-UV y transmitancia óptica optimizada al 85%.
  - Canal interior para disipación térmica de tiras LED de alta potencia ($19.2\text{ W/m}$, temperatura de unión $T_j < 55^\circ\text{C}$).
  - Grapas de anclaje oculto en acero inoxidable AISI 304 con fijación a presión clic.

### 2.2 Diseño Eléctrico y Esquemático KiCad 10 (`electrico/`)
- **Proyecto KiCad 10**: [controlador_dimmer_circadiano.kicad_pro](electrico/controlador_dimmer_circadiano.kicad_pro)
- **Esquema Electrónico**: [controlador_dimmer_circadiano.kicad_sch](electrico/controlador_dimmer_circadiano.kicad_sch)
- **Vectorial SVG**: [controlador_dimmer_circadiano.svg](electrico/esquema_svg/controlador_dimmer_circadiano.svg)
- **Lista de Materiales y Costes (BOM)**: [BOM.md](electrico/BOM.md)
- **Script Generador KiCad**: [generar_kicad_iluminacion.py](../../scripts/generar_kicad_iluminacion.py)
- **Topología de Potencia**:
  - Fuente conmutada centralizada Mean Well HLG-240H-24 ($24\text{VDC}$, $10\text{A}$, eficiencia $94\%$, certificación SELV).
  - 4x MOSFETs de potencia canal N AOD4184A ($40\text{V}$, $50\text{A}$, $R_{DS(on)} < 8.5\text{ m}\Omega$).
  - Drivers de compuerta rápidos TC4427 para tiempos de conmutación $t_r, t_f < 30\text{ ns}$.
  - Diodos de supresión TVS SMBJ28A y Schottky SS34 para absorber la energía inductiva de líneas largas de tiras LED.

### 2.3 Firmware y Automatización ESPHome (`control/`)
- **Firmware ESPHome**: [iluminacion_circadiana_confort.yaml](control/iluminacion_circadiana_confort.yaml)
- **Lógica Integrada**:
  - Plataforma de luz `cct` que mezcla dinámicamente Warm White y Cold White con curva gamma $2.8$.
  - Seguimiento astronómico solar en tiempo real (`sun.elevation`) para sincronización biológica circadiana autónoma cada 5 minutos.
  - Sensor I2C BH1750 para compensación de lux ambiental interior (ahorro de energía cuando entra luz solar por ventanales).
  - Sensor de presencia humana por radar mmWave de $24\text{ GHz}$ Hi-Link LD2410 (detección de presencia fija / respiración sin requerir movimiento brusco).
  - Iluminación perimetral de seguridad: modo cortesía nocturna tenue ($15\%$) que transiciona en rampa suave ($1\text{ s}$) al $100\%$ ante detección de personas por Frigate NVR o sensores perimetrales, regresando automáticamente a cortesía tras 60 segundos sin actividad.
