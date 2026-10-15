#!/usr/bin/env python3
"""
generar_kicad_audio_multiroom.py
Genera el esquema electrónico KiCad 10 (.kicad_sch), el proyecto (.kicad_pro),
la lista de materiales (BOM.md) y exporta el SVG del circuito para el
Amplificador Digital Estéreo Streaming Clase D Hi-Fi (ESP32-S3 + TAS5805M I2S Direct-Digital).
"""

import os
import subprocess

KICAD_SCH_TEMPLATE = """(kicad_sch (version 20240108) (generator "open-source-domotics-audio-gen")
  (uuid "e152d404-6b74-7a3d-cef8-audio0000001")
  (paper "A3")
  (lib_symbols
    (symbol "ESP32-S3-WROOM-1" (in_bom yes) (on_board yes)
      (property "Reference" "U1" (at 0 0 0))
      (property "Value" "ESP32-S3-WROOM-1 (8MB PSRAM)" (at 0 -2.54 0))
      (property "Footprint" "RF_Module:ESP32-S3-WROOM-1" (at 0 -5.08 0))
    )
    (symbol "TAS5805M" (in_bom yes) (on_board yes)
      (property "Reference" "U2" (at 0 0 0))
      (property "Value" "TAS5805MPWPR (Clase D I2S 2x25W)" (at 0 -2.54 0))
      (property "Footprint" "Package_SO:TSSOP-28_4.4x9.7mm_P0.65mm" (at 0 -5.08 0))
    )
    (symbol "TPS7A4700" (in_bom yes) (on_board yes)
      (property "Reference" "VR1" (at 0 0 0))
      (property "Value" "TPS7A4700 (LDO Ultra-Low Noise 4uV)" (at 0 -2.54 0))
      (property "Footprint" "Package_DFN_QFN:QFN-20-1EP_5x5mm_P0.65mm_EP3.1x3.1mm" (at 0 -5.08 0))
    )
    (symbol "MP1584EN" (in_bom yes) (on_board yes)
      (property "Reference" "VR2" (at 0 0 0))
      (property "Value" "MP1584EN (Buck 24V->5V)" (at 0 -2.54 0))
      (property "Footprint" "Package_SO:SOIC-8-1EP_3.9x4.9mm_P1.27mm" (at 0 -5.08 0))
    )
    (symbol "Inductor_LC_Filter" (in_bom yes) (on_board yes)
      (property "Reference" "L1" (at 0 0 0))
      (property "Value" "10uH Inductor Toroidal Blindado" (at 0 -2.54 0))
      (property "Footprint" "Inductor_SMD:L_12x12mm_H8mm" (at 0 -5.08 0))
    )
    (symbol "Screw_Terminal_01x04" (in_bom yes) (on_board yes)
      (property "Reference" "J1" (at 0 0 0))
      (property "Value" "Bornas Altavoz (L+, L-, R+, R-)" (at 0 -2.54 0))
      (property "Footprint" "TerminalBlock:TerminalBlock_bornier-4_P5.08mm" (at 0 -5.08 0))
    )
    (symbol "Barrel_Jack" (in_bom yes) (on_board yes)
      (property "Reference" "J2" (at 0 0 0))
      (property "Value" "Jack Alimentación 24V DC" (at 0 -2.54 0))
      (property "Footprint" "Connector_BarrelJack:BarrelJack_Horizontal" (at 0 -5.08 0))
    )
  )

  (symbol (lib_id "ESP32-S3-WROOM-1") (at 100 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "e152d404-6b74-7a3d-cef8-esp32audio01")
    (property "Reference" "U1" (at 100 60 0))
    (property "Value" "ESP32-S3-WROOM-1 (8MB PSRAM)" (at 100 63 0))
    (property "Footprint" "RF_Module:ESP32-S3-WROOM-1" (at 100 66 0))
  )

  (symbol (lib_id "TAS5805M") (at 190 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "e152d404-6b74-7a3d-cef8-tas580500001")
    (property "Reference" "U2" (at 190 60 0))
    (property "Value" "TAS5805M (Amplificador Clase D)" (at 190 63 0))
    (property "Footprint" "Package_SO:TSSOP-28_4.4x9.7mm_P0.65mm" (at 190 66 0))
  )

  (symbol (lib_id "Inductor_LC_Filter") (at 250 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "e152d404-6b74-7a3d-cef8-filter0000001")
    (property "Reference" "L1" (at 250 68 0))
    (property "Value" "Filtro LC Salida Audio" (at 250 71 0))
    (property "Footprint" "Inductor_SMD:L_12x12mm_H8mm" (at 250 74 0))
  )

  (symbol (lib_id "Screw_Terminal_01x04") (at 310 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "e152d404-6b74-7a3d-cef8-spkterm00001")
    (property "Reference" "J1" (at 310 66 0))
    (property "Value" "Salidas Altavoces Estéreo" (at 310 69 0))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-4_P5.08mm" (at 310 72 0))
  )

  (symbol (lib_id "Barrel_Jack") (at 40 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "e152d404-6b74-7a3d-cef8-jack24v00001")
    (property "Reference" "J2" (at 40 66 0))
    (property "Value" "Jack 24V DC 3A" (at 40 69 0))
    (property "Footprint" "Connector_BarrelJack:BarrelJack_Horizontal" (at 40 72 0))
  )

  (symbol (lib_id "MP1584EN") (at 40 130 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "e152d404-6b74-7a3d-cef8-buck5v000001")
    (property "Reference" "VR2" (at 40 120 0))
    (property "Value" "MP1584EN (24V->5V)" (at 40 123 0))
    (property "Footprint" "Package_SO:SOIC-8-1EP_3.9x4.9mm_P1.27mm" (at 40 126 0))
  )

  (symbol (lib_id "TPS7A4700") (at 100 130 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "e152d404-6b74-7a3d-cef8-ldoaudio0001")
    (property "Reference" "VR1" (at 100 120 0))
    (property "Value" "TPS7A4700 (Ultra Low Noise)" (at 100 123 0))
    (property "Footprint" "Package_DFN_QFN:QFN-20-1EP_5x5mm_P0.65mm_EP3.1x3.1mm" (at 100 126 0))
  )

  (wire (pts (xy 55 80) (xy 80 80)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 120 75) (xy 170 75)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 120 85) (xy 170 85)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 210 80) (xy 235 80)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 265 80) (xy 295 80)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 40 95) (xy 40 115)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 55 130) (xy 80 130)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 100 115) (xy 100 95)) (stroke (width 0.25) (type default)))

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
    "filename": "amplificador_audio_multiroom.kicad_pro",
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
      "e152d404-6b74-7a3d-cef8-audio0000001",
      ""
    ]
  ]
}
"""

