# Mecánica de Suelos, Estudio Geotécnico y Cimentación (Zapatas y Riostras)

## 1. Alcance Técnico
Define el estudio del terreno, capacidad de soporte del sustrato y el cálculo estructural de las fundaciones para sostener con factor de seguridad riguroso la edificación, el banco de baterías, el volumen de agua de piscinas/termoacumuladores y los empujes de viento de la turbina eólica.

## 2. Ensayos y Parámetros Geotécnicos Requeridos
- **Sondeos y Ensayos SPT (Standard Penetration Test):** Determinación del perfil estratigráfico hasta el estrato resistente (mínimo 6-8 metros de profundidad).
- **Parámetros del Suelo:** Cohesión ($c$), ángulo de fricción interna ($\phi$), peso específico ($\gamma$), y cálculo de la capacidad portante admisible ($\sigma_{adm}$ en $kg/cm^2$ o $kPa$).
- **Nivel Freático:** Medición de variaciones estacionales de agua subterránea para diseño de impermeabilización y drenaje perimetral.
- **Clasificación Sísmica del Terreno:** Parámetros de aceleración espectral y tipo de suelo según la normativa sísmica local.

## 3. Diseño Estructural de la Cimentación
- **Tipología de Cimentación:**
  - Zapatas aisladas bajo columnas principales conectadas mediante vigas de atado/riostras antisísmicas.
  - Zapatas corridas bajo muros de carga o contención.
  - Losa de cimentación maciza armada en la zona técnica de alta concentración de masa (banco de baterías LiFePO4, generador y depósitos de agua).
- **Armado y Materiales:**
  - Hormigón estructural de resistencia $f'_c \ge 250\ kg/cm^2$ ($H-25$ / $25\ MPa$) con aditivos hidrófugos.
  - Acero de refuerzo corrugado $f_y = 4200\ kg/cm^2$ ($B400S$ / Grado 60).
  - Recubrimiento mínimo de hormigón contra terreno: 5.0 cm a 7.5 cm con solera de hormigón de limpieza previa.

## 4. Contenido del Directorio
- `planos_y_calculos/`:
  - [`plano_cimentacion_ejes.dxf`](./planos_y_calculos/plano_cimentacion_ejes.dxf): Plano CAD 2D de replanteo con ejes 1-3 y A-C, zapatas aisladas ($1.30 \times 1.30\text{ m}$), vigas riostras y columna maestra C-TURB.
  - [`plano_cimentacion_ejes.svg`](./planos_y_calculos/plano_cimentacion_ejes.svg): Vista vectorial interactiva de replanteo de zapatas, vigas riostras y losa técnica de sala de baterías.
  - [`cimentacion_zapatas_pilares.FCStd`](./planos_y_calculos/cimentacion_zapatas_pilares.FCStd): Modelo 3D paramétrico nativo en FreeCAD 1.1+.
  - [`cimentacion_zapatas_pilares.step`](./planos_y_calculos/cimentacion_zapatas_pilares.step): Exportación universal STEP AP214 para visualización e interoperabilidad BIM.
- `especificaciones/`: Fichas técnicas de hormigones, estudio geotécnico del terreno y directrices de excavación y drenajes.
- [`NOTA_DE_DISENO.md`](./NOTA_DE_DISENO.md): Memoria de cálculo geotécnico y dimensionamiento estructural.
