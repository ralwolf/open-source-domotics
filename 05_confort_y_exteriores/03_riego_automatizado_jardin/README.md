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

## 5. Estructura y Entregables de este Directorio
- **`mecanico/`**:
  - [`esquema_hidraulico_riego.dxf`](mecanico/esquema_hidraulico_riego.dxf): Plano CAD del manifold distribuidor de 4 zonas + válvula maestra de seguridad 24VAC, filtro de anillas 120 mesh, caudalímetro de pulsos, tubería matriz PE 32mm y ramales a goteo (setos/macetas), aspersión (césped) y microdifusión (huerto).
  - [`esquema_hidraulico_riego.svg`](mecanico/esquema_hidraulico_riego.svg): Esquema hidráulico vectorial con especificación de caudales y presiones.
- **`electrico/`**:
  - [`controlador_riego_jardin.kicad_pro`](electrico/controlador_riego_jardin.kicad_pro): Proyecto electrónico KiCad 10.
  - [`controlador_riego_jardin.kicad_sch`](electrico/controlador_riego_jardin.kicad_sch): Esquema electrónico KiCad 10 con ESP32-WROOM-32E, 5x Triacs BT136 con optotriacs MOC3041 (cruce por cero), snubbers RC + varistores MOV, 4 canales analógicos para sondas capacitivas de suelo y acondicionamiento de pulsos de caudalímetro.
  - [`controlador_riego_jardin.svg`](electrico/esquema_svg/controlador_riego_jardin.svg): Esquema electrónico exportado con kicad-cli.
  - [`BOM.md`](electrico/BOM.md): Lista completa de materiales y componentes para ensamblaje.
- **`control/`**:
  - [`riego_inteligente_jardin.yaml`](control/riego_inteligente_jardin.yaml): Firmware ESPHome con controlador de aspersores (`sprinkler`), interbloqueo con cisterna pluvial (<15% desactiva riego), predicción de lluvia meteorológica, calibración de sondas de humedad y detección automática de fugas.

