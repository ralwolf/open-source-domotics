# Tableros de Distribución Eléctrica y Protecciones (CGMP)

## 1. Descripción y Alcance
Este subsistema define la arquitectura de potencia, corte y protección contra sobretensiones y contactos indirectos para la totalidad de la vivienda domótica. Cumple con la normativa electrotécnica de baja tensión (ITC-BT), integrando envolvente modular de 72 módulos DIN en 4 filas, interruptores magnetotérmicos con poder de corte de 6 kA, diferenciales superinmunizados Clase A (30 mA), descargadores de sobretensiones transitorias y permanentes Tipo 2 con contacto de señalización remota, y supervisión electrónica continua mediante bus Modbus RTU y ESP32-S3.

---

## 2. Entregables Mecánicos y Modelado 3D (`mecanico/`)
- [`gabinete_cuadro_general_mando_proteccion.FCStd`](./mecanico/gabinete_cuadro_general_mando_proteccion.FCStd): Modelo paramétrico 3D nativo en FreeCAD 1.1+ del cuadro modular estanco IP65/IK08 (450 x 750 x 160 mm), puerta reversible en policarbonato ahumado con cerradura de leva, 4 carriles DIN 35x7.5 mm, embarrados de cobre/latón para puesta a tierra (PE) y neutro (N), y troqueles cónicos para pasamuros M25/M32/M40.
- [`gabinete_cuadro_general_mando_proteccion.step`](./mecanico/gabinete_cuadro_general_mando_proteccion.step): Archivo STEP AP214 universal para integración en la maqueta arquitectónica y replanteo de rozas y tubos corrugados.

---

## 3. Entregables Eléctricos y Electrónica (`electrico/`)
- [`cuadro_general_unifilar.dxf`](./electrico/cuadro_general_unifilar.dxf): Plano CAD unifilar 2D normalizado con discriminación de circuitos de fuerza, iluminación, climatización, vehículo eléctrico y cargas críticas respaldadas por SAI.
- [`cuadro_general_unifilar.svg`](./electrico/cuadro_general_unifilar.svg): Esquema unifilar interactivo en formato SVG vectorial.
- [`controlador_telemetria_cuadro_cgmp.kicad_sch`](./electrico/controlador_telemetria_cuadro_cgmp.kicad_sch): Esquema electrónico profesional en KiCad 10 del módulo de supervisión sobre carril DIN con microcontrolador ESP32-S3, sensores de tensión activos ZMPT101B para las 3 fases, optoacopladores para lectura de estado de cartuchos de varistor SPD e interruptor IGA, puerto RS485 para analizador de redes Modbus RTU y relé para bobina de disparo.
- [`controlador_telemetria_cuadro_cgmp.kicad_pro`](./electrico/controlador_telemetria_cuadro_cgmp.kicad_pro): Proyecto electrónico en KiCad 10.
- [`esquema_svg/controlador_telemetria_cuadro_cgmp.svg`](./electrico/esquema_svg/controlador_telemetria_cuadro_cgmp.svg): Renderizado esquemático vectorial.
- [`BOM.md`](./electrico/BOM.md): Lista de componentes electrónicos y aparamenta modular con códigos de pedido.

---

## 4. Entregables de Control y Firmware (`control/`)
- [`controlador_tablero_cgmp.yaml`](./control/controlador_tablero_cgmp.yaml): Firmware ESPHome para adquisición en tiempo real de tensión de red, monitoreo de degradación de varistores del descargador de sobretensiones (alerta temprana antes de tormentas), temperatura del embarrado principal y disparo remoto de emergencia.
