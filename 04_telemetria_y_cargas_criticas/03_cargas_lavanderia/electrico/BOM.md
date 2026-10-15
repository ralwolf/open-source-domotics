# Lista de Materiales (BOM) - Monitorización y Seguridad Anti-Inundación en Lavandería

| Ref | Cantidad | Componente / Valor | Encapsulado | Función Técnica | Fabricante / N° de Parte |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **U1** | 1 | ESP32-C3-WROOM-02 (4MB Flash) | SMD Módulo 18x20mm | SoC RISC-V 160MHz con WiFi 802.11 b/g/n y Bluetooth 5.0 LE | Espressif ESP32-C3-WROOM-02-N4 |
| **U2** | 1 | BL0942 (Metrología Energética UART) | SSOP-10 | Medición de potencia activa (W), tensión RMS (V) y corriente (A) hasta 16A continuo | Shanghai Belling BL0942 |
| **U3** | 1 | ADXL345 (Acelerómetro Digital 3 Ejes I2C) | LGA-14 | Monitoreo de vibraciones mecánicas y detección de desbalance de tambor a 1400 RPM | Analog Devices ADXL345 |
| **OK1** | 1 | PC817 Optoacoplador | SOP-4 | Aislamiento galvánico de la sonda de inundación de suelo | Sharp PC817X |
| **Q1** | 1 | AOD4184A N-Channel MOSFET 40V 50A | TO-252 | Driver de potencia para actuador/electroválvula de corte de agua 12V 1.5A | Alpha & Omega AOD4184A |
| **D1** | 1 | 1N5408 Diodo Flyback 3A 1000V | DO-201AD | Supresor de picos inductivos de la bobina de la electroválvula solenoide de agua | Vishay 1N5408 |
| **RL1** | 1 | Hongfa HF32FV-16-12-HTF (16A 250VAC) | THT 19x15.5x15mm | Relé de corte para desenergizar el enchufe de lavadora/secadora ante inundación | Hongfa HF32FV-16 |
| **PS1** | 1 | HLK-2M03 (AC/DC Aislado 3.3V 600mA) | Módulo 28x14x16mm | Fuente conmutada compacta entrada 85-264VAC, salida 3.3V DC aislada galvánicamente | Hi-Link HLK-2M03 |
| **MOV1** | 1 | Varistor 14D471K (470V 4.5kA) | Disco 14mm THT | Supresión de sobretensiones transitorias SPD Clase III en línea de lavadora | Epcos B72214S0301K101 |
| **J1** | 1 | Bornero tornillo 6 polos paso 5.08mm | PCB Bornier | Bornas para Red L/N, Carga L_OUT, Sonda Agua, Salida 12V Válvula Agua | Phoenix Contact MKDSN 1.5/6 |
