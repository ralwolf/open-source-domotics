#!/usr/bin/env python3
"""
generar_plano_multisplit.py
Genera los planos CAD 2D en DXF R12 y SVG vectorial de la instalación de climatización
Multi-Split Inverter: bancada exterior antivibratoria, trazado frigorífico, drenaje y control IoT.
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

def generar_svg_multisplit(svg_path):
    svg_content = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 850" width="100%" height="100%" style="background-color: #0d1117; font-family: 'DejaVu Sans', Helvetica, Arial, sans-serif;">
  <defs>
    <pattern id="grid" width="50" height="50" patternUnits="userSpaceOnUse">
      <path d="M 50 0 L 0 0 0 50" fill="none" stroke="#21262d" stroke-width="1"/>
    </pattern>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M 0 0 L 8 4 L 0 8 Z" fill="#58a6ff" />
    </marker>
  </defs>

  <rect width="1100" height="850" fill="url(#grid)" />

  <!-- Carátula -->
  <rect x="50" y="30" width="1000" height="60" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="70" y="65" fill="#f0f6fc" font-size="18" font-weight="bold">ESQUEMA DE INSTALACIÓN FRIGORÍFICA, ELÉCTRICA Y CONTROL IOT: MULTI-SPLIT INVERTER</text>
  <text x="70" y="82" fill="#8b949e" font-size="12">Líneas Frigoríficas 1/4" - 3/8" Aisladas | Bancada Silentblocks EPDM | Pasarela UART CN105 ESPHome | Interbloqueo Ventana</text>

  <!-- Muro de Fachada Exterior / Interior (Separación) -->
  <rect x="520" y="120" width="60" height="580" fill="#21262d" stroke="#484f58" stroke-width="2"/>
  <text x="535" y="440" fill="#8b949e" font-size="13" font-weight="bold" transform="rotate(-90 535,440)">MURO FACHADA AISLADO (25 cm)</text>

  <!-- ZONA EXTERIOR (IZQUIERDA) -->
  <text x="150" y="150" fill="#f85149" font-size="16" font-weight="bold">EXTERIOR (FACHADA / CUBIERTA)</text>

  <!-- Unidad Condensadora Exterior Inverter -->
  <rect x="120" y="240" width="280" height="220" fill="#161b22" stroke="#58a6ff" stroke-width="3" rx="8"/>
  <circle cx="260" cy="350" r="75" fill="#21262d" stroke="#58a6ff" stroke-width="2"/>
  <text x="210" y="355" fill="#58a6ff" font-size="12" font-weight="bold">VENTILADOR EC</text>
  <text x="140" y="270" fill="#f0f6fc" font-size="13" font-weight="bold">UNIDAD EXTERIOR INVERTER</text>
  <text x="140" y="290" fill="#8b949e" font-size="11">R32 / 3.5 kW Térmicos | SEER 8.5 (A+++)</text>

  <!-- Bancada Antivibratoria y Silentblocks EPDM -->
  <rect x="100" y="460" width="320" height="15" fill="#8b949e" stroke="#c9d1d9" stroke-width="1.5"/>
  <rect x="140" y="475" width="40" height="25" fill="#e3b341" rx="4"/>
  <rect x="340" y="475" width="40" height="25" fill="#e3b341" rx="4"/>
  <text x="195" y="492" fill="#e3b341" font-size="11" font-weight="bold">SILENTBLOCKS EPDM (Anti-vibración)</text>

  <!-- Cuadro de Protección Exterior C16 -->
  <rect x="120" y="530" width="160" height="120" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="135" y="555" fill="#f0f6fc" font-size="11" font-weight="bold">CUADRO LOCAL EXT</text>
  <text x="135" y="575" fill="#8b949e" font-size="10">■ Magnetotérmico C16</text>
  <text x="135" y="595" fill="#8b949e" font-size="10">■ Relé Retardo 3-5 min</text>
  <text x="135" y="615" fill="#8b949e" font-size="10">■ Medidor de Energía</text>

  <!-- ZONA INTERIOR (DERECHA) -->
  <text x="680" y="150" fill="#2ea043" font-size="16" font-weight="bold">INTERIOR (SALÓN / DORMITORIO)</text>

  <!-- Unidad Evaporadora Interior Split -->
  <rect x="650" y="220" width="360" height="130" fill="#161b22" stroke="#2ea043" stroke-width="3" rx="8"/>
  <text x="670" y="255" fill="#f0f6fc" font-size="14" font-weight="bold">UNIDAD INTERIOR SPLIT MURAL</text>
  <text x="670" y="275" fill="#8b949e" font-size="11">Batería Evaporadora + Vane Oscilante 3D</text>

  <!-- Pasarela IoT empotrada dentro del split -->
  <rect x="910" y="235" width="85" height="50" fill="#1f6feb" stroke="#58a6ff" stroke-width="1.5" rx="4"/>
  <text x="915" y="255" fill="#ffffff" font-size="9" font-weight="bold">PASARELA IoT</text>
  <text x="918" y="270" fill="#f0f6fc" font-size="8">ESP32 CN105</text>

  <!-- Tubo Frigorífico 1/4" Líquido (Rojo/Naranja) -->
  <path d="M 400 300 L 520 300 L 580 300 L 650 300" stroke="#f0883e" stroke-width="4" stroke-dasharray="4,2"/>
  <text x="430" y="290" fill="#f0883e" font-size="10" font-weight="bold">Líquido 1/4"</text>

  <!-- Tubo Frigorífico 3/8" Gas (Azul) -->
  <path d="M 400 320 L 520 320 L 580 320 L 650 320" stroke="#388bfd" stroke-width="6"/>
  <text x="430" y="340" fill="#388bfd" font-size="10" font-weight="bold">Gas 3/8" (Aislado 13mm)</text>

  <!-- Tubería de Desagüe de Condensados (Verde) -->
  <path d="M 650 340 L 580 360 L 520 380 L 460 400 L 460 620" stroke="#2ea043" stroke-width="4"/>
  <text x="600" y="375" fill="#2ea043" font-size="10" font-weight="bold">Drenaje Condensados (Pendiente ≥ 1.5%)</text>

  <!-- Ventana y Sensor Magnético de Seguridad -->
  <rect x="750" y="430" width="160" height="180" fill="#21262d" stroke="#58a6ff" stroke-width="2"/>
  <text x="770" y="460" fill="#c9d1d9" font-size="12" font-weight="bold">VENTANA HABITACIÓN</text>

  <!-- Sensor Magnético Reed Switch -->
  <rect x="740" y="470" width="10" height="30" fill="#d29922"/>
  <rect x="752" y="470" width="10" height="30" fill="#d29922"/>
  <text x="660" y="490" fill="#d29922" font-size="10" font-weight="bold">SENSOR REED</text>
  <!-- Cable hacia pasarela IoT -->
  <path d="M 740 485 L 700 485 L 700 320 L 910 280" stroke="#d29922" stroke-width="1.5" stroke-dasharray="3,3"/>

  <!-- Sensor SHT31 Ambiente a altura ergonómica (1.5m) -->
  <rect x="940" y="520" width="40" height="40" fill="#161b22" stroke="#58a6ff" stroke-width="2" rx="4"/>
  <text x="945" y="545" fill="#58a6ff" font-size="9" font-weight="bold">SHT31</text>
  <text x="900" y="580" fill="#8b949e" font-size="10">Temp/HR a 1.5m</text>

  <!-- Pie de plano con lógica operativa -->
  <rect x="50" y="720" width="1000" height="100" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="70" y="745" fill="#f0f6fc" font-size="12" font-weight="bold">LÓGICAS DE INTEGRACIÓN ENERGÉTICA Y PROTECCIÓN:</text>
  <text x="70" y="765" fill="#2ea043" font-size="11">■ Apagado por Ventana Abierta: Si el sensor magnético detecta apertura &gt; 3 min, el split apaga el compresor para evitar pérdidas. Al cerrar, reanuda consigna.</text>
  <text x="70" y="785" fill="#388bfd" font-size="11">■ Climatización Solar por Excedentes: Si el banco ESS LiFePO4 está al 100% y hay producción solar excedente, la consigna se modula automáticamente para acumulación térmica.</text>
  <text x="70" y="805" fill="#e3b341" font-size="11">■ Protección de Compresor: El cuadro eléctrico exterior incorpora retardo de reenganche de 3 a 5 minutos para ecualización de presiones de gas R32 tras cortes eléctricos.</text>
</svg>"""

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Plano SVG generado: {svg_path}")

