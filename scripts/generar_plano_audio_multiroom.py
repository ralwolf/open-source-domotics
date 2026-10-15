#!/usr/bin/env python3
"""
generar_plano_audio_multiroom.py
Genera los planos CAD 2D en DXF R12 y SVG vectorial de la red de audio distribuido
multiroom de alta fidelidad para la vivienda de 10x10m (6 zonas acústicas independientes).
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

def generar_svg_audio_multiroom(svg_path):
    svg_content = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 1100" width="100%" height="100%" style="background-color: #0d1117; font-family: 'DejaVu Sans', Helvetica, Arial, sans-serif;">
  <defs>
    <pattern id="grid" width="50" height="50" patternUnits="userSpaceOnUse">
      <path d="M 50 0 L 0 0 0 50" fill="none" stroke="#21262d" stroke-width="1"/>
    </pattern>
  </defs>

  <rect width="1100" height="1100" fill="url(#grid)" />

  <!-- Carátula -->
  <rect x="50" y="30" width="1000" height="60" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="70" y="65" fill="#f0f6fc" font-size="20" font-weight="bold">PLANO DE DISTRIBUCIÓN ACÚSTICA: AUDIO MULTIROOM DE ALTA FIDELIDAD (6 ZONAS)</text>
  <text x="70" y="82" fill="#8b949e" font-size="12">Vivienda 10x10m | Amplificación Clase D TAS5805M | Snapcast / Music Assistant | Atenuación Audio Ducking</text>

  <!-- Muros Perimetrales (10x10m = 800x800 px) de (150, 150) a (950, 950) -->
  <rect x="150" y="150" width="800" height="800" fill="none" stroke="#8b949e" stroke-width="4"/>

  <!-- Sala IT Central (Rack de Amplificadores Streamers Hub) -->
  <rect x="470" y="470" width="160" height="160" fill="#161b22" stroke="#484f58" stroke-width="2"/>
  <rect x="500" y="520" width="100" height="70" fill="#21262d" stroke="#58a6ff" stroke-width="2" rx="4"/>
  <text x="510" y="545" fill="#58a6ff" font-size="11" font-weight="bold">HUB STREAMER</text>
  <text x="512" y="565" fill="#8b949e" font-size="9">6x TAS5805M Hi-Fi</text>

  <!-- ZONA 1: SALÓN - COMEDOR (Noreste) -->
  <rect x="530" y="150" width="420" height="320" fill="none" stroke="#30363d" stroke-width="2"/>
  <text x="550" y="180" fill="#58a6ff" font-size="14" font-weight="bold">ZONA 1: SALÓN - COMEDOR (Hi-Fi 60W RMS)</text>
  <!-- Altavoces L y R en falso techo -->
  <circle cx="650" cy="280" r="22" fill="#1f6feb" stroke="#58a6ff" stroke-width="2"/>
  <circle cx="650" cy="280" r="8" fill="#ffffff"/>
  <text x="635" y="320" fill="#58a6ff" font-size="11" font-weight="bold">Z1-L (6.5")</text>

  <circle cx="850" cy="280" r="22" fill="#1f6feb" stroke="#58a6ff" stroke-width="2"/>
  <circle cx="850" cy="280" r="8" fill="#ffffff"/>
  <text x="835" y="320" fill="#58a6ff" font-size="11" font-weight="bold">Z1-R (6.5")</text>

  <!-- Cableado Z1 hacia Rack -->
  <path d="M 650 280 L 650 470 L 530 470 L 530 520" stroke="#58a6ff" stroke-width="2" stroke-dasharray="4,2"/>
  <path d="M 850 280 L 850 490 L 570 490 L 570 520" stroke="#58a6ff" stroke-width="2" stroke-dasharray="4,2"/>

  <!-- ZONA 2: COCINA (Sureste) -->
  <rect x="630" y="600" width="320" height="350" fill="none" stroke="#30363d" stroke-width="2"/>
  <text x="650" y="630" fill="#e3b341" font-size="14" font-weight="bold">ZONA 2: COCINA (IP44 Antihumedad 40W)</text>
  <circle cx="720" cy="740" r="20" fill="#d29922" stroke="#e3b341" stroke-width="2"/>
  <circle cx="720" cy="740" r="7" fill="#ffffff"/>
  <text x="705" y="780" fill="#e3b341" font-size="11" font-weight="bold">Z2-L (5.25")</text>

  <circle cx="860" cy="740" r="20" fill="#d29922" stroke="#e3b341" stroke-width="2"/>
  <circle cx="860" cy="740" r="7" fill="#ffffff"/>
  <text x="845" y="780" fill="#e3b341" font-size="11" font-weight="bold">Z2-R (5.25")</text>
  <path d="M 720 740 L 720 620 L 570 620 L 570 590" stroke="#e3b341" stroke-width="2" stroke-dasharray="4,2"/>

  <!-- ZONA 3: DORMITORIO PRINCIPAL (Noroeste) -->
  <rect x="150" y="150" width="380" height="320" fill="none" stroke="#30363d" stroke-width="2"/>
  <text x="170" y="180" fill="#2ea043" font-size="14" font-weight="bold">ZONA 3: DORMITORIO PRINCIPAL (50W RMS)</text>
  <circle cx="260" cy="280" r="22" fill="#238636" stroke="#2ea043" stroke-width="2"/>
  <circle cx="260" cy="280" r="8" fill="#ffffff"/>
  <text x="245" y="320" fill="#2ea043" font-size="11" font-weight="bold">Z3-L (6.5")</text>

  <circle cx="420" cy="280" r="22" fill="#238636" stroke="#2ea043" stroke-width="2"/>
  <circle cx="420" cy="280" r="8" fill="#ffffff"/>
  <text x="405" y="320" fill="#2ea043" font-size="11" font-weight="bold">Z3-R (6.5")</text>
  <path d="M 260 280 L 260 480 L 500 480 L 500 520" stroke="#2ea043" stroke-width="2" stroke-dasharray="4,2"/>

  <!-- ZONA 4: DORMITORIO INFANTIL / ESTUDIO (Suroeste) -->
  <rect x="150" y="570" width="320" height="380" fill="none" stroke="#30363d" stroke-width="2"/>
  <text x="170" y="600" fill="#a371f7" font-size="14" font-weight="bold">ZONA 4: ESTUDIO / INFANTIL (40W)</text>
  <circle cx="250" cy="730" r="20" fill="#8957e5" stroke="#a371f7" stroke-width="2"/>
  <circle cx="250" cy="730" r="7" fill="#ffffff"/>
  <text x="235" y="770" fill="#a371f7" font-size="11" font-weight="bold">Z4-L (5.25")</text>

  <circle cx="390" cy="730" r="20" fill="#8957e5" stroke="#a371f7" stroke-width="2"/>
  <circle cx="390" cy="730" r="7" fill="#ffffff"/>
  <text x="375" y="770" fill="#a371f7" font-size="11" font-weight="bold">Z4-R (5.25")</text>
  <path d="M 250 730 L 250 620 L 500 620 L 500 590" stroke="#a371f7" stroke-width="2" stroke-dasharray="4,2"/>

  <!-- ZONA 5: BAÑO PRINCIPAL (Sur Central) -->
  <rect x="470" y="700" width="160" height="250" fill="none" stroke="#30363d" stroke-width="2"/>
  <text x="480" y="730" fill="#f0883e" font-size="13" font-weight="bold">ZONA 5: BAÑO</text>
  <circle cx="550" cy="810" r="22" fill="#bd561d" stroke="#f0883e" stroke-width="2"/>
  <circle cx="550" cy="810" r="8" fill="#ffffff"/>
  <text x="515" y="850" fill="#f0883e" font-size="10" font-weight="bold">Z5: Dual Stereo IP44</text>
  <path d="M 550 810 L 550 590" stroke="#f0883e" stroke-width="2" stroke-dasharray="4,2"/>

  <!-- ZONA 6: TERRAZA / JARDÍN EXTERIOR (Norte Exterior) -->
  <rect x="350" y="90" width="400" height="50" fill="#161b22" stroke="#f85149" stroke-width="1.5" rx="4"/>
  <text x="365" y="115" fill="#f85149" font-size="12" font-weight="bold">ZONA 6: TERRAZA / PISCINA (Intemperie IP65 60W RMS)</text>
  <circle cx="380" cy="120" r="16" fill="#da3633" stroke="#f85149" stroke-width="2"/>
  <circle cx="720" cy="120" r="16" fill="#da3633" stroke="#f85149" stroke-width="2"/>

  <!-- Especificaciones Técnicas y Ducking -->
  <rect x="50" y="970" width="1000" height="100" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="70" y="995" fill="#f0f6fc" font-size="12" font-weight="bold">ESPECIFICACIONES DE INTEGRACIÓN Y AUDIO DUCKING:</text>
  <text x="70" y="1015" fill="#58a6ff" font-size="11">■ Cableado: Manguera libre de oxígeno (OFC 99.99%) 2x1.5 mm² apantallada, segregada de líneas de fuerza 230V.</text>
  <text x="70" y="1035" fill="#2ea043" font-size="11">■ Music Assistant &amp; Snapcast: Agrupación en tiempo real (Party Mode síncrono &lt;2ms) o reproducción individual independiente por zona.</text>
  <text x="70" y="1055" fill="#f85149" font-size="11">■ Audio Ducking Automático: Al detectar llamada de videoportero o alerta de seguridad (fuego/intrusión), la música se atenúa en un 80% en todas las zonas activas.</text>
</svg>"""

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Plano SVG generado: {svg_path}")

