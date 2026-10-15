#!/usr/bin/env python3
"""
generar_kicad_rele_pared.py
Genera el esquema electrónico KiCad 10 (.kicad_sch), el proyecto (.kicad_pro),
la lista de materiales (BOM.md) y exporta el SVG del circuito para el
Micromódulo de Pared de Doble Relé con Conmutación en Paso por Cero (Zero-Cross)
y Metrología Energética Integrada BL0942.
"""

import os
import subprocess

KICAD_SCH_TEMPLATE = """(kicad_sch (version 20240108) (generator "open-source-domotics-relay-gen")
  (uuid "c930b202-4952-581b-ace6-rele00000001")
  (paper "A3")
  (lib_symbols
    (symbol "ESP32-C3-WROOM-02" (in_bom yes) (on_board yes)
      (property "Reference" "U1" (at 0 0 0))
      (property "Value" "ESP32-C3-WROOM-02" (at 0 -2.54 0))
      (property "Footprint" "RF_Module:ESP32-C3-WROOM-02" (at 0 -5.08 0))
    )
    (symbol "HLK-2M03" (in_bom yes) (on_board yes)
      (property "Reference" "PS1" (at 0 0 0))
      (property "Value" "HLK-2M03 (230VAC->3.3VDC 600mA)" (at 0 -2.54 0))
      (property "Footprint" "Converter_ACDC:Converter_ACDC_HiLink_HLK-2Mxx" (at 0 -5.08 0))
    )
    (symbol "EL814" (in_bom yes) (on_board yes)
      (property "Reference" "OK1" (at 0 0 0))
      (property "Value" "EL814 (Detector Zero-Cross AC)" (at 0 -2.54 0))
      (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 0 -5.08 0))
    )
    (symbol "BL0942" (in_bom yes) (on_board yes)
      (property "Reference" "U2" (at 0 0 0))
      (property "Value" "BL0942 (Metrologia Shunt 1mOhm)" (at 0 -2.54 0))
      (property "Footprint" "Package_SO:SSOP-10_3.9x4.9mm_P1.00mm" (at 0 -5.08 0))
    )
    (symbol "HF32FV-16" (in_bom yes) (on_board yes)
      (property "Reference" "RL1" (at 0 0 0))
      (property "Value" "HF32FV-16-16A-250VAC" (at 0 -2.54 0))
      (property "Footprint" "Relay_THT:Relay_SPST_Hongfa_HF32FV" (at 0 -5.08 0))
    )
    (symbol "PC817" (in_bom yes) (on_board yes)
      (property "Reference" "OK2" (at 0 0 0))
      (property "Value" "PC817 (Aislamiento S1/S2)" (at 0 -2.54 0))
      (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 0 -5.08 0))
    )
    (symbol "Screw_Terminal_01x06" (in_bom yes) (on_board yes)
      (property "Reference" "J1" (at 0 0 0))
      (property "Value" "Bornero 6 Polos (L, N, L1, L2, S1, S2)" (at 0 -2.54 0))
      (property "Footprint" "TerminalBlock:TerminalBlock_bornier-6_P5.08mm" (at 0 -5.08 0))
    )
  )

  (symbol (lib_id "ESP32-C3-WROOM-02") (at 110 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "c930b202-4952-581b-ace6-c30000000001")
    (property "Reference" "U1" (at 110 60 0))
    (property "Value" "ESP32-C3-WROOM-02" (at 110 63 0))
    (property "Footprint" "RF_Module:ESP32-C3-WROOM-02" (at 110 66 0))
  )

  (symbol (lib_id "HLK-2M03") (at 45 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "c930b202-4952-581b-ace6-hlk000000001")
    (property "Reference" "PS1" (at 45 48 0))
    (property "Value" "HLK-2M03" (at 45 51 0))
    (property "Footprint" "Converter_ACDC:Converter_ACDC_HiLink_HLK-2Mxx" (at 45 54 0))
  )

  (symbol (lib_id "EL814") (at 45 110 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "c930b202-4952-581b-ace6-zc0000000001")
    (property "Reference" "OK1" (at 45 100 0))
    (property "Value" "EL814 (Detector Zero-Cross)" (at 45 103 0))
    (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 45 106 0))
  )

  (symbol (lib_id "BL0942") (at 180 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "c930b202-4952-581b-ace6-meter00000001")
    (property "Reference" "U2" (at 180 50 0))
    (property "Value" "BL0942 (Metrologia W/V/A)" (at 180 53 0))
    (property "Footprint" "Package_SO:SSOP-10_3.9x4.9mm_P1.00mm" (at 180 56 0))
  )

  (symbol (lib_id "HF32FV-16") (at 240 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "c930b202-4952-581b-ace6-rele100000001")
    (property "Reference" "RL1" (at 240 48 0))
    (property "Value" "HF32FV-16 (Relé L1 16A)" (at 240 51 0))
    (property "Footprint" "Relay_THT:Relay_SPST_Hongfa_HF32FV" (at 240 54 0))
  )

  (symbol (lib_id "HF32FV-16") (at 240 110 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "c930b202-4952-581b-ace6-rele200000001")
    (property "Reference" "RL2" (at 240 98 0))
    (property "Value" "HF32FV-16 (Relé L2 16A)" (at 240 101 0))
    (property "Footprint" "Relay_THT:Relay_SPST_Hongfa_HF32FV" (at 240 104 0))
  )

  (symbol (lib_id "PC817") (at 110 150 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "c930b202-4952-581b-ace6-inopt0000001")
    (property "Reference" "OK2" (at 110 140 0))
    (property "Value" "PC817 (Aislamiento Entradas S1/S2)" (at 110 143 0))
    (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 110 146 0))
  )

  (symbol (lib_id "Screw_Terminal_01x06") (at 300 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "c930b202-4952-581b-ace6-borna00000001")
    (property "Reference" "J1" (at 300 68 0))
    (property "Value" "Bornero L/N/L1/L2/S1/S2" (at 300 71 0))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-6_P5.08mm" (at 300 74 0))
  )

  (wire (pts (xy 60 60) (xy 90 75)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 60 110) (xy 90 85)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 130 75) (xy 160 60)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 130 85) (xy 220 60)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 130 90) (xy 220 110)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 110 130) (xy 110 105)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 260 60) (xy 280 70)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 260 110) (xy 280 85)) (stroke (width 0.25) (type default)))

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
    "filename": "micromodulo_rele_zerocross.kicad_pro",
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
      "c930b202-4952-581b-ace6-rele00000001",
      ""
    ]
  ]
}
"""

