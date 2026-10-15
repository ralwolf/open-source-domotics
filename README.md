# open-source-domotics: Hogar Autosustentable, Inteligente y Seguro

Repositorio central para el diseño, dimensionamiento, automatización y despliegue del ecosistema de domótica integral, energía renovable y seguridad residencial.

## 📌 Documentación Principal

- **[OBJETIVOS.md](OBJETIVOS.md)**: Plan maestro detallado que describe las 6 fases de implementación:
  0. **Diseño Arquitectónico, Estructural e Instalaciones Base:** Mecánica de suelos (SPT), zapatas/pilares para sobrecargas renovables, zonificación con cuarto técnico IT, ventilación cruzada natural, vitrina/lucernario astronómico cenital (luz natural y observación de estrellas), red hidráulica con recirculación solar, red de gas dual (comisión + tanque recargable/biogás) y canalizaciones normadas con segregación de fuerza y datos.
  1. **Matriz de Energía Renovable y Respaldo:** Aerogenerador helicoidal Arquímedes MK9, horno solar térmico para agua y piso radiante, energía solar fotovoltaica, banco de baterías LiFePO4, biodigestor séptico (biogás/biometano), generador a gasolina y diseño de tableros eléctricos.
  2. **Infraestructura IT y Cómputo Local:** Router (OpenWrt/pfSense/OPNsense), switch PoE+, servidor Proxmox VE con Frigate NVR, TrueNAS, Home Assistant y UPS online de doble conversión con protocolo NUT.
  3. **Seguridad Perimetral, Accesos e Intercomunicación:** Cámaras PoE con IA, cerraduras biométricas, videoportero en puerta de entrada con botón y relé de cerradura, intercomunicadores de pared/sobremesa multi-estancia (SIP/WebRTC), monitores con visión invisible 940nm y detección acústica de llanto/ladridos (bebés y mascotas), electroválvulas de corte para agua/gas, cortinas y relés.
  4. **Telemetría y Monitorización Eléctrica Granular:** Medición precisa de voltaje y corriente en cocina (estufa, horno, refrigerador con regulador y UPS, extractor, lavavajillas, microondas), recámara/multimedia, lavandería (con protectores de picos), climatización multi-split y oficina (PC, periféricos, audio de estudio).
  5. **Confort y Exteriores:** Iluminación circadiana y regulada, robot aspirador/limpiador, riego inteligente para plantas y automatización/química para piscina.
- **[Notas de Diseño y Memorias de Cálculo](docs/notas_de_diseno/README.md)**: Cuadernos de ingeniería con fórmulas gobernantes, dimensionamiento de cargas y flujos de modelado FOSS (Geotecnia, Cúpula Astronómica, Canalizaciones Segregadas, Baterías LiFePO4, Redes VLAN).

---

## 🚀 Entregables Técnicos Generados (CAD 2D, FreeCAD 3D, KiCad y Firmware)

