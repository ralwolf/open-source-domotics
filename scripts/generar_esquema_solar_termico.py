#!/usr/bin/env python3
"""
Generador del Esquema Hidráulico de Principio (P&ID) de Solar Térmico y Suelo Radiante
Formatos de salida: DXF y SVG vectorial
Proyecto: open-source-domotics
"""

import os
from generar_planos_dxf import SimpleDXF

def generar_esquema_solar_termico(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_ROTULO", color=7)
    dxf.add_layer("TUBERIA_SOLAR_CALOR", color=1)    # Rojo
    dxf.add_layer("TUBERIA_RETORNO_FRIO", color=5)   # Azul
    dxf.add_layer("INTERACUMULADOR_500L", color=4)   # Cian
    dxf.add_layer("PISO_RADIANTE_CIRCUITO", color=2) # Amarillo
    dxf.add_layer("VALVULAS_Y_SENSORES", color=3)    # Verde
    dxf.add_layer("TEXTO_ROTULOS", color=7)

    dxf.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf.add_rect(240, 10, 170, 40, layer="MARCO_ROTULO")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", 245, 38, height=4.0, layer="TEXTO_ROTULOS")
    dxf.add_text("ESQUEMA HIDRÁULICO SOLAR TÉRMICO Y SUELO RADIANTE", 245, 28, height=2.4, layer="TEXTO_ROTULOS")
    dxf.add_text("Colectores Tubos Vacío -> Tanque Inercia 500L -> ACS & Suelo 35°C", 245, 18, height=1.8, layer="TEXTO_ROTULOS")

    # 1. Colectores Solares en Cubierta (Y: 230 a 265)
    dxf.add_rect(40, 230, 100, 35, layer="TUBERIA_SOLAR_CALOR")
    dxf.add_text("CAMPO SOLAR TÉRMICO (4x TUBOS VACÍO)", 43, 255, height=2.0, layer="TEXTO_ROTULOS")
    dxf.add_text("Superficie: 8.4 m² | Fluido: Glicol 40%", 45, 246, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Sonda T_colector (PT1000)", 45, 237, height=1.6, layer="TEXTO_ROTULOS")

    # Línea Ida Solar (Glicol Caliente - Rojo)
    dxf.add_line(140, 260, 200, 260, layer="TUBERIA_SOLAR_CALOR")
    dxf.add_line(200, 260, 200, 120, layer="TUBERIA_SOLAR_CALOR")

    # Tanque Interacumulador de 500L (X: 180 a 250, Y: 40 a 170)
    dxf.add_rect(180, 40, 70, 130, layer="INTERACUMULADOR_500L")
    dxf.add_text("INTERACUMULADOR", 185, 155, height=2.2, layer="TEXTO_ROTULOS")
    dxf.add_text("INERCIA 500 LITROS", 185, 147, height=2.0, layer="TEXTO_ROTULOS")
    dxf.add_text("Aislamiento PU 100mm", 185, 139, height=1.5, layer="TEXTO_ROTULOS")
    # Serpentín Inferior Solar
    dxf.add_line(190, 60, 240, 60, layer="TUBERIA_SOLAR_CALOR")
    dxf.add_line(190, 75, 240, 75, layer="TUBERIA_SOLAR_CALOR")
    dxf.add_line(190, 90, 240, 90, layer="TUBERIA_SOLAR_CALOR")
    dxf.add_text("Serpentín Solar", 188, 67, height=1.5, layer="TEXTO_ROTULOS")

    # Retorno Solar (Glicol Frío - Azul) con Bomba Solar y Vaso Expansión
    dxf.add_line(200, 50, 90, 50, layer="TUBERIA_RETORNO_FRIO")
    dxf.add_line(90, 50, 90, 230, layer="TUBERIA_RETORNO_FRIO")
    # Bomba Solar
    dxf.add_circle(90, 140, 8, layer="VALVULAS_Y_SENSORES")
    dxf.add_text("BOMBA SOLAR PWM", 65, 153, height=1.6, layer="TEXTO_ROTULOS")
    # Vaso Expansión Solar
    dxf.add_rect(50, 90, 20, 25, layer="VALVULAS_Y_SENSORES")
    dxf.add_text("VASO 25L", 52, 102, height=1.5, layer="TEXTO_ROTULOS")

    # Salida Superior ACS (Agua Caliente Sanitaria 45°C)
    dxf.add_line(215, 170, 215, 205, layer="TUBERIA_SOLAR_CALOR")
    dxf.add_rect(205, 205, 45, 20, layer="VALVULAS_Y_SENSORES")
    dxf.add_text("VÁLVULA MEZCLADORA ACS", 207, 217, height=1.5, layer="TEXTO_ROTULOS")
    dxf.add_text("Tarada a 45°C (Antiescaldamiento)", 207, 210, height=1.3, layer="TEXTO_ROTULOS")
    dxf.add_line(227, 225, 227, 260, layer="TUBERIA_SOLAR_CALOR")
    dxf.add_text("HACIA DUCHAS Y GRIFOS (ACS)", 205, 268, height=1.8, layer="TEXTO_ROTULOS")

    # Circuito de Suelo Radiante (Baja Temperatura 35°C)
    dxf.add_line(250, 130, 290, 130, layer="PISO_RADIANTE_CIRCUITO")
    # Válvula Mezcladora 3 Vías Climatización
    dxf.add_rect(290, 115, 30, 30, layer="VALVULAS_Y_SENSORES")
    dxf.add_text("V3V 35°C", 295, 132, height=1.8, layer="TEXTO_ROTULOS")
    dxf.add_text("Bomba SR", 295, 123, height=1.5, layer="TEXTO_ROTULOS")

    # Colector Distribuidor de Suelo Radiante (6 Zonas)
    dxf.add_rect(340, 70, 60, 130, layer="PISO_RADIANTE_CIRCUITO")
    dxf.add_text("COLECTOR SUELO RADIANTE", 342, 188, height=1.8, layer="TEXTO_ROTULOS")
    dxf.add_text("(6 CIRCUITOS MOTORIZADOS 24V)", 342, 180, height=1.4, layer="TEXTO_ROTULOS")

    zonas = ["Z1: Salón-Comedor", "Z2: Cocina", "Z3: Recámara Suite", "Z4: Recámara Infantil", "Z5: Baños", "Z6: Sala IT / Oficina"]
    y_z = 165
    for z in zonas:
        dxf.add_text(f"- {z}", 344, y_z, height=1.6, layer="TEXTO_ROTULOS")
        y_z -= 15

    dxf.save()

    # 2. GENERACIÓN SVG VECTORIAL
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 850" width="100%" height="100%" style="background:#11111b; font-family:sans-serif;">
  <defs>
    <style>
      .title {{ fill: #cdd6f4; font-size: 22px; font-weight: bold; }}
      .sub {{ fill: #89b4fa; font-size: 13px; }}
      .box {{ fill: #1e1e2e; stroke: #45475a; stroke-width: 2; rx: 6; }}
      .lbl {{ fill: #cdd6f4; font-size: 11px; }}
      .lbl-bold {{ fill: #ffffff; font-size: 12px; font-weight: bold; }}
      .lbl-sm {{ fill: #a6adc8; font-size: 9.5px; }}
      .pipe-hot {{ stroke: #f38ba8; stroke-width: 4; fill: none; }}
      .pipe-cold {{ stroke: #89b4fa; stroke-width: 4; fill: none; }}
      .pipe-radiant {{ stroke: #fab387; stroke-width: 3.5; fill: none; }}
      .tank {{ fill: #181825; stroke: #89dceb; stroke-width: 3; rx: 12; }}
    </style>
  </defs>

  <!-- Marco -->
  <rect x="20" y="20" width="1160" height="810" fill="none" stroke="#313244" stroke-width="2" rx="10"/>

  <!-- Encabezado -->
  <text x="50" y="60" class="title">SISTEMA SOLAR TÉRMICO Y CALEFACCIÓN POR PISO RADIANTE MULTIZONA</text>
  <text x="50" y="85" class="sub">Colectores de Tubos de Vacío (Heat-Pipes) | Tanque Inercia 500L | ACS Termostática 45°C | Colector Suelo 35°C (6 Zonas)</text>

  <!-- 1. Colectores Solares Térmicos en Azotea -->
  <rect x="80" y="130" width="280" height="110" class="box" stroke="#f38ba8"/>
  <text x="100" y="165" class="lbl-bold" style="fill:#f38ba8; font-size:14px;">CAMPO SOLAR TÉRMICO (AZOTEA)</text>
  <text x="100" y="185" class="lbl">• 4x Colectores Tubos de Vacío (8.4 m² útiles)</text>
  <text x="100" y="205" class="lbl">• Caloductos Heat-Pipe (Rendimiento invernal 72%)</text>
  <text x="100" y="225" class="lbl" style="fill:#fab387;">• Sonda Temperatura T_colector (PT1000)</text>

  <!-- Ida Solar Caliente (Rojo) hacia el Tanque -->
  <line x1="360" y1="180" x2="520" y2="180" class="pipe-hot"/>
  <line x1="520" y1="180" x2="520" y2="520" class="pipe-hot"/>
  <line x1="520" y1="520" x2="560" y2="520" class="pipe-hot"/>

  <!-- 2. Tanque Interacumulador de Inercia 500L -->
  <rect x="560" y="220" width="220" height="480" class="tank"/>
  <text x="585" y="260" class="lbl-bold" style="fill:#89dceb; font-size:16px;">INTERACUMULADOR</text>
  <text x="585" y="280" class="lbl-bold" style="fill:#89dceb; font-size:15px;">INERCIA 500 LITROS</text>
  <text x="585" y="305" class="lbl-sm">Aislamiento PU rígido 100 mm</text>
  <text x="585" y="320" class="lbl-sm">Estratificación térmica de alta eficiencia</text>

  <!-- Serpentín Superior (Apoyo caldera / resistencia) -->
  <rect x="585" y="350" width="170" height="45" fill="#313244" stroke="#fab387" rx="4"/>
  <text x="600" y="375" class="lbl-sm" style="fill:#fab387; font-weight:bold;">Serpentín Apoyo (Biogás/Resistencia)</text>

  <!-- Serpentín Inferior Solar -->
  <rect x="585" y="500" width="170" height="70" fill="#313244" stroke="#f38ba8" rx="4"/>
  <text x="600" y="535" class="lbl-sm" style="fill:#f38ba8; font-weight:bold;">Serpentín Primario Solar Térmico</text>
  <text x="600" y="555" class="lbl-sm">Sonda T_acumulador_inferior (PT1000)</text>

  <!-- Retorno Solar Frío (Azul) -->
  <line x1="560" y1="560" x2="220" y2="560" class="pipe-cold"/>
  <line x1="220" y1="560" x2="220" y2="240" class="pipe-cold"/>

  <!-- Estación de Bombeo Solar en Retorno -->
  <circle cx="220" cy="400" r="28" fill="#181825" stroke="#89b4fa" stroke-width="2.5"/>
  <text x="198" y="405" class="lbl-bold" style="fill:#89b4fa; font-size:10px;">BOMBA</text>
  <text x="195" y="445" class="lbl-sm">Grupo Solar PWM</text>

  <!-- Vaso de Expansión Solar -->
  <rect x="100" y="370" width="65" height="70" class="box" stroke="#89b4fa"/>
  <text x="110" y="405" class="lbl-sm" style="font-weight:bold;">VASO 25L</text>
  <text x="105" y="425" class="lbl-sm">Solar 6 bar</text>
  <line x1="165" y1="400" x2="192" y2="400" stroke="#89b4fa" stroke-width="2"/>

  <!-- 3. Módulo ACS Instantánea -->
  <line x1="670" y1="220" x2="670" y2="150" class="pipe-hot"/>
  <rect x="610" y="110" width="190" height="50" class="box" stroke="#a6e3a1"/>
  <text x="625" y="132" class="lbl-bold" style="fill:#a6e3a1;">VÁLVULA MEZCLADORA ACS</text>
  <text x="625" y="150" class="lbl-sm">Regulación termostática fija a 45°C</text>
  <line x1="800" y1="135" x2="900" y2="135" class="pipe-hot"/>
  <text x="910" y="140" class="lbl-bold" style="fill:#f38ba8;">HACIA ACS (GRIFOS Y DUCHAS)</text>

  <!-- 4. Colector Suelo Radiante -->
  <line x1="780" y1="440" x2="880" y2="440" class="pipe-radiant"/>
  <!-- V3V Mezcladora de suelo -->
  <rect x="880" y="415" width="80" height="50" class="box" stroke="#fab387"/>
  <text x="895" y="438" class="lbl-bold" style="fill:#fab387;">V3V 35°C</text>
  <text x="890" y="455" class="lbl-sm">+ Bomba SR</text>

  <!-- Colector de Zonas -->
  <line x1="960" y1="440" x2="1020" y2="440" class="pipe-radiant"/>
  <rect x="1020" y="270" width="130" height="380" class="box" stroke="#fab387" stroke-width="2.5"/>
  <text x="1030" y="300" class="lbl-bold" style="fill:#fab387; font-size:12px;">COLECTOR DISTRIB.</text>
  <text x="1030" y="320" class="lbl-sm" style="font-weight:bold;">PISO RADIANTE 6Z</text>

  <!-- 6 Zonas -->
  <text x="1030" y="360" class="lbl">1. Salón / Social</text>
  <text x="1030" y="410" class="lbl">2. Cocina</text>
  <text x="1030" y="460" class="lbl">3. Suite Principal</text>
  <text x="1030" y="510" class="lbl">4. Recámara Infantil</text>
  <text x="1030" y="560" class="lbl">5. Baños</text>
  <text x="1030" y="610" class="lbl">6. Oficina / IT</text>

</svg>
"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Esquema solar térmico generado: DXF={dxf_path}, SVG={svg_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dxf_target = os.path.join(base_dir, "01_energia_renovable_y_potencia/02_solar_termico_y_calefaccion/mecanico/esquema_hidraulico_piso_radiante.dxf")
    svg_target = os.path.join(base_dir, "01_energia_renovable_y_potencia/02_solar_termico_y_calefaccion/mecanico/esquema_hidraulico_piso_radiante.svg")
    generar_esquema_solar_termico(dxf_target, svg_target)
