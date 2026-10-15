# Lista de Materiales (BOM) - Satélite de Voz Local ESP32-S3

| Ref | Cantidad | Descripción | Encapsulado | Función Técnica | Proveedor / P/N | Coste Est. (EUR) |
|---|---|---|---|---|---|---|
| U1 | 1 | Regulador LDO 3.3V 600mA Ruido Ultra-Bajo AP2112K | SOT-23-5 | Alimentación limpia para micrófonos y ESP32-S3 ($<30\ \mu	ext{V}_{RMS}$) | Diodes Inc. AP2112K-3.3TRG1 | 0.65 |
| U2 | 1 | SoC ESP32-S3 Doble Núcleo 240MHz 8MB Flash 8MB PSRAM | SMD Module | Pipeline openWakeWord local + audio I2S + Wi-Fi | Espressif ESP32-S3-WROOM-1-N8R8 | 3.80 |
| MK1-2 | 2 | Micrófono MEMS Digital Omnidireccional I2S INMP441 | LGA-14 / Módulo | Captura estéreo 24-bit 16kHz beamforming ($SNR = 61	ext{ dBA}$) | TDK InvenSense INMP441 | 3.20 |
| U3 | 1 | Amplificador Audio Mono I2S Clase D 3.2W MAX98357A | TQFN-16 | Decodificación DAC I2S y amplificación altavoz | Analog Devices MAX98357AETE+ | 2.10 |
| SPK1 | 1 | Altavoz Dinámico 40mm 4Ω 3W con imán de neodimio | Chasis 40mm | Reproducción nítida de respuestas Piper TTS | PUI Audio AS04004MR-R | 2.50 |
| D1 | 1 | Anillo Circular de 12 LEDs RGB WS2812B 5050 | Anillo PCB Ø45mm | Señalización visual de estados de voz | Worldsemi WS2812B-5050 | 1.80 |
| SW1 | 1 | Pulsador de Bloqueo / Corte Físico Mute de Micrófonos | THT 6x6mm | Desconexión por hardware del riel VDD analógico | C&K PTS645 | 0.45 |
| J2 | 1 | Conector Hembra USB-C 16-pin 5V 3A | SMD Chasis | Entrada de alimentación USB 5V | Palconn UTC16-G | 0.70 |
| U4 | 1 | Matriz de Protección ESD USB USBLC6-2SC6 | SOT-23-6 | Supresión de descargas electrostáticas 15kV | STMicroelectronics USBLC6-2SC6 | 0.35 |
| C1-C8 | 8 | Condensadores Cerámicos 100nF, 10µF, 22µF X7R | SMD 0805 | Filtrado de desacoplo de alta frecuencia | Murata GRM21 | 0.60 |
| R1-R6 | 6 | Resistencias 5.1kΩ (CC1/CC2), 33Ω (Líneas I2S) | SMD 0603 | Adaptación de impedancia en bus de audio | Yageo RC0603 | 0.25 |
| PCB | 1 | Placa de Circuito Impreso Doble Cara FR4 | Ø50mm Circular | Integración mecánica en base cilíndrica | JLCPCB / PCBWay | 2.00 |
| **TOTAL** | | | | | | **18.40 EUR** |
