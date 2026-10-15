#!/usr/bin/env python3
"""
Generador de Proyecto y Esquema Electrónico KiCad 10.0
Proyecto: Controlador Autónomo de Corte de Emergencia de Gas y Agua
Módulo: 03_seguridad_y_control_acceso/03_actuadores_valvulas_gas_agua/electrico
"""

import os
import uuid
import subprocess

def generar_kicad_valvulas(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    pro_path = os.path.join(output_dir, "controlador_valvulas_seguridad.kicad_pro")
    sch_path = os.path.join(output_dir, "controlador_valvulas_seguridad.kicad_sch")
    bom_path = os.path.join(output_dir, "BOM.md")

    root_uuid = str(uuid.uuid4())

    # 1. KICAD PROJECT (.kicad_pro)
    pro_content = f"""{{
  "boards": [],
  "meta": {{
    "filename": "controlador_valvulas_seguridad.kicad_pro",
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
        "clearance": 0.4,
        "diff_pair_gap": 0.3,
        "diff_pair_width": 0.4,
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
      "Root"
    ]
  ]
}}
"""
    with open(pro_path, "w", encoding="utf-8") as f:
        f.write(pro_content)

    # 2. KICAD SCHEMATIC (.kicad_sch)
    sch_content = f"""(kicad_sch
	(version 20250114)
	(generator "eeschema")
	(generator_version "10.0")
	(uuid "{root_uuid}")
	(paper "A3")
	(title_block
		(title "Emergency Gas & Water Shutoff Controller with Battery Backup")
		(date "2026-10-14")
		(rev "1.0")
		(company "Open Source Domotics")
		(comment 1 "Zero-Latency Hardware Interruption + Dual 12V 5A Actuator Drivers + 85dB Siren")
		(comment 2 "Hardware 100% Abierto y Reproducible en KiCad")
	)
	(lib_symbols)
	(text "SECCIÓN 1: ALIMENTACIÓN 12VDC CON RESPALDO DE BATERÍA DE LITIO (UPS MINI)"
		(at 30 25 0)
		(effects
			(font
				(size 2.5 2.5)
				(bold yes)
			)
			(justify left)
		)
		(uuid "{uuid.uuid4()}")
	)
	(text "J1: Entrada 12VDC 2A Jack o Bornera\\nU1: Cargador BMS y Step-Up 12V con celda Li-Ion 18650 3.7V 3000mAh (Garantiza cierre de válvulas en apagón)\\nU2: Regulador LDO AMS1117-3.3V (Alimentación MCU y sensores analógicos)\\nC1: 470uF 25V Low-ESR | C2, C3: 100nF Cerámico | D1: Diodo Schottky SS34"
		(at 30 35 0)
		(effects
			(font
				(size 1.8 1.8)
			)
			(justify left)
		)
		(uuid "{uuid.uuid4()}")
	)
	(text "SECCIÓN 2: MICROCONTROLADOR ESP32 Y CONECTIVIDAD"
		(at 160 25 0)
		(effects
			(font
				(size 2.5 2.5)
				(bold yes)
			)
			(justify left)
		)
		(uuid "{uuid.uuid4()}")
	)
	(text "U3: ESP32-WROOM-32E (4MB Flash)\\n- Pin IO14: Disparo Válvula de Gas (Corte instantáneo <1s)\\n- Pin IO12: Cierre Válvula de Agua (Motorizada DN25)\\n- Pin IO13: Activación Zumbador / Sirena 85 dB\\n- Pin IO34: Sensor Fuga Agua Cocina (Optoacoplado)\\n- Pin IO35: Sensor Fuga Agua Lavandería/Baños\\n- Pin IO32: Sensor Detector de Gas Metano/GLP (Entrada analógica/digital)\\n- Pin IO2: LED de Estado del Sistema (Verde: OK / Rojo: Fuga Detectada)"
		(at 160 35 0)
		(effects
			(font
				(size 1.8 1.8)
			)
			(justify left)
		)
		(uuid "{uuid.uuid4()}")
	)
	(text "SECCIÓN 3: ETAPA DE DISPARO DE ELECTROVÁLVULAS DE GAS Y AGUA"
		(at 30 115 0)
		(effects
			(font
				(size 2.5 2.5)
				(bold yes)
			)
			(justify left)
		)
		(uuid "{uuid.uuid4()}")
	)
	(text "OK1, OK2: Optoacopladores PC817 para aislamiento galvánico completo entre ESP32 y actuadores\\nQ1, Q2: MOSFETs de Potencia Logic-Level IRLZ44N (Vds 55V, Id 47A, Rds_on 0.022 Ohm)\\nD2, D3: Diodos Flyback de Protección 1N5408 en paralelo con las bobinas de las válvulas\\nJ2: Bornera 12V 2A para Electroválvula de Gas (Disparo biestable por pulso)\\nJ3: Bornera 12V 2A para Válvula Motorizada de Agua (DN25 1 pulgada con retorno por condensador)"
		(at 30 125 0)
		(effects
			(font
				(size 1.8 1.8)
			)
			(justify left)
		)
		(uuid "{uuid.uuid4()}")
	)
	(text "SECCIÓN 4: SENSORES DE INUNDACIÓN Y DETECCIÓN DE GAS"
		(at 160 115 0)
		(effects
			(font
				(size 2.5 2.5)
				(bold yes)
			)
			(justify left)
		)
		(uuid "{uuid.uuid4()}")
	)
	(text "J4: Entrada Cable Conductor Resistivo Sensor de Agua Cocina (Detección por conductividad)\\nJ5: Entrada Cable Conductor Sensor de Agua Lavandería y Cuarto Técnico\\nJ6: Conector para Módulo Sensor de Gas Metano / GLP (MQ-4 / Figaro TGS2611)\\n- Circuito comparador con histéresis (LM393) para evitar falsos positivos por humedad ambiental"
		(at 160 125 0)
		(effects
			(font
				(size 1.8 1.8)
			)
			(justify left)
		)
		(uuid "{uuid.uuid4()}")
	)
	(sheet_instances
		(path "/"
			(page "1")
		)
	)
)
"""
    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(sch_content)

    # 3. BOM.md
    bom_content = """# Lista de Materiales y Componentes (BOM)
## Proyecto: Controlador Autónomo de Corte de Emergencia de Gas y Agua
**Directorio:** `03_seguridad_y_control_acceso/03_actuadores_valvulas_gas_agua/electrico/`  
**Diseño:** KiCad 10.0 | Código de Proyecto: `ESP32-SHUTOFF-V1`

---

### 1. Circuitos Integrados y Módulos
| Referencia | Componente | Encapsulado | Función | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **U3** | ESP32-WROOM-32E | Módulo SMD | MCU Dual-Core 240MHz con WiFi + BLE para telemetría | 1 |
| **U1** | Módulo UPS 18650 12V | PCB Through-Hole | Cargador Li-Ion + Elevador Step-Up 12V continuo de respaldo | 1 |
| **U2** | AMS1117-3.3 | SOT-223 | Regulador lineal de bajo voltaje (12V/5V -> 3.3V 800mA) | 1 |
| **U4** | LM393 | DIP-8 / SOIC-8 | Comparador dual de voltaje para sondas resistivas de agua | 1 |
| **OK1, OK2** | PC817 | DIP-4 | Optoacopladores de aislamiento galvánico | 2 |

---

### 2. Etapa de Potencia y Disparo de Válvulas
| Referencia | Componente | Encapsulado | Descripción | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **Q1, Q2** | IRLZ44N | TO-220 | MOSFET canal N Logic-Level (55V 47A) para electroválvulas | 2 |
| **D2, D3** | 1N5408 | DO-201AD | Diodos de supresión de picos inductivos (Flyback 3A 1000V) | 2 |
| **BZ1** | Zumbador Piezoeléctrico | 12V DC | Sirena acústica continua de 85 dB a 1 metro | 1 |
| **F1** | Fusible Rearmable Polyswitch | PPTC 16V 3A | Protección contra sobrecorriente en actuadores | 1 |

---

### 3. Válvulas y Actuadores Vinculados
- **1x Electroválvula de Gas con Rearme Manual:** 12V DC, cuerpo de latón DN20 (3/4") o DN25 (1"), cierre por pulso en <1 segundo.
- **1x Válvula Motorizada de Agua:** 12V DC, cuerpo de latón DN25 (1"), cierre por condensador de retorno automático en <3 segundos.
- **3x Sensores de Inundación de Cable Conductivo:** 2 metros de cable sensor trenzado para zócalos de cocina, lavandería y colector de calefacción.
"""
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(bom_content)

    print(f"Proyecto KiCad de válvulas generado en: {output_dir}")
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
        print(f"Esquema SVG de válvulas exportado mediante kicad-cli en: {svg_dir}")
    except Exception as e:
        print(f"Aviso al exportar con kicad-cli: {e}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_dir = os.path.join(base_dir, "03_seguridad_y_control_acceso/03_actuadores_valvulas_gas_agua/electrico")
    generar_kicad_valvulas(target_dir)
