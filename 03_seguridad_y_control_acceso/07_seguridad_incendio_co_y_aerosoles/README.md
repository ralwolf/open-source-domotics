# Seguridad Contra Incendios, Monóxido de Carbono (CO) y Extinción por Aerosol

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Cápsulas generadoras de aerosol condensado de extinción sin agua (Stat-X / FirePro) instaladas dentro del Rack de Servidores IT y del gabinete de baterías LiFePO4.
- Soportes mecánicos con disipador térmico para anclaje en estructura de gabinetes cerrados.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Detectores ópticos fotoeléctricos de humo interconectados en todas las habitaciones, pasillos y áreas comunes (cableados y enlazados por bus seguro).
- Detectores electroquímicos de Monóxido de Carbono (CO) en cocina, cuarto de calderas y caseta de generadores.
- Línea de disparo eléctrico supervisada para la activación de las cápsulas de aerosol mediante módulo de extinción certificado.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Automatización de emergencia en Home Assistant ante alarma de humo/fuego:
- - Apagado automático e inmediato de la ventilación mecánica (VMC) y del aire acondicionado Multi-Split para evitar propagar el oxígeno y humo.
- - Corte inmediato de las electroválvulas de gas natural y tanque estacionario.
- - Levantamiento automático de persianas motorizadas y encendido de luces de cortesía en blanco brillante al 100% para facilitar la evacuación.
- - Activación de sirena de evacuación y envío de notificación crítica al móvil.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D (FreeCAD / Open CAD Studio), modelos STL/STEP, tolerancias y anclajes.
- `electrico/`: Diagramas unifilares y esquemas de conexionado (QElectroTech / KiCad), protecciones y lista de materiales (BOM).
- `control/`: Configuraciones YAML de Home Assistant, firmware (ESPHome / Arduino CLI), integraciones locales.
