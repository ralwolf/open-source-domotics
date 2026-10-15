#!/usr/bin/env python3
"""
generar_kicad_lavanderia.py
Genera el esquema electrónico KiCad 10 (.kicad_sch), el proyecto (.kicad_pro),
la lista de materiales (BOM.md) y exporta el SVG del circuito para la
Placa de Monitorización y Seguridad Anti-Inundación en Lavandería (ESP32-C3 + BL0942 + Corte de Agua y Potencia).
"""

import os
import subprocess

KICAD_SCH_TEMPLATE = """(kicad_sch (version 20240108) (generator "open-source-domotics-lavanderia-gen")
  (uuid "f374f606-8d96-9c5f-e01a-lavand000001")
  (paper "A3")
  (lib_symbols
    (symbol "ESP32-C3-WROOM-02" (in_bom yes) (on_board yes)
      (property "Reference" "U1" (at 0 0 0))
      (property "Value" "ESP32-C3-WROOM-02" (at 0 -2.54 0))
      (property "Footprint" "RF_Module:ESP32-C3-WROOM-02" (at 0 -5.08 0))
    )
    (symbol "BL0942" (in_bom yes) (on_board yes)
      (property "Reference" "U2" (at 0 0 0))
      (property "Value" "BL0942 (Metrologia 16A)" (at 0 -2.54 0))
      (property "Footprint" "Package_SO:SSOP-10_3.9x4.9mm_P1.00mm" (at 0 -5.08 0))
    )
    (symbol "ADXL345" (in_bom yes) (on_board yes)
      (property "Reference" "U3" (at 0 0 0))
      (property "Value" "ADXL345 (Acelerómetro Vibración)" (at 0 -2.54 0))
      (property "Footprint" "Package_LGA:LGA-14_3x5mm_P0.8mm" (at 0 -5.08 0))
    )
    (symbol "PC817" (in_bom yes) (on_board yes)
      (property "Reference" "OK1" (at 0 0 0))
      (property "Value" "PC817 (Sonda Inundación)" (at 0 -2.54 0))
      (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 0 -5.08 0))
    )
    (symbol "AOD4184A" (in_bom yes) (on_board yes)
      (property "Reference" "Q1" (at 0 0 0))
      (property "Value" "AOD4184A (Driver Valvula Agua 12V)" (at 0 -2.54 0))
      (property "Footprint" "Package_TO_SOT_SMD:TO-252-2" (at 0 -5.08 0))
    )
    (symbol "HF32FV-16" (in_bom yes) (on_board yes)
      (property "Reference" "RL1" (at 0 0 0))
      (property "Value" "HF32FV-16 (Corte Potencia 16A)" (at 0 -2.54 0))
      (property "Footprint" "Relay_THT:Relay_SPST_Hongfa_HF32FV" (at 0 -5.08 0))
    )
    (symbol "HLK-2M03" (in_bom yes) (on_board yes)
      (property "Reference" "PS1" (at 0 0 0))
      (property "Value" "HLK-2M03 (230VAC->3.3VDC)" (at 0 -2.54 0))
      (property "Footprint" "Converter_ACDC:Converter_ACDC_HiLink_HLK-2Mxx" (at 0 -5.08 0))
    )
    (symbol "Screw_Terminal_01x06" (in_bom yes) (on_board yes)
      (property "Reference" "J1" (at 0 0 0))
      (property "Value" "Bornero Lavandería" (at 0 -2.54 0))
      (property "Footprint" "TerminalBlock:TerminalBlock_bornier-6_P5.08mm" (at 0 -5.08 0))
    )
  )

  (symbol (lib_id "ESP32-C3-WROOM-02") (at 110 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f374f606-8d96-9c5f-e01a-esp32lav0001")
    (property "Reference" "U1" (at 110 60 0))
    (property "Value" "ESP32-C3-WROOM-02" (at 110 63 0))
    (property "Footprint" "RF_Module:ESP32-C3-WROOM-02" (at 110 66 0))
  )

  (symbol (lib_id "HLK-2M03") (at 45 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f374f606-8d96-9c5f-e01a-hlklav000001")
    (property "Reference" "PS1" (at 45 48 0))
    (property "Value" "HLK-2M03" (at 45 51 0))
    (property "Footprint" "Converter_ACDC:Converter_ACDC_HiLink_HLK-2Mxx" (at 45 54 0))
  )

  (symbol (lib_id "BL0942") (at 180 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f374f606-8d96-9c5f-e01a-meterlav0001")
    (property "Reference" "U2" (at 180 50 0))
    (property "Value" "BL0942 (16A Continuo)" (at 180 53 0))
    (property "Footprint" "Package_SO:SSOP-10_3.9x4.9mm_P1.00mm" (at 180 56 0))
  )

  (symbol (lib_id "ADXL345") (at 110 130 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f374f606-8d96-9c5f-e01a-adxl00000001")
    (property "Reference" "U3" (at 110 120 0))
    (property "Value" "ADXL345" (at 110 123 0))
    (property "Footprint" "Package_LGA:LGA-14_3x5mm_P0.8mm" (at 110 126 0))
  )

  (symbol (lib_id "PC817") (at 45 110 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f374f606-8d96-9c5f-e01a-flood0000001")
    (property "Reference" "OK1" (at 45 100 0))
    (property "Value" "PC817 (Sonda Inundación)" (at 45 103 0))
    (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 45 106 0))
  )

  (symbol (lib_id "AOD4184A") (at 180 110 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f374f606-8d96-9c5f-e01a-valve00000001")
    (property "Reference" "Q1" (at 180 100 0))
    (property "Value" "AOD4184A (Válvula Agua)" (at 180 103 0))
    (property "Footprint" "Package_TO_SOT_SMD:TO-252-2" (at 180 106 0))
  )

  (symbol (lib_id "HF32FV-16") (at 240 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f374f606-8d96-9c5f-e01a-relaypwr0001")
    (property "Reference" "RL1" (at 240 48 0))
    (property "Value" "HF32FV-16 (Corte Enchufe)" (at 240 51 0))
    (property "Footprint" "Relay_THT:Relay_SPST_Hongfa_HF32FV" (at 240 54 0))
  )

  (symbol (lib_id "Screw_Terminal_01x06") (at 300 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "f374f606-8d96-9c5f-e01a-termlav00001")
    (property "Reference" "J1" (at 300 68 0))
    (property "Value" "Bornero Lavandería" (at 300 71 0))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-6_P5.08mm" (at 300 74 0))
  )

  (wire (pts (xy 60 60) (xy 90 75)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 60 110) (xy 90 85)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 130 75) (xy 160 60)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 130 85) (xy 160 110)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 110 115) (xy 110 100)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 200 60) (xy 220 60)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 260 60) (xy 280 75)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 200 110) (xy 280 85)) (stroke (width 0.25) (type default)))

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
    "filename": "controlador_lavanderia_seguridad.kicad_pro",
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
      "f374f606-8d96-9c5f-e01a-lavand000001",
      ""
    ]
  ]
}
"""

