# Telemetría de Potencia y Medición en Cuadro Eléctrico

## 1. Descripción y Alcance
Este subsistema constituye el dispositivo central de adquisición y desagregación de consumo eléctrico para toda la vivienda. Diseñado en formato modular estándar DIN 43880 de 4 módulos (72 mm de anchura), integra microcontrolador ESP32, pantalla OLED frontal, puerto RJ45 para bus RS485 Modbus RTU aislado, hasta 6 canales de medida de corriente mediante pinzas amperimétricas CT sin corte de suministro, y relés de corte para desconexión de cargas secundarias ante sobrecarga del inversor solar.

---

## 2. Entregables Mecánicos y Modelado 3D (`mecanico/`)
- [`gabinete_din_medidor_potencia.FCStd`](./mecanico/gabinete_din_medidor_potencia.FCStd): Modelo paramétrico 3D nativo en FreeCAD 1.1+ de la envolvente modular de carril DIN 4M (72 x 90 x 65 mm), pestaña elástica de anclaje a perfil TS-35, ventana de visualización OLED 0.96", puerto frontal RJ45, pulsadores de navegación y calados para borneros enchufables de 5.08 mm.
- [`gabinete_din_medidor_potencia.step`](./mecanico/gabinete_din_medidor_potencia.step): Archivo de intercambio neutro STEP AP214 para ensamblaje en los cuadros de distribución eléctrica.
- [`plano_medidor_potencia_cuadro.dxf`](./mecanico/plano_medidor_potencia_cuadro.dxf): Plano CAD 2D normalizado con cotas exteriores, alzado frontal y distribución funcional de pines.
- [`plano_medidor_potencia_cuadro.svg`](./mecanico/plano_medidor_potencia_cuadro.svg): Vista vectorial interactiva.

---

## 3. Entregables Eléctricos y Electrónica (`electrico/`)
- [`medidor_potencia_iot.kicad_sch`](./electrico/medidor_potencia_iot.kicad_sch): Esquema electrónico profesional en KiCad 10 con ESP32-WROOM-32, interfaz aislada RS485 (MAX485 + optoacopladores), 4 canales UART para transductores PZEM / CT, fuente interna de 230VAC a 5VDC (HLK-PM01) y relés Omron G5LE.
- [`medidor_potencia_iot.kicad_pro`](./electrico/medidor_potencia_iot.kicad_pro): Proyecto en KiCad 10.
- [`esquema_svg/medidor_potencia_iot.svg`](./electrico/esquema_svg/medidor_potencia_iot.svg): Renderizado esquemático vectorial interactivo.
- [`BOM.md`](./electrico/BOM.md): Lista completa de materiales y componentes.

---

## 4. Entregables de Control y Firmware (`control/`)
- [`esp32_energy_monitor.yaml`](./control/esp32_energy_monitor.yaml): Firmware para ESPHome con lectura Modbus Controller, soporte de pantalla OLED SSD1306 e integración directa en el Energy Dashboard de Home Assistant.
- [`platformio.ini`](./control/platformio.ini) y [`src/main.cpp`](./control/src/main.cpp): Firmware en C++ PlatformIO alternativo con reglas locales de load-shedding autónomas y transmisión MQTT.
- [`NOTA_DE_DISENO.md`](./NOTA_DE_DISENO.md): Memoria de cálculo y criterios de desagregación energética.
