# Infraestructura Eléctrica y Monitoreo de Oficina Técnica

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Canaleta técnica de superficie o perfiles bajo escritorio para gestión limpia de cables de datos y potencia.
- Brazo articulado para cámara y suspensión elástica (shock mount) para micrófono capacitivo.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- UPS interactivo o senoidal puro de 800VA - 1200VA para estación de trabajo (PC).
- Filtro de red supresor de ruidos EMI/RFI para evitar interferencias en el micrófono capacitivo y equipo de audio.
- Línea protegida para impresora láser y escáner.
- Tomas inteligentes con desconexión de cargas vampiro al apagar el equipo principal.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Automatización de iluminación de videoconferencia y señalización exterior "En Grabación" sincronizada con la cámara/micrófono.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
