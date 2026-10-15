#!/usr/bin/env python3
"""
Generador de Proyecto y Esquema Electrónico KiCad 10.0
Proyecto: Controlador Dimmer PWM 4 Canales 24V para Iluminación Circadiana y Exterior
Módulo: 05_confort_y_exteriores/01_iluminacion_circadiana_y_exterior/electrico
"""

import os
import uuid
import subprocess

def generar_kicad_iluminacion(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    pro_path = os.path.join(output_dir, "controlador_dimmer_circadiano.kicad_pro")
    sch_path = os.path.join(output_dir, "controlador_dimmer_circadiano.kicad_sch")
    bom_path = os.path.join(output_dir, "BOM.md")

    root_uuid = str(uuid.uuid4())

    # 1. KICAD PROJECT (.kicad_pro)
    pro_content = f"""{{
  "boards": [],
  "meta": {{
    "filename": "controlador_dimmer_circadiano.kicad_pro",
    "version": 3
  }},
  "net_settings": {{
    "classes": [
      {{
        "clearance": 0.25,
        "diff_pair_gap": 0.25,
        "diff_pair_width": 0.35,
        "name": "Default",
        "track_width": 0.3,
        "via_diameter": 0.8,
        "via_drill": 0.4
      }},
      {{
        "clearance": 0.5,
        "diff_pair_gap": 0.3,
        "diff_pair_width": 0.5,
        "name": "Power_24V_HighCurrent",
        "track_width": 1.5,
        "via_diameter": 1.8,
        "via_drill": 1.0
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
    (title "CONTROLADOR DIMMER PWM 4 CANALES 24V - ILUMINACION CIRCADIANA")
    (date "2026-10-15")
    (rev "v1.0")
    (company "open-source-domotics (Hardware Libre)")
    (comment 1 "PWM 20 kHz Flicker-Free | MOSFET AOD4184A | CCT + RGBW + Exterior")
    (comment 2 "Mean Well HLG 24V SELV | Sensor Lux BH1750 + mmWave LD2410 + RS485")
  )

  (wire (pts (xy 35.0 50.0) (xy 75.0 50.0))
    (stroke (width 0) (type default))
    (uuid "{u()}")
  )
  (text "ALIMENTACION_24VDC_SELV"
    (at 35.0 48.0 0)
    (effects (font (size 1.5 1.5)))
    (uuid "{u()}")
  )

  (symbol
    (lib_id "Regulator_Switching:MP1584")
    (at 85.0 65.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U1" (at 85.0 50.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "MP1584_StepDown_3V3" (at 85.0 53.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Converter_DCDC:Converter_DCDC_MP1584_Mini" (at 85.0 65.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "RF_Module:ESP32-WROOM-32E")
    (at 160.0 75.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U2" (at 160.0 45.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "ESP32-WROOM-32E" (at 160.0 48.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "RF_Module:ESP32-WROOM-32E" (at 160.0 75.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Driver_FET:TC4427")
    (at 220.0 60.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U3" (at 220.0 45.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TC4427_DualGateDriver" (at 220.0 48.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 220.0 60.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Transistor_FET:AOD4184A")
    (at 270.0 65.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "Q1" (at 270.0 52.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "AOD4184A_40V_50A" (at 270.0 55.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:TO-252-2" (at 270.0 65.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Transistor_FET:AOD4184A")
    (at 270.0 95.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "Q2" (at 270.0 82.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "AOD4184A_40V_50A" (at 270.0 85.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:TO-252-2" (at 270.0 95.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Transistor_FET:AOD4184A")
    (at 270.0 125.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "Q3" (at 270.0 112.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "AOD4184A_40V_50A" (at 270.0 115.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:TO-252-2" (at 270.0 125.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Transistor_FET:AOD4184A")
    (at 270.0 155.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "Q4" (at 270.0 142.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "AOD4184A_40V_50A" (at 270.0 145.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:TO-252-2" (at 270.0 155.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x02")
    (at 330.0 65.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J1" (at 330.0 55.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BORNA_CH1_WW_2200K" (at 330.0 58.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" (at 330.0 65.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x02")
    (at 330.0 95.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J2" (at 330.0 85.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BORNA_CH2_CW_6500K" (at 330.0 88.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" (at 330.0 95.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x02")
    (at 330.0 125.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J3" (at 330.0 115.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BORNA_CH3_EXTERIOR_PERGOLA" (at 330.0 118.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" (at 330.0 125.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x02")
    (at 330.0 155.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J4" (at 330.0 145.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BORNA_CH4_SEGURIDAD_FACHADA" (at 330.0 148.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" (at 330.0 155.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Sensor:BH1750")
    (at 100.0 130.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U4" (at 100.0 118.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BH1750_Lux_Sensor_I2C" (at 100.0 121.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 100.0 130.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Interface_UART:LD2410B")
    (at 100.0 160.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U5" (at 100.0 148.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "HLK-LD2410_mmWave_Radar" (at 100.0 151.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_PinHeader_2.54mm:PinHeader_1x05_P2.54mm_Vertical" (at 100.0 160.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Interface_UART:MAX13487")
    (at 160.0 145.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U6" (at 160.0 132.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "MAX13487_RS485_AutoDir" (at 160.0 135.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 160.0 145.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (sheet_instances
    (path "/" (page "1"))
  )
)
"""
    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(sch_content)

    # 3. LISTA DE MATERIALES (BOM.md)
    bom_content = """# Lista de Materiales (BOM) - Controlador Dimmer Circadiano 4x 24V

| Ref | Cantidad | Descripción | Encapsulado | Función Técnica | Proveedor / P/N | Coste Est. (EUR) |
|---|---|---|---|---|---|---|
| U1 | 1 | Regulador Buck Step-Down MP1584 | Módulo SMD | 24V a 3.3V / 1.5A para lógica ESP32 | Monolithic Power MP1584EN | 1.80 |
| U2 | 1 | Microcontrolador ESP32-WROOM-32E 8MB | SMD Module | Lógica de control solar, ESPHome, Wi-Fi | Espressif ESP32-WROOM-32E | 3.50 |
| U3 | 2 | Driver de Puerta Dual MOSFET TC4427 | SOIC-8 | Conmutación ultrarrápida 20 kHz sin ringing | Microchip TC4427EOA | 2.20 |
| Q1-Q4 | 4 | MOSFET Canal N AOD4184A (40V, 50A, 8.5mΩ) | TO-252 (DPAK) | Conmutación PWM canales LED WW/CW/Ext | Alpha & Omega AOD4184A | 2.80 |
| D1-D4 | 4 | Diodo Schottky SS34 (40V, 3A) | SMC | Diodo de marcha libre contra inductancia de cable | Vishay SS34 | 0.80 |
| TVS1-4| 4 | Supresor TVS SMBJ28A | SMB | Protección contra transitorios y descargas | Littelfuse SMBJ28A | 1.20 |
| U4 | 1 | Sensor Digital de Luz Ambiental BH1750 | SOIC-8 / Módulo | Medición de lux ambiental (1 - 65535 lx) | ROHM BH1750FVI | 1.50 |
| U5 | 1 | Sensor Radar Micro-ondas mmWave 24 GHz | Módulo 5-pin | Detección de presencia estática micrométrica | Hi-Link HLK-LD2410B | 4.50 |
| U6 | 1 | Transceptor RS-485 Auto-Dirección MAX13487 | SOIC-8 | Interfaz DMX512 / Modbus RTU cableada | Analog Devices MAX13487EESA | 2.40 |
| J1-J4 | 4 | Bloque de Terminales Tornillo 2P 5.08mm 15A | THT | Salidas de potencia a tiras LED 24V | Phoenix Contact 1729128 | 3.20 |
| J5 | 1 | Bloque de Terminales Tornillo 2P 5.08mm 20A | THT | Entrada alimentación 24VDC desde fuente | Phoenix Contact 1729128 | 1.00 |
| C1-C6 | 6 | Condensador Cerámico 10µF 50V X7R | SMD 1206 | Filtrado desacoplo de rizado PWM 20kHz | Murata GRM31CR71H106KA12L | 1.10 |
| R1-R8 | 8 | Resistencias 10Ω (Gate) + 10kΩ (Pull-down) | SMD 0805 | Control de gate y estado seguro apagado | Yageo RC0805FR | 0.40 |
| PCB | 1 | Placa de Circuito Impreso 2 Caras 2oz Cu | FR4 100x80mm | Conducción pistas alta corriente 10A | JLCPCB / PCBWay | 2.50 |
| **TOTAL** | | | | | | **28.40 EUR** |
"""
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(bom_content)

    print(f"Proyecto KiCad Dimmer Circadiano generado en: {output_dir}")
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
    out = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/01_iluminacion_circadiana_y_exterior/electrico"
    generar_kicad_iluminacion(out)
