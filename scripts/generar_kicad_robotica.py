#!/usr/bin/env python3
"""
generar_kicad_robotica.py
Genera el esquema electrónico KiCad 10 (.kicad_sch), el proyecto (.kicad_pro),
la lista de materiales (BOM.md) y exporta el SVG del circuito para la
Placa de Monitorización y Seguridad de la Estación Base de Robótica de Limpieza.
"""

import os
import subprocess

KICAD_SCH_TEMPLATE = """(kicad_sch (version 20240108) (generator "open-source-domotics-robot-gen")
  (uuid "f5961808-afb8-be81-023c-robot0000001")
  (paper "A3")
  (lib_symbols
    (symbol "ESP32-C3-WROOM-02" (in_bom yes) (on_board yes)
      (property "Reference" "U1" (at 0 0 0))
      (property "Value" "ESP32-C3-WROOM-02" (at 0 -2.54 0))
      (property "Footprint" "RF_Module:ESP32-C3-WROOM-02" (at 0 -5.08 0))
    )
    (symbol "BL0942" (in_bom yes) (on_board yes)
      (property "Reference" "U2" (at 0 0 0))
      (property "Value" "BL0942 (Metrologia Estacion)" (at 0 -2.54 0))
      (property "Footprint" "Package_SO:SSOP-10_3.9x4.9mm_P1.00mm" (at 0 -5.08 0))
    )
    (symbol "DS18B20" (in_bom yes) (on_board yes)
      (property "Reference" "TH1" (at 0 0 0))
      (property "Value" "DS18B20 (Temp Secado Mopas)" (at 0 -2.54 0))
      (property "Footprint" "Package_TO_SOT_THT:TO-92_Inline" (at 0 -5.08 0))
    )
    (symbol "HF32FV-16" (in_bom yes) (on_board yes)
      (property "Reference" "RL1" (at 0 0 0))
      (property "Value" "HF32FV-16 (Corte Seguridad Termico)" (at 0 -2.54 0))
      (property "Footprint" "Relay_THT:Relay_SPST_Hongfa_HF32FV" (at 0 -5.08 0))
    )
    (symbol "HLK-2M03" (in_bom yes) (on_board yes)
      (property "Reference" "PS1" (at 0 0 0))
      (property "Value" "HLK-2M03 (230VAC->3.3VDC)" (at 0 -2.54 0))
      (property "Footprint" "Converter_ACDC:Converter_ACDC_HiLink_HLK-2Mxx" (at 0 -5.08 0))
    )
    (symbol "Screw_Terminal_01x06" (in_bom yes) (on_board yes)
      (property "Reference" "J1" (at 0 0 0))
      (property "Value" "Bornero Estacion Robot" (at 0 -2.54 0))
      (property "Footprint" "TerminalBlock:TerminalBlock_bornier-6_P5.08mm" (at 0 -5.08 0))
    )
  )

  (symbol (lib_id "ESP32-C3-WROOM-02") (at 110 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f5961808-afb8-be81-023c-esp32rob0001")
    (property "Reference" "U1" (at 110 60 0))
    (property "Value" "ESP32-C3-WROOM-02" (at 110 63 0))
    (property "Footprint" "RF_Module:ESP32-C3-WROOM-02" (at 110 66 0))
  )

  (symbol (lib_id "HLK-2M03") (at 45 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f5961808-afb8-be81-023c-hlkrob000001")
    (property "Reference" "PS1" (at 45 48 0))
    (property "Value" "HLK-2M03" (at 45 51 0))
    (property "Footprint" "Converter_ACDC:Converter_ACDC_HiLink_HLK-2Mxx" (at 45 54 0))
  )

  (symbol (lib_id "BL0942") (at 180 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f5961808-afb8-be81-023c-meterrob0001")
    (property "Reference" "U2" (at 180 50 0))
    (property "Value" "BL0942 (Potencia Base)" (at 180 53 0))
    (property "Footprint" "Package_SO:SSOP-10_3.9x4.9mm_P1.00mm" (at 180 56 0))
  )

  (symbol (lib_id "DS18B20") (at 110 130 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f5961808-afb8-be81-023c-ds18b20rob01")
    (property "Reference" "TH1" (at 110 120 0))
    (property "Value" "DS18B20 (Temp Secado)" (at 110 123 0))
    (property "Footprint" "Package_TO_SOT_THT:TO-92_Inline" (at 110 126 0))
  )

  (symbol (lib_id "HF32FV-16") (at 240 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f5961808-afb8-be81-023c-relayrob0001")
    (property "Reference" "RL1" (at 240 48 0))
    (property "Value" "HF32FV-16 (Corte Calentador)" (at 240 51 0))
    (property "Footprint" "Relay_THT:Relay_SPST_Hongfa_HF32FV" (at 240 54 0))
  )

  (symbol (lib_id "Screw_Terminal_01x06") (at 300 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f5961808-afb8-be81-023c-termrob00001")
    (property "Reference" "J1" (at 300 68 0))
    (property "Value" "Bornero Estacion Robot" (at 300 71 0))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-6_P5.08mm" (at 300 74 0))
  )

  (wire (pts (xy 60 60) (xy 90 75)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 130 75) (xy 160 60)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 110 115) (xy 110 100)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 200 60) (xy 220 60)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 260 60) (xy 280 75)) (stroke (width 0.25) (type default)))

  (sheet_instances
    (path "/" (page "1"))
  )
)
"""