BOM_AUDIO_CONTENT = """# Lista de Materiales (BOM) - Amplificador Digital Streaming Clase D Hi-Fi

| Ref | Cantidad | Componente / Valor | Encapsulado | Función Técnica | Fabricante / N° de Parte |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **U1** | 1 | ESP32-S3-WROOM-1 (8MB PSRAM, 16MB Flash) | SMD Módulo 18x25.5mm | Procesador Dual-Core 240MHz con soporte de buffers Hi-Res y protocolos Squeezelite/Snapcast | Espressif ESP32-S3-WROOM-1-N16R8 |
| **U2** | 1 | Texas Instruments TAS5805MPWPR | TSSOP-28 | Amplificador digital estéreo Clase D, entrada direct-digital I2S, DSP integrado, 2x25W RMS | Texas Instruments TAS5805M |
| **VR1** | 1 | TPS7A4700 (LDO Ultra-Bajo Ruido 4.17µV) | QFN-20 | Regulador lineal de muy bajo ruido para la alimentación del reloj y sección de audio sensible | Texas Instruments TPS7A4700 |
| **VR2** | 1 | MP1584EN Step-Down 24V $\to$ 5V 3A | SOIC-8-1EP | Convertidor buck DC-DC síncrono para alimentación general de placa | Monolithic Power MP1584EN |
| **L1-L4** | 4 | Inductor Toroidal Blindado 10 µH 5A | SMD 12x12mm | Inductancias de potencia del filtro pasivo LC de reconstrucción de salida de altavoces | Wurth Elektronik 744314101 |
| **C1-C4** | 4 | Condensador Película Polipropileno 680 nF 50V | SMD 1812 | Condensadores de filtro LC grado audiófilo de muy bajo factor de disipación | KEMET C1812C684K5RACTU |
| **J1** | 1 | Bornero de tornillo 4 polos paso 5.08mm | PCB Bornier | Terminales de salida estéreo para altavoces pasivos (L+, L-, R+, R-) | Phoenix Contact MKDSN 1.5/4 |
| **J2** | 1 | Jack de alimentación DC 5.5 x 2.1 mm | Montaje PCB Horizontal | Entrada de alimentación principal de 12V a 24V DC / 3.5A | CUI Devices PJ-002A |
| **C_IN** | 2 | Condensador electrolítico Low-ESR 470 µF 35V | Radial Ø10x16mm | Filtro desacoplo de alta corriente para la etapa de potencia de audio | Nichicon UHW1V471MPD |
| **F1** | 1 | Fusible SMD PTC Polyswitch 30V 4A | SMD 2920 | Protección contra sobrecorrientes en la línea de 24V DC | Littelfuse 2920L400PR |
"""

def main():
    base_dir = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/05_audio_distribuido_multiroom/electrico"
    os.makedirs(base_dir, exist_ok=True)
    svg_dir = os.path.join(base_dir, "esquema_svg")
    os.makedirs(svg_dir, exist_ok=True)

    sch_path = os.path.join(base_dir, "amplificador_audio_multiroom.kicad_sch")
    pro_path = os.path.join(base_dir, "amplificador_audio_multiroom.kicad_pro")
    bom_path = os.path.join(base_dir, "BOM.md")

    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(KICAD_SCH_TEMPLATE)
    with open(pro_path, "w", encoding="utf-8") as f:
        f.write(KICAD_PRO_TEMPLATE)
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(BOM_AUDIO_CONTENT)
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
