# Lista de Materiales (BOM) - Controlador Diferencial Solar Térmico

| Referencia | Componente | Descripción | Encapsulado | Cantidad | Función Principal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-S3-WROOM-1 | Microcontrolador Dual-Core 240MHz Wi-Fi/BLE con 8MB Flash | SMD RF Module | 1 | Ejecución de algoritmo diferencial ΔT y modulación de bomba |
| **U2** | MAX31865 (x4) | Convertidores digitales de precisión RTD a 15 bits por SPI | SSOP-20 | 4 | Lectura de 4 sondas PT1000 de alta temperatura (-50°C a +200°C) |
| **U3** | LM358 | Amplificador operacional dual rail-to-rail | SOIC-8 | 1 | Acondicionamiento de señal PWM a salida analógica 0-10V |
| **RL1** | Hongfa HF32FV-16 | Relé electromecánico de potencia 16A 250VAC | THT SPDT | 1 | Conmutación de válvula motorizada mezcladora de 3 vías |
| **PS1** | Hi-Link HLK-PM01 | Fuente de alimentación aislada 230VAC a 5VDC 3W | Módulo THT | 1 | Alimentación primaria del módulo en carril DIN |
| **R_REF** | 4.30kΩ 0.1% (x4) | Resistencias de referencia de película metálica ultra-precisión | SMD 0805 | 4 | Referencia de calibración ratiométrica para sondas PT1000 |
| **J1** | Dinkle 5.08mm | Bornero de tornillo enchufable 8 polos | THT 5.08mm | 1 | Conexión de sondas térmicas de inmersión y bomba solar |
