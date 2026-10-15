#!/usr/bin/env python3
"""
generar_plano_oficina.py
Genera los planos CAD 2D en DXF R12 y SVG vectorial de la infraestructura eléctrica,
filtrado EMI/RFI, UPS senoidal y señalización "ON AIR" para la oficina técnica.
"""

import os

class SimpleDXF:
    def __init__(self, filename):
        self.filename = filename
        self.entities = []

    def add_line(self, x1, y1, x2, y2, layer="0", color=7):
        self.entities.append(f"0\nLINE\n8\n{layer}\n62\n{color}\n10\n{x1:.3f}\n20\n{y1:.3f}\n30\n0.0\n11\n{x2:.3f}\n21\n{y2:.3f}\n31\n0.0")

    def add_circle(self, cx, cy, radius, layer="0", color=7):
        self.entities.append(f"0\nCIRCLE\n8\n{layer}\n62\n{color}\n10\n{cx:.3f}\n20\n{cy:.3f}\n30\n0.0\n40\n{radius:.3f}")

    def add_rect(self, x, y, w, h, layer="0", color=7):
        self.add_line(x, y, x + w, y, layer, color)
        self.add_line(x + w, y, x + w, y + h, layer, color)
        self.add_line(x + w, y + h, x, y + h, layer, color)
        self.add_line(x, y + h, x, y, layer, color)

    def add_text(self, text, x, y, height=150, layer="0", color=7):
        self.entities.append(f"0\nTEXT\n8\n{layer}\n62\n{color}\n10\n{x:.3f}\n20\n{y:.3f}\n30\n0.0\n40\n{height:.3f}\n1\n{text}")

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write("0\nSECTION\n2\nHEADER\n0\nENDSEC\n")
            f.write("0\nSECTION\n2\nENTITIES\n")
            for e in self.entities:
                f.write(e + "\n")
            f.write("0\nENDSEC\n0\nEOF\n")
        print(f"Plano DXF generado: {self.filename}")

