#!/usr/bin/env python3
"""
generar_kicad_solar_pv.py
Genera el esquema electrónico KiCad 10 (.kicad_sch), el proyecto (.kicad_pro),
la lista de materiales (BOM.md) y exporta el SVG del circuito para la
Caja Combinadora y Telemetría Solar Fotovoltaica
(ESP32-S3 + ACS758 50A + Divisor DC 600V + Aux SPD DC 1000V + SHT31).
"""

import os
import subprocess

KICAD_SCH_TEMPLATE = """(kicad_sch (version 20240108) (generator "open-source-domotics-pv-gen")
  (uuid "c3400101-6ba4-4334-9e3c-solp00000001")
  (paper "A3")
  (lib_symbols
    (symbol "ESP32-S3-WROOM-1" (in_bom yes) (on_board yes)
      (property "Reference" "U1" (at 0 0 0))
      (property "Value" "ESP32-S3-WROOM-1" (at 0 -2.54 0))
      (property "Footprint" "RF_Module:ESP32-S3-WROOM-1" (at 0 -5.08 0))
    )
    (symbol "ACS758LCB-050B" (in_bom yes) (on_board yes)
      (property "Reference" "U2" (at 0 0 0))
      (property "Value" "ACS758LCB-050B (Sensor Efecto Hall 50A DC)" (at 0 -2.54 0))
      (property "Footprint" "Sensor_Current:Allegro_CB_PFF" (at 0 -5.08 0))
    )
    (symbol "PC817_SPD_DC" (in_bom yes) (on_board yes)
      (property "Reference" "U3" (at 0 0 0))
      (property "Value" "PC817 (Aislador Contacto Auxiliar SPD DC)" (at 0 -2.54 0))
      (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 0 -5.08 0))
    )
    (symbol "SHT31_Panel" (in_bom yes) (on_board yes)
      (property "Reference" "U4" (at 0 0 0))
      (property "Value" "SHT31-DIS (Temp Cara Posterior Panel)" (at 0 -2.54 0))
      (property "Footprint" "Package_DFN_QFN:DFN-8-1EP_2.5x2.5mm_P0.5mm_EP1.4x1.7mm" (at 0 -5.08 0))
    )
    (symbol "HLK-PM01" (in_bom yes) (on_board yes)
      (property "Reference" "PS1" (at 0 0 0))
      (property "Value" "HLK-PM01 (230VAC/DC a 5VDC)" (at 0 -2.54 0))
      (property "Footprint" "Converter_ACDC:Converter_ACDC_HiLink_HLK-PMxx" (at 0 -5.08 0))
    )
    (symbol "Fuse_gPV_1000V" (in_bom yes) (on_board yes)
      (property "Reference" "F1" (at 0 0 0))
      (property "Value" "Fusible gPV 10x38 1000VDC 15A" (at 0 -2.54 0))
      (property "Footprint" "Fuse:Fuseholder_Cylinder-10x38mm_Schurter_ESO" (at 0 -5.08 0))
    )
    (symbol "SPD_DC_1000V" (in_bom yes) (on_board yes)
      (property "Reference" "SPD1" (at 0 0 0))
      (property "Value" "Descargador SPD Tipo II DC 1000V 40kA" (at 0 -2.54 0))
      (property "Footprint" "Module:DIN_Rail_2_Modules" (at 0 -5.08 0))
    )
    (symbol "Screw_Terminal_PV" (in_bom yes) (on_board yes)
      (property "Reference" "J1" (at 0 0 0))
      (property "Value" "Bornero Potencia DC Strings" (at 0 -2.54 0))
      (property "Footprint" "TerminalBlock:TerminalBlock_bornier-6_P5.08mm" (at 0 -5.08 0))
    )
  )

  (symbol (lib_id "ESP32-S3-WROOM-1") (at 120 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "c3400101-6ba4-4334-9e3c-esp32pv00001")
    (property "Reference" "U1" (at 120 60 0))
    (property "Value" "ESP32-S3-WROOM-1" (at 120 63 0))
    (property "Footprint" "RF_Module:ESP32-S3-WROOM-1" (at 120 66 0))
  )

  (symbol (lib_id "Fuse_gPV_1000V") (at 45 40 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "c3400101-6ba4-4334-9e3c-fusepv000001")
    (property "Reference" "F1" (at 45 28 0))
    (property "Value" "gPV 1000V 15A" (at 45 31 0))
    (property "Footprint" "Fuse:Fuseholder_Cylinder-10x38mm_Schurter_ESO" (at 45 34 0))
  )

  (symbol (lib_id "SPD_DC_1000V") (at 45 70 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "c3400101-6ba4-4334-9e3c-spddc0000001")
    (property "Reference" "SPD1" (at 45 58 0))
    (property "Value" "SPD DC 1000V" (at 45 61 0))
    (property "Footprint" "Module:DIN_Rail_2_Modules" (at 45 64 0))
  )

  (symbol (lib_id "ACS758LCB-050B") (at 45 110 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "c3400101-6ba4-4334-9e3c-acs758000001")
    (property "Reference" "U2" (at 45 95 0))
    (property "Value" "ACS758-050B" (at 45 98 0))
    (property "Footprint" "Sensor_Current:Allegro_CB_PFF" (at 45 101 0))
  )

  (symbol (lib_id "PC817_SPD_DC") (at 45 150 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "c3400101-6ba4-4334-9e3c-pc817pv00001")
    (property "Reference" "U3" (at 45 135 0))
    (property "Value" "PC817" (at 45 138 0))
    (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 45 141 0))
  )

  (symbol (lib_id "SHT31_Panel") (at 120 140 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "c3400101-6ba4-4334-9e3c-sht31pv00001")
    (property "Reference" "U4" (at 120 125 0))
    (property "Value" "SHT31" (at 120 128 0))
    (property "Footprint" "Package_DFN_QFN:DFN-8-1EP_2.5x2.5mm_P0.5mm_EP1.4x1.7mm" (at 120 131 0))
  )

  (symbol (lib_id "HLK-PM01") (at 190 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "c3400101-6ba4-4334-9e3c-hlkpv0000001")
    (property "Reference" "PS1" (at 190 42 0))
    (property "Value" "HLK-PM01" (at 190 45 0))
    (property "Footprint" "Converter_ACDC:Converter_ACDC_HiLink_HLK-PMxx" (at 190 48 0))
  )

  (symbol (lib_id "Screw_Terminal_PV") (at 250 95 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "c3400101-6ba4-4334-9e3c-termpv000001")
    (property "Reference" "J1" (at 250 78 0))
    (property "Value" "Bornero Strings PV" (at 250 81 0))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-6_P5.08mm" (at 250 84 0))
  )

  (wire (pts (xy 45 40) (xy 45 70))
    (stroke (width 0.254) (type solid))
    (uuid "c3400101-6ba4-4334-9e3c-wire00000001")
  )
  (wire (pts (xy 45 70) (xy 45 110))
    (stroke (width 0.254) (type solid))
    (uuid "c3400101-6ba4-4334-9e3c-wire00000002")
  )
  (wire (pts (xy 45 110) (xy 120 80))
    (stroke (width 0.254) (type solid))
    (uuid "c3400101-6ba4-4334-9e3c-wire00000003")
  )
  (wire (pts (xy 45 150) (xy 120 80))
    (stroke (width 0.254) (type solid))
    (uuid "c3400101-6ba4-4334-9e3c-wire00000004")
  )
  (wire (pts (xy 120 140) (xy 120 80))
    (stroke (width 0.254) (type solid))
    (uuid "c3400101-6ba4-4334-9e3c-wire00000005")
  )
  (wire (pts (xy 120 80) (xy 190 60))
    (stroke (width 0.254) (type solid))
    (uuid "c3400101-6ba4-4334-9e3c-wire00000006")
  )
  (wire (pts (xy 120 80) (xy 250 95))
    (stroke (width 0.254) (type solid))
    (uuid "c3400101-6ba4-4334-9e3c-wire00000007")
  )

  (text "CAJA COMBINADORA Y TELEMETRIA SOLAR FOTOVOLTAICA DC\\nESP32-S3 + ACS758 50A + DIVISOR DC 600V + SPD DC 1000V + SHT31"
    (at 50 175 0)
    (effects (font (size 3.5 3.5)) (justify left bottom))
    (uuid "c3400101-6ba4-4334-9e3c-title0000001")
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
    "filename": "combinador_telemetria_pv.kicad_pro",
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
      "c3400101-6ba4-4334-9e3c-solp00000001",
      ""
    ]
  ],
  "text_variables": {}
}
"""

