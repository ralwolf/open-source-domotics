# Motorización y Control Bioclimático de Persianas y Cortinas

Este subsistema implementa el control motorizado inteligente de persianas enrollables y cortinas arquitectónicas, optimizando el confort térmico y lumínico mediante algoritmos solares bioclimáticos (azimut y elevación solar) e incorporando protección física de interbloqueo (*hardware interlock*) para salvaguardar los bobinados de los motores tubulares.

---

## 1. Arquitectura de Control e Interbloqueo Físico

```
                           +-------------------------+
                           |  RED ELÉCTRICA 230VAC   |
                           +------------+------------+
                                        | Fase L
                                        v
                           +-------------------------+
                           |  RELÉ K1 (POWER ON/OFF) |
                           |  Contacto SPST (GPIO18) |
                           +------------+------------+
                                        | Fase Conmutada
                                        v
                           +-------------------------+
                           | RELÉ K2 (SUBIR / BAJAR) |
                           | Contacto SPDT (GPIO19)  |
                           +------------+------------+
                               /                   \
           Contacto NC        /                     \  Contacto NO
                             v                       v
                  +--------------------+   +--------------------+
                  | FASE BAJAR (L_DOWN)|   | FASE SUBIR (L_UP)  |
                  | Cable Negro Motor  |   | Cable Marrón Motor |
                  +--------------------+   +--------------------+
```

### Seguridad por Diseño (*Zero-Short-Circuit*)
En los motores tubulares tradicionales de 4 hilos (Subir, Bajar, Neutro, Tierra), energizar simultáneamente las fases de subida y bajada provoca un cortocircuito entre los condensadores de desfase internos, destruyendo instantáneamente el devanado del estator. La topología de doble relé en cascada (K1 corte general + K2 conmutador SPDT) **hace físicamente imposible** la conexión simultánea de ambas fases, incluso ante cuelgues del firmware o fallos de software.

---

## 2. Entregables y Modelos del Subsistema

### 2.1 Diseño Mecánico y Eje Octogonal 3D (`mecanico/`)
- **Modelo CAD FreeCAD 1.1+**: [mecanismo_persiana_eje_octogonal.FCStd](mecanico/mecanismo_persiana_eje_octogonal.FCStd)
- **Modelo de Intercambio STEP**: [mecanismo_persiana_eje_octogonal.step](mecanico/mecanismo_persiana_eje_octogonal.step)
- **Script Generador 3D**: [generar_persiana_3d.py](../../scripts/generar_persiana_3d.py)
- **Plano 2D CAD (DXF)**: [plano_mecanismo_persiana.dxf](mecanico/plano_mecanismo_persiana.dxf)
- **Plano Vectorial SVG**: [plano_mecanismo_persiana.svg](mecanico/plano_mecanismo_persiana.svg)
- **Script Generador Plano 2D**: [generar_plano_persiana.py](../../scripts/generar_plano_persiana.py)
- **Especificaciones**:
  - Eje octogonal de chapa de acero galvanizado $\varnothing 60\text{ mm}$ (longitud representativa $1200\text{ mm}$).
  - Motor tubular embutido de $20\text{ Nm}$ ($17\text{ rpm}$, $160\text{W}$, capacidad de elevación hasta $38\text{ kg}$).
  - Corona de acople octogonal y contera plástica de poliamida con rodamiento de bolas estanco de acero.
  - Cajón monoblock termoacústico con aislamiento de poliestireno expandido y lamas de aluminio inyectadas con poliuretano de alta densidad ($45\text{ mm}$).

### 2.2 Diseño Eléctrico y Esquemático KiCad 10 (`electrico/`)
- **Proyecto KiCad 10**: [controlador_persianas_motorizadas.kicad_pro](electrico/controlador_persianas_motorizadas.kicad_pro)
- **Esquema Electrónico**: [controlador_persianas_motorizadas.kicad_sch](electrico/controlador_persianas_motorizadas.kicad_sch)
- **Vectorial SVG**: [controlador_persianas_motorizadas.svg](electrico/esquema_svg/controlador_persianas_motorizadas.svg)
- **Lista de Materiales y Costes (BOM)**: [BOM.md](electrico/BOM.md)
- **Script Generador KiCad**: [generar_kicad_persianas.py](../../scripts/generar_kicad_persianas.py)
- **Topología Electrónica**:
  - Fuente conmutada Hi-Link HLK-PM01 integrada ($230\text{VAC}$ a $5\text{VDC}$).
  - Microcontrolador ESP32-WROOM-32E.
  - Módulo de relés de maniobra 10A con red amortiguadora snubber RC ($47\ \Omega + 47\text{ nF}$ clase X2) para absorción de arco inductivo.
  - Entradas de pulsador doble de pared (Subir/Bajar) aisladas ópticamente mediante optoacopladores PC817 ($5\text{ kV}$).
  - Sensor de corriente efecto Hall ACS712 para detección en tiempo real de sobreesfuerzos mecánicos y obstáculos anti-atrapamiento.

### 2.3 Firmware y Automatización ESPHome (`control/`)
- **Firmware ESPHome**: [persiana_bioclimatica_control.yaml](control/persiana_bioclimatica_control.yaml)
- **Lógica Integrada**:
  - Plataforma `cover: time_based` con posicionamiento porcentual exacto (0% a 100%).
  - Tiempos de maniobra calibrados: Apertura $22\text{ s}$, Cierre $20\text{ s}$.
  - Algoritmo solar bioclimático autónomo:
    - **Protección solar de verano:** Si la elevación solar supera $30^\circ$ y el azimut coincide con la fachada expuesta, la persiana desciende automáticamente al 75% para mitigar la ganancia térmica por radiación directa manteniendo la micro-ventilación.
    - **Aislamiento nocturno de invierno:** Al descender el sol por debajo del horizonte astronómico (elevación $< -1.0^\circ$), la persiana se cierra totalmente al 0% para retener el calor interior.
  - Parada automática instantánea ($< 200\text{ ms}$) si el sensor de corriente detecta un pico superior a $1.4\text{ A}$ (detección de atasco o presencia de objetos).
