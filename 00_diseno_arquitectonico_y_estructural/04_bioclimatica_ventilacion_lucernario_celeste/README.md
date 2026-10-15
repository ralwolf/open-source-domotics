# Lucernario Cenital Bioclimático y Chimenea Solar

## 1. Descripción y Alcance
Este subsistema combina el confort lumínico y térmico pasivo con la pasión por la astronomía amateur. Consiste en una cúpula cenital acristalada a dos aguas ($3.0 \times 2.0\text{ m}$) sobre el patio central de la vivienda, dotada de vidrio doble de seguridad bajo emisivo extraclaro (*low-iron*), compuertas perimetrales basculantes accionadas por actuadores lineales de 24V DC y control meteorológico predictivo que explota el efecto chimenea solar para refrigerar pasivamente la vivienda durante la noche estival.

---

## 2. Entregables Mecánicos y Modelado 3D (`mecanico/`)
- [`lucernario_astronomico_cenital.FCStd`](./mecanico/lucernario_astronomico_cenital.FCStd): Modelo paramétrico 3D nativo en FreeCAD 1.1+ del lucernario cenital ($3.0 \times 2.0\text{ m}$), perfilería de aluminio estructural con rotura de puente térmico (RPT), compuertas basculantes y actuadores lineales.
- [`lucernario_astronomico_cenital.step`](./mecanico/lucernario_astronomico_cenital.step): Archivo STEP AP214 para análisis CFD y verificación de estanqueidad.
- [`seccion_bioclimatica_lucernario.dxf`](./mecanico/seccion_bioclimatica_lucernario.dxf): Plano CAD 2D de sección transversal arquitectónica mostrando el tiro térmico ascendente, las cotas del brocal de coronación y la entrada de aire fresco desde el patio interior.
- [`seccion_bioclimatica_lucernario.svg`](./mecanico/seccion_bioclimatica_lucernario.svg): Esquema vectorial ilustrativo del flujo convectivo nocturno.

---

## 3. Entregables Eléctricos y Electrónica (`electrico/`)
- [`controlador_lucernario_bioclimatico.kicad_sch`](./electrico/controlador_lucernario_bioclimatico.kicad_sch): Esquema electrónico profesional en KiCad 10 con ESP32-S3, etapa de potencia en puente H LMD18200 (24V 3A), interfaz para sensor óptico de lluvia Hydreon RG-11, contador de pulsos para anemómetro de cazoletas y fuente industrial Mean Well IRM-15-24.
- [`controlador_lucernario_bioclimatico.kicad_pro`](./electrico/controlador_lucernario_bioclimatico.kicad_pro): Archivo de proyecto en KiCad 10.
- [`esquema_svg/controlador_lucernario_bioclimatico.svg`](./electrico/esquema_svg/controlador_lucernario_bioclimatico.svg): Renderizado esquemático vectorial.
- [`BOM.md`](./electrico/BOM.md): Lista completa de materiales y componentes.

---

## 4. Entregables de Control y Firmware (`control/`)
- [`controlador_lucernario.yaml`](./control/controlador_lucernario.yaml): Firmware para ESPHome con algoritmo de ventilación pasiva libre (*free-cooling*), enclavamiento por hardware ante lluvia inminente (<100 ms) y repliegue preventivo ante rachas de viento superiores a 40 km/h.
- [`NOTA_DE_DISENO.md`](./NOTA_DE_DISENO.md): Memoria técnica de cálculo del caudal volumétrico por convección natural según gradiente térmico $\Delta T$.
