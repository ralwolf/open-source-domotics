# Integración de Robótica de Limpieza (Aspirado y Trapeado) con Valetudo

Este subsistema comprende la infraestructura mecánica, eléctrica, electrónica y de control para la integración de robots aspiradores y fregonas autónomas gobernadas exclusivamente por **firmware libre Valetudo**, garantizando privacidad absoluta (cero telemetría ni dependencia de servidores cloud externos), navegación LiDAR local y base multifunción de vaciado ciclónico y secado térmico de mopas.

---

## 1. Alcance y Especificaciones Técnicas

### 1.1 Estación Base Multifunción de Acoplamiento (Dock)
- **Carcasa y Dimensiones:** $450 \times 400 \times 480\text{ mm}$ en termoplástico técnico resistente a impactos con rampa de entrada ranurada de alineación micrométrica.
- **Bahías Interiores de Servicio:**
  - Depósito de agua limpia ($4\text{ L}$) con tratamiento de electrolisis para desinfección de mopas.
  - Depósito estanco de agua sucia residual ($4\text{ L}$) con flotador de sobrellenado.
  - Módulo de vaciado de polvo ciclónico con bolsa sellada de $3\text{ L}$ y filtro HEPA clase H13.
  - Cámara de secado de mopas por flujo forzado de aire caliente a 45 °C para prevenir la proliferación de moho y bacterias.

### 1.2 Firmware Libre Valetudo y Comunicación MQTT Local
- **Desconexión Total de la Nube:**
  - El robot ejecuta Valetudo sobre el sistema operativo embebido basado en Linux, eliminando cualquier comunicación con servidores en Asia o Estados Unidos.
  - Comunicación bidireccional local por Wi-Fi segregada en la **VLAN 30 (IoT sin acceso WAN)** conectada directamente al broker local Mosquitto MQTT en Proxmox (`02_03`).
- **Navegación Láser LiDAR (LDS) y Zonificación:**
  - Generación local de mapas de estancias con segmentación precisa (Salón, Cocina, Dormitorios, Pasillos).
  - Configuración de barreras virtuales y zonas de exclusión (*No-Go Zones*) en áreas con cableado sensible o alfombras de pelo largo.

### 1.3 Telemetría y Automatizaciones Inteligentes
- **Limpieza por Ausencia Total:** Al bloquearse las cerraduras biométricas exteriores (`03_02`) y confirmarse la vivienda desocupada por geofencing/radares mmWave, el robot arranca automáticamente la limpieza completa.
- **Interrupción Silenciosa:** Si un usuario regresa a la vivienda antes de finalizar, el robot aborta la tarea y regresa de forma silenciosa a la base de recarga.
- **Monitoreo Energético y Protección Térmica:** La estación base cuenta con metrología BL0942 y sensor DS18B20 con desconexión térmica preventiva por relé si la cámara de secado supera los 65 °C.

---

## 2. Entregables Técnicos Generados

| Componente | Tipo de Archivo | Enlaces | Descripción Técnica |
| :--- | :--- | :--- | :--- |
| **Estación Base de Limpieza** | Modelo 3D CAD | [estacion_carga_robot_limpieza.FCStd](mecanico/estacion_carga_robot_limpieza.FCStd)<br>[estacion_carga_robot_limpieza.step](mecanico/estacion_carga_robot_limpieza.step) | Ensamble 3D FreeCAD de la torre de vaciado y lavado ($450\times400\times480\text{ mm}$), rampa de acceso, compuertas de tanques de agua y cono ciclónico. |
| **Plano de Integración y LiDAR** | Plano 2D CAD | [plano_estacion_robotica_limpieza.svg](mecanico/plano_estacion_robotica_limpieza.svg)<br>[plano_estacion_robotica_limpieza.dxf](mecanico/plano_estacion_robotica_limpieza.dxf) | Distribución en planta 2D de la estación base, trayectorias en S de navegación LiDAR, zonificación de estancias y áreas de exclusión virtuales. |
| **Placa PCB Control Estación** | Esquema KiCad 10 | [controlador_estacion_robotica.kicad_sch](electrico/controlador_estacion_robotica.kicad_sch)<br>[controlador_estacion_robotica.svg](electrico/esquema_svg/controlador_estacion_robotica.svg) | Hardware KiCad 10 con ESP32-C3, metrología BL0942, relé de seguridad térmico 16A, sensor 1-Wire DS18B20 y fuente aislada HLK-2M03. |
| **Lista de Materiales** | Lista BOM | [BOM.md](electrico/BOM.md) | Componentes de la placa, sensor DS18B20, relé Hongfa 16A, varistores y borneros de potencia. |
| **Firmware e Integración** | Configuración YAML | [integracion_robotica_valetudo.yaml](control/integracion_robotica_valetudo.yaml) | Integración local Home Assistant mediante MQTT con entidades de aspirador, batería, estado de consumibles y automatizaciones de presencia. |

---

## 3. Scripts de Generación Paramétrica

- `scripts/generar_robotica_limpieza_3d.py`: Genera el sólido 3D en FreeCAD 1.1+ y exporta en formato neutro STEP AP214.
- `scripts/generar_plano_robotica.py`: Dibuja el plano de distribución y mapa LiDAR en DXF R12 y SVG vectorial.
- `scripts/generar_kicad_robotica.py`: Genera el esquema KiCad 10 y exporta el SVG mediante `kicad-cli`.
