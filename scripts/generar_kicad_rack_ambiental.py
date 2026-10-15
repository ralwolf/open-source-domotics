#!/usr/bin/env python3
"""
generar_kicad_rack_ambiental.py
Genera el esquema electrónico KiCad 10 (.kicad_sch), el proyecto (.kicad_pro),
la lista de materiales (BOM.md) y exporta el SVG del circuito para el
Controlador Ambiental, Monitoreo de Puerta y PDU de Rack 19" (ESP32-S3 + DS18B20 + SHT31 + PWM Fans + CT Sensor).
"""

import os
import subprocess

KICAD_SCH_TEMPLATE = """(kicad_sch (version 20240108) (generator "open-source-domotics-rack-gen")
  (uuid "a1200101-8ee4-4112-9c1a-rack00000001")
  (paper "A3")
  (lib_symbols
    (symbol "ESP32-S3-WROOM-1" (in_bom yes) (on_board yes)
      (property "Reference" "U1" (at 0 0 0))
      (property "Value" "ESP32-S3-WROOM-1" (at 0 -2.54 0))
      (property "Footprint" "RF_Module:ESP32-S3-WROOM-1" (at 0 -5.08 0))
    )
    (symbol "SHT31-DIS" (in_bom yes) (on_board yes)
      (property "Reference" "U2" (at 0 0 0))
      (property "Value" "SHT31-DIS (Humedad/Temp Intake)" (at 0 -2.54 0))
      (property "Footprint" "Package_DFN_QFN:DFN-8-1EP_2.5x2.5mm_P0.5mm_EP1.4x1.7mm" (at 0 -5.08 0))
    )
    (symbol "DS18B20_Dual" (in_bom yes) (on_board yes)
      (property "Reference" "J2" (at 0 0 0))
      (property "Value" "DS18B20 (1-Wire Exhaust/Intake)" (at 0 -2.54 0))
      (property "Footprint" "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" (at 0 -5.08 0))
    )
    (symbol "IRM-10-12" (in_bom yes) (on_board yes)
      (property "Reference" "PS1" (at 0 0 0))
      (property "Value" "Mean Well IRM-10-12 (230VAC->12VDC)" (at 0 -2.54 0))
      (property "Footprint" "Converter_ACDC:Converter_ACDC_MeanWell_IRM-10-xx_THT" (at 0 -5.08 0))
    )
    (symbol "IRLZ44N_PWM" (in_bom yes) (on_board yes)
      (property "Reference" "Q1" (at 0 0 0))
      (property "Value" "IRLZ44N (Driver PWM Extractores 12V)" (at 0 -2.54 0))
      (property "Footprint" "Package_TO_SOT_THT:TO-220-3_Vertical" (at 0 -5.08 0))
    )
    (symbol "Relay_G5LE" (in_bom yes) (on_board yes)
      (property "Reference" "RL1" (at 0 0 0))
      (property "Value" "Omron G5LE-1-DC12 (Iluminacion LED Rack)" (at 0 -2.54 0))
      (property "Footprint" "Relay_THT:Relay_SPDT_Omron-G5LE-1" (at 0 -5.08 0))
    )
    (symbol "SCT-013_CT" (in_bom yes) (on_board yes)
      (property "Reference" "J3" (at 0 0 0))
      (property "Value" "SCT-013-000 (Metrologia Corriente AC Rack)" (at 0 -2.54 0))
      (property "Footprint" "Connector_Audio:Jack_3.5mm_CUI_SJ1-3533NG_Horizontal" (at 0 -5.08 0))
    )
    (symbol "Screw_Terminal_01x08" (in_bom yes) (on_board yes)
      (property "Reference" "J1" (at 0 0 0))
      (property "Value" "Bornero I/O Rack & Puertas" (at 0 -2.54 0))
      (property "Footprint" "TerminalBlock:TerminalBlock_bornier-8_P5.08mm" (at 0 -5.08 0))
    )
  )

  (symbol (lib_id "ESP32-S3-WROOM-1") (at 120 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "a1200101-8ee4-4112-9c1a-esp32rk00001")
    (property "Reference" "U1" (at 120 60 0))
    (property "Value" "ESP32-S3-WROOM-1" (at 120 63 0))
    (property "Footprint" "RF_Module:ESP32-S3-WROOM-1" (at 120 66 0))
  )

  (symbol (lib_id "IRM-10-12") (at 45 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "a1200101-8ee4-4112-9c1a-psu10rk00001")
    (property "Reference" "PS1" (at 45 42 0))
    (property "Value" "Mean Well IRM-10-12 (230VAC->12VDC)" (at 45 45 0))
    (property "Footprint" "Converter_ACDC:Converter_ACDC_MeanWell_IRM-10-xx_THT" (at 45 48 0))
  )

  (symbol (lib_id "SHT31-DIS") (at 75 110 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "a1200101-8ee4-4112-9c1a-sht31rk00001")
    (property "Reference" "U2" (at 75 95 0))
    (property "Value" "SHT31-DIS (Humedad/Temp Intake)" (at 75 98 0))
    (property "Footprint" "Package_DFN_QFN:DFN-8-1EP_2.5x2.5mm_P0.5mm_EP1.4x1.7mm" (at 75 101 0))
  )

  (symbol (lib_id "DS18B20_Dual") (at 75 140 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "a1200101-8ee4-4112-9c1a-ds18brk00001")
    (property "Reference" "J2" (at 75 125 0))
    (property "Value" "DS18B20 (1-Wire Exhaust/Intake)" (at 75 128 0))
    (property "Footprint" "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" (at 75 131 0))
  )

  (symbol (lib_id "IRLZ44N_PWM") (at 190 70 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "a1200101-8ee4-4112-9c1a-fanmosrk0001")
    (property "Reference" "Q1" (at 190 55 0))
    (property "Value" "IRLZ44N (Driver PWM Extractores 12V)" (at 190 58 0))
    (property "Footprint" "Package_TO_SOT_THT:TO-220-3_Vertical" (at 190 61 0))
  )

  (symbol (lib_id "Relay_G5LE") (at 190 120 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "a1200101-8ee4-4112-9c1a-releledrk001")
    (property "Reference" "RL1" (at 190 105 0))
    (property "Value" "Omron G5LE-1-DC12 (Iluminacion LED Rack)" (at 190 108 0))
    (property "Footprint" "Relay_THT:Relay_SPDT_Omron-G5LE-1" (at 190 111 0))
  )

  (symbol (lib_id "SCT-013_CT") (at 75 75 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "a1200101-8ee4-4112-9c1a-sctct0rk0001")
    (property "Reference" "J3" (at 75 62 0))
    (property "Value" "SCT-013-000 (Metrologia Corriente AC Rack)" (at 75 65 0))
    (property "Footprint" "Connector_Audio:Jack_3.5mm_CUI_SJ1-3533NG_Horizontal" (at 75 68 0))
  )

  (symbol (lib_id "Screw_Terminal_01x08") (at 250 95 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "a1200101-8ee4-4112-9c1a-termblk00001")
    (property "Reference" "J1" (at 250 78 0))
    (property "Value" "Bornero I/O Rack & Puertas" (at 250 81 0))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-8_P5.08mm" (at 250 84 0))
  )

  (wire (pts (xy 45 60) (xy 75 75))
    (stroke (width 0.254) (type solid))
    (uuid "a1200101-8ee4-4112-9c1a-wire00000001")
  )
  (wire (pts (xy 75 75) (xy 120 80))
    (stroke (width 0.254) (type solid))
    (uuid "a1200101-8ee4-4112-9c1a-wire00000002")
  )
  (wire (pts (xy 75 110) (xy 120 80))
    (stroke (width 0.254) (type solid))
    (uuid "a1200101-8ee4-4112-9c1a-wire00000003")
  )
  (wire (pts (xy 75 140) (xy 120 80))
    (stroke (width 0.254) (type solid))
    (uuid "a1200101-8ee4-4112-9c1a-wire00000004")
  )
  (wire (pts (xy 120 80) (xy 190 70))
    (stroke (width 0.254) (type solid))
    (uuid "a1200101-8ee4-4112-9c1a-wire00000005")
  )
  (wire (pts (xy 120 80) (xy 190 120))
    (stroke (width 0.254) (type solid))
    (uuid "a1200101-8ee4-4112-9c1a-wire00000006")
  )
  (wire (pts (xy 190 70) (xy 250 95))
    (stroke (width 0.254) (type solid))
    (uuid "a1200101-8ee4-4112-9c1a-wire00000007")
  )
  (wire (pts (xy 190 120) (xy 250 95))
    (stroke (width 0.254) (type solid))
    (uuid "a1200101-8ee4-4112-9c1a-wire00000008")
  )

  (text "CONTROLADOR AMBIENTAL Y TELEMETRIA RACK 19 PULGADAS DATACENTER\\nESP32-S3 + DUAL DS18B20 + SHT31 + EXTRACTORES PWM + REED PUERTAS + SCT-013"
    (at 50 175 0)
    (effects (font (size 3.5 3.5)) (justify left bottom))
    (uuid "a1200101-8ee4-4112-9c1a-title0000001")
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
    "filename": "controlador_ambiental_rack_pdu.kicad_pro",
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
      "a1200101-8ee4-4112-9c1a-rack00000001",
      ""
    ]
  ],
  "text_variables": {}
}
"""

