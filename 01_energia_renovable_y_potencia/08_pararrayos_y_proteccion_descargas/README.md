# Sistema de Pararrayos y Protección Atmosférica Integral

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Cabezal captador de pararrayos con dispositivo de cebado (PDC ionizante con avance de cebado delta-t >= 45 microsegundos) o punta Franklin según radio de protección calculado.
- Mástil soporte de acero galvanizado fijado en la torre del aerogenerador o punto más alto de la vivienda.
- Conductor de bajada exterior de cobre desnudo de 50-70 mm² o platina de cobre fijada con aisladores cerámicos.
- Tubo de protección mecánica en los últimos 2.5 metros antes del suelo y arqueta de registro equipotencial.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Malla de puesta a tierra dedicada del pararrayos compuesta por 3 picas de cobre de 2 metros en triangulación con compuesto mineral mejorador de conductividad (resistencia < 5 ohmios).
- Vía de chispas (Spark Gap) de unión equipotencial entre la tierra del pararrayos y la tierra eléctrica general.
- Descargadores de sobretensiones transitorias Tipo 1 (Iimp >= 25 kA por polo, 10/350 microsegundos) instalados en la cabecera del cuadro general de distribución.
- Contador electromecánico/digital de impactos de rayo en el conductor de bajada.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Sensor inductivo de impacto de descarga atmosférica conectado a Home Assistant.
- Disparo de alerta de inspección preventiva tras una tormenta eléctrica para comprobar el estado de los cartuchos descargadores de sobretensión.

---

## 5. Estructura y Entregables de este Directorio
- **`mecanico/`**:
  - [`pararrayos_pdc_mastil.FCStd`](mecanico/pararrayos_pdc_mastil.FCStd): Modelo 3D FreeCAD del cabezal ionizador PDC con avance de cebado $\Delta t \ge 45\ \mu\text{s}$, mástil de acero inoxidable 3 m, abrazaderas de fijación, bajante de cobre exterior y arqueta con pica de tierra.
  - [`pararrayos_pdc_mastil.step`](mecanico/pararrayos_pdc_mastil.step): Exportación neutra STEP para fabricación.
- **`electrico/`**:
  - [`esquema_pararrayos_tierras.dxf`](electrico/esquema_pararrayos_tierras.dxf): Plano CAD de equipotencialidad, bajante de cobre 50 mm², malla de tierras triangulada (3 picas de 2m a 4m de distancia con compuesto mejorador para $R \le 5\ \Omega$), vía de chispas (Spark Gap 100 kA 10/350µs) unida a la barra BEP y descargadores combinados DPS Tipo 1+2 en el cuadro TGBT.
  - [`esquema_pararrayos_tierras.svg`](electrico/esquema_pararrayos_tierras.svg): Diagrama esquemático vectorial de protección atmosférica y tierras.
  - [`contador_rayos_iot.kicad_pro`](electrico/contador_rayos_iot.kicad_pro): Proyecto electrónico KiCad 10.
  - [`contador_rayos_iot.kicad_sch`](electrico/contador_rayos_iot.kicad_sch): Esquema electrónico KiCad 10 con ESP32, entrada para bobina toroidal/Rogowski, comparador LM393 con umbral de 500 A, optoacopladores para supervisión de cartuchos DPS Tipo 1 y 2, y cargador solar TP4056 con batería 18650.
  - [`contador_rayos_iot.svg`](electrico/esquema_svg/contador_rayos_iot.svg): Esquema renderizado mediante kicad-cli.
  - [`BOM.md`](electrico/BOM.md): Lista completa de materiales de protección externa e interna.
- **`control/`**:
  - [`contador_descargas_atmosfericas.yaml`](control/contador_descargas_atmosfericas.yaml): Firmware ESPHome con contador de pulsos de descarga por hardware, registro acumulativo en Home Assistant y alertas críticas inmediatas ante disparo de cartuchos DPS o impacto de rayo directo.

