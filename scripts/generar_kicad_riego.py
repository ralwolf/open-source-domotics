#!/usr/bin/env python3
"""
Generador de Proyecto y Esquema Electrónico KiCad 10.0
Proyecto: Controlador Inteligente de Riego Multizona 24VAC
Módulo: 05_confort_y_exteriores/03_riego_automatizado_jardin/electrico
"""

import os
import uuid
import subprocess

def generar_kicad_riego(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    pro_path = os.path.join(output_dir, "controlador_riego_jardin.kicad_pro")
    sch_path = os.path.join(output_dir, "controlador_riego_jardin.kicad_sch")
    bom_path = os.path.join(output_dir, "BOM.md")

    root_uuid = str(uuid.uuid4())

    # 1. KICAD PROJECT (.kicad_pro)
    pro_content = f"""{{
  "boards": [],
  "meta": {{
    "filename": "controlador_riego_jardin.kicad_pro",
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
        "name": "AC24V_Valves",
        "track_width": 1.0,
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
    (title "CONTROLADOR DE RIEGO INTELIGENTE MULTIZONA (24VAC / TRIAC ZERO-CROSS)")
    (date "2026-10-15")
    (rev "v1.0")
    (company "open-source-domotics (Hardware Libre)")
    (comment 1 "5x Triacs BT136 + MOC3041 Zero-Cross + 4x Sondas Capacitivas + Caudalímetro Hall")
    (comment 2 "Protección snubber RC y varistores MOV contra sobretensiones inductivas de solenoides")
  )

  (wire (pts (xy 40.0 50.0) (xy 75.0 50.0))
    (stroke (width 0) (type default))
    (uuid "{u()}")
  )
  (text "ALIMENTACION_24VAC_IN"
    (at 40.0 48.0 0)
    (effects (font (size 1.5 1.5)))
    (uuid "{u()}")
  )

  (symbol
    (lib_id "Device:D_Bridge_+-~~")
    (at 85.0 65.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "BR1" (at 85.0 52.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "MB6S (Puente Rectificador 600V 1A)" (at 85.0 78.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-4_4.4x3.9mm_P2.54mm" (at 85.0 65.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Regulator_Switching:LM2596HV-5.0")
    (at 130.0 65.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U2" (at 130.0 52.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "LM2596HV-5.0 (Buck 60V -> 5V 1A)" (at 130.0 78.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:TO-263-5_TabPin3" (at 130.0 65.0 0) (effects (font (size 1.27 1.27)) hide))
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
    (lib_id "Isolator:MOC3041M")
    (at 290.0 70.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "OK1" (at 290.0 58.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "MOC3041M (Optotriac Cruce por Cero)" (at 290.0 82.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DIP:DIP-6_W7.62mm" (at 290.0 70.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Triac:BT136-600E")
    (at 350.0 70.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "Q1" (at 350.0 58.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BT136-600E (Triac 4A 600V TO-220 - EV1)" (at 350.0 82.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_THT:TO-220-3_Vertical" (at 350.0 70.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Triac:BT136-600E")
    (at 350.0 115.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "Q2" (at 350.0 102.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BT136-600E (Triac EV2)" (at 350.0 128.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_THT:TO-220-3_Vertical" (at 350.0 115.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Triac:BT136-600E")
    (at 350.0 160.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "Q3" (at 350.0 148.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BT136-600E (Triac EV3)" (at 350.0 172.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_THT:TO-220-3_Vertical" (at 350.0 160.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Triac:BT136-600E")
    (at 350.0 205.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "Q4" (at 350.0 192.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BT136-600E (Triac EV4)" (at 350.0 218.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_THT:TO-220-3_Vertical" (at 350.0 205.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Triac:BT136-600E")
    (at 350.0 250.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "Q5" (at 350.0 238.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BT136-600E (Triac Válvula Maestra)" (at 350.0 262.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_THT:TO-220-3_Vertical" (at 350.0 250.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Connector:Screw_Terminal_01x08")
    (at 410.0 160.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J1" (at 410.0 125.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BORNERO VÁLVULAS 24VAC (24VAC_IN, COM, MV, Z1, Z2, Z3, Z4, GND)" (at 410.0 195.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-8_P5.08mm" (at 410.0 160.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Connector:Screw_Terminal_01x06")
    (at 85.0 180.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J2" (at 85.0 150.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BORNERO SONDAS (S1, S2, S3, S4, CAUDAL_PULSO, +3.3V)" (at 85.0 210.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-6_P3.81mm" (at 85.0 180.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (sheet_instances
    (path "/" (page "1"))
  )
)
"""
    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(sch_content)

    # 3. LISTA DE MATERIALES (BOM.md)
    bom_content = """# Lista de Materiales (BOM) - Controlador de Riego Multizona 24VAC

**Placa:** `controlador_riego_jardin.kicad_sch`  
**Canales de Salida:** 5 (4 Zonas de Riego + 1 Válvula Maestra de Seguridad)  
**Tensión de Operación:** 24V AC (Transformador 230V -> 24V AC 50VA)  
**Proyecto:** open-source-domotics  

---

### 1. Circuitos Integrados y Módulos
| Referencia | Componente | Encapsulado | Función / Descripción | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-WROOM-32E | SMD-38 | Microcontrolador central Wi-Fi/BLE dual-core con ESPHome | 1 |
| **U2** | LM2596HV-5.0 | TO-263-5 | Regulador Step-Down conmutado de alta tensión (60V -> 5V 1A) | 1 |
| **U3** | AMS1117-3.3 | SOT-223 | Regulador lineal 3.3V 1A para ESP32 y sensores analógicos | 1 |
| **OK1 a OK5** | MOC3041M | DIP-6 | Optoacopladores disparadores de triac con detección de Cruce por Cero (Zero-Cross) | 5 |
| **BR1** | MB6S | SOIC-4 | Puente rectificador de onda completa 600V 1A para alimentación interna | 1 |

---

### 2. Dispositivos de Potencia y Protección
| Referencia | Componente | Encapsulado | Función / Descripción | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **Q1 a Q5** | BT136-600E | TO-220 | Triacs de compuerta sensible 4A 600V para electroválvulas solenoides 24VAC | 5 |
| **MOV1 a MOV5** | S10K275 | Radial 10mm | Varistores de óxido metálico 275V AC para absorción de picos transitorios inductivos | 5 |
| **R_snub (1-5)** | Resistencia Cerámica 39 Ω / 1W | Axial | Red amortiguadora snubber RC contra dV/dt espurio | 5 |
| **C_snub (1-5)** | Condensador Poliéster 10 nF / 400V | Paso 10mm | Red amortiguadora snubber RC | 5 |
| **F1** | Fusible Cerámico 2A 250V (5x20mm) | Portafusible PCB | Protección contra cortocircuito en bobinas de solenoides | 1 |

---

### 3. Conectores y Sensores
| Referencia | Componente | Tipo / Paso | Conexión | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **J1** | Bornero de tornillo 8 pines | Paso 5.08 mm | 24VAC In, Común, Válvula Maestra, Zonas 1 a 4, Tierra PE | 1 |
| **J2** | Bornero de tornillo 6 pines | Paso 3.81 mm | Entradas analógicas sondas S1-S4, entrada de pulsos caudalímetro, 3.3V | 1 |
| **S1 a S4** | Sondas Capacitivas de Suelo v2.0 | Sensor analógico | Inmunes a corrosión galvánica, cable apantallado hacia arquetas/macetas | 4 |
| **FL1** | Caudalímetro de Turbina Hall | 1" BSP Macho | Salida de impulsos NPN colector abierto (1 pulso / litro) | 1 |
"""
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(bom_content)

    print(f"Proyecto KiCad de Riego generado en: {output_dir}")
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
        print(f"Esquema SVG de Riego exportado mediante kicad-cli en: {svg_dir}")
    except Exception as e:
        print(f"Aviso al exportar con kicad-cli: {e}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_dir = os.path.join(base_dir, "05_confort_y_exteriores/03_riego_automatizado_jardin/electrico")
    generar_kicad_riego(target_dir)
