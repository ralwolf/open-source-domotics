# Cargador de Vehículo Eléctrico (Wallbox Inteligente con Solar Diversion)

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Carcasa de punto de recarga Wallbox con grado de protección IP54 contra polvo/lluvia e impacto IK10.
- Soporte mural ergonómico con enrollador de cable y conector Tipo 2 (Mennekes) de 5 a 7 metros.
- Canalización directa en conduit metálico desde el cuadro eléctrico hasta la cochera/estacionamiento.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Circuito de alimentación independiente de 32A (7.4 kW monofásico) o trifásico (11-22 kW) con cableado de 6 mm² a 10 mm².
- Disyuntor magnetotérmico curvo C de 32A/40A exclusivo.
- Interruptor diferencial Clase B o Clase A con módulo de detección de fugas en corriente continua RDC-DD (6mA DC).
- Medidor de energía bidireccional integrado con comunicación Modbus / WiFi.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Integración con Home Assistant mediante protocolo abierto OCPP 1.6J o API local.
- Modulación dinámica de potencia de carga en tiempo real:
- - Modo Solar Puro: carga el vehículo exclusivamente con los excedentes de generación solar y eólica sin tomar energía de la batería del hogar ni de la red.
- - Modo Híbrido Rápido: complementa energía solar con red o generador según tarifas horarias o necesidades del usuario.

---

## 5. Estructura y Entregables de este Directorio
- **`mecanico/`**:
  - [`cargador_ev_wallbox.FCStd`](mecanico/cargador_ev_wallbox.FCStd): Modelo 3D paramétrico FreeCAD de la carcasa Wallbox IP54 / IK10 con receptáculo Tipo 2 (Mennekes IEC 62196-2), aro LED RGB difusor, ventana para OLED/RFID, seta de paro de emergencia y gancho enrollador de cable.
  - [`cargador_ev_wallbox.step`](mecanico/cargador_ev_wallbox.step): Exportación neutra STEP para fabricación y mecanizado.
- **`electrico/`**:
  - [`esquema_ev_wallbox.dxf`](electrico/esquema_ev_wallbox.dxf): Plano CAD unifilar y de maniobra con acometida 230V 32A (3x10mm²), MCB C40A, RCD Tipo B (30mA AC + 6mA DC según IEC 62955), contactor de potencia 40A 2P con contacto auxiliar y bus RS-485.
  - [`esquema_ev_wallbox.svg`](electrico/esquema_ev_wallbox.svg): Diagrama vectorial en alta resolución.
  - [`controlador_ev_wallbox.kicad_pro`](electrico/controlador_ev_wallbox.kicad_pro): Proyecto electrónico KiCad 10.
  - [`controlador_ev_wallbox.kicad_sch`](electrico/controlador_ev_wallbox.kicad_sch): Esquema electrónico KiCad 10 con ESP32-WROOM-32E, circuito analógico CP ±12V PWM 1kHz, sensado ADC de niveles A-F, divisor PP, transceptor aislado ISO3082 y driver para relé de contactor.
  - [`controlador_ev_wallbox.svg`](electrico/esquema_svg/controlador_ev_wallbox.svg): Esquema renderizado con kicad-cli.
  - [`BOM.md`](electrico/BOM.md): Lista detallada de componentes (ICs, semiconductores, transformadores y aparamenta modular de potencia).
- **`control/`**:
  - [`ev_smart_charger.yaml`](control/ev_smart_charger.yaml): Firmware ESPHome con máquina de estados IEC 61851-1, telemetría Modbus de tensión/corriente/energía, selector de consigna dinámica y 3 modos operativos: Solar Puro (cero importación/inyección), Eco Solar (base 6A + excedentes) y Rápido (32A / 7.4 kW).

