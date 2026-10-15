# Lista de Materiales (BOM) - Placa Controladora de Generador de Respaldo y Conmutación ATS

| Ref | Cantidad | Componente / Valor | Encapsulado | Función Técnica | Fabricante / N° de Parte |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **U1** | 1 | ESP32-C3-WROOM-02 (4MB Flash) | SMD Módulo 18x20mm | SoC RISC-V 160MHz con WiFi y BLE para gestión de secuencias de arranque y ATS | Espressif ESP32-C3-WROOM-02-N4 |
| **OK1** | 1 | EL814 / PC814 (Optoacoplador entrada AC) | SOP-4 | Detección inmediata de tensión 230VAC generada para desconectar el motor de arranque | Everlight EL814S |
| **RL1** | 1 | Hongfa HF32FV-16-12-HTF (16A 250VAC) | THT 19x15.5x15mm | Relé de accionamiento de solenoide de arranque térmico (Start) | Hongfa HF32FV-16 |
| **RL2** | 1 | Hongfa HF32FV-16-12-HTF (16A 250VAC) | THT 19x15.5x15mm | Relé de ignición / válvula solenoide de gasolina (Run / Stop) | Hongfa HF32FV-16 |
| **RL3** | 1 | Hongfa HF115F/012-1ZS3A (16A 250VAC) | THT 29x12.7x15.7mm | Relé de comando para motor de conmutación del tablero ATS 63A | Hongfa HF115F |
| **VR1** | 1 | MP1584EN Step-Down 12V $	o$ 3.3V 3A | SOIC-8-1EP | Convertidor buck DC-DC de alta eficiencia alimentado por batería de arranque 12V | Monolithic Power MP1584EN |
| **D1-D3** | 3 | 1N4007 Diodo Supresor | DO-41 | Diodos de libre circulación (flyback) en bobinas de relé de potencia | Diodes Inc. 1N4007 |
| **R_DIV** | 2 | Divisor de tensión 100kΩ / 22kΩ 1% | SMD 0805 | Lectura analógica precisa del voltaje de la batería de 12V (10.0V - 14.8V) | Yageo RC0805 |
| **F1** | 1 | Fusible automotriz tipo cuchilla 5A 32V | Mini Fuse THT | Protección de sobrecorriente en línea de batería de 12V | Littelfuse 0297005.WXNV |
| **J1** | 1 | Bornero tornillo 8 polos paso 5.08mm | PCB Bornier | Bornas para Bat +/-, Start, Ignition, ATS Comando, Sensor Boya, Entrada 230VAC | Phoenix Contact MKDSN 1.5/8 |
