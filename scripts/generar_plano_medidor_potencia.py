#!/usr/bin/env python3
"""
generar_plano_medidor_potencia.py
Genera los planos CAD 2D normalizados (.dxf y .svg) del medidor modular de carril DIN 4M
con cotas milimétricas, perfil normalizado DIN 43880 y distribución de conectores.
"""

import os

DXF_CONTENT = """0
SECTION
2
HEADER
9
$ACADVER
1
AC1009
0
ENDSEC
0
SECTION
2
ENTITIES
0
LINE
8
COTAS
10
0.0
20
0.0
30
0.0
11
72.0
21
0.0
31
0.0
0
LINE
8
COTAS
10
72.0
20
0.0
30
0.0
11
72.0
21
90.0
31
0.0
0
LINE
8
COTAS
10
72.0
20
90.0
30
0.0
11
0.0
21
90.0
31
0.0
0
LINE
8
COTAS
10
0.0
20
90.0
30
0.0
11
0.0
21
0.0
31
0.0
0
LINE
8
DETALLES
10
0.0
20
22.5
30
0.0
11
72.0
21
22.5
31
0.0
0
LINE
8
DETALLES
10
0.0
20
67.5
30
0.0
11
72.0
21
67.5
31
0.0
0
LINE
8
DETALLES
10
22.0
20
47.0
30
0.0
11
50.0
21
47.0
31
0.0
0
LINE
8
DETALLES
10
50.0
20
47.0
30
0.0
11
50.0
21
63.0
31
0.0
0
LINE
8
DETALLES
10
50.0
20
63.0
30
0.0
11
22.0
21
63.0
31
0.0
0
LINE
8
DETALLES
10
22.0
20
63.0
30
0.0
11
22.0
21
47.0
31
0.0
0
TEXT
8
TEXTO
10
25.0
20
53.0
30
0.0
40
3.0
1
OLED 0.96
0
TEXT
8
TEXTO
10
10.0
20
32.0
30
0.0
40
3.0
1
RJ45 MODBUS
0
TEXT
8
TEXTO
10
5.0
20
80.0
30
0.0
40
3.5
1
ENTRADAS CT 1-6 (BORNERO SUP)
0
TEXT
8
TEXTO
10
5.0
20
10.0
30
0.0
40
3.5
1
ALIMENTACION 230V Y RELES (INF)
0
ENDSEC
0
EOF
"""

SVG_CONTENT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <rect width="800" height="600" fill="#1e1e1e"/>
  <rect x="250" y="80" width="300" height="420" rx="8" fill="#2d3748" stroke="#cbd5e0" stroke-width="3"/>
  <!-- Nariz DIN central -->
  <rect x="250" y="180" width="300" height="220" fill="#3a4759" stroke="#cbd5e0" stroke-width="2"/>
  <!-- Pantalla OLED -->
  <rect x="330" y="210" width="140" height="80" rx="4" fill="#0f172a" stroke="#00f2fe" stroke-width="2"/>
  <text x="350" y="245" fill="#00f2fe" font-family="monospace" font-size="12">V: 230.4 V</text>
  <text x="350" y="265" fill="#38ef7d" font-family="monospace" font-size="12">P: 3420 W</text>
  <!-- Puerto RJ45 -->
  <rect x="280" y="315" width="75" height="65" rx="3" fill="#1a202c" stroke="#a0aec0" stroke-width="1.5"/>
  <text x="290" y="355" fill="#a0aec0" font-family="sans-serif" font-size="10">RS-485</text>
  <!-- Botones navegacion -->
  <circle cx="410" cy="345" r="10" fill="#4a5568" stroke="#cbd5e0" stroke-width="1.5"/>
  <circle cx="450" cy="345" r="10" fill="#4a5568" stroke="#cbd5e0" stroke-width="1.5"/>
  <circle cx="490" cy="345" r="10" fill="#4a5568" stroke="#cbd5e0" stroke-width="1.5"/>
  <!-- Borneros superiores e inferiores -->
  <rect x="270" y="95" width="260" height="60" fill="#4a5568" stroke="#cbd5e0" stroke-dasharray="4"/>
  <text x="285" y="130" fill="#e2e8f0" font-family="sans-serif" font-size="12">BORNERO CT1 .. CT6 (5.08mm)</text>
  <rect x="270" y="425" width="260" height="60" fill="#4a5568" stroke="#cbd5e0" stroke-dasharray="4"/>
  <text x="280" y="460" fill="#e2e8f0" font-family="sans-serif" font-size="12">ALIMENTACION L/N + RELES (5.08mm)</text>
  <!-- Titulo y cotas -->
  <text x="400" y="45" fill="#f7fafc" font-family="sans-serif" font-size="18" font-weight="bold" text-anchor="middle">ENVOLVENTE MODULAR CARRIL DIN 4M (72 mm) - MEDIDOR TELEMETRÍA IOT</text>
  <text x="400" y="540" fill="#a0aec0" font-family="sans-serif" font-size="14" text-anchor="middle">Ancho: 72 mm (4 Módulos) | Alto: 90 mm | Profundidad: 65 mm | Norma DIN 43880</text>
</svg>
"""

def generar_planos():
    base_dir = "/home/ral/Documents/GitHub/open-source-domotics/04_telemetria_y_cargas_criticas/01_medicion_potencia_cuadro/mecanico"
    os.makedirs(base_dir, exist_ok=True)

    dxf_path = os.path.join(base_dir, "plano_medidor_potencia_cuadro.dxf")
    svg_path = os.path.join(base_dir, "plano_medidor_potencia_cuadro.svg")

    with open(dxf_path, "w", encoding="utf-8") as f:
        f.write(DXF_CONTENT)
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(SVG_CONTENT)

    print(f"Plano DXF guardado en: {dxf_path}")
    print(f"Plano SVG guardado en: {svg_path}")

if __name__ == "__main__":
    generar_planos()

