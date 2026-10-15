#!/usr/bin/env python3
"""
Generador del Esquema P&ID de Captación Pluvial, Cisterna y Tren de Potabilización UV-C
Formatos de salida: DXF y SVG vectorial
Proyecto: open-source-domotics
"""

import os
from generar_planos_dxf import SimpleDXF

def generar_esquema_pluvial(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_ROTULO", color=7)
    dxf.add_layer("CAPTACION_TEJADO", color=1)
    dxf.add_layer("CISTERNA_10000L", color=4)
    dxf.add_layer("TREN_FILTRADO_UVC", color=2)
    dxf.add_layer("RED_DISTRIBUCION", color=5)
    dxf.add_layer("TEXTO_ROTULOS", color=7)

    dxf.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf.add_rect(240, 10, 170, 40, layer="MARCO_ROTULO")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", 245, 38, height=4.0, layer="TEXTO_ROTULOS")
    dxf.add_text("CAPTACIÓN PLUVIAL, CISTERNA Y TREN DE POTABILIZACIÓN UV-C", 245, 28, height=2.2, layer="TEXTO_ROTULOS")
    dxf.add_text("First-Flush -> Cisterna 10kL -> Filtros 20u/5u/CTO -> UV-C 55W -> Red", 245, 18, height=1.7, layer="TEXTO_ROTULOS")

    # 1. Bajante y First Flush (Izquierda)
    dxf.add_line(40, 260, 90, 260, layer="CAPTACION_TEJADO")
    dxf.add_line(90, 260, 90, 180, layer="CAPTACION_TEJADO")
    dxf.add_text("RECOLECCIÓN AZOTEA (100 m²)", 35, 268, height=2.0, layer="TEXTO_ROTULOS")

    # Separador de Primeras Aguas (First Flush 150L)
    dxf.add_rect(80, 120, 20, 60, layer="CAPTACION_TEJADO")
    dxf.add_text("FIRST FLUSH 150L", 55, 155, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Purga Inicial Suciedad", 55, 147, height=1.4, layer="TEXTO_ROTULOS")

    # 2. Cisterna Enterrada 10,000 Litros
    dxf.add_line(90, 190, 140, 190, layer="CAPTACION_TEJADO")
    dxf.add_line(140, 190, 140, 60, layer="CISTERNA_10000L") # Entrada calmada

    dxf.add_rect(130, 40, 90, 160, layer="CISTERNA_10000L")
    dxf.add_text("CISTERNA ENTERRADA", 135, 185, height=2.2, layer="TEXTO_ROTULOS")
    dxf.add_text("CAPACIDAD: 10,000 LITROS", 135, 175, height=1.8, layer="TEXTO_ROTULOS")
    dxf.add_text("- Sonda Nivel Hidrostático (4-20mA)", 135, 155, height=1.5, layer="TEXTO_ROTULOS")
    dxf.add_text("- Entrada Calmada Antisedimento", 135, 140, height=1.5, layer="TEXTO_ROTULOS")
    dxf.add_text("- Toma Flotante de Aspiración", 135, 125, height=1.5, layer="TEXTO_ROTULOS")
    dxf.add_text("- Rebose con Sifón Antiroedores", 135, 110, height=1.5, layer="TEXTO_ROTULOS")

    # Bomba Sumergible Multietapa
    dxf.add_circle(175, 70, 12, layer="TREN_FILTRADO_UVC")
    dxf.add_text("BOMBA 1.1kW", 160, 52, height=1.5, layer="TEXTO_ROTULOS")

    # Tubería de Impulsión hacia Tren de Tratamiento
    dxf.add_line(175, 82, 175, 220, layer="RED_DISTRIBUCION")
    dxf.add_line(175, 220, 240, 220, layer="RED_DISTRIBUCION")

    # 3. Tren de Filtración en Caseta / Sala Técnica
    # Filtro 1: Sedimentos 20 micras
    dxf.add_rect(240, 205, 20, 30, layer="TREN_FILTRADO_UVC")
    dxf.add_text("F1 20u", 242, 222, height=1.6, layer="TEXTO_ROTULOS")

    # Filtro 2: Sedimentos 5 micras
    dxf.add_line(260, 220, 275, 220, layer="RED_DISTRIBUCION")
    dxf.add_rect(275, 205, 20, 30, layer="TREN_FILTRADO_UVC")
    dxf.add_text("F2 5u", 278, 222, height=1.6, layer="TEXTO_ROTULOS")

    # Filtro 3: Carbón Activado CTO
    dxf.add_line(295, 220, 310, 220, layer="RED_DISTRIBUCION")
    dxf.add_rect(310, 205, 22, 30, layer="TREN_FILTRADO_UVC")
    dxf.add_text("CTO Carbón", 311, 222, height=1.5, layer="TEXTO_ROTULOS")

    # 4. Esterilizador Ultravioleta UV-C 55W Germicida
    dxf.add_line(332, 220, 345, 220, layer="RED_DISTRIBUCION")
    dxf.add_rect(345, 200, 35, 40, layer="TREN_FILTRADO_UVC")
    dxf.add_text("LÁMPARA UV-C 55W", 347, 230, height=1.8, layer="TEXTO_ROTULOS")
    dxf.add_text("254 nm Germicida", 347, 220, height=1.5, layer="TEXTO_ROTULOS")
    dxf.add_text("99.99% Esterilización", 347, 210, height=1.3, layer="TEXTO_ROTULOS")

    # Salida a Red Presurizada Doméstica
    dxf.add_line(380, 220, 410, 220, layer="RED_DISTRIBUCION")
    dxf.add_text("RED AGUA POTABLE (3.5 bar)", 280, 185, height=2.0, layer="TEXTO_ROTULOS")

    dxf.save()

    # 2. GENERACIÓN SVG
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1150 750" width="100%" height="100%" style="background:#11111b; font-family:sans-serif;">
  <defs>
    <style>
      .title {{ fill: #cdd6f4; font-size: 20px; font-weight: bold; }}
      .sub {{ fill: #89b4fa; font-size: 13px; }}
      .box {{ fill: #1e1e2e; stroke: #45475a; stroke-width: 2; rx: 6; }}
      .lbl {{ fill: #cdd6f4; font-size: 11px; }}
      .lbl-bold {{ fill: #ffffff; font-size: 12px; font-weight: bold; }}
      .lbl-sm {{ fill: #a6adc8; font-size: 9.5px; }}
      .pipe-raw {{ stroke: #a6adc8; stroke-width: 4; fill: none; }}
      .pipe-pure {{ stroke: #89dceb; stroke-width: 4; fill: none; }}
      .cistern {{ fill: #181825; stroke: #89b4fa; stroke-width: 3; rx: 10; }}
      .filter-box {{ fill: #1e1e2e; stroke: #a6e3a1; stroke-width: 2; rx: 4; }}
      .uv-box {{ fill: #181825; stroke: #cba6f7; stroke-width: 2.5; rx: 6; }}
    </style>
  </defs>

  <!-- Marco -->
  <rect x="20" y="20" width="1110" height="710" fill="none" stroke="#313244" stroke-width="2" rx="10"/>

  <!-- Encabezado -->
  <text x="50" y="55" class="title">CAPTACIÓN PLUVIAL, CISTERNA 10,000L Y TREN DE POTABILIZACIÓN UV-C</text>
  <text x="50" y="80" class="sub">Separador First-Flush 150L | Bomba Sumergible con Toma Flotante | Filtros 20µm / 5µm / Carbón CTO | Lámpara UV-C 55W</text>

  <!-- 1. Tejado y Bajante -->
  <rect x="50" y="130" width="160" height="70" class="box" stroke="#fab387"/>
  <text x="65" y="155" class="lbl-bold" style="fill:#fab387;">AZOTEA DE RECOGIDA</text>
  <text x="65" y="175" class="lbl-sm">100 m² Cubierta limpia</text>
  <text x="65" y="190" class="lbl-sm">Canalón con rejilla anti-hojas</text>

  <line x1="210" y1="165" x2="260" y2="165" class="pipe-raw"/>
  <line x1="260" y1="165" x2="260" y2="220" class="pipe-raw"/>

  <!-- First Flush -->
  <rect x="230" y="220" width="60" height="150" class="box" stroke="#f38ba8"/>
  <text x="240" y="250" class="lbl-bold" style="fill:#f38ba8; font-size:10px;">FIRST</text>
  <text x="240" y="268" class="lbl-bold" style="fill:#f38ba8; font-size:10px;">FLUSH</text>
  <text x="238" y="295" class="lbl-sm">150 Litros</text>
  <text x="235" y="325" class="lbl-sm">Drenaje de</text>
  <text x="235" y="340" class="lbl-sm">suciedad</text>

  <line x1="260" y1="220" x2="350" y2="220" class="pipe-raw"/>
  <line x1="350" y1="220" x2="350" y2="300" class="pipe-raw"/>

  <!-- 2. Cisterna Enterrada 10,000L -->
  <rect x="330" y="280" width="260" height="380" class="cistern"/>
  <text x="355" y="320" class="lbl-bold" style="fill:#89b4fa; font-size:16px;">CISTERNA 10,000 LITROS</text>
  <text x="355" y="345" class="lbl-sm">• Hormigón impermeabilizado / PEAD</text>
  <text x="355" y="370" class="lbl-sm">• Entrada calmada (no remueve fondos)</text>
  <text x="355" y="395" class="lbl-sm">• Sonda hidrostática 4-20mA (Nivel cm)</text>
  <text x="355" y="420" class="lbl-sm">• Rebose sifónico con malla anti-roedores</text>

  <!-- Bomba Sumergible con Toma Flotante -->
  <circle cx="460" cy="580" r="35" fill="#313244" stroke="#89dceb" stroke-width="2"/>
  <text x="435" y="585" class="lbl-bold" style="fill:#89dceb; font-size:11px;">BOMBA 1.1kW</text>
  <text x="430" y="605" class="lbl-sm">Toma Flotante</text>

  <!-- Impulsión hacia Tren de Potabilización -->
  <line x1="495" y1="580" x2="650" y2="580" class="pipe-pure"/>
  <line x1="650" y1="580" x2="650" y2="230" class="pipe-pure"/>
  <line x1="650" y1="230" x2="690" y2="230" class="pipe-pure"/>

  <!-- 3. Tren de Tratamiento (Caseta Técnica) -->
  <rect x="680" y="140" width="410" height="230" class="box" stroke="#a6e3a1"/>
  <text x="700" y="170" class="lbl-bold" style="fill:#a6e3a1; font-size:14px;">TREN DE POTABILIZACIÓN EN SALA TÉCNICA</text>

  <!-- Filtro 20u -->
  <rect x="700" y="190" width="60" height="90" class="filter-box"/>
  <text x="712" y="225" class="lbl-bold">F1</text>
  <text x="705" y="245" class="lbl-sm">20 µm</text>
  <text x="705" y="260" class="lbl-sm">Sedim.</text>

  <!-- Filtro 5u -->
  <line x1="760" y1="235" x2="790" y2="235" class="pipe-pure"/>
  <rect x="790" y="190" width="60" height="90" class="filter-box"/>
  <text x="802" y="225" class="lbl-bold">F2</text>
  <text x="798" y="245" class="lbl-sm">5 µm</text>
  <text x="795" y="260" class="lbl-sm">Fino</text>

  <!-- Filtro CTO -->
  <line x1="850" y1="235" x2="880" y2="235" class="pipe-pure"/>
  <rect x="880" y="190" width="60" height="90" class="filter-box"/>
  <text x="892" y="225" class="lbl-bold">CTO</text>
  <text x="885" y="245" class="lbl-sm">Carbón</text>
  <text x="883" y="260" class="lbl-sm">Activo</text>

  <!-- Lámpara UV-C 55W -->
  <line x1="940" y1="235" x2="970" y2="235" class="pipe-pure"/>
  <rect x="970" y="180" width="105" height="110" class="uv-box"/>
  <text x="980" y="215" class="lbl-bold" style="fill:#cba6f7;">LÁMPARA UV-C</text>
  <text x="980" y="235" class="lbl-sm">Potencia: 55 W</text>
  <text x="980" y="250" class="lbl-sm">254 nm germicida</text>
  <text x="980" y="265" class="lbl-sm" style="fill:#a6e3a1; font-weight:bold;">99.99% Bacterias</text>

  <!-- Salida a Casa -->
  <line x1="1075" y1="235" x2="1110" y2="235" class="pipe-pure"/>
  <text x="700" y="325" class="lbl-bold" style="fill:#89dceb; font-size:13px;">AGUA 100% POTABLE HACIA RED DE VIVIENDA (3.5 BAR CONSTANTE)</text>
  <text x="700" y="345" class="lbl-sm">• Monitoreo de caudal instantáneo y horas de vida de lámpara UV en Home Assistant</text>

</svg>
"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Esquema pluvial generado: DXF={dxf_path}, SVG={svg_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dxf_target = os.path.join(base_dir, "00_diseno_arquitectonico_y_estructural/07_captacion_pluvial_cisterna_y_potabilizacion/mecanico/esquema_captacion_potabilizacion_pluvial.dxf")
    svg_target = os.path.join(base_dir, "00_diseno_arquitectonico_y_estructural/07_captacion_pluvial_cisterna_y_potabilizacion/mecanico/esquema_captacion_potabilizacion_pluvial.svg")
    generar_esquema_pluvial(dxf_target, svg_target)

