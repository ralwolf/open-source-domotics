#!/usr/bin/env python3
"""
Generador del Plano de Canalizaciones Segregadas de Fuerza y Datos según Normativa
Formatos de salida: DXF y SVG vectorial
Proyecto: open-source-domotics
"""

import os
from generar_planos_dxf import SimpleDXF

def generar_plano_canalizaciones(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_ROTULO", color=7)
    dxf.add_layer("DISTRIBUCION_MUROS", color=8)
    dxf.add_layer("CANALIZACION_FUERZA_AC", color=1) # Rojo
    dxf.add_layer("CANALIZACION_DATOS_POE", color=5) # Azul
    dxf.add_layer("CANALIZACION_BUS_SENSORES", color=3) # Verde
    dxf.add_layer("CAJAS_REGISTRO", color=4) # Cyan
    dxf.add_layer("TEXTO_NOTAS", color=7)

    # Marco y Cajetín A3
    dxf.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf.add_rect(230, 10, 180, 42, layer="MARCO_ROTULO")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", 235, 42, height=4.0, layer="TEXTO_NOTAS")
    dxf.add_text("PLANO DE CANALIZACIONES SEGREGADAS Y DUCTOS NORMATIVOS", 235, 32, height=2.0, layer="TEXTO_NOTAS")
    dxf.add_text("Segregación Fuerza vs Datos >= 30 cm | Cruces a 90° | Ocupación <= 40%", 235, 22, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Normas ANSI/TIA-569-E, ISO/IEC 11801, NEC Art. 300 / REBT ITC-BT-21", 235, 14, height=1.4, layer="TEXTO_NOTAS")

    # Origen del plano (Vivienda 10m x 10m escalada a 18 unidades/m)
    ox, oy = 30.0, 75.0
    s = 18.0

    # Perímetro y Muros de la Vivienda
    dxf.add_rect(ox, oy, 10.0 * s, 10.0 * s, layer="DISTRIBUCION_MUROS")
    
    # Cuarto Técnico IT Central (X=4.5 a 6.5m, Y=4.5 a 6.5m)
    cx, cy = ox + 4.5 * s, oy + 4.5 * s
    cw, ch = 2.0 * s, 2.0 * s
    dxf.add_rect(cx, cy, cw, ch, layer="DISTRIBUCION_MUROS")
    dxf.add_text("CUARTO TÉCNICO IT", cx + 3, cy + ch - 8, height=1.8, layer="TEXTO_NOTAS")
    dxf.add_text("(Rack 19\" + TGBT)", cx + 3, cy + ch - 15, height=1.4, layer="TEXTO_NOTAS")

    # Cocina (Esquina Noroeste: X=0.5 a 4.0m, Y=5.5 a 9.5m)
    dxf.add_rect(ox + 0.5 * s, oy + 5.5 * s, 3.5 * s, 4.0 * s, layer="DISTRIBUCION_MUROS")
    dxf.add_text("COCINA / LAVANDERÍA", ox + 0.8 * s, oy + 9.0 * s, height=1.6, layer="TEXTO_NOTAS")

    # Sala / Comedor (Suroeste: X=0.5 a 4.5m, Y=0.5 a 5.0m)
    dxf.add_rect(ox + 0.5 * s, oy + 0.5 * s, 4.0 * s, 4.5 * s, layer="DISTRIBUCION_MUROS")
    dxf.add_text("SALA / COMEDOR", ox + 0.8 * s, oy + 4.2 * s, height=1.6, layer="TEXTO_NOTAS")

    # Recámara Principal (Sureste: X=5.5 a 9.5m, Y=0.5 a 4.5m)
    dxf.add_rect(ox + 5.5 * s, oy + 0.5 * s, 4.0 * s, 4.0 * s, layer="DISTRIBUCION_MUROS")
    dxf.add_text("RECÁMARA PRINCIPAL", ox + 5.8 * s, oy + 4.0 * s, height=1.6, layer="TEXTO_NOTAS")

    # Recámara Infantil / Estudio (Noreste: X=6.8 a 9.5m, Y=5.5 a 9.5m)
    dxf.add_rect(ox + 6.8 * s, oy + 5.5 * s, 2.7 * s, 4.0 * s, layer="DISTRIBUCION_MUROS")
    dxf.add_text("ESTUDIO / DORMITORIO", ox + 7.0 * s, oy + 9.0 * s, height=1.6, layer="TEXTO_NOTAS")

    # 1. RUTA FUERZA AC 230V (PVC Cédula 40 1" / EMT rígido) - Rojo
    # Salida desde TGBT Cuarto Técnico hacia Cocina
    dxf.add_line(cx + 5, cy + ch / 2.0 + 8, ox + 3.5 * s, oy + 7.5 * s, layer="CANALIZACION_FUERZA_AC")
    dxf.add_line(ox + 3.5 * s, oy + 7.5 * s, ox + 1.0 * s, oy + 7.5 * s, layer="CANALIZACION_FUERZA_AC")
    dxf.add_text("Fuerza Cocina (Horno/Inducción/Refri)", ox + 1.2 * s, oy + 7.8 * s, height=1.3, layer="TEXTO_NOTAS")

    # Salida hacia Sala / Multimedia
    dxf.add_line(cx + 5, cy + 5, ox + 2.5 * s, oy + 2.5 * s, layer="CANALIZACION_FUERZA_AC")
    dxf.add_text("Fuerza Sala / Audio", ox + 1.5 * s, oy + 2.8 * s, height=1.3, layer="TEXTO_NOTAS")

    # Salida hacia Recámaras y Clima
    dxf.add_line(cx + cw - 5, cy + 5, ox + 7.5 * s, oy + 2.5 * s, layer="CANALIZACION_FUERZA_AC")
    dxf.add_text("Fuerza Recámaras + AC Multi-Split", ox + 5.8 * s, oy + 2.2 * s, height=1.3, layer="TEXTO_NOTAS")

    # 2. RUTA DATOS UTP Cat6A / PoE (Corrugado libre de halógenos 25 mm) - Azul (Separado >= 30cm)
    # Hacia Punto de Acceso WiFi / Videoportero Entrada
    dxf.add_line(cx + 15, cy - 10, ox + 4.5 * s, oy + 0.5 * s, layer="CANALIZACION_DATOS_POE")
    dxf.add_text("Cat6A PoE Videoportero / AP", ox + 4.7 * s, oy + 1.2 * s, height=1.3, layer="TEXTO_NOTAS")

    # Hacia Cámaras CCTV Fachada
    dxf.add_line(cx + cw / 2.0, cy + ch + 5, ox + 5.5 * s, oy + 9.5 * s, layer="CANALIZACION_DATOS_POE")
    dxf.add_text("Cat6A PoE Cámaras Frigate", ox + 5.7 * s, oy + 8.8 * s, height=1.3, layer="TEXTO_NOTAS")

    # Hacia Escritorio Oficina / Estudio
    dxf.add_line(cx + cw, cy + ch / 2.0 - 5, ox + 8.5 * s, oy + 7.0 * s, layer="CANALIZACION_DATOS_POE")
    dxf.add_text("Cat6A Red LAN Estudio (10 Gbps)", ox + 6.8 * s, oy + 6.6 * s, height=1.3, layer="TEXTO_NOTAS")

    # 3. RUTA BUS DE SENSORES / MODBUS RS-485 - Verde
    # Hacia Azotea (Lucernario, Aerogenerador, Solar)
    dxf.add_line(cx + 8, cy + ch - 5, cx + 8, cy + ch + 15, layer="CANALIZACION_BUS_SENSORES")
    dxf.add_text("Columna Montante Azotea (Sensores Eólicos + PT1000 + BMS)", cx - 25, cy + ch + 20, height=1.3, layer="TEXTO_NOTAS")

    # 4. Cajas de Registro y Derivación (4x4" e intermedias)
    cajas = [
        (ox + 3.5 * s, oy + 7.5 * s, "CR-01"),
        (ox + 2.5 * s, oy + 2.5 * s, "CR-02"),
        (ox + 7.5 * s, oy + 2.5 * s, "CR-03"),
        (ox + 8.5 * s, oy + 7.0 * s, "CR-04"),
        (ox + 5.5 * s, oy + 9.5 * s, "CR-05"),
        (ox + 4.5 * s, oy + 0.5 * s, "CR-06"),
    ]
    for px, py, tag in cajas:
        dxf.add_rect(px - 3, py - 3, 6, 6, layer="CAJAS_REGISTRO")
        dxf.add_text(tag, px - 3, py + 4, height=1.2, layer="TEXTO_NOTAS")

    # Tabla Normativa de Segregación y Ocupación
    tx, ty = 230.0, 75.0
    dxf.add_rect(tx, ty, 180, 165, layer="MARCO_ROTULO")
    dxf.add_text("TABLA DE SEGREGACIÓN FÍSICA Y OCUPACIÓN NORMATIVA", tx + 5, ty + 155, height=2.0, layer="TEXTO_NOTAS")
    dxf.add_line(tx, ty + 148, tx + 180, ty + 148, layer="MARCO_ROTULO")

    dxf.add_text("Servicio", tx + 5, ty + 140, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("Tipo Ducto", tx + 45, ty + 140, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("Separación", tx + 105, ty + 140, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("Ocup. Máx", tx + 145, ty + 140, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_line(tx, ty + 135, tx + 180, ty + 135, layer="MARCO_ROTULO")

    filas = [
        ("Fuerza AC 230V", "PVC Cédula 40 1\"", "0 cm (Base)", "40% (3 cond.)"),
        ("Datos Cat6A PoE", "Corrugado LSZH 25mm", "≥ 30 cm", "38% (4 cables)"),
        ("Bus RS-485 / KNX", "Corrugado LSZH 20mm", "≥ 30 cm", "30% (2 pares)"),
        ("Fibra Óptica OS2", "Tubo rígido 20mm", "≥ 10 cm", "20% (1 microt.)"),
        ("Cruces Fuerza/Datos", "Perpendicular 90°", "Contacto 0 cm", "Blindado Fe"),
    ]
    cy_f = ty + 125
    for s_name, d_type, sep, ocu in filas:
        dxf.add_text(s_name, tx + 5, cy_f, height=1.4, layer="TEXTO_NOTAS")
        dxf.add_text(d_type, tx + 45, cy_f, height=1.3, layer="TEXTO_NOTAS")
        dxf.add_text(sep, tx + 105, cy_f, height=1.3, layer="TEXTO_NOTAS")
        dxf.add_text(ocu, tx + 145, cy_f, height=1.3, layer="TEXTO_NOTAS")
        cy_f -= 12

    # Notas Técnicas
    dxf.add_line(tx, ty + 68, tx + 180, ty + 68, layer="MARCO_ROTULO")
    dxf.add_text("REGLAS DE INSTALACIÓN ELECTROMECÁNICA:", tx + 5, ty + 60, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("1. Prohibido compartir ducto o caja entre fuerza (>50V) y MBTS/Datos.", tx + 5, ty + 50, height=1.2, layer="TEXTO_NOTAS")
    dxf.add_text("2. Radio mínimo de curvatura: R ≥ 6 x D exterior (mínimo 150 mm en Cat6A).", tx + 5, ty + 42, height=1.2, layer="TEXTO_NOTAS")
    dxf.add_text("3. Cajas de registro intermedias cada 15 metros o tras 2 codos de 90°.", tx + 5, ty + 34, height=1.2, layer="TEXTO_NOTAS")
    dxf.add_text("4. Hilo guía de nylon de tracción 50 kg permanente en todos los ductos.", tx + 5, ty + 26, height=1.2, layer="TEXTO_NOTAS")
    dxf.add_text("5. Materiales libres de halógenos y baja emisión de humos (LSZH / CPR Cca).", tx + 5, ty + 18, height=1.2, layer="TEXTO_NOTAS")

    dxf.save()
    print(f"DXF canalizaciones guardado en: {dxf_path}")

    # 2. GENERACIÓN SVG
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 850" width="100%" height="100%" style="background-color: #0b111a; font-family: monospace, sans-serif;">
  <rect x="20" y="20" width="1160" height="810" fill="none" stroke="#1e293b" stroke-width="2" rx="8" />

  <!-- Cajetin -->
  <rect x="680" y="730" width="480" height="80" fill="#152132" stroke="#3b82f6" stroke-width="2" rx="4" />
  <text x="700" y="755" fill="#60a5fa" font-size="16" font-weight="bold">OPEN-SOURCE-DOMOTICS</text>
  <text x="700" y="775" fill="#f8fafc" font-size="13" font-weight="bold">PLANO DE CANALIZACIONES SEGREGADAS Y DUCTOS NORMATIVOS</text>
  <text x="700" y="795" fill="#94a3b8" font-size="11">Segregación ≥ 30 cm | Cruces a 90° | Ocupación ≤ 40% | ANSI/TIA-569 / REBT</text>

  <!-- Vivienda 10m x 10m y Distribución -->
  <g transform="translate(60, 60)">
    <!-- Perímetro Exterior -->
    <rect x="0" y="0" width="550" height="550" fill="#111827" stroke="#475569" stroke-width="3" />

    <!-- Cuarto Técnico IT Central -->
    <rect x="220" y="220" width="110" height="110" fill="#1e293b" stroke="#3b82f6" stroke-width="2.5" />
    <text x="230" y="260" fill="#60a5fa" font-size="11" font-weight="bold">SALA IT</text>
    <text x="230" y="280" fill="#cbd5e1" font-size="9">Rack 19"</text>
    <text x="230" y="295" fill="#cbd5e1" font-size="9">+ TGBT</text>

    <!-- Habitaciones -->
    <!-- Cocina Noroeste -->
    <rect x="20" y="20" width="180" height="200" fill="#0f172a" stroke="#334155" stroke-width="1.5" />
    <text x="35" y="45" fill="#94a3b8" font-size="12" font-weight="bold">COCINA / LAVANDERÍA</text>

    <!-- Sala Suroeste -->
    <rect x="20" y="280" width="180" height="250" fill="#0f172a" stroke="#334155" stroke-width="1.5" />
    <text x="35" y="310" fill="#94a3b8" font-size="12" font-weight="bold">SALA / ESTAR</text>

    <!-- Recámara Sureste -->
    <rect x="350" y="280" width="180" height="250" fill="#0f172a" stroke="#334155" stroke-width="1.5" />
    <text x="365" y="310" fill="#94a3b8" font-size="12" font-weight="bold">RECÁMARA PRINCIPAL</text>

    <!-- Estudio Noreste -->
    <rect x="350" y="20" width="180" height="200" fill="#0f172a" stroke="#334155" stroke-width="1.5" />
    <text x="365" y="45" fill="#94a3b8" font-size="12" font-weight="bold">ESTUDIO / DORMITORIO</text>

    <!-- 1. Trazados de Fuerza AC 230V (Rojo) -->
    <!-- TGBT a Cocina -->
    <path d="M 240 220 L 240 120 L 110 120" stroke="#ef4444" stroke-width="4" fill="none" />
    <text x="120" y="110" fill="#f87171" font-size="10" font-weight="bold">Fuerza Cocina (1" PVC C40)</text>

    <!-- TGBT a Sala -->
    <path d="M 230 330 L 230 420 L 110 420" stroke="#ef4444" stroke-width="4" fill="none" />
    <text x="120" y="440" fill="#f87171" font-size="10" font-weight="bold">Fuerza Sala / Audio</text>

    <!-- TGBT a Recámara -->
    <path d="M 320 330 L 320 420 L 440 420" stroke="#ef4444" stroke-width="4" fill="none" />
    <text x="330" y="440" fill="#f87171" font-size="10" font-weight="bold">Fuerza Recámaras + AC</text>

    <!-- 2. Trazados de Red de Datos Cat6A PoE (Azul, Segregado >= 30cm) -->
    <!-- Rack a AP / Videoportero Entrada Sur -->
    <path d="M 275 330 L 275 530" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,3" fill="none" />
    <text x="285" y="510" fill="#38bdf8" font-size="10" font-weight="bold">Cat6A PoE Videoportero / AP</text>

    <!-- Rack a Cámaras CCTV Norte -->
    <path d="M 275 220 L 275 20" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,3" fill="none" />
    <text x="285" y="35" fill="#38bdf8" font-size="10" font-weight="bold">Cat6A PoE Frigate NVR</text>

    <!-- Rack a Estudio LAN -->
    <path d="M 330 250 L 440 250 L 440 120" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,3" fill="none" />
    <text x="350" y="240" fill="#38bdf8" font-size="10" font-weight="bold">Cat6A LAN Estudio 10G</text>

    <!-- 3. Bus de Sensores / Modbus (Verde) -->
    <path d="M 290 220 L 290 170 L 480 170" stroke="#10b981" stroke-width="2.5" stroke-dasharray="4,2" fill="none" />
    <text x="310" y="160" fill="#34d399" font-size="10" font-weight="bold">Bus RS-485 / Sensores</text>

    <!-- Cajas de Registro -->
    <circle cx="110" cy="120" r="7" fill="#0284c7" stroke="#e0f2fe" stroke-width="1.5" />
    <circle cx="110" cy="420" r="7" fill="#0284c7" stroke="#e0f2fe" stroke-width="1.5" />
    <circle cx="440" cy="420" r="7" fill="#0284c7" stroke="#e0f2fe" stroke-width="1.5" />
    <circle cx="440" cy="120" r="7" fill="#0284c7" stroke="#e0f2fe" stroke-width="1.5" />
    <circle cx="275" cy="530" r="7" fill="#0284c7" stroke="#e0f2fe" stroke-width="1.5" />
  </g>

  <!-- Tabla Normativa a la Derecha -->
  <g transform="translate(680, 60)">
    <rect x="0" y="0" width="480" height="640" fill="#152132" stroke="#475569" stroke-width="2" rx="6" />
    <text x="20" y="35" fill="#f8fafc" font-size="14" font-weight="bold">TABLA DE SEGREGACIÓN Y OCUPACIÓN</text>
    <line x1="15" y1="50" x2="465" y2="50" stroke="#64748b" stroke-width="1.5" />

    <!-- Encabezados -->
    <text x="20" y="75" fill="#94a3b8" font-size="11" font-weight="bold">SERVICIO</text>
    <text x="140" y="75" fill="#94a3b8" font-size="11" font-weight="bold">DUCTO</text>
    <text x="270" y="75" fill="#94a3b8" font-size="11" font-weight="bold">SEPARACIÓN</text>
    <text x="390" y="75" fill="#94a3b8" font-size="11" font-weight="bold">OCUPACIÓN</text>
    <line x1="15" y1="85" x2="465" y2="85" stroke="#334155" stroke-width="1" />

    <text x="20" y="115" fill="#ef4444" font-size="11" font-weight="bold">Fuerza AC 230V</text>
    <text x="140" y="115" fill="#cbd5e1" font-size="11">PVC C40 / EMT 1"</text>
    <text x="270" y="115" fill="#cbd5e1" font-size="11">0 cm (Base)</text>
    <text x="390" y="115" fill="#e2e8f0" font-size="11">40% máx.</text>

    <text x="20" y="155" fill="#38bdf8" font-size="11" font-weight="bold">Datos Cat6A PoE</text>
    <text x="140" y="155" fill="#cbd5e1" font-size="11">Corrugado LSZH 25mm</text>
    <text x="270" y="155" fill="#4ade80" font-size="11" font-weight="bold">≥ 30 cm</text>
    <text x="390" y="155" fill="#e2e8f0" font-size="11">38% máx.</text>

    <text x="20" y="195" fill="#34d399" font-size="11" font-weight="bold">Bus RS-485 / KNX</text>
    <text x="140" y="195" fill="#cbd5e1" font-size="11">Corrugado LSZH 20mm</text>
    <text x="270" y="195" fill="#4ade80" font-size="11" font-weight="bold">≥ 30 cm</text>
    <text x="390" y="195" fill="#e2e8f0" font-size="11">30% máx.</text>

    <text x="20" y="235" fill="#facc15" font-size="11" font-weight="bold">Fibra Óptica OS2</text>
    <text x="140" y="235" fill="#cbd5e1" font-size="11">Tubo rígido 20mm</text>
    <text x="270" y="235" fill="#cbd5e1" font-size="11">≥ 10 cm</text>
    <text x="390" y="235" fill="#e2e8f0" font-size="11">20% máx.</text>

    <text x="20" y="275" fill="#c084fc" font-size="11" font-weight="bold">Cruces AC / Datos</text>
    <text x="140" y="275" fill="#cbd5e1" font-size="11">Cruce perpendicular</text>
    <text x="270" y="275" fill="#c084fc" font-size="11" font-weight="bold">Ángulo 90°</text>
    <text x="390" y="275" fill="#cbd5e1" font-size="11">Blindado Fe</text>

    <line x1="15" y1="305" x2="465" y2="305" stroke="#64748b" stroke-width="1.5" />

    <text x="20" y="335" fill="#facc15" font-size="12" font-weight="bold">REGLAS CRÍTICAS DE EJECUCIÓN:</text>
    <text x="20" y="365" fill="#cbd5e1" font-size="10">• Inmunidad a EMI: Separación mínima de 30 cm en recorridos paralelos.</text>
    <text x="20" y="390" fill="#cbd5e1" font-size="10">• Cruces Obligatorios: En ángulo exacto de 90° para anular acoplamiento inductivo.</text>
    <text x="20" y="415" fill="#cbd5e1" font-size="10">• Radio de Curvatura: R ≥ 6 x D (mínimo 150 mm) para no estrangular Cat6A.</text>
    <text x="20" y="440" fill="#cbd5e1" font-size="10">• Cajas de Registro: Máximo cada 15 metros o tras dos codos acumulados (180°).</text>
    <text x="20" y="465" fill="#cbd5e1" font-size="10">• Cero Halógenos: Todos los ductos empotrados deben ser LSZH (autoextinguibles).</text>
    <text x="20" y="490" fill="#cbd5e1" font-size="10">• Hilo Guía: Hilo de tracción de nylon 50 kg permanente en cada conduit.</text>
    <text x="20" y="515" fill="#cbd5e1" font-size="10">• Factor de Relleno: Nunca superar el 40% de la sección útil para disipación térmica.</text>
    <text x="20" y="550" fill="#38bdf8" font-size="10" font-weight="bold">Conformidad: ANSI/TIA-569-E, ISO/IEC 11801, REBT ITC-BT-21 y NEC Art. 300</text>
  </g>
</svg>"""

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"SVG canalizaciones guardado en: {svg_path}")

if __name__ == "__main__":
    dxf_out = "/home/ral/Documents/GitHub/open-source-domotics/00_diseno_arquitectonico_y_estructural/06_canalizaciones_y_ductos_electricos_normativa/trazado_canalizaciones/plano_canalizaciones_segregadas.dxf"
    svg_out = "/home/ral/Documents/GitHub/open-source-domotics/00_diseno_arquitectonico_y_estructural/06_canalizaciones_y_ductos_electricos_normativa/trazado_canalizaciones/plano_canalizaciones_segregadas.svg"
    generar_plano_canalizaciones(dxf_out, svg_out)

