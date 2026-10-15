#!/usr/bin/env python3
"""
generar_kicad_cocina.py
Genera el esquema electrónico KiCad 10 (.kicad_sch), el proyecto (.kicad_pro),
la lista de materiales (BOM.md) y exporta el SVG del circuito para la
Monitorización y Gestión de Cargas Críticas en Cocina y Controlador de Mini-UPS Refrigerador.
"""

import os
import subprocess

KICAD_SCH_TEMPLATE = """(kicad_sch (version 20240108) (generator "open-source-domotics-cocina-gen")
  (uuid "f263e505-7c85-8b4e-df09-cocina000001")
  (paper "A3")
  (lib_symbols
    (symbol "ESP32-C3-WROOM-02" (in_bom yes) (on_board yes)
      (property "Reference" "U1" (at 0 0 0))
      (property "Value" "ESP32-C3-WROOM-02" (at 0 -2.54 0))
      (property "Footprint" "RF_Module:ESP32-C3-WROOM-02" (at 0 -5.08 0))
    )
    (symbol "BL0942" (in_bom yes) (on_board yes)
      (property "Reference" "U2" (at 0 0 0))
      (property "Value" "BL0942 (Metrologia Refrig)" (at 0 -2.54 0))
      (property "Footprint" "Package_SO:SSOP-10_3.9x4.9mm_P1.00mm" (at 0 -5.08 0))
    )
    (symbol "BL0942_DW" (in_bom yes) (on_board yes)
      (property "Reference" "U3" (at 0 0 0))
      (property "Value" "BL0942 (Metrologia Lavavajillas)" (at 0 -2.54 0))
      (property "Footprint" "Package_SO:SSOP-10_3.9x4.9mm_P1.00mm" (at 0 -5.08 0))
    )
    (symbol "INA219" (in_bom yes) (on_board yes)
      (property "Reference" "U4" (at 0 0 0))
      (property "Value" "INA219AIDR (Monitor Bateria LiFePO4)" (at 0 -2.54 0))
      (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 0 -5.08 0))
    )
    (symbol "Relay_SPDT_16A" (in_bom yes) (on_board yes)
      (property "Reference" "RL1" (at 0 0 0))
      (property "Value" "HF115F-16A (Transferencia UPS <10ms)" (at 0 -2.54 0))
      (property "Footprint" "Relay_THT:Relay_SPDT_Finder_40.61" (at 0 -5.08 0))
    )
    (symbol "HLK-2M03" (in_bom yes) (on_board yes)
      (property "Reference" "PS1" (at 0 0 0))
      (property "Value" "HLK-2M03 (230VAC->3.3VDC)" (at 0 -2.54 0))
      (property "Footprint" "Converter_ACDC:Converter_ACDC_HiLink_HLK-2Mxx" (at 0 -5.08 0))
    )
    (symbol "Screw_Terminal_01x06" (in_bom yes) (on_board yes)
      (property "Reference" "J1" (at 0 0 0))
      (property "Value" "Bornero Potencia Cocina" (at 0 -2.54 0))
      (property "Footprint" "TerminalBlock:TerminalBlock_bornier-6_P5.08mm" (at 0 -5.08 0))
    )
  )

  (symbol (lib_id "ESP32-C3-WROOM-02") (at 110 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f263e505-7c85-8b4e-df09-esp32coc0001")
    (property "Reference" "U1" (at 110 60 0))
    (property "Value" "ESP32-C3-WROOM-02" (at 110 63 0))
    (property "Footprint" "RF_Module:ESP32-C3-WROOM-02" (at 110 66 0))
  )

  (symbol (lib_id "HLK-2M03") (at 45 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f263e505-7c85-8b4e-df09-hlkcocina001")
    (property "Reference" "PS1" (at 45 48 0))
    (property "Value" "HLK-2M03" (at 45 51 0))
    (property "Footprint" "Converter_ACDC:Converter_ACDC_HiLink_HLK-2Mxx" (at 45 54 0))
  )

  (symbol (lib_id "BL0942") (at 180 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f263e505-7c85-8b4e-df09-blrefrig0001")
    (property "Reference" "U2" (at 180 50 0))
    (property "Value" "BL0942 (Refrigerador)" (at 180 53 0))
    (property "Footprint" "Package_SO:SSOP-10_3.9x4.9mm_P1.00mm" (at 180 56 0))
  )

  (symbol (lib_id "BL0942_DW") (at 180 110 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f263e505-7c85-8b4e-df09-bllavavaj001")
    (property "Reference" "U3" (at 180 100 0))
    (property "Value" "BL0942 (Lavavajillas)" (at 180 103 0))
    (property "Footprint" "Package_SO:SSOP-10_3.9x4.9mm_P1.00mm" (at 180 106 0))
  )

  (symbol (lib_id "INA219") (at 110 140 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f263e505-7c85-8b4e-df09-ina219coc001")
    (property "Reference" "U4" (at 110 130 0))
    (property "Value" "INA219 (Batería UPS 4S)" (at 110 133 0))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 110 136 0))
  )

  (symbol (lib_id "Relay_SPDT_16A") (at 250 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f263e505-7c85-8b4e-df09-relayups0001")
    (property "Reference" "RL1" (at 250 48 0))
    (property "Value" "HF115F (Transferencia UPS)" (at 250 51 0))
    (property "Footprint" "Relay_THT:Relay_SPDT_Finder_40.61" (at 250 54 0))
  )

  (symbol (lib_id "Screw_Terminal_01x06") (at 310 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f263e505-7c85-8b4e-df09-termcocina01")
    (property "Reference" "J1" (at 310 68 0))
    (property "Value" "Bornero Potencia Cocina" (at 310 71 0))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-6_P5.08mm" (at 310 74 0))
  )

  (wire (pts (xy 60 60) (xy 90 75)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 130 75) (xy 160 60)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 130 85) (xy 160 110)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 110 115) (xy 110 105)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 200 60) (xy 230 60)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 270 60) (xy 290 75)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 200 110) (xy 290 85)) (stroke (width 0.25) (type default)))

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
    "filename": "controlador_cargas_cocina_ups.kicad_pro",
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
      "f263e505-7c85-8b4e-df09-cocina000001",
      ""
    ]
  ]
}
"""

