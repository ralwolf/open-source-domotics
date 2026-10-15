#!/usr/bin/env python3
"""
Generador de Diagrama Unifilar Eléctrico (Esquema de Tablero General de Distribución)
Formatos de salida: DXF (AutoCAD/LibreCAD/Ingetrazzo) y SVG vectorial estándar.
Proyecto: open-source-domotics
"""

import os
from generar_planos_dxf import SimpleDXF

def generar_diagrama_unifilar(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_ROTULO", color=7)
    dxf.add_layer("ACOMETIDA_POTENCIA", color=1)
    dxf.add_layer("BARRAS_DISTRIBUCION", color=3)
    dxf.add_layer("DISPOSITIVOS_PROTECCION", color=4)
    dxf.add_layer("CIRCUITOS_DERIVADOS", color=2)
    dxf.add_layer("CONTROL_DOMOTICA", color=6)
    dxf.add_layer("TEXTO_ROTULOS", color=7)

    # Marco A3 (420 x 297 mm en escala 1:1 mm)
    dxf.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    # Cuadro de título
    dxf.add_rect(240, 10, 170, 40, layer="MARCO_ROTULO")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", 245, 38, height=4.0, layer="TEXTO_ROTULOS")
    dxf.add_text("DIAGRAMA UNIFILAR - TABLERO GENERAL (TGBT)", 245, 28, height=3.0, layer="TEXTO_ROTULOS")
    dxf.add_text("Escala: 1:1  |  Norma: IEC 60364 / REBT  |  Rev: 1.0", 245, 18, height=2.2, layer="TEXTO_ROTULOS")

    # Acometidas superiores (Red Pública + Híbrido Solar/Eólico ESS)
    # Entrada Red
    dxf.add_line(60, 275, 60, 245, layer="ACOMETIDA_POTENCIA")
    dxf.add_text("RED PUBLICA 230V L+N", 40, 280, height=2.5, layer="TEXTO_ROTULOS")
    # Entrada Inversor Híbrido
    dxf.add_line(120, 275, 120, 245, layer="ACOMETIDA_POTENCIA")
    dxf.add_text("INVERSOR / ESS / EOLICO", 100, 280, height=2.5, layer="TEXTO_ROTULOS")

    # Conmutador de transferencia automática (ATS)
    dxf.add_rect(50, 230, 80, 15, layer="DISPOSITIVOS_PROTECCION")
    dxf.add_text("ATS 63A (CONMUTADOR DE RED / ISLA)", 53, 236, height=2.2, layer="TEXTO_ROTULOS")
    dxf.add_line(90, 230, 90, 215, layer="ACOMETIDA_POTENCIA")

    # Cabecera TGBT: DPS + IGA + RCD + Medidor
    # DPS (Descargador de sobretensiones)
    dxf.add_line(90, 215, 35, 215, layer="ACOMETIDA_POTENCIA")
    dxf.add_line(35, 215, 35, 195, layer="ACOMETIDA_POTENCIA")
    dxf.add_rect(25, 180, 20, 15, layer="DISPOSITIVOS_PROTECCION")
    dxf.add_text("DPS TIPO 2", 27, 188, height=2.0, layer="TEXTO_ROTULOS")
    dxf.add_text("40kA In / Up 1.5kV", 26, 183, height=1.6, layer="TEXTO_ROTULOS")
    # Tierra DPS
    dxf.add_line(35, 180, 35, 170, layer="ACOMETIDA_POTENCIA")
    dxf.add_line(30, 170, 40, 170, layer="ACOMETIDA_POTENCIA")
    dxf.add_line(32, 168, 38, 168, layer="ACOMETIDA_POTENCIA")

    # Medidor de Energía en cabecera (Modbus RS485)
    dxf.add_rect(75, 198, 30, 14, layer="CONTROL_DOMOTICA")
    dxf.add_text("MEDIDOR MODBUS", 77, 206, height=2.0, layer="TEXTO_ROTULOS")
    dxf.add_text("SDM630 / ATM90E32", 76, 201, height=1.6, layer="TEXTO_ROTULOS")

    # IGA General 63A
    dxf.add_rect(75, 175, 30, 15, layer="DISPOSITIVOS_PROTECCION")
    dxf.add_text("IGA 2P 63A 10kA", 77, 183, height=2.2, layer="TEXTO_ROTULOS")
    dxf.add_text("Curva C", 83, 178, height=1.8, layer="TEXTO_ROTULOS")

    # Diferencial General RCD 63A 30mA Superinmunizado
    dxf.add_line(90, 175, 90, 165, layer="ACOMETIDA_POTENCIA")
    dxf.add_rect(75, 150, 30, 15, layer="DISPOSITIVOS_PROTECCION")
    dxf.add_text("RCD 2P 63A 30mA", 76, 158, height=2.0, layer="TEXTO_ROTULOS")
    dxf.add_text("Tipo A-SI", 82, 153, height=1.8, layer="TEXTO_ROTULOS")

    # Bajada a Barra Distribución Principal
    dxf.add_line(90, 150, 90, 135, layer="ACOMETIDA_POTENCIA")

    # Barra Colectora Principal (X: 30 a 390, Y: 135)
    dxf.add_line(30, 135, 390, 135, layer="BARRAS_DISTRIBUCION")
    dxf.add_line(30, 134, 390, 134, layer="BARRAS_DISTRIBUCION")
    dxf.add_text("BARRA COLECTORA PRINCIPAL DISTRIBUCION (63A)", 35, 138, height=2.5, layer="TEXTO_ROTULOS")

    # Contactor de Cargas Críticas / Desconexión Cargas Pesadas (Load Shedding)
    dxf.add_rect(240, 120, 45, 12, layer="CONTROL_DOMOTICA")
    dxf.add_text("CONTACTOR LOAD-SHEDDING", 242, 126, height=1.8, layer="TEXTO_ROTULOS")
    dxf.add_text("Controlado por ESP32 / HA", 242, 122, height=1.5, layer="TEXTO_ROTULOS")

    # 9 Circuitos Derivados
    circuitos = [
        {"id": "C1", "nombre": "Alumbrado + Domótica", "mcb": "10A C", "rcd": "10mA", "cable": "3x1.5 mm²", "critica": True, "x": 45},
        {"id": "C2", "nombre": "Tomas Generales", "mcb": "16A C", "rcd": "30mA", "cable": "3x2.5 mm²", "critica": True, "x": 85},
        {"id": "C3", "nombre": "Sala IT / Domótica / Router", "mcb": "16A C", "rcd": "30mA A-SI", "cable": "3x2.5 mm²", "critica": True, "x": 125},
        {"id": "C4", "nombre": "Ventilación VMC y Lucernario", "mcb": "10A C", "rcd": "30mA", "cable": "3x1.5 mm²", "critica": True, "x": 165},
        {"id": "C5", "nombre": "Refrigeración / Bomba Agua", "mcb": "16A C", "rcd": "30mA", "cable": "3x2.5 mm²", "critica": True, "x": 205},
        {"id": "C6", "nombre": "Cocina Inducción / Horno", "mcb": "32A C", "rcd": "30mA", "cable": "3x6.0 mm²", "critica": False, "x": 260},
        {"id": "C7", "nombre": "Climatización Multi-Split", "mcb": "20A C", "rcd": "30mA", "cable": "3x4.0 mm²", "critica": False, "x": 300},
        {"id": "C8", "nombre": "Lavadora / Secadora", "mcb": "20A C", "rcd": "30mA", "cable": "3x4.0 mm²", "critica": False, "x": 340},
        {"id": "C9", "nombre": "Cargador EV Wallbox", "mcb": "32A C", "rcd": "30mA Tipo B", "cable": "3x10.0 mm²", "critica": False, "x": 380},
    ]

    for c in circuitos:
        x = c["x"]
        # Conexión desde barra
        dxf.add_line(x, 134, x, 115, layer="CIRCUITOS_DERIVADOS")
        # Transformador de Corriente (CT de Medición Sub-panel)
        dxf.add_circle(x, 110, 3.0, layer="CONTROL_DOMOTICA")
        dxf.add_line(x, 107, x, 100, layer="CIRCUITOS_DERIVADOS")
        # Disyuntor Magnetotérmico (MCB)
        dxf.add_rect(x - 8, 85, 16, 15, layer="DISPOSITIVOS_PROTECCION")
        dxf.add_text(c["mcb"], x - 6, 92, height=1.8, layer="TEXTO_ROTULOS")
        dxf.add_line(x, 85, x, 75, layer="CIRCUITOS_DERIVADOS")
        # Caja bornera salida
        dxf.add_rect(x - 9, 58, 18, 16, layer="CIRCUITOS_DERIVADOS")
        dxf.add_text(c["id"], x - 4, 69, height=2.2, layer="TEXTO_ROTULOS")
        dxf.add_text(c["cable"], x - 8, 62, height=1.5, layer="TEXTO_ROTULOS")
        # Línea de salida final
        dxf.add_line(x, 58, x, 40, layer="CIRCUITOS_DERIVADOS")
        # Etiqueta de circuito vertical o inclinada en bloque
        dxf.add_text(c["nombre"][:14], x - 12, 34, height=1.6, layer="TEXTO_ROTULOS")
        tipo_carga = "[CRITICA - UPS]" if c["critica"] else "[DESCONECTABLE]"
        dxf.add_text(tipo_carga, x - 12, 28, height=1.3, layer="TEXTO_ROTULOS")

    dxf.save()

    # 2. GENERACIÓN SVG (Vectorial nítido para vista directa en GitHub/Navegador)
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 850" width="100%" height="100%" style="background:#1e1e2e; font-family:sans-serif;">
  <defs>
    <style>
      .title {{ fill: #cdd6f4; font-size: 22px; font-weight: bold; }}
      .subtitle {{ fill: #89b4fa; font-size: 14px; }}
      .label {{ fill: #cdd6f4; font-size: 11px; }}
      .sublabel {{ fill: #a6adc8; font-size: 9px; }}
      .critica {{ fill: #a6e3a1; font-weight: bold; font-size: 9px; }}
      .descon {{ fill: #f38ba8; font-size: 9px; }}
      .wire-main {{ stroke: #f38ba8; stroke-width: 3.5; fill: none; }}
      .wire-bus {{ stroke: #a6e3a1; stroke-width: 5; fill: none; }}
      .wire-branch {{ stroke: #89b4fa; stroke-width: 2; fill: none; }}
      .wire-ct {{ stroke: #f9e2af; stroke-width: 1.5; fill: none; }}
      .box-dev {{ fill: #313244; stroke: #cdd6f4; stroke-width: 1.5; rx: 4; }}
      .box-meter {{ fill: #181825; stroke: #fab387; stroke-width: 2; rx: 4; }}
      .box-shed {{ fill: #181825; stroke: #f38ba8; stroke-width: 1.5; stroke-dasharray: 4; rx: 3; }}
    </style>
  </defs>

  <!-- Marco Exterior -->
  <rect x="20" y="20" width="1160" height="810" fill="none" stroke="#45475a" stroke-width="2" rx="8"/>
  <rect x="35" y="35" width="1130" height="780" fill="none" stroke="#313244" stroke-width="1"/>

  <!-- Cuadro de Título -->
  <rect x="750" y="50" width="400" height="90" fill="#181825" stroke="#45475a" stroke-width="1.5" rx="5"/>
  <text x="770" y="80" class="title">OPEN-SOURCE-DOMOTICS</text>
  <text x="770" y="105" class="subtitle">TGBT - Esquema Unifilar Cuadro de Distribución</text>
  <text x="770" y="125" class="sublabel">Norma: IEC 60364 / REBT | 230V 50Hz | Acometida Híbrida 63A</text>

  <!-- Entradas de Potencia -->
  <text x="150" y="70" class="title" style="font-size:14px; fill:#fab387;">RED PÚBLICA 230V L+N</text>
  <line x1="220" y1="80" x2="220" y2="150" class="wire-main"/>

  <text x="350" y="70" class="title" style="font-size:14px; fill:#89b4fa;">INVERSOR ESS / EÓLICO</text>
  <line x1="420" y1="80" x2="420" y2="150" class="wire-main"/>

  <!-- ATS Conmutador -->
  <rect x="180" y="150" width="280" height="40" class="box-dev"/>
  <text x="210" y="175" class="label" style="font-weight:bold;">ATS 63A 4P (Transferencia Automática)</text>

  <!-- Línea hacia Cabecera -->
  <line x1="320" y1="190" x2="320" y2="230" class="wire-main"/>

  <!-- DPS Sobretensiones -->
  <line x1="320" y1="230" x2="140" y2="230" class="wire-branch"/>
  <line x1="140" y1="230" x2="140" y2="270" class="wire-branch"/>
  <rect x="90" y="270" width="100" height="50" class="box-dev"/>
  <text x="105" y="295" class="label" style="fill:#fab387;">DPS Tipo 2</text>
  <text x="100" y="310" class="sublabel">40kA / Up 1.5kV</text>
  <line x1="140" y1="320" x2="140" y2="350" stroke="#a6e3a1" stroke-width="2"/>
  <text x="120" y="365" class="sublabel" style="fill:#a6e3a1;">⏚ P. Tierra</text>

  <!-- Medidor Telemetría Cabecera -->
  <rect x="250" y="240" width="140" height="45" class="box-meter"/>
  <text x="260" y="262" class="label" style="fill:#fab387; font-weight:bold;">MEDIDOR MODBUS</text>
  <text x="268" y="277" class="sublabel">SDM630 / ATM90E32 (RS485)</text>

  <!-- IGA Principal -->
  <line x1="320" y1="285" x2="320" y2="310" class="wire-main"/>
  <rect x="250" y="310" width="140" height="40" class="box-dev"/>
  <text x="265" y="332" class="label" style="font-weight:bold;">IGA 2P 63A 10kA (Curva C)</text>

  <!-- RCD General Superinmunizado -->
  <line x1="320" y1="350" x2="320" y2="375" class="wire-main"/>
  <rect x="250" y="375" width="140" height="40" class="box-dev"/>
  <text x="260" y="397" class="label" style="font-weight:bold;">RCD 2P 63A 30mA (Tipo A-SI)</text>

  <!-- Conexión a Barra Distribución -->
  <line x1="320" y1="415" x2="320" y2="460" class="wire-main"/>

  <!-- BARRA DISTRIBUCION GENERAL -->
  <line x1="70" y1="460" x2="1120" y2="460" class="wire-bus"/>
  <text x="80" y="450" class="label" style="fill:#a6e3a1; font-weight:bold;">BARRA PRINCIPAL DE DISTRIBUCIÓN (230V / 63A Cu)</text>

  <!-- Load Shedding Contactor -->
  <rect x="710" y="475" width="410" height="25" class="box-shed"/>
  <text x="730" y="492" class="sublabel" style="fill:#f38ba8; font-weight:bold;">CORTACARGAS AUTOMÁTICO (LOAD-SHEDDING EN MODO ISLA / BATERÍA CRÍTICA)</text>
"""

    svg_circs = [
        {"id": "C1", "name": "Alumbrado + Domótica", "mcb": "10A C", "cable": "3x1.5 mm²", "crit": True, "x": 120},
        {"id": "C2", "name": "Tomas de Corriente", "mcb": "16A C", "cable": "3x2.5 mm²", "crit": True, "x": 240},
        {"id": "C3", "name": "Sala IT / Router / HA", "mcb": "16A C", "cable": "3x2.5 mm²", "crit": True, "x": 360},
        {"id": "C4", "name": "VMC + Lucernario", "mcb": "10A C", "cable": "3x1.5 mm²", "crit": True, "x": 480},
        {"id": "C5", "name": "Refrigerador / Bomba", "mcb": "16A C", "cable": "3x2.5 mm²", "crit": True, "x": 600},
        {"id": "C6", "name": "Cocina Inducción / Horno", "mcb": "32A C", "cable": "3x6.0 mm²", "crit": False, "x": 760},
        {"id": "C7", "name": "Climatización MultiSplit", "mcb": "20A C", "cable": "3x4.0 mm²", "crit": False, "x": 880},
        {"id": "C8", "name": "Lavadora y Secadora", "mcb": "20A C", "cable": "3x4.0 mm²", "crit": False, "x": 1000},
        {"id": "C9", "name": "Cargador EV Wallbox", "mcb": "32A C", "cable": "3x10.0 mm²", "crit": False, "x": 1090},
    ]

    for c in svg_circs:
        x = c["x"]
        crit_text = '<text x="%d" y="785" class="critica">● ESENCIAL (UPS)</text>' % (x - 38) if c["crit"] else '<text x="%d" y="785" class="descon">○ DESCONECTABLE</text>' % (x - 42)
        svg_content += f"""
  <!-- Circuito {c['id']} -->
  <line x1="{x}" y1="460" x2="{x}" y2="520" class="wire-branch"/>
  <!-- Sensor CT Medición -->
  <circle cx="{x}" cy="530" r="8" fill="#181825" stroke="#f9e2af" stroke-width="2"/>
  <text x="{x-4}" y="534" style="fill:#f9e2af; font-size:9px; font-weight:bold;">CT</text>
  <line x1="{x}" y1="538" x2="{x}" y2="570" class="wire-branch"/>
  <!-- Magnetotérmico MCB -->
  <rect x="{x-35}" y="570" width="70" height="45" class="box-dev"/>
  <text x="{x-20}" y="592" class="label" style="font-weight:bold;">MCB 2P</text>
  <text x="{x-16}" y="607" class="sublabel">{c['mcb']}</text>
  <line x1="{x}" y1="615" x2="{x}" y2="650" class="wire-branch"/>
  <!-- Borna Salida -->
  <rect x="{x-42}" y="650" width="84" height="45" fill="#1e1e2e" stroke="#89b4fa" stroke-width="1.5" rx="3"/>
  <text x="{x-10}" y="670" class="label" style="fill:#89b4fa; font-weight:bold;">{c['id']}</text>
  <text x="{x-32}" y="685" class="sublabel">{c['cable']}</text>
  <line x1="{x}" y1="695" x2="{x}" y2="730" class="wire-branch"/>
  <!-- Etiqueta Nombre y Prioridad -->
  <text x="{x-40}" y="750" class="label">{c['name']}</text>
  {crit_text}
"""

    svg_content += "\n</svg>\n"
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Esquema SVG generado: {svg_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dxf_dest = os.path.join(base_dir, "01_energia_renovable_y_potencia/07_tableros_distribucion_y_protecciones/electrico/cuadro_general_unifilar.dxf")
    svg_dest = os.path.join(base_dir, "01_energia_renovable_y_potencia/07_tableros_distribucion_y_protecciones/electrico/cuadro_general_unifilar.svg")
    generar_diagrama_unifilar(dxf_dest, svg_dest)

