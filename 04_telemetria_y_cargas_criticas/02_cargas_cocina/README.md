# Monitorización y Protección de Cargas Críticas en Cocina

Este subsistema comprende la infraestructura eléctrica de potencia, protecciones y telemetría granular de cargas en la cocina de la vivienda (10x10 m), con línea de alta capacidad C32 para inducción/horno, respaldo ininterrumpido dedicado para el refrigerador mediante mini-UPS LiFePO4 y detección inteligente de fin de ciclo en lavavajillas.

---

## 1. Alcance y Especificaciones Técnicas

### 1.1 Distribución y Circuitos Eléctricos
- **Circuito C32 (Placa de Inducción + Horno Eléctrico):**
  - Conductor de fase, neutro y tierra de $6\text{ mm}^2$ libre de halógenos canalizado en tubo rígido de $25\text{ mm}$.
  - Capacidad para alimentar simultáneamente la encimera de inducción de 4 fuegos ($7.2\text{ kW}$) y el horno multifunción pirolítico ($3.5\text{ kW}$).
- **Circuito C20 Prioritario (Refrigerador Inverter + Mini-UPS):**
  - Conductor de $4\text{ mm}^2$, circuito no desconectable por algoritmos de *load-shedding* (desconexión de cargas no prioritarias en modo isla).
  - Incorpora un **Mini-UPS de estado sólido con banco de baterías LiFePO4 de 4S (12.8V 20Ah / 256 Wh)** y relé de transferencia ultrarrápido ($<10\text{ ms}$), eliminando apagados bruscos del compresor inverter ante microcortes o conmutaciones del inversor solar ESS.
- **Circuito C16 (Lavavajillas, Microondas y Tomas de Encimera):**
  - Conductores de $2.5\text{ mm}^2$ protegidos con magnetotérmicos individuales y dispositivos de supresión de sobretensiones transitorias SPD Clase III en las bases de enchufe.

### 1.2 Telemetría y Automatizaciones Inteligentes
- **Detección Automática de Fin de Ciclo (Lavavajillas):**
  - Monitoreo continuo mediante chip de metrología BL0942 con derivador shunt de manganina de $1\text{ m}\Omega$.
  - Algoritmo de reconocimiento de estados: tras el pico térmico de secado ($1800\text{ W}$), si la potencia cae por debajo de $3\text{ W}$ durante más de 2 minutos seguidos, el sistema envía aviso sonoro por el sistema multiroom (`05_05`), aviso de voz (`05_06`) y notificación push a los dispositivos móviles.
- **Alerta de Anomalía en Refrigerador:**
  - Si el consumo eléctrico del compresor supera los $350\text{ W}$ de forma ininterrumpida durante más de 3 horas, Home Assistant emite una alerta crítica por posible puerta mal cerrada o pérdida de gas refrigerante.

---

## 2. Entregables Técnicos Generados

| Componente | Tipo de Archivo | Enlaces | Descripción Técnica |
| :--- | :--- | :--- | :--- |
| **Gabinete Mini-UPS Refrigerador** | Modelo 3D CAD | [gabinete_mini_ups_refrigerador.FCStd](mecanico/gabinete_mini_ups_refrigerador.FCStd)<br>[gabinete_mini_ups_refrigerador.step](mecanico/gabinete_mini_ups_refrigerador.step) | Ensamble 3D FreeCAD del gabinete protector ($280\times200\times95\text{ mm}$), bahía de celdas 4S LiFePO4, tomas C20, display LCD y ranuras de ventilación. |
| **Plano Eléctrico de Cocina** | Plano 2D CAD | [plano_cargas_cocina.svg](mecanico/plano_cargas_cocina.svg)<br>[plano_cargas_cocina.dxf](mecanico/plano_cargas_cocina.dxf) | Plano 2D de distribución en planta de bancada, esquema unifilar de protecciones C32/C20/C16, SPD Tipo 3 y telemetría de cargas. |
| **Placa PCB Telemetría y UPS** | Esquema KiCad 10 | [controlador_cargas_cocina_ups.kicad_sch](electrico/controlador_cargas_cocina_ups.kicad_sch)<br>[controlador_cargas_cocina_ups.svg](electrico/esquema_svg/controlador_cargas_cocina_ups.svg) | Hardware KiCad 10 con ESP32-C3, dual BL0942 para metrología shunt, relé de transferencia <10ms, monitor de batería INA219 y varistores SPD. |
| **Lista de Materiales** | Lista BOM | [BOM.md](electrico/BOM.md) | Componentes de la placa, varistores 14D471K, relé Finder/Hongfa 16A, shunt de manganina y borneros de potencia. |
| **Firmware de Control** | Firmware ESPHome | [monitoreo_cocina_ups.yaml](control/monitoreo_cocina_ups.yaml) | Firmware nativo Home Assistant con telemetría de refrigerador/lavavajillas, conmutación automática a batería por subtensión (<195V) y notificación fin de ciclo. |

---

## 3. Scripts de Generación Paramétrica

- `scripts/generar_cocina_ups_3d.py`: Genera el sólido 3D en FreeCAD 1.1+ y exporta en formato neutro STEP AP214.
- `scripts/generar_plano_cocina.py`: Dibuja el plano de distribución y esquema unifilar en DXF R12 y SVG vectorial.
- `scripts/generar_kicad_cocina.py`: Genera el esquema KiCad 10 y exporta el SVG mediante `kicad-cli`.
