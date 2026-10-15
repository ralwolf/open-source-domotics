#!/usr/bin/env python3
"""
generar_kicad_tablero_cgmp.py
Genera el esquema electrónico KiCad 10 (.kicad_sch), el proyecto (.kicad_pro),
la lista de materiales (BOM.md) y exporta el SVG del circuito para el
Módulo de Telemetría y Supervisión del Cuadro General (CGMP)
(ESP32-S3 + ZMPT101B + Contactos Auxiliares SPD/IGA + RS485 Modbus + Bobina Emisión).
"""

import os
import subprocess

KICAD_SCH_TEMPLATE = """(kicad_sch (version 20240108) (generator "open-source-domotics-cgmp-gen")
  (uuid "b2300101-7fa5-4223-8d2b-cgmp00000001")
  (paper "A3")
  (lib_symbols
    (symbol "ESP32-S3-WROOM-1" (in_bom yes) (on_board yes)
      (property "Reference" "U1" (at 0 0 0))
      (property "Value" "ESP32-S3-WROOM-1" (at 0 -2.54 0))
      (property "Footprint" "RF_Module:ESP32-S3-WROOM-1" (at 0 -5.08 0))
    )
    (symbol "ZMPT101B_Triple" (in_bom yes) (on_board yes)
      (property "Reference" "U2" (at 0 0 0))
      (property "Value" "ZMPT101B (Medicion Tension L1/L2/L3)" (at 0 -2.54 0))
      (property "Footprint" "Module:ZMPT101B_Voltage_Sensor_Module" (at 0 -5.08 0))
    )
    (symbol "PC817_Dual" (in_bom yes) (on_board yes)
      (property "Reference" "U3" (at 0 0 0))
      (property "Value" "PC817 (Aislador Contacto Auxiliar SPD y IGA)" (at 0 -2.54 0))
      (property "Footprint" "Package_DIP:DIP-8_W7.62mm" (at 0 -5.08 0))
    )
    (symbol "SP3485_RS485" (in_bom yes) (on_board yes)
      (property "Reference" "U4" (at 0 0 0))
      (property "Value" "SP3485 (Transceptor RS485 Modbus RTU)" (at 0 -2.54 0))
      (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 0 -5.08 0))
    )
    (symbol "HLK-PM01" (in_bom yes) (on_board yes)
      (property "Reference" "PS1" (at 0 0 0))
      (property "Value" "HLK-PM01 (230VAC a 5VDC)" (at 0 -2.54 0))
      (property "Footprint" "Converter_ACDC:Converter_ACDC_HiLink_HLK-PMxx" (at 0 -5.08 0))
    )
    (symbol "Relay_Bobina_Disparo" (in_bom yes) (on_board yes)
      (property "Reference" "RL1" (at 0 0 0))
      (property "Value" "HF32FV-G (Rele Bobina Emision Disparo IGA)" (at 0 -2.54 0))
      (property "Footprint" "Relay_THT:Relay_SPST_Hongfa_HF32FV" (at 0 -5.08 0))
    )
    (symbol "DS18B20_Embarrado" (in_bom yes) (on_board yes)
      (property "Reference" "J2" (at 0 0 0))
      (property "Value" "DS18B20 (Sonda Termica Embarrado)" (at 0 -2.54 0))
      (property "Footprint" "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" (at 0 -5.08 0))
    )
    (symbol "Screw_Terminal_CGMP" (in_bom yes) (on_board yes)
      (property "Reference" "J1" (at 0 0 0))
      (property "Value" "Bornero Telemetria CGMP" (at 0 -2.54 0))
      (property "Footprint" "TerminalBlock:TerminalBlock_bornier-8_P5.08mm" (at 0 -5.08 0))
    )
  )

  (symbol (lib_id "ESP32-S3-WROOM-1") (at 120 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "b2300101-7fa5-4223-8d2b-esp32cgmp001")
    (property "Reference" "U1" (at 120 60 0))
    (property "Value" "ESP32-S3-WROOM-1" (at 120 63 0))
    (property "Footprint" "RF_Module:ESP32-S3-WROOM-1" (at 120 66 0))
  )

  (symbol (lib_id "HLK-PM01") (at 45 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "b2300101-7fa5-4223-8d2b-hlkcgmp00001")
    (property "Reference" "PS1" (at 45 42 0))
    (property "Value" "HLK-PM01" (at 45 45 0))
    (property "Footprint" "Converter_ACDC:Converter_ACDC_HiLink_HLK-PMxx" (at 45 48 0))
  )

  (symbol (lib_id "ZMPT101B_Triple") (at 45 110 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "b2300101-7fa5-4223-8d2b-zmptcgmp0001")
    (property "Reference" "U2" (at 45 95 0))
    (property "Value" "ZMPT101B" (at 45 98 0))
    (property "Footprint" "Module:ZMPT101B_Voltage_Sensor_Module" (at 45 101 0))
  )

  (symbol (lib_id "PC817_Dual") (at 45 150 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "b2300101-7fa5-4223-8d2b-pc817cgmp001")
    (property "Reference" "U3" (at 45 135 0))
    (property "Value" "PC817 Dual" (at 45 138 0))
    (property "Footprint" "Package_DIP:DIP-8_W7.62mm" (at 45 141 0))
  )

  (symbol (lib_id "SP3485_RS485") (at 190 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "b2300101-7fa5-4223-8d2b-rs485cgmp001")
    (property "Reference" "U4" (at 190 45 0))
    (property "Value" "SP3485" (at 190 48 0))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 190 51 0))
  )

  (symbol (lib_id "Relay_Bobina_Disparo") (at 190 110 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "b2300101-7fa5-4223-8d2b-relecgmp0001")
    (property "Reference" "RL1" (at 190 95 0))
    (property "Value" "HF32FV-G" (at 190 98 0))
    (property "Footprint" "Relay_THT:Relay_SPST_Hongfa_HF32FV" (at 190 101 0))
  )

  (symbol (lib_id "DS18B20_Embarrado") (at 120 150 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "b2300101-7fa5-4223-8d2b-ds18bcgmp001")
    (property "Reference" "J2" (at 120 135 0))
    (property "Value" "DS18B20" (at 120 138 0))
    (property "Footprint" "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" (at 120 141 0))
  )

  (symbol (lib_id "Screw_Terminal_CGMP") (at 250 95 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "b2300101-7fa5-4223-8d2b-termcgmp0001")
    (property "Reference" "J1" (at 250 78 0))
    (property "Value" "Bornero CGMP" (at 250 81 0))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-8_P5.08mm" (at 250 84 0))
  )

  (wire (pts (xy 45 60) (xy 120 80))
    (stroke (width 0.254) (type solid))
    (uuid "b2300101-7fa5-4223-8d2b-wire00000001")
  )
  (wire (pts (xy 45 110) (xy 120 80))
    (stroke (width 0.254) (type solid))
    (uuid "b2300101-7fa5-4223-8d2b-wire00000002")
  )
  (wire (pts (xy 45 150) (xy 120 80))
    (stroke (width 0.254) (type solid))
    (uuid "b2300101-7fa5-4223-8d2b-wire00000003")
  )
  (wire (pts (xy 120 150) (xy 120 80))
    (stroke (width 0.254) (type solid))
    (uuid "b2300101-7fa5-4223-8d2b-wire00000004")
  )
  (wire (pts (xy 120 80) (xy 190 60))
    (stroke (width 0.254) (type solid))
    (uuid "b2300101-7fa5-4223-8d2b-wire00000005")
  )
  (wire (pts (xy 120 80) (xy 190 110))
    (stroke (width 0.254) (type solid))
    (uuid "b2300101-7fa5-4223-8d2b-wire00000006")
  )
  (wire (pts (xy 190 60) (xy 250 95))
    (stroke (width 0.254) (type solid))
    (uuid "b2300101-7fa5-4223-8d2b-wire00000007")
  )
  (wire (pts (xy 190 110) (xy 250 95))
    (stroke (width 0.254) (type solid))
    (uuid "b2300101-7fa5-4223-8d2b-wire00000008")
  )

  (text "SUPERVISOR Y TELEMETRIA CUADRO GENERAL CGMP\\nESP32-S3 + ZMPT101B + AUX SPD/IGA + RS485 MODBUS RTU + DISPARO REMOTO"
    (at 50 175 0)
    (effects (font (size 3.5 3.5)) (justify left bottom))
    (uuid "b2300101-7fa5-4223-8d2b-title0000001")
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
    "filename": "controlador_telemetria_cuadro_cgmp.kicad_pro",
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
      "b2300101-7fa5-4223-8d2b-cgmp00000001",
      ""
    ]
  ],
  "text_variables": {}
}
"""

