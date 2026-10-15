#!/usr/bin/env python3
"""
generar_kicad_cisterna_pluvial.py
Genera el esquema electrónico KiCad 10 (.kicad_sch), el proyecto (.kicad_pro),
la lista de materiales (BOM.md) y exporta el SVG del circuito para el
Controlador de Cisterna Pluvial y Skid de Potabilización UV-C
(ESP32-S3 + Sensor Ultrasonico JSN-SR04T + Presion 4-20mA + Monitor Balastro UV + Relé Bomba).
"""

import os
import subprocess

KICAD_SCH_TEMPLATE = """(kicad_sch (version 20240108) (generator "open-source-domotics-cisterna-gen")
  (uuid "e5600101-4ba2-4556-8e5e-cist00000001")
  (paper "A3")
  (lib_symbols
    (symbol "ESP32-S3-WROOM-1" (in_bom yes) (on_board yes)
      (property "Reference" "U1" (at 0 0 0))
      (property "Value" "ESP32-S3-WROOM-1" (at 0 -2.54 0))
      (property "Footprint" "RF_Module:ESP32-S3-WROOM-1" (at 0 -5.08 0))
    )
    (symbol "JSN-SR04T" (in_bom yes) (on_board yes)
      (property "Reference" "U2" (at 0 0 0))
      (property "Value" "JSN-SR04T (Nivel Ultrasonico Sumergible)" (at 0 -2.54 0))
      (property "Footprint" "Module:JSN-SR04T_Ultrasonic_Module" (at 0 -5.08 0))
    )
    (symbol "Receiver_4_20mA" (in_bom yes) (on_board yes)
      (property "Reference" "U3" (at 0 0 0))
      (property "Value" "Receptor Bucle 4-20mA Presion" (at 0 -2.54 0))
      (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 0 -5.08 0))
    )
    (symbol "PC817_UV_Monitor" (in_bom yes) (on_board yes)
      (property "Reference" "U4" (at 0 0 0))
      (property "Value" "PC817 (Supervision Balastro UV-C)" (at 0 -2.54 0))
      (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 0 -5.08 0))
    )
    (symbol "Relay_Bomba_Agua" (in_bom yes) (on_board yes)
      (property "Reference" "RL1" (at 0 0 0))
      (property "Value" "HF32FV-16 (Contactor Bomba Presurizadora)" (at 0 -2.54 0))
      (property "Footprint" "Relay_THT:Relay_SPST_Hongfa_HF32FV" (at 0 -5.08 0))
    )
    (symbol "HLK-PM01" (in_bom yes) (on_board yes)
      (property "Reference" "PS1" (at 0 0 0))
      (property "Value" "HLK-PM01 (230VAC a 5VDC)" (at 0 -2.54 0))
      (property "Footprint" "Converter_ACDC:Converter_ACDC_HiLink_HLK-PMxx" (at 0 -5.08 0))
    )
    (symbol "Screw_Terminal_Cisterna" (in_bom yes) (on_board yes)
      (property "Reference" "J1" (at 0 0 0))
      (property "Value" "Bornero Skid Pluvial" (at 0 -2.54 0))
      (property "Footprint" "TerminalBlock:TerminalBlock_bornier-8_P5.08mm" (at 0 -5.08 0))
    )
  )

  (symbol (lib_id "ESP32-S3-WROOM-1") (at 120 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "e5600101-4ba2-4556-8e5e-esp32cist0001")
    (property "Reference" "U1" (at 120 60 0))
    (property "Value" "ESP32-S3-WROOM-1" (at 120 63 0))
    (property "Footprint" "RF_Module:ESP32-S3-WROOM-1" (at 120 66 0))
  )

  (symbol (lib_id "HLK-PM01") (at 45 45 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "e5600101-4ba2-4556-8e5e-hlkcist000001")
    (property "Reference" "PS1" (at 45 28 0))
    (property "Value" "HLK-PM01" (at 45 31 0))
    (property "Footprint" "Converter_ACDC:Converter_ACDC_HiLink_HLK-PMxx" (at 45 34 0))
  )

  (symbol (lib_id "JSN-SR04T") (at 45 85 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "e5600101-4ba2-4556-8e5e-jsn0000000001")
    (property "Reference" "U2" (at 45 70 0))
    (property "Value" "JSN-SR04T" (at 45 73 0))
    (property "Footprint" "Module:JSN-SR04T_Ultrasonic_Module" (at 45 76 0))
  )

  (symbol (lib_id "Receiver_4_20mA") (at 45 125 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "e5600101-4ba2-4556-8e5e-rcvr420cist001")
    (property "Reference" "U3" (at 45 110 0))
    (property "Value" "4-20mA" (at 45 113 0))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 45 116 0))
  )

  (symbol (lib_id "PC817_UV_Monitor") (at 45 160 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "e5600101-4ba2-4556-8e5e-pc817uv000001")
    (property "Reference" "U4" (at 45 145 0))
    (property "Value" "PC817 UV" (at 45 148 0))
    (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 45 151 0))
  )

  (symbol (lib_id "Relay_Bomba_Agua") (at 190 75 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "e5600101-4ba2-4556-8e5e-relecist000001")
    (property "Reference" "RL1" (at 190 60 0))
    (property "Value" "HF32FV-16" (at 190 63 0))
    (property "Footprint" "Relay_THT:Relay_SPST_Hongfa_HF32FV" (at 190 66 0))
  )

  (symbol (lib_id "Screw_Terminal_Cisterna") (at 250 90 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "e5600101-4ba2-4556-8e5e-termcist000001")
    (property "Reference" "J1" (at 250 72 0))
    (property "Value" "Bornero Skid" (at 250 75 0))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-8_P5.08mm" (at 250 78 0))
  )

  (wire (pts (xy 45 45) (xy 120 80))
    (stroke (width 0.254) (type solid))
    (uuid "e5600101-4ba2-4556-8e5e-wire00000001")
  )
  (wire (pts (xy 45 85) (xy 120 80))
    (stroke (width 0.254) (type solid))
    (uuid "e5600101-4ba2-4556-8e5e-wire00000002")
  )
  (wire (pts (xy 45 125) (xy 120 80))
    (stroke (width 0.254) (type solid))
    (uuid "e5600101-4ba2-4556-8e5e-wire00000003")
  )
  (wire (pts (xy 45 160) (xy 120 80))
    (stroke (width 0.254) (type solid))
    (uuid "e5600101-4ba2-4556-8e5e-wire00000004")
  )
  (wire (pts (xy 120 80) (xy 190 75))
    (stroke (width 0.254) (type solid))
    (uuid "e5600101-4ba2-4556-8e5e-wire00000005")
  )
  (wire (pts (xy 190 75) (xy 250 90))
    (stroke (width 0.254) (type solid))
    (uuid "e5600101-4ba2-4556-8e5e-wire00000006")
  )

  (text "CONTROLADOR DE CISTERNA PLUVIAL Y SKID DE POTABILIZACION UV-C\\nESP32-S3 + JSN-SR04T ULTRASONICO + BUCLE 4-20mA PRESION + MONITOR UV-C"
    (at 50 180 0)
    (effects (font (size 3.5 3.5)) (justify left bottom))
    (uuid "e5600101-4ba2-4556-8e5e-title0000001")
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
    "filename": "controlador_potabilizacion_pluvial.kicad_pro",
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
      "e5600101-4ba2-4556-8e5e-cist00000001",
      ""
    ]
  ],
  "text_variables": {}
}
"""

