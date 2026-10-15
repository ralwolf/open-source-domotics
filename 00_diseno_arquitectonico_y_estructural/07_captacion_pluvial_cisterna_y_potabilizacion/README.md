# Captación Pluvial, Cisterna y Sistema de Potabilización UV-C

## 1. Descripción y Alcance
Este subsistema asegura la autonomía hídrica de la vivienda recolectando el agua de lluvia procedente de las cubiertas y terrazas, prefiltrándola mediante separación centrífuga de hojas y partículas gruesas, almacenándola en una cisterna subterránea de 10.000 litros y acondicionándola para uso sanitario y potable mediante un skid de filtración de 3 etapas y esterilización germicida por radiación ultravioleta UV-C.

---

## 2. Entregables Mecánicos y Modelado 3D (`mecanico/`)
- [`cisterna_y_skid_potabilizacion_3d.FCStd`](./mecanico/cisterna_y_skid_potabilizacion_3d.FCStd): Modelo paramétrico 3D nativo en FreeCAD 1.1+ de la cisterna subterránea de 10.000 L (Ø2400 x 2600 mm) con registro DN600 y tapa de fundición B125, filtro vórtex centrífugo de bajante, y bancada metálica antivibratoria para el skid de potabilización con bomba vertical multietapa, 3 vasos portacartuchos Big Blue 10" y reactor de desinfección UV-C en acero inoxidable AISI 304 (55W).
- [`cisterna_y_skid_potabilizacion_3d.step`](./mecanico/cisterna_y_skid_potabilizacion_3d.step): Archivo STEP AP214 universal para replanteo de excavación civil y conexionado de tuberías.
- [`esquema_captacion_potabilizacion_pluvial.dxf`](./mecanico/esquema_captacion_potabilizacion_pluvial.dxf): Plano CAD P&ID 2D de la línea de captación, decantación de primeros litros (*first flush*), almacenamiento, bombeo presurizado y desinfección bacteriológica.
- [`esquema_captacion_potabilizacion_pluvial.svg`](./mecanico/esquema_captacion_potabilizacion_pluvial.svg): Esquema hidráulico interactivo vectorial.

---

## 3. Entregables Eléctricos y Electrónica (`electrico/`)
- [`controlador_potabilizacion_pluvial.kicad_sch`](./electrico/controlador_potabilizacion_pluvial.kicad_sch): Esquema electrónico profesional en KiCad 10 con microcontrolador ESP32-S3, interfaz para sensor de nivel ultrasónico estanco JSN-SR04T, receptor de bucle de corriente 4-20mA para transductor de presión de red de 0-6 bar, circuito optoacoplado de monitoreo de corriente del balastro UV-C (alerta de fallo de lámpara germicida) y relé de 16A para contactor de electrobomba.
- [`controlador_potabilizacion_pluvial.kicad_pro`](./electrico/controlador_potabilizacion_pluvial.kicad_pro): Proyecto en KiCad 10.
- [`esquema_svg/controlador_potabilizacion_pluvial.svg`](./electrico/esquema_svg/controlador_potabilizacion_pluvial.svg): Renderizado esquemático vectorial.
- [`BOM.md`](./electrico/BOM.md): Lista completa de materiales y componentes para el skid y su electrónica de control.

---

## 4. Entregables de Control y Firmware (`control/`)
- [`monitoreo_cisterna_potabilizacion.yaml`](./control/monitoreo_cisterna_potabilizacion.yaml): Firmware ESPHome para cálculo de volumen en litros y porcentaje de llenado de la cisterna con filtrado de eco acústico, vigilancia de presión de servicio en bar, enclavamiento de bomba ante nivel bajo crítico (protección contra marcha en seco) y supervisión del estado de desinfección UV-C.
