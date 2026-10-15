#!/usr/bin/env python3
"""
Generador de Proyecto y Esquema Electrónico KiCad 10.0
Proyecto: Controlador de Persianas y Cortinas con Interbloqueo Físico y Medición de Corriente
Módulo: 03_seguridad_y_control_acceso/04_cortinas_y_persianas_motorizadas/electrico
"""

import os
import uuid
import subprocess

def generar_kicad_persianas(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    pro_path = os.path.join(output_dir, "controlador_persianas_motorizadas.kicad_pro")
    sch_path = os.path.join(output_dir, "controlador_persianas_motorizadas.kicad_sch")
    bom_path = os.path.join(output_dir, "BOM.md")

    root_uuid = str(uuid.uuid4())

    # 1. KICAD PROJECT (.kicad_pro)
    pro_content = f"""{{
  "boards": [],
  "meta": {{
    "filename": "controlador_persianas_motorizadas.kicad_pro",
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
        "clearance": 1.2,
        "diff_pair_gap": 0.3,
        "diff_pair_width": 0.5,
        "name": "Mains_230VAC_Manoeuvre",
        "track_width": 1.8,
        "via_diameter": 2.2,
        "via_drill": 1.2
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
    (title "CONTROLADOR DE PERSIANAS CON INTERBLOQUEO POR HARDWARE")
    (date "2026-10-15")
    (rev "v1.0")
    (company "open-source-domotics (Hardware Libre)")
    (comment 1 "Interbloqueo SPDT Imposible de Cortocircuito + Snubber RC")
    (comment 2 "Entradas Pulsador de Pared Aisladas + Medición Corriente Anti-Atrapamiento")
  )

  (wire (pts (xy 30.0 50.0) (xy 70.0 50.0))
    (stroke (width 0) (type default))
    (uuid "{u()}")
  )
  (text "ALIMENTACION_230VAC"
    (at 30.0 48.0 0)
    (effects (font (size 1.5 1.5)))
    (uuid "{u()}")
  )

  (symbol
    (lib_id "Converter_ACDC:HLK-PM01")
    (at 80.0 65.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "PS1" (at 80.0 50.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "HLK-PM01_230VAC_to_5V" (at 80.0 53.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Converter_ACDC:Converter_ACDC_HiLink_HLK-PMxx" (at 80.0 65.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Regulator_Linear:AMS1117-3.3")
    (at 120.0 65.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U1" (at 120.0 52.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "AMS1117-3.3" (at 120.0 55.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:SOT-223-3_TabPin2" (at 120.0 65.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "RF_Module:ESP32-WROOM-32E")
    (at 180.0 75.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U2" (at 180.0 42.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "ESP32-WROOM-32E" (at 180.0 45.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "RF_Module:ESP32-WROOM-32E" (at 180.0 75.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Relay:Relay_SPST")
    (at 260.0 60.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "K1" (at 260.0 48.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "RELE_POWER_ON_OFF_10A" (at 260.0 51.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Relay_THT:Relay_SPDT_Omron-G5Q-1" (at 260.0 60.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Relay:Relay_SPDT")
    (at 260.0 95.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "K2" (at 260.0 82.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "RELE_INTERLOCK_SUBIR_BAJAR" (at 260.0 85.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Relay_THT:Relay_SPDT_Omron-G5Q-1" (at 260.0 95.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Sensor_Current:ACS712xLCTR-05B")
    (at 320.0 60.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U3" (at 320.0 48.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "ACS712_Medicion_Corriente_5A" (at 320.0 51.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 320.0 60.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Isolator:PC817")
    (at 120.0 120.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U4" (at 120.0 108.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "OPTO_PULSADOR_SUBIR" (at 120.0 111.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 120.0 120.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Isolator:PC817")
    (at 120.0 145.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U5" (at 120.0 133.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "OPTO_PULSADOR_BAJAR" (at 120.0 136.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 120.0 145.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x04")
    (at 380.0 80.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J1" (at 380.0 68.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BORNA_MOTOR_TUBULAR_4HILOS" (at 380.0 71.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-4_P5.08mm" (at 380.0 80.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (symbol
    (lib_id "Connector_Generic:Conn_01x03")
    (at 60.0 130.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J2" (at 60.0 118.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BORNA_PULSADOR_DOBLE_PARED" (at 60.0 121.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-3_P5.08mm" (at 60.0 130.0 0) (effects (font (size 1.27 1.27)) (hide yes)))
  )

  (sheet_instances
    (path "/" (page "1"))
  )
)
"""
    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(sch_content)

    # 3. LISTA DE MATERIALES (BOM.md)
    bom_content = """# Lista de Materiales (BOM) - Controlador Persianas con Interbloqueo Hardware

| Ref | Cantidad | Descripción | Encapsulado | Función Técnica | Proveedor / P/N | Coste Est. (EUR) |
|---|---|---|---|---|---|---|
| PS1 | 1 | Fuente AC/DC Conmutada 230VAC a 5VDC 3W HLK-PM01 | Módulo THT | Alimentación directa desde la red eléctrica | Hi-Link HLK-PM01 | 2.50 |
| U1 | 1 | Regulador Lineal LDO 3.3V 800mA AMS1117-3.3 | SOT-223 | Regulación 5V a 3.3V para ESP32 | Advanced Monolithic Systems | 0.35 |
| U2 | 1 | Microcontrolador SoC ESP32-WROOM-32E 8MB | SMD Module | Lógica de posición porcentual, ESPHome, Wi-Fi | Espressif ESP32-WROOM-32E | 3.50 |
| K1 | 1 | Relé de Potencia 10A 250VAC SPST Bobina 5V | THT | Corte y encendido general de energía motor | Omron G5Q-1 5VDC | 1.80 |
| K2 | 1 | Relé de Potencia 10A 250VAC SPDT Conmutado | THT | Conmutador de fase Subir / Bajar (Interlock) | Omron G5Q-1 5VDC | 1.80 |
| U3 | 1 | Sensor de Corriente Efecto Hall Aislado ACS712-05B | SOIC-8 | Detección de sobreesfuerzo y anti-atrapamiento | Allegro MicroSystems ACS712ELCTR-05B | 2.20 |
| U4-U5 | 2 | Optoacoplador Fototransistor Aislamiento 5kV PC817 | DIP-4 | Lectura de pulsadores mecánicos de pared 230V | Sharp PC817 | 0.60 |
| R_SNUB | 2 | Resistencia de Potencia 47Ω 2W Antiflama | THT Axial | Red amortiguadora RC snubber de contactos relé | Yageo FKN2WS | 0.50 |
| C_SNUB | 2 | Condensador Polipropileno X2 47nF 275VAC | THT Radial | Supresión de arco voltaico en desconexión motor | KEMET R46 | 0.80 |
| J1 | 1 | Bornero Tornillo 4P 5.08mm 16A | THT | Conexión cable motor (L_UP, L_DOWN, N, PE) | Phoenix Contact 1729144 | 1.40 |
| J2 | 1 | Bornero Tornillo 3P 5.08mm | THT | Conexión pulsador doble de pared (Subir/Bajar) | Phoenix Contact 1729131 | 1.10 |
| PCB | 1 | Placa de Circuito Impreso Doble Cara 2oz Cu | FR4 70x60mm | Pistas con aislamiento de 2.5 mm de fuga | JLCPCB / PCBWay | 2.00 |
| **TOTAL** | | | | | | **18.55 EUR** |
"""
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(bom_content)

    print(f"Proyecto KiCad Persianas generado en: {output_dir}")
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
    out = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/04_cortinas_y_persianas_motorizadas/electrico"
    generar_kicad_persianas(out)

