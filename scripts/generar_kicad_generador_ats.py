#!/usr/bin/env python3
"""
generar_kicad_generador_ats.py
Genera el esquema electrónico KiCad 10 (.kicad_sch), el proyecto (.kicad_pro),
la lista de materiales (BOM.md) y exporta el SVG del circuito para la
Placa Controladora de Arranque Automático de Grupo Electrógeno y Conmutación ATS.
"""

import os
import subprocess

KICAD_SCH_TEMPLATE = """(kicad_sch (version 20240108) (generator "open-source-domotics-genats-gen")
  (uuid "f6a72909-b0c9-cf92-134d-genats000001")
  (paper "A3")
  (lib_symbols
    (symbol "ESP32-C3-WROOM-02" (in_bom yes) (on_board yes)
      (property "Reference" "U1" (at 0 0 0))
      (property "Value" "ESP32-C3-WROOM-02" (at 0 -2.54 0))
      (property "Footprint" "RF_Module:ESP32-C3-WROOM-02" (at 0 -5.08 0))
    )
    (symbol "EL814" (in_bom yes) (on_board yes)
      (property "Reference" "OK1" (at 0 0 0))
      (property "Value" "EL814 (Detector 230V Generador)" (at 0 -2.54 0))
      (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 0 -5.08 0))
    )
    (symbol "Relay_Start" (in_bom yes) (on_board yes)
      (property "Reference" "RL1" (at 0 0 0))
      (property "Value" "HF32FV-16 (Relé Arranque / Estárter)" (at 0 -2.54 0))
      (property "Footprint" "Relay_THT:Relay_SPST_Hongfa_HF32FV" (at 0 -5.08 0))
    )
    (symbol "Relay_Ignition" (in_bom yes) (on_board yes)
      (property "Reference" "RL2" (at 0 0 0))
      (property "Value" "HF32FV-16 (Contacto / Válvula Combustible)" (at 0 -2.54 0))
      (property "Footprint" "Relay_THT:Relay_SPST_Hongfa_HF32FV" (at 0 -5.08 0))
    )
    (symbol "Relay_ATS" (in_bom yes) (on_board yes)
      (property "Reference" "RL3" (at 0 0 0))
      (property "Value" "HF115F-16A (Comando Motor ATS)" (at 0 -2.54 0))
      (property "Footprint" "Relay_THT:Relay_SPDT_Finder_40.61" (at 0 -5.08 0))
    )
    (symbol "MP1584EN" (in_bom yes) (on_board yes)
      (property "Reference" "VR1" (at 0 0 0))
      (property "Value" "MP1584EN (12V Bateria->3.3V)" (at 0 -2.54 0))
      (property "Footprint" "Package_SO:SOIC-8-1EP_3.9x4.9mm_P1.27mm" (at 0 -5.08 0))
    )
    (symbol "Screw_Terminal_01x08" (in_bom yes) (on_board yes)
      (property "Reference" "J1" (at 0 0 0))
      (property "Value" "Bornero ATS y Generador" (at 0 -2.54 0))
      (property "Footprint" "TerminalBlock:TerminalBlock_bornier-8_P5.08mm" (at 0 -5.08 0))
    )
  )

  (symbol (lib_id "ESP32-C3-WROOM-02") (at 110 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f6a72909-b0c9-cf92-134d-esp32gen0001")
    (property "Reference" "U1" (at 110 60 0))
    (property "Value" "ESP32-C3-WROOM-02" (at 110 63 0))
    (property "Footprint" "RF_Module:ESP32-C3-WROOM-02" (at 110 66 0))
  )

  (symbol (lib_id "MP1584EN") (at 45 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f6a72909-b0c9-cf92-134d-buckgen00001")
    (property "Reference" "VR1" (at 45 48 0))
    (property "Value" "MP1584EN" (at 45 51 0))
    (property "Footprint" "Package_SO:SOIC-8-1EP_3.9x4.9mm_P1.27mm" (at 45 54 0))
  )

  (symbol (lib_id "EL814") (at 45 110 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f6a72909-b0c9-cf92-134d-voltgen00001")
    (property "Reference" "OK1" (at 45 100 0))
    (property "Value" "EL814 (Detector AC Gen)" (at 45 103 0))
    (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 45 106 0))
  )

  (symbol (lib_id "Relay_Start") (at 190 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f6a72909-b0c9-cf92-134d-startgen0001")
    (property "Reference" "RL1" (at 190 48 0))
    (property "Value" "HF32FV-16 (Start)" (at 190 51 0))
    (property "Footprint" "Relay_THT:Relay_SPST_Hongfa_HF32FV" (at 190 54 0))
  )

  (symbol (lib_id "Relay_Ignition") (at 190 100 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f6a72909-b0c9-cf92-134d-ignitgen0001")
    (property "Reference" "RL2" (at 190 88 0))
    (property "Value" "HF32FV-16 (Ignition)" (at 190 91 0))
    (property "Footprint" "Relay_THT:Relay_SPST_Hongfa_HF32FV" (at 190 94 0))
  )

  (symbol (lib_id "Relay_ATS") (at 190 140 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f6a72909-b0c9-cf92-134d-atsrelay0001")
    (property "Reference" "RL3" (at 190 128 0))
    (property "Value" "HF115F (Comando ATS)" (at 190 131 0))
    (property "Footprint" "Relay_THT:Relay_SPDT_Finder_40.61" (at 190 134 0))
  )

  (symbol (lib_id "Screw_Terminal_01x08") (at 280 100 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f6a72909-b0c9-cf92-134d-termgen00001")
    (property "Reference" "J1" (at 280 86 0))
    (property "Value" "Bornero ATS y Generador" (at 280 89 0))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-8_P5.08mm" (at 280 92 0))
  )

  (wire (pts (xy 60 60) (xy 90 75)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 60 110) (xy 90 85)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 130 75) (xy 170 60)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 130 85) (xy 170 100)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 130 95) (xy 170 140)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 210 60) (xy 260 85)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 210 100) (xy 260 95)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 210 140) (xy 260 105)) (stroke (width 0.25) (type default)))

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
    "filename": "controlador_generador_respaldo_ats.kicad_pro",
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
      "f6a72909-b0c9-cf92-134d-genats000001",
      ""
    ]
  ]
}
"""