def generar_svg_oficina(svg_path):
    svg_content = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 850" width="100%" height="100%" style="background-color: #0d1117; font-family: 'DejaVu Sans', Helvetica, Arial, sans-serif;">
  <defs>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#21262d" stroke-width="1"/>
    </pattern>
  </defs>

  <rect width="1100" height="850" fill="url(#grid)" />

  <!-- Carátula -->
  <rect x="50" y="30" width="1000" height="60" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="70" y="65" fill="#f0f6fc" font-size="18" font-weight="bold">INFRAESTRUCTURA ELÉCTRICA, FILTRADO AUDIO Y SEÑALIZACIÓN ON-AIR: OFICINA TÉCNICA</text>
  <text x="70" y="82" fill="#8b949e" font-size="12">PDU Escritorio Filtrada EMI/RFI | UPS Senoidal 1000VA | Desconexión Cargas Vampiro | Señalizador Puerta "ON AIR"</text>

  <!-- PLANO DISTRIBUCIÓN PUESTO DE TRABAJO (IZQUIERDA) -->
  <rect x="60" y="120" width="480" height="580" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="80" y="150" fill="#58a6ff" font-size="14" font-weight="bold">PLANTA DE ESTACIÓN DE TRABAJO (1.80 x 0.80 m)</text>

  <!-- Tablero Escritorio -->
  <rect x="90" y="200" width="420" height="240" fill="#21262d" stroke="#58a6ff" stroke-width="3" rx="6"/>
  <text x="110" y="225" fill="#8b949e" font-size="11" font-weight="bold">MESA DE TRABAJO TÉCNICA</text>

  <!-- Doble Monitor 27" -->
  <rect x="150" y="240" width="130" height="20" fill="#30363d" stroke="#c9d1d9" stroke-width="1.5" rx="2"/>
  <rect x="300" y="240" width="130" height="20" fill="#30363d" stroke="#c9d1d9" stroke-width="1.5" rx="2"/>
  <text x="250" y="255" fill="#c9d1d9" font-size="10">MONITORES 4K</text>

  <!-- Monitores de Audio de Estudio Nearfield -->
  <rect x="105" y="240" width="35" height="45" fill="#161b22" stroke="#58a6ff" stroke-width="1.5" rx="3"/>
  <rect x="440" y="240" width="35" height="45" fill="#161b22" stroke="#58a6ff" stroke-width="1.5" rx="3"/>
  <text x="110" y="270" fill="#58a6ff" font-size="8">AUDIO L</text>
  <text x="445" y="270" fill="#58a6ff" font-size="8">AUDIO R</text>

  <!-- Brazo articulado con Micrófono XLR Capacitivo -->
  <circle cx="210" cy="320" r="10" fill="#d29922" stroke="#f0e68c" stroke-width="1.5"/>
  <path d="M 170 360 L 210 320" stroke="#d29922" stroke-width="2"/>
  <text x="140" y="380" fill="#d29922" font-size="9" font-weight="bold">MICRÓFONO XLR</text>

  <!-- Torre PC Workstation bajo mesa -->
  <rect x="400" y="320" width="70" height="100" fill="#161b22" stroke="#2ea043" stroke-width="2" rx="4"/>
  <text x="410" y="375" fill="#2ea043" font-size="10" font-weight="bold">PC MAESTRO</text>

  <!-- PDU de Escritorio con Señalizador On-Air -->
  <rect x="250" y="390" width="120" height="35" fill="#1f6feb" stroke="#58a6ff" stroke-width="2" rx="4"/>
  <text x="260" y="412" fill="#ffffff" font-size="9" font-weight="bold">PDU FILTRADA EMI</text>

  <!-- UPS Senoidal Interactivo 1000VA en Suelo -->
  <rect x="110" y="480" width="100" height="180" fill="#21262d" stroke="#e3b341" stroke-width="2" rx="6"/>
  <text x="120" y="560" fill="#e3b341" font-size="11" font-weight="bold">UPS 1000VA</text>
  <text x="120" y="580" fill="#8b949e" font-size="9">Onda Senoidal Pura</text>

  <!-- Puerta de Oficina y Señalizador "ON AIR" -->
  <rect x="360" y="520" width="120" height="15" fill="#30363d" stroke="#8b949e" stroke-width="2"/>
  <rect x="390" y="495" width="60" height="20" fill="#da3633" stroke="#f85149" stroke-width="2" rx="3"/>
  <text x="400" y="510" fill="#ffffff" font-size="9" font-weight="bold">ON AIR</text>
  <text x="360" y="555" fill="#f85149" font-size="10" font-weight="bold">Señalizador Exterior Puerta</text>

  <!-- ESQUEMA ELÉCTRICO Y DE AUTOMATIZACIÓN (DERECHA) -->
  <rect x="560" y="120" width="490" height="580" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="580" y="150" fill="#58a6ff" font-size="14" font-weight="bold">ARQUITECTURA DE ENERGÍA Y CONTROL VAMPIRO</text>

  <!-- Bloque UPS e Inversor -->
  <rect x="580" y="180" width="160" height="50" fill="#21262d" stroke="#e3b341" stroke-width="2" rx="4"/>
  <text x="595" y="210" fill="#e3b341" font-size="12" font-weight="bold">UPS SENOIDAL 1000VA</text>

  <!-- Filtro de Red EMI/RFI Grado Estudio -->
  <rect x="760" y="180" width="160" height="50" fill="#21262d" stroke="#58a6ff" stroke-width="2" rx="4"/>
  <text x="770" y="210" fill="#58a6ff" font-size="11" font-weight="bold">FILTRO EMI/RFI LC</text>

  <!-- Salida Toma Maestra (PC Principal) -->
  <path d="M 840 230 L 840 280 L 660 280 L 660 320" stroke="#2ea043" stroke-width="3"/>
  <rect x="620" y="320" width="160" height="65" fill="#21262d" stroke="#2ea043" stroke-width="2" rx="4"/>
  <text x="635" y="345" fill="#2ea043" font-size="12" font-weight="bold">TOMA MAESTRA (PC)</text>
  <text x="635" y="365" fill="#8b949e" font-size="10">Monitorización Potencia W</text>

  <!-- Lógica Relé Esclavo Cargas Vampiro -->
  <path d="M 840 280 L 840 320" stroke="#f85149" stroke-width="3"/>
  <rect x="800" y="320" width="180" height="65" fill="#21262d" stroke="#f85149" stroke-width="2" rx="4"/>
  <text x="815" y="345" fill="#f85149" font-size="11" font-weight="bold">RELÉ CARGAS ESCLAVAS</text>
  <text x="815" y="365" fill="#8b949e" font-size="10">Monitores + Altavoces + Luz</text>

  <!-- Controlador PDU ESP32-C3 -->
  <rect x="620" y="420" width="360" height="140" fill="#21262d" stroke="#58a6ff" stroke-width="2" rx="6"/>
  <text x="640" y="450" fill="#58a6ff" font-size="13" font-weight="bold">CONTROLADOR PDU OFICINA (ESP32-C3)</text>
  <text x="640" y="475" fill="#f0f6fc" font-size="11">■ Detección PC &lt; 20W: Apaga automáticamente cargas vampiro</text>
  <text x="640" y="500" fill="#f0f6fc" font-size="11">■ Detección PC &gt; 45W: Enciende periféricos al arrancar equipo</text>
  <text x="640" y="525" fill="#f85149" font-size="11">■ Salida 12V Señalizador ON AIR: Activado por cámara/micrófono</text>
  <text x="640" y="545" fill="#8b949e" font-size="10">Ahorro anual estimado: ~180 kWh en consumos fantasma</text>

  <!-- Pie de plano -->
  <rect x="50" y="720" width="1000" height="100" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="70" y="745" fill="#f0f6fc" font-size="12" font-weight="bold">ESPECIFICACIONES DE CALIDAD ELÉCTRICA Y AUTOMATIZACIÓN:</text>
  <text x="70" y="765" fill="#58a6ff" font-size="11">■ Filtrado EMI/RFI: Atenuación &gt;45 dB en banda 150 kHz - 30 MHz para eliminar zumbidos en preamplificadores de micrófonos capacitivos e interfaces USB.</text>
  <text x="70" y="785" fill="#2ea043" font-size="11">■ Cero Cargas Vampiro: Al apagar el PC, los transformadores de monitores y altavoces activos se desconectan físicamente mediante relé por hardware.</text>
  <text x="70" y="805" fill="#f85149" font-size="11">■ Señalización Automática ON AIR: Integrada con Home Assistant vía MQTT al detectar que la cámara o el micrófono entran en estado activo en el sistema operativo.</text>
