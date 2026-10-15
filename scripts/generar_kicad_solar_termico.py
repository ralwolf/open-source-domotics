#!/usr/bin/env python3
"""
generar_kicad_solar_termico.py
Genera el esquema electrónico KiCad 10 (.kicad_sch), el proyecto (.kicad_pro),
la lista de materiales (BOM.md) y exporta el SVG del circuito para el
Controlador Diferencial Solar Térmico y Calefacción
(ESP32-S3 + Cuádruple MAX31865 PT1000 + Driver Bomba PWM 0-10V + Relé Válvula 3 Vías).
"""

import os
import subprocess

KICAD_SCH_TEMPLATE = """(kicad_sch (version 20240108) (generator "open-source-domotics-solar-term-gen")
  (uuid "d4500101-5ca3-4445-8f4d-solt00000001")
  (paper "A3")
  (lib_symbols
    (symbol "ESP32-S3-WROOM-1" (in_bom yes) (on_board yes)
      (property "Reference" "U1" (at 0 0 0))
      (property "Value" "ESP32-S3-WROOM-1" (at 0 -2.54 0))
      (property "Footprint" "RF_Module:ESP32-S3-WROOM-1" (at 0 -5.08 0))
    )
    (symbol "MAX31865_Quad" (in_bom yes) (on_board yes)
      (property "Reference" "U2" (at 0 0 0))
      (property "Value" "MAX31865 (SPI RTD PT1000 Colector y Tanque)" (at 0 -2.54 0))
      (property "Footprint" "Package_SO:SSOP-20_5.3x7.2mm_P0.65mm" (at 0 -5.08 0))
    )
    (symbol "LM358_0_10V" (in_bom yes) (on_board yes)
      (property "Reference" "U3" (at 0 0 0))
      (property "Value" "LM358 (Driver PWM a 0-10V Bomba Solar)" (at 0 -2.54 0))
      (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 0 -5.08 0))
    )
    (symbol "Relay_Valvula_3Vias" (in_bom yes) (on_board yes)
      (property "Reference" "RL1" (at 0 0 0))
      (property "Value" "HF32FV-16 (Valvula Mezcladora 3 Vias)" (at 0 -2.54 0))
      (property "Footprint" "Relay_THT:Relay_SPDT_Hongfa_HF32FV" (at 0 -5.08 0))
    )
    (symbol "HLK-PM01" (in_bom yes) (on_board yes)
      (property "Reference" "PS1" (at 0 0 0))
      (property "Value" "HLK-PM01 (230VAC a 5VDC)" (at 0 -2.54 0))
      (property "Footprint" "Converter_ACDC:Converter_ACDC_HiLink_HLK-PMxx" (at 0 -5.08 0))
    )
    (symbol "Screw_Terminal_SolarT" (in_bom yes) (on_board yes)
      (property "Reference" "J1" (at 0 0 0))
      (property "Value" "Bornero PT1000 & Bomba Solar" (at 0 -2.54 0))
      (property "Footprint" "TerminalBlock:TerminalBlock_bornier-8_P5.08mm" (at 0 -5.08 0))
    )
  )

  (symbol (lib_id "ESP32-S3-WROOM-1") (at 120 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "d4500101-5ca3-4445-8f4d-esp32st00001")
    (property "Reference" "U1" (at 120 60 0))
    (property "Value" "ESP32-S3-WROOM-1" (at 120 63 0))
    (property "Footprint" "RF_Module:ESP32-S3-WROOM-1" (at 120 66 0))
  )

  (symbol (lib_id "HLK-PM01") (at 45 50 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "d4500101-5ca3-4445-8f4d-hlkst0000001")
    (property "Reference" "PS1" (at 45 32 0))
    (property "Value" "HLK-PM01" (at 45 35 0))
    (property "Footprint" "Converter_ACDC:Converter_ACDC_HiLink_HLK-PMxx" (at 45 38 0))
  )

  (symbol (lib_id "MAX31865_Quad") (at 45 100 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "d4500101-5ca3-4445-8f4d-maxrtd000001")
    (property "Reference" "U2" (at 45 85 0))
    (property "Value" "MAX31865 Quad" (at 45 88 0))
    (property "Footprint" "Package_SO:SSOP-20_5.3x7.2mm_P0.65mm" (at 45 91 0))
  )

  (symbol (lib_id "LM358_0_10V") (at 190 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "d4500101-5ca3-4445-8f4d-lm358st00001")
    (property "Reference" "U3" (at 190 45 0))
    (property "Value" "LM358 0-10V" (at 190 48 0))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 190 51 0))
  )

  (symbol (lib_id "Relay_Valvula_3Vias") (at 190 110 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "d4500101-5ca3-4445-8f4d-relest000001")
    (property "Reference" "RL1" (at 190 95 0))
    (property "Value" "HF32FV-16" (at 190 98 0))
    (property "Footprint" "Relay_THT:Relay_SPDT_Hongfa_HF32FV" (at 190 101 0))
  )

  (symbol (lib_id "Screw_Terminal_SolarT") (at 250 90 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "d4500101-5ca3-4445-8f4d-termst000001")
    (property "Reference" "J1" (at 250 72 0))
    (property "Value" "Bornero Solar Termico" (at 250 75 0))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-8_P5.08mm" (at 250 78 0))
  )

  (wire (pts (xy 45 50) (xy 120 80))
    (stroke (width 0.254) (type solid))
    (uuid "d4500101-5ca3-4445-8f4d-wire00000001")
  )
  (wire (pts (xy 45 100) (xy 120 80))
    (stroke (width 0.254) (type solid))
    (uuid "d4500101-5ca3-4445-8f4d-wire00000002")
  )
  (wire (pts (xy 120 80) (xy 190 60))
    (stroke (width 0.254) (type solid))
    (uuid "d4500101-5ca3-4445-8f4d-wire00000003")
  )
  (wire (pts (xy 120 80) (xy 190 110))
    (stroke (width 0.254) (type solid))
    (uuid "d4500101-5ca3-4445-8f4d-wire00000004")
  )
  (wire (pts (xy 190 60) (xy 250 90))
    (stroke (width 0.254) (type solid))
    (uuid "d4500101-5ca3-4445-8f4d-wire00000005")
  )
  (wire (pts (xy 190 110) (xy 250 90))
    (stroke (width 0.254) (type solid))
    (uuid "d4500101-5ca3-4445-8f4d-wire00000006")
  )

  (text "CONTROLADOR DIFERENCIAL SOLAR TERMICO Y PISO RADIANTE\\nESP32-S3 + 4x MAX31865 PT1000 + DRIVER BOMBA PWM 0-10V + RELÉ VALVULA 3 VIAS"
    (at 50 165 0)
    (effects (font (size 3.5 3.5)) (justify left bottom))
    (uuid "d4500101-5ca3-4445-8f4d-title0000001")
  )
)
"""

