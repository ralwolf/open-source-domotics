# Iluminación Modulada Circadiana y Control Exterior

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Perfiles de aluminio disipador con difusores opalinos para tiras LED.
- Luminarias exteriores estancas con clasificación IP65/IP66.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Fuentes de alimentación conmutadas Mean Well de 24V DC con certificación SELV.
- Dimmers multicanal PWM de alta frecuencia (>1kHz) libres de parpadeo (flicker-free).
- Sensores de presencia por ondas milimétricas (mmWave 24GHz/60GHz) de bajo voltaje.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Curva circadiana automática: ajuste de temperatura de color (2700K a 5000K) y brillo según la posición solar.
- Iluminación exterior perimetral interactiva: modo tenue (20%) que asciende al 100% de forma suave al detectar personas con las cámaras.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
