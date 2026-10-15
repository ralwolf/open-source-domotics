#!/usr/bin/env python3
"""
Generador de Proyecto y Esquema Electrónico KiCad 10.0
Proyecto: Controlador Inteligente de Biogás y Arranque de Generador Dual (ATS)
Módulo: 01_energia_renovable_y_potencia/05_biodigestor_biogas_generador/electrico
"""

import os
import uuid
import subprocess

def generar_kicad_biogas(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    pro_path = os.path.join(output_dir, "controlador_biogas_generador.kicad_pro")
    sch_path = os.path.join(output_dir, "controlador_biogas_generador.kicad_sch")
    bom_path = os.path.join(output_dir, "BOM.md")

    root_uuid = str(uuid.uuid4())

    # 1. KICAD PROJECT (.kicad_pro)
    pro_content = f"""{{
  "boards": [],
  "meta": {{
    "filename": "controlador_biogas_generador.kicad_pro",
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
        "name": "Power_12V",
        "track_width": 0.8,
        "via_diameter": 1.2,
        "via_drill": 0.6
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
    (title "CONTROLADOR INTELIGENTE DE BIOGÁS Y ARRANQUE AUTOMÁTICO GENERADOR DUAL (ATS)")
    (date "2026-10-15")
    (rev "v1.0")
    (company "open-source-domotics (Hardware Libre)")
    (comment 1 "Telemetría Presión 0-50mbar + Sensor CH4/H2S + Secuencia Start/Choke/Run + Válvula ATEX")
    (comment 2 "Arranque autónomo por baja tensión de baterías LiFePO4 o contingencia de red")
  )

  (wire (pts (xy 40.0 50.0) (xy 75.0 50.0))
    (stroke (width 0) (type default))
    (uuid "{u()}")
  )
  (text "ALIMENTACION_12VDC_BAT"
    (at 40.0 48.0 0)
    (effects (font (size 1.5 1.5)))
    (uuid "{u()}")
  )

  (symbol
    (lib_id "Regulator_Linear:AMS1117-3.3")
    (at 85.0 65.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U2" (at 85.0 52.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "AMS1117-3.3 (12V -> 3.3V 1A)" (at 85.0 78.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_SMD:SOT-223-3_TabPin2" (at 85.0 65.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "RF_Module:ESP32-WROOM-32E")
    (at 180.0 110.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U1" (at 180.0 80.0 0) (effects (font (size 1.5 1.5))))
    (property "Value" "ESP32-WROOM-32E (16MB Flash)" (at 180.0 142.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "RF_Module:ESP32-WROOM-32E" (at 180.0 110.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Sensor_Gas:MQ-4")
    (at 85.0 130.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "S1" (at 85.0 118.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "MQ-4 (Detector Metano CH4)" (at 85.0 142.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Sensor:MQ-4" (at 85.0 130.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Sensor_Current:ZMPT101B")
    (at 85.0 180.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "T1" (at 85.0 168.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "ZMPT101B (Transformador Tensión AC 230V)" (at 85.0 192.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Transformer_THT:Transformer_ZMPT101B" (at 85.0 180.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Relay:G5LE-1")
    (at 280.0 65.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "K1" (at 280.0 52.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Relé 1: Ignición / Run Generador" (at 280.0 78.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Relay_THT:Relay_SPDT_Omron-G5LE-1" (at 280.0 65.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Relay:G5LE-1")
    (at 280.0 110.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "K2" (at 280.0 98.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Relé 2: Solenoide Starter Motor (Pulso 4s)" (at 280.0 122.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Relay_THT:Relay_SPDT_Omron-G5LE-1" (at 280.0 110.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Relay:G5LE-1")
    (at 280.0 155.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "K3" (at 280.0 142.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Relé 3: Choke Cebador Motorizado" (at 280.0 168.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Relay_THT:Relay_SPDT_Omron-G5LE-1" (at 280.0 155.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Relay:G5LE-1")
    (at 280.0 200.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "K4" (at 280.0 188.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Relé 4: Válvula de Corte Biogás ATEX 12V" (at 280.0 212.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Relay_THT:Relay_SPDT_Omron-G5LE-1" (at 280.0 200.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Connector:Screw_Terminal_01x08")
    (at 350.0 130.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J1" (at 350.0 100.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BORNERO GENERADOR (IGN+, IGN-, START, CHOKE, GAS_EV+, GAS_EV-, ATS_CMD, GND)" (at 350.0 160.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-8_P5.08mm" (at 350.0 130.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (sheet_instances
    (path "/" (page "1"))
  )
)
"""
    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(sch_content)

    # 3. LISTA DE MATERIALES (BOM.md)
    bom_content = """# Lista de Materiales (BOM) - Controlador de Biogás y Generador Dual (ATS)

**Placa:** `controlador_biogas_generador.kicad_sch`  
**Potencia Generador Soportada:** 5 kW (Motor 4T 389cc gasolina/biogás)  
**Tensión de Operación:** 12V DC (Batería de arranque del grupo con cargador flotante)  
**Proyecto:** open-source-domotics  

---

### 1. Circuitos Integrados y Módulos
| Referencia | Componente | Encapsulado | Función / Descripción | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-WROOM-32E | SMD-38 | Microcontrolador central Wi-Fi/BLE con ESPHome | 1 |
| **U2** | AMS1117-3.3 | SOT-223 | Regulador lineal 3.3V 1A para ESP32 | 1 |
| **S1** | MQ-4 | Módulo Sensor | Sensor catalítico/semiconductor de gas Metano (CH4) | 1 |
| **T1** | ZMPT101B | Módulo PCB | Transformador de tensión de precisión para verificación 230VAC generador | 1 |
| **K1 a K4** | Omron G5LE-1 12VDC | THT | Relés SPDT 10A (Ignición, Arranque motor, Choke y Válvula ATEX) | 4 |
| **Q1 a Q4** | 2N7002 / IRLML2502 | SOT-23 | Transistores MOSFET canal N para excitación de bobinas de relé | 4 |
| **D1 a D4** | 1N4007 | DO-41 | Diodos de rueda libre flyback de supresión inductiva | 4 |

---

### 2. Equipamiento de Campo e Instalación de Biogás
- **1x Transmisor de Presión Piezorresistivo:** 0 a 50 mbar con salida analógica 4-20mA / 0.5-4.5V y conexión 1/4" NPT inox.
- **1x Electroválvula de Biogás Certificada ATEX (Zona 1/2):** 12V DC normalmente cerrada (NC), cuerpo de latón/aluminio DN20 (3/4").
- **1x Arrestador de Llama (Parallamas):** Malla de acero inoxidable AISI 316 certificada EN ISO 16852.
- **1x Actuador Lineal 12V para Choke:** Solenoide/servomotor para cierre y apertura gradual del cebador de aire en arranque frío.
- **1x Conmutador ATS (Automatic Transfer Switch):** 63A 2P conmutación mecánica motorizada con interbloqueo eléctrico.
"""
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(bom_content)

    print(f"Proyecto KiCad de Biogás generado en: {output_dir}")
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
        print(f"Esquema SVG de Biogás exportado mediante kicad-cli en: {svg_dir}")
    except Exception as e:
        print(f"Aviso al exportar con kicad-cli: {e}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_dir = os.path.join(base_dir, "01_energia_renovable_y_potencia/05_biodigestor_biogas_generador/electrico")
    generar_kicad_biogas(target_dir)

