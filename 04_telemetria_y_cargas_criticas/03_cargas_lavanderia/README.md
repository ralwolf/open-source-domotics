# Monitorización y Protección de Cargas en Lavandería con Seguridad Anti-Inundación

Este subsistema comprende la infraestructura eléctrica, mecánica, electrónica y de control para la zona de lavandería de la vivienda (10x10 m), con toma estanca de alta capacidad IP55 para lavadora/secadora, base de desacoplo de vibraciones a 1400 RPM, telemetría energética de fin de ciclo y enclavamiento de seguridad con corte de agua y desenergización de enchufes ante fugas.

---

## 1. Alcance y Especificaciones Técnicas

### 1.1 Distribución Eléctrica y Protecciones
- **Línea Dedicada C20:**
  - Conductor de cobre libre de halógenos de $4\text{ mm}^2$ canalizado en tubo rígido estanco con protección magnetotérmica C20 e interruptor diferencial clase A-SI (superinmunizado) de 30 mA.
  - Supresor de sobretensiones transitorias SPD Clase III instalado en la propia caja de mecanismos para proteger la electrónica inverter del motor sin escobillas (BLDC) de la lavadora y la bomba de calor de la secadora.
- **Enchufe Estanco IP55 de Superficie:**
  - Envolvente termoplástica con tapa abatible y junta de sellado elastomérica para soportar ambientes con alta humedad y salpicaduras directas de agua.

### 1.2 Amortiguación Mecánica y Desacoplo de Vibraciones
- Alfombra / base amortiguadora de caucho vulcanizado EPDM de alta densidad ($15\text{ mm}$) bajo las patas de la lavadora y secadora, reduciendo la transmisión de vibraciones dinámicas a la losa de hormigón armado durante la fase de centrifugado a 1400 RPM en más de un 85%.

### 1.3 Sistema de Seguridad Anti-Inundación Fail-Safe
- **Sonda de Presencia de Líquidos en Suelo:**
  - Sensor de detección de agua por conductividad resistiva/óptica ubicado en el punto más bajo del cuarto de lavandería junto al sumidero sifónico.
- **Enclavamiento Doble por Hardware (< 50 ms):**
  - Al detectar fuga de agua, el microcontrolador actúa en dos frentes inmediatos:
    1. **Corte Hidráulico:** Cierra la electroválvula solenoide de $3/4"$ instalada en el grifo de acometida de la lavadora mediante driver MOSFET de 12V.
    2. **Desconexión Eléctrica:** Abre el relé de potencia de 16A del enchufe, cortando la tensión eléctrica en las máquinas para prevenir riesgos de electrocución con el suelo mojado.
  - Envío simultáneo de alerta crítica prioritaria a Home Assistant y activación de avisos acústicos.

### 1.4 Reconocimiento de Fin de Ciclo
- Sensor de metrología energética BL0942 que analiza la curva de consumo: tras registrar la fase de centrifugado y calefacción ($> 1500\text{ W}$), al detectar que la potencia cae por debajo de $2.5\text{ W}$ durante más de 90 segundos seguidos, emite un aviso sonoro por el sistema multiroom (`05_05`) y notificación al teléfono móvil.

---

## 2. Entregables Técnicos Generados

| Componente | Tipo de Archivo | Enlaces | Descripción Técnica |
| :--- | :--- | :--- | :--- |
| **Enchufe Estanco y Base Antivibración** | Modelo 3D CAD | [enchufe_estanco_lavanderia_antivibracion.FCStd](mecanico/enchufe_estanco_lavanderia_antivibracion.FCStd)<br>[enchufe_estanco_lavanderia_antivibracion.step](mecanico/enchufe_estanco_lavanderia_antivibracion.step) | Ensamble 3D FreeCAD de la caja estanca IP55 ($160\times120\times85\text{ mm}$) con doble tapa abatible, prensaestopas PG16 y silentblock de caucho vulcanizado. |
| **Plano Eléctrico y de Seguridad** | Plano 2D CAD | [plano_cargas_lavanderia_seguridad.svg](mecanico/plano_cargas_lavanderia_seguridad.svg)<br>[plano_cargas_lavanderia_seguridad.dxf](mecanico/plano_cargas_lavanderia_seguridad.dxf) | Planta 2D de lavandería, esquema unifilar C20, SPD Tipo 3, ubicación de sonda de suelo y electroválvula de corte de agua en acometida. |
| **Placa PCB Control y Seguridad** | Esquema KiCad 10 | [controlador_lavanderia_seguridad.kicad_sch](electrico/controlador_lavanderia_seguridad.kicad_sch)<br>[controlador_lavanderia_seguridad.svg](electrico/esquema_svg/controlador_lavanderia_seguridad.svg) | Hardware KiCad 10 con ESP32-C3, metrología BL0942 16A, driver MOSFET AOD4184A para electroválvula, relé de corte de enchufe y sonda optoaislada. |
| **Lista de Materiales** | Lista BOM | [BOM.md](electrico/BOM.md) | Componentes de la placa, varistor 14D471K, relé 16A Hongfa, MOSFET 50A, diodo 1N5408 y acelerómetro opcional. |
| **Firmware de Control** | Firmware ESPHome | [controlador_lavanderia.yaml](control/controlador_lavanderia.yaml) | Firmware nativo Home Assistant con enclavamiento anti-inundación (<50ms), corte automático de agua y potencia, y notificación de fin de ciclo. |

---

## 3. Scripts de Generación Paramétrica

- `scripts/generar_lavanderia_ip55_3d.py`: Genera el sólido 3D en FreeCAD 1.1+ y exporta en formato neutro STEP AP214.
- `scripts/generar_plano_lavanderia.py`: Dibuja el plano de distribución y esquema unifilar en DXF R12 y SVG vectorial.
- `scripts/generar_kicad_lavanderia.py`: Genera el esquema KiCad 10 y exporta el SVG mediante `kicad-cli`.
