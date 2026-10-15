# Lista de Materiales (BOM) - Caja Combinadora y Telemetría Solar PV

| Referencia | Componente | Descripción | Encapsulado | Cantidad | Función Principal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-S3-WROOM-1 | Microcontrolador Wi-Fi/BLE Dual Core 240MHz 8MB Flash | SMD RF Module | 1 | Cálculo de potencia DC, algoritmo MPPT y enlace ESPHome |
| **U2** | ACS758LCB-050B-PFF-T | Sensor de corriente por efecto Hall galvanicamente aislado 50A | Allegro CB PFF | 1 | Medición bidireccional continua de amperaje del string fotovoltaico |
| **U3** | PC817 | Optoacoplador de aislamiento 5kV | DIP-4 | 1 | Supervisión del contacto auxiliar del descargador SPD DC |
| **U4** | SHT31-DIS | Sensor digital de temperatura y humedad (±0.2°C) | DFN-8 | 1 | Telemetría térmica de cara posterior para cálculo de pérdidas térmicas |
| **SPD1** | SPD DC Tipo II | Protector contra sobretensiones transitorias 1000V DC 40kA | Carril DIN 2M | 1 | Desvío seguro a tierra de inducciones de rayo en strings |
| **F1-F2** | gPV 10x38 15A 1000V | Fusibles cerámicos especiales para protección fotovoltaica | Cilindro 10x38mm | 2 | Protección contra corrientes inversas de defecto |
| **PS1** | Hi-Link HLK-PM01 | Convertidor conmutado 230VAC a 5VDC 3W | Módulo THT | 1 | Alimentación electrónica interna del combinador |
| **R1-R6** | 1MΩ 1% 250V (x6) | Cadena de resistencias de alta tensión para divisor | SMD 1206 | 6 | Reducción de escala de tensión DC hasta 600V para entrada ADC |
| **R7** | 33kΩ 0.1% | Resistencia de precisión parte baja divisor | SMD 0805 | 1 | Ajuste fino de ganancia de lectura de tensión DC |
| **J1** | Phoenix Contact 7.62mm | Bornero de potencia para cable solar de 6 mm² (PV1-F) | THT 7.62mm | 1 | Entrada y salida de strings fotovoltaicos |
