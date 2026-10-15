# Rack de Servidores Central y Sistema UPS

## 1. Descripción y Alcance
Este subsistema aloja el núcleo de computación, almacenamiento redundante y comunicaciones de la infraestructura domótica local bajo filosofía 100% Zero-Trust y auto-alojada. Incluye el diseño mecánico 3D del armario rack de 19 pulgadas normalizado EIA-310-D de 15U, el plano 2D de distribución frontal de equipos, la electrónica a medida para telemetría ambiental interna y control de ventilación termorregulada, y la integración de monitorización de alimentación continua UPS/SAI mediante protocolo NUT.

---

## 2. Entregables Mecánicos y Modelado 3D (`mecanico/`)
- [`gabinete_rack_19u_datacenter.FCStd`](./mecanico/gabinete_rack_19u_datacenter.FCStd): Modelo paramétrico 3D nativo en FreeCAD 1.1+ del armario rack de 19 pulgadas (15U, dimensiones exteriores 600 x 600 x 770 mm) en chapa de acero laminado en frío SPCC de 2 mm, 4 postes angulares verticales con troquelado normalizado EIA-310, puerta frontal acristalada ahumada con cerradura, extractores superiores duales de 120 mm y distribución completa de chasis rackeables.
- [`gabinete_rack_19u_datacenter.step`](./mecanico/gabinete_rack_19u_datacenter.step): Exportación neutra universal STEP AP214 para análisis de flujo térmico e integración arquitectónica en el patinillo técnico.
- [`elevacion_rack_19u.dxf`](./mecanico/elevacion_rack_19u.dxf): Plano CAD 2D de elevación frontal en formato DXF R12 con cotas exactas en milímetros y unidades de rack (1U a 15U).
- [`elevacion_rack_19u.svg`](./mecanico/elevacion_rack_19u.svg): Vista vectorial interactiva de la distribución de equipos (UPS Online 2U, PDU 1U, TrueNAS 2U, Proxmox VE 1U, Switch PoE+ 24P 1U, Patch Panel Cat6A 1U y Firewall OPNsense 1U).

---

## 3. Entregables Eléctricos y Electrónica (`electrico/`)
- [`controlador_ambiental_rack_pdu.kicad_sch`](./electrico/controlador_ambiental_rack_pdu.kicad_sch): Esquema electrónico profesional en KiCad 10 con microcontrolador ESP32-S3, interfaz I2C con sensor higrométrico de admisión Sensirion SHT31, bus 1-Wire con sondas duales DS18B20 en tobera de escape y banco de baterías, driver MOSFET PWM para extractores de 12V, relé para tira LED de servicio y sensor de corriente no invasivo SCT-013 en acometida de la PDU.
- [`controlador_ambiental_rack_pdu.kicad_pro`](./electrico/controlador_ambiental_rack_pdu.kicad_pro): Archivo de gestión de proyecto en KiCad 10.
- [`esquema_svg/controlador_ambiental_rack_pdu.svg`](./electrico/esquema_svg/controlador_ambiental_rack_pdu.svg): Renderizado vectorial del esquemático para consulta directa.
- [`BOM.md`](./electrico/BOM.md): Lista completa de materiales y componentes con referencias comerciales, tolerancias y encapsulados.

---

## 4. Entregables de Control y Firmware (`control/`)
- [`controlador_rack_ambiental.yaml`](./control/controlador_rack_ambiental.yaml): Firmware autónomo ESPHome para ESP32-S3 con algoritmo PID/lineal de velocidad de extractores según gradiente térmico de escape (25°C a 35°C), encendido automático de iluminación de cortesía al abrir puertas frontal/trasera mediante sensores magnéticos reed e informe de corriente RMS.
- [`upsmon.conf`](./control/upsmon.conf): Configuración del demonio de cliente Network UPS Tools (NUT) para apagado ordenado escalonado de hypervisores y cabinas de almacenamiento ante autonomía crítica de batería.