BOM_COCINA_CONTENT = """# Lista de Materiales (BOM) - Monitorización de Cargas de Cocina y Mini-UPS Refrigerador

| Ref | Cantidad | Componente / Valor | Encapsulado | Función Técnica | Fabricante / N° de Parte |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **U1** | 1 | ESP32-C3-WROOM-02 (4MB Flash) | SMD Módulo 18x20mm | SoC RISC-V 160MHz con WiFi 802.11 b/g/n y Bluetooth 5.0 LE | Espressif ESP32-C3-WROOM-02-N4 |
| **U2, U3** | 2 | BL0942 (Metrología Energética UART) | SSOP-10 | Medición de potencia activa (W), tensión RMS (V) y corriente (A) para refrigerador y lavavajillas | Shanghai Belling BL0942 |
| **U4** | 1 | INA219AIDR (Monitor I2C Corriente/Tensión) | SOIC-8 | Monitoreo bidireccional del estado de carga y salud de la batería LiFePO4 de 12.8V | Texas Instruments INA219 |
| **PS1** | 1 | HLK-2M03 (AC/DC Aislado 3.3V 600mA) | Módulo 28x14x16mm | Fuente de alimentación auxiliar de lógica de control conectada a red | Hi-Link HLK-2M03 |
| **RL1** | 1 | Hongfa HF115F/012-1ZS3A (16A 250VAC) | THT 29x12.7x15.7mm | Relé de transferencia ultrarrápida (<10ms) de alimentación AC a inversor de batería | Hongfa HF115F |
| **R_SH1, R_SH2** | 2 | Shunt Manganina 1 mΩ 3W 1% | SMD 2512 | Resistencias derivadoras para lectura precisa de corriente sin caída apreciable | Vishay WSL25121L000FEA |
| **MOV1-MOV3** | 3 | Varistor 14D471K (470V 4.5kA) | Disco 14mm THT | Supresor de sobretensiones transitorias SPD Clase III en las tomas críticas | Epcos B72214S0301K101 |
| **J1** | 1 | Bornero tornillo 6 polos paso 5.08mm | PCB Bornier | Conexiones de entrada Red AC, salida Refrig, salida Lavavajillas, neutros y tierra | Phoenix Contact MKDSN 1.5/6 |
"""

def main():
    base_dir = "/home/ral/Documents/GitHub/open-source-domotics/04_telemetria_y_cargas_criticas/02_cargas_cocina/electrico"
    os.makedirs(base_dir, exist_ok=True)
    svg_dir = os.path.join(base_dir, "esquema_svg")
    os.makedirs(svg_dir, exist_ok=True)

    sch_path = os.path.join(base_dir, "controlador_cargas_cocina_ups.kicad_sch")
    pro_path = os.path.join(base_dir, "controlador_cargas_cocina_ups.kicad_pro")
    bom_path = os.path.join(base_dir, "BOM.md")

    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(KICAD_SCH_TEMPLATE)
    with open(pro_path, "w", encoding="utf-8") as f:
        f.write(KICAD_PRO_TEMPLATE)
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(BOM_COCINA_CONTENT)
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
