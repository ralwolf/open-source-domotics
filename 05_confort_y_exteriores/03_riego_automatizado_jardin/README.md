# Automatización del Sistema de Riego para Plantas y Jardín

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Arqueta de riego enterrada de polietileno con tapa reforzada.
- Múltiple colector de electroválvulas con filtro de anillas/malla de entrada.
- Tuberías de polietileno agrícola (PE) de 25mm / 16mm y emisores de goteo/aspersores.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Electroválvulas de solenoide de 24V AC o 12V DC normalmente cerradas.
- Transformador de aislamiento galvánico de 230V a 24V AC.
- Módulo de control de relés con aislamiento optoacoplado comandado por ESPHome / OpenSprinkler.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Sensores de humedad de suelo capacitivos anticorrosión conectados a la pasarela.
- Algoritmo de riego inteligente: omisión automática de riego si las previsiones meteorológicas indican lluvia en las siguientes 12-24 horas.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
