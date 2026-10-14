# Sistema Solar Térmico, Termotanque y Calefacción por Piso Radiante

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Colector solar de tubos de vacío de borosilicato de 3 capas con tecnología Heat Pipe (resistente a impactos y granizo).
- Estructura de soporte de aluminio anodizado con ajuste de ángulo estacional.
- Termotanque presurizado acumulador (Buffer Tank de 200-300L) con aislamiento térmico de poliuretano expandido y doble serpentín de intercambio de cobre.
- Múltiple colector de distribución de piso radiante con caudalímetros y válvulas de zona.
- Tuberías de cobre o multicapa aisladas térmicamente con coquilla elastomérica de alta temperatura.
- Vaso de expansión cerrado y válvula de seguridad de sobrepresión (3-6 bar).

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Bomba de circulación de alta eficiencia (bomba solar PWM / AC) para el circuito primario.
- Bomba circuladora modulada para el circuito de suelo radiante.
- Válvula mezcladora motorizada proporcional de 3 vías con servomotor 24V/230V.
- Termostato de seguridad y alimentación para caldera auxiliar de respaldo.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Sondas de temperatura PT100 / DS18B20 en cabezal de colector solar, parte superior e inferior del acumulador, y retorno de calefacción.
- Lógica de control diferencial de temperatura (Delta-T) para activación de bomba solar.
- Integración con Home Assistant para conmutación de caldera de apoyo cuando el acumulador solar esté por debajo del setpoint.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