def generar_plano_multisplit_dxf(dxf_path):
    dxf = SimpleDXF(dxf_path)
    # Muro de fachada (5000 mm x 250 mm)
    dxf.add_rect(5000, 0, 250, 4000, layer="MURO_FACHADA", color=7)

    # Unidad exterior (800x600 mm) en bancada
    dxf.add_rect(3800, 1000, 800, 600, layer="UNIDAD_EXTERIOR", color=4) # Cyan
    dxf.add_circle(4200, 1300, 250, layer="VENTILADOR_EXTERIOR", color=4)
    dxf.add_text("UNIDAD CONDENSADORA INVERTER R32", 3600, 1700, height=100, layer="TEXTOS", color=4)

    # Silentblocks
    dxf.add_rect(3900, 900, 100, 80, layer="SILENTBLOCKS", color=2)
    dxf.add_rect(4400, 900, 100, 80, layer="SILENTBLOCKS", color=2)

    # Unidad interior split (900x300 mm)
    dxf.add_rect(5500, 2500, 900, 300, layer="UNIDAD_INTERIOR", color=3) # Verde
    dxf.add_text("UNIDAD SPLIT INTERIOR CON PASARELA CN105", 5500, 2900, height=100, layer="TEXTOS", color=3)

    # Tuberías frigoríficas (1/4" y 3/8")
    dxf.add_line(4600, 1400, 5500, 2500, layer="LINEA_GAS_3_8", color=1) # Rojo
    dxf.add_line(4600, 1350, 5500, 2450, layer="LINEA_LIQUIDO_1_4", color=5) # Azul

    # Drenaje
    dxf.add_line(5500, 2400, 4800, 500, layer="DRENAJE_CONDENSADOS", color=3)

    dxf.save()

if __name__ == "__main__":
    out_dir = "/home/ral/Documents/GitHub/open-source-domotics/04_telemetria_y_cargas_criticas/05_climatizacion_multisplit/mecanico"
    os.makedirs(out_dir, exist_ok=True)
    dxf_file = os.path.join(out_dir, "plano_instalacion_multisplit.dxf")
    svg_file = os.path.join(out_dir, "plano_instalacion_multisplit.svg")

    generar_plano_multisplit_dxf(dxf_file)
    generar_svg_multisplit(svg_file)

