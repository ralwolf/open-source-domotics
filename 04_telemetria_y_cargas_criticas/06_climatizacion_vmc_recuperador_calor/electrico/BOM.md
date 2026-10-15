# Lista de Materiales (BOM) - Placa Controladora de VMC con Recuperador Entálpico

| Ref | Cantidad | Componente / Valor | Encapsulado | Función Técnica | Fabricante / N° de Parte |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **U1** | 1 | ESP32-S3-WROOM-1 (8MB Flash) | SMD Módulo 18x25.5mm | Microcontrolador central Dual-Core 240MHz, WiFi, BLE, FreeRTOS | Espressif ESP32-S3-WROOM-1-N8 |
| **U2** | 2 | MCP4725A0T-E/CH (DAC 12-bit I2C) | SOT-23-6 | Generador de tensión analógica precisa 0 a 3.3V para control de velocidad | Microchip MCP4725 |
| **U3** | 1 | LM358DR (Op-Amp Rail-to-Rail) | SOIC-8 | Amplificador no inversor ganancia $G=3.03$ para convertir $0-3.3	ext{V} 	o 0-10	ext{V}$ EC | Texas Instruments LM358DR |
| **U4** | 1 | DRV8871DDAR (Puente H 3.6A 45V) | SOIC-8-1EP | Driver PWM para actuador reversible 24V de compuerta bypass Free-Cooling | Texas Instruments DRV8871 |
| **OK1-OK2** | 2 | PC817 Optoacoplador | DIP-4 | Aislamiento galvánico 5kV para lectura tacométrica (TACH) de RPM de motores EC | Sharp PC817X |
| **SEN1** | 1 | Sensirion SDP810-500Pa | Montaje placa con toberas | Sensor de presión diferencial I2C de ultra-precisión para colmatación de filtros | Sensirion SDP810-500Pa |
| **SEN2** | 1 | Sensirion SCD41 (NDIR CO2 + RH + T) | SMD 10.1x10.1mm | Sensor fotoacústico de CO2 (400-5000 ppm) y HR interior | Sensirion SCD41 |
| **TH1-TH4** | 4 | DS18B20 / NTC 10k 1% | Sondas encapsuladas AISI316 | Monitoreo de 4 temperaturas: T_exterior, T_impulsión, T_extracción, T_expulsión | Dallas/Maxim DS18B20 |
| **VR1** | 1 | MP1584EN Step-Down 24V $	o$ 5V 3A | SOIC-8-1EP | Convertidor buck DC-DC síncrono de alta eficiencia (>92%) | Monolithic Power MP1584EN |
| **VR2** | 1 | AMS1117-3.3 LDO | SOT-223 | Regulador lineal ultra-bajo ruido para lógica 3.3V y sensores I2C | Diodes Inc. AMS1117-3.3 |
| **J1-J4** | 4 | Borneros de tornillo paso 5.08mm | PCB Bornier 4P/3P | Conexión para motores EC (24V, GND, 0-10V, TACH) y actuador Belimo | Phoenix Contact MKDSN |
| **F1** | 1 | Fusible rearmable PTC Polyswitch 30V 2A | SMD 2920 | Protección contra sobrecorrientes en línea de alimentación y bypass | Littelfuse 2920L200 |