BOM_GENERADOR_CONTENT = """# Lista de Materiales (BOM) - Placa Controladora de Generador de Respaldo y Conmutación ATS

| Ref | Cantidad | Componente / Valor | Encapsulado | Función Técnica | Fabricante / N° de Parte |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **U1** | 1 | ESP32-C3-WROOM-02 (4MB Flash) | SMD Módulo 18x20mm | SoC RISC-V 160MHz con WiFi y BLE para gestión de secuencias de arranque y ATS | Espressif ESP32-C3-WROOM-02-N4 |
| **OK1** | 1 | EL814 / PC814 (Optoacoplador entrada AC) | SOP-4 | Detección inmediata de tensión 230VAC generada para desconectar el motor de arranque | Everlight EL814S |
| **RL1** | 1 | Hongfa HF32FV-16-12-HTF (16A 250VAC) | THT 19x15.5x15mm | Relé de accionamiento de solenoide de arranque térmico (Start) | Hongfa HF32FV-16 |
| **RL2** | 1 | Hongfa HF32FV-16-12-HTF (16A 250VAC) | THT 19x15.5x15mm | Relé de ignición / válvula solenoide de gasolina (Run / Stop) | Hongfa HF32FV-16 |
| **RL3** | 1 | Hongfa HF115F/012-1ZS3A (16A 250VAC) | THT 29x12.7x15.7mm | Relé de comando para motor de conmutación del tablero ATS 63A | Hongfa HF115F |
| **VR1** | 1 | MP1584EN Step-Down 12V $\to$ 3.3V 3A | SOIC-8-1EP | Convertidor buck DC-DC de alta eficiencia alimentado por batería de arranque 12V | Monolithic Power MP1584EN |
| **D1-D3** | 3 | 1N4007 Diodo Supresor | DO-41 | Diodos de libre circulación (flyback) en bobinas de relé de potencia | Diodes Inc. 1N4007 |
| **R_DIV** | 2 | Divisor de tensión 100kΩ / 22kΩ 1% | SMD 0805 | Lectura analógica precisa del voltaje de la batería de 12V (10.0V - 14.8V) | Yageo RC0805 |
| **F1** | 1 | Fusible automotriz tipo cuchilla 5A 32V | Mini Fuse THT | Protección de sobrecorriente en línea de batería de 12V | Littelfuse 0297005.WXNV |
| **J1** | 1 | Bornero tornillo 8 polos paso 5.08mm | PCB Bornier | Bornas para Bat +/-, Start, Ignition, ATS Comando, Sensor Boya, Entrada 230VAC | Phoenix Contact MKDSN 1.5/8 |
"""

def main():
    base_dir = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/06_generador_gasolina_respaldo/electrico"
    os.makedirs(base_dir, exist_ok=True)
    svg_dir = os.path.join(base_dir, "esquema_svg")
    os.makedirs(svg_dir, exist_ok=True)

    sch_path = os.path.join(base_dir, "controlador_generador_respaldo_ats.kicad_sch")
    pro_path = os.path.join(base_dir, "controlador_generador_respaldo_ats.kicad_pro")
    bom_path = os.path.join(base_dir, "BOM.md")

    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(KICAD_SCH_TEMPLATE)
    with open(pro_path, "w", encoding="utf-8") as f:
        f.write(KICAD_PRO_TEMPLATE)
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(BOM_GENERADOR_CONTENT)
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
