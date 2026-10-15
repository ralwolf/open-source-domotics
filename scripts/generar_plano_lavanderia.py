#!/usr/bin/env python3
"""
generar_plano_lavanderia.py
Genera los planos CAD 2D en DXF R12 y SVG vectorial de la instalación de potencia,
protección contra sobretensiones y seguridad contra inundación en la lavandería.
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

def generar_svg_lavanderia(svg_path):
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
  <text x="70" y="65" fill="#f0f6fc" font-size="18" font-weight="bold">INSTALACIÓN ELÉCTRICA, TELEMETRÍA Y SEGURIDAD ANTI-INUNDACIÓN: LAVANDERÍA</text>
  <text x="70" y="82" fill="#8b949e" font-size="12">Circuito C20 (4 mm²) | Base Estanca IP55 | Detección Fin de Ciclo | Electroválvula de Corte Inmediato de Agua</text>

  <!-- PLANTA DE LAVANDERÍA (IZQUIERDA) -->
  <rect x="60" y="120" width="480" height="580" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="80" y="150" fill="#58a6ff" font-size="14" font-weight="bold">DISTRIBUCIÓN EN PLANTA - LAVANDERÍA (2.2 x 2.0 m)</text>

  <!-- Lavadora de Carga Frontal (60 x 60 cm) -->
  <rect x="100" y="220" width="160" height="160" fill="#21262d" stroke="#58a6ff" stroke-width="3" rx="8"/>
  <circle cx="180" cy="300" r="50" fill="#161b22" stroke="#58a6ff" stroke-width="2"/>
  <text x="135" y="305" fill="#58a6ff" font-size="12" font-weight="bold">LAVADORA</text>
  <text x="130" y="325" fill="#8b949e" font-size="10">1400 RPM / 2.2 kW</text>

  <!-- Secadora con Bomba de Calor (60 x 60 cm) -->
  <rect x="290" y="220" width="160" height="160" fill="#21262d" stroke="#58a6ff" stroke-width="3" rx="8"/>
  <circle cx="370" cy="300" r="50" fill="#161b22" stroke="#58a6ff" stroke-width="2"/>
  <text x="330" y="305" fill="#58a6ff" font-size="12" font-weight="bold">SECADORA</text>
  <text x="325" y="325" fill="#8b949e" font-size="10">Bomba Calor 900W</text>

  <!-- Base Antivibratoria de Caucho EPDM bajo máquinas -->
  <rect x="90" y="385" width="370" height="15" fill="#d29922" rx="3"/>
  <text x="160" y="396" fill="#0d1117" font-size="10" font-weight="bold">ALFOMBRA / BASE ANTIVIBRATORIA EPDM</text>

  <!-- Base de Enchufe Doble Estanca IP55 en Pared -->
  <rect x="225" y="150" width="100" height="40" fill="#1f6feb" stroke="#58a6ff" stroke-width="2" rx="4"/>
  <text x="240" y="175" fill="#ffffff" font-size="11" font-weight="bold">ENCHUFE IP55</text>

  <!-- Sensor de Inundación en Suelo -->
  <circle cx="275" cy="520" r="25" fill="#da3633" stroke="#f85149" stroke-width="2"/>
  <text x="260" y="525" fill="#ffffff" font-size="10" font-weight="bold">SONDA</text>
  <text x="200" y="560" fill="#f85149" font-size="11" font-weight="bold">SENSOR INUNDACIÓN SUELO</text>

  <!-- Toma de Agua y Electroválvula de Corte Solenoide 12V -->
  <rect x="100" y="150" width="50" height="30" fill="#238636" stroke="#2ea043" stroke-width="2" rx="3"/>
  <text x="108" y="170" fill="#ffffff" font-size="10" font-weight="bold">CORTE</text>
  <text x="70" y="140" fill="#2ea043" font-size="10" font-weight="bold">Válvula Corte 3/4"</text>

  <!-- ESQUEMA ELÉCTRICO Y DE SEGURIDAD (DERECHA) -->
  <rect x="560" y="120" width="490" height="580" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="580" y="150" fill="#58a6ff" font-size="14" font-weight="bold">CIRCUITO ELÉCTRICO C20 Y ENCLAVAMIENTO DE AGUA</text>

  <!-- Cuadro C20 -->
  <rect x="580" y="190" width="100" height="45" fill="#21262d" stroke="#58a6ff" stroke-width="2" rx="4"/>
  <text x="595" y="218" fill="#58a6ff" font-size="12" font-weight="bold">MCB C20</text>
  <text x="700" y="218" fill="#f0f6fc" font-size="12">Línea C20 (Cable 4 mm²) $\to$ Lavandería</text>

  <rect x="580" y="255" width="120" height="45" fill="#21262d" stroke="#58a6ff" stroke-width="2" rx="4"/>
  <text x="590" y="282" fill="#58a6ff" font-size="11" font-weight="bold">RCD 30mA A-SI</text>
  <text x="720" y="282" fill="#8b949e" font-size="11">Protección diferencial alta inmunidad</text>

  <rect x="580" y="320" width="100" height="45" fill="#21262d" stroke="#d29922" stroke-width="2" rx="4"/>
  <text x="595" y="348" fill="#d29922" font-size="11" font-weight="bold">SPD TIPO 3</text>
  <text x="700" y="348" fill="#d29922" font-size="11">Supresor de picos transitorios</text>

  <!-- Controlador IoT Lavandería y Relés -->
  <rect x="620" y="410" width="370" height="150" fill="#21262d" stroke="#2ea043" stroke-width="2" rx="6"/>
  <text x="640" y="440" fill="#2ea043" font-size="13" font-weight="bold">CONTROLADOR IOT LAVANDERÍA (ESP32-C3)</text>
  <text x="640" y="465" fill="#f0f6fc" font-size="11">■ Metrología BL0942 (16A continuo): Potencia en tiempo real</text>
  <text x="640" y="490" fill="#f0f6fc" font-size="11">■ Entrada Sensor de Inundación: Detección óptica/resistiva</text>
  <text x="640" y="515" fill="#f0f6fc" font-size="11">■ Salida MOSFET 12V 1.5A: Cierre instantáneo válvula de agua</text>
  <text x="640" y="540" fill="#f0f6fc" font-size="11">■ Relé Desconexión 16A: Desenergiza el enchufe si hay agua</text>

  <!-- Pie de plano -->
  <rect x="50" y="720" width="1000" height="100" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="70" y="745" fill="#f0f6fc" font-size="12" font-weight="bold">LÓGICAS DE SEGURIDAD Y TELEMETRÍA EN LAVANDERÍA:</text>
  <text x="70" y="765" fill="#f85149" font-size="11">■ Enclavamiento Anti-Inundación (&lt;50ms): Al detectarse presencia de líquido en el suelo, el microcontrolador corta la electroválvula de entrada de agua y desenergiza las tomas de corriente para evitar electrocución.</text>
  <text x="70" y="785" fill="#388bfd" font-size="11">■ Detección Fin de Ciclo: Reconoce el ciclo de centrifugado (picos de 400-600W de motor) seguido del descenso a &lt;2W continuo por 90s, emitiendo alerta sonora en toda la casa.</text>
  <text x="70" y="805" fill="#e3b341" font-size="11">■ Aislamiento de Vibración: La base elastomérica de 15 mm absorbe la energía cinética del centrifugado a 1400 RPM, protegiendo la estructura de la vivienda.</text>
</svg>"""

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Plano SVG generado: {svg_path}")