BOM_CONTENT = """# Lista de Materiales (BOM) - Caja Combinadora y Telemetría Solar PV

| Referencia | Componente | Descripción | Encapsulado | Cantidad | Función Principal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-S3-WROOM-1 | Microcontrolador Wi-Fi/BLE Dual Core 240MHz 8MB Flash | SMD RF Module | 1 | Cálculo de potencia DC, algoritmo MPPT y enlace ESPHome |
| **U2** | ACS758LCB-050B-PFF-T | Sensor de corriente por efecto Hall galvanicamente aislado 50A | Allegro CB PFF | 1 | Medición bidireccional continua de amperaje del string fotovoltaico |
| **U3** | PC817 | Optoacoplador de aislamiento 5kV | DIP-4 | 1 | Supervisión del contacto auxiliar del descargador SPD DC |
| **U4** | SHT31-DIS | Sensor digital de temperatura y humedad (±0.2°C) | DFN-8 | 1 | Telemetría térmica de cara posterior para cálculo de pérdidas térmicas |
| **SPD1** | SPD DC Tipo II | Protector contra sobretensiones transitorias 1000V DC 40kA | Carril DIN 2M | 1 | Desvío seguro a tierra de inducciones de rayo en strings |
| **F1-F2** | gPV 10x38 15A 1000V | Fusibles cerámicos especiales para protección fotovoltaica | Cilindro 10x38mm | 2 | Protección contra corrientes inversas de defecto |
| **PS1** | Hi-Link HLK-PM01 | Convertidor conmutado 230VAC a 5VDC 3W | Módulo THT | 1 | Alimentación electrónica interna del combinador |
| **R1-R6** | 1MΩ 1% 250V (x6) | Cadena de resistencias de alta tensión para divisor | SMD 1206 | 6 | Reducción de escala de tensión DC hasta 600V para entrada ADC |
| **R7** | 33kΩ 0.1% | Resistencia de precisión parte baja divisor | SMD 0805 | 1 | Ajuste fino de ganancia de lectura de tensión DC |
| **J1** | Phoenix Contact 7.62mm | Bornero de potencia para cable solar de 6 mm² (PV1-F) | THT 7.62mm | 1 | Entrada y salida de strings fotovoltaicos |
"""

def generar_kicad_pv():
    base_dir = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/03_solar_fotovoltaica/electrico"
    svg_dir = os.path.join(base_dir, "esquema_svg")
    os.makedirs(svg_dir, exist_ok=True)

    sch_path = os.path.join(base_dir, "combinador_telemetria_pv.kicad_sch")
    pro_path = os.path.join(base_dir, "combinador_telemetria_pv.kicad_pro")
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
    generar_kicad_pv()