BOM_CONTENT = """# Lista de Materiales (BOM) - Telemetría y Supervisión CGMP

| Referencia | Componente | Descripción | Encapsulado | Cantidad | Función Principal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-S3-WROOM-1 | Microcontrolador Dual-Core 240MHz Wi-Fi/BLE con 8MB Flash | SMD RF Module | 1 | Procesamiento local y telemetría de red eléctrica |
| **U2** | ZMPT101B (x3) | Transformadores de tensión activos de ultra-alta precisión | Módulo PCB THT | 3 | Lectura analógica de tensión RMS en L1, L2 y L3 |
| **U3** | PC817 (x2) | Optoacopladores de aislamiento galvánico 5kV | DIP-8 | 1 | Supervisión de contactos auxiliares de disparo SPD y IGA |
| **U4** | SP3485 | Transceptor diferencial RS485 half-duplex 3.3V | SOIC-8 | 1 | Bus Modbus RTU para integración de analizador de redes MID |
| **PS1** | Hi-Link HLK-PM01 | Fuente conmutada encapsulada 230VAC a 5VDC 3W | Módulo THT | 1 | Alimentación primaria del módulo en carril DIN |
| **RL1** | Hongfa HF32FV-G | Relé de alta capacidad 16A 250VAC | THT SPST | 1 | Disparo de bobina de emisión por sobretensión persistente |
| **J2** | DS18B20 | Sonda de temperatura digital 1-Wire TO-92 | Conector 3 pines | 1 | Termometría de contacto en embarrado principal de cobre |
| **J1** | Dinkle 5.08mm | Bornero de tornillo enchufable 8 polos | THT 5.08mm | 1 | Conexiones de señal externa, RS485 y contactos secos |
| **MOV1-3** | S14K275 | Varistores de óxido metálico de protección fina secundaria | Radial 14mm | 3 | Supresión de micro-sobretensiones en entradas de medida |
"""

def generar_kicad_cgmp():
    base_dir = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/07_tableros_distribucion_y_protecciones/electrico"
    svg_dir = os.path.join(base_dir, "esquema_svg")
    os.makedirs(svg_dir, exist_ok=True)

    sch_path = os.path.join(base_dir, "controlador_telemetria_cuadro_cgmp.kicad_sch")
    pro_path = os.path.join(base_dir, "controlador_telemetria_cuadro_cgmp.kicad_pro")
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

    # Exportar SVG con kicad-cli vía flatpak
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
    generar_kicad_cgmp()
