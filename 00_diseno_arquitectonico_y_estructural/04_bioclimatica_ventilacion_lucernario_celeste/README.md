# Diseño Bioclimático: Ventilación Cruzada, Iluminación Pasiva y Vitrina Astronómica Cenital

## 1. Alcance Técnico
Aprovechamiento de los recursos naturales del entorno (radiación solar, vientos dominantes y bóveda celeste) para reducir drásticamente el consumo energético activo y proporcionar una experiencia sensorial única mediante observación estelar.

## 2. Ventilación Natural Cruzada y Flujo Dinámico de Aire
- **Orientación de Vanos:** Ventanas enfrentadas estratégicamente situadas según los cuadrantes de los vientos predominantes locales.
- **Efecto Chimenea / Tiro Térmico:** Entrada de aire fresco a nivel inferior por patios sombreados que desplaza el aire caliente acumulado hacia las salidas superiores del lucernario en el techo.
- **Carpinterías Eficientes:** Ventanas de PVC o aluminio con rotura de puente térmico (RPT), doble o triple acristalamiento bajo emisivo (*Low-E*) con gas argón en cámara (4/16/4 o 6/16/6) y apertura oscilobatiente.

## 3. Vitrina / Cúpula Cenital para Iluminación y Observación Astronómica de Estrellas
- **Diseño del Lucernario de Cubierta:**
  - Estructura de vidrio templado extraclaro laminado de alta resistencia al impacto de granizo y deformaciones térmicas.
  - Inclinación geométrica calculada para máxima captación de luz natural en invierno y reducción de deslumbramiento en verano.
  - Tratamiento óptico antirreflejante de alta transmitancia luminosa para **observación astronómica nocturna de constelaciones y estrellas** desde el interior (salón o distribuidor central).
- **Mecanismo de Ventilación y Oscurecimiento Motorizado:**
  - Apertura basculante o corrediza motorizada mediante actuador lineal de 24V DC integrado a Home Assistant: se abre automáticamente en noches frescas de verano para refrescar la casa y se cierra al detectar lluvia mediante sensor pluviométrico.
  - Cortina plisada celular motorizada para oscurecimiento total y aislamiento térmico en horas de máxima radiación estival.

## 4. Contenido del Directorio
- `mecanico/`:
  - [`lucernario_astronomico_cenital.FCStd`](./mecanico/lucernario_astronomico_cenital.FCStd): Modelo 3D paramétrico en FreeCAD 1.1+ (marco perimetral de $3.0 \times 2.0\text{ m}$, acristalamiento doble laminado low-iron y actuador lineal basculante de $24\text{ V}$).
  - [`lucernario_astronomico_cenital.step`](./mecanico/lucernario_astronomico_cenital.step): Modelo universal STEP AP214 para fabricación y ensamble mecánico.
- `diseno_lucernario/`: Planos de detalle constructivo del lucernario cenital, sellados impermeables EPDM, marco de aluminio y especificaciones del vidrio astronómico.
- `simulacion_ventilacion/`: Diagramas de flujo de ventilación cruzada, estudios de asoleamiento estacional y confort térmico pasivo.
- [`NOTA_DE_DISENO.md`](./NOTA_DE_DISENO.md): Memoria de cálculo bioclimático, transmitancia lumínica y tiro térmico pasivo.
