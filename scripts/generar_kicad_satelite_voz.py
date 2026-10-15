#!/usr/bin/env python3
"""
Generador de Proyecto y Esquema Electrónico KiCad 10.0
Proyecto: Satélite de Voz de Sobremesa ESP32-S3 con Audio I2S Dúplex y Mute Físico
Módulo: 05_confort_y_exteriores/06_asistente_voz_local_privado/electrico
"""

import os
import uuid
import subprocess

def generar_kicad_satelite_voz(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    pro_path = os.path.join(output_dir, "satelite_voz_esp32s3.kicad_pro")
    sch_path = os.path.join(output_dir, "satelite_voz_esp32s3.kicad_sch")
    bom_path = os.path.join(output_dir, "BOM.md")

    root_uuid = str(uuid.uuid4())

    # 1. KICAD PROJECT (.kicad_pro)
    pro_content = f"""{{
  "boards": [],
  "meta": {{
    "filename": "satelite_voz_esp32s3.kicad_pro",
    "version": 3
  }},
  "net_settings": {{
    "classes": [
      {{
        "clearance": 0.2,
        "diff_pair_gap": 0.25,
        "diff_pair_width": 0.35,
        "name": "Default",
        "track_width": 0.25,
        "via_diameter": 0.7,
        "via_drill": 0.35
      }},
      {{
        "clearance": 0.3,
        "diff_pair_gap": 0.2,
        "diff_pair_width": 0.3,
        "name": "Audio_I2S_HighQuality",
        "track_width": 0.3,
        "via_diameter": 0.8,
        "via_drill": 0.4
      }}
    ],
    "meta": {{
      "version": 4
    }}
  }},
  "schematic": {{
    "annotate_start_num": 0,
    "bom_export_filename": "${{PROJECTNAME}}.csv",
    "meta": {{
      "version": 1
    }}
  }},
  "sheets": [
    [
      "{root_uuid}",
      ""
    ]
  ]
}}
"""
    with open(pro_path, "w", encoding="utf-8") as f:
        f.write(pro_content)

    # 2. KICAD SCHEMATIC (.kicad_sch)
    def u(): return str(uuid.uuid4())

    sch_content = f"""(kicad_sch
  (version 20231120)
  (generator "open-source-domotics-gen")
  (generator_version "10.0")
  (uuid "{root_uuid}")
  (paper "A3")
  (title_block
    (title "SATELITE DE VOZ PRIVADO ESP32-S3 (AUDIO I2S DUPLEX)")
    (date "2026-10-15")
    (rev "v1.0")
    (company "open-source-domotics (Hardware Libre)")
    (comment 1 "Matriz 2x INMP441 I2S + DAC Amplificador MAX98357A 3.2W")
    (comment 2 "Corte Analógico de Mute de Hardware + 12x LED NeoPixel WS2812B")
  )

  (wire (pts (xy 35.0 50.0) (xy 75.0 50.0))
    (stroke (width 0) (type default))
    (uuid "{u()}")
  )
  (text "ALIMENTACION_5VDC_USBC"
    (at 35.0 48.0 0)
    (effects (font (size 1.5 1.5)))
    (uuid "{u()}")
  )

  (symbol
    (lib_id "Regulator_Linear:AP2112K-3.3")
    (at 85.0 65.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U1" (at 85.0 52.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "AP2112K_3V3_600mA_UltraLowNoise" (at 85.0 55.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:SOT-23-5" (at 85.0 65.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "RF_Module:ESP32-S3-WROOM-1")
    (at 160.0 75.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U2" (at 160.0 42.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "ESP32-S3-WROOM-1-N8R8" (at 160.0 45.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "RF_Module:ESP32-S3-WROOM-1" (at 160.0 75.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Audio:INMP441")
    (at 230.0 55.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "MK1" (at 230.0 42.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "INMP441_MEMS_MIC_LEFT" (at 230.0 45.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Audio:INMP441_Breakout" (at 230.0 55.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Audio:INMP441")
    (at 230.0 85.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "MK2" (at 230.0 72.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "INMP441_MEMS_MIC_RIGHT" (at 230.0 75.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Audio:INMP441_Breakout" (at 230.0 85.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Audio_Amplifier:MAX98357A")
    (at 230.0 125.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U3" (at 230.0 112.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "MAX98357A_I2S_DAC_AMP_3W" (at 230.0 115.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DFN_QFN:TQFN-16-1EP_3x3mm_P0.5mm_EP1.7x1.7mm" (at 230.0 125.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x02")
    (at 290.0 125.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J1" (at 290.0 115.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "CONECTOR_ALTAVOZ_40MM" (at 290.0 118.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_JST:JST_PH_B2B-PH-K_1x02_P2.00mm_Vertical" (at 290.0 125.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "LED:WS2812B")
    (at 160.0 135.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "D1" (at 160.0 122.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "WS2812B_Ring_12LEDs" (at 160.0 125.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "LED_SMD:LED_WS2812B_PLCC4_5.0x5.0mm_P3.2mm" (at 160.0 135.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Switch:SW_Push")
    (at 100.0 120.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "SW1" (at 100.0 108.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "MUTE_HARDWARE_SWITCH" (at 100.0 111.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Button_Switch_SMD:SW_Push_1P1T_NO_6x6mm_H9.5mm" (at 100.0 120.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector:USB_C_Receptacle_USB2.0")
    (at 35.0 70.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J2" (at 35.0 58.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "USB_C_ALIMENTACION_5V" (at 35.0 61.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_USB:USB_C_Receptacle_Palconn_UTC16-G" (at 35.0 70.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (sheet_instances
    (path "/" (page "1"))
  )
)
"""
    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(sch_content)

    # 3. LISTA DE MATERIALES (BOM.md)
    bom_content = """# Lista de Materiales (BOM) - Satélite de Voz Local ESP32-S3

| Ref | Cantidad | Descripción | Encapsulado | Función Técnica | Proveedor / P/N | Coste Est. (EUR) |
|---|---|---|---|---|---|---|
| U1 | 1 | Regulador LDO 3.3V 600mA Ruido Ultra-Bajo AP2112K | SOT-23-5 | Alimentación limpia para micrófonos y ESP32-S3 ($<30\ \mu\text{V}_{RMS}$) | Diodes Inc. AP2112K-3.3TRG1 | 0.65 |
| U2 | 1 | SoC ESP32-S3 Doble Núcleo 240MHz 8MB Flash 8MB PSRAM | SMD Module | Pipeline openWakeWord local + audio I2S + Wi-Fi | Espressif ESP32-S3-WROOM-1-N8R8 | 3.80 |
| MK1-2 | 2 | Micrófono MEMS Digital Omnidireccional I2S INMP441 | LGA-14 / Módulo | Captura estéreo 24-bit 16kHz beamforming ($SNR = 61\text{ dBA}$) | TDK InvenSense INMP441 | 3.20 |
| U3 | 1 | Amplificador Audio Mono I2S Clase D 3.2W MAX98357A | TQFN-16 | Decodificación DAC I2S y amplificación altavoz | Analog Devices MAX98357AETE+ | 2.10 |
| SPK1 | 1 | Altavoz Dinámico 40mm 4Ω 3W con imán de neodimio | Chasis 40mm | Reproducción nítida de respuestas Piper TTS | PUI Audio AS04004MR-R | 2.50 |
| D1 | 1 | Anillo Circular de 12 LEDs RGB WS2812B 5050 | Anillo PCB Ø45mm | Señalización visual de estados de voz | Worldsemi WS2812B-5050 | 1.80 |
| SW1 | 1 | Pulsador de Bloqueo / Corte Físico Mute de Micrófonos | THT 6x6mm | Desconexión por hardware del riel VDD analógico | C&K PTS645 | 0.45 |
| J2 | 1 | Conector Hembra USB-C 16-pin 5V 3A | SMD Chasis | Entrada de alimentación USB 5V | Palconn UTC16-G | 0.70 |
| U4 | 1 | Matriz de Protección ESD USB USBLC6-2SC6 | SOT-23-6 | Supresión de descargas electrostáticas 15kV | STMicroelectronics USBLC6-2SC6 | 0.35 |
| C1-C8 | 8 | Condensadores Cerámicos 100nF, 10µF, 22µF X7R | SMD 0805 | Filtrado de desacoplo de alta frecuencia | Murata GRM21 | 0.60 |
| R1-R6 | 6 | Resistencias 5.1kΩ (CC1/CC2), 33Ω (Líneas I2S) | SMD 0603 | Adaptación de impedancia en bus de audio | Yageo RC0603 | 0.25 |
| PCB | 1 | Placa de Circuito Impreso Doble Cara FR4 | Ø50mm Circular | Integración mecánica en base cilíndrica | JLCPCB / PCBWay | 2.00 |
| **TOTAL** | | | | | | **18.40 EUR** |
"""
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(bom_content)

    print(f"Proyecto KiCad Satélite de Voz generado en: {output_dir}")
    print(f"BOM generado en: {bom_path}")

    # 4. EXPORTAR ESQUEMA A SVG MEDIANTE KICAD-CLI
    svg_dir = os.path.join(output_dir, "esquema_svg")
    os.makedirs(svg_dir, exist_ok=True)
    cmd = [
        "flatpak-spawn", "--host", "flatpak", "run",
        "--command=kicad-cli", "org.kicad.KiCad",
        "sch", "export", "svg",
        sch_path,
        "-o", svg_dir
    ]
    try:
        subprocess.run(cmd, check=True)
        print(f"Esquema SVG exportado mediante kicad-cli en: {svg_dir}")
    except Exception as e:
        print(f"Nota: kicad-cli finalizó: {e}")

if __name__ == "__main__":
    out = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/06_asistente_voz_local_privado/electrico"
    generar_kicad_satelite_voz(out)
