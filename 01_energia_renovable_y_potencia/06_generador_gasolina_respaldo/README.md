# Generador Eléctrico a Gasolina (Respaldo Terciario ATS)

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Cabina exterior insonorizada (insonorización acústica con deflectores de aire).
- Silentblocks y amortiguadores de goma antivibratorios.
- Línea de escape con silenciador orientada hacia el exterior y tanque de combustible con boya.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Generador a gasolina de 5-8 kVA con arranque eléctrico de 12V.
- Cargador de flotación de batería de arranque conectado a la red.
- Tablero de conmutación automática (ATS - Automatic Transfer Switch) con enclavamiento mecánico y eléctrico.
- Protección magnetotérmica y diferencial exclusiva para la salida del grupo.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Módulo de control de arranque por contacto seco comandado por el inversor híbrido o Home Assistant ante SoC < 20%.
- Rutina automática de arranque en vacío periódica para lubricación y verificación operativa.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
