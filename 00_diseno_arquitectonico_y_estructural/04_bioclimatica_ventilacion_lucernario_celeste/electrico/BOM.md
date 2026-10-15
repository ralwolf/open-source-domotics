# Lista de Materiales (BOM) - Controlador Lucernario Bioclimático

| Referencia | Componente | Descripción | Encapsulado | Cantidad | Función Principal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-S3-WROOM-1 | Microcontrolador Dual-Core 240MHz Wi-Fi/BLE con 8MB Flash | SMD RF Module | 1 | Lógica de ventilación pasiva, seguridad meteorológica y MQTT |
| **U2** | LMD18200T | Puente H DMOS 55V 3A con frenado dinámico y sensado térmico | TO-220-11 | 1 | Accionamiento reversible suave de los actuadores lineales 24V |
| **U3** | Hydreon RG-11 | Sensor de lluvia óptico infrarrojo estanco para exteriores | Módulo externo | 1 | Cierre de emergencia instantáneo ante primeras gotas (<100ms) |
| **J2** | Davis / MISOL | Anemómetro de cazoletas generador de pulsos reed por vuelta | Conector 3 pines | 1 | Medición de racha de viento para cierre preventivo (>40 km/h) |
| **PS1** | Mean Well IRM-15-24 | Fuente conmutada industrial 230VAC a 24VDC 0.63A | Módulo THT | 1 | Alimentación de potencia para los motores lineales de compuerta |
| **J1** | Dinkle 5.08mm | Bornero de tornillo enchufable 8 polos | THT 5.08mm | 1 | Cableado a motores de carrera y sensores de tejado |
