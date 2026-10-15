# Lista de Materiales (BOM) - Amplificador Digital Streaming Clase D Hi-Fi

| Ref | Cantidad | Componente / Valor | Encapsulado | Función Técnica | Fabricante / N° de Parte |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **U1** | 1 | ESP32-S3-WROOM-1 (8MB PSRAM, 16MB Flash) | SMD Módulo 18x25.5mm | Procesador Dual-Core 240MHz con soporte de buffers Hi-Res y protocolos Squeezelite/Snapcast | Espressif ESP32-S3-WROOM-1-N16R8 |
| **U2** | 1 | Texas Instruments TAS5805MPWPR | TSSOP-28 | Amplificador digital estéreo Clase D, entrada direct-digital I2S, DSP integrado, 2x25W RMS | Texas Instruments TAS5805M |
| **VR1** | 1 | TPS7A4700 (LDO Ultra-Bajo Ruido 4.17µV) | QFN-20 | Regulador lineal de muy bajo ruido para la alimentación del reloj y sección de audio sensible | Texas Instruments TPS7A4700 |
| **VR2** | 1 | MP1584EN Step-Down 24V $	o$ 5V 3A | SOIC-8-1EP | Convertidor buck DC-DC síncrono para alimentación general de placa | Monolithic Power MP1584EN |
| **L1-L4** | 4 | Inductor Toroidal Blindado 10 µH 5A | SMD 12x12mm | Inductancias de potencia del filtro pasivo LC de reconstrucción de salida de altavoces | Wurth Elektronik 744314101 |
| **C1-C4** | 4 | Condensador Película Polipropileno 680 nF 50V | SMD 1812 | Condensadores de filtro LC grado audiófilo de muy bajo factor de disipación | KEMET C1812C684K5RACTU |
| **J1** | 1 | Bornero de tornillo 4 polos paso 5.08mm | PCB Bornier | Terminales de salida estéreo para altavoces pasivos (L+, L-, R+, R-) | Phoenix Contact MKDSN 1.5/4 |
| **J2** | 1 | Jack de alimentación DC 5.5 x 2.1 mm | Montaje PCB Horizontal | Entrada de alimentación principal de 12V a 24V DC / 3.5A | CUI Devices PJ-002A |
| **C_IN** | 2 | Condensador electrolítico Low-ESR 470 µF 35V | Radial Ø10x16mm | Filtro desacoplo de alta corriente para la etapa de potencia de audio | Nichicon UHW1V471MPD |
| **F1** | 1 | Fusible SMD PTC Polyswitch 30V 4A | SMD 2920 | Protección contra sobrecorrientes en la línea de 24V DC | Littelfuse 2920L400PR |