BOM_CONTENT = """# Lista de Materiales (BOM) - Controlador Cisterna y Skid Potabilización

| Referencia | Componente | Descripción | Encapsulado | Cantidad | Función Principal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-S3-WROOM-1 | Microcontrolador Dual-Core 240MHz Wi-Fi/BLE con 8MB Flash | SMD RF Module | 1 | Telemetría de nivel pluvial, gestión de presión y esterilización |
| **U2** | JSN-SR04T | Sensor de distancia ultrasónico estanco IP67 con sonda cableada | Módulo PCB | 1 | Medición sin contacto de nivel de agua en cisterna (20 cm a 450 cm) |
| **U3** | RCV420 / Shunt 150Ω | Receptor de bucle de corriente 4-20mA de precisión con filtro | SOIC-8 | 1 | Interfaz para transductor de presión hidrostática de línea (0-6 bar) |
| **U4** | PC817 | Optoacoplador de aislamiento galvánico 5kV | DIP-4 | 1 | Supervisión del estado operativo del balastro de la lámpara UV-C |
| **RL1** | Hongfa HF32FV-16 | Relé electromecánico de potencia 16A 250VAC | THT SPST | 1 | Conmutación de contactor de la electrobomba de presurización |
| **PS1** | Hi-Link HLK-PM01 | Fuente compacta 230VAC a 5VDC 3W | Módulo THT | 1 | Alimentación de bajo consumo para lógica electrónica |
| **J1** | Dinkle 5.08mm | Bornero de tornillo enchufable 8 polos | THT 5.08mm | 1 | Conexión de alimentación, sensores analógicos y bomba |
"""

def generar_kicad_cisterna():
    base_dir = "/home/ral/Documents/GitHub/open-source-domotics/00_diseno_arquitectonico_y_estructural/07_captacion_pluvial_cisterna_y_potabilizacion/electrico"
    svg_dir = os.path.join(base_dir, "esquema_svg")
    os.makedirs(svg_dir, exist_ok=True)

    sch_path = os.path.join(base_dir, "controlador_potabilizacion_pluvial.kicad_sch")
    pro_path = os.path.join(base_dir, "controlador_potabilizacion_pluvial.kicad_pro")
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
    generar_kicad_cisterna()
