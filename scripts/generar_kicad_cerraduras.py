#!/usr/bin/env python3
"""
Generador de Proyecto y Esquema Electrónico KiCad 10.0
Proyecto: Controlador de Acceso Autónomo para Cerraduras Biométricas
Módulo: 03_seguridad_y_control_acceso/02_cerraduras_biometricas/electrico
"""

import os
import uuid
import subprocess

def generar_kicad_cerraduras(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    pro_path = os.path.join(output_dir, "controlador_acceso_cerraduras.kicad_pro")
    sch_path = os.path.join(output_dir, "controlador_acceso_cerraduras.kicad_sch")
    bom_path = os.path.join(output_dir, "BOM.md")

    root_uuid = str(uuid.uuid4())

    # 1. KICAD PROJECT (.kicad_pro)
    pro_content = f"""{{
  "boards": [],
  "meta": {{
    "filename": "controlador_acceso_cerraduras.kicad_pro",
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
        "name": "Power_Lock_12V",
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
    (title "CONTROLADOR DE ACCESO AUTÓNOMO Y CERRADURAS BIOMÉTRICAS")
    (date "2026-10-15")
    (rev "v1.0")
    (company "open-source-domotics (Hardware Libre)")
    (comment 1 "Sensor Huella Capacitivo R503 + Driver Fail-Safe / Fail-Secure 12V 3A")
    (comment 2 "Operación 100% autónoma offline con base de credenciales local en flash")
  )

  (wire (pts (xy 40.0 50.0) (xy 75.0 50.0))
    (stroke (width 0) (type default))
    (uuid "{u()}")
  )
  (text "ALIMENTACION_12VDC_UPS"
    (at 40.0 48.0 0)
    (effects (font (size 1.5 1.5)))
    (uuid "{u()}")
  )

  (symbol
    (lib_id "Regulator_Switching:MP1584")
    (at 85.0 65.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "U2" (at 85.0 52.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "MP1584 (Buck 12V -> 3.3V 2A)" (at 85.0 78.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" (at 85.0 65.0 0) (effects (font (size 1.27 1.27)) hide))
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
    (lib_id "Connector:Conn_01x06_Pin")
    (at 85.0 130.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J2" (at 85.0 118.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "CONECTOR SENSOR R503 (VCC, GND, TX, RX, WAKE, LED)" (at 85.0 142.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Connector_JST:JST_SH_SM06B-SRSS-TB_1x06-1MP_P1.00mm_Horizontal" (at 85.0 130.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Transistor_FET:IRLZ44N")
    (at 280.0 70.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "Q1" (at 280.0 58.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "IRLZ44N (MOSFET N 55V 47A - Driver Cerradura)" (at 280.0 82.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_TO_SOT_THT:TO-220-3_Vertical" (at 280.0 70.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Diode:1N5408")
    (at 280.0 100.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "D1" (at 280.0 92.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "1N5408 (Diodo Flyback 3A 1000V)" (at 280.0 108.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Diode_THT:D_DO-201AD_P15.24mm_Horizontal" (at 280.0 100.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Relay:G5LE-1")
    (at 280.0 145.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "K1" (at 280.0 132.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "Relé SPDT 10A (Selector Fail-Safe / Fail-Secure)" (at 280.0 158.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Relay_THT:Relay_SPDT_Omron-G5LE-1" (at 280.0 145.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Isolator:PC817")
    (at 85.0 185.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "OK1" (at 85.0 172.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "PC817 (Sensor Magnético Puerta + REX Interior)" (at 85.0 198.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "Package_DIP:DIP-4_W7.62mm" (at 85.0 185.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (symbol
    (lib_id "Connector:Screw_Terminal_01x08")
    (at 360.0 110.0 0)
    (unit 1)
    (uuid "{u()}")
    (property "Reference" "J1" (at 360.0 80.0 0) (effects (font (size 1.27 1.27))))
    (property "Value" "BORNERO CERRADURA (12V_IN, GND, LOCK_NO, LOCK_COM, LOCK_NC, DOOR_SENS, REX_BTN, TAMPER)" (at 360.0 142.0 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "TerminalBlock:TerminalBlock_bornier-8_P5.08mm" (at 360.0 110.0 0) (effects (font (size 1.27 1.27)) hide))
  )

  (sheet_instances
    (path "/" (page "1"))
  )
)
"""
    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(sch_content)

    # 3. LISTA DE MATERIALES (BOM.md)
    bom_content = """# Lista de Materiales (BOM) - Controlador de Acceso para Cerraduras Biométricas

**Placa:** `controlador_acceso_cerraduras.kicad_sch`  
**Alimentación:** 12V DC (Batería de respaldo 12V 7Ah con cargador flotante)  
**Carga Máxima de Salida:** 12V DC / 3A (Soporta cerradura electromagnética o cerradura motorizada de perno)  
**Proyecto:** open-source-domotics  

---

### 1. Semiconductores y Circuitos Integrados
| Referencia | Componente | Encapsulado | Función / Descripción | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **U1** | ESP32-WROOM-32E | SMD-38 | Microcontrolador central Wi-Fi/BLE con base de datos de huellas local | 1 |
| **U2** | MP1584EN | SOIC-8 | Convertidor reductor síncrono 12V a 3.3V 2A de alta eficiencia | 1 |
| **Q1** | IRLZ44N | TO-220 | MOSFET canal N Logic-Level (55V 47A) para disparo de cerradura | 1 |
| **D1** | 1N5408 | DO-201AD | Diodo rectificador 3A 1000V de supresión de picos flyback | 1 |
| **K1** | Omron G5LE-1 12VDC | THT | Relé SPDT 10A conmutador (Configuración Fail-Safe / Fail-Secure) | 1 |
| **OK1** | PC817 | DIP-4 | Optoacoplador para aislamiento de entrada de sensor de puerta y pulsador REX | 1 |
| **BZ1** | Zumbador 12V | THT | Buzzer piezoeléctrico continuo para aviso de apertura y alarma de sabotaje | 1 |

---

### 2. Dispositivos Periféricos Vinculados
- **1x Sensor de Huella Dactilar Capacitivo R503:** Resolución 508 DPI, sensor circular con anillo LED RGB bicolor, capacidad para 200 huellas, interfaz UART TTL.
- **1x Sensor Magnético de Puerta (Reed Switch):** Grado 2 de seguridad, contacto NC empotrado en marco de puerta para supervisión de puerta abierta.
- **1x Pulsador Interior de Salida (REX):** Tipo contacto seco capacitivo No-Touch (sensor infrarrojo de aproximación sin contacto físico).
- **1x Microswitch Tamper:** Contacto NC situado en el respaldo del panel para disparo de alarma si se intenta desprender de la pared.
"""
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(bom_content)

    print(f"Proyecto KiCad de Cerraduras generado en: {output_dir}")
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
        print(f"Esquema SVG de Cerraduras exportado mediante kicad-cli en: {svg_dir}")
    except Exception as e:
        print(f"Aviso al exportar con kicad-cli: {e}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_dir = os.path.join(base_dir, "03_seguridad_y_control_acceso/02_cerraduras_biometricas/electrico")
    generar_kicad_cerraduras(target_dir)

