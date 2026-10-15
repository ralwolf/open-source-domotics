# Lista de Materiales (BOM) - Telemetría y Supervisión CGMP

| Referencia | Componente | Descripción | Encapsulado | Cantidad | Función Principal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-S3-WROOM-1 | Microcontrolador Dual-Core 240MHz Wi-Fi/BLE con 8MB Flash | SMD RF Module | 1 | Procesamiento local y telemetría de red eléctrica |
| **U2** | ZMPT101B (x3) | Transformadores de tensión activos de ultra-alta precisión | Módulo PCB THT | 3 | Lectura analógica de tensión RMS en L1, L2 y L3 |
| **U3** | PC817 (x2) | Optoacopladores de aislamiento galvánico 5kV | DIP-8 | 1 | Supervisión de contactos auxiliares de disparo SPD y IGA |
| **U4** | SP3485 | Transceptor diferencial RS485 half-duplex 3.3V | SOIC-8 | 1 | Bus Modbus RTU para integración de analizador de redes MID |
| **PS1** | Hi-Link HLK-PM01 | Fuente conmutada encapsulada 230VAC a 5VDC 3W | Módulo THT | 1 | Alimentación primaria del módulo en carril DIN |
| **RL1** | Hongfa HF32FV-G | Relé de alta capacidad 16A 250VAC | THT SPST | 1 | Disparo de bobina de emisión por sobretensión persistente |
| **J2** | DS18B20 | Sonda de temperatura digital 1-Wire TO-92 | Conector 3 pines | 1 | Termometría de contacto en embarrado principal de cobre |
| **J1** | Dinkle 5.08mm | Bornero de tornillo enchufable 8 polos | THT 5.08mm | 1 | Conexiones de señal externa, RS485 y contactos secos |
| **MOV1-3** | S14K275 | Varistores de óxido metálico de protección fina secundaria | Radial 14mm | 3 | Supresión de micro-sobretensiones en entradas de medida |