| Subsistema / Módulo | Formatos y Archivos Generados | Descripción Técnica |
| :--- | :--- | :--- |
| **Cimentación y Geotecnia** | [`plano_cimentacion_ejes.dxf`](00_diseno_arquitectonico_y_estructural/01_mecanica_suelos_y_cimentacion/planos_y_calculos/plano_cimentacion_ejes.dxf)<br>[`cimentacion_zapatas_pilares.FCStd`](00_diseno_arquitectonico_y_estructural/01_mecanica_suelos_y_cimentacion/planos_y_calculos/cimentacion_zapatas_pilares.FCStd)<br>[`cimentacion_zapatas_pilares.step`](00_diseno_arquitectonico_y_estructural/01_mecanica_suelos_y_cimentacion/planos_y_calculos/cimentacion_zapatas_pilares.step) | Ejes de replanteo 1-3 y A-C, 9 zapatas aisladas ($1.30 \times 1.30\text{ m}$), vigas riostras y columna C-TURB ($35 \times 35\text{ cm}$) para absorción de momentos del aerogenerador Archimedes MK9. |
| **Arquitectura Base** | [`planta_arquitectonica_base.dxf`](00_diseno_arquitectonico_y_estructural/03_arquitectura_habitaciones_patios_terrazas/planos_2d_dxf/planta_arquitectonica_base.dxf) | Distribución 2D de vivienda ($10 \times 10\text{ m}$): Sala/Comedor, Cocina ergonómica, Recámara principal, Recámara infantil, Cuarto Técnico IT central, Patio interior y hueco cenital. |
| **Lucernario Bioclimático** | [`lucernario_astronomico_cenital.FCStd`](00_diseno_arquitectonico_y_estructural/04_bioclimatica_ventilacion_lucernario_celeste/mecanico/lucernario_astronomico_cenital.FCStd)<br>[`lucernario_astronomico_cenital.step`](00_diseno_arquitectonico_y_estructural/04_bioclimatica_ventilacion_lucernario_celeste/mecanico/lucernario_astronomico_cenital.step) | Modelo 3D de cúpula cenital ($3.0 \times 2.0\text{ m}$) con marco de aluminio con RPT, doble acristalamiento templado low-iron para observación estelar y actuador lineal $24\text{ V}$ para ventilación nocturna. |
| **Tablero Eléctrico General** | [`cuadro_general_unifilar.dxf`](01_energia_renovable_y_potencia/07_tableros_distribucion_y_protecciones/electrico/cuadro_general_unifilar.dxf)<br>[`cuadro_general_unifilar.svg`](01_energia_renovable_y_potencia/07_tableros_distribucion_y_protecciones/electrico/cuadro_general_unifilar.svg) | Diagrama unifilar TGBT con conmutación ATS (Red / Inversor ESS), DPS Clase II, IGA 63A, RCD 63A/30mA A-SI, medidor Modbus y 9 circuitos derivados segregados (cargas esenciales vs. load-shedding). |
| **Gateway Telemetría IoT** | [`medidor_potencia_iot.kicad_sch`](04_telemetria_y_cargas_criticas/01_medicion_potencia_cuadro/electrico/medidor_potencia_iot.kicad_sch)<br>[`medidor_potencia_iot.svg`](04_telemetria_y_cargas_criticas/01_medicion_potencia_cuadro/electrico/esquema_svg/medidor_potencia_iot.svg)<br>[`BOM.md`](04_telemetria_y_cargas_criticas/01_medicion_potencia_cuadro/electrico/BOM.md) | Hardware KiCad 10 con ESP32-WROOM-32, interfaz Modbus RS-485 aislada, 4 canales PZEM UART, fuente HLK-PM01 integrada y doble relé de seguridad/corte de cargas secundarias. |
| **Firmware de Telemetría** | [`esp32_energy_monitor.yaml`](04_telemetria_y_cargas_criticas/01_medicion_potencia_cuadro/control/esp32_energy_monitor.yaml)<br>[`src/main.cpp`](04_telemetria_y_cargas_criticas/01_medicion_potencia_cuadro/control/src/main.cpp) | Firmware dual: (1) ESPHome con Modbus Controller, PZEMAC, pantalla OLED SSD1306 y API nativa HA; (2) Firmware C++ PlatformIO con watchdog, reglas autónomas de corte y MQTT. |
| **Topología Red VLANs** | [`topologia_red_vlans.dxf`](02_infraestructura_it_y_red/02_red_vlans_y_comunicaciones/electrico/topologia_red_vlans.dxf)<br>[`topologia_red_vlans.svg`](02_infraestructura_it_y_red/02_red_vlans_y_comunicaciones/electrico/topologia_red_vlans.svg)<br>[`opnsense_vlans_firewall.json`](02_infraestructura_it_y_red/02_red_vlans_y_comunicaciones/control/opnsense_vlans_firewall.json) | Arquitectura Zero-Trust de 5 VLANs segregadas (Gestión, Confiable, IoT sin WAN, CCTV aislado y Clientes), troncal LACP 5 Gbps y reglas de firewall. |
| **Rack IT 19" y UPS** | [`elevacion_rack_19u.dxf`](02_infraestructura_it_y_red/01_rack_servidores_y_ups/mecanico/elevacion_rack_19u.dxf)<br>[`elevacion_rack_19u.svg`](02_infraestructura_it_y_red/01_rack_servidores_y_ups/mecanico/elevacion_rack_19u.svg)<br>[`upsmon.conf`](02_infraestructura_it_y_red/01_rack_servidores_y_ups/control/upsmon.conf) | Alzado frontal normalizado EIA-310-D de 15U en Sala IT central, distribución de UPS Online de doble conversión, PDU y configuración cliente NUT para apagado limpio. |
| **Servidores Locales** | [`docker-compose.yml`](02_infraestructura_it_y_red/03_servidores_proxmox_ha_frigate_truenas/control/docker-compose.yml) | Despliegue de Home Assistant Core, Mosquitto MQTT, Frigate NVR con aceleración Coral Edge TPU y go2rtc WebRTC. |
| **Videoportero y Accesos** | [`videoportero_carcasa.FCStd`](03_seguridad_y_control_acceso/06_intercomunicacion_videoportero_y_multizona/mecanico/videoportero_carcasa.FCStd)<br>[`videoportero_carcasa.step`](03_seguridad_y_control_acceso/06_intercomunicacion_videoportero_y_multizona/mecanico/videoportero_carcasa.step)<br>[`videoportero_esp32s3.kicad_sch`](03_seguridad_y_control_acceso/06_intercomunicacion_videoportero_y_multizona/electrico/videoportero_esp32s3.kicad_sch)<br>[`videoportero_esp32s3.svg`](03_seguridad_y_control_acceso/06_intercomunicacion_videoportero_y_multizona/electrico/esquema_svg/videoportero_esp32s3.svg)<br>[`esp32s3_doorbell.yaml`](03_seguridad_y_control_acceso/06_intercomunicacion_videoportero_y_multizona/control/esp32s3_doorbell.yaml)<br>[`go2rtc.yaml`](03_seguridad_y_control_acceso/06_intercomunicacion_videoportero_y_multizona/control/go2rtc.yaml)<br>[`intercom_baby_monitor.yaml`](03_seguridad_y_control_acceso/06_intercomunicacion_videoportero_y_multizona/control/intercom_baby_monitor.yaml) | Carcasa 3D antivandálica IP65, hardware KiCad 10 con ESP32-S3, cámara DVP 160°, audio I2S dúplex (INMP441 + MAX98357A), relé cerradura 12V 2A, PoE, streaming WebRTC y monitor de bebés con LEDs IR de 940 nm invisibles. |
| **Aerogenerador Archimedes** | [`rotor_archimedes_mk9.FCStd`](01_energia_renovable_y_potencia/01_aerogenerador_archimedes_mk9/mecanico/rotor_archimedes_mk9.FCStd)<br>[`rotor_archimedes_mk9.step`](01_energia_renovable_y_potencia/01_aerogenerador_archimedes_mk9/mecanico/rotor_archimedes_mk9.step)<br>[`esquema_potencia_eolico.dxf`](01_energia_renovable_y_potencia/01_aerogenerador_archimedes_mk9/electrico/esquema_potencia_eolico.dxf)<br>[`esquema_potencia_eolico.svg`](01_energia_renovable_y_potencia/01_aerogenerador_archimedes_mk9/electrico/esquema_potencia_eolico.svg)<br>[`controlador_freno_eolico.yaml`](01_energia_renovable_y_potencia/01_aerogenerador_archimedes_mk9/control/controlador_freno_eolico.yaml) | Rotor cónico helicoidal 3D de 3 palas espirales ($\varnothing 1.50\text{ m}$), esquema de potencia PMSG 48V, rectificador Schottky, MPPT eólico con dump-load de 1.5 kW y control de freno de emergencia por cortocircuito. |
| **Solar Térmico y Suelo** | [`esquema_hidraulico_piso_radiante.dxf`](01_energia_renovable_y_potencia/02_solar_termico_y_calefaccion/mecanico/esquema_hidraulico_piso_radiante.dxf)<br>[`esquema_hidraulico_piso_radiante.svg`](01_energia_renovable_y_potencia/02_solar_termico_y_calefaccion/mecanico/esquema_hidraulico_piso_radiante.svg)<br>[`control_diferencial_solar.yaml`](01_energia_renovable_y_potencia/02_solar_termico_y_calefaccion/control/control_diferencial_solar.yaml) | Esquema hidráulico P&ID de 4 colectores de tubos de vacío, interacumulador de inercia de 500L, módulo ACS termostático a 45°C, suelo radiante de baja temperatura (35°C) con 6 zonas y control diferencial solar con sondas PT1000. |
| **Solar PV & Almacenamiento ESS** | [`esquema_fotovoltaico_ess.dxf`](01_energia_renovable_y_potencia/03_solar_fotovoltaica/electrico/esquema_fotovoltaico_ess.dxf)<br>[`esquema_fotovoltaico_ess.svg`](01_energia_renovable_y_potencia/03_solar_fotovoltaica/electrico/esquema_fotovoltaico_ess.svg)<br>[`gabinete_baterias_lifepo4_16s.FCStd`](01_energia_renovable_y_potencia/04_almacenamiento_baterias_ess/mecanico/gabinete_baterias_lifepo4_16s.FCStd)<br>[`gabinete_baterias_lifepo4_16s.step`](01_energia_renovable_y_potencia/04_almacenamiento_baterias_ess/mecanico/gabinete_baterias_lifepo4_16s.step)<br>[`bms_lifepo4_monitor.yaml`](01_energia_renovable_y_potencia/04_almacenamiento_baterias_ess/control/bms_lifepo4_monitor.yaml) | Arreglo fotovoltaico 5 kWp (2 strings de 6 paneles 450W), inversor híbrido 6 kW 48V, gabinete rack 19" 3D con 16 celdas LiFePO4 EVE 280Ah (14.3 kWh), barraje de cobre, BMS Daly/JBD UART/RS485 y monitor en ESPHome con balanceo pasivo. |
| **Corte de Emergencia Agua y Gas** | [`esquema_corte_valvulas_gas_agua.dxf`](03_seguridad_y_control_acceso/03_actuadores_valvulas_gas_agua/mecanico/esquema_corte_valvulas_gas_agua.dxf)<br>[`esquema_corte_valvulas_gas_agua.svg`](03_seguridad_y_control_acceso/03_actuadores_valvulas_gas_agua/mecanico/esquema_corte_valvulas_gas_agua.svg)<br>[`controlador_valvulas_seguridad.kicad_sch`](03_seguridad_y_control_acceso/03_actuadores_valvulas_gas_agua/electrico/controlador_valvulas_seguridad.kicad_sch)<br>[`controlador_valvulas_seguridad.svg`](03_seguridad_y_control_acceso/03_actuadores_valvulas_gas_agua/electrico/controlador_valvulas_seguridad.svg)<br>[`BOM.md`](03_seguridad_y_control_acceso/03_actuadores_valvulas_gas_agua/electrico/BOM.md)<br>[`corte_emergencia_gas_agua.yaml`](03_seguridad_y_control_acceso/03_actuadores_valvulas_gas_agua/control/corte_emergencia_gas_agua.yaml) | Esquema mecánico de corte rápido, PCB KiCad 10 con ESP32, optoacopladores para sondas de agua en cocina/lavandería, interfaz MQ-4 para gas, control de actuadores 12V 2A e interbloqueo analógico fail-safe local por hardware (<50ms). |
| **Captación Pluvial y Potabilización** | [`esquema_captacion_potabilizacion_pluvial.dxf`](00_diseno_arquitectonico_y_estructural/07_captacion_pluvial_cisterna_y_potabilizacion/mecanico/esquema_captacion_potabilizacion_pluvial.dxf)<br>[`esquema_captacion_potabilizacion_pluvial.svg`](00_diseno_arquitectonico_y_estructural/07_captacion_pluvial_cisterna_y_potabilizacion/mecanico/esquema_captacion_potabilizacion_pluvial.svg)<br>[`monitoreo_cisterna_potabilizacion.yaml`](00_diseno_arquitectonico_y_estructural/07_captacion_pluvial_cisterna_y_potabilizacion/control/monitoreo_cisterna_potabilizacion.yaml) | P&ID hidráulico completo con First Flush, cisterna subterránea 10.000 L, filtración por sedimentos (20µm) y carbón activado (5µm), esterilizador UV-C 55W, bomba sumergible, sensor de nivel hidrostático 4-20mA y conmutación automática cisterna/red. |
| **Estructura Portante y Losa** | [`estructura_portante_vivienda.FCStd`](00_diseno_arquitectonico_y_estructural/02_estructura_pilares_y_losas/planos_y_calculos/estructura_portante_vivienda.FCStd)<br>[`estructura_portante_vivienda.step`](00_diseno_arquitectonico_y_estructural/02_estructura_pilares_y_losas/planos_y_calculos/estructura_portante_vivienda.step)<br>[`plano_estructura_pilares_losas.dxf`](00_diseno_arquitectonico_y_estructural/02_estructura_pilares_y_losas/planos_y_calculos/plano_estructura_pilares_losas.dxf)<br>[`plano_estructura_pilares_losas.svg`](00_diseno_arquitectonico_y_estructural/02_estructura_pilares_y_losas/planos_y_calculos/plano_estructura_pilares_losas.svg) | Esqueleto estructural 3D FreeCAD (10x10 m), 9 pilares (P1-P8 $30\times30\text{ cm}$ y P9 C-TURB $35\times35\text{ cm}$ reforzado), vigas de amarre V-101 ($25\times40\text{ cm}$), losa maciza $20\text{ cm}$ con hueco cenital $3.0\times2.0\text{ m}$ y cuadro de armaduras. |
| **Cargador EV Wallbox Solar** | [`cargador_ev_wallbox.FCStd`](01_energia_renovable_y_potencia/09_cargador_vehiculo_electrico_ev/mecanico/cargador_ev_wallbox.FCStd)<br>[`cargador_ev_wallbox.step`](01_energia_renovable_y_potencia/09_cargador_vehiculo_electrico_ev/mecanico/cargador_ev_wallbox.step)<br>[`esquema_ev_wallbox.dxf`](01_energia_renovable_y_potencia/09_cargador_vehiculo_electrico_ev/electrico/esquema_ev_wallbox.dxf)<br>[`esquema_ev_wallbox.svg`](01_energia_renovable_y_potencia/09_cargador_vehiculo_electrico_ev/electrico/esquema_ev_wallbox.svg)<br>[`controlador_ev_wallbox.kicad_sch`](01_energia_renovable_y_potencia/09_cargador_vehiculo_electrico_ev/electrico/controlador_ev_wallbox.kicad_sch)<br>[`controlador_ev_wallbox.svg`](01_energia_renovable_y_potencia/09_cargador_vehiculo_electrico_ev/electrico/esquema_svg/controlador_ev_wallbox.svg)<br>[`BOM.md`](01_energia_renovable_y_potencia/09_cargador_vehiculo_electrico_ev/electrico/BOM.md)<br>[`ev_smart_charger.yaml`](01_energia_renovable_y_potencia/09_cargador_vehiculo_electrico_ev/control/ev_smart_charger.yaml) | Carcasa 3D IP54 con base Tipo 2, esquema unifilar con MCB 40A, RCD Tipo B (6mA DC), contactor 40A, medidor Modbus RS485, PCB KiCad 10 con circuito CP ±12V PWM 1kHz, y firmware ESPHome con modos Solar Puro, Eco Solar y Rápido. |
| **Riego Inteligente de Jardín** | [`esquema_hidraulico_riego.dxf`](05_confort_y_exteriores/03_riego_automatizado_jardin/mecanico/esquema_hidraulico_riego.dxf)<br>[`esquema_hidraulico_riego.svg`](05_confort_y_exteriores/03_riego_automatizado_jardin/mecanico/esquema_hidraulico_riego.svg)<br>[`controlador_riego_jardin.kicad_sch`](05_confort_y_exteriores/03_riego_automatizado_jardin/electrico/controlador_riego_jardin.kicad_sch)<br>[`controlador_riego_jardin.svg`](05_confort_y_exteriores/03_riego_automatizado_jardin/electrico/esquema_svg/controlador_riego_jardin.svg)<br>[`BOM.md`](05_confort_y_exteriores/03_riego_automatizado_jardin/electrico/BOM.md)<br>[`riego_inteligente_jardin.yaml`](05_confort_y_exteriores/03_riego_automatizado_jardin/control/riego_inteligente_jardin.yaml) | P&ID hidráulico de colector manifold 1" (4 zonas + válvula maestra 24VAC + filtro de anillas), caudalímetro de pulsos, PCB KiCad 10 con 5x Triacs BT136 con cruce por cero MOC3041, y firmware ESPHome con sprinkler secuencial y anti-fugas. |