BOM_RELE_CONTENT = """# Lista de Materiales (BOM) - Micromódulo de Pared Dual Zero-Cross con Metrología

| Ref | Cantidad | Componente / Valor | Encapsulado | Función Técnica | Fabricante / N° de Parte |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **U1** | 1 | ESP32-C3-WROOM-02 (4MB Flash) | SMD Módulo 18x20mm | SoC RISC-V 160MHz, WiFi 802.11 b/g/n, BLE 5.0, gestión de interrupciones Zero-Cross | Espressif ESP32-C3-WROOM-02-N4 |
| **PS1** | 1 | HLK-2M03 (AC/DC Aislado 3.3V 600mA) | Módulo 28x14x16mm | Fuente conmutada compacta entrada 85-264VAC, salida 3.3V DC aislada galvánicamente | Hi-Link HLK-2M03 |
| **OK1** | 1 | EL814 / PC814 (Optoacoplador entrada AC) | SMD SOP-4 | Detector de cruce por cero en ambos semiciclos de la red eléctrica AC | Everlight EL814S |
| **U2** | 1 | BL0942 (Chip Metrología Energética UART) | SSOP-10 | Medidor de alta precisión: Potencia activa (W), RMS Voltaje (V), RMS Corriente (A) | Shanghai Belling BL0942 |
| **R_SHUNT** | 1 | Shunt 1 mΩ 3W 1% Manganina | SMD 2512 | Derivador de corriente de muy bajo coeficiente térmico para medición de carga | Vishay WSL25121L000FEA |
| **RL1, RL2** | 2 | Hongfa HF32FV-16-12-HTF (16A 250VAC) | THT 19x15.5x15mm | Relés de potencia ultra-compactos con bobina de bajo consumo (200mW) y contactos AgSnO2 | Hongfa HF32FV-16 |
| **Q1, Q2** | 2 | S8050 NPN Transistor 40V 0.5A | SOT-23 | Drivers de activación de bobinas de relé gobernados por GPIO de ESP32-C3 | JCST S8050 |
| **D1, D2** | 2 | 1N4148W Diodo Flyback | SOD-123 | Supresión de picos inductivos de desenergización de las bobinas de los relés | Diodes Inc. 1N4148W |
| **OK2, OK3** | 2 | PC817 Optoacopladores de entrada | SOP-4 | Lectura optoaislada de tensión AC proveniente de pulsadores o conmutadas de pared S1/S2 | Sharp PC817X |
| **MOV1** | 1 | Varistor 10D471K (470V) | Disco 10mm THT | Supresión de sobretensiones transitorias en la entrada de línea AC | Epcos/TDK S10K300 |
| **F1** | 1 | Fusible cilíndrico cerámico 2A 250V Slow-Blow | Subminiatura THT | Protección de sobrecorriente y cortocircuito en placa | Littelfuse 39212000000 |
| **J1** | 1 | Bornero de tornillo 6 polos paso 5.0mm | Bloque modular THT | Terminales para L, N, L1_OUT, L2_OUT, S1_IN, S2_IN | Phoenix Contact MKDSN 1.5/6 |
"""

def main():
    base_dir = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/05_reles_conmutacion_pared/electrico"
    os.makedirs(base_dir, exist_ok=True)
    svg_dir = os.path.join(base_dir, "esquema_svg")
    os.makedirs(svg_dir, exist_ok=True)

    sch_path = os.path.join(base_dir, "micromodulo_rele_zerocross.kicad_sch")
    pro_path = os.path.join(base_dir, "micromodulo_rele_zerocross.kicad_pro")
    bom_path = os.path.join(base_dir, "BOM.md")

    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(KICAD_SCH_TEMPLATE)
    with open(pro_path, "w", encoding="utf-8") as f:
        f.write(KICAD_PRO_TEMPLATE)
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(BOM_RELE_CONTENT)
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
