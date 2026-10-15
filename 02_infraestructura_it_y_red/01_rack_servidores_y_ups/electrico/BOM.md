# Lista de Materiales (BOM) - Controlador Ambiental y PDU Rack 19"

| Referencia | Componente | Descripción | Encapsulado | Cantidad | Función Principal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-S3-WROOM-1 | Microcontrolador Dual-Core 240MHz Wi-Fi/BLE con 8MB Flash | SMD RF Module | 1 | Procesamiento local y enlace ESPHome/MQTT |
| **U2** | SHT31-DIS | Sensor digital precisión I2C (±1.5% RH, ±0.2°C) | DFN-8 | 1 | Telemetría higrométrica de admisión frontal |
| **J2** | DS18B20 (x2) | Sensores térmicos 1-Wire encapsulados en acero inoxidable | Cabezal 1x3 THT | 2 | Monitoreo térmico directo en tobera de escape y SAI |
| **PS1** | Mean Well IRM-10-12 | Fuente AC/DC conmutada compacta 230VAC a 12VDC 0.85A | Módulo THT | 1 | Alimentación autónoma aislada 4kV del controlador |
| **Q1** | IRLZ44N | MOSFET N-Channel Logic Level 55V 47A RDS(on) 28mΩ | TO-220-3 | 1 | Modulación PWM silenciosa de ventiladores de techo 12V |
| **RL1** | Omron G5LE-1-DC12 | Relé electromecánico 12VDC bobina, 10A 250VAC contactos | THT SPDT | 1 | Conmutación de tira LED interior al abrir puerta |
| **J3** | SCT-013-000 | Transformador de corriente de núcleo partido 100A:50mA | Jack 3.5mm hembra | 1 | Medición de consumo RMS de la PDU sin interrumpir servicio |
| **J1** | Dinkle 5.08mm | Bornero de tornillo enchufable 8 polos | THT 5.08mm | 1 | Interfaz reed switches magnéticos puerta y ventiladores |
| **BZ1** | Piezo Buzzer 5V | Transductor piezoeléctrico acústico 85dB | THT 12mm | 1 | Alarma sonora por sobrecalentamiento o puerta abierta >2min |
| **R1-R4** | 4.7kΩ, 10kΩ, 22Ω | Resistencias de pull-up 1-Wire/I2C y carga burden CT | SMD 0805 | 6 | Acondicionamiento de señales y bus digital |
| **C1-C4** | 100nF, 10µF, 470µF | Condensadores cerámicos y electrolítico bajo ESR | 0805 / Radial | 5 | Desacoplo y filtrado de rizado de alimentación |
