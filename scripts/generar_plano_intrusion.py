#!/usr/bin/env python3
"""
Generador de Plano CAD 2D: Sistema de Intrusión Perimetral, Barreras AIR y Sirena Exterior
Formatos de salida: DXF (AutoCAD R12) y SVG vectorial
Módulo: 03_seguridad_y_control_acceso/08_intrusion_perimetral_sensores_y_sirena/mecanico
"""

import os
import sys

# Asegurar path para importar SimpleDXF
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generar_planos_dxf import SimpleDXF

def generar_plano_intrusion(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_ROTULO", color=7)
    dxf.add_layer("PERIMETRO_PARCELA", color=8)
    dxf.add_layer("ESTRUCTURA_VIVIENDA", color=8)
    dxf.add_layer("BARRERAS_AIR", color=1)
    dxf.add_layer("HACES_INFRARROJOS", color=1)
    dxf.add_layer("SENSORES_MAGNETICOS", color=3)
    dxf.add_layer("ROTURA_CRISTAL", color=2)
    dxf.add_layer("SIRENA_EXTERIOR", color=6)
    dxf.add_layer("TEXTO_NOTAS", color=7)

    # Marco y Cajetín A3 (420 x 297 mm)
    dxf.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf.add_rect(210, 10, 200, 45, layer="MARCO_ROTULO")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", 215, 45, height=4.0, layer="TEXTO_NOTAS")
    dxf.add_text("PLANO DE SEGURIDAD PERIMETRAL, BARRERAS AIR Y SIRENA EXTERIOR", 215, 36, height=2.0, layer="TEXTO_NOTAS")
    dxf.add_text("Barreras AIR Haz Cuadruple 60m | Contactos Reed Ocultos | Rotura Cristal Dual", 215, 26, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Sirena 120dB IP65 Autoalimentada | Lazo Supervisado DEOL 2x2.2kΩ | Alarmo HA", 215, 16, height=1.4, layer="TEXTO_NOTAS")

    # Parcela Exterior 20 x 20 m (Escala s=9.5, origen en X=20, Y=70)
    ox, oy = 20.0, 70.0
    sp = 9.5  # escala parcela

    # Vallado de la Parcela (20 x 20 m -> 190 x 190 mm)
    dxf.add_rect(ox, oy, 20.0 * sp, 20.0 * sp, layer="PERIMETRO_PARCELA")
    dxf.add_text("VALLADO PERIMETRAL DE PARCELA (20 x 20 m)", ox + 5, oy + 20.0*sp + 4, height=1.8, layer="TEXTO_NOTAS")

    # Vivienda Centrada (10 x 10 m en X=5 a 15m, Y=5 a 15m)
    vx, vy = ox + 5.0 * sp, oy + 5.0 * sp
    dxf.add_rect(vx, vy, 10.0 * sp, 10.0 * sp, layer="ESTRUCTURA_VIVIENDA")
    dxf.add_text("VIVIENDA (10 x 10 m)", vx + 25, vy + 45, height=2.0, layer="TEXTO_NOTAS")

    # 1. Cuatro Columnas de Barreras Infrarrojas Activas (AIR) en las esquinas de la parcela
    # AIR-01: Esquina Suroeste (X=1.0m, Y=1.0m)
    c1_x, c1_y = ox + 1.0 * sp, oy + 1.0 * sp
    dxf.add_circle(c1_x, c1_y, 3.5, layer="BARRERAS_AIR")
    dxf.add_text("AIR-01", c1_x - 12, c1_y - 6, height=1.4, layer="BARRERAS_AIR")

    # AIR-02: Esquina Sureste (X=19.0m, Y=1.0m)
    c2_x, c2_y = ox + 19.0 * sp, oy + 1.0 * sp
    dxf.add_circle(c2_x, c2_y, 3.5, layer="BARRERAS_AIR")
    dxf.add_text("AIR-02", c2_x + 5, c2_y - 6, height=1.4, layer="BARRERAS_AIR")

    # AIR-03: Esquina Noreste (X=19.0m, Y=19.0m)
    c3_x, c3_y = ox + 19.0 * sp, oy + 19.0 * sp
    dxf.add_circle(c3_x, c3_y, 3.5, layer="BARRERAS_AIR")
    dxf.add_text("AIR-03", c3_x + 5, c3_y + 4, height=1.4, layer="BARRERAS_AIR")

    # AIR-04: Esquina Noroeste (X=1.0m, Y=19.0m)
    c4_x, c4_y = ox + 1.0 * sp, oy + 19.0 * sp
    dxf.add_circle(c4_x, c4_y, 3.5, layer="BARRERAS_AIR")
    dxf.add_text("AIR-04", c4_x - 12, c4_y + 4, height=1.4, layer="BARRERAS_AIR")

    # Haces infrarrojos perimetrales activos (Líneas perimetrales)
    dxf.add_line(c1_x, c1_y, c2_x, c2_y, layer="HACES_INFRARROJOS")
    dxf.add_line(c2_x, c2_y, c3_x, c3_y, layer="HACES_INFRARROJOS")
    dxf.add_line(c3_x, c3_y, c4_x, c4_y, layer="HACES_INFRARROJOS")
    dxf.add_line(c4_x, c4_y, c1_x, c1_y, layer="HACES_INFRARROJOS")
    dxf.add_text("Anillo Infrarrojo Cuádruple Activo (Protección Perimetral Exterior)", ox + 35, oy + 8, height=1.5, layer="HACES_INFRARROJOS")

    # 2. Contactos Magnéticos Reed Ocultos (Puertas y Ventanas)
    # Puerta Principal (Fachada Sur, X=5m)
    dxf.add_rect(vx + 4.5 * sp, vy - 2, 1.0 * sp, 4, layer="SENSORES_MAGNETICOS")
    dxf.add_text("MAG-01 (Puerta Pral)", vx + 3.0 * sp, vy - 7, height=1.3, layer="SENSORES_MAGNETICOS")

    # Ventanales Salón (Fachada Oeste)
    dxf.add_rect(vx - 2, vy + 2.0 * sp, 4, 2.0 * sp, layer="SENSORES_MAGNETICOS")
    dxf.add_text("MAG-02", vx - 18, vy + 3.0 * sp, height=1.3, layer="SENSORES_MAGNETICOS")

    # Ventanales Dormitorios (Fachada Este)
    dxf.add_rect(vx + 10.0 * sp - 2, vy + 3.0 * sp, 4, 3.0 * sp, layer="SENSORES_MAGNETICOS")
    dxf.add_text("MAG-03", vx + 10.0 * sp + 5, vy + 4.5 * sp, height=1.3, layer="SENSORES_MAGNETICOS")

    # 3. Detectores Acústicos de Rotura de Cristal (GB)
    dxf.add_circle(vx + 2.0 * sp, vy + 2.5 * sp, 3.0, layer="ROTURA_CRISTAL")
    dxf.add_text("GB-01 (Salón)", vx + 2.0 * sp - 8, vy + 2.5 * sp + 5, height=1.3, layer="ROTURA_CRISTAL")

    dxf.add_circle(vx + 5.0 * sp, vy + 5.0 * sp, 3.0, layer="ROTURA_CRISTAL")
    dxf.add_text("GB-02 (Lucernario)", vx + 5.0 * sp - 10, vy + 5.0 * sp + 5, height=1.3, layer="ROTURA_CRISTAL")

    # 4. Sirena Exterior 120 dB con Strobe
    dxf.add_rect(vx + 9.5 * sp, vy - 6, 8, 6, layer="SIRENA_EXTERIOR")
    dxf.add_text("SIRENA 120dB + STROBE", vx + 7.0 * sp, vy - 12, height=1.4, layer="SIRENA_EXTERIOR")

    # 5. Esquema Lazo Supervisado DEOL (Derecha X=230, Y=140)
    sx, sy = 240.0, 160.0
    dxf.add_text("ARQUITECTURA DE LAZO SUPERVISADO DEOL (2x 2.2 kΩ)", sx - 15, sy + 45, height=2.0, layer="TEXTO_NOTAS")

    dxf.add_rect(sx - 15, sy + 5, 80, 32, layer="ESTRUCTURA_VIVIENDA")
    dxf.add_text("ESTADOS DE ZONA BALANCEADA:", sx - 10, sy + 30, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("• Reposo (Normal): R = 2.2 kΩ (Contacto cerrado)", sx - 10, sy + 22, height=1.3, layer="SENSORES_MAGNETICOS")
    dxf.add_text("• Alarma (Apertura): R = 4.4 kΩ (Contacto abierto)", sx - 10, sy + 15, height=1.3, layer="BARRERAS_AIR")
    dxf.add_text("• Sabotaje (Tamper): R = Infinito o R = 0 Ω", sx - 10, sy + 8, height=1.3, layer="SIRENA_EXTERIOR")

    dxf.add_rect(sx - 15, sy - 55, 80, 50, layer="ESTRUCTURA_VIVIENDA")
    dxf.add_text("MODOS DE SEGURIDAD ALARMO (HA):", sx - 10, sy - 12, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("1. MODO FUERA (Armado Total):", sx - 10, sy - 20, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("   - Barreras AIR + Reed + Rotura Cristal + Cámaras", sx - 5, sy - 27, height=1.2, layer="BARRERAS_AIR")
    dxf.add_text("2. MODO NOCHE (Perimetral):", sx - 10, sy - 34, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("   - Barreras AIR + Reed + Lucernario (Interiores OFF)", sx - 5, sy - 41, height=1.2, layer="SENSORES_MAGNETICOS")
    dxf.add_text("3. DISUASION ACTIVA:", sx - 10, sy - 47, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("   - Strobe + Sirena + Luces exteriores parpadeo", sx - 5, sy - 53, height=1.2, layer="SIRENA_EXTERIOR")

    dxf.save()

    # 2. GENERACIÓN SVG VECTORIAL
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 297" width="100%" height="100%" style="background-color: #171c26; font-family: monospace;">
  <defs>
    <style>
      .marco {{ stroke: #454d66; stroke-width: 1.0; fill: none; }}
      .parcela {{ stroke: #5c677d; stroke-width: 1.4; fill: #1e2533; stroke-dasharray: 4,2; }}
      .vivienda {{ stroke: #8d99ae; stroke-width: 1.6; fill: #2b3445; }}
      .haz-air {{ stroke: #ef233c; stroke-width: 1.4; stroke-dasharray: 2,1; fill: none; }}
      .col-air {{ stroke: #d90429; stroke-width: 1.2; fill: #ff4d6d; }}
      .reed {{ stroke: #06d6a0; stroke-width: 1.2; fill: #1b4332; }}
      .rotura {{ stroke: #ffd166; stroke-width: 1.2; fill: #f3722c; }}
      .sirena {{ stroke: #7209b7; stroke-width: 1.4; fill: #f72585; }}
      .bloque {{ stroke: #4361ee; stroke-width: 1.2; fill: #1d2d44; }}
      .txt-title {{ fill: #ffffff; font-size: 4px; font-weight: bold; }}
      .txt-sub {{ fill: #00f0ff; font-size: 2.2px; font-weight: bold; }}
      .txt-body {{ fill: #cad2c5; font-size: 1.6px; }}
      .txt-alert {{ fill: #ff4d6d; font-size: 1.4px; font-weight: bold; }}
      .txt-ok {{ fill: #06d6a0; font-size: 1.3px; }}
    </style>
  </defs>

  <!-- Marco A3 -->
  <rect x="5" y="5" width="410" height="287" class="marco"/>
  <rect x="210" y="242" width="200" height="45" class="marco"/>
  <text x="215" y="254" class="txt-title">OPEN-SOURCE-DOMOTICS</text>
  <text x="215" y="262" class="txt-sub">PLANO DE SEGURIDAD PERIMETRAL, BARRERAS AIR Y SIRENA</text>
  <text x="215" y="271" class="txt-body">Barreras AIR Haz Cuádruple 60m | Contactos Reed Ocultos | Rotura Cristal Dual</text>
  <text x="215" y="279" class="txt-body">Sirena 120dB IP65 Autoalimentada | Lazo Supervisado DEOL 2x2.2kΩ | Alarmo HA</text>

  <!-- Parcela y Anillo Infrarrojo -->
  <g id="terreno">
    <rect x="{ox}" y="{297 - (oy + 20.0*sp)}" width="{20.0*sp}" height="{20.0*sp}" class="parcela"/>
    <text x="{ox + 5}" y="{297 - (oy + 20.0*sp + 4)}" class="txt-sub">VALLADO PERIMETRAL (20 x 20 m)</text>

    <!-- Vivienda Centrada -->
    <rect x="{vx}" y="{297 - (vy + 10.0*sp)}" width="{10.0*sp}" height="{10.0*sp}" class="vivienda"/>
    <text x="{vx + 15}" y="{297 - (vy + 5.0*sp)}" class="txt-sub">VIVIENDA (10x10 m)</text>

    <!-- Haces AIR Perimetrales -->
    <line x1="{c1_x}" y1="{297 - c1_y}" x2="{c2_x}" y2="{297 - c2_y}" class="haz-air"/>
    <line x1="{c2_x}" y1="{297 - c2_y}" x2="{c3_x}" y2="{297 - c3_y}" class="haz-air"/>
    <line x1="{c3_x}" y1="{297 - c3_y}" x2="{c4_x}" y2="{297 - c4_y}" class="haz-air"/>
    <line x1="{c4_x}" y1="{297 - c4_y}" x2="{c1_x}" y2="{297 - c1_y}" class="haz-air"/>

    <!-- Columnas AIR -->
    <circle cx="{c1_x}" cy="{297 - c1_y}" r="4" class="col-air"/>
    <circle cx="{c2_x}" cy="{297 - c2_y}" r="4" class="col-air"/>
    <circle cx="{c3_x}" cy="{297 - c3_y}" r="4" class="col-air"/>
    <circle cx="{c4_x}" cy="{297 - c4_y}" r="4" class="col-air"/>
    <text x="{c1_x - 10}" y="{297 - (c1_y - 8)}" class="txt-alert">AIR-01</text>
    <text x="{c2_x + 5}" y="{297 - (c2_y - 8)}" class="txt-alert">AIR-02</text>
    <text x="{c3_x + 5}" y="{297 - (c3_y + 8)}" class="txt-alert">AIR-03</text>
    <text x="{c4_x - 10}" y="{297 - (c4_y + 8)}" class="txt-alert">AIR-04</text>

    <!-- Sensores Reed en accesos -->
    <rect x="{vx + 4.5*sp}" y="{297 - (vy + 2)}" width="{1.0*sp}" height="4" class="reed"/>
    <text x="{vx + 2.0*sp}" y="{297 - (vy - 8)}" class="txt-ok">Puerta Principal</text>

    <!-- Sensor Rotura Cristal -->
    <circle cx="{vx + 2.0*sp}" cy="{297 - (vy + 2.5*sp)}" r="3" class="rotura"/>
    <text x="{vx + 1.0*sp}" y="{297 - (vy + 2.5*sp + 6)}" class="txt-alert">Rotura Cristal</text>

    <!-- Sirena Exterior Strobe -->
    <rect x="{vx + 9.5*sp}" y="{297 - (vy - 2)}" width="8" height="6" class="sirena"/>
    <text x="{vx + 7.5*sp}" y="{297 - (vy - 10)}" class="txt-alert">SIRENA 120dB</text>
  </g>

  <!-- Lógica Alarmo (Derecha) -->
  <g id="modos_alarmo">
    <text x="215" y="45" class="txt-sub">SUPERVISIÓN DE LAZOS Y MODOS DE ALARMA</text>

    <rect x="215" y="55" width="190" height="75" class="bloque" rx="2"/>
    <text x="220" y="70" class="txt-sub">SUPERVISIÓN DE DOBLE FIN DE LÍNEA (DEOL):</text>
    <text x="225" y="80" class="txt-body">• Reposo Normal: R = 2.2 kΩ (Lazo cerrado)</text>
    <text x="225" y="88" class="txt-body">• Alarma Intrusión: R = 4.4 kΩ (Contacto abierto)</text>
    <text x="225" y="96" class="txt-alert">• Sabotaje Tamper: R = ∞ (Cable cortado) o R = 0 Ω (Cortocircuito)</text>
    <text x="225" y="104" class="txt-body">• Inmunidad electromagnética contra interferencias de radio</text>

    <rect x="215" y="140" width="190" height="90" class="bloque" rx="2"/>
    <text x="220" y="155" class="txt-sub">PERFILES DE SEGURIDAD EN HOME ASSISTANT:</text>
    <text x="225" y="165" class="txt-body">• MODO FUERA DE CASA (Armado Total):</text>
    <text x="230" y="173" class="txt-body">  Barreras exteriores + Puertas + Ventanas + Cámaras Frigate</text>
    <text x="225" y="183" class="txt-body">• MODO NOCHE (Armado Perimetral):</text>
    <text x="230" y="191" class="txt-body">  Barreras exteriores + Accesos cerrados (Libre paso interior)</text>
    <text x="225" y="201" class="txt-alert">• RESPUESTA DISUASIVA AUTOMÁTICA:</text>
    <text x="230" y="209" class="txt-body">  Sirena 120dB + Flash Strobe + Focos perimetrales intermitentes</text>
  </g>
</svg>
"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Plano CAD 2D DXF generado en: {dxf_path}")
    print(f"Plano vectorial SVG generado en: {svg_path}")

if __name__ == "__main__":
    dxf_out = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/08_intrusion_perimetral_sensores_y_sirena/mecanico/plano_seguridad_perimetral_intrusion.dxf"
    svg_out = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/08_intrusion_perimetral_sensores_y_sirena/mecanico/plano_seguridad_perimetral_intrusion.svg"
    generar_plano_intrusion(dxf_out, svg_out)
