#!/usr/bin/env python3
"""
Generador de Planos CAD 2D: Fontanería (AF/ACS/Retorno) y Red de Gas Dual con Conmutación
Formatos de salida: DXF (AutoCAD R12) y SVG vectorial
Módulo: 00_diseno_arquitectonico_y_estructural/05_instalaciones_hidraulicas_y_gas/
"""

import os
import sys

# Asegurar path para importar SimpleDXF
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generar_planos_dxf import SimpleDXF

def generar_planos_fontaneria_y_gas(base_dir):
    font_dxf = os.path.join(base_dir, "planos_fontaneria", "plano_fontaneria_af_acs_retorno.dxf")
    font_svg = os.path.join(base_dir, "planos_fontaneria", "plano_fontaneria_af_acs_retorno.svg")
    gas_dxf = os.path.join(base_dir, "planos_gas_dual", "plano_gas_dual_conmutacion.dxf")
    gas_svg = os.path.join(base_dir, "planos_gas_dual", "plano_gas_dual_conmutacion.svg")

    os.makedirs(os.path.dirname(font_dxf), exist_ok=True)
    os.makedirs(os.path.dirname(gas_dxf), exist_ok=True)

    # =========================================================================
    # PLANO 1: FONTANERÍA AF, ACS, RETORNO Y SANEAMIENTO
    # =========================================================================
    dxf1 = SimpleDXF(font_dxf)
    dxf1.add_layer("MARCO_ROTULO", color=7)
    dxf1.add_layer("MUROS_VIVIENDA", color=8)
    dxf1.add_layer("TUBERIA_AGUA_FRIA", color=4)
    dxf1.add_layer("TUBERIA_ACS", color=1)
    dxf1.add_layer("TUBERIA_RETORNO_ACS", color=3)
    dxf1.add_layer("SANEAMIENTO_NEGRAS", color=6)
    dxf1.add_layer("TEXTO_NOTAS", color=7)

    # Marco A3
    dxf1.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf1.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf1.add_rect(210, 10, 200, 45, layer="MARCO_ROTULO")
    dxf1.add_text("OPEN-SOURCE-DOMOTICS", 215, 45, height=4.0, layer="TEXTO_NOTAS")
    dxf1.add_text("INSTALACION HIDRAULICA: AGUA FRIA, ACS SOLAR Y RETORNO", 215, 36, height=2.0, layer="TEXTO_NOTAS")
    dxf1.add_text("PEX-a D25/D20/D16 | Colector Manifold 1\" | Bomba Circuladora 24V", 215, 26, height=1.6, layer="TEXTO_NOTAS")
    dxf1.add_text("Separación Aguas Grises y Negras | Conducción a Biodigestor Séptico", 215, 16, height=1.4, layer="TEXTO_NOTAS")

    # Vivienda 10x10 m (X=25, Y=75, s=18.0)
    ox, oy = 25.0, 75.0
    s = 18.0
    dxf1.add_rect(ox, oy, 10.0 * s, 10.0 * s, layer="MUROS_VIVIENDA")
    dxf1.add_text("VIVIENDA 10 x 10 m", ox + 5, oy + 10.0*s + 4, height=1.8, layer="TEXTO_NOTAS")

    # Cuarto Técnico IT / Fontanería (Centro X=4.0, Y=4.0)
    cx, cy = ox + 4.0 * s, oy + 4.0 * s
    dxf1.add_rect(cx, cy, 2.5 * s, 2.5 * s, layer="MUROS_VIVIENDA")
    dxf1.add_text("CUARTO TECNICO / ACS 500L", cx + 5, cy + 38, height=1.5, layer="TEXTO_NOTAS")

    # Cocina (X=0 a 4.0, Y=6.0 a 10.0)
    dxf1.add_rect(ox, oy + 6.0 * s, 4.0 * s, 4.0 * s, layer="MUROS_VIVIENDA")
    dxf1.add_text("COCINA / LAVANDERIA", ox + 5, oy + 9.5 * s, height=1.5, layer="TEXTO_NOTAS")

    # Baño Principal (X=0 a 3.5, Y=3.5 a 6.0)
    dxf1.add_rect(ox, oy + 3.5 * s, 3.5 * s, 2.5 * s, layer="MUROS_VIVIENDA")
    dxf1.add_text("BAÑO PRINCIPAL", ox + 5, oy + 5.5 * s, height=1.5, layer="TEXTO_NOTAS")

    # Red de Tuberías desde Cuarto Técnico
    # Colector Manifold en Cuarto Técnico (cx + 10, cy + 20)
    dxf1.add_rect(cx + 8, cy + 15, 25, 12, layer="TUBERIA_AGUA_FRIA")
    dxf1.add_text("Manifold AF/ACS", cx + 5, cy + 30, height=1.3, layer="TEXTO_NOTAS")

    # Línea AF (Azul) hacia Cocina y Baño
    dxf1.add_line(cx + 8, cy + 20, ox + 30, cy + 20, layer="TUBERIA_AGUA_FRIA")
    dxf1.add_line(ox + 30, cy + 20, ox + 30, oy + 8.0 * s, layer="TUBERIA_AGUA_FRIA")
    dxf1.add_text("PEX-a D25 Agua Fría", ox + 35, cy + 23, height=1.3, layer="TUBERIA_AGUA_FRIA")

    # Línea ACS (Rojo) hacia Cocina y Baño
    dxf1.add_line(cx + 8, cy + 17, ox + 25, cy + 17, layer="TUBERIA_ACS")
    dxf1.add_line(ox + 25, cy + 17, ox + 25, oy + 8.0 * s, layer="TUBERIA_ACS")
    dxf1.add_text("PEX-a D20 ACS Aislada", ox + 35, cy + 12, height=1.3, layer="TUBERIA_ACS")

    # Anillo de Retorno ACS (Verde) desde punto más lejano de cocina
    dxf1.add_line(ox + 20, oy + 8.0 * s, ox + 20, cy + 14, layer="TUBERIA_RETORNO_ACS")
    dxf1.add_line(ox + 20, cy + 14, cx + 8, cy + 14, layer="TUBERIA_RETORNO_ACS")
    dxf1.add_text("PEX-a D16 Retorno ACS", ox + 35, cy + 4, height=1.3, layer="TUBERIA_RETORNO_ACS")

    # Drenaje Saneamiento Negras hacia Biodigestor exterior
    dxf1.add_line(ox + 15, oy + 4.0 * s, ox - 15, oy + 4.0 * s, layer="SANEAMIENTO_NEGRAS")
    dxf1.add_text("PVC D110 a Biodigestor", ox - 20, oy + 4.0 * s + 4, height=1.3, layer="SANEAMIENTO_NEGRAS")

    dxf1.save()

    # SVG Plano 1
    svg1_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 297" width="100%" height="100%" style="background-color: #1a1e29; font-family: monospace;">
  <defs>
    <style>
      .marco {{ stroke: #455066; stroke-width: 1.0; fill: none; }}
      .muros {{ stroke: #8d99ae; stroke-width: 1.6; fill: #242c3d; }}
      .tubo-af {{ stroke: #00b4d8; stroke-width: 2.0; fill: none; }}
      .tubo-acs {{ stroke: #e63946; stroke-width: 2.0; fill: none; }}
      .tubo-ret {{ stroke: #52b788; stroke-width: 1.6; stroke-dasharray: 4,2; fill: none; }}
      .saneamiento {{ stroke: #f77f00; stroke-width: 2.5; stroke-dasharray: 6,3; fill: none; }}
      .bloque {{ stroke: #4361ee; stroke-width: 1.2; fill: #192338; }}
      .txt-title {{ fill: #ffffff; font-size: 4px; font-weight: bold; }}
      .txt-sub {{ fill: #00f0ff; font-size: 2.2px; font-weight: bold; }}
      .txt-body {{ fill: #cad2c5; font-size: 1.6px; }}
      .txt-af {{ fill: #00b4d8; font-size: 1.4px; }}
      .txt-acs {{ fill: #e63946; font-size: 1.4px; }}
      .txt-ret {{ fill: #52b788; font-size: 1.4px; }}
    </style>
  </defs>

  <!-- Marco A3 -->
  <rect x="5" y="5" width="410" height="287" class="marco"/>
  <rect x="210" y="242" width="200" height="45" class="marco"/>
  <text x="215" y="254" class="txt-title">OPEN-SOURCE-DOMOTICS</text>
  <text x="215" y="262" class="txt-sub">RED HIDRÁULICA: AGUA FRÍA, ACS Y RETORNO</text>
  <text x="215" y="271" class="txt-body">PEX-a D25/D20/D16 | Colector Manifold 1\" | Bomba Circuladora 24V</text>
  <text x="215" y="279" class="txt-body">Separación Aguas Grises y Negras | Conducción a Biodigestor Séptico</text>

  <!-- Vivienda -->
  <g id="red_hidraulica">
    <rect x="{ox}" y="{297 - (oy + 10.0*s)}" width="{10.0*s}" height="{10.0*s}" class="muros"/>
    <text x="{ox + 5}" y="{297 - (oy + 10.0*s + 4)}" class="txt-sub">VIVIENDA 10 x 10 m - DISTRIBUCIÓN HIDRÁULICA</text>

    <!-- Cuarto Técnico -->
    <rect x="{cx}" y="{297 - (cy + 2.5*s)}" width="{2.5*s}" height="{2.5*s}" fill="#1b2433" stroke="#00f0ff" stroke-width="1.2"/>
    <text x="{cx + 4}" y="{297 - (cy + 2.0*s)}" class="txt-sub">SALA TÉCNICA (ACS 500L)</text>

    <!-- Tuberías -->
    <line x1="{cx + 8}" y1="{297 - (cy + 20)}" x2="{ox + 30}" y2="{297 - (cy + 20)}" class="tubo-af"/>
    <line x1="{ox + 30}" y1="{297 - (cy + 20)}" x2="{ox + 30}" y2="{297 - (oy + 8.0*s)}" class="tubo-af"/>
    <text x="{ox + 35}" y="{297 - (cy + 23)}" class="txt-af">Agua Fría PEX-a D25 (2.5 bar)</text>

    <line x1="{cx + 8}" y1="{297 - (cy + 17)}" x2="{ox + 25}" y2="{297 - (cy + 17)}" class="tubo-acs"/>
    <line x1="{ox + 25}" y1="{297 - (cy + 17)}" x2="{ox + 25}" y2="{297 - (oy + 8.0*s)}" class="tubo-acs"/>
    <text x="{ox + 35}" y="{297 - (cy + 12)}" class="txt-acs">ACS Solar PEX-a D20 (45°C)</text>

    <line x1="{ox + 20}" y1="{297 - (oy + 8.0*s)}" x2="{ox + 20}" y2="{297 - (cy + 14)}" class="tubo-ret"/>
    <line x1="{ox + 20}" y1="{297 - (cy + 14)}" x2="{cx + 8}" y2="{297 - (cy + 14)}" class="tubo-ret"/>
    <text x="{ox + 35}" y="{297 - (cy + 4)}" class="txt-ret">Anillo Retorno ACS D16 (Agua Caliente Inmediata)</text>
  </g>

  <!-- Memoria Técnica (Derecha) -->
  <g id="memoria">
    <text x="215" y="45" class="txt-sub">PARÁMETROS TÉCNICOS DE DISEÑO HIDRÁULICO</text>

    <rect x="215" y="55" width="190" height="75" class="bloque" rx="2"/>
    <text x="220" y="70" class="txt-sub">1. RED DE AGUA FRÍA Y PRESIÓN CONSTANTE:</text>
    <text x="225" y="80" class="txt-body">• Alimentación: Cisterna pluvial 10kL + Red conmutada</text>
    <text x="225" y="88" class="txt-body">• Grupo hidroneumático con variador de frecuencia (2.5 bar)</text>
    <text x="225" y="96" class="txt-body">• Caudal simultáneo de cálculo: Qpico = 0.65 L/s</text>
    <text x="225" y="104" class="txt-body">• Colector manifold con llaves de corte individuales por punto</text>

    <rect x="215" y="140" width="190" height="90" class="bloque" rx="2"/>
    <text x="220" y="155" class="txt-sub">2. RED DE AGUA CALIENTE SANITARIA SOLAR (ACS):</text>
    <text x="225" y="165" class="txt-body">• Interacumulador solar de inercia 500 Litros (4 tubos de vacío)</text>
    <text x="225" y="173" class="txt-body">• Válvula mezcladora termostática a 45°C (antiescaldamiento)</text>
    <text x="225" y="181" class="txt-body">• Bomba de recirculación síncrona 24V de rotor húmedo</text>
    <text x="225" y="189" class="txt-ret">• Ahorro de agua: 100% agua caliente instantánea en grifos</text>
    <text x="225" y="197" class="txt-body">• Drenaje: Aguas negras a biodigestor, grises a biofiltro</text>
  </g>
</svg>
"""
    with open(font_svg, "w", encoding="utf-8") as f:
        f.write(svg1_content)

    print(f"Plano Fontanería DXF: {font_dxf}")
    print(f"Plano Fontanería SVG: {font_svg}")

    # =========================================================================
    # PLANO 2: RED DUAL DE GAS (RED DE COMISIÓN + GLP / BIOGÁS)
    # =========================================================================
    dxf2 = SimpleDXF(gas_dxf)
    dxf2.add_layer("MARCO_ROTULO", color=7)
    dxf2.add_layer("GAS_NATURAL_RED", color=1)
    dxf2.add_layer("GAS_GLP_BIOGAS", color=2)
    dxf2.add_layer("GAS_COLECTOR_DISTRIB", color=3)
    dxf2.add_layer("ELECTROVALVULAS_SEG", color=6)
    dxf2.add_layer("TEXTO_NOTAS", color=7)

    # Marco A3
    dxf2.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf2.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf2.add_rect(210, 10, 200, 45, layer="MARCO_ROTULO")
    dxf2.add_text("OPEN-SOURCE-DOMOTICS", 215, 45, height=4.0, layer="TEXTO_NOTAS")
    dxf2.add_text("ESQUEMA P&ID: RED DE GAS DUAL (COMISION + GLP/BIOGAS)", 215, 36, height=2.0, layer="TEXTO_NOTAS")
    dxf2.add_text("Cobre Tipo L D3/4\" Rígido | Reguladores 1ª/2ª Etapa | Electroválvulas NC", 215, 26, height=1.6, layer="TEXTO_NOTAS")
    dxf2.add_text("Conmutación Automática/Manual | Interbloqueo Físico con Sensor MQ-4", 215, 16, height=1.4, layer="TEXTO_NOTAS")

    # Diagrama Isométrico P&ID de Gas
    # Fuente 1: Acometida Red Pública (Gas Natural 20 mbar)
    dxf2.add_rect(20, 180, 40, 25, layer="GAS_NATURAL_RED")
    dxf2.add_text("ACOMETIDA RED", 22, 198, height=1.8, layer="TEXTO_NOTAS")
    dxf2.add_text("Gas Natural (20 mbar)", 22, 185, height=1.3, layer="TEXTO_NOTAS")

    # Fuente 2: Tanque GLP / Biogás
    dxf2.add_rect(20, 100, 40, 25, layer="GAS_GLP_BIOGAS")
    dxf2.add_text("RESERVA GLP / BIOGAS", 22, 118, height=1.8, layer="TEXTO_NOTAS")
    dxf2.add_text("Tanque / Biodigestor", 22, 105, height=1.3, layer="TEXTO_NOTAS")

    # Líneas hacia electroválvulas normalmente cerradas (NC)
    dxf2.add_line(60, 192, 100, 192, layer="GAS_NATURAL_RED")
    dxf2.add_rect(100, 185, 14, 14, layer="ELECTROVALVULAS_SEG")
    dxf2.add_text("EV-1 (NC)", 96, 204, height=1.4, layer="ELECTROVALVULAS_SEG")

    dxf2.add_line(60, 112, 100, 112, layer="GAS_GLP_BIOGAS")
    dxf2.add_rect(100, 105, 14, 14, layer="ELECTROVALVULAS_SEG")
    dxf2.add_text("EV-2 (NC)", 96, 124, height=1.4, layer="ELECTROVALVULAS_SEG")

    # Válvula de Conmutación de 3 Vías Motorizada (X=140, Y=150)
    dxf2.add_line(114, 192, 140, 192, layer="GAS_NATURAL_RED")
    dxf2.add_line(140, 192, 140, 160, layer="GAS_NATURAL_RED")

    dxf2.add_line(114, 112, 140, 112, layer="GAS_GLP_BIOGAS")
    dxf2.add_line(140, 112, 140, 140, layer="GAS_GLP_BIOGAS")

    dxf2.add_circle(140, 150, 10, layer="ELECTROVALVULAS_SEG")
    dxf2.add_text("VALV-3V", 132, 152, height=1.5, layer="TEXTO_NOTAS")
    dxf2.add_text("Conmutador Dual", 125, 134, height=1.3, layer="TEXTO_NOTAS")

    # Línea Colectora Común hacia consumos interiores (Cobre rígido 3/4")
    dxf2.add_line(150, 150, 200, 150, layer="GAS_COLECTOR_DISTRIB")
    dxf2.add_text("Cobre Tipo L D3/4\" (Ventilada)", 152, 155, height=1.4, layer="GAS_COLECTOR_DISTRIB")

    # Manómetro e Inyector de Emergencia
    dxf2.add_circle(175, 165, 6, layer="TEXTO_NOTAS")
    dxf2.add_line(175, 150, 175, 159, layer="TEXTO_NOTAS")
    dxf2.add_text("Manómetro 0-60mbar", 162, 175, height=1.3, layer="TEXTO_NOTAS")

    # Consumos finales: Cocina, Caldera Solar y Generador
    dxf2.add_rect(240, 175, 55, 25, layer="GAS_COLECTOR_DISTRIB")
    dxf2.add_text("COCINA (Estufa/Horno)", 242, 190, height=1.5, layer="TEXTO_NOTAS")
    dxf2.add_text("Consumo: 1.2 m3/h", 242, 180, height=1.2, layer="TEXTO_NOTAS")

    dxf2.add_rect(240, 135, 55, 25, layer="GAS_COLECTOR_DISTRIB")
    dxf2.add_text("APOYO SOLAR ACS", 242, 150, height=1.5, layer="TEXTO_NOTAS")
    dxf2.add_text("Consumo: 1.8 m3/h", 242, 140, height=1.2, layer="TEXTO_NOTAS")

    dxf2.add_rect(240, 95, 55, 25, layer="GAS_COLECTOR_DISTRIB")
    dxf2.add_text("GENERADOR DUAL 5kW", 242, 110, height=1.5, layer="TEXTO_NOTAS")
    dxf2.add_text("Consumo: 2.1 m3/h", 242, 100, height=1.2, layer="TEXTO_NOTAS")

    dxf2.add_line(200, 150, 240, 187, layer="GAS_COLECTOR_DISTRIB")
    dxf2.add_line(200, 150, 240, 147, layer="GAS_COLECTOR_DISTRIB")
    dxf2.add_line(200, 150, 240, 107, layer="GAS_COLECTOR_DISTRIB")

    dxf2.save()

    # SVG Plano 2
    svg2_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 297" width="100%" height="100%" style="background-color: #1a1e24; font-family: monospace;">
  <defs>
    <style>
      .marco {{ stroke: #455066; stroke-width: 1.0; fill: none; }}
      .gas-red {{ stroke: #3a86ff; stroke-width: 2.0; fill: none; }}
      .gas-glp {{ stroke: #ffb703; stroke-width: 2.0; fill: none; }}
      .gas-dist {{ stroke: #fb8500; stroke-width: 2.2; fill: none; }}
      .valvula {{ stroke: #d90429; stroke-width: 1.4; fill: #6a040f; }}
      .bloque {{ stroke: #8ecae6; stroke-width: 1.2; fill: #212d40; }}
      .txt-title {{ fill: #ffffff; font-size: 4px; font-weight: bold; }}
      .txt-sub {{ fill: #00f0ff; font-size: 2.2px; font-weight: bold; }}
      .txt-body {{ fill: #cad2c5; font-size: 1.6px; }}
      .txt-gas {{ fill: #ffb703; font-size: 1.4px; font-weight: bold; }}
      .txt-alert {{ fill: #ff4d6d; font-size: 1.4px; }}
    </style>
  </defs>

  <!-- Marco A3 -->
  <rect x="5" y="5" width="410" height="287" class="marco"/>
  <rect x="210" y="242" width="200" height="45" class="marco"/>
  <text x="215" y="254" class="txt-title">OPEN-SOURCE-DOMOTICS</text>
  <text x="215" y="262" class="txt-sub">RED DE GAS DUAL: COMISIÓN + GLP/BIOMÁS</text>
  <text x="215" y="271" class="txt-body">Cobre Tipo L D3/4\" Rígido | Reguladores 1ª/2ª Etapa | Electroválvulas NC</text>
  <text x="215" y="279" class="txt-body">Conmutación Automática/Manual | Interbloqueo Físico con Sensor MQ-4</text>

  <!-- P&ID Gas Dual -->
  <g id="pid_gas">
    <!-- Fuente 1: Red -->
    <rect x="20" y="65" width="45" height="30" class="bloque"/>
    <text x="23" y="78" class="txt-sub">RED COMISIÓN</text>
    <text x="23" y="87" class="txt-body">Gas Natural (20 mbar)</text>

    <!-- Fuente 2: GLP / Biogás -->
    <rect x="20" y="145" width="45" height="30" class="bloque"/>
    <text x="23" y="158" class="txt-sub">GLP / BIOGÁS</text>
    <text x="23" y="167" class="txt-body">Depósito / Biodigestor</text>

    <!-- Líneas a Válvulas NC -->
    <line x1="65" y1="80" x2="105" y2="80" class="gas-red"/>
    <rect x="105" y="73" width="14" height="14" class="valvula"/>
    <text x="100" y="65" class="txt-alert">EV-1 (NC)</text>

    <line x1="65" y1="160" x2="105" y2="160" class="gas-glp"/>
    <rect x="105" y="153" width="14" height="14" class="valvula"/>
    <text x="100" y="145" class="txt-alert">EV-2 (NC)</text>

    <!-- Hacia Válvula 3 Vías -->
    <line x1="119" y1="80" x2="140" y2="80" class="gas-red"/>
    <line x1="140" y1="80" x2="140" y2="110" class="gas-red"/>

    <line x1="119" y1="160" x2="140" y2="160" class="gas-glp"/>
    <line x1="140" y1="160" x2="140" y2="130" class="gas-glp"/>

    <circle cx="140" cy="120" r="10" fill="#2b2d42" stroke="#ffb703" stroke-width="1.5"/>
    <text x="133" y="122" class="txt-gas">3-VÍAS</text>

    <!-- Salida de Distribución Interior -->
    <line x1="150" y1="120" x2="200" y2="120" class="gas-dist"/>
    <text x="152" y="114" class="txt-body">Cobre 3/4\"</text>

    <!-- Cargas -->
    <rect x="230" y="65" width="60" height="28" class="bloque"/>
    <text x="234" y="78" class="txt-sub">COCINA</text>
    <text x="234" y="86" class="txt-body">Estufa / Horno</text>

    <rect x="230" y="105" width="60" height="28" class="bloque"/>
    <text x="234" y="118" class="txt-sub">APOYO ACS</text>
    <text x="234" y="126" class="txt-body">Caldera Solar</text>

    <rect x="230" y="145" width="60" height="28" class="bloque"/>
    <text x="234" y="158" class="txt-sub">GENERADOR</text>
    <text x="234" y="166" class="txt-body">Dual 5 kW ATS</text>

    <line x1="200" y1="120" x2="230" y2="79" class="gas-dist"/>
    <line x1="200" y1="120" x2="230" y2="119" class="gas-dist"/>
    <line x1="200" y1="120" x2="230" y2="159" class="gas-dist"/>
  </g>
</svg>
"""
    with open(gas_svg, "w", encoding="utf-8") as f:
        f.write(svg2_content)

    print(f"Plano Gas Dual DXF: {gas_dxf}")
    print(f"Plano Gas Dual SVG: {gas_svg}")

if __name__ == "__main__":
    base = "/home/ral/Documents/GitHub/open-source-domotics/00_diseno_arquitectonico_y_estructural/05_instalaciones_hidraulicas_y_gas"
    generar_planos_fontaneria_y_gas(base)