---

## 🏗️ Arquitectura Tecnológica y Software 100% Libre (Puro FOSS)

- **Diseño Arquitectónico y Civil:** Ingetrazzo (trazados/replanteo), LibreCAD (planos 2D DXF) y Blender.
- **Modelado Mecánico 3D y BIM:** Open CAD Studio / FreeCAD (`.FCStd`, `.step`, `.stl`, `.ifc`).
- **Ingeniería Eléctrica y Electrónica:** QElectroTech (diagramas unifilares y tableros `.qet`), KiCad EDA (esquemas y PCBs `.kicad_sch`, `.kicad_pcb`).
- **Firmware y Embebidos:** Arduino CLI (compilación headless), ESPHome (firmware nativo HA), PlatformIO Core CLI.
- **Servidores y Control:** Proxmox VE, Home Assistant OS, Frigate NVR, TrueNAS SCALE, OPNsense / OpenWrt, Asterisk PBX + go2rtc.
- **Protocolos de Integración:** MQTT, Modbus RTU/TCP, Zigbee 3.0, Matter/Thread, ESPHome, PoE (802.3at/bt), SIP / WebRTC.
- **Guía de Software Libre:** Consulte [`docs/SOFTWARE_Y_HERRAMIENTAS_LIBRES.md`](docs/SOFTWARE_Y_HERRAMIENTAS_LIBRES.md).

