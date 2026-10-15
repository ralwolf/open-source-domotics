#!/usr/bin/env python3
"""
Generador de Proyecto y Esquema Electrónico KiCad 10.0
Proyecto: Contador IoT de Descargas Atmosféricas y Telemetría de Protectores DPS
Módulo: 01_energia_renovable_y_potencia/08_pararrayos_y_proteccion_descargas/electrico
"""

import os
import uuid
import subprocess

def generar_kicad_pararrayos(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    pro_path = os.path.join(output_dir, "contador_rayos_iot.kicad_pro")
    sch_path = os.path.join(output_dir, "contador_rayos_iot.kicad_sch")
    bom_path = os.path.join(output_dir, "BOM.md")

    root_uuid = str(uuid.uuid4())

    # 1. KICAD PROJECT (.kicad_pro)
    pro_content = f"""{{
  "boards": [],
  "meta": {{
    "filename": "contador_rayos_iot.kicad_pro",
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
        "diff_pair_gap": 0.4,
        "diff_pair_width": 0.5,
        "name": "HV_Impulse",
        "track_width": 0.8,
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
    (title "CONTADOR IOT DE DESCARGAS ATMOSFÉRICAS Y TELEMETRÍA DPS")
    (date "2026-10-15")
    (rev "v1.0")
    (company "open-source-domotics (Hardware Libre)")
    (comment 1 "Bobina Rogowski / Transformador de corriente de pulso + Comparador ultra-rápido")
    (comment 2 "Monitoreo de estado de cartuchos de sobretensión Tipo 1 y 2 en cuadro TGBT")
  )

  (wire (pts (xy 40.0 50.0) (xy 75.0 50.0))
    (stroke (width 0) (type default))
    (uuid "{u()}")
  )
  (text "ALIMENTACION_BATERIA_18650"
    (at 40.0 48.0 0)
    (effects (font (size 1.5 1.5)))
    (uuid "{u()}")
  )

  (symbol
    (lib_id "Battery_Management:TP4056")
    (at 85.0 65.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U2" (at 85.0 52.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "TP4056 (Cargador Solar/USB Batería Li-Ion)" (at 85.0 78.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 85.0 65.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Regulator_Linear:AMS1117-3.3")
    (at 130.0 65.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U3" (at 130.0 52.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "AMS1117-3.3 (LDO 3.3V 1A)" (at 130.0 78.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:SOT-223-3_TabPin2" (at 130.0 65.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "RF_Module:ESP32-WROOM-32E")
    (at 200.0 110.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U1" (at 200.0 80.0 0) (effects (font (size 1.5 1.5))))
    (property "Value" "ESP32-WROOM-32E (16MB Flash)" (at 200.0 142.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "RF_Module:ESP32-WROOM-32E" (at 200.0 110.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Comparator:LM393")
    (at 85.0 140.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U4" (at 85.0 128.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LM393 (Discriminador Rápido Impulso >500A)" (at 85.0 152.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 85.0 140.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Isolator:PC817")
    (at 290.0 75.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "OK1" (at 290.0 62.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "PC817 (Supervisión Contacto DPS Clase 1)" (at 290.0 88.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 290.0 75.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Isolator:PC817")
    (at 290.0 125.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "OK2" (at 290.0 112.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "PC817 (Supervisión Contacto DPS Clase 2)" (at 290.0 138.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 290.0 125.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Connector:Screw_Terminal_01x04")
    (at 40.0 140.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J1" (at 40.0 118.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "ENTRADA BOBINA ROGOWSKI (SIG+, SIG-, GND, SHIELD)" (at 40.0 162.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-4_P5.08mm" (at 40.0 140.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Connector:Screw_Terminal_01x06")
    (at 360.0 100.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J2" (at 360.0 70.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BORNERO TELEMETRÍA DPS (DPS1_NO, DPS1_COM, DPS2_NO, DPS2_COM, ALARM, GND)" (at 360.0 130.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-6_P3.81mm" (at 360.0 100.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (sheet_instances
    (path "/" (page "1"))
  )
)
"""
    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(sch_content)

    # 3. LISTA DE MATERIALES (BOM.md)
    bom_content = """# Lista de Materiales (BOM) - Contador IoT de Rayos y Telemetría DPS

**Placa:** `contador_rayos_iot.kicad_sch`  
**Función:** Detección y conteo de descargas atmosféricas (>500A) y supervisión de protectores de sobretensión transitoria  
**Alimentación:** Micro-panel solar 5V + Batería Li-Ion 18650 (Autonomía continua en exteriores)  
**Proyecto:** open-source-domotics  

---

### 1. Semiconductores y Circuitos Integrados
| Referencia | Componente | Encapsulado | Función / Descripción | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-WROOM-32E | SMD-38 | Microcontrolador central Wi-Fi/BLE con contador de pulsos por hardware (PCNT) | 1 |
| **U2** | TP4056 | SOIC-8 | Controlador de carga de batería Li-Ion 1A con protección térmica | 1 |
| **U3** | AMS1117-3.3 | SOT-223 | Regulador lineal LDO 3.3V 1A de bajo ruido | 1 |
| **U4** | LM393 | SOIC-8 | Comparador de tensión analógico de alta velocidad para detección de picos de rayo | 1 |
| **OK1, OK2** | PC817 | DIP-4 | Optoacopladores para lectura aislada de contactos auxiliares de cartuchos DPS | 2 |
| **TVS1** | SMAJ36A | SMA | Diodo supresor de transitorios TVS para protección de entrada de bobina captadora | 1 |
| **D1, D2** | BAT54S | SOT-23 | Diodos Schottky duales para rectificación ultrarrápida del pulso inducido | 1 |

---

### 2. Componentes de Protección Atmosférica en Campo
- **1x Bobina Rogowski / Captador Toroidal:** Bobina toroidal de núcleo de aire o ferrita para abrazo de conductor Cu 50 mm² sin interrumpir la bajante.
- **1x Descargador Combinado Tipo 1+2 (TGBT):** Dehn DG M TNC 275 / Schneider iPRD1 12.5r con contacto auxiliar inversor de disparo.
- **1x Vía de Chispas Equipotencial (Spark Gap):** Dehn TFS / OBO Bettermann 100 kA (10/350 µs) para unión de malla pararrayos con tierra de servicio.
- **3x Picas de Acero Cobrizado:** $\phi 16\text{ mm} \times 2.0\text{ m}$ con abrazaderas de bronce y arqueta de registro de $30 \times 30\text{ cm}$.
"""
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(bom_content)

    print(f"Proyecto KiCad de Contador de Rayos generado en: {output_dir}")
    print(f"BOM generado en: {bom_path}")

    # 4. EXPORTAR A SVG CON KICAD-CLI
    svg_dir = os.path.join(output_dir, "esquema_svg")
    os.makedirs(svg_dir, exist_ok=True)
    cmd = [
        "flatpak-spawn", "--host", "flatpak", "run", "--command=kicad-cli",
        "org.kicad.KiCad", "sch", "export", "svg", sch_path, "-o", svg_dir
    ]
    try:
        subprocess.run(cmd, check=True)
        print(f"Esquema SVG de Contador de Rayos exportado mediante kicad-cli en: {svg_dir}")
    except Exception as e:
        print(f"Aviso al exportar con kicad-cli: {e}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_dir = os.path.join(base_dir, "01_energia_renovable_y_potencia/08_pararrayos_y_proteccion_descargas/electrico")
    generar_kicad_pararrayos(target_dir)