KICAD_PRO_TEMPLATE = """{
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
    "filename": "controlador_estacion_robotica.kicad_pro",
    "version": 1
  },
  "net_settings": {
    "classes": []
  },
  "pcbnew": {
    "last_paths": {
      "gencad": "",
      "idf": "",
      "netlist": "",
      "specctra_dsn": "",
      "step": "",
      "vrml": ""
    }
  },
  "schematic": {
    "drawing": {
      "dashed_lines_dash_length_ratio": 12.0,
      "dashed_lines_gap_length_ratio": 3.0,
      "default_line_thickness": 6.0,
      "default_text_size": 50.0,
      "field_names": []
    },
    "meta": {
      "version": 2
    },
    "net_format_name": "Opamp",
    "subsheets": []
  },
  "sheets": [
    [
      "f5961808-afb8-be81-023c-robot0000001",
      ""
    ]
  ]
}
"""

BOM_ROBOTICA_CONTENT = """# Lista de Materiales (BOM) - Placa Controladora y Monitor de Estación Base Robótica

| Ref | Cantidad | Componente / Valor | Encapsulado | Función Técnica | Fabricante / N° de Parte |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **U1** | 1 | ESP32-C3-WROOM-02 (4MB Flash) | SMD Módulo 18x20mm | SoC RISC-V 160MHz con WiFi 802.11 b/g/n y Bluetooth 5.0 LE | Espressif ESP32-C3-WROOM-02-N4 |
| **U2** | 1 | BL0942 (Metrología Energética UART) | SSOP-10 | Medición de potencia activa (W) distinguiendo carga (<30W) de secado térmico (500W) | Shanghai Belling BL0942 |
| **TH1** | 1 | DS18B20 Sensor Digital 1-Wire | TO-92 / Sonda AISI316 | Monitoreo de temperatura del conducto de aire caliente de secado de mopas | Dallas/Maxim DS18B20 |
| **RL1** | 1 | Hongfa HF32FV-16-12-HTF (16A 250VAC) | THT 19x15.5x15mm | Relé de seguridad para desconexión térmica preventiva si T > 65°C | Hongfa HF32FV-16 |
| **PS1** | 1 | HLK-2M03 (AC/DC Aislado 3.3V 600mA) | Módulo 28x14x16mm | Fuente conmutada compacta entrada 85-264VAC, salida 3.3V DC aislada galvánicamente | Hi-Link HLK-2M03 |
| **MOV1** | 1 | Varistor 14D471K (470V 4.5kA) | Disco 14mm THT | Supresión de sobretensiones transitorias en la alimentación de la estación base | Epcos B72214S0301K101 |
| **J1** | 1 | Bornero tornillo 6 polos paso 5.08mm | PCB Bornier | Bornas para Red AC, Calentador, Sondas Ultrasónicas de Tanques de Agua | Phoenix Contact MKDSN 1.5/6 |
"""

def main():
    base_dir = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/02_robotica_limpieza/electrico"
    os.makedirs(base_dir, exist_ok=True)
    svg_dir = os.path.join(base_dir, "esquema_svg")
    os.makedirs(svg_dir, exist_ok=True)

    sch_path = os.path.join(base_dir, "controlador_estacion_robotica.kicad_sch")
    pro_path = os.path.join(base_dir, "controlador_estacion_robotica.kicad_pro")
    bom_path = os.path.join(base_dir, "BOM.md")

    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(KICAD_SCH_TEMPLATE)
    with open(pro_path, "w", encoding="utf-8") as f:
        f.write(KICAD_PRO_TEMPLATE)
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(BOM_ROBOTICA_CONTENT)
    print(f"Esquema KiCad 10 guardado: {sch_path}")
    print(f"BOM guardada: {bom_path}")

    # Exportar SVG mediante kicad-cli
    cmd = [
        "flatpak-spawn", "--host", "flatpak", "run",
        "--command=kicad-cli", "org.kicad.KiCad",
        "sch", "export", "svg",
        sch_path,
        "-o", svg_dir
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("Exportación SVG completada con kicad-cli.")
    except Exception as e:
        print(f"Error exportando SVG: {e}")

if __name__ == "__main__":
    main()
