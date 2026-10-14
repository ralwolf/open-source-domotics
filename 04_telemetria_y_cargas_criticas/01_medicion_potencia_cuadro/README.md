# Telemetría de Potencia y Medición en Cuadro Eléctrico

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Montaje en carril DIN dentro del cuadro eléctrico principal.
- Espacio para paso de núcleos de transformadores de corriente (CT).

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Medidores de energía multicanal de carril DIN (Shelly Pro 3EM / Modbus Eastron SDM630 / PZEM).
- Transformadores de corriente de núcleo partido (CT Clamps de 50A / 120A) instalados sin cortar cables.
- Fusible de protección para las tomas de medición de voltaje de referencia.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Monitoreo en tiempo real de voltaje (V), corriente (A), potencia activa (W), potencia reactiva (VAR), factor de potencia y armónicos.
- Transmisión continua por MQTT / Modbus TCP hacia el Energy Dashboard de Home Assistant.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
