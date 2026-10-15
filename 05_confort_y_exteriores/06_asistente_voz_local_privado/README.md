# Asistente de Voz 100% Local, Privado y Seguro (Sin Nube)

Este subsistema implementa un satélite de interacción por voz natural residencial sin dependencias de servicios externos ni proveedores de nube comercial (Amazon Alexa, Google Assistant, Apple Siri). Toda la captura de audio, detección de palabra de activación (Wake Word), reconocimiento de habla (STT), inferencia de intenciones y síntesis de voz (TTS) se ejecuta íntegramente en la red local sobre el servidor Proxmox VE y los microcontroladores de borde ESP32-S3.

---

## 1. Arquitectura del Pipeline de Voz Local (Wyoming Protocol)

```
+-------------------------------------------------------------------------------+
|                      SATÉLITE DE SOBREMESA (ESP32-S3)                         |
|  +--------------------+        +--------------------+        +-------------+  |
|  | Matriz 2x INMP441  |        | openWakeWord Borde |        | Altavoz 3W  |  |
|  | I2S 16kHz Beamform | -----> | ("Okay Nabu" local)| -----> | DAC MAX98357|  |
|  +--------------------+        +---------+----------+        +------^------+  |
|             |                            |                          |         |
|      [Mute Hardware]                     v                          |         |
|      (Desconexión VDD)             Trigger Wake-word                |         |
+-------------|----------------------------|--------------------------|---------+
              |                            | RAW Audio Stream PCM     | Audio
              |                            v                          | TTS
+---------------------------------------------------------------------|---------+
|                    SERVIDOR PROXMOX VE (Lado Seguro VLAN 20)        |         |
|                                                                     |         |
|  +-------------------------+     +-------------------------+        |         |
|  | Whisper STT (Español)   | --> | Home Assistant Intents  |        |         |
|  | Transcripción neuronal  |     | Procesamiento de orden  |        |         |
|  +-------------------------+     +------------+------------+        |         |
|                                               |                     |         |
|                                               v                     |         |
|                                  +-------------------------+        |         |
|                                  | Piper TTS (Español)     | -------+         |
|                                  | Síntesis de voz natural |                  |
|                                  +-------------------------+                  |
+-------------------------------------------------------------------------------+
```

### Privacidad y Seguridad por Diseño
1. **Zero-Cloud:** El satélite opera en la VLAN 30 IoT sin acceso a internet (WAN bloqueada en OPNsense).
2. **Mute Analógico Físico:** El botón de privacidad superior interrumpe directamente la alimentación física $V_{DD}$ de los micrófonos MEMS y enciende un LED rojo fijo.
3. **openWakeWord en el Borde:** El satélite no envía ningún byte de audio a la red hasta que detecta la palabra clave localmente en su memoria RAM de 8 MB con aceleración vectorial de punto flotante en el ESP32-S3.

---

## 2. Entregables y Modelos del Subsistema

### 2.1 Diseño Mecánico y Carcasa 3D (`mecanico/`)
- **Modelo CAD FreeCAD 1.1+**: [satelite_voz_sobremesa.FCStd](mecanico/satelite_voz_sobremesa.FCStd)
- **Modelo de Intercambio STEP**: [satelite_voz_sobremesa.step](mecanico/satelite_voz_sobremesa.step)
- **Script Generador 3D**: [generar_satelite_voz_3d.py](../../scripts/generar_satelite_voz_3d.py)
- **Plano 2D CAD (DXF)**: [plano_satelite_voz.dxf](mecanico/plano_satelite_voz.dxf)
- **Plano Vectorial SVG**: [plano_satelite_voz.svg](mecanico/plano_satelite_voz.svg)
- **Script Generador Plano 2D**: [generar_plano_satelite_voz.py](../../scripts/generar_plano_satelite_voz.py)
- **Especificaciones**:
  - Carcasa troncocónica de sobremesa ($\varnothing_{\text{base}} = 90\text{ mm}$, $\varnothing_{\text{top}} = 75\text{ mm}$, altura $55\text{ mm}$).
  - Rejilla acústica superior con orificios concéntricos para difusión omnidireccional del altavoz de $40\text{ mm}$.
  - Matriz frontal con dos puertos acústicos separados $45\text{ mm}$ para los micrófonos MEMS.
  - Difusor anular inferior translúcido en policarbonato para anillo de 12 LEDs WS2812B.
  - Botón superior táctil/mecánico de privacidad mute.

### 2.2 Diseño Eléctrico y Esquemático KiCad 10 (`electrico/`)
- **Proyecto KiCad 10**: [satelite_voz_esp32s3.kicad_pro](electrico/satelite_voz_esp32s3.kicad_pro)
- **Esquema Electrónico**: [satelite_voz_esp32s3.kicad_sch](electrico/satelite_voz_esp32s3.kicad_sch)
- **Vectorial SVG**: [satelite_voz_esp32s3.svg](electrico/esquema_svg/satelite_voz_esp32s3.svg)
- **Lista de Materiales y Costes (BOM)**: [BOM.md](electrico/BOM.md)
- **Script Generador KiCad**: [generar_kicad_satelite_voz.py](../../scripts/generar_kicad_satelite_voz.py)
- **Topología de Audio**:
  - Microcontrolador ESP32-S3-WROOM-1 con 8MB Flash y 8MB Octal PSRAM.
  - Matriz de entrada: 2x Micrófonos MEMS digitales I2S INMP441 ($SNR = 61\text{ dBA}$, respuesta plana $60\text{ Hz - }15\text{ kHz}$).
  - Amplificador de salida: DAC I2S Clase D MAX98357A ($3.2\text{W}$, $4\ \Omega$, THD+N $0.05\%$).
  - Regulador LDO AP2112K-3.3 de ultra bajo ruido ($< 30\ \mu\text{V}_{RMS}$) para evitar zumbidos en los micrófonos.
  - Supresor de transitorios ESD USBLC6-2SC6 en puerto USB-C.

### 2.3 Firmware y Automatización ESPHome (`control/`)
- **Firmware ESPHome**: [satelite_voz_local.yaml](control/satelite_voz_local.yaml)
- **Lógica Integrada**:
  - Detección de palabra de activación local con modelo `micro_wake_word: okay_nabu`.
  - Integración transparente con Home Assistant Voice Assistant mediante Wyoming Protocol.
  - Control dinámico de efectos de luz en anillo LED WS2812B según la fase de la conversación:
    - **Reposo:** Luz ámbar cálida tenue ($15\%$) o apagado.
    - **Palabra clave detectada:** Pulso cian rápido.
    - **Escuchando orden:** Cian brillante continuo.
    - **Procesando:** Cometa azul en rotación.
    - **Respondiendo:** Onda verde de respiración sincronizada con la voz.
    - **Mute de privacidad:** Anillo rojo continuo.
