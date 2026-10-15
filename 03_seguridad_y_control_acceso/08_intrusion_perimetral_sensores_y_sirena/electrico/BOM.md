# Lista de Materiales (BOM) - Central de Intrusión Perimetral DEOL

| Ref | Cantidad | Descripción | Encapsulado | Función Técnica | Proveedor / P/N | Coste Est. (EUR) |
|---|---|---|---|---|---|---|
| U1 | 1 | Regulador Buck Step-Down MP1584 | Módulo SMD | 12V a 3.3V / 1.5A para lógica ESP32 | Monolithic Power MP1584EN | 1.80 |
| U2 | 1 | Microcontrolador ESP32-WROOM-32E 8MB | SMD Module | Lógica de zonas supervisadas DEOL, ESPHome | Espressif ESP32-WROOM-32E | 3.50 |
| Q1-Q2 | 2 | MOSFET Potencia Canal N AOD4184A (40V, 50A, 8.5mΩ) | TO-252 | Driver Sirena 12V 2A y Flash Strobe | Alpha & Omega AOD4184A | 1.40 |
| F1 | 1 | Fusible Rearmable Polyswitch PTC 2.5A 30V | Radial | Protección de sobrecorriente para sirena | Littelfuse RUEF250 | 0.65 |
| R_DEOL | 8 | Resistencia Película Metálica 2.2kΩ 1% 0.25W | SMD 0805 | Resistencias balanceo Doble Fin de Línea | Yageo RC0805FR-072K2L | 0.25 |
| TVS1-4 | 4 | Supresores TVS Bidireccionales SMBJ15CA | SMB | Protección contra descargas ESD en cableado exterior | Littelfuse SMBJ15CA | 1.20 |
| J1-J6 | 6 | Bornero de Tornillo 2P 5.08mm 16A | THT | Conexión zonas DEOL, sirena y flash | Phoenix Contact 1729128 | 4.80 |
| C1-C6 | 6 | Condensadores Cerámicos 100nF y 10µF 50V | SMD 0805 | Filtro pasabajos anti-rebotes y RF en zonas | Murata GRM21 | 0.50 |
| PCB | 1 | Placa de Circuito Impreso Doble Cara 2oz Cu | FR4 100x80mm | Pistas masa en estrella de bajo ruido | JLCPCB / PCBWay | 2.50 |
| **TOTAL** | | | | | | **16.60 EUR** |
