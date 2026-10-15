#!/usr/bin/env python3
"""
Generador de Proyecto y Esquema Electrónico KiCad 10.0
Proyecto: Controlador Inteligente de Cargador EV Wallbox 32A (IEC 61851-1 / SAE J1772)
Módulo: 01_energia_renovable_y_potencia/09_cargador_vehiculo_electrico_ev/electrico
"""

import os
import uuid
import subprocess

def generar_kicad_ev_wallbox(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    pro_path = os.path.join(output_dir, "controlador_ev_wallbox.kicad_pro")
    sch_path = os.path.join(output_dir, "controlador_ev_wallbox.kicad_sch")
    bom_path = os.path.join(output_dir, "BOM.md")

    root_uuid = str(uuid.uuid4())

    # 1. KICAD PROJECT (.kicad_pro)
    pro_content = f"""{{
  "boards": [],
  "meta": {{
    "filename": "controlador_ev_wallbox.kicad_pro",
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
        "diff_pair_width": 0.4,
        "name": "Pilot_Control",
        "track_width": 0.5,
        "via_diameter": 1.0,
        "via_drill": 0.5
      }},
      {{
        "clearance": 0.8,
        "diff_pair_gap": 0.4,
        "diff_pair_width": 0.6,
        "name": "Mains_Contactor",
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
    (title "CONTROLADOR INTELIGENTE EV WALLBOX 32A (IEC 61851-1 / SAE J1772)")
    (date "2026-10-15")
    (rev "v1.0")
    (company "open-source-domotics (Hardware Libre)")
    (comment 1 "CP PWM ±12V + PP Cable Sense + RCMB 6mA DC + Contactor 40A + Modbus RS-485")
    (comment 2 "Control dinámico de excedentes solares fotovoltaicos y eólicos (6A a 32A)")
  )

  (wire (pts (xy 40.0 50.0) (xy 75.0 50.0))
    (stroke (width 0) (type default))
    (uuid "{u()}")
  )
  (text "ALIMENTACION_230VAC_IN"
    (at 40.0 48.0 0)
    (effects (font (size 1.5 1.5)))
    (uuid "{u()}")
  )

  (symbol
    (lib_id "Power_Supply:HLK-PM12")
    (at 85.0 65.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "PS1" (at 85.0 52.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "HLK-PM12 (230VAC -> 12VDC 3W)" (at 85.0 78.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Converter_ACDC:Converter_ACDC_HiLink_HLK-PMxx" (at 85.0 65.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Regulator_Linear:AMS1117-3.3")
    (at 130.0 65.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U2" (at 130.0 52.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "AMS1117-3.3 (12V -> 3.3V 1A)" (at 130.0 78.0 0) (effects (font (size 1.27 1.27))))
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
    (lib_id "Amplifier_Operational:MCP6002")
    (at 85.0 140.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U3" (at 85.0 128.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "MCP6002 (Generador CP ±12V PWM 1kHz)" (at 85.0 152.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 85.0 140.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Converter_DCDC:B1212S-1WR3")
    (at 40.0 140.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "DC1" (at 40.0 128.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "B1212S (Rail Negativo -12V)" (at 40.0 152.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Converter_DCDC:Converter_DCDC_Mornsun_B_S-1WR3_Single" (at 40.0 140.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Relay:G5LE-1")
    (at 290.0 80.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "K1" (at 290.0 68.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Relé Bobina Contactor 40A (12VDC / 250VAC 10A)" (at 290.0 92.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Relay_THT:Relay_SPDT_Omron-G5LE-1" (at 290.0 80.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Driver_Motor:L9110S")
    (at 290.0 135.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U4" (at 290.0 122.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "L9110S (Driver Bloqueo Motor Tipo 2)" (at 290.0 148.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOP-8_3.9x4.9mm_P1.27mm" (at 290.0 135.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Interface_UART:ISO3082")
    (at 200.0 200.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U5" (at 200.0 188.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "ISO3082 (Transceptor RS-485 Aislado Galvánico)" (at 200.0 212.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm" (at 200.0 200.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Connector:Screw_Terminal_01x06")
    (at 360.0 110.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J1" (at 360.0 80.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BORNERO TIPO 2 (CP, PP, LOCK+, LOCK-, GND, PE)" (at 360.0 142.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-6_P5.08mm" (at 360.0 110.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Connector:Screw_Terminal_01x04")
    (at 360.0 200.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J2" (at 360.0 178.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BORNERO MODBUS RS-485 (A, B, GND_ISO, SHIELD)" (at 360.0 222.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-4_P5.08mm" (at 360.0 200.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (sheet_instances
    (path "/" (page "1"))
  )
)
"""
    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(sch_content)

    # 3. LISTA DE MATERIALES (BOM.md)
    bom_content = """# Lista de Materiales (BOM) - Controlador EV Wallbox 32A

**Placa:** `controlador_ev_wallbox.kicad_sch`  
**Norma de Carga:** IEC 61851-1 / SAE J1772 Modo 3 Caso B/C  
**Potencia Soportada:** 7.4 kW (Monofásico 32A) / 22 kW (Trifásico 32A)  
**Proyecto:** open-source-domotics  

---

### 1. Circuitos Integrados y Módulos Principales
| Referencia | Componente | Encapsulado | Función / Descripción | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-WROOM-32E | SMD-38 | Microcontrolador central Wi-Fi/BLE dual-core, máquina de estados IEC 61851 | 1 |
| **U2** | AMS1117-3.3 | SOT-223 | Regulador lineal de baja caída 3.3V 1A para MCU y lógica | 1 |
| **U3** | MCP6002-I/P | SOIC-8 | Amplificador operacional doble Rail-to-Rail para driver PWM ±12V CP | 1 |
| **U4** | L9110S | SOP-8 | Driver puente H de corriente continua (12V 1.5A) para solenoide de bloqueo | 1 |
| **U5** | ISO3082DW | SOIC-16W | Transceptor RS-485 aislado galvánicamente 2.5 kV para Medidor Modbus RTU | 1 |
| **PS1** | HLK-PM12 | Módulo PCB | Fuente ACDC conmutada 230VAC a 12VDC 3W clase II | 1 |
| **DC1** | B1212S-1WR3 | SIP-4 | Convertidor DC-DC aislado 12V a -12V 1W para nivel negativo del CP (-12V) | 1 |

---

### 2. Elementos de Conmutación y Protecciones
| Referencia | Componente | Encapsulado | Función / Descripción | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **K1** | Omron G5LE-1 12VDC | THT | Relé SPDT 10A 250VAC para excitación de bobina de contactor principal 40A | 1 |
| **OK1, OK2** | PC817 | DIP-4 | Optoacopladores para feedback de contacto auxiliar y trigger RCMB 6mA DC | 2 |
| **D1, D2** | 1N4148 / 1N4007 | SOD-123 / DO-41 | Diodo flyback de protección de bobinas y rectificación en lazo CP | 2 |
| **ZD1** | BZX84C3V3 | SOT-23 | Diodo Zener 3.3V de protección de entrada ADC frente a sobretensiones | 1 |
| **F1** | PPTC 16V 1.5A | SMD 1812 | Fusible rearmable de protección línea de 12V y solenoide | 1 |

---

### 3. Equipamiento Eléctrico de Potencia en Carril DIN
- **1x Contactor Bipolar 40A AC-1 (230VAC Bobina):** Schneider Acti9 iCT / Finder 22.32 con contacto auxiliar 1NO para supervisión de soldadura de contactos.
- **1x Disyuntor Magnetotérmico 2P C40A (10kA):** Protección exclusiva de sobrecorriente.
- **1x Interruptor Diferencial Tipo B / RDC-DD (IEC 62955):** Sensibilidad 30mA AC y disparo instantáneo a 6mA DC continuos lisos.
- **1x Medidor de Energía Modbus RS-485:** Eastron SDM120 / Finder 7M.24 (bidireccional, MID).
- **1x Base Receptáculo Tipo 2 (IEC 62196-2):** Hembra con pestillo motorizado 12V.
- **1x Seta de Parada de Emergencia:** Contacto NC cableado en serie directo a la bobina del contactor (seguridad intrínseca por hardware).
"""
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(bom_content)

    print(f"Proyecto KiCad de Wallbox EV generado en: {output_dir}")
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
        print(f"Esquema SVG de Wallbox EV exportado mediante kicad-cli en: {svg_dir}")
    except Exception as e:
        print(f"Aviso al exportar con kicad-cli: {e}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_dir = os.path.join(base_dir, "01_energia_renovable_y_potencia/09_cargador_vehiculo_electrico_ev/electrico")
    generar_kicad_ev_wallbox(target_dir)
