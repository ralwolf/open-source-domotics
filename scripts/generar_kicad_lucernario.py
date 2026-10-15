#!/usr/bin/env python3
"""
generar_kicad_lucernario.py
Genera el esquema electrónico KiCad 10 (.kicad_sch), el proyecto (.kicad_pro),
la lista de materiales (BOM.md) y exporta el SVG del circuito para el
Controlador Bioclimático del Lucernario Cenital
(ESP32-S3 + Puente H 24V Actuadores Lineales + Sensor Lluvia Óptico + Anemómetro + SHT31).
"""

import os
import subprocess

KICAD_SCH_TEMPLATE = """(kicad_sch (version 20240108) (generator "open-source-domotics-lucernario-gen")
  (uuid "f6700101-3ba1-4667-8f6f-luce00000001")
  (paper "A3")
  (lib_symbols
    (symbol "ESP32-S3-WROOM-1" (in_bom yes) (on_board yes)
      (property "Reference" "U1" (at 0 0 0))
      (property "Value" "ESP32-S3-WROOM-1" (at 0 -2.54 0))
      (property "Footprint" "RF_Module:ESP32-S3-WROOM-1" (at 0 -5.08 0))
    )
    (symbol "LMD18200_HBridge" (in_bom yes) (on_board yes)
      (property "Reference" "U2" (at 0 0 0))
      (property "Value" "LMD18200 (Puente H 24V 3A Actuadores)" (at 0 -2.54 0))
      (property "Footprint" "Package_TO_SOT_THT:TO-220-11_P3.4mm_StaggerOdd_Lead5.08mm_Vertical" (at 0 -5.08 0))
    )
    (symbol "Rain_Sensor_Optic" (in_bom yes) (on_board yes)
      (property "Reference" "U3" (at 0 0 0))
      (property "Value" "Sensor Lluvia Optico RG-11" (at 0 -2.54 0))
      (property "Footprint" "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" (at 0 -5.08 0))
    )
    (symbol "Anemometer_Pulses" (in_bom yes) (on_board yes)
      (property "Reference" "J2" (at 0 0 0))
      (property "Value" "Anemometro Pulsos Viento" (at 0 -2.54 0))
      (property "Footprint" "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" (at 0 -5.08 0))
    )
    (symbol "IRM-15-24" (in_bom yes) (on_board yes)
      (property "Reference" "PS1" (at 0 0 0))
      (property "Value" "Mean Well IRM-15-24 (230VAC a 24VDC)" (at 0 -2.54 0))
      (property "Footprint" "Converter_ACDC:Converter_ACDC_MeanWell_IRM-15-xx_THT" (at 0 -5.08 0))
    )
    (symbol "Screw_Terminal_Lucernario" (in_bom yes) (on_board yes)
      (property "Reference" "J1" (at 0 0 0))
      (property "Value" "Bornero Motores & Sensores" (at 0 -2.54 0))
      (property "Footprint" "TerminalBlock:TerminalBlock_bornier-8_P5.08mm" (at 0 -5.08 0))
    )
  )

  (symbol (lib_id "ESP32-S3-WROOM-1") (at 120 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f6700101-3ba1-4667-8f6f-esp32luce0001")
    (property "Reference" "U1" (at 120 60 0))
    (property "Value" "ESP32-S3-WROOM-1" (at 120 63 0))
    (property "Footprint" "RF_Module:ESP32-S3-WROOM-1" (at 120 66 0))
  )

  (symbol (lib_id "IRM-15-24") (at 45 45 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f6700101-3ba1-4667-8f6f-psu24luce0001")
    (property "Reference" "PS1" (at 45 28 0))
    (property "Value" "Mean Well IRM-15-24" (at 45 31 0))
    (property "Footprint" "Converter_ACDC:Converter_ACDC_MeanWell_IRM-15-xx_THT" (at 45 34 0))
  )

  (symbol (lib_id "Rain_Sensor_Optic") (at 45 90 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f6700101-3ba1-4667-8f6f-rainrg1100001")
    (property "Reference" "U3" (at 45 75 0))
    (property "Value" "Sensor Lluvia RG-11" (at 45 78 0))
    (property "Footprint" "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" (at 45 81 0))
  )

  (symbol (lib_id "Anemometer_Pulses") (at 45 135 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f6700101-3ba1-4667-8f6f-anemom0000001")
    (property "Reference" "J2" (at 45 120 0))
    (property "Value" "Anemometro Pulsos" (at 45 123 0))
    (property "Footprint" "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" (at 45 126 0))
  )

  (symbol (lib_id "LMD18200_HBridge") (at 190 75 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f6700101-3ba1-4667-8f6f-hbridg0000001")
    (property "Reference" "U2" (at 190 60 0))
    (property "Value" "LMD18200" (at 190 63 0))
    (property "Footprint" "Package_TO_SOT_THT:TO-220-11_P3.4mm_StaggerOdd_Lead5.08mm_Vertical" (at 190 66 0))
  )

  (symbol (lib_id "Screw_Terminal_Lucernario") (at 250 90 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f6700101-3ba1-4667-8f6f-termluce00001")
    (property "Reference" "J1" (at 250 72 0))
    (property "Value" "Bornero Lucernario" (at 250 75 0))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-8_P5.08mm" (at 250 78 0))
  )

  (wire (pts (xy 45 45) (xy 120 80))
    (stroke (width 0.254) (type solid))
    (uuid "f6700101-3ba1-4667-8f6f-wire00000001")
  )
  (wire (pts (xy 45 90) (xy 120 80))
    (stroke (width 0.254) (type solid))
    (uuid "f6700101-3ba1-4667-8f6f-wire00000002")
  )
  (wire (pts (xy 45 135) (xy 120 80))
    (stroke (width 0.254) (type solid))
    (uuid "f6700101-3ba1-4667-8f6f-wire00000003")
  )
  (wire (pts (xy 120 80) (xy 190 75))
    (stroke (width 0.254) (type solid))
    (uuid "f6700101-3ba1-4667-8f6f-wire00000004")
  )
  (wire (pts (xy 190 75) (xy 250 90))
    (stroke (width 0.254) (type solid))
    (uuid "f6700101-3ba1-4667-8f6f-wire00000005")
  )

  (text "CONTROLADOR BIOCLIMATICO Y METEOROLOGICO DEL LUCERNARIO\\nESP32-S3 + PUENTE H 24V LMD18200 + SENSOR LLUVIA OPTICO + ANEMOMETRO"
    (at 50 170 0)
    (effects (font (size 3.5 3.5)) (justify left bottom))
    (uuid "f6700101-3ba1-4667-8f6f-title0000001")
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
    "filename": "controlador_lucernario_bioclimatico.kicad_pro",
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
      "f6700101-3ba1-4667-8f6f-luce00000001",
      ""
    ]
  ],
  "text_variables": {}
}
"""

