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

## 4. Contenido del Directorio
- `planos_y_calculos/`: Planos de encofrado, cuadros de pilares, despiece de vigas y losas, memoria de cálculo estructural.
- `especificaciones/`: Criterios de dosificación, ensayos de probetas de hormigón y especificaciones de soldaduras y uniones metálicas.