KICAD_PRO_CONTENT = """{
  "boards": [],
  "cvpcb": {
    "equivalence_files": []
  },
  "erc": {
    "erc_exclusions": [],
    "meta": {
      "version": 2
    },
    "rule_severities": {}
  },
  "libraries": {
    "pinned_footprint_libs": [],
    "pinned_symbol_libs": []
  },
  "meta": {
    "filename": "controlador_diferencial_solar.kicad_pro",
    "version": 1
  },
  "net_settings": {
    "classes": [
      {
        "bus_width": 12,
        "clearance": 0.2,
        "diff_pair_gap": 0.25,
        "diff_pair_via_gap": 0.25,
        "line_style": 0,
        "microvia_diameter": 0.3,
        "microvia_drill": 0.1,
        "name": "Default",
        "pcb_color": "rgba(0, 0, 0, 0.000)",
        "schematic_color": "rgba(0, 0, 0, 0.000)",
        "track_width": 0.25,
        "via_diameter": 0.8,
        "via_drill": 0.4,
        "wire_width": 6
      }
    ]
  },
  "pcbnew": {
    "last_paths": {
      "gencad": "",
      "idf": "",
      "netlist": "",
      "specctra_dsn": "",
      "step": "",
      "svg": "",
      "vrml": ""
    }
  },
  "schematic": {
    "annotate_start_num": 1,
    "drawing": {
      "dashed_lines_dash_length_ratio": 12.0,
      "dashed_lines_gap_length_ratio": 3.0,
      "default_line_thickness": 6.0,
      "default_text_size": 50.0,
      "field_names": [],
      "intersheets_ref_alignings": 2,
      "intersheets_ref_custom_text": "",
      "intersheets_ref_show": false,
      "intersheets_ref_show_coord": false,
      "intersheets_ref_show_parent": false,
      "junction_size_choice": 3,
      "label_size_ratio": 0.375,
      "pin_symbol_size": 25.0,
      "text_offset_ratio": 0.15
    },
    "legacy_lib_dir": "",
    "legacy_lib_list": [],
    "meta": {
      "version": 1
    },
    "net_format_name": "",
    "page_layout_descr_file": "",
    "plot_directory": "",
    "subsheet": {
      "border_style": 0,
      "border_width": 0.0
    }
  },
  "sheets": [
    [
      "d4500101-5ca3-4445-8f4d-solt00000001",
      ""
    ]
  ],
  "text_variables": {}
}
"""

