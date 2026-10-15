#!/usr/bin/env python3
"""
Generador de Proyecto y Esquema Electrónico KiCad 10.0
Proyecto: Controlador de Filtración y Dosificación Química de Piscina (pH / Redox / Temperatura)
Módulo: 05_confort_y_exteriores/04_mantenimiento_automatizado_piscina/electrico
"""

import os
import uuid
import subprocess

def generar_kicad_piscina(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    pro_path = os.path.join(output_dir, "controlador_quimica_piscina.kicad_pro")
    sch_path = os.path.join(output_dir, "controlador_quimica_piscina.kicad_sch")
    bom_path = os.path.join(output_dir, "BOM.md")

    root_uuid = str(uuid.uuid4())

    # 1. KICAD PROJECT (.kicad_pro)
    pro_content = f"""{{
  "boards": [],
  "meta": {{
    "filename": "controlador_quimica_piscina.kicad_pro",
    "version": 3
  }},
  "net_settings": {{
    "classes": [
      {{
        "clearance": 0.25,
        "diff_pair_gap": 0.25,
        "diff_pair_width": 0.35,
        "name": "Default",
        "track_width": 0.3,
        "via_diameter": 0.8,
        "via_drill": 0.4
      }},
      {{
        "clearance": 0.8,
        "diff_pair_gap": 0.3,
        "diff_pair_width": 0.5,
        "name": "Mains_230VAC_Isolation",
        "track_width": 1.5,
        "via_diameter": 2.0,
        "via_drill": 1.0
      }},
      {{
        "clearance": 0.5,
        "diff_pair_gap": 0.25,
        "diff_pair_width": 0.35,
        "name": "Analog_Isolated_pH_ORP",
        "track_width": 0.4,
        "via_diameter": 0.8,
        "via_drill": 0.4
      }}
    ],
    "meta": {{
      "version": 4
    }}
  }},
  "schematic": {{
    "annotate_start_num": 0,
    "bom_export_filename": "${{PROJECTNAME}}.csv",
    "meta": {{
      "version": 1
    }}
  }},
  "sheets": [
    [
      "{root_uuid}",
      ""
    ]
  ]
}}
"""
    with open(pro_path, "w", encoding="utf-8") as f:
        f.write(pro_content)

    # 2. KICAD SCHEMATIC (.kicad_sch)
    def u(): return str(uuid.uuid4())

    sch_content = f"""(kicad_sch
  (version 20231120)
  (generator "open-source-domotics-gen")
  (generator_version "10.0")
  (uuid "{root_uuid}")
  (paper "A3")
  (title_block
    (title "CONTROLADOR DE FILTRACION Y DOSIFICACION QUIMICA DE PISCINA")
    (date "2026-10-15")
    (rev "v1.0")
    (company "open-source-domotics (Hardware Libre)")
    (comment 1 "Front-End Aislado Galvánicamente pH y Redox (ORP) con ADS1115 16-bit")
    (comment 2 "Interbloqueo Flow-Switch + Bombas Peristálticas 24V + Relé Bomba 1CV 230V")
  )

  (wire (pts (xy 30.0 45.0) (xy 70.0 45.0))
    (stroke (width 0) (type default))
    (uuid "{u()}")
  )
  (text "ALIMENTACION_24VDC"
    (at 30.0 43.0 0)
    (effects (font (size 1.5 1.5)))
    (uuid "{u()}")
  )

  (symbol
    (lib_id "Regulator_Switching:MP1584")
    (at 80.0 55.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U1" (at 80.0 42.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "MP1584_24V_to_5V" (at 80.0 45.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Converter_DCDC:Converter_DCDC_MP1584_Mini" (at 80.0 55.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Converter_DCDC:B0505S-1WR3")
    (at 80.0 85.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U2" (at 80.0 72.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "B0505S_Aislamiento_1kV" (at 80.0 75.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Converter_DCDC:Converter_DCDC_Mornsun_B_S-1WR3" (at 80.0 85.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "RF_Module:ESP32-WROOM-32E")
    (at 150.0 70.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U3" (at 150.0 40.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "ESP32-WROOM-32E" (at 150.0 43.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "RF_Module:ESP32-WROOM-32E" (at 150.0 70.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Amplifier_Operational:LMC6001")
    (at 220.0 60.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U4" (at 220.0 48.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LMC6001_pH_Ib_25fA" (at 220.0 51.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 220.0 60.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Amplifier_Operational:LMC6001")
    (at 220.0 90.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U5" (at 220.0 78.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LMC6001_ORP_Ib_25fA" (at 220.0 81.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 220.0 90.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Analog_ADC:ADS1115IDGS")
    (at 220.0 125.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U6" (at 220.0 112.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "ADS1115_16Bit_I2C" (at 220.0 115.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:MSOP-10_3x3mm_P0.5mm" (at 220.0 125.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector:BNC")
    (at 275.0 60.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J1" (at 275.0 50.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BNC_ELECTRODO_PH" (at 275.0 53.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_Coaxial:BNC_Amphenol_B6252HB-NPP3G-50_Horizontal" (at 275.0 60.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector:BNC")
    (at 275.0 90.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J2" (at 275.0 80.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BNC_ELECTRODO_ORP" (at 275.0 83.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_Coaxial:BNC_Amphenol_B6252HB-NPP3G-50_Horizontal" (at 275.0 90.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Transistor_FET:AOD4184A")
    (at 330.0 60.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "Q1" (at 330.0 48.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "AOD4184A_DOSI_PH" (at 330.0 51.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:TO-252-2" (at 330.0 60.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Transistor_FET:AOD4184A")
    (at 330.0 90.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "Q2" (at 330.0 78.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "AOD4184A_DOSI_CLORO" (at 330.0 81.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:TO-252-2" (at 330.0 90.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Relay:Relay_SPST")
    (at 330.0 125.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "K1" (at 330.0 112.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "RELE_BOMBA_1CV_16A" (at 330.0 115.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Relay_THT:Relay_SPDT_Omron-G5Q-1" (at 330.0 125.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x02")
    (at 380.0 60.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J3" (at 380.0 50.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "SALIDA_DOSI_PH_24V" (at 380.0 53.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" (at 380.0 60.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x02")
    (at 380.0 90.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J4" (at 380.0 80.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "SALIDA_DOSI_CL_24V" (at 380.0 83.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" (at 380.0 90.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x02")
    (at 380.0 125.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J5" (at 380.0 115.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "SALIDA_CONTACTOR_BOMBA" (at 380.0 118.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" (at 380.0 125.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x02")
    (at 100.0 130.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J6" (at 100.0 120.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "ENTRADA_FLOW_SWITCH" (at 100.0 123.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" (at 100.0 130.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x03")
    (at 100.0 155.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J7" (at 100.0 145.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "SONDA_TEMP_DS18B20" (at 100.0 148.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-3_P5.08mm" (at 100.0 155.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (sheet_instances
    (path "/" (page "1"))
  )
)
"""
    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(sch_content)

    # 3. LISTA DE MATERIALES (BOM.md)
    bom_content = """# Lista de Materiales (BOM) - Controlador Químico y Filtración Piscina

| Ref | Cantidad | Descripción | Encapsulado | Función Técnica | Proveedor / P/N | Coste Est. (EUR) |
|---|---|---|---|---|---|---|
| U1 | 1 | Regulador Buck Step-Down MP1584 | Módulo SMD | 24V a 5V/3.3V para ESP32 y periféricos | Monolithic Power MP1584EN | 1.80 |
| U2 | 1 | Convertidor DC-DC Aislado B0505S-1WR3 | SIP-4 | Aislamiento galvánico 1kV para sondas pH/ORP | Mornsun B0505S-1WR3 | 3.20 |
| U3 | 1 | Microcontrolador ESP32-WROOM-32E 8MB | SMD Module | Lógica de filtración, PID químico, ESPHome | Espressif ESP32-WROOM-32E | 3.50 |
| U4-U5 | 2 | Amp Op Ultra-Baja Corriente Polarización LMC6001 | SOIC-8 | Amplificador de electroteca para electrodos pH/ORP ($I_b < 25\text{ fA}$) | Texas Instruments LMC6001AIN | 5.80 |
| U6 | 1 | Convertidor ADC 16-Bit I2C Aislado ADS1115 | MSOP-10 | Muestreo de alta resolución para lecturas mV | Texas Instruments ADS1115IDGST | 3.10 |
| J1-J2 | 2 | Conector BNC Hembra 50Ω Montaje PCB Chasis | BNC THT | Conexión blindada para electrodos de vidrio | Amphenol B6252HB | 3.60 |
| Q1-Q2 | 2 | MOSFET Canal N AOD4184A (40V, 50A, 8.5mΩ) | TO-252 | Driver PWM bombas peristálticas 24V 1.5A | Alpha & Omega AOD4184A | 1.40 |
| D1-D2 | 2 | Diodo Flyback Ultrarrápido 1N5408 | DO-201AD | Protección contra fuerza contraelectromotriz motor | Vishay 1N5408 | 0.60 |
| K1 | 1 | Relé de Potencia 16A 250VAC Bobina 12V/24V | THT | Maniobra contactor bobina bomba 1 CV 230V | Omron G5Q-1 24VDC | 2.20 |
| J3-J6 | 4 | Bornero Tornillo 2P 5.08mm 15A | THT | Conexión peristálticas, contactor y flow switch | Phoenix Contact 1729128 | 3.20 |
| J7 | 1 | Bornero Tornillo 3P 5.08mm | THT | Conexión sonda temperatura digital DS18B20 | Phoenix Contact 1729131 | 1.10 |
| R1-R6 | 6 | Resistencias SMD 0805 1% (10k, 4.7k, 1k) | SMD 0805 | Pull-ups 1-Wire e I2C y filtros pasivos | Yageo RC0805FR | 0.30 |
| C1-C8 | 8 | Condensadores Cerámicos 100nF y 10µF X7R | SMD 0805 | Desacoplo de ruido analógico y alimentación | Murata GRM21 | 0.80 |
| PCB | 1 | Placa de Circuito Impreso Doble Cara 2oz Cu | FR4 100x80mm | Plano de masa analógica aislada | JLCPCB / PCBWay | 2.50 |
| **TOTAL** | | | | | | **33.10 EUR** |
"""
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(bom_content)

    print(f"Proyecto KiCad Piscina generado en: {output_dir}")
    print(f"BOM generado en: {bom_path}")

    # 4. EXPORTAR ESQUEMA A SVG MEDIANTE KICAD-CLI
    svg_dir = os.path.join(output_dir, "esquema_svg")
    os.makedirs(svg_dir, exist_ok=True)
    cmd = [
        "flatpak-spawn", "--host", "flatpak", "run",
        "--command=kicad-cli", "org.kicad.KiCad",
        "sch", "export", "svg",
        sch_path,
        "-o", svg_dir
    ]
    try:
        subprocess.run(cmd, check=True)
        print(f"Esquema SVG exportado mediante kicad-cli en: {svg_dir}")
    except Exception as e:
        print(f"Nota: kicad-cli finalizó: {e}")

if __name__ == "__main__":
    out = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/04_mantenimiento_automatizado_piscina/electrico"
    generar_kicad_piscina(out)