---

## 📐 Esquemas Técnicos de Referencia (`docs/referencias/`)

- **Tablero de Distribución Eléctrica:** [cuadro_electrico_distribucion.jpg](docs/referencias/cuadro_electrico_distribucion.jpg) (Acometida 25 mm², DPS, interruptor bipolar, diferencial 63A/30mA y disyuntores C10-C32).
- **Sistema Solar Fotovoltaico + Baterías:** [sistema_solar_fotovoltaico_baterias.jpg](docs/referencias/sistema_solar_fotovoltaico_baterias.jpg) (Combiner box, MPPT, seccionador DC, banco de baterías y puesta a tierra).
- **Calefacción Solar por Piso Radiante:** [calefaccion_solar_piso_radiante.jpg](docs/referencias/calefaccion_solar_piso_radiante.jpg) (Colector solar térmico, tanque acumulador, caldera de apoyo y suelo radiante).
- **Acumulador con Serpentín:** [colector_solar_acumulador_caldera.jpg](docs/referencias/colector_solar_acumulador_caldera.jpg).

---

## 📂 Estructura de Carpetas de Diseño (Arquitectónico, Estructural, Eléctrico y Mecánico)

Cada componente técnico cuenta con subcarpetas estructuradas de diseño:
- Planos CAD 2D/3D (STEP/STL/DWG), memorias de cálculo geotécnico y estructural.
- Diagramas unifilares/multifilares, esquemas de borneros, protecciones (MCB/DPS) y lista de materiales (BOM).
- Configuraciones de Home Assistant, ESPHome, tópicos MQTT y lógica de automatización.

