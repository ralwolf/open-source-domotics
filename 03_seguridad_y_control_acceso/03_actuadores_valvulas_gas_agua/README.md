# Actuadores Motorizados para Válvulas de Gas y Agua (Corte de Emergencia)

## 1. Descripción y Alcance
Este subsistema proporciona la capacidad de corte electromecánico ultra-rápido (<50 ms por hardware analógico y <10 s mecánico completo) ante fugas de gas combustible (metano/propano) o inundación por rotura de tuberías en puntos neurálgicos como cocina, lavandería y sala de calderas.

---

## 2. Entregables Mecánicos y Modelado 3D (`mecanico/`)
- [`actuador_motorizado_valvula_3d.FCStd`](./mecanico/actuador_motorizado_valvula_3d.FCStd): Modelo paramétrico 3D nativo en FreeCAD 1.1+ del actuador motorizado sobrepuesto IP65 (100 x 70 x 85 mm), motorreductor planetario 12V DC de alto torque (60 kgf·cm), horquilla de arrastre para palancas de válvulas de bola de 1/2", 3/4" y 1", anilla de desembrague manual y soporte metálico ajustable con abrazadera U-Bolt.
- [`actuador_motorizado_valvula_3d.step`](./mecanico/actuador_motorizado_valvula_3d.step): Archivo STEP AP214 universal para simulación cinemática y validación de holguras en baterías de contadores y colectores.
- [`esquema_corte_valvulas_gas_agua.dxf`](./mecanico/esquema_corte_valvulas_gas_agua.dxf): Plano CAD 2D de replanteo mecánico de tuberías y actuadores.
- [`esquema_corte_valvulas_gas_agua.svg`](./mecanico/esquema_corte_valvulas_gas_agua.svg): Esquema funcional vectorial.

---

## 3. Entregables Eléctricos y Electrónica (`electrico/`)
- [`controlador_valvulas_seguridad.kicad_sch`](./electrico/controlador_valvulas_seguridad.kicad_sch): Esquema electrónico en KiCad 10 con microcontrolador ESP32, comparador analógico fail-safe por hardware con histéresis (corte inmediato sin esperar ciclo de CPU), optoacopladores para sondas de agua resistivas, interfaz para sensor catalítico de gas MQ-4 y etapas de potencia en puente H para inversión de polaridad en apertura/cierre de válvulas.
- [`controlador_valvulas_seguridad.kicad_pro`](./electrico/controlador_valvulas_seguridad.kicad_pro): Archivo de proyecto en KiCad 10.
- [`controlador_valvulas_seguridad.svg`](./electrico/esquema_svg/controlador_valvulas_seguridad.svg): Renderizado esquemático interactivo.
- [`BOM.md`](./electrico/BOM.md): Lista completa de componentes y materiales.

---

## 4. Entregables de Control y Firmware (`control/`)
- [`corte_emergencia_gas_agua.yaml`](./control/corte_emergencia_gas_agua.yaml): Firmware para ESPHome con autodiagnóstico periódico (test de carrera mensual para evitar gripado de válvulas de bola por calcificación), telemetría de estado abierto/cerrado por microinterruptores de fin de carrera y reporte a Home Assistant.
