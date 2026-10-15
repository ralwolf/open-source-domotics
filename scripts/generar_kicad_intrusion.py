#!/usr/bin/env python3
"""
Generador de Proyecto y Esquema Electrónico KiCad 10.0
Proyecto: Central de Alarma de Intrusión Perimetral con Supervisión DEOL y Driver de Sirena 120dB
Módulo: 03_seguridad_y_control_acceso/08_intrusion_perimetral_sensores_y_sirena/electrico
"""

import os
import uuid
import subprocess

def generar_kicad_intrusion(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    pro_path = os.path.join(output_dir, "central_alarma_intrusion_perimetral.kicad_pro")
    sch_path = os.path.join(output_dir, "central_alarma_intrusion_perimetral.kicad_sch")
    bom_path = os.path.join(output_dir, "BOM.md")

    root_uuid = str(uuid.uuid4())

    # 1. KICAD PROJECT (.kicad_pro)
    pro_content = f"""{{
  "boards": [],
  "meta": {{
    "filename": "central_alarma_intrusion_perimetral.kicad_pro",
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
        "clearance": 0.5,
        "diff_pair_gap": 0.3,
        "diff_pair_width": 0.5,
        "name": "Power_Siren_12V",
        "track_width": 1.2,
        "via_diameter": 1.5,
        "via_drill": 0.8
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
    (title "CENTRAL DE INTRUSION PERIMETRAL DEOL Y DRIVER SIRENA 120dB")
    (date "2026-10-15")
    (rev "v1.0")
    (company "open-source-domotics (Hardware Libre)")
    (comment 1 "4 Zonas Balanceadas DEOL 2x 2.2kΩ (Alarma + Tamper + Corte)")
    (comment 2 "Driver MOSFET Sirena 120dB + Flash Strobe con Respaldo Batería 12V")
  )

  (wire (pts (xy 30.0 50.0) (xy 70.0 50.0))
    (stroke (width 0) (type default))
    (uuid "{u()}")
  )
  (text "ALIMENTACION_12VDC_BATERIA"
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
    (property "Value" "MP1584_12V_to_3V3" (at 80.0 53.0 0) (effects (font (size 1.27 1.27))))
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
    (lib_id "Transistor_FET:AOD4184A")
    (at 240.0 60.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "Q1" (at 240.0 48.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "AOD4184A_SIRENA_120dB" (at 240.0 51.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:TO-252-2" (at 240.0 60.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Transistor_FET:AOD4184A")
    (at 240.0 95.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "Q2" (at 240.0 82.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "AOD4184A_FLASH_STROBE" (at 240.0 85.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:TO-252-2" (at 240.0 95.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x02")
    (at 300.0 60.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J1" (at 300.0 50.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BORNA_SIRENA_EXTERIOR_12V" (at 300.0 53.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" (at 300.0 60.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x02")
    (at 300.0 95.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J2" (at 300.0 85.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BORNA_FLASH_STROBE_12V" (at 300.0 88.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" (at 300.0 95.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x02")
    (at 80.0 100.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J3" (at 80.0 90.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "ZONA_1_BARRERAS_AIR_DEOL" (at 80.0 93.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" (at 80.0 100.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x02")
    (at 80.0 125.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J4" (at 80.0 115.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "ZONA_2_PUERTAS_REED_DEOL" (at 80.0 118.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" (at 80.0 125.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x02")
    (at 80.0 150.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J5" (at 80.0 140.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "ZONA_3_VENTANAS_REED_DEOL" (at 80.0 143.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" (at 80.0 150.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x02")
    (at 80.0 175.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J6" (at 80.0 165.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "ZONA_4_ROTURA_CRISTAL_DEOL" (at 80.0 168.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" (at 80.0 175.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (sheet_instances
    (path "/" (page "1"))
  )
)
"""
    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(sch_content)

    # 3. LISTA DE MATERIALES (BOM.md)
    bom_content = """# Lista de Materiales (BOM) - Central de Intrusión Perimetral DEOL

| Ref | Cantidad | Descripción | Encapsulado | Función Técnica | Proveedor / P/N | Coste Est. (EUR) |
|---|---|---|---|---|---|---|
| U1 | 1 | Regulador Buck Step-Down MP1584 | Módulo SMD | 12V a 3.3V / 1.5A para lógica ESP32 | Monolithic Power MP1584EN | 1.80 |
| U2 | 1 | Microcontrolador ESP32-WROOM-32E 8MB | SMD Module | Lógica de zonas supervisadas DEOL, ESPHome | Espressif ESP32-WROOM-32E | 3.50 |
| Q1-Q2 | 2 | MOSFET Potencia Canal N AOD4184A (40V, 50A, 8.5mΩ) | TO-252 | Driver Sirena 12V 2A y Flash Strobe | Alpha & Omega AOD4184A | 1.40 |
| F1 | 1 | Fusible Rearmable Polyswitch PTC 2.5A 30V | Radial | Protección de sobrecorriente para sirena | Littelfuse RUEF250 | 0.65 |
| R_DEOL | 8 | Resistencia Película Metálica 2.2kΩ 1% 0.25W | SMD 0805 | Resistencias balanceo Doble Fin de Línea | Yageo RC0805FR-072K2L | 0.25 |
| TVS1-4 | 4 | Supresores TVS Bidireccionales SMBJ15CA | SMB | Protección contra descargas ESD en cableado exterior | Littelfuse SMBJ15CA | 1.20 |
| J1-J6 | 6 | Bornero de Tornillo 2P 5.08mm 16A | THT | Conexión zonas DEOL, sirena y flash | Phoenix Contact 1729128 | 4.80 |
| C1-C6 | 6 | Condensadores Cerámicos 100nF y 10µF 50V | SMD 0805 | Filtro pasabajos anti-rebotes y RF en zonas | Murata GRM21 | 0.50 |
| PCB | 1 | Placa de Circuito Impreso Doble Cara 2oz Cu | FR4 100x80mm | Pistas masa en estrella de bajo ruido | JLCPCB / PCBWay | 2.50 |
| **TOTAL** | | | | | | **16.60 EUR** |
"""
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(bom_content)

    print(f"Proyecto KiCad Central de Intrusión generado en: {output_dir}")
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
    out = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/08_intrusion_perimetral_sensores_y_sirena/electrico"
    generar_kicad_intrusion(out)

