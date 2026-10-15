# Micromódulos Inteligentes de Pared con Conmutación Zero-Cross y Metrología

Este módulo comprende el diseño mecánico ultra-compacto, electrónico y de firmware para micromódulos de conmutación empotrables en cajas de mecanismos estándar de 65 mm detrás de interruptores o pulsadores existentes, con conmutación en cruce por cero (*Zero-Crossing*) y medición de consumo energético en tiempo real.

---

## 1. Alcance y Especificaciones Técnicas

### 1.1 Diseño Mecánico y Factor de Forma
- **Dimensiones Compactas:** $42 \times 38 \times 17\text{ mm}$, permitiendo su alojamiento holgado en cajas de empotrar de $\varnothing 65\text{ mm}$ y profundidad $\ge 50\text{ mm}$ dejando espacio para conductores de fase, neutro y retorno de $2.5\text{ mm}^2$.
- **Material de la Carcasa:** Polímero termoplástico ignífugo ABS/PC grado UL94-V0 con ranuras laterales de disipación térmica y bornero frontal de 6 polos paso 5.0 mm.

### 1.2 Tecnología Zero-Crossing (Cruce por Cero)
- **Problemática en Cargas LED:** Las luminarias LED y fuentes conmutadas modernas generan corrientes de irrupción transitorias (*inrush current*) de hasta 30-50 veces la corriente nominal al conectarse en el pico de la onda sinusoidal ($V_{pico} \approx 325\text{ V}$), provocando micro-arcos que sueldan o degradan prematuramente los contactos del relé.
- **Solución Hardware Zero-Cross:** Un optoacoplador bidireccional EL814 detecta los cruces de tensión por cero voltios ($V = 0\text{ V}$) cada semiciclo ($10\text{ ms}$ a $50\text{ Hz}$). El microcontrolador sincroniza el disparo del relé exactamente en el instante de cruce, reduciendo la corriente de irrupción a un mínimo estricto y multiplicando por 3 la vida útil de los contactos mecánicos AgSnO2.

### 1.3 Metrología Energética Integrada BL0942
- Chip de metrología energética de alta precisión calibrado mediante derivador de corriente (*shunt*) de manganina de $1\text{ m}\Omega$ clase 1.0.
- Telemetría de alta resolución reportada a Home Assistant: Voltaje RMS (V), Corriente RMS (A), Potencia Activa (W), Potencia Reactiva (VAr) y Energía Acumulada (kWh).

### 1.4 Modo Desacoplado (*Decoupled / Smart Bulb Mode*)
- Permite configurar las entradas S1 y S2 para enviar eventos domóticos por software (pulsación simple, doble, sostenida) a Home Assistant sin interrumpir la alimentación eléctrica de las bombillas inteligentes (Zigbee 3.0 / Matter / Wi-Fi), evitando que queden offline.
- Funcionamiento autónomo garantizado: si se pierde la conexión Wi-Fi, el micromódulo conmuta físicamente la carga de forma inmediata.

---

## 2. Entregables Técnicos Generados

| Componente | Tipo de Archivo | Enlaces | Descripción Técnica |
| :--- | :--- | :--- | :--- |
| **Carcasa Micromódulo** | Modelo 3D CAD | [micromodulo_rele_pared.FCStd](mecanico/micromodulo_rele_pared.FCStd)<br>[micromodulo_rele_pared.step](mecanico/micromodulo_rele_pared.step) | Ensamble 3D FreeCAD de la carcasa ultracompacta ($42\times38\times17\text{ mm}$), bornero de 6 polos, clips de fijación y ranuras de ventilación. |
| **Plano de Integración en Caja** | Plano 2D CAD | [plano_instalacion_micromodulo_pared.svg](mecanico/plano_instalacion_micromodulo_pared.svg)<br>[plano_instalacion_micromodulo_pared.dxf](mecanico/plano_instalacion_micromodulo_pared.dxf) | Sección transversal y esquema de conexionado en caja universal de 65 mm con paso de cables de 2.5 mm² y cableado a interruptores existentes. |
| **Placa PCB Micromódulo** | Esquema KiCad 10 | [micromodulo_rele_zerocross.kicad_sch](electrico/micromodulo_rele_zerocross.kicad_sch)<br>[micromodulo_rele_zerocross.svg](electrico/esquema_svg/micromodulo_rele_zerocross.svg) | Hardware KiCad 10 con ESP32-C3 RISC-V, fuente aislada HLK-2M03, detector de paso por cero EL814, metrología BL0942 con shunt y relés Hongfa 16A. |
| **Lista de Materiales** | Lista BOM | [BOM.md](electrico/BOM.md) | Componentes de la placa, varistor MOV 10D471K, fusible 2A lento, relés HF32FV y optoacopladores. |
| **Firmware de Control** | Firmware ESPHome | [micromodulo_rele_zerocross.yaml](control/micromodulo_rele_zerocross.yaml) | Firmware nativo Home Assistant con conmutación Zero-Cross, multiclick en pulsadores, modo desacoplado y telemetría de potencia. |

---

## 3. Scripts de Generación Paramétrica

- `scripts/generar_micromodulo_rele_3d.py`: Genera el sólido 3D en FreeCAD 1.1+ y exporta en formato neutro STEP AP214.
- `scripts/generar_plano_rele_pared.py`: Dibuja el plano de instalación y esquema unifilar en DXF R12 y SVG vectorial.
- `scripts/generar_kicad_rele_pared.py`: Genera el esquema KiCad 10 y exporta el SVG mediante `kicad-cli`.