def generar_plano_audio_dxf(dxf_path):
    dxf = SimpleDXF(dxf_path)
    # Perímetro vivienda 10x10 m (10000x10000 mm)
    dxf.add_rect(0, 0, 10000, 10000, layer="MUROS_PERIMETRALES", color=7)

    # Sala IT central
    dxf.add_rect(4700, 4700, 1600, 1600, layer="SALA_IT", color=4)
    dxf.add_text("RACK CENTRAL - HUB STREAMERS MULTIROOM", 4800, 5500, height=150, layer="TEXTOS", color=4)

    # Zona 1: Salón
    dxf.add_circle(6500, 2800, 200, layer="ALTAVOCES_ZONA1", color=5) # Azul
    dxf.add_circle(8500, 2800, 200, layer="ALTAVOCES_ZONA1", color=5)
    dxf.add_text("ALTAVOCES SALON (Z1-L / Z1-R 60W)", 6500, 2400, height=150, layer="TEXTOS", color=5)

    # Zona 2: Cocina
    dxf.add_circle(7200, 7400, 180, layer="ALTAVOCES_ZONA2", color=2) # Amarillo
    dxf.add_circle(8600, 7400, 180, layer="ALTAVOCES_ZONA2", color=2)
    dxf.add_text("ALTAVOCES COCINA IP44 (Z2-L / Z2-R)", 7200, 8000, height=150, layer="TEXTOS", color=2)

    # Zona 3: Dormitorio Principal
    dxf.add_circle(2600, 2800, 200, layer="ALTAVOCES_ZONA3", color=3) # Verde
    dxf.add_circle(4200, 2800, 200, layer="ALTAVOCES_ZONA3", color=3)
    dxf.add_text("ALTAVOCES DORMITORIO PPAL (Z3)", 2600, 2400, height=150, layer="TEXTOS", color=3)

    # Zona 4: Dormitorio Infantil
    dxf.add_circle(2500, 7300, 180, layer="ALTAVOCES_ZONA4", color=6) # Magenta
    dxf.add_circle(3900, 7300, 180, layer="ALTAVOCES_ZONA4", color=6)
    dxf.add_text("ALTAVOCES INFANTIL/ESTUDIO (Z4)", 2500, 8000, height=150, layer="TEXTOS", color=6)

    # Zona 5: Baño
    dxf.add_circle(5500, 8100, 200, layer="ALTAVOCES_ZONA5", color=1) # Rojo
    dxf.add_text("ALTAVOZ BANO DUAL STEREO IP44 (Z5)", 4800, 8600, height=150, layer="TEXTOS", color=1)

    dxf.save()

if __name__ == "__main__":
    out_dir = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/05_audio_distribuido_multiroom/mecanico"
    os.makedirs(out_dir, exist_ok=True)
    dxf_file = os.path.join(out_dir, "plano_distribucion_audio_multiroom.dxf")
    svg_file = os.path.join(out_dir, "plano_distribucion_audio_multiroom.svg")

    generar_plano_audio_dxf(dxf_file)
    generar_svg_audio_multiroom(svg_file)