</svg>"""

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Plano SVG generado: {svg_path}")

def generar_plano_oficina_dxf(dxf_path):
    dxf = SimpleDXF(dxf_path)
    # Mesa oficina (1800 x 800 mm)
    dxf.add_rect(0, 0, 1800, 800, layer="MESA_OFICINA", color=7)

    # Monitores 4K
    dxf.add_rect(300, 500, 550, 50, layer="MONITORES", color=4) # Cyan
    dxf.add_rect(950, 500, 550, 50, layer="MONITORES", color=4)
    dxf.add_text("DOBLE MONITOR 4K (CARGA ESCLAVA)", 400, 450, height=50, layer="TEXTOS", color=4)

    # PC Workstation (toma maestra)
    dxf.add_rect(1300, 100, 300, 500, layer="PC_MAESTRO", color=3) # Verde
    dxf.add_text("PC WORKSTATION (TOMA MAESTRA C20)", 1250, 650, height=50, layer="TEXTOS", color=3)

    # PDU Filtrada
    dxf.add_rect(700, 100, 400, 100, layer="PDU_FILTRADA", color=5) # Azul
    dxf.add_text("PDU ESCRITORIO CON FILTRO EMI/RFI", 700, 50, height=50, layer="TEXTOS", color=5)

    # Puerta y Señalizador On Air
    dxf.add_rect(2000, 0, 100, 800, layer="PUERTA_OFICINA", color=1)
    dxf.add_rect(1950, 350, 50, 150, layer="SENALIZADOR_ON_AIR", color=1)
    dxf.add_text("SENALIZADOR PUERTA ON AIR", 1850, 550, height=50, layer="TEXTOS", color=1)

    dxf.save()

if __name__ == "__main__":
    out_dir = "/home/ral/Documents/GitHub/open-source-domotics/04_telemetria_y_cargas_criticas/04_cargas_oficina/mecanico"
    os.makedirs(out_dir, exist_ok=True)
    dxf_file = os.path.join(out_dir, "plano_oficina_electrico_telemetria.dxf")
    svg_file = os.path.join(out_dir, "plano_oficina_electrico_telemetria.svg")

    generar_plano_oficina_dxf(dxf_file)
    generar_svg_oficina(svg_file)
