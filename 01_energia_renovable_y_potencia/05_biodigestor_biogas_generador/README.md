# Biodigestor Séptico, Purificación de Biogás y Generación Eléctrica

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Tanque biodigestor anaeróbico modificado para tratamiento de efluentes y lodos orgánicos con cierre hermético.
- Campana o gasómetro de acumulación de baja presión con membrana flexible o sello hidráulico.
- Trampa de condensado y purga de agua en el punto más bajo de la línea de gas.
- Filtro desulfurador de sulfuro de hidrógeno (H2S) con viruta de hierro o carbón activado.
- Columna o trampa de enriquecimiento de metano (separación de CO2).
- Válvula de alivio de presión mecánica calibrada y arrestador de flama (parallamas certificado).

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Motogenerador adaptable a biogás (carburador dual gas/nafta con gobernador de velocidad).
- Electroválvula de corte de biogás normalmente cerrada con certificación ATEX.
- Sensor industrial de presión diferencial piezoeléctrico en línea de gas.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Detectores de gas metano (CH4) instalados en la caseta técnica con interlock de corte físico.
- Monitoreo de presión de gasómetro y producción volumétrica estimada en Home Assistant.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