BOM_CONTENT = """# Lista de Materiales (BOM) - Controlador Diferencial Solar Térmico

| Referencia | Componente | Descripción | Encapsulado | Cantidad | Función Principal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-S3-WROOM-1 | Microcontrolador Dual-Core 240MHz Wi-Fi/BLE con 8MB Flash | SMD RF Module | 1 | Ejecución de algoritmo diferencial ΔT y modulación de bomba |
| **U2** | MAX31865 (x4) | Convertidores digitales de precisión RTD a 15 bits por SPI | SSOP-20 | 4 | Lectura de 4 sondas PT1000 de alta temperatura (-50°C a +200°C) |
| **U3** | LM358 | Amplificador operacional dual rail-to-rail | SOIC-8 | 1 | Acondicionamiento de señal PWM a salida analógica 0-10V |
| **RL1** | Hongfa HF32FV-16 | Relé electromecánico de potencia 16A 250VAC | THT SPDT | 1 | Conmutación de válvula motorizada mezcladora de 3 vías |
| **PS1** | Hi-Link HLK-PM01 | Fuente de alimentación aislada 230VAC a 5VDC 3W | Módulo THT | 1 | Alimentación primaria del módulo en carril DIN |
| **R_REF** | 4.30kΩ 0.1% (x4) | Resistencias de referencia de película metálica ultra-precisión | SMD 0805 | 4 | Referencia de calibración ratiométrica para sondas PT1000 |
| **J1** | Dinkle 5.08mm | Bornero de tornillo enchufable 8 polos | THT 5.08mm | 1 | Conexión de sondas térmicas de inmersión y bomba solar |
"""

def generar_kicad_solar_termico():
    base_dir = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/02_solar_termico_y_calefaccion/electrico"
    svg_dir = os.path.join(base_dir, "esquema_svg")
    os.makedirs(svg_dir, exist_ok=True)

    sch_path = os.path.join(base_dir, "controlador_diferencial_solar.kicad_sch")
    pro_path = os.path.join(base_dir, "controlador_diferencial_solar.kicad_pro")
    bom_path = os.path.join(base_dir, "BOM.md")

    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(KICAD_SCH_TEMPLATE)
    with open(pro_path, "w", encoding="utf-8") as f:
        f.write(KICAD_PRO_CONTENT)
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(BOM_CONTENT)

    print(f"Esquema KiCad guardado en: {sch_path}")
    print(f"Proyecto KiCad guardado en: {pro_path}")
    print(f"BOM guardado en: {bom_path}")

    cmd = [
        "flatpak-spawn", "--host", "flatpak", "run",
        "--command=kicad-cli", "org.kicad.KiCad",
        "sch", "export", "svg",
        sch_path,
        "-o", svg_dir
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("Exportación SVG completada con éxito.")
    except Exception as e:
        print(f"Aviso al exportar SVG: {e}")

if __name__ == "__main__":
    generar_kicad_solar_termico()
