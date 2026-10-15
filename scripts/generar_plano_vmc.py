#!/usr/bin/env python3
"""
generar_plano_vmc.py
Genera los planos CAD 2D en DXF R12 y SVG vectorial de la red de conductos de
Ventilación Mecánica Controlada (VMC) de doble flujo para la vivienda de 10x10m.
"""

import os
import math

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

def generar_svg_vmc(svg_path):
    # Coordenadas 10x10m escaladas a 1000x1000 px
    svg_content = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 1100" width="100%" height="100%" style="background-color: #0d1117; font-family: 'DejaVu Sans', Helvetica, Arial, sans-serif;">
  <defs>
    <pattern id="grid" width="50" height="50" patternUnits="userSpaceOnUse">
      <path d="M 50 0 L 0 0 0 50" fill="none" stroke="#21262d" stroke-width="1"/>
    </pattern>
    <marker id="arrow_blue" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M 0 0 L 8 4 L 0 8 Z" fill="#388bfd" />
    </marker>
    <marker id="arrow_red" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M 0 0 L 8 4 L 0 8 Z" fill="#f85149" />
    </marker>
  </defs>

  <rect width="1100" height="1100" fill="url(#grid)" />

  <!-- Título y Carátula -->
  <rect x="50" y="30" width="1000" height="60" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="70" y="65" fill="#f0f6fc" font-size="20" font-weight="bold">PLANO DE DISTRIBUCIÓN DE CONDUCTOS Y CLIMATIZACIÓN VMC DE DOBLE FLUJO</text>
  <text x="70" y="82" fill="#8b949e" font-size="12">Vivienda Bioclimática 10x10m | Unidad Recuperadora Entálpica 92% | Conductos Antibacterianos DN90 | Bypass Free-Cooling</text>

  <!-- Muros Perimetrales (10x10m = 800x800 px) de (150, 150) a (950, 950) -->
  <rect x="150" y="150" width="800" height="800" fill="none" stroke="#8b949e" stroke-width="4"/>

  <!-- Muros Interiores -->
  <!-- Sala IT Central (470, 470) a (630, 630) -->
  <rect x="470" y="470" width="160" height="160" fill="#161b22" stroke="#484f58" stroke-width="2"/>
  <text x="485" y="495" fill="#58a6ff" font-size="12" font-weight="bold">SALA IT TÉCNICA</text>
  <text x="485" y="510" fill="#8b949e" font-size="10">Ubicación Unidad VMC</text>

  <!-- Unidad VMC física en falso techo IT -->
  <rect x="500" y="520" width="100" height="90" fill="#21262d" stroke="#58a6ff" stroke-width="2" rx="4"/>
  <text x="515" y="565" fill="#58a6ff" font-size="11" font-weight="bold">UNIDAD VMC</text>
  <text x="510" y="580" fill="#8b949e" font-size="9">Bypass 24V / F7</text>

  <!-- Estancias -->
  <!-- Dormitorio Principal (Noroeste) -->
  <rect x="150" y="150" width="380" height="320" fill="none" stroke="#30363d" stroke-width="2"/>
  <text x="170" y="180" fill="#c9d1d9" font-size="14" font-weight="bold">DORMITORIO PRINCIPAL (Seco)</text>
  <text x="170" y="198" fill="#8b949e" font-size="11">Impulsión Aire Limpio: 45 m³/h | Bocas DN90</text>

  <!-- Dormitorio Infantil / Estudio (Suroeste) -->
  <rect x="150" y="570" width="320" height="380" fill="none" stroke="#30363d" stroke-width="2"/>
  <text x="170" y="600" fill="#c9d1d9" font-size="14" font-weight="bold">DORMITORIO INFANTIL (Seco)</text>
  <text x="170" y="618" fill="#8b949e" font-size="11">Impulsión Aire Limpio: 30 m³/h | Bocas DN90</text>

  <!-- Salón / Comedor (Este - Noreste) -->
  <rect x="530" y="150" width="420" height="380" fill="none" stroke="#30363d" stroke-width="2"/>
  <text x="550" y="180" fill="#c9d1d9" font-size="14" font-weight="bold">SALÓN - COMEDOR (Seco)</text>
  <text x="550" y="198" fill="#8b949e" font-size="11">Impulsión Aire Limpio: 60 m³/h | Bocas DN90</text>

  <!-- Cocina (Sureste) -->
  <rect x="630" y="600" width="320" height="350" fill="none" stroke="#30363d" stroke-width="2"/>
  <text x="650" y="630" fill="#c9d1d9" font-size="14" font-weight="bold">COCINA (Húmeda)</text>
  <text x="650" y="648" fill="#8b949e" font-size="11">Extracción Aire Viciado: 60 m³/h | Bocas DN90</text>

  <!-- Baño Principal (Sur Central) -->
  <rect x="470" y="700" width="160" height="250" fill="none" stroke="#30363d" stroke-width="2"/>
  <text x="480" y="730" fill="#c9d1d9" font-size="13" font-weight="bold">BAÑO (Húmedo)</text>
  <text x="480" y="748" fill="#8b949e" font-size="10">Extracción: 35 m³/h</text>

  <!-- RED DE CONDUCTOS AZUL (IMPULSIÓN DE AIRE LIMPIO FILTRADO) -->
  <!-- Silenciador acústico primario -->
  <rect x="580" y="495" width="40" height="20" fill="#1f6feb" stroke="#58a6ff" stroke-width="1.5" rx="3"/>
  <text x="583" y="508" fill="#ffffff" font-size="8">SILENC</text>

  <!-- Tuberías de Impulsión (Azul) -->
  <!-- A Salón -->
  <path d="M 600 520 L 600 480 L 750 480 L 750 250" fill="none" stroke="#388bfd" stroke-width="4" stroke-dasharray="6,3" marker-end="url(#arrow_blue)"/>
  <!-- Bocas de impulsión Salón -->
  <circle cx="750" cy="250" r="14" fill="#1f6feb" stroke="#58a6ff" stroke-width="2"/>
  <text x="735" y="240" fill="#58a6ff" font-size="10" font-weight="bold">IMP-01</text>

  <!-- A Dormitorio Principal -->
  <path d="M 520 520 L 520 450 L 320 450 L 320 250" fill="none" stroke="#388bfd" stroke-width="4" stroke-dasharray="6,3" marker-end="url(#arrow_blue)"/>
  <!-- Boca Dormitorio Principal -->
  <circle cx="320" cy="250" r="14" fill="#1f6feb" stroke="#58a6ff" stroke-width="2"/>
  <text x="305" y="240" fill="#58a6ff" font-size="10" font-weight="bold">IMP-02</text>

  <!-- A Dormitorio Infantil -->
  <path d="M 500 550 L 400 550 L 400 750 L 280 750" fill="none" stroke="#388bfd" stroke-width="4" stroke-dasharray="6,3" marker-end="url(#arrow_blue)"/>
  <circle cx="280" cy="750" r="14" fill="#1f6feb" stroke="#58a6ff" stroke-width="2"/>
  <text x="265" y="740" fill="#58a6ff" font-size="10" font-weight="bold">IMP-03</text>

  <!-- RED DE CONDUCTOS ROJA (EXTRACCIÓN DE AIRE VICIADO) -->
  <!-- De Cocina -->
  <path d="M 780 750 L 780 620 L 580 620 L 580 590" fill="none" stroke="#f85149" stroke-width="4" marker-end="url(#arrow_red)"/>
  <circle cx="780" cy="750" r="14" fill="#da3633" stroke="#f85149" stroke-width="2"/>
  <text x="765" y="780" fill="#f85149" font-size="10" font-weight="bold">EXT-01 (Cocina)</text>

  <!-- De Baño -->
  <path d="M 550 820 L 550 610" fill="none" stroke="#f85149" stroke-width="4" marker-end="url(#arrow_red)"/>
  <circle cx="550" cy="820" r="14" fill="#da3633" stroke="#f85149" stroke-width="2"/>
  <text x="535" y="850" fill="#f85149" font-size="10" font-weight="bold">EXT-02 (Baño)</text>

  <!-- CONDUCTOS EXTERIORES DN160 AISLADOS -->
  <!-- Toma de aire exterior fachada Norte -->
  <path d="M 500 530 L 440 530 L 440 150" fill="none" stroke="#2ea043" stroke-width="6" stroke-linecap="round"/>
  <text x="350" y="140" fill="#2ea043" font-size="11" font-weight="bold">TOMA AIRE EXTERIOR DN160 (Rejilla Fachada Norte)</text>

  <!-- Expulsión a cubierta / fachada -->
  <path d="M 600 550 L 660 550 L 660 150" fill="none" stroke="#8b949e" stroke-width="6" stroke-linecap="round"/>
  <text x="670" y="140" fill="#8b949e" font-size="11" font-weight="bold">EXPULSIÓN AIRE VICIADO DN160 (Fachada)</text>

  <!-- Cuadro de Leyenda y Especificaciones -->
  <rect x="50" y="970" width="1000" height="100" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="70" y="995" fill="#f0f6fc" font-size="12" font-weight="bold">PARÁMETROS DE DISEÑO HIGROTÉRMICO Y CONTROL:</text>
  <text x="70" y="1015" fill="#388bfd" font-size="11">■ Impulsión Aire Nuevo (DN90): 135 m³/h total modulada por CO2 (&lt;800 ppm: Vel 1 (60 m³/h), 800-1100: Vel 2 (120 m³/h), &gt;1100: Boost (210 m³/h))</text>
  <text x="70" y="1035" fill="#f85149" font-size="11">■ Extracción Húmeda (DN90): 95 m³/h base con Boost automático por humedad relativa en baño (&gt;70% HR activa Boost por 20 min)</text>
  <text x="70" y="1055" fill="#2ea043" font-size="11">■ Bypass Free-Cooling: Apertura 100% de compuerta si T_exterior &lt; T_interior y T_interior &gt; 23°C (refrescamiento pasivo nocturno de verano)</text>
