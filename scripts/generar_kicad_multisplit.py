#!/usr/bin/env python3
"""
generar_kicad_multisplit.py
Genera el esquema electrónico KiCad 10 (.kicad_sch), el proyecto (.kicad_pro),
la lista de materiales (BOM.md) y exporta el SVG del circuito para la
Pasarela IoT de Climatización Multi-Split (Puerto CN105 / Midea UART + IR + SHT31 + Sensor Ventana).
"""

import os
import subprocess

KICAD_SCH_TEMPLATE = """(kicad_sch (version 20240108) (generator "open-source-domotics-split-gen")
  (uuid "d041c303-5a63-692c-bdf7-split0000001")
  (paper "A3")
  (lib_symbols
    (symbol "ESP32-C3-WROOM-02" (in_bom yes) (on_board yes)
      (property "Reference" "U1" (at 0 0 0))
      (property "Value" "ESP32-C3-WROOM-02" (at 0 -2.54 0))
      (property "Footprint" "RF_Module:ESP32-C3-WROOM-02" (at 0 -5.08 0))
    )
    (symbol "TXS0102DCUR" (in_bom yes) (on_board yes)
      (property "Reference" "U2" (at 0 0 0))
      (property "Value" "TXS0102 (Level Shifter 3.3V<->5V)" (at 0 -2.54 0))
      (property "Footprint" "Package_SO:VSSOP-8_2.3x2mm_P0.5mm" (at 0 -5.08 0))
    )
    (symbol "SHT31-DIS" (in_bom yes) (on_board yes)
      (property "Reference" "SEN1" (at 0 0 0))
      (property "Value" "SHT31-DIS (Temp/HR I2C)" (at 0 -2.54 0))
      (property "Footprint" "Sensor_Humidity:Sensirion_DFN-8-1EP_2.5x2.5mm_P0.5mm_EP1.1x1.7mm" (at 0 -5.08 0))
    )
    (symbol "MP1584EN" (in_bom yes) (on_board yes)
      (property "Reference" "VR1" (at 0 0 0))
      (property "Value" "MP1584EN (Buck 12V->3.3V)" (at 0 -2.54 0))
      (property "Footprint" "Package_SO:SOIC-8-1EP_3.9x4.9mm_P1.27mm" (at 0 -5.08 0))
    )
    (symbol "PC817" (in_bom yes) (on_board yes)
      (property "Reference" "OK1" (at 0 0 0))
      (property "Value" "PC817 (Aislamiento Sensor Ventana)" (at 0 -2.54 0))
      (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 0 -5.08 0))
    )
    (symbol "VS1838B" (in_bom yes) (on_board yes)
      (property "Reference" "IR1" (at 0 0 0))
      (property "Value" "VS1838B (Receptor IR 38kHz)" (at 0 -2.54 0))
      (property "Footprint" "OptoDevice:Receiver_Infrared_ThroughHole" (at 0 -5.08 0))
    )
    (symbol "Conn_01x05" (in_bom yes) (on_board yes)
      (property "Reference" "J1" (at 0 0 0))
      (property "Value" "Conector CN105 / Midea (12V, GND, TX, RX, 5V)" (at 0 -2.54 0))
      (property "Footprint" "Connector_JST:JST_PA_S5B-PASK-2_1x05_P2.00mm_Horizontal" (at 0 -5.08 0))
    )
  )

  (symbol (lib_id "ESP32-C3-WROOM-02") (at 120 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "d041c303-5a63-692c-bdf7-esp32c300001")
    (property "Reference" "U1" (at 120 60 0))
    (property "Value" "ESP32-C3-WROOM-02" (at 120 63 0))
    (property "Footprint" "RF_Module:ESP32-C3-WROOM-02" (at 120 66 0))
  )

  (symbol (lib_id "MP1584EN") (at 50 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "d041c303-5a63-692c-bdf7-buck00000001")
    (property "Reference" "VR1" (at 50 48 0))
    (property "Value" "MP1584EN (12V->3.3V)" (at 50 51 0))
    (property "Footprint" "Package_SO:SOIC-8-1EP_3.9x4.9mm_P1.27mm" (at 50 54 0))
  )

  (symbol (lib_id "TXS0102DCUR") (at 190 70 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "d041c303-5a63-692c-bdf7-txs000000001")
    (property "Reference" "U2" (at 190 58 0))
    (property "Value" "TXS0102 (Adaptador UART)" (at 190 61 0))
    (property "Footprint" "Package_SO:VSSOP-8_2.3x2mm_P0.5mm" (at 190 64 0))
  )

  (symbol (lib_id "Conn_01x05") (at 260 70 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "d041c303-5a63-692c-bdf7-cn1050000001")
    (property "Reference" "J1" (at 260 56 0))
    (property "Value" "Conector CN105 Split" (at 260 59 0))
    (property "Footprint" "Connector_JST:JST_PA_S5B-PASK-2_1x05_P2.00mm_Horizontal" (at 260 62 0))
  )

  (symbol (lib_id "SHT31-DIS") (at 120 130 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "d041c303-5a63-692c-bdf7-sht310000001")
    (property "Reference" "SEN1" (at 120 120 0))
    (property "Value" "SHT31-DIS" (at 120 123 0))
    (property "Footprint" "Sensor_Humidity:Sensirion_DFN-8-1EP_2.5x2.5mm_P0.5mm_EP1.1x1.7mm" (at 120 126 0))
  )

  (symbol (lib_id "PC817") (at 50 110 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "d041c303-5a63-692c-bdf7-reed00000001")
    (property "Reference" "OK1" (at 50 100 0))
    (property "Value" "PC817 (Sensor Ventana)" (at 50 103 0))
    (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 50 106 0))
  )

  (symbol (lib_id "VS1838B") (at 190 120 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "d041c303-5a63-692c-bdf7-ir0000000001")
    (property "Reference" "IR1" (at 190 110 0))
    (property "Value" "VS1838B (Receptor IR)" (at 190 113 0))
    (property "Footprint" "OptoDevice:Receiver_Infrared_ThroughHole" (at 190 116 0))
  )

  (wire (pts (xy 65 60) (xy 100 75)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 140 75) (xy 170 70)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 210 70) (xy 240 70)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 120 110) (xy 120 95)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 65 110) (xy 100 85)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 170 120) (xy 140 85)) (stroke (width 0.25) (type default)))

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
    "filename": "pasarela_climatizacion_split.kicad_pro",
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
      "d041c303-5a63-692c-bdf7-split0000001",
      ""
    ]
  ]
}
"""

