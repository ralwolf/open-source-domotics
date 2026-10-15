# Lista de Materiales (BOM) - Monitorización de Cargas de Cocina y Mini-UPS Refrigerador

| Ref | Cantidad | Componente / Valor | Encapsulado | Función Técnica | Fabricante / N° de Parte |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **U1** | 1 | ESP32-C3-WROOM-02 (4MB Flash) | SMD Módulo 18x20mm | SoC RISC-V 160MHz con WiFi 802.11 b/g/n y Bluetooth 5.0 LE | Espressif ESP32-C3-WROOM-02-N4 |
| **U2, U3** | 2 | BL0942 (Metrología Energética UART) | SSOP-10 | Medición de potencia activa (W), tensión RMS (V) y corriente (A) para refrigerador y lavavajillas | Shanghai Belling BL0942 |
| **U4** | 1 | INA219AIDR (Monitor I2C Corriente/Tensión) | SOIC-8 | Monitoreo bidireccional del estado de carga y salud de la batería LiFePO4 de 12.8V | Texas Instruments INA219 |
| **PS1** | 1 | HLK-2M03 (AC/DC Aislado 3.3V 600mA) | Módulo 28x14x16mm | Fuente de alimentación auxiliar de lógica de control conectada a red | Hi-Link HLK-2M03 |
| **RL1** | 1 | Hongfa HF115F/012-1ZS3A (16A 250VAC) | THT 29x12.7x15.7mm | Relé de transferencia ultrarrápida (<10ms) de alimentación AC a inversor de batería | Hongfa HF115F |
| **R_SH1, R_SH2** | 2 | Shunt Manganina 1 mΩ 3W 1% | SMD 2512 | Resistencias derivadoras para lectura precisa de corriente sin caída apreciable | Vishay WSL25121L000FEA |
| **MOV1-MOV3** | 3 | Varistor 14D471K (470V 4.5kA) | Disco 14mm THT | Supresor de sobretensiones transitorias SPD Clase III en las tomas críticas | Epcos B72214S0301K101 |
| **J1** | 1 | Bornero tornillo 6 polos paso 5.08mm | PCB Bornier | Conexiones de entrada Red AC, salida Refrig, salida Lavavajillas, neutros y tierra | Phoenix Contact MKDSN 1.5/6 |
