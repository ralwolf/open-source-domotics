#!/usr/bin/env python3
"""
generar_plano_cerradura_biometrica.py
Genera los planos CAD 2D (.dxf y .svg) del Panel de Control de Acceso Biométrico y Cerradura Inteligente
(Lector capacitivo Grow R503, teclado táctil retroiluminado, lector NFC Mifare Classic/DESFire y cerradura de embutir).
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
PLACA_FRONTAL
10
0.0
20
0.0
30
0.0
11
80.0
21
0.0
31
0.0
0
LINE
8
PLACA_FRONTAL
10
80.0
20
0.0
30
0.0
11
80.0
21
220.0
31
0.0
0
LINE
8
PLACA_FRONTAL
10
80.0
20
220.0
30
0.0
11
0.0
21
220.0
31
0.0
0
LINE
8
PLACA_FRONTAL
10
0.0
20
220.0
30
0.0
11
0.0
21
0.0
31
0.0
0
CIRCLE
8
SENSOR_R503
10
40.0
20
170.0
30
0.0
40
14.0
0
TEXT
8
TEXTO
10
15.0
20
165.0
30
0.0
40
4.0
1
R503 BIOMETRICO
0
TEXT
8
TEXTO
10
18.0
20
110.0
30
0.0
40
4.0
1
TECLADO TACTIL PIN
0
TEXT
8
TEXTO
10
22.0
20
40.0
30
0.0
40
4.0
1
ANTENA NFC PN532
0
ENDSEC
0
EOF
"""

SVG_CONTENT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 750" width="100%" height="100%">
  <rect width="600" height="750" fill="#0f172a"/>

  <!-- Placa frontal de aluminio cepillado / cristal templado (80 x 220 mm escalado) -->
  <rect x="180" y="80" width="240" height="580" rx="16" fill="#1e293b" stroke="#cbd5e1" stroke-width="4"/>

  <!-- Lector de huella circular Grow R503 (anillo LED RGB) -->
  <circle cx="300" cy="180" r="45" fill="#0284c7" stroke="#38bdf8" stroke-width="5"/>
  <circle cx="300" cy="180" r="35" fill="#0f172a"/>
  <text x="300" y="185" fill="#38bdf8" font-family="sans-serif" font-size="12" text-anchor="middle">R503 HUELLA</text>

  <!-- Teclado capacitivo numérico táctil (3x4 botones) -->
  <g id="teclado" transform="translate(215, 260)">
    <circle cx="25" cy="25" r="18" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="25" y="30" fill="#f8fafc" font-family="sans-serif" font-size="12" text-anchor="middle">1</text>
    <circle cx="85" cy="25" r="18" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="85" y="30" fill="#f8fafc" font-family="sans-serif" font-size="12" text-anchor="middle">2</text>
    <circle cx="145" cy="25" r="18" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="145" y="30" fill="#f8fafc" font-family="sans-serif" font-size="12" text-anchor="middle">3</text>

    <circle cx="25" cy="75" r="18" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="25" y="80" fill="#f8fafc" font-family="sans-serif" font-size="12" text-anchor="middle">4</text>
    <circle cx="85" cy="75" r="18" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="85" y="80" fill="#f8fafc" font-family="sans-serif" font-size="12" text-anchor="middle">5</text>
    <circle cx="145" cy="75" r="18" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="145" y="80" fill="#f8fafc" font-family="sans-serif" font-size="12" text-anchor="middle">6</text>

    <circle cx="25" cy="125" r="18" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="25" y="130" fill="#f8fafc" font-family="sans-serif" font-size="12" text-anchor="middle">7</text>
    <circle cx="85" cy="125" r="18" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="85" y="130" fill="#f8fafc" font-family="sans-serif" font-size="12" text-anchor="middle">8</text>
    <circle cx="145" cy="125" r="18" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="145" y="130" fill="#f8fafc" font-family="sans-serif" font-size="12" text-anchor="middle">9</text>

    <circle cx="25" cy="175" r="18" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="25" y="180" fill="#f8fafc" font-family="sans-serif" font-size="12" text-anchor="middle">*</text>
    <circle cx="85" cy="175" r="18" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="85" y="180" fill="#f8fafc" font-family="sans-serif" font-size="12" text-anchor="middle">0</text>
    <circle cx="145" cy="175" r="18" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="145" y="180" fill="#f8fafc" font-family="sans-serif" font-size="12" text-anchor="middle">#</text>
  </g>

  <!-- Zona de lectura NFC / RFID (PN532) -->
  <rect x="220" y="500" width="160" height="70" rx="8" fill="#0f172a" stroke="#10b981" stroke-dasharray="4" stroke-width="2"/>
  <text x="300" y="535" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">NFC / RFID</text>
  <text x="300" y="555" fill="#a7f3d0" font-family="sans-serif" font-size="10" text-anchor="middle">ISO 14443A (13.56 MHz)</text>

  <!-- Perno de bloqueo de seguridad / cerradura mecánica oculta inferior -->
  <circle cx="300" cy="620" r="8" fill="#475569" stroke="#94a3b8" stroke-width="2"/>

  <!-- Titulos y cotas -->
  <text x="300" y="45" fill="#f8fafc" font-family="sans-serif" font-size="18" font-weight="bold" text-anchor="middle">PANEL DE ACCESO BIOMÉTRICO IP65</text>
  <text x="300" y="705" fill="#94a3b8" font-family="sans-serif" font-size="12" text-anchor="middle">Cotas: 80 mm ancho x 220 mm alto x 22 mm profundidad | Acabado Negro Anodizado</text>
</svg>
"""

def generar_planos_cerradura():
    base_dir = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/02_cerraduras_biometricas/mecanico"
    dxf_path = os.path.join(base_dir, "plano_cerradura_biometrica.dxf")
    svg_path = os.path.join(base_dir, "plano_cerradura_biometrica.svg")

    with open(dxf_path, "w", encoding="utf-8") as f:
        f.write(DXF_CONTENT)
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(SVG_CONTENT)

    print(f"Plano DXF guardado en: {dxf_path}")
    print(f"Plano SVG guardado en: {svg_path}")

if __name__ == "__main__":
    generar_planos_cerradura()
