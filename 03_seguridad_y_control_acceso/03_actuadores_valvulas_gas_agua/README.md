# Actuadores y Electroválvulas de Seguridad para Agua y Gas

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Válvula de bola para línea general de agua con actuador motorizado de cuarto de vuelta.
- Electroválvula de gas certificada normalmente cerrada con rearme manual seguro.
- Soportes mecánicos de montaje en tubería resistentes a vibraciones.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Actuadores motorizados de 12V/24V con retorno por resorte o enclavamiento biestable.
- Sensores cableados de inundación e inflamabilidad con relé directo hacia el actuador (enlace de hardware sin depender de red).
- Alimentación respaldada por la red de emergencia / UPS.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Integración a Home Assistant con corte de agua inmediato ante detección de humedad en baños, cocina o lavandería.
- Corte de gas y corte eléctrico de circuitos adyacentes ante detección de metano o gas LP.

---

## 5. Estructura y Entregables de este Directorio
- **`mecanico/`**:
  - [`esquema_corte_valvulas_gas_agua.dxf`](mecanico/esquema_corte_valvulas_gas_agua.dxf): Plano CAD de tuberías, válvulas motorizadas de bola 1", electroválvula de gas normalmente cerrada con rearme manual, y sensores de fuga.
  - [`esquema_corte_valvulas_gas_agua.svg`](mecanico/esquema_corte_valvulas_gas_agua.svg): Render vectorial del esquema de seguridad de gas y agua.
- **`electrico/`**:
  - [`controlador_valvulas_seguridad.kicad_pro`](electrico/controlador_valvulas_seguridad.kicad_pro): Proyecto KiCad 10.
  - [`controlador_valvulas_seguridad.kicad_sch`](electrico/controlador_valvulas_seguridad.kicad_sch): Esquema electrónico KiCad 10 con ESP32, optoacopladores para sondas cableadas de agua, sensor MQ-4/MQ-2 gas, mosfets/relés para actuadores 12V e interbloqueo analógico fail-safe por hardware.
  - [`controlador_valvulas_seguridad.svg`](electrico/controlador_valvulas_seguridad.svg): Esquema electrónico renderizado en SVG.
  - [`BOM.md`](electrico/BOM.md): Lista detallada de componentes (ESP32, PC817, relés 10A, fusibles automotrices 2A, convertidor Buck MP1584, borneros tornillo).
- **`control/`**:
  - [`corte_emergencia_gas_agua.yaml`](control/corte_emergencia_gas_agua.yaml): Configuración ESPHome con corte autónomo local inmediato (<50ms) sin depender de WiFi/Home Assistant, telemetría de fugas y sirena piezoeléctrica local.

