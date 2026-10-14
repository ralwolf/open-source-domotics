# Monitorización y Control de Climatización Multi-Split

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Soportes antivibratorios para unidad condensadora exterior.
- Canaletas de aluminio o PVC para tuberías de cobre frigoríficas y desagües de condensado.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Alimentación exclusiva C16 con cable de 2.5 mm².
- Protector de sobre y bajo voltaje con retardo de reconexión de 3 a 5 minutos para salvaguardar el compresor inverter.
- Medidor de potencia dedicado para calcular el COP y consumo térmico estacional.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Interfaz de control domótico (ESPHome mediante puerto CN105 / Midea UART / pasarela IR bidireccional).
- Modulación de temperatura de consigna y apagado automático si hay ventanas abiertas durante más de 3 minutos.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
