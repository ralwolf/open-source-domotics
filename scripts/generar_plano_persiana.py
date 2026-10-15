#!/usr/bin/env python3
"""
Generador de Plano CAD 2D: Mecanismo de Persiana Enrollable y Control Motorizado
Formatos de salida: DXF (AutoCAD R12) y SVG vectorial
Módulo: 03_seguridad_y_control_acceso/04_cortinas_y_persianas_motorizadas/mecanico
"""

import os
import sys

# Asegurar path para importar SimpleDXF
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generar_planos_dxf import SimpleDXF

def generar_plano_persiana(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_ROTULO", color=7)
    dxf.add_layer("EJE_OCTOGONAL", color=8)
    dxf.add_layer("MOTOR_TUBULAR", color=1)
    dxf.add_layer("LAMAS_CAJON", color=4)
    dxf.add_layer("CIRCUITO_ELECTRICO", color=3)
    dxf.add_layer("COTAS_COTACION", color=2)
    dxf.add_layer("TEXTO_NOTAS", color=7)

    # Marco y Cajetín A3 (420 x 297 mm)
    dxf.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf.add_rect(210, 10, 200, 45, layer="MARCO_ROTULO")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", 215, 45, height=4.0, layer="TEXTO_NOTAS")
    dxf.add_text("MECANISMO Y CONTROL DE PERSIANA BIOCLIMATICA MOTORIZADA", 215, 36, height=2.0, layer="TEXTO_NOTAS")
    dxf.add_text("Eje Octogonal D60 | Motor Tubular 20Nm 230VAC | Interlock por Hardware", 215, 26, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Lamas Aluminio Térmico 45mm | Control Solar por Azimut y Elevación", 215, 16, height=1.4, layer="TEXTO_NOTAS")

    # Vista 1: Sección Longitudinal del Eje y Motor (Arriba)
    ex, ey = 30.0, 200.0
    # Eje total longitud 340 mm en plano (escala reducida)
    dxf.add_rect(ex, ey, 340, 30, layer="EJE_OCTOGONAL")
    dxf.add_text("EJE OCTOGONAL ACERO GALVANIZADO D=60mm (L=1200mm)", ex + 40, ey + 35, height=1.8, layer="TEXTO_NOTAS")

    # Motor tubular embutido a la derecha (longitud 160 mm en dibujo)
    dxf.add_rect(ex + 180, ey + 4, 155, 22, layer="MOTOR_TUBULAR")
    dxf.add_text("MOTOR TUBULAR 20Nm (EMBUTIDO)", ex + 185, ey + 12, height=1.5, layer="TEXTO_NOTAS")
    # Corona de arrastre
    dxf.add_rect(ex + 185, ey + 2, 10, 26, layer="MOTOR_TUBULAR")
    # Cabeza con finales de carrera
    dxf.add_rect(ex + 335, ey - 2, 12, 34, layer="MOTOR_TUBULAR")
    dxf.add_text("Cabeza Motor", ex + 325, ey + 38, height=1.3, layer="TEXTO_NOTAS")

    # Contera y rodamiento a la izquierda
    dxf.add_rect(ex - 15, ey + 5, 15, 20, layer="EJE_OCTOGONAL")
    dxf.add_rect(ex - 22, ey + 11, 7, 8, layer="EJE_OCTOGONAL")
    dxf.add_text("Rodamiento / Contera", ex - 28, ey - 8, height=1.3, layer="TEXTO_NOTAS")

    # Cotas Eje
    dxf.add_line(ex, ey - 15, ex + 340, ey - 15, layer="COTAS_COTACION")
    dxf.add_text("Luz de Hueco Ventana: 1200 mm", ex + 110, ey - 13, height=1.8, layer="COTAS_COTACION")

    # Vista 2: Sección Transversal de Cajón y Guía Lateral (Abajo Izquierda X=40, Y=70)
    cx, cy = 60.0, 80.0
    # Cajón Monoblock 185 x 185 mm (escala 0.35)
    dxf.add_rect(cx, cy, 65, 65, layer="LAMAS_CAJON")
    dxf.add_text("CAJON MONOBLOCK TERMOACUSTICO", cx - 5, cy + 72, height=1.8, layer="TEXTO_NOTAS")
    # Eje y enrollamiento
    dxf.add_circle(cx + 32, cy + 32, 12, layer="EJE_OCTOGONAL")
    dxf.add_circle(cx + 32, cy + 32, 24, layer="LAMAS_CAJON")
    # Lamas cayendo por la guía
    dxf.add_line(cx + 8, cy + 32, cx + 8, cy - 40, layer="LAMAS_CAJON")
    dxf.add_line(cx + 12, cy + 32, cx + 12, cy - 40, layer="LAMAS_CAJON")
    dxf.add_text("Guía con felpudo silencioso", cx + 15, cy - 20, height=1.4, layer="TEXTO_NOTAS")

    # Vista 3: Esquema Eléctrico con Interbloqueo Físico (Abajo Derecha X=230, Y=100)
    px, py = 240.0, 110.0
    dxf.add_text("ESQUEMA ELECTRICO CON INTERBLOQUEO MECANICO/HARDWARE", px - 15, py + 55, height=2.2, layer="TEXTO_NOTAS")

    # Microcontrolador ESP32
    dxf.add_rect(px - 15, py + 10, 50, 35, layer="CIRCUITO_ELECTRICO")
    dxf.add_text("ESP32-WROOM-32E", px - 10, py + 36, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("GPIO18: Relé Power ON", px - 10, py + 26, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("GPIO19: Relé Dirección", px - 10, py + 18, height=1.3, layer="TEXTO_NOTAS")

    # Módulo Relés SPDT con Interbloqueo Imposible de Cortocircuito
    dxf.add_rect(px + 45, py + 10, 65, 35, layer="CIRCUITO_ELECTRICO")
    dxf.add_text("ETAPA DE POTENCIA 230VAC", px + 48, py + 38, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("K1: Alimentación Principal (NO)", px + 48, py + 30, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("K2: Conmutador SPDT (Subir/Bajar)", px + 48, py + 22, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("✓ CERO RIESGO DE FASE SIMULTANEA", px + 48, py + 14, height=1.2, layer="TEXTO_NOTAS")

    # Conexión hacia Motor Tubular (4 hilos)
    dxf.add_rect(px + 120, py + 5, 45, 45, layer="MOTOR_TUBULAR")
    dxf.add_text("MOTOR TUBULAR", px + 122, py + 42, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("• L1: Subir (Marrón)", px + 122, py + 34, height=1.2, layer="TEXTO_NOTAS")
    dxf.add_text("• L2: Bajar (Negro)", px + 122, py + 26, height=1.2, layer="TEXTO_NOTAS")
    dxf.add_text("• N: Neutro (Azul)", px + 122, py + 18, height=1.2, layer="TEXTO_NOTAS")
    dxf.add_text("• PE: Tierra (Verde/Am)", px + 122, py + 10, height=1.2, layer="TEXTO_NOTAS")

    dxf.add_line(px + 110, py + 30, px + 120, py + 30, layer="CIRCUITO_ELECTRICO")

    dxf.save()

    # 2. GENERACIÓN SVG VECTORIAL
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 297" width="100%" height="100%" style="background-color: #1a1e29; font-family: monospace;">
  <defs>
    <style>
      .marco {{ stroke: #455066; stroke-width: 1.0; fill: none; }}
      .eje {{ stroke: #90a4ae; stroke-width: 1.5; fill: #2c3440; }}
      .motor {{ stroke: #e63946; stroke-width: 1.4; fill: #451a20; }}
      .cajon {{ stroke: #48cae4; stroke-width: 1.2; fill: #1c2e3d; }}
      .bloque {{ stroke: #52b788; stroke-width: 1.2; fill: #193325; }}
      .cable {{ stroke: #ffd166; stroke-width: 1.2; stroke-dasharray: 3,2; fill: none; }}
      .txt-title {{ fill: #ffffff; font-size: 4px; font-weight: bold; }}
      .txt-sub {{ fill: #00f0ff; font-size: 2.2px; font-weight: bold; }}
      .txt-body {{ fill: #cad2c5; font-size: 1.6px; }}
      .txt-cota {{ fill: #f4a261; font-size: 1.8px; }}
      .txt-ok {{ fill: #2a9d8f; font-size: 1.4px; font-weight: bold; }}
    </style>
  </defs>

  <!-- Marco A3 -->
  <rect x="5" y="5" width="410" height="287" class="marco"/>
  <rect x="210" y="242" width="200" height="45" class="marco"/>
  <text x="215" y="254" class="txt-title">OPEN-SOURCE-DOMOTICS</text>
  <text x="215" y="262" class="txt-sub">MECANISMO Y CONTROL DE PERSIANA BIOCLIMÁTICA</text>
  <text x="215" y="271" class="txt-body">Eje Octogonal D60 | Motor Tubular 20Nm 230VAC | Interlock por Hardware</text>
  <text x="215" y="279" class="txt-body">Lamas Aluminio Térmico 45mm | Control Solar por Azimut y Elevación</text>

  <!-- Sección Longitudinal Eje y Motor -->
  <g id="eje_motor">
    <text x="35" y="45" class="txt-sub">SECCIÓN LONGITUDINAL DEL EJE Y MOTOR TUBULAR</text>
    
    <!-- Eje Octogonal -->
    <rect x="{ex}" y="65" width="340" height="30" class="eje"/>
    <text x="{ex + 30}" y="82" class="txt-body">Eje Octogonal Acero Galvanizado Ø 60 mm (L = 1200 mm)</text>

    <!-- Motor Embutido -->
    <rect x="{ex + 180}" y="69" width="155" height="22" class="motor"/>
    <text x="{ex + 190}" y="82" class="txt-title" font-size="2">MOTOR TUBULAR 20 Nm</text>

    <!-- Corona de Arrastre -->
    <rect x="{ex + 185}" y="67" width="10" height="26" fill="#f4a261" stroke="#e76f51"/>
    <!-- Cabeza Motor -->
    <rect x="{ex + 335}" y="63" width="12" height="34" fill="#333333" stroke="#e63946"/>

    <!-- Contera izquierda -->
    <rect x="{ex - 15}" y="70" width="15" height="20" class="eje"/>
    <rect x="{ex - 22}" y="76" width="7" height="8" fill="#cccccc"/>

    <!-- Cota -->
    <line x1="{ex}" y1="110" x2="{ex + 340}" y2="110" stroke="#f4a261" stroke-width="0.8"/>
    <text x="{ex + 120}" y="118" class="txt-cota">Luz de Ventana: 1200 mm</text>
  </g>

  <!-- Sección Cajón Monoblock -->
  <g id="cajon">
    <text x="30" y="145" class="txt-sub">SECCIÓN CAJÓN TERMOACÚSTICO</text>
    <rect x="{cx}" y="160" width="65" height="65" class="cajon" rx="2"/>
    <circle cx="{cx + 32}" cy="192" r="12" class="eje"/>
    <circle cx="{cx + 32}" cy="192" r="24" stroke="#48cae4" stroke-width="1.2" fill="none" stroke-dasharray="2,2"/>
    <line x1="{cx + 8}" y1="192" x2="{cx + 8}" y2="240" stroke="#48cae4" stroke-width="2.0"/>
    <text x="{cx + 14}" y="235" class="txt-body">Lamas Térmicas 45mm</text>
  </g>

  <!-- Diagrama Interbloqueo Hardware (Derecha) -->
  <g id="circuito">
    <text x="215" y="145" class="txt-sub">ARQUITECTURA DE POTENCIA E INTERBLOQUEO</text>

    <!-- ESP32 -->
    <rect x="215" y="160" width="60" height="45" class="bloque" rx="2"/>
    <text x="220" y="175" class="txt-sub">ESP32-S3</text>
    <text x="220" y="185" class="txt-body">• Lógica de Posición</text>
    <text x="220" y="193" class="txt-body">• Algoritmo Solar</text>

    <!-- Relés Interlock -->
    <rect x="285" y="160" width="75" height="52" class="bloque" rx="2"/>
    <text x="290" y="173" class="txt-sub">RELÉS INTERLOCK</text>
    <text x="290" y="182" class="txt-body">K1: Potencia ON/OFF</text>
    <text x="290" y="190" class="txt-body">K2: Conmutador SPDT</text>
    <text x="290" y="202" class="txt-ok">✓ IMPOSIBLE FASE DUAL</text>

    <!-- Motor 230V -->
    <rect x="370" y="160" width="40" height="52" class="motor" rx="2"/>
    <text x="373" y="175" class="txt-sub" font-size="1.8">MOTOR</text>
    <text x="373" y="184" class="txt-body">L1 (Subir)</text>
    <text x="373" y="192" class="txt-body">L2 (Bajar)</text>
    <text x="373" y="200" class="txt-body">N (Neutro)</text>
  </g>
</svg>
"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Plano CAD 2D DXF generado en: {dxf_path}")
    print(f"Plano vectorial SVG generado en: {svg_path}")

if __name__ == "__main__":
    dxf_out = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/04_cortinas_y_persianas_motorizadas/mecanico/plano_mecanismo_persiana.dxf"
    svg_out = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/04_cortinas_y_persianas_motorizadas/mecanico/plano_mecanismo_persiana.svg"
    generar_plano_persiana(dxf_out, svg_out)
