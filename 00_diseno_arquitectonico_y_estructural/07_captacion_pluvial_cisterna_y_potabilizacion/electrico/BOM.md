# Lista de Materiales (BOM) - Controlador Cisterna y Skid Potabilización

| Referencia | Componente | Descripción | Encapsulado | Cantidad | Función Principal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-S3-WROOM-1 | Microcontrolador Dual-Core 240MHz Wi-Fi/BLE con 8MB Flash | SMD RF Module | 1 | Telemetría de nivel pluvial, gestión de presión y esterilización |
| **U2** | JSN-SR04T | Sensor de distancia ultrasónico estanco IP67 con sonda cableada | Módulo PCB | 1 | Medición sin contacto de nivel de agua en cisterna (20 cm a 450 cm) |
| **U3** | RCV420 / Shunt 150Ω | Receptor de bucle de corriente 4-20mA de precisión con filtro | SOIC-8 | 1 | Interfaz para transductor de presión hidrostática de línea (0-6 bar) |
| **U4** | PC817 | Optoacoplador de aislamiento galvánico 5kV | DIP-4 | 1 | Supervisión del estado operativo del balastro de la lámpara UV-C |
| **RL1** | Hongfa HF32FV-16 | Relé electromecánico de potencia 16A 250VAC | THT SPST | 1 | Conmutación de contactor de la electrobomba de presurización |
| **PS1** | Hi-Link HLK-PM01 | Fuente compacta 230VAC a 5VDC 3W | Módulo THT | 1 | Alimentación de bajo consumo para lógica electrónica |
| **J1** | Dinkle 5.08mm | Bornero de tornillo enchufable 8 polos | THT 5.08mm | 1 | Conexión de alimentación, sensores analógicos y bomba |
