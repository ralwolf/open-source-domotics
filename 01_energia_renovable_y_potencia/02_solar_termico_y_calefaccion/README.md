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
- `mecanico/`:
  - [`esquema_hidraulico_piso_radiante.dxf`](./mecanico/esquema_hidraulico_piso_radiante.dxf): Plano CAD 2D normalizado del esquema de principio hidráulico (P&ID) de la instalación solar térmica, tanque interacumulador de 500L, módulo ACS antiescaldadura y colector de suelo radiante de 6 zonas.
  - [`esquema_hidraulico_piso_radiante.svg`](./mecanico/esquema_hidraulico_piso_radiante.svg): Vista vectorial interactiva a color del circuito hidráulico primario (glicol) y secundario (suelo radiante baja temperatura 35°C).
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`:
  - [`control_diferencial_solar.yaml`](./control/control_diferencial_solar.yaml): Firmware ESPHome para control diferencial solar $\Delta T$ con sondas PT1000, bomba de velocidad variable PWM, protección anti-heladas y control individual de 6 cabezales electrotérmicos de zona.
