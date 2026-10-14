# Monitorización y Protección de Cargas en Cocina

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Bases de enchufe empotradas de alta resistencia térmica.
- Carcasa protectora para regulador y mini-UPS de refrigerador.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Línea dedicada C32 con cable de 6 mm² para estufa de inducción y horno eléctrico.
- Línea C20 prioritaria para refrigerador equipada con regulador de voltaje de estado sólido + mini-UPS dedicado.
- Tomas con medición de potencia para lavavajillas, microondas y extractor de aire.
- Dispositivos de supresión de picos (SPD Clase III) en tomas sensibles.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Notificaciones automáticas de fin de ciclo en lavavajillas por caída de potencia residual.
- Alarma de pérdida de alimentación o fluctuación severa de voltaje en el refrigerador.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