</svg>"""

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Plano SVG generado: {svg_path}")

def generar_plano_vmc_dxf(dxf_path):
    dxf = SimpleDXF(dxf_path)
    # Perímetro 10x10m (10000x10000 mm)
    dxf.add_rect(0, 0, 10000, 10000, layer="MUROS_EXTERIORES", color=7)

    # Sala IT (4700, 4700) a (6300, 6300)
    dxf.add_rect(4700, 4700, 1600, 1600, layer="SALA_IT", color=4)
    dxf.add_text("SALA IT - RECUPERADOR VMC", 4800, 5500, height=200, layer="TEXTOS", color=4)

    # Unidad VMC en falso techo (5000, 5200, 1000x900)
    dxf.add_rect(5000, 5200, 1000, 900, layer="EQUIPO_VMC", color=4)
    dxf.add_text("UNIDAD VMC ENTALPICA 92%", 5100, 5600, height=120, layer="TEXTOS", color=7)

    # Distribución Dormitorio Principal
    dxf.add_line(5200, 5200, 3200, 2500, layer="CONDUCTOS_IMPULSION", color=5) # Azul
    dxf.add_circle(3200, 2500, 150, layer="BOCAS_IMPULSION", color=5)
    dxf.add_text("BOCA IMPULSION DORM. PPAL (45 m3/h)", 2200, 2300, height=150, layer="TEXTOS", color=5)

    # Distribución Salón
    dxf.add_line(6000, 5200, 7500, 2500, layer="CONDUCTOS_IMPULSION", color=5)
    dxf.add_circle(7500, 2500, 150, layer="BOCAS_IMPULSION", color=5)
    dxf.add_text("BOCA IMPULSION SALON (60 m3/h)", 6500, 2300, height=150, layer="TEXTOS", color=5)

    # Extracción Cocina
    dxf.add_line(5800, 5900, 7800, 7500, layer="CONDUCTOS_EXTRACCION", color=1) # Rojo
    dxf.add_circle(7800, 7500, 150, layer="BOCAS_EXTRACCION", color=1)
    dxf.add_text("BOCA EXTRACCION COCINA (60 m3/h)", 6500, 7800, height=150, layer="TEXTOS", color=1)

    # Extracción Baño
    dxf.add_line(5500, 6100, 5500, 8200, layer="CONDUCTOS_EXTRACCION", color=1)
    dxf.add_circle(5500, 8200, 150, layer="BOCAS_EXTRACCION", color=1)
    dxf.add_text("BOCA EXTRACCION BANO (35 m3/h)", 4800, 8500, height=150, layer="TEXTOS", color=1)

    # Acometidas exteriores DN160
    dxf.add_line(5000, 5300, 4400, 10000, layer="TOMA_AIRE_EXT", color=3) # Verde
    dxf.add_text("TOMA AIRE EXTERIOR DN160 FACHADA", 3000, 9800, height=150, layer="TEXTOS", color=3)

    dxf.add_line(6000, 5500, 6600, 10000, layer="EXPULSION_AIRE", color=8) # Gris
    dxf.add_text("EXPULSION AIRE VICIADO DN160", 6700, 9800, height=150, layer="TEXTOS", color=8)

    dxf.save()

if __name__ == "__main__":
    out_dir = "/home/ral/Documents/GitHub/open-source-domotics/04_telemetria_y_cargas_criticas/06_climatizacion_vmc_recuperador_calor/mecanico"
    os.makedirs(out_dir, exist_ok=True)
    dxf_file = os.path.join(out_dir, "plano_distribucion_conductos_vmc.dxf")
    svg_file = os.path.join(out_dir, "plano_distribucion_conductos_vmc.svg")

    generar_plano_vmc_dxf(dxf_file)
    generar_svg_vmc(svg_file)
