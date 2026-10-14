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
- `electrico/`:
  - [`medidor_potencia_iot.kicad_pro`](./electrico/medidor_potencia_iot.kicad_pro) y [`medidor_potencia_iot.kicad_sch`](./electrico/medidor_potencia_iot.kicad_sch): Proyecto y esquema electrónico completo en KiCad 10.0.
  - [`medidor_potencia_iot.svg`](./electrico/esquema_svg/medidor_potencia_iot.svg): Exportación vectorial completa del esquema electrónico.
  - [`BOM.md`](./electrico/BOM.md): Lista completa de materiales y componentes (ESP32, MAX485, PZEM, fuentes HLK-PM01, relés Omron, varistores y TVS).
- `control/`:
  - [`esp32_energy_monitor.yaml`](./control/esp32_energy_monitor.yaml): Configuración lista para compilar y flashear con ESPHome y vinculación nativa a Home Assistant.
  - [`platformio.ini`](./control/platformio.ini) y [`src/main.cpp`](./control/src/main.cpp): Firmware C++ alternativo para PlatformIO con soporte ModbusMaster, PZEM-004T v30, pantalla OLED SSD1306 y MQTT.
- [`NOTA_DE_DISENO.md`](./NOTA_DE_DISENO.md): Ficha técnica y criterios de cálculo para la arquitectura de medición granular.
