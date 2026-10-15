# Generación Solar Fotovoltaica (PV)

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Racks y rieles de montaje coplanar/triangular de aluminio con anclajes impermeabilizados para techumbre.
- Grapas intermedias y finales de fijación para módulos fotovoltaicos.
- Canalizaciones metálicas tipo conduit galvanizado en intemperie para paso de cables DC.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Módulos solares monocristalinos bifaciales / PERC (ej. 6x 350W+ en serie-paralelo).
- Caja combinadora DC (PV Combiner Box) con fusibles seccionables en ambos polos (+ y -) y supresor de sobretensiones DC (SPD Clase II).
- Cable solar fotovoltaico de 4-6 mm² doblemente aislado con conectores MC4 certificados.
- Inversor híbrido de onda senoidal pura con entradas MPPT.
- Conexión a medidor bidireccional (Net Metering) y varilla de tierra (Ground Rod).

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Telemetría continua de producción instantánea (W), kWh diarios, tensión y corriente de strings vía Modbus TCP/RTU o CAN Bus a Home Assistant.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`:
  - [`esquema_fotovoltaico_ess.dxf`](./electrico/esquema_fotovoltaico_ess.dxf): Plano CAD 2D normalizado del esquema unifilar de 2 strings fotovoltaicos (8.8 kWp), Combiner Box DC con fusibles gPV 15A / DPS 1000V, inversor híbrido 8 kW, banco LiFePO4 48V y salidas AC Grid / EPS Backup.
  - [`esquema_fotovoltaico_ess.svg`](./electrico/esquema_fotovoltaico_ess.svg): Vista vectorial interactiva a color del flujo de energía solar y almacenamiento.
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
- [`NOTA_DE_DISENO.md`](./NOTA_DE_DISENO.md): Memoria de cálculo fotovoltaico, horas de sol pico (HSP) y dimensionamiento de strings.