BOM_LAVANDERIA_CONTENT = """# Lista de Materiales (BOM) - Monitorización y Seguridad Anti-Inundación en Lavandería

| Ref | Cantidad | Componente / Valor | Encapsulado | Función Técnica | Fabricante / N° de Parte |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **U1** | 1 | ESP32-C3-WROOM-02 (4MB Flash) | SMD Módulo 18x20mm | SoC RISC-V 160MHz con WiFi 802.11 b/g/n y Bluetooth 5.0 LE | Espressif ESP32-C3-WROOM-02-N4 |
| **U2** | 1 | BL0942 (Metrología Energética UART) | SSOP-10 | Medición de potencia activa (W), tensión RMS (V) y corriente (A) hasta 16A continuo | Shanghai Belling BL0942 |
| **U3** | 1 | ADXL345 (Acelerómetro Digital 3 Ejes I2C) | LGA-14 | Monitoreo de vibraciones mecánicas y detección de desbalance de tambor a 1400 RPM | Analog Devices ADXL345 |
| **OK1** | 1 | PC817 Optoacoplador | SOP-4 | Aislamiento galvánico de la sonda de inundación de suelo | Sharp PC817X |
| **Q1** | 1 | AOD4184A N-Channel MOSFET 40V 50A | TO-252 | Driver de potencia para actuador/electroválvula de corte de agua 12V 1.5A | Alpha & Omega AOD4184A |
| **D1** | 1 | 1N5408 Diodo Flyback 3A 1000V | DO-201AD | Supresor de picos inductivos de la bobina de la electroválvula solenoide de agua | Vishay 1N5408 |
| **RL1** | 1 | Hongfa HF32FV-16-12-HTF (16A 250VAC) | THT 19x15.5x15mm | Relé de corte para desenergizar el enchufe de lavadora/secadora ante inundación | Hongfa HF32FV-16 |
| **PS1** | 1 | HLK-2M03 (AC/DC Aislado 3.3V 600mA) | Módulo 28x14x16mm | Fuente conmutada compacta entrada 85-264VAC, salida 3.3V DC aislada galvánicamente | Hi-Link HLK-2M03 |
| **MOV1** | 1 | Varistor 14D471K (470V 4.5kA) | Disco 14mm THT | Supresión de sobretensiones transitorias SPD Clase III en línea de lavadora | Epcos B72214S0301K101 |
| **J1** | 1 | Bornero tornillo 6 polos paso 5.08mm | PCB Bornier | Bornas para Red L/N, Carga L_OUT, Sonda Agua, Salida 12V Válvula Agua | Phoenix Contact MKDSN 1.5/6 |
"""

def main():
    base_dir = "/home/ral/Documents/GitHub/open-source-domotics/04_telemetria_y_cargas_criticas/03_cargas_lavanderia/electrico"
    os.makedirs(base_dir, exist_ok=True)
    svg_dir = os.path.join(base_dir, "esquema_svg")
    os.makedirs(svg_dir, exist_ok=True)

    sch_path = os.path.join(base_dir, "controlador_lavanderia_seguridad.kicad_sch")
    pro_path = os.path.join(base_dir, "controlador_lavanderia_seguridad.kicad_pro")
    bom_path = os.path.join(base_dir, "BOM.md")

    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(KICAD_SCH_TEMPLATE)
    with open(pro_path, "w", encoding="utf-8") as f:
        f.write(KICAD_PRO_TEMPLATE)
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(BOM_LAVANDERIA_CONTENT)
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
