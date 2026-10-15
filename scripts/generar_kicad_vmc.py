#!/usr/bin/env python3
"""
generar_kicad_vmc.py
Genera el esquema electrónico KiCad 10 (.kicad_sch), el proyecto (.kicad_pro),
la lista de materiales (BOM.md) y exporta el SVG del circuito controlador de la
Unidad de Ventilación Mecánica Controlada (VMC) de doble flujo con recuperación entálpica.
"""

import os
import subprocess

KICAD_SCH_TEMPLATE = """(kicad_sch (version 20240108) (generator "open-source-domotics-vmc-gen")
  (uuid "b820a101-3841-470a-9bc5-vmc000000001")
  (paper "A3")
  (lib_symbols
    (symbol "ESP32-S3-WROOM-1" (in_bom yes) (on_board yes)
      (property "Reference" "U1" (at 0 0 0))
      (property "Value" "ESP32-S3-WROOM-1" (at 0 -2.54 0))
      (property "Footprint" "RF_Module:ESP32-S3-WROOM-1" (at 0 -5.08 0))
    )
    (symbol "MCP4725" (in_bom yes) (on_board yes)
      (property "Reference" "U2" (at 0 0 0))
      (property "Value" "MCP4725A0T-E/CH" (at 0 -2.54 0))
      (property "Footprint" "Package_TO_SOT_SMD:SOT-23-6" (at 0 -5.08 0))
    )
    (symbol "LM358" (in_bom yes) (on_board yes)
      (property "Reference" "U3" (at 0 0 0))
      (property "Value" "LM358DR" (at 0 -2.54 0))
      (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 0 -5.08 0))
    )
    (symbol "DRV8871" (in_bom yes) (on_board yes)
      (property "Reference" "U4" (at 0 0 0))
      (property "Value" "DRV8871DDAR" (at 0 -2.54 0))
      (property "Footprint" "Package_SO:SOIC-8-1EP_3.9x4.9mm_P1.27mm" (at 0 -5.08 0))
    )
    (symbol "PC817" (in_bom yes) (on_board yes)
      (property "Reference" "OK1" (at 0 0 0))
      (property "Value" "PC817" (at 0 -2.54 0))
      (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 0 -5.08 0))
    )
    (symbol "SDP810-500Pa" (in_bom yes) (on_board yes)
      (property "Reference" "SEN1" (at 0 0 0))
      (property "Value" "SDP810-500Pa" (at 0 -2.54 0))
      (property "Footprint" "Sensor_Pressure:Sensirion_SDP8xx" (at 0 -5.08 0))
    )
    (symbol "SCD41" (in_bom yes) (on_board yes)
      (property "Reference" "SEN2" (at 0 0 0))
      (property "Value" "SCD41-CO2" (at 0 -2.54 0))
      (property "Footprint" "Sensor:Sensirion_SCD4x" (at 0 -5.08 0))
    )
    (symbol "MP1584EN" (in_bom yes) (on_board yes)
      (property "Reference" "VR1" (at 0 0 0))
      (property "Value" "MP1584EN-Buck-24V-5V" (at 0 -2.54 0))
      (property "Footprint" "Package_SO:SOIC-8-1EP_3.9x4.9mm_P1.27mm" (at 0 -5.08 0))
    )
    (symbol "Screw_Terminal_01x04" (in_bom yes) (on_board yes)
      (property "Reference" "J1" (at 0 0 0))
      (property "Value" "Screw_Terminal_01x04" (at 0 -2.54 0))
      (property "Footprint" "TerminalBlock:TerminalBlock_bornier-4_P5.08mm" (at 0 -5.08 0))
    )
  )

  (symbol (lib_id "ESP32-S3-WROOM-1") (at 100 80 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "b820a101-3841-470a-9bc5-esp32s3000001")
    (property "Reference" "U1" (at 100 60 0))
    (property "Value" "ESP32-S3-WROOM-1" (at 100 63 0))
    (property "Footprint" "RF_Module:ESP32-S3-WROOM-1" (at 100 66 0))
  )

  (symbol (lib_id "MCP4725") (at 180 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "b820a101-3841-470a-9bc5-dac000000001")
    (property "Reference" "U2" (at 180 50 0))
    (property "Value" "MCP4725A0T-E/CH (DAC 0-3.3V)" (at 180 53 0))
    (property "Footprint" "Package_TO_SOT_SMD:SOT-23-6" (at 180 56 0))
  )

  (symbol (lib_id "LM358") (at 230 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "b820a101-3841-470a-9bc5-opamp0000001")
    (property "Reference" "U3" (at 230 50 0))
    (property "Value" "LM358DR (Amplificador 0-10V)" (at 230 53 0))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 230 56 0))
  )

  (symbol (lib_id "DRV8871") (at 180 110 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "b820a101-3841-470a-9bc5-drv000000001")
    (property "Reference" "U4" (at 180 100 0))
    (property "Value" "DRV8871 (Driver Bypass 24V 3.6A)" (at 180 103 0))
    (property "Footprint" "Package_SO:SOIC-8-1EP_3.9x4.9mm_P1.27mm" (at 180 106 0))
  )

  (symbol (lib_id "PC817") (at 100 150 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "b820a101-3841-470a-9bc5-optotach0001")
    (property "Reference" "OK1" (at 100 140 0))
    (property "Value" "PC817 (Aislamiento Tacómetro RPM)" (at 100 143 0))
    (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 100 146 0))
  )

  (symbol (lib_id "SDP810-500Pa") (at 260 110 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "b820a101-3841-470a-9bc5-sdp810000001")
    (property "Reference" "SEN1" (at 260 100 0))
    (property "Value" "SDP810-500Pa (Sensor Presion Filtros)" (at 260 103 0))
    (property "Footprint" "Sensor_Pressure:Sensirion_SDP8xx" (at 260 106 0))
  )

  (symbol (lib_id "SCD41") (at 260 150 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "b820a101-3841-470a-9bc5-scd410000001")
    (property "Reference" "SEN2" (at 260 140 0))
    (property "Value" "SCD41-CO2 (NDIR 400-5000 ppm)" (at 260 143 0))
    (property "Footprint" "Sensor:Sensirion_SCD4x" (at 260 146 0))
  )

  (symbol (lib_id "MP1584EN") (at 50 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "b820a101-3841-470a-9bc5-buck00000001")
    (property "Reference" "VR1" (at 50 50 0))
    (property "Value" "MP1584EN (Regulador Buck 24V a 5V/3.3V)" (at 50 53 0))
    (property "Footprint" "Package_SO:SOIC-8-1EP_3.9x4.9mm_P1.27mm" (at 50 56 0))
  )

  (symbol (lib_id "Screw_Terminal_01x04") (at 320 60 0) (unit 1)
    (in_bom yes) (on_board yes) (uuid "b820a101-3841-470a-9bc5-termec000001")
    (property "Reference" "J1" (at 320 50 0))
    (property "Value" "Bornero Ventiladores EC (0-10V + TACH)" (at 320 53 0))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-4_P5.08mm" (at 320 56 0))
  )

  (wire (pts (xy 65 60) (xy 80 80)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 120 75) (xy 160 60)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 200 60) (xy 215 60)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 245 60) (xy 300 60)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 120 85) (xy 160 110)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 120 95) (xy 240 110)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 120 100) (xy 240 150)) (stroke (width 0.25) (type default)))
  (wire (pts (xy 100 130) (xy 100 110)) (stroke (width 0.25) (type default)))

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
    "filename": "controlador_vmc_recuperador.kicad_pro",
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
      "b820a101-3841-470a-9bc5-vmc000000001",
      ""
    ]
  ]
}
"""

