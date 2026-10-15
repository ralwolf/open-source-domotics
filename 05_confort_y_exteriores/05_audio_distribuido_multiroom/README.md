# Sistema de Audio Distribuido Multiroom de Alta Fidelidad

Este subsistema comprende la ingeniería acústica, mecánica, electrónica y de control para la distribución de audio estéreo de alta fidelidad sincronizado en 6 zonas independientes de la vivienda (10x10 m), basado en amplificadores digitales puros Clase D (*Direct-Digital I2S*), protocolo Snapcast / Music Assistant y atenuación inteligente (*Audio Ducking*).

---

## 1. Alcance y Especificaciones Técnicas

### 1.1 Zonificación Acústica de la Vivienda (6 Zonas Estéreo)
- **Zona 1 (Salón - Comedor):** 2 altavoces coaxiales de 2 vías empotrados en falso techo de 6.5" ($60\text{ W RMS}$, cono de fibra de vidrio trenzada y tweeter orientable de cúpula de seda $\pm 15^\circ$, respuesta $45\text{ Hz} - 20\text{ kHz}$).
- **Zona 2 (Cocina):** 2 altavoces empotrables de 5.25" ($40\text{ W RMS}$) con tratamiento antihumedad IP44 y cono de polipropileno inyectado.
- **Zona 3 (Dormitorio Principal):** 2 altavoces empotrados de 6.5" ($50\text{ W RMS}$) con crossover pasivo audiófilo de 12 dB/octava.
- **Zona 4 (Dormitorio Infantil / Estudio):** 2 altavoces empotrados de 5.25" ($40\text{ W RMS}$).
- **Zona 5 (Baño Principal):** 1 altavoz empotrado dual estéreo de 6.5" ($50\text{ W RMS}$, doble bobina móvil y doble tweeter) con certificación IP44 para condensación de vapor.
- **Zona 6 (Terraza Exterior y Piscina):** 2 altavoces de superficie tipo monitor con soporte articulado y certificación IP65 intemperie ($60\text{ W RMS}$, rejilla de aluminio y recinto estanco con tratamiento UV).

### 1.2 Líneas de Altavoz y Segregación Electromagnética
- Cableado con manguera de cobre 100% libre de oxígeno (OFC 99.99%) de $2 \times 1.5\text{ mm}^2$ con apantallamiento perimetral de mylar/aluminio y drenaje a tierra para evitar diafonía (*crosstalk*) o captación de zumbidos de 50 Hz.
- Tendido segregado por tubos corrugados exclusivos para audio, manteniendo una distancia $\ge 30\text{ cm}$ de las canalizaciones de fuerza eléctrica 230V.

### 1.3 Amplificación Digital Directa I2S (Texas Instruments TAS5805M)
- Enlace digital puro: la señal de audio fluye en formato I2S digital de 24-bit / 96 kHz directamente desde el SoC ESP32-S3 hasta la modulación PWM del TAS5805M, sin etapas intermedias de conversión digital-analógica (DAC) que introduzcan distorsión o ruido de fondo.
- Relación señal-ruido $SNR > 105\text{ dB}$, distorsión armónica total más ruido $THD+N < 0.04\%$ y rendimiento de potencia $> 90\%$ a 24V DC.
- Filtro LC de reconstrucción con bobinas toroidales apantalladas y condensadores de película de polipropileno para mínima interferencia electromagnética (EMI).

### 1.4 Lógicas de Control: Snapcast y Audio Ducking
- **Music Assistant en Home Assistant:** Gestión centralizada de fuentes locales (biblioteca FLAC en TrueNAS), Spotify Connect, AirPlay 2 y emisoras web.
- **Sincronización Multiroom:** Permite el agrupamiento de todas las zonas en "Modo Fiesta" con retardo entre habitaciones imperceptible ($< 2\text{ ms}$) o reproducción independiente de listas en cada estancia.
- **Audio Ducking:** Cuando se produce una llamada en el videoportero de la entrada (`03_06`) o se activa un mensaje prioritario de voz del asistente local (`05_06`) o alarma de seguridad, el sistema reduce inmediatamente el volumen en un 80% en todas las zonas activas y lo restaura tras finalizar la locución.

---

## 2. Entregables Técnicos Generados

| Componente | Tipo de Archivo | Enlaces | Descripción Técnica |
| :--- | :--- | :--- | :--- |
| **Carcasa Amplificador Streamer** | Modelo 3D CAD | [amplificador_streamer_multiroom.FCStd](mecanico/amplificador_streamer_multiroom.FCStd)<br>[amplificador_streamer_multiroom.step](mecanico/amplificador_streamer_multiroom.step) | Ensamble 3D FreeCAD de la carcasa de aluminio anodizado ($110\times85\times32\text{ mm}$), aletas de refrigeración, dial de volumen y bornas banana. |
| **Plano de Red Acústica** | Plano 2D CAD | [plano_distribucion_audio_multiroom.svg](mecanico/plano_distribucion_audio_multiroom.svg)<br>[plano_distribucion_audio_multiroom.dxf](mecanico/plano_distribucion_audio_multiroom.dxf) | Distribución en planta 2D de las 6 zonas estéreo, ubicación de altavoces de techo e intemperie y trazado de mangueras de audio hacia el Rack IT. |
| **Placa PCB Amplificador Hi-Fi** | Esquema KiCad 10 | [amplificador_audio_multiroom.kicad_sch](electrico/amplificador_audio_multiroom.kicad_sch)<br>[amplificador_audio_multiroom.svg](electrico/esquema_svg/amplificador_audio_multiroom.svg) | Hardware KiCad 10 con ESP32-S3 (8MB PSRAM), etapa Clase D TAS5805M I2S direct-digital, regulador ultra-bajo ruido TPS7A4700 y filtro pasivo LC. |
| **Lista de Materiales** | Lista BOM | [BOM.md](electrico/BOM.md) | Componentes de la placa, inductores toroidales apantallados, condensadores de polipropileno, bornas y conectores. |
| **Firmware de Control** | Firmware ESPHome | [streamer_audio_multiroom.yaml](control/streamer_audio_multiroom.yaml) | Firmware nativo ESPHome con Media Player I2S, integración con Music Assistant / Snapcast y automatización de atenuación Audio Ducking. |

---

## 3. Scripts de Generación Paramétrica

- `scripts/generar_amplificador_multiroom_3d.py`: Genera el sólido 3D en FreeCAD 1.1+ y exporta en formato neutro STEP AP214.
- `scripts/generar_plano_audio_multiroom.py`: Dibuja el plano de distribución acústica en DXF R12 y SVG vectorial.
- `scripts/generar_kicad_audio_multiroom.py`: Genera el esquema KiCad 10 y exporta el SVG mediante `kicad-cli`.
