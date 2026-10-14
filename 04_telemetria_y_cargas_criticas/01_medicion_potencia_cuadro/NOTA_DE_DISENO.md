# Ficha Técnica y Nota de Cálculo: Medición de Potencia Granular en Tableros

## 1. Arquitectura de Medición de Circuitos
- **Medidores Principales de Acometida / Inversor:** Medidor trifásico/bifásico Eastron SDM630 Modbus V2 o módulo de doble canal ATM90E32 conectado vía bus RS-485 blindado con terminación de $120\ \Omega$.
- **Sub-medición de Circuitos Derivados:**
  - Cocina (Horno, Inducción, Refrigerador): Módulos PZEM-004T v3 individuales con transformadores de corriente de núcleo partido $100\text{A}/50\text{mA}$.
  - Climatización (Multi-Split y VMC): Medidores de carril DIN con salida de pulsos e interfaz Modbus RTU.
  - Lavandería y Oficina: CTs dedicados con muestreo de armónicos (THD) para detectar picos inductivos o ruidos de fuentes conmutadas.

## 2. Gateway y Protocolos
- **Microcontrolador Gateway:** Módulo ESP32-WROOM-32U con conector de antena externa o interfaz Ethernet cableada (W5500 / Olimex ESP32-POE).
- **Firmware:** ESPHome con componentes nativos `modbus_controller` y `pzemac`.
- **Frecuencia de Publicación:** Telemetría a $1\text{ Hz}$ local vía MQTT hacia Home Assistant sin nube externa.

*Para la memoria de cálculo completa, consulte [`docs/notas_de_diseno/04_balance_cargas_y_dimensionamiento_energetico.md`](../../docs/notas_de_diseno/04_balance_cargas_y_dimensionamiento_energetico.md).*

