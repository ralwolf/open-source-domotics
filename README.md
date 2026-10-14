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
│   └── 06_canalizaciones_y_ductos_electricos_normativa/
├── 01_energia_renovable_y_potencia/
│   ├── 01_aerogenerador_archimedes_mk9/
│   ├── 02_solar_termico_y_calefaccion/
│   ├── 03_solar_fotovoltaica/
│   ├── 04_almacenamiento_baterias_ess/
│   ├── 05_biodigestor_biogas_generador/
│   ├── 06_generador_gasolina_respaldo/
│   └── 07_tableros_distribucion_y_protecciones/
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

