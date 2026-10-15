# Estructura Portante: Pilares, Columnas, Vigas y Losas de Cubierta

## 1. Alcance Técnico
Cálculo y diseño de la estructura portante de la vivienda (esqueleto resistente), concebida para permitir plantas diáfanas, vanos amplios para iluminación y absorción de cargas vivas y muertas especiales.

## 2. Cargas Consideradas en el Cálculo Estructural
- **Cargas Muertas Permanentes ($D$):**
  - Peso propio de losas, vigas, muros divisorios y acabados de piso.
  - Carga concentrada de bancada de baterías LiFePO4 en área técnica (~400-600 kg).
  - Carga de termoacumulador solar presurizado en azotea (300 L de agua + estanque = ~400 kg).
  - Peso de colectores solares térmicos y módulos solares fotovoltaicos con su estructura de aluminio.
- **Cargas Vivas ($L$):**
  - Sobrecarga de uso residencial ($200\ kg/m^2$).
  - Sobrecarga de terraza transitable ($300\ kg/m^2$).
- **Cargas Dinámicas y Ambientales:**
  - **Empuje y Vórtices Eólicos en Torre:** Momento volcador y vibración transmitida por la turbina eólica Archimedes MK9; anclaje a través de pilar estructural arriostrado con amortiguación elastomérica de neopreno.
  - Acción sísmica tridimensional ($E$) combinada según código sismorresistente.

## 3. Elementos Constructivos
- **Pilares / Columnas:** Secciones de hormigón armado o perfiles tubulares de acero estructural rellenos de hormigón (sección mixta para mayor esbeltez).
- **Vigas de Carga:** Vigas descolgadas o planas con estribado reforzado en nudos columna-viga contra fuerzas cortantes sísmicas.
- **Losas de Entrepiso y Techo:**
  - Losas aligeradas con bovedillas termoaislantes o losas macizas de hormigón armado.
  - Pendientes mínimas del 2% en azotea hacia canalones pluviales de gran sección.

## 4. Contenido y Entregables del Directorio
- **`planos_y_calculos/`**:
  - [`estructura_portante_vivienda.FCStd`](planos_y_calculos/estructura_portante_vivienda.FCStd): Modelo 3D paramétrico FreeCAD del esqueleto estructural completo (10x10 m): 9 pilares (P1 a P8 en 30x30 cm y P9 C-TURB en 35x35 cm con pedestal eólico), vigas de amarre perimetrales e interiores V-101 (25x40 cm), vigas de borde V-102 (20x40 cm) y losa maciza de cubierta ($e = 20\text{ cm}$) con hueco cenital de 3.0x2.0 m para el lucernario astronómico.
  - [`estructura_portante_vivienda.step`](planos_y_calculos/estructura_portante_vivienda.step): Modelo 3D exportado en formato estándar neutro STEP.
  - [`plano_estructura_pilares_losas.dxf`](planos_y_calculos/plano_estructura_pilares_losas.dxf): Plano CAD 2D de forjado de cubierta, ejes de replanteo 1-3 y A-C, cuadro de pilares, armaduras longitudinales, estribos de confinamiento y notas de diseño sismorresistente.
  - [`plano_estructura_pilares_losas.svg`](planos_y_calculos/plano_estructura_pilares_losas.svg): Plano estructural vectorial renderizado con cotas y cuadro de pilares.
- **`NOTA_DE_DISENO.md`**: Memoria técnica de cálculo y cuadro de pilares según Eurocódigo 2 / ACI 318.
- **`especificaciones/`**: Criterios de dosificación HA-25 / f'c = 25 MPa, acero B500S, control de fisuración y ensayos destructivos/no destructivos.

