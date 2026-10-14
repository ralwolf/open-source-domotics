# Aerogenerador Helicoidal Archimedes Adaptable Wind Turbine MK9

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Rotor helicoidal tipo tornillo de Arquímedes MK9 (diámetro y paso optimizado para bajas velocidades de viento).
- Eje central con rodamientos sellados de baja fricción y brida de montaje mecanizada.
- Mástil o torre arriostrada con soporte antivibratorio y amortiguadores de torsión.
- Carenado o cono aerodinámico de protección contra intemperie.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Generador síncrono de imanes permanentes (PMSG) trifásico AC.
- Puente rectificador de onda completa de diodos Schottky de baja pérdida.
- Controlador de carga MPPT eólico con entrada para freno electrónico (Dump Load).
- Banco de resistencias de frenado de disipación de calor para sobrevelocidad.
- Interruptor seccionador manual de corte y cableado apantallado hacia el banco de baterías.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Sensor óptico o inductivo de RPM de rotor.
- Medición de voltaje y corriente DC/AC integrada a Home Assistant (ESPHome / Modbus RS485).
- Automatización de parada segura por ráfagas superiores a velocidad crítica (>60 km/h).

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
