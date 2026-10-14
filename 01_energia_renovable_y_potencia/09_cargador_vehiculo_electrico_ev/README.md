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

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D (FreeCAD / Open CAD Studio), modelos STL/STEP, tolerancias y anclajes.
- `electrico/`: Diagramas unifilares y esquemas de conexionado (QElectroTech / KiCad), protecciones y lista de materiales (BOM).
- `control/`: Configuraciones YAML de Home Assistant, firmware (ESPHome / Arduino CLI), integraciones locales.