BOM_VMC_CONTENT = """# Lista de Materiales (BOM) - Placa Controladora de VMC con Recuperador Entálpico

| Ref | Cantidad | Componente / Valor | Encapsulado | Función Técnica | Fabricante / N° de Parte |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **U1** | 1 | ESP32-S3-WROOM-1 (8MB Flash) | SMD Módulo 18x25.5mm | Microcontrolador central Dual-Core 240MHz, WiFi, BLE, FreeRTOS | Espressif ESP32-S3-WROOM-1-N8 |
| **U2** | 2 | MCP4725A0T-E/CH (DAC 12-bit I2C) | SOT-23-6 | Generador de tensión analógica precisa 0 a 3.3V para control de velocidad | Microchip MCP4725 |
| **U3** | 1 | LM358DR (Op-Amp Rail-to-Rail) | SOIC-8 | Amplificador no inversor ganancia $G=3.03$ para convertir $0-3.3\text{V} \to 0-10\text{V}$ EC | Texas Instruments LM358DR |
| **U4** | 1 | DRV8871DDAR (Puente H 3.6A 45V) | SOIC-8-1EP | Driver PWM para actuador reversible 24V de compuerta bypass Free-Cooling | Texas Instruments DRV8871 |
| **OK1-OK2** | 2 | PC817 Optoacoplador | DIP-4 | Aislamiento galvánico 5kV para lectura tacométrica (TACH) de RPM de motores EC | Sharp PC817X |
| **SEN1** | 1 | Sensirion SDP810-500Pa | Montaje placa con toberas | Sensor de presión diferencial I2C de ultra-precisión para colmatación de filtros | Sensirion SDP810-500Pa |
| **SEN2** | 1 | Sensirion SCD41 (NDIR CO2 + RH + T) | SMD 10.1x10.1mm | Sensor fotoacústico de CO2 (400-5000 ppm) y HR interior | Sensirion SCD41 |
| **TH1-TH4** | 4 | DS18B20 / NTC 10k 1% | Sondas encapsuladas AISI316 | Monitoreo de 4 temperaturas: T_exterior, T_impulsión, T_extracción, T_expulsión | Dallas/Maxim DS18B20 |
| **VR1** | 1 | MP1584EN Step-Down 24V $\to$ 5V 3A | SOIC-8-1EP | Convertidor buck DC-DC síncrono de alta eficiencia (>92%) | Monolithic Power MP1584EN |
| **VR2** | 1 | AMS1117-3.3 LDO | SOT-223 | Regulador lineal ultra-bajo ruido para lógica 3.3V y sensores I2C | Diodes Inc. AMS1117-3.3 |
| **J1-J4** | 4 | Borneros de tornillo paso 5.08mm | PCB Bornier 4P/3P | Conexión para motores EC (24V, GND, 0-10V, TACH) y actuador Belimo | Phoenix Contact MKDSN |
| **F1** | 1 | Fusible rearmable PTC Polyswitch 30V 2A | SMD 2920 | Protección contra sobrecorrientes en línea de alimentación y bypass | Littelfuse 2920L200 |
"""

def main():
    base_dir = "/home/ral/Documents/GitHub/open-source-domotics/04_telemetria_y_cargas_criticas/06_climatizacion_vmc_recuperador_calor/electrico"
    os.makedirs(base_dir, exist_ok=True)
    svg_dir = os.path.join(base_dir, "esquema_svg")
    os.makedirs(svg_dir, exist_ok=True)

    sch_path = os.path.join(base_dir, "controlador_vmc_recuperador.kicad_sch")
    pro_path = os.path.join(base_dir, "controlador_vmc_recuperador.kicad_pro")
    bom_path = os.path.join(base_dir, "BOM.md")

    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(KICAD_SCH_TEMPLATE)
    with open(pro_path, "w", encoding="utf-8") as f:
        f.write(KICAD_PRO_TEMPLATE)
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(BOM_VMC_CONTENT)
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
