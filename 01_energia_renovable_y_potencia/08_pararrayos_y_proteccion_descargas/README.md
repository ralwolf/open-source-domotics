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

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D (FreeCAD / Open CAD Studio), modelos STL/STEP, tolerancias y anclajes.
- `electrico/`: Diagramas unifilares y esquemas de conexionado (QElectroTech / KiCad), protecciones y lista de materiales (BOM).
- `control/`: Configuraciones YAML de Home Assistant, firmware (ESPHome / Arduino CLI), integraciones locales.
