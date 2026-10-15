# Captación de Agua de Lluvia, Cisterna Subterránea, Presurización y Potabilización

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Red de canalones perimetrales de aluminio/cinc sobredimensionados para lluvias torrenciales.
- Filtro ciclónico y separador de primeras lluvias (First-Flush diverter) para descarte de polvo del tejado.
- Cisterna subterránea de acumulación (capacidad 5.000 L a 10.000 L) con registro estanco, boya de nivel y rebose con válvula antirretorno a drenaje pluvial.
- Tren de filtración mecánica multicapa (filtro de sedimentos de 20 y 5 micras + filtro de carbón activado en bloque).
- Separación física de red de aguas grises (lavamanos, duchas) hacia tanque de decantación previo al biodigestor.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Bomba presurizadora de agua sumergible o de superficie con Variador de Frecuencia (VFD) para presión constante (3 bar) con mínimo consumo.
- Esterilizador por lámpara ultravioleta (UV-C de 55W) con balastro electrónico y horómetro de vida útil.
- Electroválvula de 3 vías de conmutación automática entre agua de cisterna y agua de red pública.
- Alimentación respaldada por la red de emergencia / UPS.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Sensor de nivel de agua hidrostático sumergible (4-20mA) o ultrasónico conectado por ESPHome.
- Lógica en Home Assistant: conmutación a agua de red únicamente si la cisterna pluvial desciende del 10% de capacidad.
- Alerta de cambio de filtros mecánicos y lámpara UV según horas de operación y caudal acumulado.

---

## 5. Estructura y Entregables de este Directorio
- **`mecanico/`**:
  - [`esquema_captacion_potabilizacion_pluvial.dxf`](mecanico/esquema_captacion_potabilizacion_pluvial.dxf): Plano CAD P&ID completo del tren pluvial: captación perimetral, separador de primeras lluvias (First Flush), cisterna subterránea de 10.000 L, bomba sumergible, sedimentador 20µm, carbón activado 5µm, esterilizador UV-C 55W y válvula de 3 vías conmutadora red/pluvial.
  - [`esquema_captacion_potabilizacion_pluvial.svg`](mecanico/esquema_captacion_potabilizacion_pluvial.svg): Diagrama vectorial del sistema pluvial y potabilización.
- **`control/`**:
  - [`monitoreo_cisterna_potabilizacion.yaml`](control/monitoreo_cisterna_potabilizacion.yaml): Configuración ESPHome con sensor de nivel hidrostático 4-20mA, sensor de presión piezorresistivo, conmutación automática cisterna/red, contador horario para vida útil de lámpara UV-C y control de bomba.

