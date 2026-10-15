#!/usr/bin/env python3
"""
generar_svg_planta_arquitectonica.py
Genera la representación gráfica vectorial interactiva (.svg) de la Planta Arquitectónica Base (10x10 m)
con zonificación de estancias, cotas y orientación bioclimática.
"""

import os

SVG_CONTENT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" width="100%" height="100%">
  <rect width="1000" height="1000" fill="#0f172a"/>

  <!-- Rosa de los vientos / Norte -->
  <g transform="translate(900, 100)">
    <circle cx="0" cy="0" r="30" fill="none" stroke="#64748b" stroke-width="2"/>
    <polygon points="0,-26 8,0 0,-6 -8,0" fill="#ef4444"/>
    <polygon points="0,26 8,0 0,6 -8,0" fill="#94a3b8"/>
    <text x="-5" y="-32" fill="#ef4444" font-family="sans-serif" font-weight="bold" font-size="14">N</text>
  </g>

  <!-- Muros exteriores (10 x 10 m escalados a 700 x 700 px) -->
  <!-- Origen vivienda en (150, 150) a (850, 850) -->
  <rect x="150" y="150" width="700" height="700" fill="#1e293b" stroke="#cbd5e1" stroke-width="12"/>

  <!-- Patio interior central (3.0 x 2.0 m -> 210 x 140 px en X: 395, Y: 430) -->
  <rect x="395" y="430" width="210" height="140" fill="#064e3b" stroke="#34d399" stroke-width="6"/>
  <text x="500" y="505" fill="#a7f3d0" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">PATIO CENTRAL</text>
  <text x="500" y="525" fill="#6ee7b7" font-family="sans-serif" font-size="11" text-anchor="middle">(LUCERNARIO CENITAL 3x2m)</text>

  <!-- Dormitorio Principal (Noroeste) -->
  <rect x="156" y="156" width="233" height="274" fill="#334155" fill-opacity="0.3" stroke="#94a3b8" stroke-width="4"/>
  <text x="272" y="290" fill="#f8fafc" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">DORMITORIO</text>
  <text x="272" y="310" fill="#94a3b8" font-family="sans-serif" font-size="12" text-anchor="middle">PRINCIPAL (16 m²)</text>

  <!-- Dormitorio Infantil / Invitados (Noreste) -->
  <rect x="611" y="156" width="233" height="274" fill="#334155" fill-opacity="0.3" stroke="#94a3b8" stroke-width="4"/>
  <text x="727" y="290" fill="#f8fafc" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">DORMITORIO</text>
  <text x="727" y="310" fill="#94a3b8" font-family="sans-serif" font-size="12" text-anchor="middle">INFANTIL (16 m²)</text>

  <!-- Baño Completo Compartido (Norte Central) -->
  <rect x="395" y="156" width="210" height="200" fill="#1e3a8a" fill-opacity="0.3" stroke="#60a5fa" stroke-width="3"/>
  <text x="500" y="255" fill="#bfdbfe" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">BAÑO (8.5 m²)</text>

  <!-- Cocina Ergonómica (Suroeste) -->
  <rect x="156" y="576" width="233" height="268" fill="#78350f" fill-opacity="0.3" stroke="#f59e0b" stroke-width="4"/>
  <text x="272" y="700" fill="#fef3c7" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">COCINA ABIERTA</text>
  <text x="272" y="720" fill="#fcd34d" font-family="sans-serif" font-size="12" text-anchor="middle">Y OFFICE (17 m²)</text>

  <!-- Sala de Estar / Salón / Comedor (Sureste) -->
  <rect x="611" y="576" width="233" height="268" fill="#4c1d95" fill-opacity="0.3" stroke="#a78bfa" stroke-width="4"/>
  <text x="727" y="700" fill="#ede9fe" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">SALA DE ESTAR</text>
  <text x="727" y="720" fill="#c4b5fd" font-family="sans-serif" font-size="12" text-anchor="middle">Y COMEDOR (24 m²)</text>

  <!-- Cuarto Técnico IT y Sala de Baterías (Central Este) -->
  <rect x="611" y="430" width="140" height="140" fill="#831843" fill-opacity="0.4" stroke="#f43f5e" stroke-width="3"/>
  <text x="681" y="495" fill="#fecdd3" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">SALA IT / SAI</text>
  <text x="681" y="515" fill="#fda4af" font-family="sans-serif" font-size="10" text-anchor="middle">RACK 19" (6 m²)</text>

  <!-- Foyer / Entrada Principal (Sur Central) -->
  <rect x="420" y="740" width="160" height="104" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
  <text x="500" y="795" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">ACCESO PRINCIPAL</text>

  <!-- Huecos de puertas y ventanas destacados -->
  <rect x="450" y="840" width="100" height="16" fill="#38bdf8"/> <!-- Puerta principal -->
  <rect x="640" y="840" width="180" height="16" fill="#f59e0b"/> <!-- Ventanal salon -->
  <rect x="144" y="620" width="16" height="120" fill="#f59e0b"/> <!-- Ventana cocina -->
  <rect x="200" y="144" width="120" height="16" fill="#f59e0b"/> <!-- Ventana dorm1 -->
  <rect x="680" y="144" width="120" height="16" fill="#f59e0b"/> <!-- Ventana dorm2 -->

  <!-- Titulo y cotas -->
  <text x="500" y="70" fill="#f8fafc" font-family="sans-serif" font-size="22" font-weight="bold" text-anchor="middle">DISTRIBUCIÓN ARQUITECTÓNICA VIVIENDA BIOCLIMÁTICA 10x10 m</text>
  <text x="500" y="100" fill="#94a3b8" font-family="sans-serif" font-size="14" text-anchor="middle">Superficie Construida: 100 m² | Altura Libre: 2.80 m | Patio Central Térmico</text>
  <text x="500" y="930" fill="#64748b" font-family="sans-serif" font-size="12" text-anchor="middle">Cota Exterior: 10.000 mm x 10.000 mm | Muros de termoarcilla rectificada 30 cm con SATE</text>
</svg>
"""

def generar_svg():
    base_dir = "/home/ral/Documents/GitHub/open-source-domotics/00_diseno_arquitectonico_y_estructural/03_arquitectura_habitaciones_patios_terrazas/planos_2d_dxf"
    svg_path = os.path.join(base_dir, "planta_arquitectonica_base.svg")

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(SVG_CONTENT)

    print(f"Planta arquitectónica SVG guardada en: {svg_path}")

if __name__ == "__main__":
    generar_svg()