BOM_CONTENT = """# Lista de Materiales (BOM) - Controlador Lucernario Bioclimático

| Referencia | Componente | Descripción | Encapsulado | Cantidad | Función Principal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-S3-WROOM-1 | Microcontrolador Dual-Core 240MHz Wi-Fi/BLE con 8MB Flash | SMD RF Module | 1 | Lógica de ventilación pasiva, seguridad meteorológica y MQTT |
| **U2** | LMD18200T | Puente H DMOS 55V 3A con frenado dinámico y sensado térmico | TO-220-11 | 1 | Accionamiento reversible suave de los actuadores lineales 24V |
| **U3** | Hydreon RG-11 | Sensor de lluvia óptico infrarrojo estanco para exteriores | Módulo externo | 1 | Cierre de emergencia instantáneo ante primeras gotas (<100ms) |
| **J2** | Davis / MISOL | Anemómetro de cazoletas generador de pulsos reed por vuelta | Conector 3 pines | 1 | Medición de racha de viento para cierre preventivo (>40 km/h) |
| **PS1** | Mean Well IRM-15-24 | Fuente conmutada industrial 230VAC a 24VDC 0.63A | Módulo THT | 1 | Alimentación de potencia para los motores lineales de compuerta |
| **J1** | Dinkle 5.08mm | Bornero de tornillo enchufable 8 polos | THT 5.08mm | 1 | Cableado a motores de carrera y sensores de tejado |
"""

def generar_kicad_lucernario():
    base_dir = "/home/ral/Documents/GitHub/open-source-domotics/00_diseno_arquitectonico_y_estructural/04_bioclimatica_ventilacion_lucernario_celeste/electrico"
    svg_dir = os.path.join(base_dir, "esquema_svg")
    os.makedirs(svg_dir, exist_ok=True)

    sch_path = os.path.join(base_dir, "controlador_lucernario_bioclimatico.kicad_sch")
    pro_path = os.path.join(base_dir, "controlador_lucernario_bioclimatico.kicad_pro")
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
    generar_kicad_lucernario()

