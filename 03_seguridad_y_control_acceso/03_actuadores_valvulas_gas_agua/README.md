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

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