def generar_plano_lavanderia_dxf(dxf_path):
    dxf = SimpleDXF(dxf_path)
    # Planta de lavandería (2200 x 2000 mm)
    dxf.add_rect(0, 0, 2200, 2000, layer="MUROS_LAVANDERIA", color=7)

    # Lavadora (600x600 mm)
    dxf.add_rect(200, 200, 600, 600, layer="LAVADORA", color=4)
    dxf.add_circle(500, 500, 200, layer="TAMBOR", color=4)
    dxf.add_text("LAVADORA 1400 RPM", 250, 450, height=50, layer="TEXTOS", color=4)

    # Secadora (600x600 mm)
    dxf.add_rect(900, 200, 600, 600, layer="SECADORA", color=4)
    dxf.add_circle(1200, 500, 200, layer="TAMBOR", color=4)
    dxf.add_text("SECADORA BOMBA CALOR", 950, 450, height=50, layer="TEXTOS", color=4)

    # Sonda inundación
    dxf.add_circle(850, 1200, 100, layer="SENSOR_INUNDACION", color=1)
    dxf.add_text("SENSOR INUNDACION SUELO", 600, 1400, height=60, layer="TEXTOS", color=1)

    # Electroválvula corte agua
    dxf.add_rect(200, 1000, 200, 150, layer="VALVULA_AGUA", color=3)
    dxf.add_text("ELECTROVALVULA CORTE AGUA", 150, 1200, height=50, layer="TEXTOS", color=3)

    dxf.save()

if __name__ == "__main__":
    out_dir = "/home/ral/Documents/GitHub/open-source-domotics/04_telemetria_y_cargas_criticas/03_cargas_lavanderia/mecanico"
    os.makedirs(out_dir, exist_ok=True)
    dxf_file = os.path.join(out_dir, "plano_cargas_lavanderia_seguridad.dxf")
    svg_file = os.path.join(out_dir, "plano_cargas_lavanderia_seguridad.svg")

    generar_plano_lavanderia_dxf(dxf_file)
    generar_svg_lavanderia(svg_file)

