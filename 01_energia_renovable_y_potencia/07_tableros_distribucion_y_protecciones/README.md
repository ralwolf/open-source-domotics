# Tablero Principal de Distribución Eléctrica y Protecciones (Consumer Unit)

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Gabinete para montaje en pared de carril DIN (2 a 4 filas, mínimo 36 a 72 módulos).
- Separación física interna entre sección de potencia (230V) y sección de medición/control.
- Canaletas ranuradas para guiado de cableado de potencia.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Acometida con conductores de fase y neutro de 25 mm².
- Protector contra sobretensiones transitorias y permanentes (DPS Clase II).
- Medidor de energía digital bidireccional en cabecera.
- Interruptor seccionador general bipolar (DP Main Isolator Switch) con puentes de 16 mm².
- Interruptor diferencial general (RCCB / ELCB) de 63A y 30mA de sensibilidad.
- Barras colectoras sólidas de Neutro y Tierra (Earth Bar) conectada a jabalina de puesta a tierra (< 5 ohm).
- Disyuntores termomagnéticos (MCB): C16 Iluminación, C10 Tomas generales, C20 Lavadora, C20 Refrigerador, C20 Calentador eléctrico, C32 Placa/horno de inducción, C16 Climatización, C16 Extractor, C16 Oficina.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Integración de analizadores de energía Modbus / Shelly Pro para medición por circuito en tiempo real.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
