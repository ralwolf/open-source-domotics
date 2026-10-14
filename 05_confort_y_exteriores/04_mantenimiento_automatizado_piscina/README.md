# Automatización, Filtrado y Mantenimiento Químico de Piscina

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Caseta técnica de piscina ventilada e impermeable.
- Bomba de recirculación autoaspirante y filtro de lecho de arena/vidrio con válvula de 6 vías.
- Soporte y enchufe para robot limpiafondos automático.
- Cámara de análisis en bypass con portasondas para electrodos de pH y ORP.
- Inyección de químicos mediante collarines de toma en tubería de impulsión de PVC.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Cuadro eléctrico de piscina con diferencial de alta sensibilidad (10mA) y contactores para bombas.
- Bombas dosificadoras peristálticas de 12V/24V para corrector de pH y desinfectante.
- Sensor ultrasónico o sensor de presión hidrostática para medición de nivel de agua y electroválvula de llenado.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Filtrado inteligente coordinado con las horas de exceso de generación solar fotovoltaica.
- Dosificación automática de productos químicos según lecturas continuas de sondas de pH y Redox (ORP) en Home Assistant.
- Protección de la bomba contra funcionamiento en seco.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