BOM_SPLIT_CONTENT = """# Lista de Materiales (BOM) - Pasarela IoT de Climatización Multi-Split

| Ref | Cantidad | Componente / Valor | Encapsulado | Función Técnica | Fabricante / N° de Parte |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **U1** | 1 | ESP32-C3-WROOM-02 (4MB Flash) | SMD Módulo 18x20mm | SoC RISC-V 160MHz con WiFi 802.11 b/g/n y Bluetooth Low Energy 5.0 | Espressif ESP32-C3-WROOM-02-N4 |
| **U2** | 1 | TXS0102DCUR (Level Shifter Bidireccional) | VSSOP-8 | Conversor de nivel de voltaje bidireccional de 3.3V (ESP32) a 5V (Bus CN105/Midea) | Texas Instruments TXS0102 |
| **VR1** | 1 | MP1584EN Step-Down DC-DC | SOIC-8-1EP | Convertidor reductor síncrono para obtener 3.3V estables desde los 12V del split | Monolithic Power MP1584EN |
| **SEN1** | 1 | Sensirion SHT31-DIS | DFN-8 | Sensor digital de temperatura (±0.2°C) y humedad relativa (±2%) por I2C | Sensirion SHT31-DIS-B |
| **OK1** | 1 | PC817 Optoacoplador | SOP-4 | Aislamiento galvánico de la entrada cableada para sensor magnético de ventana | Sharp PC817X |
| **IR1** | 1 | VS1838B Receptor Infrarrojo 38kHz | THT 3 pines | Decodificador de comandos IR para compatibilidad con mandos a distancia originales | Vishay TSOP38238 / VS1838B |
| **D1** | 1 | IR LED 940nm 5mm de alta potencia | THT Radial | Emisor de ráfagas infrarrojas para control universal de splits sin puerto serie | Vishay TSAL6400 |
| **Q1** | 1 | 2N2222A Transistor NPN 40V 0.8A | SOT-23 | Driver de conmutación de corriente para el LED emisor de infrarrojos | ON Semi MMBT2222A |
| **J1** | 1 | Conector JST-PA 5 pines horizontal 2.0mm | PCB Conector | Enchufe hembra para cable arnés hacia el puerto CN105 / CN40 de la placa del split | JST S5B-PASK-2(LF)(SN) |
| **F1** | 1 | Fusible SMD PTC Polyswitch 30V 500mA | SMD 1812 | Protección autorrearmable contra sobrecorrientes en la línea de 12V del split | Littelfuse 1812L050PR |
"""

def main():
    base_dir = "/home/ral/Documents/GitHub/open-source-domotics/04_telemetria_y_cargas_criticas/05_climatizacion_multisplit/electrico"
    os.makedirs(base_dir, exist_ok=True)
    svg_dir = os.path.join(base_dir, "esquema_svg")
    os.makedirs(svg_dir, exist_ok=True)

    sch_path = os.path.join(base_dir, "pasarela_climatizacion_split.kicad_sch")
    pro_path = os.path.join(base_dir, "pasarela_climatizacion_split.kicad_pro")
    bom_path = os.path.join(base_dir, "BOM.md")

    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(KICAD_SCH_TEMPLATE)
    with open(pro_path, "w", encoding="utf-8") as f:
        f.write(KICAD_PRO_TEMPLATE)
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(BOM_SPLIT_CONTENT)
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

