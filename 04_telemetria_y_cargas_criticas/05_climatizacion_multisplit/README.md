# Monitorización y Control de Climatización Multi-Split Inverter

Este subsistema comprende la ingeniería mecánica, eléctrica, electrónica y de control para la integración bidireccional de bombas de calor y sistemas de aire acondicionado inverter multi-split mediante bus serie nativo UART (puerto CN105 / Midea), bancada exterior con desacoplo de vibraciones y automatizaciones de ahorro energético vinculadas a excedentes solares y ventanas.

---

## 1. Alcance y Especificaciones Técnicas

### 1.1 Instalación Mecánica y Frigorífica
- **Bancada Exterior Antivibratoria:**
  - Estructura de soporte en escuadra de acero galvanizado fijada a muro portante con 4 amortiguadores cilíndricos cónicos de caucho EPDM (*silentblocks*) con espárrago M8, garantizando un aislamiento de vibraciones mecánicas y resonancias acústicas $\ge 95\%$ hacia la estructura de la vivienda.
- **Tuberías Frigoríficas y Drenaje:**
  - Tuberías de cobre electrolítico desoxidado al fósforo Cu-DHP (línea de líquido $1/4"$, línea de aspiración de gas $3/8"$) aisladas térmicamente de forma independiente con coquilla elastomérica de célula cerrada Armaflex Clase 0 de 13 mm ($\lambda \le 0.033\text{ W/m}\cdot\text{K}$).
  - Tubería de desagüe de condensados en PVC rígido $\varnothing 20\text{ mm}$ tendida con pendiente uniforme $\ge 1.5\%$ canalizada a la red de aguas grises.

### 1.2 Protecciones Eléctricas y Seguridad del Compresor
- Línea de alimentación eléctrica dedicada protegida con magnetotérmico C16 (cable $3 \times 2.5\text{ mm}^2$ libre de halógenos).
- Relé de protección de sobre/subtensión con **retardo de reconexión obligatorio de 3 a 5 minutos**, impidiendo rearranques con el compresor presurizado tras microcortes de la red eléctrica o conmutación del inversor.

### 1.3 Pasarela de Control IoT Bidireccional
- Dispositivo ultra-compacto ($60 \times 40 \times 16\text{ mm}$) instalado en el compartimento interior de la placa base del split sin alterar la estética.
- Conexión directa al conector nativo de la placa base (CN105 de Mitsubishi Electric o CN40 de Midea/Carrier) con aislamiento de niveles lógicos TXS0102 (3.3V a 5V) y alimentación directa desde el bus de 12V del split sin fuentes externas.
- Sensor digital I2C de alta precisión SHT31 ($\pm 0.2\ ^\circ\text{C}$, $\pm 2\%\text{ HR}$) montado a altura de confort (1.5 m) para eliminar el error por estratificación térmica en el techo.

### 1.4 Lógicas de Automatización Energética
- **Interbloqueo con Ventanas:** Si el sensor magnético cableado detecta que la ventana de la habitación permanece abierta más de 3 minutos, el split detiene el compresor automáticamente; al cerrarla, reanuda la consigna previa.
- **Acumulación Térmica por Excedentes Solares:** En verano, cuando el banco de baterías LiFePO4 está lleno ($SOC > 95\%$) y la producción fotovoltaica supera la demanda, la consigna de frío se modula a la baja (ej. 22.5 °C) para almacenar inercia térmica en la masa constructiva de la vivienda sin coste económico.

---

## 2. Entregables Técnicos Generados

| Componente | Tipo de Archivo | Enlaces | Descripción Técnica |
| :--- | :--- | :--- | :--- |
| **Pasarela Split y Bancada** | Modelo 3D CAD | [pasarela_split_iot_y_bancada.FCStd](mecanico/pasarela_split_iot_y_bancada.FCStd)<br>[pasarela_split_iot_y_bancada.step](mecanico/pasarela_split_iot_y_bancada.step) | Ensamble 3D FreeCAD de la pasarela IoT ($60\times40\times16\text{ mm}$) y soporte exterior en escuadra con silentblocks de caucho EPDM. |
| **Plano de Instalación Multi-Split** | Plano 2D CAD | [plano_instalacion_multisplit.svg](mecanico/plano_instalacion_multisplit.svg)<br>[plano_instalacion_multisplit.dxf](mecanico/plano_instalacion_multisplit.dxf) | Sección transversal y esquema de conexionado unifilar: unidad exterior, cuadro C16, líneas frigoríficas 1/4"-3/8", drenaje y sensor de ventana. |
| **Placa PCB Pasarela IoT** | Esquema KiCad 10 | [pasarela_climatizacion_split.kicad_sch](electrico/pasarela_climatizacion_split.kicad_sch)<br>[pasarela_climatizacion_split.svg](electrico/esquema_svg/pasarela_climatizacion_split.svg) | Hardware KiCad 10 con ESP32-C3, convertidor de niveles TXS0102, conector CN105, sensor SHT31, receptor IR 38kHz y entrada optoaislada para ventana. |
| **Lista de Materiales** | Lista BOM | [BOM.md](electrico/BOM.md) | Componentes de la pasarela, conectores JST-PA, transistores, regulador reductor MP1584EN y diodo IR de alta potencia. |
| **Firmware de Control** | Firmware ESPHome | [controlador_climatizacion_split.yaml](control/controlador_climatizacion_split.yaml) | Firmware nativo Home Assistant con integración de termostato inteligente, protección de tiempo mínimo de compresor, retardo por ventana y acumulación solar. |

---

## 3. Scripts de Generación Paramétrica

- `scripts/generar_multisplit_interfaz_3d.py`: Genera el sólido 3D en FreeCAD 1.1+ y exporta en formato neutro STEP AP214.
- `scripts/generar_plano_multisplit.py`: Dibuja el plano de instalación frigorífica y conexionado en DXF R12 y SVG vectorial.
- `scripts/generar_kicad_multisplit.py`: Genera el esquema KiCad 10 y exporta el SVG mediante `kicad-cli`.
