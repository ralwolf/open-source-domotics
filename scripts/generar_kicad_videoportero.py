#!/usr/bin/env python3
"""
Generador de Proyecto y Esquema Electrónico KiCad 10.0
Proyecto: Videoportero Inteligente de Entrada ESP32-S3 con Audio Bidireccional I2S, Cerradura Eléctrica y PoE
Módulo: 03_seguridad_y_control_acceso/06_intercomunicacion_videoportero_y_multizona/electrico
"""

import os
import uuid
import subprocess

def generar_kicad_videoportero(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    pro_path = os.path.join(output_dir, "videoportero_esp32s3.kicad_pro")
    sch_path = os.path.join(output_dir, "videoportero_esp32s3.kicad_sch")
    bom_path = os.path.join(output_dir, "BOM.md")

    root_uuid = str(uuid.uuid4())

    # 1. KICAD PROJECT (.kicad_pro)
    pro_content = f"""{{
  "boards": [],
  "meta": {{
    "filename": "videoportero_esp32s3.kicad_pro",
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
        "name": "Power_12V_5V",
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
		(title "ESP32-S3 Smart Video Doorbell & Access Control")
		(date "2026-10-14")
		(rev "1.0")
		(company "Open Source Domotics")
		(comment 1 "Full-Duplex I2S Audio + DVP Camera + NFC PN532 + 12V 2A Lock Driver + PoE")
		(comment 2 "Hardware 100% Abierto y Reproducible en KiCad")
	)
	(lib_symbols)
	(text "SECCIÓN 1: ALIMENTACIÓN POE (IEEE 802.3af 48V -> 12V / 5V / 3.3V)"
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
	(text "J1: Conector RJ45 blindado con transformador PoE (MagJack 10/100)\\nU1: Módulo PoE Aislado Si3402-B / Silvertel Ag9905 (Entrada 36-57V -> Salida 5V 2A / 10W)\\nU2: Regulador LDO AMS1117-3.3V (Alimentación MCU y sensores analógicos)\\nU3: Step-Up Boost o Inyector 12V para bobina de cerradura de impacto\\nC1: 470uF 25V Low-ESR | C2, C3: 100nF Cerámicos | D1: Diodo Schottky SS34"
		(at 30 35 0)
		(effects
			(font
				(size 1.8 1.8)
			)
			(justify left)
		)
		(uuid "{uuid.uuid4()}")
	)
	(text "SECCIÓN 2: MICROCONTROLADOR ESP32-S3 Y CONECTIVIDAD"
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
	(text "U4: ESP32-S3-WROOM-1 (16MB Flash, 8MB Octal PSRAM)\\n- Bus DVP Cámara: Y2-Y9 (GPIO 11, 12, 13, 14, 21, 47, 48, 45), VSYNC, HREF, PCLK, XCLK (GPIO 15)\\n- Bus I2C SCCB Cámara & NFC: SDA (GPIO 4), SCL (GPIO 5)\\n- Audio I2S Micrófono: SCK (GPIO 41), WS (GPIO 42), SD_IN (GPIO 2)\\n- Audio I2S Altavoz: BCLK (GPIO 38), LRCLK (GPIO 39), DIN (GPIO 40)\\n- Botón Timbre: GPIO 0 (Entrada digital filtrada con antirrebote por hardware)\\n- Gatillo Cerradura: GPIO 1 (Salida hacia optoacoplador y MOSFET)\\n- LED Iluminación Botón: GPIO 6 (PWM para atenuación nocturna)\\n- Sensor PIR / Radar mmWave: GPIO 7 (Detección de presencia exterior a 3 metros)"
		(at 160 35 0)
		(effects
			(font
				(size 1.8 1.8)
			)
			(justify left)
		)
		(uuid "{uuid.uuid4()}")
	)
	(text "SECCIÓN 3: ETAPA DE AUDIO BIDIRECCIONAL I2S (FULL-DUPLEX CON CANCELACIÓN DE ECO)"
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
	(text "U5: Micrófono MEMS Digital I2S INMP441 / ICS-43434 (SNR 65 dBA, Sensibilidad -26 dBFS)\\n- Conectado directamente a bus I2S de grabación del ESP32-S3\\n\\nU6: Amplificador de Audio Digital I2S Clase D MAX98357A (Mono 3.2W en 4 Ohm, 92% eficiencia)\\n- Entrada directa PCM I2S sin ruido analógico de masa ni zumbidos\\n- J2: Conector hacia Altavoz Mylar Impermeable 4 Ohm / 3W de 40mm diámetro (90 dB SPL a 1m)"
		(at 30 125 0)
		(effects
			(font
				(size 1.8 1.8)
			)
			(justify left)
		)
		(uuid "{uuid.uuid4()}")
	)
	(text "SECCIÓN 4: CÁMARA GRAN ANGULAR Y VISIÓN NOCTURNA"
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
	(text "J3: Conector FPC 24 pines para sensor de imagen OV2640 / OV5640 (Gran Angular 160 D-FOV)\\n- Lente M12 con filtro mecánico conmutable IR-CUT motorizado (solenoide biestable 5V)\\n- Control IR-CUT: GPIO 8 y GPIO 9 mediante puente H miniatura (TC78H660FNG)\\n- D2, D3: LEDs Infrarrojos 850nm / 940nm de alta potencia con disipador térmico SMD\\n- Sensor LDR (Fotorresistencia): Detección automática del nivel crepuscular"
		(at 160 125 0)
		(effects
			(font
				(size 1.8 1.8)
			)
			(justify left)
		)
		(uuid "{uuid.uuid4()}")
	)
	(text "SECCIÓN 5: ACCESO SEGURO, CERRADURA ELÉCTRICA Y RFID/NFC"
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
	(text "OK1: Optoacoplador PC817 para aislamiento galvanico completo entre lógica y cerradura\\nQ1: MOSFET N-Channel de Potencia IRLZ44N (Vds 55V, Id 47A, Rds_on 0.022 Ohm, Logic-Level)\\nD4: Diodo Supresor Flyback 1N5408 / SB560 en paralelo con la cerradura (absorción de picos inductivos)\\nJ4: Bornera enchufable 5.08mm para electrocerradura 12V 2A (Normalmente Abierta o Cerrada)\\nU7: Módulo Lector NFC/RFID PN532 (Antena integrada en PCB frontal para tarjetas ISO14443A/Mifare y Apple/Google Pay)"
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
## Proyecto: Videoportero Inteligente ESP32-S3 y Control de Acceso VoIP / WebRTC
**Directorio:** `03_seguridad_y_control_acceso/06_intercomunicacion_videoportero_y_multizona/electrico/`  
**Diseño:** KiCad 10.0 | Código de Proyecto: `ESP32S3-DOORBELL-V1`

---

### 1. Circuitos Integrados y Módulos Principales
| Referencia | Componente | Encapsulado | Función / Especificación | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **U4** | ESP32-S3-WROOM-1-N16R8 | SMD Módulo | MCU Dual-Core 240MHz, 16MB Flash, 8MB Octal PSRAM | 1 |
| **U5** | INMP441 / ICS-43434 | SMD QFN-14 | Micrófono MEMS Digital I2S (SNR 65 dBA) | 1 |
| **U6** | MAX98357A | SMD WLP / TQFN | Amplificador de Audio Digital I2S Clase D Mono 3.2W | 1 |
| **U1** | Silvertel Ag9905M | Módulo SIL Through-Hole | Extractor PoE IEEE 802.3af (Entrada 48V -> Salida 5V 1.8A Aislada) | 1 |
| **U2** | AMS1117-3.3 | SOT-223 | Regulador lineal de bajo voltaje (5V -> 3.3V 800mA) | 1 |
| **U7** | NXP PN532 | QFN-40 / Breakout | Controlador NFC/RFID 13.56MHz con soporte Mifare/NFC Forum | 1 |
| **CAM1** | Módulo Sensor OV2640 / OV5640 | FPC 24 pines | Sensor CMOS HD con lente M12 gran angular 160° y filtro IR-CUT | 1 |

---

### 2. Driver de Cerradura Eléctrica y Potencia
| Referencia | Componente | Encapsulado | Función | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **OK1** | PC817 | DIP-4 / SMD | Optoacoplador para aislamiento de la señal de apertura | 1 |
| **Q1** | IRLZ44N / IRLML0030 | TO-220 / SOT-23 | MOSFET canal N Logic-Level para accionar cerradura 12V 2A | 1 |
| **D4** | SB560 / 1N5408 | DO-201AD | Diodo Schottky de protección contra picos inductivos (Flyback) | 1 |
| **K1** | Omron G5V-1 (Opcional) | DIP-6 | Relé miniatura de contacto seco (contacto libre de potencial) | 1 |

---

### 3. Componentes de Interfaz Humana y Acústica
| Referencia | Componente | Tipo | Especificación | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **SW1** | Pulsador Piezoeléctrico Antivandálico | Diámetro 19mm | Acero inoxidable 316, anillo LED iluminado, IP68 | 1 |
| **SPK1** | Altavoz Cónico de Mylar | Diámetro 40mm | Impedancia 4 Ω, Potencia 3 W, membrana impermeable IP65 | 1 |
| **IR1, IR2** | LEDs Infrarrojos de Potencia | SMD 3535 | Longitud de onda 850nm / 940nm con lente de 120° | 2 |
| **PIR1** | Sensor PIR miniatura / LD2410 | Cabezal 5-pin | Sensor de presencia radar 24 GHz para pre-activación de vídeo | 1 |

---

### 4. Conectores y Borneras
| Referencia | Conector | Pines | Uso | Cantidad |
| :--- | :--- | :--- | :--- | :--- |
| **J1** | Conector RJ45 blindado con imanes | 8 pines | Entrada Ethernet 10/100 con soporte PoE pasivo/activo | 1 |
| **J2** | Conector JST-PH 2.0mm | 2 pines | Salida hacia altavoz frontal impermeable | 1 |
| **J3** | Conector FPC 0.5mm paso | 24 pines | Conexión directa al módulo de cámara HD | 1 |
| **J4** | Bornera Enchufable KF2EDG 5.08mm | 4 pines | Conexión externa de electrocerradura (12V DC, GND, Contacto) | 1 |
"""
    with open(bom_path, "w", encoding="utf-8") as f:
        f.write(bom_content)

    print(f"Proyecto KiCad videoportero generado en: {output_dir}")
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
        print(f"Esquema SVG videoportero exportado mediante kicad-cli en: {svg_dir}")
    except Exception as e:
        print(f"Aviso al exportar videoportero con kicad-cli: {e}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_dir = os.path.join(base_dir, "03_seguridad_y_control_acceso/06_intercomunicacion_videoportero_y_multizona/electrico")
    generar_kicad_videoportero(target_dir)

