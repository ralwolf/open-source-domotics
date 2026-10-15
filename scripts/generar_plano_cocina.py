#!/usr/bin/env python3
"""
generar_plano_cocina.py
Genera los planos CAD 2D en DXF R12 y SVG vectorial de la distribución eléctrica,
protecciones y telemetría de cargas críticas en la cocina de la vivienda 10x10m.
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

def generar_svg_cocina(svg_path):
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
  <text x="70" y="65" fill="#f0f6fc" font-size="18" font-weight="bold">DISTRIBUCIÓN ELÉCTRICA, TELEMETRÍA Y PROTECCIÓN DE CARGAS EN COCINA</text>
  <text x="70" y="82" fill="#8b949e" font-size="12">Circuito C32 (6 mm²) Inducción/Horno | C20 Prioritario Mini-UPS Refrigerador | C16 Lavavajillas con Detección de Fin de Ciclo</text>

  <!-- PLANO EN PLANTA DE LA COCINA (IZQUIERDA) -->
  <rect x="60" y="120" width="480" height="580" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="80" y="150" fill="#58a6ff" font-size="14" font-weight="bold">DISTRIBUCIÓN EN PLANTA - COCINA (3.5 x 3.2 m)</text>

  <!-- Bancada en L -->
  <rect x="80" y="180" width="420" height="100" fill="#21262d" stroke="#484f58" stroke-width="2"/>
  <rect x="80" y="280" width="120" height="380" fill="#21262d" stroke="#484f58" stroke-width="2"/>

  <!-- Placa de Inducción (C32) -->
  <rect x="230" y="190" width="110" height="80" fill="#30363d" stroke="#f85149" stroke-width="2" rx="4"/>
  <circle cx="260" cy="230" r="18" fill="none" stroke="#f85149" stroke-width="2"/>
  <circle cx="310" cy="230" r="14" fill="none" stroke="#f85149" stroke-width="2"/>
  <text x="240" y="285" fill="#f85149" font-size="10" font-weight="bold">INDUCCIÓN C32 (7.2 kW)</text>

  <!-- Horno Eléctrico bajo encimera -->
  <rect x="360" y="190" width="90" height="80" fill="#30363d" stroke="#f85149" stroke-width="2" rx="4"/>
  <text x="375" y="235" fill="#f85149" font-size="10" font-weight="bold">HORNO C32</text>

  <!-- Fregadero y Lavavajillas -->
  <rect x="90" y="320" width="100" height="100" fill="#1f6feb" stroke="#58a6ff" stroke-width="2" rx="4"/>
  <text x="105" y="370" fill="#ffffff" font-size="11" font-weight="bold">LAVAVAJILLAS</text>
  <text x="105" y="388" fill="#f0f6fc" font-size="9">C16 + Telemetría</text>

  <!-- Refrigerador Combi con Mini-UPS -->
  <rect x="90" y="520" width="100" height="120" fill="#238636" stroke="#2ea043" stroke-width="3" rx="6"/>
  <text x="100" y="570" fill="#ffffff" font-size="12" font-weight="bold">REFRIGERADOR</text>
  <text x="105" y="590" fill="#f0f6fc" font-size="9">Línea C20 Prioritaria</text>

  <!-- Mini-UPS LiFePO4 detrás/sobre refrigerador -->
  <rect x="100" y="605" width="80" height="25" fill="#161b22" stroke="#e3b341" stroke-width="1.5" rx="3"/>
  <text x="110" y="622" fill="#e3b341" font-size="9" font-weight="bold">MINI-UPS 4S</text>

  <!-- DIAGRAMA UNIFILAR DE PROTECCIONES Y METROLOGÍA (DERECHA) -->
  <rect x="560" y="120" width="490" height="580" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="580" y="150" fill="#58a6ff" font-size="14" font-weight="bold">ESQUEMA UNIFILAR DE CUADRO DERIVADO COCINA</text>

  <!-- IGA y Diferencial Superinmunizado -->
  <rect x="580" y="180" width="100" height="40" fill="#21262d" stroke="#58a6ff" stroke-width="1.5" rx="4"/>
  <text x="595" y="205" fill="#58a6ff" font-size="11" font-weight="bold">IGA 40A / 2P</text>

  <rect x="710" y="180" width="120" height="40" fill="#21262d" stroke="#58a6ff" stroke-width="1.5" rx="4"/>
  <text x="720" y="205" fill="#58a6ff" font-size="11" font-weight="bold">ID 40A / 30mA A-SI</text>

  <rect x="850" y="180" width="180" height="40" fill="#21262d" stroke="#d29922" stroke-width="1.5" rx="4"/>
  <text x="860" y="205" fill="#d29922" font-size="10" font-weight="bold">DPS TIPO 3 (Supresor Picos)</text>

  <!-- Circuitos Derivados -->
  <!-- Circuito 1: Inducción y Horno -->
  <path d="M 630 220 L 630 270 L 630 300" stroke="#f85149" stroke-width="3"/>
  <rect x="590" y="300" width="80" height="35" fill="#21262d" stroke="#f85149" stroke-width="2" rx="3"/>
  <text x="605" y="322" fill="#f85149" font-size="11" font-weight="bold">MCB C32</text>
  <text x="680" y="322" fill="#f0f6fc" font-size="11">Cable 6 mm² $\to$ Encimera Inducción + Horno</text>

  <!-- Circuito 2: Refrigerador con Regulador y Mini-UPS -->
  <path d="M 630 270 L 630 380" stroke="#2ea043" stroke-width="3"/>
  <rect x="590" y="380" width="80" height="35" fill="#21262d" stroke="#2ea043" stroke-width="2" rx="3"/>
  <text x="605" y="402" fill="#2ea043" font-size="11" font-weight="bold">MCB C20</text>
  <text x="680" y="395" fill="#2ea043" font-size="11" font-weight="bold">Línea Prioritaria Refrigerador (No cortable)</text>
  <text x="680" y="412" fill="#8b949e" font-size="10">Equipada con Mini-UPS LiFePO4 (Cero microcortes)</text>

  <!-- Circuito 3: Lavavajillas con Shunt Metrológico -->
  <path d="M 630 270 L 630 460" stroke="#388bfd" stroke-width="3"/>
  <rect x="590" y="460" width="80" height="35" fill="#21262d" stroke="#388bfd" stroke-width="2" rx="3"/>
  <text x="605" y="482" fill="#388bfd" font-size="11" font-weight="bold">MCB C16</text>
  <text x="680" y="475" fill="#388bfd" font-size="11" font-weight="bold">Lavavajillas + BL0942 Metrología</text>
  <text x="680" y="492" fill="#8b949e" font-size="10">Notificación fin de ciclo: Caída P &lt; 2.5W tras lavado</text>

  <!-- Circuito 4: Microondas y Pequeños Electrodomésticos -->
  <path d="M 630 270 L 630 540" stroke="#bc8cff" stroke-width="3"/>
  <rect x="590" y="540" width="80" height="35" fill="#21262d" stroke="#bc8cff" stroke-width="2" rx="3"/>
  <text x="605" y="562" fill="#bc8cff" font-size="11" font-weight="bold">MCB C16</text>
  <text x="680" y="562" fill="#f0f6fc" font-size="11">Tomas Encimera + Microondas + Extractor</text>

  <!-- Cuadro de Funciones de Automatización -->
  <rect x="50" y="720" width="1000" height="100" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="70" y="745" fill="#f0f6fc" font-size="12" font-weight="bold">ALGORITMOS DE MONITORIZACIÓN Y TELEMETRÍA:</text>
  <text x="70" y="765" fill="#388bfd" font-size="11">■ Detección Fin de Ciclo Lavavajillas: El sensor BL0942 detecta cuando la potencia desciende por debajo de 3W durante más de 2 min tras el secado a 1800W, enviando notificación a móviles y voz.</text>
  <text x="70" y="785" fill="#2ea043" font-size="11">■ Mini-UPS Refrigerador: Si la red sufre microcortes o apagón, el relé de transferencia conmuta en &lt;10ms a la batería interna LiFePO4 de 12.8V 20Ah, manteniendo el compresor inverter sin despresurizaciones.</text>
  <text x="70" y="805" fill="#f85149" font-size="11">■ Alarma Térmica y Fallo Compresor: Si el consumo del refrigerador supera 350W de forma continuada durante más de 3 horas, se emite alerta de posible puerta abierta o anomalía en el evaporador.</text>
</svg>"""

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Plano SVG generado: {svg_path}")