BOM_CONTENT = """# Lista de Materiales (BOM) - Controlador Ambiental y PDU Rack 19"

| Referencia | Componente | Descripción | Encapsulado | Cantidad | Función Principal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-S3-WROOM-1 | Microcontrolador Dual-Core 240MHz Wi-Fi/BLE con 8MB Flash | SMD RF Module | 1 | Procesamiento local y enlace ESPHome/MQTT |
| **U2** | SHT31-DIS | Sensor digital precisión I2C (±1.5% RH, ±0.2°C) | DFN-8 | 1 | Telemetría higrométrica de admisión frontal |
| **J2** | DS18B20 (x2) | Sensores térmicos 1-Wire encapsulados en acero inoxidable | Cabezal 1x3 THT | 2 | Monitoreo térmico directo en tobera de escape y SAI |
| **PS1** | Mean Well IRM-10-12 | Fuente AC/DC conmutada compacta 230VAC a 12VDC 0.85A | Módulo THT | 1 | Alimentación autónoma aislada 4kV del controlador |
| **Q1** | IRLZ44N | MOSFET N-Channel Logic Level 55V 47A RDS(on) 28mΩ | TO-220-3 | 1 | Modulación PWM silenciosa de ventiladores de techo 12V |
| **RL1** | Omron G5LE-1-DC12 | Relé electromecánico 12VDC bobina, 10A 250VAC contactos | THT SPDT | 1 | Conmutación de tira LED interior al abrir puerta |
| **J3** | SCT-013-000 | Transformador de corriente de núcleo partido 100A:50mA | Jack 3.5mm hembra | 1 | Medición de consumo RMS de la PDU sin interrumpir servicio |
| **J1** | Dinkle 5.08mm | Bornero de tornillo enchufable 8 polos | THT 5.08mm | 1 | Interfaz reed switches magnéticos puerta y ventiladores |
| **BZ1** | Piezo Buzzer 5V | Transductor piezoeléctrico acústico 85dB | THT 12mm | 1 | Alarma sonora por sobrecalentamiento o puerta abierta >2min |
| **R1-R4** | 4.7kΩ, 10kΩ, 22Ω | Resistencias de pull-up 1-Wire/I2C y carga burden CT | SMD 0805 | 6 | Acondicionamiento de señales y bus digital |
| **C1-C4** | 100nF, 10µF, 470µF | Condensadores cerámicos y electrolítico bajo ESR | 0805 / Radial | 5 | Desacoplo y filtrado de rizado de alimentación |
"""

def generar_kicad_rack():
    base_dir = "/home/ral/Documents/GitHub/open-source-domotics/02_infraestructura_it_y_red/01_rack_servidores_y_ups/electrico"
    svg_dir = os.path.join(base_dir, "esquema_svg")
    os.makedirs(svg_dir, exist_ok=True)

    sch_path = os.path.join(base_dir, "controlador_ambiental_rack_pdu.kicad_sch")
    pro_path = os.path.join(base_dir, "controlador_ambiental_rack_pdu.kicad_pro")
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
    generar_kicad_rack()
