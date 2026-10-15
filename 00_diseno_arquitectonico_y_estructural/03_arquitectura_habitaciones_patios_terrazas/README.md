# Diseño Arquitectónico: Habitaciones, Patios y Terrazas

## 1. Descripción y Alcance
Este subsistema define la distribución espacial bioclimática, circulaciones ergonómicas y optimización solar pasiva de la vivienda unifamiliar aislada de $10.00 \times 10.00\text{ m}$ (100 m² construidos en planta). La planta se organiza en torno a un patio interior central ($3.00 \times 2.00\text{ m}$) que actúa como chimenea solar, pozo de luz natural para todas las estancias y pulmón verde termorregulador.

---

## 2. Entregables de Diseño Arquitectónico y Modelado 3D (`mecanico/`)
- [`modelo_arquitectonico_vivienda_3d.FCStd`](./mecanico/modelo_arquitectonico_vivienda_3d.FCStd): Modelo paramétrico 3D volumétrico nativo en FreeCAD 1.1+ de la envolvente edificatoria, solera de cimentación, cerramientos exteriores de 30 cm con aislamiento térmico continuo (SATE), tabiquería interior divisoria, patio central cenital con hueco de lucernario en cubierta y vanos de carpintería exterior (puertas y ventanas).
- [`modelo_arquitectonico_vivienda_3d.step`](./mecanico/modelo_arquitectonico_vivienda_3d.step): Archivo de intercambio neutro STEP AP214 para simulaciones energéticas dinámicas (BEM / EnergyPlus) y análisis de asoleamiento.

---

## 3. Planos 2D de Distribución y Replanteo (`planos_2d_dxf/`)
- [`planta_arquitectonica_base.dxf`](./planos_2d_dxf/planta_arquitectonica_base.dxf): Plano CAD 2D normalizado con cotas acotadas en milímetros, distribución de estancias (Dormitorio principal 16 m², Dormitorio infantil 16 m², Salón-Comedor 24 m², Cocina ergonómica 17 m², Baño 8.5 m², Sala IT central 6 m² y Patio interior 6 m²).
- [`planta_arquitectonica_base.svg`](./planos_2d_dxf/planta_arquitectonica_base.svg): Plano vectorial interactivo en formato SVG en alta resolución con zonificación cromática y orientación norte.
