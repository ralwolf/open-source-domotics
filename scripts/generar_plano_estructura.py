#!/usr/bin/env python3
"""
Generador del Plano Estructural 2D de Pilares, Vigas y Losas de Cubierta
Formatos de salida: DXF y SVG vectorial
Proyecto: open-source-domotics
"""

import os
from generar_planos_dxf import SimpleDXF

def generar_plano_estructura(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_ROTULO", color=7)
    dxf.add_layer("EJES_ESTRUCTURALES", color=1)
    dxf.add_layer("PILARES_HORMIGON", color=4)
    dxf.add_layer("VIGAS_HORMIGON", color=3)
    dxf.add_layer("LOSA_CUBIERTA", color=2)
    dxf.add_layer("COTAS_MEDIDAS", color=5)
    dxf.add_layer("TEXTO_NOTAS", color=7)

    # Marco y Cajetín A3
    dxf.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf.add_rect(230, 10, 180, 42, layer="MARCO_ROTULO")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", 235, 42, height=4.0, layer="TEXTO_NOTAS")
    dxf.add_text("PLANO ESTRUCTURAL: PILARES, VIGAS Y LOSA ALIGERADA", 235, 32, height=2.2, layer="TEXTO_NOTAS")
    dxf.add_text("Planta Forjado Cubierta E: 1/50 | f'c = 25 MPa | B500S (fy = 4200 kg/cm²)", 235, 22, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Refuerzo especial pilar C-TURB para momento eólico 3.57 kN·m", 235, 14, height=1.4, layer="TEXTO_NOTAS")

    # Origen del dibujo estructural (Escala: 1m = 18 unidades DXF)
    # Vivienda 10m x 10m -> 180 x 180 unidades DXF
    ox, oy = 25.0, 75.0
    scale = 18.0

    # Contorno perimetral de losa (10m x 10m)
    dxf.add_rect(ox, oy, 10.0 * scale, 10.0 * scale, layer="LOSA_CUBIERTA")
    dxf.add_text("LOSA DE CUBIERTA e = 20 cm (Doble Mallazo fi 10 c/15)", ox + 5, oy + 10.0 * scale - 8, height=2.0, layer="TEXTO_NOTAS")

    # Hueco Cenital Central del Lucernario Astronómico (3.0m x 2.0m en centro)
    # Centrado en X=3.5 a 6.5m, Y=4.0 a 6.0m
    hx = ox + 3.5 * scale
    hy = oy + 4.0 * scale
    hw = 3.0 * scale
    hh = 2.0 * scale
    dxf.add_rect(hx, hy, hw, hh, layer="LOSA_CUBIERTA")
    # Cruces diagonales indicando hueco estructural
    dxf.add_line(hx, hy, hx + hw, hy + hh, layer="LOSA_CUBIERTA")
    dxf.add_line(hx, hy + hh, hx + hw, hy, layer="LOSA_CUBIERTA")
    dxf.add_text("HUECO CENITAL 3.00 x 2.00 m", hx + 5, hy + hh / 2.0 + 3, height=2.0, layer="TEXTO_NOTAS")
    dxf.add_text("(Lucernario Astronómico)", hx + 5, hy + hh / 2.0 - 3, height=1.6, layer="TEXTO_NOTAS")

    # Ejes Estructurales
    # Ejes 1, 2, 3 (X = 0.5m, 5.0m, 9.5m)
    ejes_x = [0.5, 5.0, 9.5]
    nombres_x = ["1", "2", "3"]
    for ex_val, tag in zip(ejes_x, nombres_x):
        x_pos = ox + ex_val * scale
        dxf.add_line(x_pos, oy - 15, x_pos, oy + 10.0 * scale + 15, layer="EJES_ESTRUCTURALES")
        dxf.add_circle(x_pos, oy + 10.0 * scale + 20, 4.0, layer="EJES_ESTRUCTURALES")
        dxf.add_text(tag, x_pos - 1.2, oy + 10.0 * scale + 18.5, height=2.5, layer="TEXTO_NOTAS")

    # Ejes A, B, C (Y = 0.5m, 5.0m, 9.5m)
    ejes_y = [0.5, 5.0, 9.5]
    nombres_y = ["A", "B", "C"]
    for ey_val, tag in zip(ejes_y, nombres_y):
        y_pos = oy + ey_val * scale
        dxf.add_line(ox - 15, y_pos, ox + 10.0 * scale + 15, y_pos, layer="EJES_ESTRUCTURALES")
        dxf.add_circle(ox - 20, y_pos, 4.0, layer="EJES_ESTRUCTURALES")
        dxf.add_text(tag, ox - 21.5, y_pos - 1.2, height=2.5, layer="TEXTO_NOTAS")

    # Vigas Principales de Enlace V-101 (25 x 40 cm) a lo largo de los ejes
    w_viga_dxf = 0.25 * scale
    for ey_val in ejes_y:
        y_pos = oy + ey_val * scale
        dxf.add_rect(ox, y_pos - w_viga_dxf / 2.0, 10.0 * scale, w_viga_dxf, layer="VIGAS_HORMIGON")
        dxf.add_text("V-101 (25x40)", ox + 35, y_pos + w_viga_dxf / 2.0 + 1.5, height=1.3, layer="TEXTO_NOTAS")

    for ex_val in ejes_x:
        x_pos = ox + ex_val * scale
        dxf.add_rect(x_pos - w_viga_dxf / 2.0, oy, w_viga_dxf, 10.0 * scale, layer="VIGAS_HORMIGON")
        dxf.add_text("V-101 (25x40)", x_pos + w_viga_dxf / 2.0 + 1.5, oy + 35, height=1.3, layer="TEXTO_NOTAS")

    # Brocal / Vigas de Borde del Lucernario V-102 (20 x 40 cm)
    dxf.add_rect(hx - 2, hy - 2, hw + 4, hh + 4, layer="VIGAS_HORMIGON")
    dxf.add_text("V-102 (20x40) Borde Hueco", hx + 5, hy - 4, height=1.3, layer="TEXTO_NOTAS")

    # Pilares (P1 a P9)
    pilares_info = [
        ("P1", 0.5, 0.5, 0.30, 0.30, "4fi16 + 4fi12"),
        ("P2", 5.0, 0.5, 0.30, 0.30, "4fi16 + 4fi12"),
        ("P3", 9.5, 0.5, 0.30, 0.30, "4fi16 + 4fi12"),
        ("P4", 0.5, 5.0, 0.30, 0.30, "4fi16 + 4fi12"),
        ("P5", 5.0, 5.0, 0.30, 0.30, "4fi16 + 4fi12"),
        ("P6", 9.5, 5.0, 0.30, 0.30, "4fi16 + 4fi12"),
        ("P7", 0.5, 9.5, 0.30, 0.30, "4fi16 + 4fi12"),
        ("P8", 5.0, 9.5, 0.30, 0.30, "4fi16 + 4fi12"),
        ("P9 (C-TURB)", 9.5, 9.5, 0.35, 0.35, "8fi16 (Eólico)"),
    ]

    for tag, px, py, pw, ph, rebar in pilares_info:
        cx = ox + px * scale
        cy = oy + py * scale
        pw_d = pw * scale
        ph_d = ph * scale
        dxf.add_rect(cx - pw_d / 2.0, cy - ph_d / 2.0, pw_d, ph_d, layer="PILARES_HORMIGON")
        dxf.add_line(cx - pw_d / 2.0, cy - ph_d / 2.0, cx + pw_d / 2.0, cy + ph_d / 2.0, layer="PILARES_HORMIGON")
        dxf.add_line(cx - pw_d / 2.0, cy + ph_d / 2.0, cx + pw_d / 2.0, cy - ph_d / 2.0, layer="PILARES_HORMIGON")
        dxf.add_text(tag, cx + pw_d / 2.0 + 2.0, cy + 1.0, height=1.6, layer="TEXTO_NOTAS")

    # Zona Reforzada Cuarto Técnico IT y Baterías LiFePO4
    dxf.add_rect(ox + 4.8 * scale, oy + 4.8 * scale, 4.8 * scale, 4.8 * scale, layer="COTAS_MEDIDAS")
    dxf.add_text("ZONA TÉCNICA IT + BATERÍAS (Planta Baja)", ox + 5.0 * scale + 5, oy + 7.5 * scale, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("Sobrecarga admisible: 4.0 kN/m²", ox + 5.0 * scale + 5, oy + 7.0 * scale, height=1.3, layer="TEXTO_NOTAS")

    # Cuadro de Columnas y Armaduras (Tabla a la derecha)
    tx, ty = 230.0, 80.0
    dxf.add_rect(tx, ty, 180, 160, layer="MARCO_ROTULO")
    dxf.add_text("CUADRO DE PILARES Y ESPECIFICACIONES ESTRUCTURALES", tx + 5, ty + 152, height=2.2, layer="TEXTO_NOTAS")
    
    # Encabezados de tabla
    dxf.add_line(tx, ty + 145, tx + 180, ty + 145, layer="MARCO_ROTULO")
    dxf.add_text("Pilar", tx + 5, ty + 140, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Sección", tx + 35, ty + 140, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Armadura Long.", tx + 75, ty + 140, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Estribos", tx + 130, ty + 140, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_line(tx, ty + 135, tx + 180, ty + 135, layer="MARCO_ROTULO")

    filas = [
        ("P1 a P8", "30 x 30 cm", "4fi16 + 4fi12", "fi8 c/15 cm"),
        ("P9 (C-TURB)", "35 x 35 cm", "8fi16 (B500S)", "fi8 c/10 cm conf."),
        ("V-101 (Princ.)", "25 x 40 cm", "3fi16 sup + 3fi16 inf", "fi8 c/12 cm"),
        ("V-102 (Borde)", "20 x 40 cm", "2fi16 sup + 2fi16 inf", "fi8 c/15 cm"),
        ("Losa Cubierta", "e = 20 cm", "Doble malla fi10 c/15", "Separadores 30mm"),
    ]
    curr_y = ty + 125
    for p_col, s_col, a_col, e_col in filas:
        dxf.add_text(p_col, tx + 5, curr_y, height=1.5, layer="TEXTO_NOTAS")
        dxf.add_text(s_col, tx + 35, curr_y, height=1.5, layer="TEXTO_NOTAS")
        dxf.add_text(a_col, tx + 75, curr_y, height=1.5, layer="TEXTO_NOTAS")
        dxf.add_text(e_col, tx + 130, curr_y, height=1.5, layer="TEXTO_NOTAS")
        curr_y -= 12

    # Notas Técnicas
    dxf.add_line(tx, ty + 65, tx + 180, ty + 65, layer="MARCO_ROTULO")
    dxf.add_text("NOTAS GENERALES DE HORMIGÓN ARMADO:", tx + 5, ty + 58, height=1.7, layer="TEXTO_NOTAS")
    dxf.add_text("1. Resistencia característica hormigón: f'c = 250 kg/cm² (25 MPa).", tx + 5, ty + 50, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("2. Límite elástico acero corrugado: fy = 4200 kg/cm² (B500S).", tx + 5, ty + 44, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("3. Recubrimiento libre nominal: 30 mm en losas y vigas, 40 mm en pilares.", tx + 5, ty + 38, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("4. Anclaje pilar C-TURB: Mástil eólico fijado con 8 pernos M20 Grado 8.8.", tx + 5, ty + 32, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("5. Pendiente de escorrentía en cubierta: 2% hacia canalones pluviales.", tx + 5, ty + 26, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("6. Empalmes por solape: mínimo 55 diámetros (L_solape = 88 cm para fi 16).", tx + 5, ty + 20, height=1.3, layer="TEXTO_NOTAS")

    dxf.save()
    print(f"DXF estructural guardado en: {dxf_path}")

    # 2. GENERACIÓN SVG
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 850" width="100%" height="100%" style="background-color: #0f172a; font-family: monospace, sans-serif;">
  <defs>
    <pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse">
      <path d="M 30 0 L 0 0 0 30" fill="none" stroke="#1e293b" stroke-width="0.5"/>
    </pattern>
  </defs>

  <rect width="100%" height="100%" fill="url(#grid)" />
  <rect x="20" y="20" width="1160" height="810" fill="none" stroke="#334155" stroke-width="2" rx="8" />

  <!-- Cajetin -->
  <rect x="680" y="720" width="480" height="90" fill="#1e293b" stroke="#3b82f6" stroke-width="2" rx="4" />
  <text x="700" y="745" fill="#60a5fa" font-size="16" font-weight="bold">OPEN-SOURCE-DOMOTICS</text>
  <text x="700" y="768" fill="#f8fafc" font-size="13" font-weight="bold">PLANO ESTRUCTURAL: PILARES, VIGAS Y LOSA ALIGERADA</text>
  <text x="700" y="790" fill="#94a3b8" font-size="11">Planta Forjado Cubierta E: 1/50 | f'c = 25 MPa | B500S (fy = 4200 kg/cm²)</text>
  <text x="700" y="805" fill="#38bdf8" font-size="10">Refuerzo especial pilar C-TURB para momento eólico 3.57 kN·m</text>

  <!-- Losa Perimetral (10m x 10m) -->
  <g transform="translate(60, 60)">
    <!-- Losa Fondo -->
    <rect x="40" y="40" width="540" height="540" fill="#1e293b" stroke="#64748b" stroke-width="3" />
    <text x="50" y="65" fill="#94a3b8" font-size="12" font-weight="bold">LOSA DE CUBIERTA e = 20 cm (Doble Mallazo fi 10 c/15)</text>

    <!-- Hueco Cenital Central (3m x 2m) -->
    <!-- X: 3.5m a 6.5m (229 a 391), Y: 4m a 6m (256 a 364) -->
    <rect x="229" y="256" width="162" height="108" fill="#0f172a" stroke="#f59e0b" stroke-width="2.5" />
    <line x1="229" y1="256" x2="391" y2="364" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,4" />
    <line x1="229" y1="364" x2="391" y2="256" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,4" />
    <text x="235" y="305" fill="#fbbf24" font-size="11" font-weight="bold">HUECO CENITAL 3.0 x 2.0 m</text>
    <text x="240" y="325" fill="#fde68a" font-size="10">(Lucernario Astronómico)</text>

    <!-- Vigas Principales V-101 (25x40 cm) -->
    <!-- Eje 1 (X=67), Eje 2 (X=310), Eje 3 (X=553) -->
    <!-- Eje A (Y=67), Eje B (Y=310), Eje C (Y=553) -->
    <!-- Vigas Horizontales -->
    <rect x="40" y="60" width="540" height="14" fill="#334155" stroke="#38bdf8" stroke-width="1.5" />
    <rect x="40" y="303" width="540" height="14" fill="#334155" stroke="#38bdf8" stroke-width="1.5" />
    <rect x="40" y="546" width="540" height="14" fill="#334155" stroke="#38bdf8" stroke-width="1.5" />

    <!-- Vigas Verticales -->
    <rect x="60" y="40" width="14" height="540" fill="#334155" stroke="#38bdf8" stroke-width="1.5" />
    <rect x="303" y="40" width="14" height="540" fill="#334155" stroke="#38bdf8" stroke-width="1.5" />
    <rect x="546" y="40" width="14" height="540" fill="#334155" stroke="#38bdf8" stroke-width="1.5" />

    <!-- Ejes Estructurales -->
    <!-- Verticales 1, 2, 3 -->
    <line x1="67" y1="15" x2="67" y2="605" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="6,4" />
    <circle cx="67" cy="615" r="12" fill="#1e293b" stroke="#ef4444" stroke-width="1.5" />
    <text x="63" y="620" fill="#f87171" font-size="12" font-weight="bold">1</text>

    <line x1="310" y1="15" x2="310" y2="605" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="6,4" />
    <circle cx="310" cy="615" r="12" fill="#1e293b" stroke="#ef4444" stroke-width="1.5" />
    <text x="306" y="620" fill="#f87171" font-size="12" font-weight="bold">2</text>

    <line x1="553" y1="15" x2="553" y2="605" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="6,4" />
    <circle cx="553" cy="615" r="12" fill="#1e293b" stroke="#ef4444" stroke-width="1.5" />
    <text x="549" y="620" fill="#f87171" font-size="12" font-weight="bold">3</text>

    <!-- Horizontales A, B, C -->
    <line x1="15" y1="67" x2="605" y2="67" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="6,4" />
    <circle cx="5" cy="67" r="12" fill="#1e293b" stroke="#ef4444" stroke-width="1.5" />
    <text x="1" y="72" fill="#f87171" font-size="12" font-weight="bold">A</text>

    <line x1="15" y1="310" x2="605" y2="310" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="6,4" />
    <circle cx="5" cy="310" r="12" fill="#1e293b" stroke="#ef4444" stroke-width="1.5" />
    <text x="1" y="315" fill="#f87171" font-size="12" font-weight="bold">B</text>

    <line x1="15" y1="553" x2="605" y2="553" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="6,4" />
    <circle cx="5" cy="553" r="12" fill="#1e293b" stroke="#ef4444" stroke-width="1.5" />
    <text x="1" y="558" fill="#f87171" font-size="12" font-weight="bold">C</text>

    <!-- Pilares P1 a P9 -->
    <!-- P1 -->
    <rect x="58" y="58" width="18" height="18" fill="#3b82f6" stroke="#93c5fd" stroke-width="1" />
    <text x="80" y="72" fill="#f8fafc" font-size="10" font-weight="bold">P1 (30x30)</text>
    <!-- P2 -->
    <rect x="301" y="58" width="18" height="18" fill="#3b82f6" stroke="#93c5fd" stroke-width="1" />
    <text x="323" y="72" fill="#f8fafc" font-size="10" font-weight="bold">P2 (30x30)</text>
    <!-- P3 -->
    <rect x="544" y="58" width="18" height="18" fill="#3b82f6" stroke="#93c5fd" stroke-width="1" />
    <text x="500" y="72" fill="#f8fafc" font-size="10" font-weight="bold">P3 (30x30)</text>

    <!-- P4 -->
    <rect x="58" y="301" width="18" height="18" fill="#3b82f6" stroke="#93c5fd" stroke-width="1" />
    <text x="80" y="315" fill="#f8fafc" font-size="10" font-weight="bold">P4 (30x30)</text>
    <!-- P5 -->
    <rect x="301" y="301" width="18" height="18" fill="#3b82f6" stroke="#93c5fd" stroke-width="1" />
    <text x="323" y="315" fill="#f8fafc" font-size="10" font-weight="bold">P5 (30x30)</text>
    <!-- P6 -->
    <rect x="544" y="301" width="18" height="18" fill="#3b82f6" stroke="#93c5fd" stroke-width="1" />
    <text x="500" y="315" fill="#f8fafc" font-size="10" font-weight="bold">P6 (30x30)</text>

    <!-- P7 -->
    <rect x="58" y="544" width="18" height="18" fill="#3b82f6" stroke="#93c5fd" stroke-width="1" />
    <text x="80" y="558" fill="#f8fafc" font-size="10" font-weight="bold">P7 (30x30)</text>
    <!-- P8 -->
    <rect x="301" y="544" width="18" height="18" fill="#3b82f6" stroke="#93c5fd" stroke-width="1" />
    <text x="323" y="558" fill="#f8fafc" font-size="10" font-weight="bold">P8 (30x30)</text>

    <!-- P9 (C-TURB Maestro Eólico 35x35 cm) -->
    <rect x="542" y="542" width="22" height="22" fill="#10b981" stroke="#6ee7b7" stroke-width="2" />
    <text x="430" y="558" fill="#34d399" font-size="11" font-weight="bold">P9 C-TURB (35x35)</text>

    <!-- Zona Tecnica Sobrecarga -->
    <rect x="303" y="303" width="243" height="243" fill="#3b82f6" fill-opacity="0.08" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="5,3" />
    <text x="320" y="440" fill="#60a5fa" font-size="11" font-weight="bold">SALA TÉCNICA IT + BATERÍAS</text>
    <text x="320" y="460" fill="#94a3b8" font-size="10">Sobrecarga: 4.0 kN/m² (LiFePO4)</text>
  </g>

  <!-- Tabla de Cuadro de Pilares a la Derecha -->
  <g transform="translate(680, 60)">
    <rect x="0" y="0" width="480" height="640" fill="#1e293b" stroke="#475569" stroke-width="2" rx="6" />
    <text x="20" y="35" fill="#f8fafc" font-size="14" font-weight="bold">CUADRO DE PILARES Y ESPECIFICACIONES</text>
    <line x1="15" y1="50" x2="465" y2="50" stroke="#64748b" stroke-width="1.5" />
    
    <!-- Encabezados -->
    <text x="20" y="75" fill="#94a3b8" font-size="11" font-weight="bold">PILAR</text>
    <text x="100" y="75" fill="#94a3b8" font-size="11" font-weight="bold">SECCIÓN</text>
    <text x="200" y="75" fill="#94a3b8" font-size="11" font-weight="bold">ARMADURA LONG.</text>
    <text x="350" y="75" fill="#94a3b8" font-size="11" font-weight="bold">ESTRIBOS</text>
    <line x1="15" y1="85" x2="465" y2="85" stroke="#334155" stroke-width="1" />

    <!-- Filas -->
    <text x="20" y="115" fill="#f8fafc" font-size="11">P1 a P8</text>
    <text x="100" y="115" fill="#cbd5e1" font-size="11">30 x 30 cm</text>
    <text x="200" y="115" fill="#38bdf8" font-size="11">4fi16 + 4fi12 (B500S)</text>
    <text x="350" y="115" fill="#e2e8f0" font-size="11">fi8 c/15 cm</text>

    <text x="20" y="155" fill="#34d399" font-size="11" font-weight="bold">P9 (C-TURB)</text>
    <text x="100" y="155" fill="#34d399" font-size="11" font-weight="bold">35 x 35 cm</text>
    <text x="200" y="155" fill="#34d399" font-size="11" font-weight="bold">8fi16 (Eólico MK9)</text>
    <text x="350" y="155" fill="#34d399" font-size="11" font-weight="bold">fi8 c/10 cm conf.</text>

    <text x="20" y="195" fill="#f8fafc" font-size="11">V-101 (Princ.)</text>
    <text x="100" y="195" fill="#cbd5e1" font-size="11">25 x 40 cm</text>
    <text x="200" y="195" fill="#38bdf8" font-size="11">3fi16 sup + 3fi16 inf</text>
    <text x="350" y="195" fill="#e2e8f0" font-size="11">fi8 c/12 cm</text>

    <text x="20" y="235" fill="#f8fafc" font-size="11">V-102 (Borde)</text>
    <text x="100" y="235" fill="#cbd5e1" font-size="11">20 x 40 cm</text>
    <text x="200" y="235" fill="#38bdf8" font-size="11">2fi16 sup + 2fi16 inf</text>
    <text x="350" y="235" fill="#e2e8f0" font-size="11">fi8 c/15 cm</text>

    <text x="20" y="275" fill="#f8fafc" font-size="11">Losa Cubierta</text>
    <text x="100" y="275" fill="#cbd5e1" font-size="11">e = 20 cm</text>
    <text x="200" y="275" fill="#38bdf8" font-size="11">Doble malla fi10 c/15</text>
    <text x="350" y="275" fill="#e2e8f0" font-size="11">Sep. 30 mm</text>

    <line x1="15" y1="305" x2="465" y2="305" stroke="#64748b" stroke-width="1.5" />
    
    <!-- Notas de Ingenieria -->
    <text x="20" y="335" fill="#facc15" font-size="12" font-weight="bold">CRITERIOS Y NOTAS DE INGENIERÍA:</text>
    <text x="20" y="365" fill="#cbd5e1" font-size="10">• Resistencia Hormigón: f'c = 250 kg/cm² (25 MPa), control intenso.</text>
    <text x="20" y="390" fill="#cbd5e1" font-size="10">• Acero Corrugado: B500S con límite elástico fy = 4200 kg/cm².</text>
    <text x="20" y="415" fill="#cbd5e1" font-size="10">• Recubrimientos libres: 30 mm losas/vigas, 40 mm pilares perimetrales.</text>
    <text x="20" y="440" fill="#cbd5e1" font-size="10">• Momento de vuelco eólico en P9: M_vuelco = 3.57 kN·m a 45 m/s.</text>
    <text x="20" y="465" fill="#cbd5e1" font-size="10">• Placa base mástil: 400x400x20 mm con 8 pernos M20 Grado 8.8.</text>
    <text x="20" y="490" fill="#cbd5e1" font-size="10">• Desacoplo de vibraciones: Almohadilla elastomérica de Neopreno 15mm.</text>
    <text x="20" y="515" fill="#cbd5e1" font-size="10">• Pendiente azotea: 2% hacia canalones pluviales perimetrales.</text>
    <text x="20" y="540" fill="#cbd5e1" font-size="10">• Longitud mínima solape armaduras: 55 fi (88 cm para fi 16).</text>
    <text x="20" y="565" fill="#cbd5e1" font-size="10">• Vibrado mecánico continuo y curado húmedo mínimo de 7 días.</text>
    <text x="20" y="595" fill="#22c55e" font-size="10" font-weight="bold">Cumplimiento: Código Estructural / Eurocódigo 2 / ACI 318</text>
  </g>
</svg>"""

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"SVG estructural guardado en: {svg_path}")

if __name__ == "__main__":
    dxf_out = "/home/ral/Documents/GitHub/open-source-domotics/00_diseno_arquitectonico_y_estructural/02_estructura_pilares_y_losas/planos_y_calculos/plano_estructura_pilares_losas.dxf"
    svg_out = "/home/ral/Documents/GitHub/open-source-domotics/00_diseno_arquitectonico_y_estructural/02_estructura_pilares_y_losas/planos_y_calculos/plano_estructura_pilares_losas.svg"
    generar_plano_estructura(dxf_out, svg_out)

