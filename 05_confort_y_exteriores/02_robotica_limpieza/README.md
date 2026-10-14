# Integración de Robots de Limpieza (Aspirado y Trapeado)

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Estación base con rampa de acceso y bahías para tanques de agua limpia, sucia y bolsa de polvo.
- Espacio reservado con ventilación adecuada.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Toma de corriente protegida con medición de consumo (identificación de ciclos de carga y secado de mopas).

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Integración de robot con firmware libre local (Valetudo / MQTT) sin dependencia de servidores cloud.
- Disparo de limpieza automatizada cuando la casa queda desocupada o tras detectar uso continuo de zonas clave.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
