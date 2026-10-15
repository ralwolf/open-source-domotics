# Sistema Solar Térmico y Calefacción por Suelo Radiante

## 1. Descripción y Alcance
Este subsistema integra la captación de radiación solar para producción de agua caliente sanitaria (ACS) y calefacción de baja temperatura mediante suelo radiante. Se compone de un campo de captadores de tubos de vacío tipo heat pipe, un acumulador estratificado de 500 litros con serpentines dobles de acero inoxidable AISI 316L, un grupo de bombeo solar de alta eficiencia con modulación electrónica y un controlador diferencial microprocesado de alta precisión.

---

## 2. Entregables Mecánicos y Modelado 3D (`mecanico/`)
- [`colector_termico_estratificacion_3d.FCStd`](./mecanico/colector_termico_estratificacion_3d.FCStd): Modelo paramétrico 3D nativo en FreeCAD 1.1+ del conjunto captador de tubos de vacío heat pipe (30 tubos de borosilicato 58x1800 mm) con soporte inclinado a 45°, depósito acumulador estratificado de 500 L aislado con poliuretano de 50 mm, conexiones hidráulicas de impulsión/retorno y vaso de expansión solar de 24 litros.
- [`colector_termico_estratificacion_3d.step`](./mecanico/colector_termico_estratificacion_3d.step): Archivo neutro STEP AP214 para análisis térmico de fluidos e integración en sala técnica de calderas.
- [`esquema_hidraulico_piso_radiante.dxf`](./mecanico/esquema_hidraulico_piso_radiante.dxf): Plano CAD P&ID 2D normalizado del circuito primario solar con glicol, circuito secundario de estratificación, válvula mezcladora de 3 vías y colectores de distribución de 6 zonas de suelo radiante.
- [`esquema_hidraulico_piso_radiante.svg`](./mecanico/esquema_hidraulico_piso_radiante.svg): Esquema hidráulico interactivo vectorial.

---

## 3. Entregables Eléctricos y Electrónica (`electrico/`)
- [`controlador_diferencial_solar.kicad_sch`](./electrico/controlador_diferencial_solar.kicad_sch): Esquema electrónico profesional en KiCad 10 con microcontrolador ESP32-S3, interfaz cuádruple SPI MAX31865 para lectura ratiométrica de sondas PT1000 de alta temperatura (-50°C a +200°C), driver PWM a 0-10V aislado mediante LM358 para modulación proporcional de caudal de bomba solar, y relé de 16A para válvula de 3 vías.
- [`controlador_diferencial_solar.kicad_pro`](./electrico/controlador_diferencial_solar.kicad_pro): Archivo de proyecto en KiCad 10.
- [`esquema_svg/controlador_diferencial_solar.svg`](./electrico/esquema_svg/controlador_diferencial_solar.svg): Renderizado esquemático vectorial.
- [`BOM.md`](./electrico/BOM.md): Lista completa de materiales y componentes electrónicos con referencias comerciales y tolerancias.

---

## 4. Entregables de Control y Firmware (`control/`)
- [`control_diferencial_solar.yaml`](./control/control_diferencial_solar.yaml): Firmware ESPHome para gestión diferencial del ciclo solar: arranque progresivo de bomba cuando $\Delta T = T_{colector} - T_{tanque\_bajo} \ge 6^\circ\text{C}$, parada de seguridad por estancamiento a $130^\circ\text{C}$, control de válvula motorizada de 3 vías hacia impulsión de suelo radiante y disipación nocturna de excedentes en verano.
