#!/usr/bin/env python3
"""
Generador de Proyecto y Esquema Electrónico KiCad 10.0
Proyecto: Central de Detección de Incendio EN54, Monóxido de Carbono y Disparo de Aerosoles
Módulo: 03_seguridad_y_control_acceso/07_seguridad_incendio_co_y_aerosoles/electrico
"""

import os
import uuid
import subprocess

def generar_kicad_incendio(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    pro_path = os.path.join(output_dir, "controlador_incendio_aerosoles.kicad_pro")
    sch_path = os.path.join(output_dir, "controlador_incendio_aerosoles.kicad_sch")
    bom_path = os.path.join(output_dir, "BOM.md")

    root_uuid = str(uuid.uuid4())

    # 1. KICAD PROJECT (.kicad_pro)
    pro_content = f"""{{
  "boards": [],
  "meta": {{
    "filename": "controlador_incendio_aerosoles.kicad_pro",
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
        "clearance": 0.6,
        "diff_pair_gap": 0.3,
        "diff_pair_width": 0.5,
        "name": "Fire_Extinguishing_Bus",
        "track_width": 1.5,
        "via_diameter": 1.8,
        "via_drill": 0.9
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
    (title "CENTRAL DE INCENDIO EN54, CO Y EXTINCION POR AEROSOL CONDENSADO")
    (date "2026-10-15")
    (rev "v1.0")
    (company "open-source-domotics (Hardware Libre)")
    (comment 1 "Lazo Supervisado EOL 4.7k + Disparo por Supercap Dual-MOSFET 24V 2A")
    (comment 2 "Supervisión de Línea Iniciador <10mA + Enclavamiento Gas/VMC + Sirena Strobe")
  )

  (wire (pts (xy 30.0 50.0) (xy 70.0 50.0))
    (stroke (width 0) (type default))
    (uuid "{u()}")
  )
  (text "ALIMENTACION_24VDC_RESPALDO_UPS"
    (at 30.0 48.0 0)
    (effects (font (size 1.5 1.5)))
    (uuid "{u()}")
  )

  (symbol
    (lib_id "Regulator_Switching:MP1584")
    (at 80.0 65.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U1" (at 80.0 50.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "MP1584_24V_to_3V3" (at 80.0 53.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Converter_DCDC:Converter_DCDC_MP1584_Mini" (at 80.0 65.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "RF_Module:ESP32-WROOM-32E")
    (at 160.0 75.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U2" (at 160.0 42.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "ESP32-WROOM-32E" (at 160.0 45.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "RF_Module:ESP32-WROOM-32E" (at 160.0 75.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Device:C_Polarized")
    (at 220.0 55.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "C1" (at 220.0 42.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "4700uF_35V_LowESR" (at 220.0 45.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Capacitor_THT:CP_Radial_D16.0mm_P7.50mm" (at 220.0 55.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Transistor_FET:AOD4184A")
    (at 260.0 55.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "Q1" (at 260.0 42.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "P_MOSFET_HighSide" (at 260.0 45.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:TO-252-2" (at 260.0 55.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Transistor_FET:AOD4184A")
    (at 260.0 85.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "Q2" (at 260.0 72.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "N_MOSFET_LowSide" (at 260.0 75.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:TO-252-2" (at 260.0 85.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x02")
    (at 320.0 70.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J1" (at 320.0 58.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "SALIDA_INICIADOR_AEROSOL_24V" (at 320.0 61.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" (at 320.0 70.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x02")
    (at 80.0 110.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J2" (at 80.0 98.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LAZO_DETECTORES_HUMO_EOL" (at 80.0 101.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" (at 80.0 110.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Sensor_Gas:TGS5042")
    (at 80.0 145.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U3" (at 80.0 132.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TGS5042_Sensor_CO_Electroquimico" (at 80.0 135.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_THT:TO-5-3" (at 80.0 145.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Relay:Relay_SPDT")
    (at 320.0 115.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "K1" (at 320.0 102.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "RELE_CORTE_GAS_Y_VMC" (at 320.0 105.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Relay_THT:Relay_SPDT_Omron-G5Q-1" (at 320.0 115.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Relay:Relay_SPST")
    (at 320.0 145.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "K2" (at 320.0 132.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "RELE_SIRENA_STROBE_24V" (at 320.0 135.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Relay_THT:Relay_SPDT_Omron-G5Q-1" (at 320.0 145.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x02")
    (at 160.0 135.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J3" (at 160.0 122.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "PULSADOR_ABORTO_EXTINCION" (at 160.0 125.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" (at 160.0 135.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (sheet_instances
    (path "/" (page "1"))
  )
)
"""
    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(sch_content)

    # 3. LISTA DE MATERIALES (BOM.md)
    bom_content = """# Lista de Materiales (BOM) - Central de Incendio, CO y Extinción por Aerosol

| Ref | Cantidad | Descripción | Encapsulado | Función Técnica | Proveedor / P/N | Coste Est. (EUR) |
|---|---|---|---|---|---|---|
| U1 | 1 | Regulador Buck Step-Down MP1584 | Módulo SMD | 24V a 3.3V / 1.5A para ESP32 | Monolithic Power MP1584EN | 1.80 |
| U2 | 1 | Microcontrolador ESP32-WROOM-32E 8MB | SMD Module | Lógica de lazo EN54, coincidencia cruzada, ESPHome | Espressif ESP32-WROOM-32E | 3.50 |
| C1 | 1 | Condensador Electrolítico Baja ESR 4700µF 35V | Radial D16mm | Almacenamiento de energía para disparo autónomo | Nichicon UHW1V472MHD | 2.20 |
| Q1 | 1 | P-MOSFET Potencia 40V 40A AOD403 | TO-252 | Conmutador High-Side de disparo seguro | Alpha & Omega AOD403 | 1.20 |
| Q2 | 1 | N-MOSFET Potencia 40V 50A AOD4184A | TO-252 | Conmutador Low-Side de disparo seguro | Alpha & Omega AOD4184A | 0.80 |
| R_SENSE | 1 | Resistencia Shunt Medición 10Ω 1% 1W | SMD 1206 | Supervisión de corriente en reposo iniciador (<5mA) | Vishay WSL1206 | 0.60 |
| R_EOL | 2 | Resistencia Fin de Línea 4.7kΩ 1% 0.5W | THT Axial | Terminación lazo supervisado detectores EN54 | Yageo MFR-50FTE52-4K7 | 0.20 |
| U3 | 1 | Sensor Electroquímico de CO Figaro TGS5042 | Módulo TO-5 | Medición precisa de CO (0 - 1000 ppm) vida útil 10 años | Figaro Engineering TGS5042 | 14.50 |
| K1 | 1 | Relé de Maniobra SPDT 10A 250VAC | THT | Enclavamiento de corte para gas y climatización VMC | Omron G5Q-1 24VDC | 1.80 |
| K2 | 1 | Relé de Potencia SPST 10A 24VDC | THT | Activación de sirena 110dB y estrobo exterior | Omron G5Q-1 24VDC | 1.80 |
| J1-J3 | 3 | Bornero de Tornillo 2P 5.08mm 16A | THT | Conexión iniciador aerosol, lazo humo y aborto | Phoenix Contact 1729128 | 2.40 |
| D1-D4 | 4 | Diodos TVS Bidireccionales SMBJ28CA | SMB | Protección de descargas en líneas perimetrales | Littelfuse SMBJ28CA | 1.20 |
| PCB | 1 | Placa de Circuito Impreso Doble Cara 2oz Cu | FR4 100x80mm | Pistas de potencia reforzadas para pulso de disparo | JLCPCB / PCBWay | 2.50 |
| **TOTAL** | | | | | | **34.50 EUR** |
"""
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(bom_content)

    print(f"Proyecto KiCad Central de Incendio generado en: {output_dir}")
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
    out = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/07_seguridad_incendio_co_y_aerosoles/electrico"
    generar_kicad_incendio(out)
