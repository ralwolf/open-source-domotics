# Actuadores de Conmutación de Pared (Micromódulos)

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Instalación dentro de cajas de mecanismos estándar de 65mm de profundidad detrás de las placas convencionales.
- Placas y teclas decorativas físicas convencionales.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Micromódulos inteligentes con y sin neutro (tecnología Zigbee 3.0 / Matter o ESPHome WiFi).
- Contactos de relé de 10A-16A con paso por cero (*zero-crossing*) para protección de lámparas LED.
- Conexión a pulsadores o interruptores conmutados existentes.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Mantenimiento de operación manual 100% funcional si el servidor o la red están apagados.
- Soporte de multiclick (simple, doble, pulsación larga) para escenas globales domóticas.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
