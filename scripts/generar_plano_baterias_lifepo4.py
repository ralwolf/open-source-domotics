#!/usr/bin/env python3
"""
generar_plano_baterias_lifepo4.py
Genera los planos CAD 2D (.dxf y .svg) del banco de baterías LiFePO4 16S (51.2V 280Ah 14.3 kWh)
mostrando la disposición de celdas prismáticas EVE LF280K, pletinas de interconexión de cobre,
placas de compresión con muelles Belleville, mazo de equilibrado BMS y fusible Class T de 200A.
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
GABINETE_RACK
10
0.0
20
0.0
30
0.0
11
482.0
21
0.0
31
0.0
0
LINE
8
GABINETE_RACK
10
482.0
20
0.0
30
0.0
11
482.0
21
600.0
31
0.0
0
LINE
8
GABINETE_RACK
10
482.0
20
600.0
30
0.0
11
0.0
21
600.0
31
0.0
0
LINE
8
GABINETE_RACK
10
0.0
20
600.0
30
0.0
11
0.0
21
0.0
31
0.0
0
TEXT
8
TEXTO
10
30.0
20
560.0
30
0.0
40
15.0
1
BANCO LiFePO4 16S 51.2V 280Ah (14.3 kWh)
0
TEXT
8
TEXTO
10
30.0
20
520.0
30
0.0
40
10.0
1
16 CELDAS PRISMATICAS EVE LF280K CON BARRAS DE COBRE FLEXIBLES
0
TEXT
8
TEXTO
10
30.0
20
480.0
30
0.0
40
10.0
1
BMS DALY/JBD 16S 200A SMART UART/RS485 + BALANCEO ACTIVO 2A
0
TEXT
8
TEXTO
10
30.0
20
440.0
30
0.0
40
10.0
1
FUSIBLE DE ACCION ULTRA-RAPIDA CLASS T 200A 125V DC
0
TEXT
8
TEXTO
10
30.0
20
400.0
30
0.0
40
10.0
1
SHUNT DE PRECISION 500A 50mV PARA COULOMB COUNTING
0
ENDSEC
0
EOF
"""

SVG_CONTENT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 650" width="100%" height="100%">
  <rect width="900" height="650" fill="#0f172a"/>

  <!-- Encabezado -->
  <text x="450" y="45" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">BANCO DE BATERÍAS ESS LiFePO4 16S (51.2V 280Ah / 14.3 kWh)</text>
  <text x="450" y="70" fill="#94a3b8" font-family="sans-serif" font-size="13" text-anchor="middle">Plano 2D de Montaje Mecánico, Pletinas de Cobre y Conexión BMS</text>

  <!-- Gabinete Rack 19" (482 x 600 mm) -->
  <rect x="70" y="100" width="760" height="500" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="3"/>

  <!-- 16 Celdas prismáticas EVE LF280K (2 filas de 8 celdas) -->
  <!-- Fila 1 (Celdas 1 a 8) -->
  <g id="fila1">
    <!-- Celdas -->
    <rect x="100" y="130" width="70" height="180" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <rect x="180" y="130" width="70" height="180" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <rect x="260" y="130" width="70" height="180" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <rect x="340" y="130" width="70" height="180" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <rect x="420" y="130" width="70" height="180" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <rect x="500" y="130" width="70" height="180" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <rect x="580" y="130" width="70" height="180" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <rect x="660" y="130" width="70" height="180" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  </g>

  <!-- Fila 2 (Celdas 9 a 16) -->
  <g id="fila2">
    <rect x="100" y="340" width="70" height="180" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <rect x="180" y="340" width="70" height="180" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <rect x="260" y="340" width="70" height="180" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <rect x="340" y="340" width="70" height="180" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <rect x="420" y="340" width="70" height="180" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <rect x="500" y="340" width="70" height="180" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <rect x="580" y="340" width="70" height="180" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <rect x="660" y="340" width="70" height="180" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  </g>

  <!-- Pletinas flexibles de cobre entre bornes (+ / -) -->
  <line x1="150" y1="160" x2="200" y2="160" stroke="#f59e0b" stroke-width="8"/>
  <line x1="230" y1="280" x2="280" y2="280" stroke="#f59e0b" stroke-width="8"/>
  <line x1="310" y1="160" x2="360" y2="160" stroke="#f59e0b" stroke-width="8"/>
  <line x1="390" y1="280" x2="440" y2="280" stroke="#f59e0b" stroke-width="8"/>
  <line x1="470" y1="160" x2="520" y2="160" stroke="#f59e0b" stroke-width="8"/>
  <line x1="550" y1="280" x2="600" y2="280" stroke="#f59e0b" stroke-width="8"/>
  <line x1="630" y1="160" x2="680" y2="160" stroke="#f59e0b" stroke-width="8"/>

  <!-- Placas de compresión laterales con varillas roscadas M8 y muelles Belleville (300 kgf) -->
  <rect x="85" y="125" width="10" height="400" fill="#94a3b8"/>
  <rect x="735" y="125" width="10" height="400" fill="#94a3b8"/>
  <line x1="80" y1="140" x2="750" y2="140" stroke="#cbd5e1" stroke-width="3" stroke-dasharray="4"/>
  <line x1="80" y1="510" x2="750" y2="510" stroke="#cbd5e1" stroke-width="3" stroke-dasharray="4"/>

  <!-- Módulo BMS Daly/JBD Smart en panel frontal -->
  <rect x="755" y="180" width="60" height="280" rx="4" fill="#111827" stroke="#10b981" stroke-width="2"/>
  <text x="785" y="320" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle" transform="rotate(-90 785 320)">BMS 200A SMART</text>

  <!-- Fusible Class T y Shunt -->
  <rect x="250" y="540" width="90" height="40" rx="4" fill="#b91c1c" stroke="#f87171" stroke-width="2"/>
  <text x="295" y="565" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">FUSIBLE 200A</text>

  <rect x="400" y="540" width="90" height="40" rx="4" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="445" y="565" fill="#e2e8f0" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">SHUNT 500A</text>

  <!-- Textos de detalle -->
  <text x="450" y="620" fill="#a0aec0" font-family="sans-serif" font-size="12" text-anchor="middle">Aislamiento dieléctrico epoxy entre celdas | Compresión constante 12-14 psi para máxima vida útil (&gt;6000 ciclos)</text>
</svg>
"""

def generar_planos_baterias():
    base_dir = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/04_almacenamiento_baterias_ess/mecanico"
    dxf_path = os.path.join(base_dir, "plano_banco_baterias_lifepo4.dxf")
    svg_path = os.path.join(base_dir, "plano_banco_baterias_lifepo4.svg")

    with open(dxf_path, "w", encoding="utf-8") as f:
        f.write(DXF_CONTENT)
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(SVG_CONTENT)

    print(f"Plano DXF guardado en: {dxf_path}")
    print(f"Plano SVG guardado en: {svg_path}")

if __name__ == "__main__":
    generar_planos_baterias()