```text
├── 00_diseno_arquitectonico_y_estructural/
│   ├── 01_mecanica_suelos_y_cimentacion/
│   ├── 02_estructura_pilares_y_losas/
│   ├── 03_arquitectura_habitaciones_patios_terrazas/
│   ├── 04_bioclimatica_ventilacion_lucernario_celeste/
│   ├── 05_instalaciones_hidraulicas_y_gas/
│   ├── 06_canalizaciones_y_ductos_electricos_normativa/
│   └── 07_captacion_pluvial_cisterna_y_potabilizacion/
├── 01_energia_renovable_y_potencia/
│   ├── 01_aerogenerador_archimedes_mk9/
│   ├── 02_solar_termico_y_calefaccion/
│   ├── 03_solar_fotovoltaica/
│   ├── 04_almacenamiento_baterias_ess/
│   ├── 05_biodigestor_biogas_generador/
│   ├── 06_generador_gasolina_respaldo/
│   ├── 07_tableros_distribucion_y_protecciones/
│   ├── 08_proteccion_rayos_tierras/
│   └── 09_cargador_vehiculo_electrico_ev/
├── 02_infraestructura_it_y_red/
│   ├── 01_rack_servidores_y_ups/
│   ├── 02_red_vlans_y_comunicaciones/
│   └── 03_servidores_proxmox_ha_frigate_truenas/
├── 03_seguridad_y_control_acceso/
│   ├── 01_videovigilancia_poe_frigate/
│   ├── 02_cerraduras_biometricas/
│   ├── 03_actuadores_valvulas_gas_agua/
│   ├── 04_cortinas_y_persianas_motorizadas/
│   ├── 05_reles_conmutacion_pared/
│   └── 06_intercomunicacion_videoportero_y_multizona/
├── 04_telemetria_y_cargas_criticas/
│   ├── 01_medicion_potencia_cuadro/
│   ├── 02_cargas_cocina/
│   ├── 03_cargas_lavanderia/
│   ├── 04_cargas_oficina/
│   └── 05_climatizacion_multisplit/
└── 05_confort_y_exteriores/
    ├── 01_iluminacion_circadiana_y_exterior/
    ├── 02_robotica_limpieza/
    ├── 03_riego_automatizado_jardin/
    └── 04_mantenimiento_automatizado_piscina/
```

