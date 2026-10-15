# Lista de Materiales (BOM) - PDU de Oficina Técnica con Filtrado EMI/RFI y Señalización ON-AIR

| Ref | Cantidad | Componente / Valor | Encapsulado | Función Técnica | Fabricante / N° de Parte |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **U1** | 1 | ESP32-C3-WROOM-02 (4MB Flash) | SMD Módulo 18x20mm | SoC RISC-V 160MHz con WiFi 802.11 b/g/n y Bluetooth 5.0 LE | Espressif ESP32-C3-WROOM-02-N4 |
| **U2** | 1 | BL0942 (Metrología Energética UART) | SSOP-10 | Lectura de potencia activa (W), tensión y corriente de la toma maestra del PC | Shanghai Belling BL0942 |
| **FL1** | 1 | Choque de modo común 2x4.7mH 10A | Toroidal THT | Filtro LC supresor de ruido de alta frecuencia EMI/RFI para tomas de audio | Wurth Elektronik 744824604 |
| **CX1** | 2 | Condensador de Seguridad X2 0.47 µF 275VAC | THT Radial paso 15mm | Supresión de interferencias de modo diferencial en la entrada de red | KEMET R46KI347000M1M |
| **CY1, CY2** | 2 | Condensador de Seguridad Y2 4.7 nF 250VAC | Disco cerámico azul THT | Supresión de ruido de modo común con derivación a tierra de protección | Murata DE2E3KY472MN3AM02F |
| **RL1** | 1 | Hongfa HF32FV-16-12-HTF (16A 250VAC) | THT 19x15.5x15mm | Relé de desconexión física de cargas esclavas (elimina consumos vampiro) | Hongfa HF32FV-16 |
| **Q1** | 1 | AOD4184A N-Channel MOSFET 40V 50A | TO-252 | Driver PWM 12V 1.5A para letrero luminoso exterior "ON AIR / EN LLAMADA" | Alpha & Omega AOD4184A |
| **PS1** | 1 | HLK-2M03 (AC/DC Aislado 3.3V 600mA) | Módulo 28x14x16mm | Fuente conmutada compacta entrada 85-264VAC, salida 3.3V DC aislada galvánicamente | Hi-Link HLK-2M03 |
| **MOV1** | 1 | Varistor 14D471K (470V 4.5kA) | Disco 14mm THT | Supresión de sobretensiones transitorias SPD Clase III en línea de oficina | Epcos B72214S0301K101 |
| **J1** | 1 | Bornero tornillo 6 polos paso 5.08mm | PCB Bornier | Bornas para Red L/N, Toma Maestra L_PC, Cargas Esclavas L_SLV, Salida 12V ON AIR | Phoenix Contact MKDSN 1.5/6 |
