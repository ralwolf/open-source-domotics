# Motorización y Control de Cortinas y Persianas

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Motores tubulares cilíndricos para eje octogonal de persiana enrollable con adaptadores de fricción.
- Rieles motorizados con correa de tracción reforzada con alambre de acero para cortinas pesadas.
- Soportes mecánicos a dintel o techo.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Motores de 230V AC con finales de carrera mecánicos/electrónicos o motores de 24V DC.
- Módulos de relé doble con interbloqueo electrónico (*interlock*) para evitar activación simultánea de subida y bajada.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Calibración de tiempo de recorrido y posicionamiento porcentual (0 a 100%) en Home Assistant.
- Automatización por azimuth y elevación solar para control térmico estacional.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
