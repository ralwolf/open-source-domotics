#!/usr/bin/env python3
"""
Generador del Diagrama Unifilar Fotovoltaico y Almacenamiento Baterías ESS
Formatos de salida: DXF y SVG vectorial
Proyecto: open-source-domotics
"""

import os
from generar_planos_dxf import SimpleDXF

def generar_diagrama_solar_ess(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_ROTULO", color=7)
    dxf.add_layer("STRINGS_DC_FOTOVOLTAICO", color=1)
    dxf.add_layer("INVERSOR_HIBRIDO", color=4)
    dxf.add_layer("BANCO_BATERIAS_LIFEPO4", color=3)
    dxf.add_layer("PROTECCIONES_FUSIBLES", color=2)
    dxf.add_layer("LINEAS_AC_SALIDA", color=6)
    dxf.add_layer("TEXTO_ROTULOS", color=7)

    dxf.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf.add_rect(240, 10, 170, 40, layer="MARCO_ROTULO")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", 245, 38, height=4.0, layer="TEXTO_ROTULOS")
    dxf.add_text("ESQUEMA SOLAR FOTOVOLTAICO Y ALMACENAMIENTO ESS", 245, 28, height=2.4, layer="TEXTO_ROTULOS")
    dxf.add_text("8.8 kWp Solar + Inversor Híbrido 8kW + Banco LiFePO4 16S (14.3 kWh)", 245, 18, height=1.8, layer="TEXTO_ROTULOS")

    # Strings Fotovoltaicos
    # String 1: 8x 550W (4.4 kWp)
    dxf.add_rect(30, 220, 80, 40, layer="STRINGS_DC_FOTOVOLTAICO")
    dxf.add_text("STRING 1: 8x 550W BIFACIAL", 33, 248, height=2.0, layer="TEXTO_ROTULOS")
    dxf.add_text("Voc: 396V | Isc: 13.8A | 4.4 kWp", 33, 238, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Orientación Sur / Azimut 0°", 33, 228, height=1.5, layer="TEXTO_ROTULOS")

    # String 2: 8x 550W (4.4 kWp)
    dxf.add_rect(30, 160, 80, 40, layer="STRINGS_DC_FOTOVOLTAICO")
    dxf.add_text("STRING 2: 8x 550W BIFACIAL", 33, 188, height=2.0, layer="TEXTO_ROTULOS")
    dxf.add_text("Voc: 396V | Isc: 13.8A | 4.4 kWp", 33, 178, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Orientación Este-Oeste", 33, 168, height=1.5, layer="TEXTO_ROTULOS")

    # Combiner Box DC (Fusibles gPV 15A + DPS DC 1000V)
    dxf.add_rect(130, 150, 45, 120, layer="PROTECCIONES_FUSIBLES")
    dxf.add_text("COMBINER BOX DC", 133, 255, height=2.0, layer="TEXTO_ROTULOS")
    dxf.add_text("4x Fusibles gPV 15A", 133, 240, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("2x DPS Tipo 2 (1000V)", 133, 220, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Seccionador DC 32A", 133, 200, height=1.6, layer="TEXTO_ROTULOS")

    # Conexiones Strings hacia Combiner
    dxf.add_line(110, 240, 130, 240, layer="STRINGS_DC_FOTOVOLTAICO")
    dxf.add_line(110, 180, 130, 180, layer="STRINGS_DC_FOTOVOLTAICO")

    # Inversor Híbrido 8 kW
    dxf.add_line(175, 240, 205, 240, layer="STRINGS_DC_FOTOVOLTAICO")
    dxf.add_line(175, 180, 205, 180, layer="STRINGS_DC_FOTOVOLTAICO")
    dxf.add_rect(205, 140, 75, 130, layer="INVERSOR_HIBRIDO")
    dxf.add_text("INVERSOR HÍBRIDO 8 kW", 210, 255, height=2.4, layer="TEXTO_ROTULOS")
    dxf.add_text("Doble MPPT (120-500V DC)", 210, 245, height=1.8, layer="TEXTO_ROTULOS")
    dxf.add_text("Cargador Batería 48V (190A)", 210, 235, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Salida EPS Backup < 10ms", 210, 225, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("CANbus / RS485 Modbus", 210, 215, height=1.6, layer="TEXTO_ROTULOS")

    # Banco de Baterías LiFePO4 48V (Abajo)
    dxf.add_rect(205, 30, 75, 80, layer="BANCO_BATERIAS_LIFEPO4")
    dxf.add_text("BANCO BATERÍAS ESS", 210, 95, height=2.2, layer="TEXTO_ROTULOS")
    dxf.add_text("16S LiFePO4 280Ah", 210, 85, height=1.8, layer="TEXTO_ROTULOS")
    dxf.add_text("Capacidad: 14.33 kWh", 210, 75, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Smart BMS 200A Activo", 210, 65, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Fusible Clase T 300A", 210, 55, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Seccionador DC 250A", 210, 45, height=1.6, layer="TEXTO_ROTULOS")

    # Enlace DC entre Batería e Inversor
    dxf.add_line(235, 110, 235, 140, layer="BANCO_BATERIAS_LIFEPO4")
    dxf.add_line(250, 110, 250, 140, layer="BANCO_BATERIAS_LIFEPO4")
    dxf.add_text("Línea 48V DC (2x 50 mm²)", 255, 125, height=1.6, layer="TEXTO_ROTULOS")

    # Salidas AC del Inversor
    # 1. AC Grid (Conexión a Tablero General y Red)
    dxf.add_line(280, 240, 360, 240, layer="LINEAS_AC_SALIDA")
    dxf.add_text("AC GRID (HACIA TGBT / RED)", 285, 248, height=1.8, layer="TEXTO_ROTULOS")
    # 2. AC Load / EPS Backup (Cargas Críticas)
    dxf.add_line(280, 180, 360, 180, layer="LINEAS_AC_SALIDA")
    dxf.add_text("AC LOAD (CARGAS CRÍTICAS UPS)", 285, 188, height=1.8, layer="TEXTO_ROTULOS")

    dxf.save()

    # 2. GENERACIÓN SVG
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="100%" height="100%" style="background:#11111b; font-family:sans-serif;">
  <defs>
    <style>
      .title {{ fill: #cdd6f4; font-size: 22px; font-weight: bold; }}
      .sub {{ fill: #89b4fa; font-size: 13px; }}
      .box {{ fill: #1e1e2e; stroke: #45475a; stroke-width: 2; rx: 6; }}
      .lbl {{ fill: #cdd6f4; font-size: 11px; }}
      .lbl-bold {{ fill: #ffffff; font-size: 12px; font-weight: bold; }}
      .lbl-sm {{ fill: #a6adc8; font-size: 9.5px; }}
      .wire-pv {{ stroke: #fab387; stroke-width: 3.5; fill: none; }}
      .wire-bat {{ stroke: #a6e3a1; stroke-width: 5; fill: none; }}
      .wire-ac {{ stroke: #f38ba8; stroke-width: 3.5; fill: none; }}
    </style>
  </defs>

  <!-- Marco -->
  <rect x="20" y="20" width="1160" height="760" fill="none" stroke="#313244" stroke-width="2" rx="10"/>

  <!-- Encabezado -->
  <text x="50" y="55" class="title">GENERACIÓN SOLAR FOTOVOLTAICA Y ALMACENAMIENTO ESS (BATERÍAS LIFEPO4)</text>
  <text x="50" y="80" class="sub">8.8 kWp Paneles Bifaciales | Inversor Híbrido 8 kW | Banco 16S 280Ah (14.3 kWh) | Cargas Críticas Ininterrumpibles</text>

  <!-- 1. Strings Fotovoltaicos -->
  <rect x="50" y="140" width="220" height="120" class="box" stroke="#fab387"/>
  <text x="70" y="170" class="lbl-bold" style="fill:#fab387; font-size:13px;">STRING 1 (SUR - 4.4 kWp)</text>
  <text x="70" y="195" class="lbl">• 8x Paneles 550W Monocristalinos</text>
  <text x="70" y="215" class="lbl">• Tensión Voc: 396 V DC</text>
  <text x="70" y="235" class="lbl">• Corriente Imp: 13.2 A DC</text>

  <rect x="50" y="300" width="220" height="120" class="box" stroke="#fab387"/>
  <text x="70" y="330" class="lbl-bold" style="fill:#fab387; font-size:13px;">STRING 2 (ESTE/OESTE - 4.4 kWp)</text>
  <text x="70" y="355" class="lbl">• 8x Paneles 550W Bifaciales</text>
  <text x="70" y="375" class="lbl">• Tensión Voc: 396 V DC</text>
  <text x="70" y="395" class="lbl">• Corriente Imp: 13.2 A DC</text>

  <!-- Combiner Box DC -->
  <line x1="270" y1="200" x2="330" y2="200" class="wire-pv"/>
  <line x1="270" y1="360" x2="330" y2="360" class="wire-pv"/>

  <rect x="330" y="160" width="130" height="240" class="box" stroke="#f9e2af"/>
  <text x="345" y="195" class="lbl-bold" style="fill:#f9e2af; font-size:11px;">COMBINER BOX DC</text>
  <text x="345" y="225" class="lbl-sm">• 4x Fusibles gPV 15A</text>
  <text x="345" y="250" class="lbl-sm">• 2x DPS DC 1000V Tipo 2</text>
  <text x="345" y="275" class="lbl-sm">• Seccionador DC 32A</text>
  <text x="345" y="300" class="lbl-sm">• Puesta a tierra solar</text>
  <text x="345" y="325" class="lbl-sm">• Protección tormentas</text>

  <!-- Líneas al Inversor -->
  <line x1="460" y1="230" x2="550" y2="230" class="wire-pv"/>
  <line x1="460" y1="330" x2="550" y2="330" class="wire-pv"/>

  <!-- 2. INVERSOR HÍBRIDO 8 kW -->
  <rect x="550" y="150" width="260" height="280" class="box" stroke="#89b4fa" stroke-width="2.5"/>
  <text x="575" y="190" class="lbl-bold" style="fill:#89b4fa; font-size:16px;">INVERSOR HÍBRIDO 8 kW</text>
  <text x="575" y="215" class="lbl">• Doble MPPT Independiente (120-500V)</text>
  <text x="575" y="235" class="lbl">• Eficiencia Euro: 97.6%</text>
  <text x="575" y="255" class="lbl">• Conexión Baterías 48V (Carga hasta 190A)</text>
  <text x="575" y="275" class="lbl">• Conmutación EPS Backup: &lt; 10 ms</text>
  <text x="575" y="295" class="lbl" style="fill:#fab387;">• Puerto CANbus / RS-485 hacia BMS</text>
  <text x="575" y="315" class="lbl">• Integración Modbus TCP a Home Assistant</text>
  <text x="575" y="345" class="lbl-sm" style="fill:#a6adc8;">Gestión dinámica de inyección cero o venta de excedentes</text>

  <!-- 3. BANCO DE BATERÍAS LIFEPO4 16S (Abajo) -->
  <line x1="680" y1="430" x2="680" y2="520" class="wire-bat"/>
  <rect x="530" y="520" width="300" height="220" class="box" stroke="#a6e3a1" stroke-width="2.5"/>
  <text x="555" y="555" class="lbl-bold" style="fill:#a6e3a1; font-size:16px;">BANCO BATERÍAS ESS 14.3 kWh</text>
  <text x="555" y="580" class="lbl">• 16 Celdas LiFePO4 EVE LF280K Grado A</text>
  <text x="555" y="600" class="lbl">• Tensión Nominal: 51.2 V (48V Bus)</text>
  <text x="555" y="620" class="lbl">• Capacidad: 280 Ah (14,336 Wh útiles al 90% DoD)</text>
  <text x="555" y="640" class="lbl">• Smart BMS 200A continuo / 350A pico</text>
  <text x="555" y="660" class="lbl">• Balanceador Activo 2A por transferencia inductiva</text>
  <text x="555" y="680" class="lbl">• Fusible Clase T de 300A (Capacidad ruptura 20kA)</text>
  <text x="555" y="700" class="lbl">• Placas de compresión con varillas M8 (300 kgf)</text>

  <!-- Salidas AC del Inversor -->
  <!-- Salida 1: Red General -->
  <line x1="810" y1="230" x2="940" y2="230" class="wire-ac"/>
  <rect x="940" y="195" width="200" height="70" class="box" stroke="#f38ba8"/>
  <text x="955" y="225" class="lbl-bold" style="fill:#f38ba8;">AC GRID (TGBT)</text>
  <text x="955" y="245" class="lbl-sm">Conexión a Red Pública y Cuadro General</text>

  <!-- Salida 2: Cargas Críticas -->
  <line x1="810" y1="350" x2="940" y2="350" class="wire-ac"/>
  <rect x="940" y="315" width="200" height="70" class="box" stroke="#a6e3a1"/>
  <text x="955" y="345" class="lbl-bold" style="fill:#a6e3a1;">AC EPS LOAD (UPS)</text>
  <text x="955" y="365" class="lbl-sm">Alimentación ininterrumpible 0-10ms:</text>
  <text x="955" y="380" class="lbl-sm">Nevera, Sala IT, CCTV, Lucernario</text>

</svg>
"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Diagrama solar y baterías ESS generado: DXF={dxf_path}, SVG={svg_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dxf_target = os.path.join(base_dir, "01_energia_renovable_y_potencia/03_solar_fotovoltaica/electrico/esquema_fotovoltaico_ess.dxf")
    svg_target = os.path.join(base_dir, "01_energia_renovable_y_potencia/03_solar_fotovoltaica/electrico/esquema_fotovoltaico_ess.svg")
    generar_diagrama_solar_ess(dxf_target, svg_target)
