# Lista de Materiales (BOM) - Micromódulo de Pared Dual Zero-Cross con Metrología

| Ref | Cantidad | Componente / Valor | Encapsulado | Función Técnica | Fabricante / N° de Parte |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **U1** | 1 | ESP32-C3-WROOM-02 (4MB Flash) | SMD Módulo 18x20mm | SoC RISC-V 160MHz, WiFi 802.11 b/g/n, BLE 5.0, gestión de interrupciones Zero-Cross | Espressif ESP32-C3-WROOM-02-N4 |
| **PS1** | 1 | HLK-2M03 (AC/DC Aislado 3.3V 600mA) | Módulo 28x14x16mm | Fuente conmutada compacta entrada 85-264VAC, salida 3.3V DC aislada galvánicamente | Hi-Link HLK-2M03 |
| **OK1** | 1 | EL814 / PC814 (Optoacoplador entrada AC) | SMD SOP-4 | Detector de cruce por cero en ambos semiciclos de la red eléctrica AC | Everlight EL814S |
| **U2** | 1 | BL0942 (Chip Metrología Energética UART) | SSOP-10 | Medidor de alta precisión: Potencia activa (W), RMS Voltaje (V), RMS Corriente (A) | Shanghai Belling BL0942 |
| **R_SHUNT** | 1 | Shunt 1 mΩ 3W 1% Manganina | SMD 2512 | Derivador de corriente de muy bajo coeficiente térmico para medición de carga | Vishay WSL25121L000FEA |
| **RL1, RL2** | 2 | Hongfa HF32FV-16-12-HTF (16A 250VAC) | THT 19x15.5x15mm | Relés de potencia ultra-compactos con bobina de bajo consumo (200mW) y contactos AgSnO2 | Hongfa HF32FV-16 |
| **Q1, Q2** | 2 | S8050 NPN Transistor 40V 0.5A | SOT-23 | Drivers de activación de bobinas de relé gobernados por GPIO de ESP32-C3 | JCST S8050 |
| **D1, D2** | 2 | 1N4148W Diodo Flyback | SOD-123 | Supresión de picos inductivos de desenergización de las bobinas de los relés | Diodes Inc. 1N4148W |
| **OK2, OK3** | 2 | PC817 Optoacopladores de entrada | SOP-4 | Lectura optoaislada de tensión AC proveniente de pulsadores o conmutadas de pared S1/S2 | Sharp PC817X |
| **MOV1** | 1 | Varistor 10D471K (470V) | Disco 10mm THT | Supresión de sobretensiones transitorias en la entrada de línea AC | Epcos/TDK S10K300 |
| **F1** | 1 | Fusible cilíndrico cerámico 2A 250V Slow-Blow | Subminiatura THT | Protección de sobrecorriente y cortocircuito en placa | Littelfuse 39212000000 |
| **J1** | 1 | Bornero de tornillo 6 polos paso 5.0mm | Bloque modular THT | Terminales para L, N, L1_OUT, L2_OUT, S1_IN, S2_IN | Phoenix Contact MKDSN 1.5/6 |
