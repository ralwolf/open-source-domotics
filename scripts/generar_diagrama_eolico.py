#!/usr/bin/env python3
"""
Generador del Diagrama Eléctrico de Potencia y Frenado del Aerogenerador Archimedes MK9
Formatos de salida: DXF y SVG vectorial
Proyecto: open-source-domotics
"""

import os
from generar_planos_dxf import SimpleDXF

def generar_diagrama_eolico(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_ROTULO", color=7)
    dxf.add_layer("LINEAS_AC_TRIFASICAS", color=1)
    dxf.add_layer("RECTIFICACION_Y_MPPT", color=4)
    dxf.add_layer("DUMP_LOAD_FRENO", color=2)
    dxf.add_layer("LINEAS_DC_BATERIA", color=3)
    dxf.add_layer("CONTROL_DOMOTICA", color=6)
    dxf.add_layer("TEXTO_ROTULOS", color=7)

    dxf.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf.add_rect(240, 10, 170, 40, layer="MARCO_ROTULO")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", 245, 38, height=4.0, layer="TEXTO_ROTULOS")
    dxf.add_text("ESQUEMA DE POTENCIA: AEROGENERADOR ARCHIMEDES MK9", 245, 28, height=2.4, layer="TEXTO_ROTULOS")
    dxf.add_text("PMSG 48V AC -> Rectificador -> MPPT Eólico -> Freno PWM -> LiFePO4", 245, 18, height=1.8, layer="TEXTO_ROTULOS")

    # Generador PMSG
    dxf.add_circle(60, 200, 25, layer="LINEAS_AC_TRIFASICAS")
    dxf.add_text("PMSG TRIFÁSICO", 40, 203, height=2.4, layer="TEXTO_ROTULOS")
    dxf.add_text("700W Nom / 1.5kW Pico", 38, 195, height=1.8, layer="TEXTO_ROTULOS")

    # 3 Fases AC (U, V, W)
    dxf.add_line(85, 210, 130, 210, layer="LINEAS_AC_TRIFASICAS")
    dxf.add_line(85, 200, 130, 200, layer="LINEAS_AC_TRIFASICAS")
    dxf.add_line(85, 190, 130, 190, layer="LINEAS_AC_TRIFASICAS")
    dxf.add_text("FASES U, V, W (48V AC Variable)", 87, 216, height=1.8, layer="TEXTO_ROTULOS")

    # Contactor de Cortocircuito de Seguridad (Freno de Emergencia)
    dxf.add_rect(130, 175, 35, 45, layer="CONTROL_DOMOTICA")
    dxf.add_text("CONTACTOR FRENO", 132, 205, height=1.8, layer="TEXTO_ROTULOS")
    dxf.add_text("Cortocircuito AC", 133, 198, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Disparo v > 18 m/s", 133, 190, height=1.5, layer="TEXTO_ROTULOS")

    # Rectificador Síncrono Trifásico
    dxf.add_line(165, 200, 190, 200, layer="LINEAS_AC_TRIFASICAS")
    dxf.add_rect(190, 175, 45, 50, layer="RECTIFICACION_Y_MPPT")
    dxf.add_text("PUENTE RECTIFICADOR", 193, 212, height=2.0, layer="TEXTO_ROTULOS")
    dxf.add_text("SCHOTTKY TRIFÁSICO", 193, 204, height=1.8, layer="TEXTO_ROTULOS")
    dxf.add_text("100A / 100V Low-Vf", 194, 194, height=1.6, layer="TEXTO_ROTULOS")

    # Bus DC intermedio
    dxf.add_line(235, 210, 270, 210, layer="LINEAS_DC_BATERIA")
    dxf.add_line(235, 190, 270, 190, layer="LINEAS_DC_BATERIA")

    # Controlador MPPT Eólico y Regulador de Carga
    dxf.add_rect(270, 160, 60, 65, layer="RECTIFICACION_Y_MPPT")
    dxf.add_text("CONTROLADOR MPPT EÓLICO", 273, 212, height=2.0, layer="TEXTO_ROTULOS")
    dxf.add_text("Seguimiento Curva P(w)", 275, 204, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Salida DC 48V (54.4V Float)", 273, 194, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Canal PWM Dump-Load", 275, 184, height=1.6, layer="TEXTO_ROTULOS")

    # Resistencia Dump Load de Frenado Térmico
    dxf.add_line(300, 160, 300, 125, layer="DUMP_LOAD_FRENO")
    dxf.add_rect(275, 80, 50, 45, layer="DUMP_LOAD_FRENO")
    dxf.add_text("DUMP LOAD (1.5 kW)", 278, 112, height=2.0, layer="TEXTO_ROTULOS")
    dxf.add_text("Banco Resistencias 48V", 278, 103, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Disipación en Exceso Eólico", 276, 94, height=1.5, layer="TEXTO_ROTULOS")

    # Salida hacia Banco de Baterías LiFePO4
    dxf.add_line(330, 205, 390, 205, layer="LINEAS_DC_BATERIA")
    dxf.add_line(330, 185, 390, 185, layer="LINEAS_DC_BATERIA")
    dxf.add_rect(360, 175, 25, 40, layer="LINEAS_DC_BATERIA")
    dxf.add_text("FUSIBLE DC 40A", 362, 198, height=1.5, layer="TEXTO_ROTULOS")
    dxf.add_text("HACIA BUS 48V LiFePO4", 335, 218, height=2.0, layer="TEXTO_ROTULOS")

    dxf.save()

    # 2. GENERACIÓN SVG
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 700" width="100%" height="100%" style="background:#11111b; font-family:sans-serif;">
  <defs>
    <style>
      .title {{ fill: #cdd6f4; font-size: 20px; font-weight: bold; }}
      .sub {{ fill: #89b4fa; font-size: 13px; }}
      .box {{ fill: #1e1e2e; stroke: #45475a; stroke-width: 2; rx: 6; }}
      .lbl {{ fill: #cdd6f4; font-size: 11px; }}
      .lbl-bold {{ fill: #ffffff; font-size: 12px; font-weight: bold; }}
      .wire-ac {{ stroke: #fab387; stroke-width: 3; fill: none; }}
      .wire-dc {{ stroke: #a6e3a1; stroke-width: 3.5; fill: none; }}
      .wire-dump {{ stroke: #f38ba8; stroke-width: 2.5; stroke-dasharray: 4; fill: none; }}
    </style>
  </defs>

  <!-- Marco -->
  <rect x="20" y="20" width="1060" height="660" fill="none" stroke="#313244" stroke-width="2" rx="10"/>

  <!-- Encabezado -->
  <text x="50" y="60" class="title">AEROGENERADOR HELICOIDAL ARCHIMEDES MK9 | ESQUEMA DE POTENCIA Y FRENADO</text>
  <text x="50" y="85" class="sub">Generador PMSG 48V AC | Rectificación Síncrona | MPPT Eólico Cúbico | Freno Electrónico Dump-Load</text>

  <!-- 1. Generador PMSG -->
  <circle cx="140" cy="250" r="60" fill="#181825" stroke="#fab387" stroke-width="3"/>
  <text x="105" y="245" class="lbl-bold" style="fill:#fab387;">PMSG EÓLICO</text>
  <text x="100" y="265" class="lbl" style="font-size:9.5px;">Archimedes MK9</text>
  <text x="95" y="280" class="lbl" style="font-size:9px;">700W Nom / 1.5kW Pico</text>

  <!-- Fases AC -->
  <line x1="200" y1="230" x2="310" y2="230" class="wire-ac"/>
  <line x1="200" y1="250" x2="310" y2="250" class="wire-ac"/>
  <line x1="200" y1="270" x2="310" y2="270" class="wire-ac"/>
  <text x="215" y="220" class="lbl" style="fill:#fab387; font-size:10px;">Líneas U, V, W (Trifásico AC)</text>

  <!-- Contactor de Freno de Emergencia -->
  <rect x="310" y="205" width="120" height="90" class="box" stroke="#f38ba8"/>
  <text x="325" y="235" class="lbl-bold" style="fill:#f38ba8;">FRENO DE PARADA</text>
  <text x="325" y="255" class="lbl" style="font-size:9.5px;">Cortocircuito Trifásico</text>
  <text x="325" y="275" class="lbl" style="font-size:9px; fill:#a6adc8;">Disparo por ráfaga &gt;18 m/s</text>

  <!-- Conexión hacia Rectificador -->
  <line x1="430" y1="250" x2="490" y2="250" class="wire-ac"/>

  <!-- 2. Rectificador Trifásico -->
  <rect x="490" y="190" width="140" height="120" class="box" stroke="#89b4fa"/>
  <text x="505" y="225" class="lbl-bold" style="fill:#89b4fa;">RECTIFICADOR</text>
  <text x="505" y="245" class="lbl" style="font-size:10px;">Puente Diodos Schottky</text>
  <text x="505" y="265" class="lbl" style="font-size:9.5px;">100A / 100V Low-Vf</text>
  <text x="505" y="285" class="lbl" style="font-size:9px; fill:#a6adc8;">Rizado &lt; 2% con filtro LC</text>

  <!-- Bus DC Rectificado -->
  <line x1="630" y1="235" x2="700" y2="235" class="wire-dc"/>
  <line x1="630" y1="265" x2="700" y2="265" stroke="#f38ba8" stroke-width="3"/>
  <text x="640" y="225" class="lbl" style="font-size:9px; fill:#a6e3a1;">DC+ (0-60V)</text>
  <text x="640" y="285" class="lbl" style="font-size:9px; fill:#f38ba8;">DC-</text>

  <!-- 3. MPPT Eólico y Gestor de Freno -->
  <rect x="700" y="180" width="180" height="140" class="box" stroke="#a6e3a1"/>
  <text x="715" y="215" class="lbl-bold" style="fill:#a6e3a1;">MPPT EÓLICO &amp; CARGADOR</text>
  <text x="715" y="235" class="lbl" style="font-size:10px;">Algoritmo Curva de Potencia</text>
  <text x="715" y="255" class="lbl" style="font-size:9.5px;">Carga Multietapa 48V LiFePO4</text>
  <text x="715" y="275" class="lbl" style="font-size:9.5px; fill:#fab387;">Salida PWM Freno Dinámico</text>
  <text x="715" y="295" class="lbl" style="font-size:9px; fill:#a6adc8;">Telemetría Modbus RTU a HA</text>

  <!-- Canal de Dump Load hacia abajo -->
  <line x1="790" y1="320" x2="790" y2="440" class="wire-dump"/>

  <!-- 4. Resistencia Dump Load -->
  <rect x="710" y="440" width="160" height="110" class="box" stroke="#f38ba8"/>
  <text x="725" y="475" class="lbl-bold" style="fill:#f38ba8;">DUMP LOAD (1.5 kW)</text>
  <text x="725" y="495" class="lbl" style="font-size:10px;">Banco Resistivo Calefactor</text>
  <text x="725" y="515" class="lbl" style="font-size:9px; fill:#a6adc8;">Disipa energía sobrante cuando</text>
  <text x="725" y="530" class="lbl" style="font-size:9px; fill:#a6adc8;">el banco LiFePO4 está al 100%</text>

  <!-- Salida hacia Batería -->
  <line x1="880" y1="235" x2="980" y2="235" class="wire-dc"/>
  <line x1="880" y1="265" x2="980" y2="265" stroke="#f38ba8" stroke-width="3"/>
  <rect x="980" y="200" width="80" height="90" class="box" stroke="#a6e3a1"/>
  <text x="990" y="235" class="lbl-bold" style="fill:#a6e3a1; font-size:10px;">BANCO ESS</text>
  <text x="990" y="255" class="lbl" style="font-size:9px;">48V LiFePO4</text>
  <text x="990" y="275" class="lbl" style="font-size:9px;">(Bus Común)</text>

</svg>
"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Diagrama eólico generado: DXF={dxf_path}, SVG={svg_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dxf_target = os.path.join(base_dir, "01_energia_renovable_y_potencia/01_aerogenerador_archimedes_mk9/electrico/esquema_potencia_eolico.dxf")
    svg_target = os.path.join(base_dir, "01_energia_renovable_y_potencia/01_aerogenerador_archimedes_mk9/electrico/esquema_potencia_eolico.svg")
    generar_diagrama_eolico(dxf_target, svg_target)

