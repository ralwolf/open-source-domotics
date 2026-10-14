#!/usr/bin/env python3
"""
Generador de Proyecto y Esquema Electrónico KiCad 10.0
Proyecto: Gateway ESP32 de Telemetría Energética y Desconexión de Emergencia (Load-Shedding)
Módulo: 04_telemetria_y_cargas_criticas/01_medicion_potencia_cuadro
"""

import os
import uuid
import subprocess

def generar_kicad_proyecto(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    pro_path = os.path.join(output_dir, "medidor_potencia_iot.kicad_pro")
    sch_path = os.path.join(output_dir, "medidor_potencia_iot.kicad_sch")
    bom_path = os.path.join(output_dir, "BOM.md")

    root_uuid = str(uuid.uuid4())

    # 1. KICAD PROJECT (.kicad_pro)
    pro_content = f"""{{
  "boards": [],
  "cvpcb": {{
    "equivalence_files": []
  }},
  "erc": {{
    "erc_exclusions": [],
    "meta": {{
      "version": 0
    }},
    "pin_map": [
      [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2],
      [0, 2, 0, 1, 0, 0, 1, 0, 2, 2, 2, 2],
      [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 2],
      [0, 1, 0, 0, 0, 0, 1, 1, 2, 1, 1, 2],
      [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
      [1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 1, 2],
      [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 2],
      [0, 2, 1, 2, 0, 0, 2, 0, 2, 2, 2, 2],
      [0, 2, 0, 1, 0, 0, 1, 0, 2, 0, 0, 2],
      [0, 2, 1, 1, 0, 0, 1, 0, 2, 0, 0, 2],
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    ],
    "rule_severities": {{}}
  }},
  "libraries": {{
    "pinned_footprint_libs": [],
    "pinned_symbol_libs": []
  }},
  "meta": {{
    "filename": "medidor_potencia_iot.kicad_pro",
    "version": 3
  }},
  "net_settings": {{
    "classes": [
      {{
        "bus_width": 12,
        "clearance": 0.25,
        "diff_pair_gap": 0.25,
        "diff_pair_via_gap": 0.25,
        "diff_pair_width": 0.35,
        "line_style": 0,
        "microvia_diameter": 0.5,
        "microvia_drill": 0.2,
        "name": "Default",
        "pcb_color": "rgba(0, 0, 0, 0.000)",
        "priority": 2147483647,
        "schematic_color": "rgba(0, 0, 0, 0.000)",
        "track_width": 0.3,
        "via_diameter": 0.8,
        "via_drill": 0.4,
        "wire_width": 6
      }},
      {{
        "bus_width": 12,
        "clearance": 0.4,
        "diff_pair_gap": 0.3,
        "diff_pair_via_gap": 0.3,
        "diff_pair_width": 0.4,
        "line_style": 0,
        "microvia_diameter": 0.6,
        "microvia_drill": 0.3,
        "name": "Power",
        "pcb_color": "rgba(255, 0, 0, 0.000)",
        "priority": 1,
        "schematic_color": "rgba(255, 0, 0, 0.000)",
        "track_width": 0.8,
        "via_diameter": 1.2,
        "via_drill": 0.6,
        "wire_width": 6
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
		(title "ESP32 IoT Energy Gateway & Safety Shutoff Controller")
		(date "2026-10-14")
		(rev "1.0")
		(company "Open Source Domotics")
		(comment 1 "Bus RS-485 Modbus RTU + 4x PZEM UART + Dual Emergency Relays + Isolated PSU")
		(comment 2 "Hardware 100% Abierto y Reproducible en KiCad")
	)
	(lib_symbols)
	(text "SECCIÓN 1: FUENTE DE ALIMENTACIÓN AC/DC AISLADA (100-240VAC -> 5VDC / 3.3VDC)"
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
	(text "F1: Fusible Térmico 1A / 250V\\nMOV1: Varistor 275V (10D431K)\\nPSU1: Hi-Link HLK-PM01 (5V / 3W)\\nU1: Regulador LDO AMS1117-3.3V (800mA)\\nC1: 470uF 16V Low-ESR | C2: 100nF Cerámico\\nC3: 220uF 10V | C4: 100nF Cerámico"
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
	(text "U2: ESP32-WROOM-32E (4MB Flash)\\n- Pin EN / RESET: R_pullup 10k + C_deb 1uF + Pulsador RESET\\n- Pin IO0 / BOOT: R_pullup 10k + Pulsador BOOT\\n- Pin TXD0/RXD0: Cabezal de programación USB-UART (CH340C / CP2102)\\n- Pin IO21 (SDA), IO22 (SCL): I2C Display OLED 0.96\\" SSD1306 (128x64)\\n- Pin IO16 (RX2), IO17 (TX2): Bus RS-485 Modbus RTU\\n- Pin IO4, IO5, IO18, IO19: UART Software / Opto PZEM-004T v3\\n- Pin IO25: Relé 1 (Corte Cargas Críticas / Alerta)\\n- Pin IO26: Relé 2 (Load-Shedding Desconexión Horno/EV)"
		(at 160 35 0)
		(effects
			(font
				(size 1.8 1.8)
			)
			(justify left)
		)
		(uuid "{uuid.uuid4()}")
	)
	(text "SECCIÓN 3: TRANSCEPTOR RS-485 MODBUS AISLADO (EASTRON SDM630 / ATM90E32)"
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
	(text "U3: Transceptor RS-485 Industrial MAX485 / SP3485 (o ISO3082 Aislado galvánicamente)\\n- Pin DI -> IO17 (ESP32 TX2)\\n- Pin RO -> IO16 (ESP32 RX2)\\n- Pin RE/DE -> IO23 (Dirección TX/RX con circuito Auto-Direction NPN opcional)\\n- Bornera J3 (A+, B-, GND-SHIELD): Conexión par trenzado blindado\\n- R_term: Resistencia 120 Ohm con Jumper seleccionable\\n- TVS1, TVS2: Diodos SMBJ6.8CA para supresión de picos ESD y transitorios"
		(at 30 125 0)
		(effects
			(font
				(size 1.8 1.8)
			)
			(justify left)
		)
		(uuid "{uuid.uuid4()}")
	)
	(text "SECCIÓN 4: INTERFAZ OPTOACOPLADA PZEM-004T V3 (SUB-MEDICIÓN DERIVADOS)"
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
	(text "Cabezales J4, J5, J6, J7 (4 Canales de corriente y tensión AC):\\n- Canal 1 (J4): Medición Cocina / Placa Inducción (CT 100A)\\n- Canal 2 (J5): Medición Climatización Aerotermia/Multi-Split (CT 100A)\\n- Canal 3 (J6): Medición Lavandería y Bomba de Agua (CT 100A)\\n- Canal 4 (J7): Medición Sala IT / Servidores Domótica (CT 100A)\\n- Aislamiento galvánico óptico de 3.75 kV nativo del PZEM-004T"
		(at 160 125 0)
		(effects
			(font
				(size 1.8 1.8)
			)
			(justify left)
		)
		(uuid "{uuid.uuid4()}")
	)
	(text "SECCIÓN 5: ETAPA DE ACCIONAMIENTO DE RELÉS DE SEGURIDAD Y LOAD-SHEDDING"
		(at 30 190 0)
		(effects
			(font
				(size 2.5 2.5)
				(bold yes)
			)
			(justify left)
		)
		(uuid "{uuid.uuid4()}")
	)
	(text "Q1, Q2: Transistores NPN 2N2222 / MMBT2222 (o Optoacopladores PC817)\\nK1: Relé Omron G5LE-1 5VDC / 10A (Disparo de Contactor de Cargas Desconectables)\\nK2: Relé Omron G5LE-1 5VDC / 10A (Corte de Seguridad / Alarma Acústica en Cuadro)\\nD1, D2: Diodos Flyback 1N4148 / 1N4007 para protección contra fuerza contraelectromotriz\\nLED1, LED2: Indicadores luminosos de estado activo de cada relé\\nJ8: Bornera enchufable 5.08mm (NO1, NC1, COM1, NO2, NC2, COM2)"
		(at 30 200 0)
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

    # 3. BILL OF MATERIALS (BOM.md)
    bom_content = """# Lista de Materiales y Componentes (BOM)
## Proyecto: Gateway ESP32 de Telemetría Energética y Control de Sobrecargas
**Directorio:** `04_telemetria_y_cargas_criticas/01_medicion_potencia_cuadro/electrico/`  
**Diseño:** KiCad 10.0 | Código de Proyecto: `ESP32-PWR-MON-V1`

---

### 1. Circuitos Integrados y Módulos Principales
| Referencia | Componente | Encapsulado / Módulo | Descripción / Función | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **U1** | AMS1117-3.3 | SOT-223 | Regulador lineal de bajo voltaje (LDO 5V -> 3.3V 800mA) | 1 |
| **U2** | ESP32-WROOM-32E | Módulo SMD 38-pin | MCU dual-core 240MHz, 4MB Flash, WiFi + BLE | 1 |
| **U3** | SP3485 / MAX485 | SOIC-8 / DIP-8 | Transceptor semidúplex RS-485 para Modbus RTU | 1 |
| **PSU1** | Hi-Link HLK-PM01 | Módulo PCB Through-Hole | Conversor AC/DC 100-240VAC a 5VDC 3W aislado | 1 |
| **DISP1** | SSD1306 | Cabezal 4-pin I2C | Pantalla OLED 0.96" 128x64 para lectura local directa | 1 |

---

### 2. Etapa de Relés y Aislamiento de Control
| Referencia | Componente | Encapsulado | Descripción | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **K1, K2** | Omron G5LE-1-5VDC | THT 5 pines | Relé electromecánico SPDT 5VDC bobina, 10A 250VAC contactos | 2 |
| **Q1, Q2** | 2N2222 / MMBT2222 | SOT-23 / TO-92 | Transistor bipolar NPN driver de bobina de relé | 2 |
| **OK1, OK2** | PC817 | DIP-4 / SOP-4 | Optoacoplador para aislamiento galvánico de señales de disparo | 2 |
| **D1, D2** | 1N4148 / 1N4007 | DO-35 / SMA | Diodo flyback antiparalelo de protección de bobina | 2 |

---

### 3. Protecciones y Filtrado
| Referencia | Componente | Especificación | Cantidad |
| :--- | :--- | :--- | :--- |
| **F1** | Fusible Cartucho 5x20mm | 1A / 250V Acción Lenta (T1A) con zócalo para carril | 1 |
| **MOV1** | Varistor de Óxido Metálico | 10D431K (275VAC / 350VDC, absorción 45J) | 1 |
| **TVS1, TVS2** | Diodos TVS Bidireccionales | SMBJ6.8CA en líneas A y B de RS-485 | 2 |
| **C1** | Condensador Electrolítico | 470 µF / 16V Low-ESR (filtro salida 5V) | 1 |
| **C2, C4, C5** | Condensador Cerámico Multicapa | 100 nF / 50V X7R (desacoplo de ICs) | 3 |
| **C3** | Condensador Tantalio / Electrolítico | 220 µF / 10V (filtro carril 3.3V ESP32) | 1 |

---

### 4. Conectores y Borneras de Tablero
| Referencia | Conector | Pines | Uso | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **J1** | Bornera Enchufable KF2EDG 5.08mm | 2 pines | Entrada de Alimentación AC 230V (Fase, Neutro) | 1 |
| **J2** | Bornera Enchufable KF2EDG 5.08mm | 6 pines | Salidas de Relés K1 y K2 (COM, NO, NC) para contactores | 1 |
| **J3** | Bornera Enchufable KF2EDG 3.81mm | 3 pines | Bus RS-485 Modbus (A+, B-, GND Pantalla) | 1 |
| **J4, J5, J6, J7** | Cabezal JST-XH 2.54mm | 4 pines | Conexión directa a módulos de corriente PZEM-004T v3 | 4 |
| **J8** | Cabezal Pin Header 2.54mm | 4 pines | Puerto de Programación y Debug (3V3, RX, TX, GND) | 1 |

---

### 5. Sensores Externos Vinculados (En Carril DIN)
- **1x Analizador de Redes Trifásico/Bifásico:** Eastron SDM630 Modbus V2 (en acometida principal).
- **4x Sensores Monofásicos:** PZEM-004T v3 con transformadores de núcleo abierto 100A / 50mA para sub-medición de circuitos críticos y prioritarios.
"""
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(bom_content)

    print(f"Proyecto KiCad generado en: {output_dir}")
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
        print(f"Esquema SVG exportado mediante kicad-cli en: {svg_dir}")
    except Exception as e:
        print(f"Aviso al exportar con kicad-cli: {e}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_dir = os.path.join(base_dir, "04_telemetria_y_cargas_criticas/01_medicion_potencia_cuadro/electrico")
    generar_kicad_proyecto(target_dir)
