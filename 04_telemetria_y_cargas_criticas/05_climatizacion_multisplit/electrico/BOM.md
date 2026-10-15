# Lista de Materiales (BOM) - Pasarela IoT de Climatización Multi-Split

| Ref | Cantidad | Componente / Valor | Encapsulado | Función Técnica | Fabricante / N° de Parte |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **U1** | 1 | ESP32-C3-WROOM-02 (4MB Flash) | SMD Módulo 18x20mm | SoC RISC-V 160MHz con WiFi 802.11 b/g/n y Bluetooth Low Energy 5.0 | Espressif ESP32-C3-WROOM-02-N4 |
| **U2** | 1 | TXS0102DCUR (Level Shifter Bidireccional) | VSSOP-8 | Conversor de nivel de voltaje bidireccional de 3.3V (ESP32) a 5V (Bus CN105/Midea) | Texas Instruments TXS0102 |
| **VR1** | 1 | MP1584EN Step-Down DC-DC | SOIC-8-1EP | Convertidor reductor síncrono para obtener 3.3V estables desde los 12V del split | Monolithic Power MP1584EN |
| **SEN1** | 1 | Sensirion SHT31-DIS | DFN-8 | Sensor digital de temperatura (±0.2°C) y humedad relativa (±2%) por I2C | Sensirion SHT31-DIS-B |
| **OK1** | 1 | PC817 Optoacoplador | SOP-4 | Aislamiento galvánico de la entrada cableada para sensor magnético de ventana | Sharp PC817X |
| **IR1** | 1 | VS1838B Receptor Infrarrojo 38kHz | THT 3 pines | Decodificador de comandos IR para compatibilidad con mandos a distancia originales | Vishay TSOP38238 / VS1838B |
| **D1** | 1 | IR LED 940nm 5mm de alta potencia | THT Radial | Emisor de ráfagas infrarrojas para control universal de splits sin puerto serie | Vishay TSAL6400 |
| **Q1** | 1 | 2N2222A Transistor NPN 40V 0.8A | SOT-23 | Driver de conmutación de corriente para el LED emisor de infrarrojos | ON Semi MMBT2222A |
| **J1** | 1 | Conector JST-PA 5 pines horizontal 2.0mm | PCB Conector | Enchufe hembra para cable arnés hacia el puerto CN105 / CN40 de la placa del split | JST S5B-PASK-2(LF)(SN) |
| **F1** | 1 | Fusible SMD PTC Polyswitch 30V 500mA | SMD 1812 | Protección autorrearmable contra sobrecorrientes en la línea de 12V del split | Littelfuse 1812L050PR |