def generar_plano_cocina_dxf(dxf_path):
    dxf = SimpleDXF(dxf_path)
    # Planta de cocina (3500 x 3200 mm)
    dxf.add_rect(0, 0, 3500, 3200, layer="MUROS_COCINA", color=7)

    # Bancada L
    dxf.add_rect(0, 2600, 3500, 600, layer="BANCADA", color=4) # Cyan
    dxf.add_rect(0, 0, 600, 2600, layer="BANCADA", color=4)

    # Placa inducción (C32 6mm²)
    dxf.add_rect(1200, 2650, 800, 500, layer="INDUCCION_C32", color=1) # Rojo
    dxf.add_text("PLACA INDUCCION 7.2 kW C32 (6 mm2)", 1000, 2550, height=80, layer="TEXTOS", color=1)

    # Lavavajillas
    dxf.add_rect(50, 1200, 500, 600, layer="LAVAVAJILLAS", color=5) # Azul
    dxf.add_text("LAVAVAJILLAS CON METROLOGIA BL0942", 50, 1050, height=80, layer="TEXTOS", color=5)

    # Refrigerador con Mini-UPS
    dxf.add_rect(50, 100, 600, 700, layer="REFRIGERADOR_UPS", color=3) # Verde
    dxf.add_text("REFRIGERADOR + MINI-UPS LiFePO4 C20", 50, 900, height=80, layer="TEXTOS", color=3)

    dxf.save()

if __name__ == "__main__":
    out_dir = "/home/ral/Documents/GitHub/open-source-domotics/04_telemetria_y_cargas_criticas/02_cargas_cocina/mecanico"
    os.makedirs(out_dir, exist_ok=True)
    dxf_file = os.path.join(out_dir, "plano_cargas_cocina.dxf")
    svg_file = os.path.join(out_dir, "plano_cargas_cocina.svg")

    generar_plano_cocina_dxf(dxf_file)
    generar_svg_cocina(svg_file)
