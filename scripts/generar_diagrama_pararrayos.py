#!/usr/bin/env python3
"""
Generador del Esquema Eléctrico de Pararrayos PDC, Equipotencialidad y Malla de Puesta a Tierra
Formatos de salida: DXF y SVG vectorial
Proyecto: open-source-domotics
"""

import os
from generar_planos_dxf import SimpleDXF

def generar_diagrama_pararrayos(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_ROTULO", color=7)
    dxf.add_layer("CABEZAL_PDC", color=1)
    dxf.add_layer("BAJADA_COBRE", color=3)
    dxf.add_layer("RED_TIERRAS", color=2)
    dxf.add_layer("EQUIPOTENCIAL_DPS", color=4)
    dxf.add_layer("TEXTO_NOTAS", color=7)

    # Marco y Cajetín A3
    dxf.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf.add_rect(230, 10, 180, 42, layer="MARCO_ROTULO")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", 235, 42, height=4.0, layer="TEXTO_NOTAS")
    dxf.add_text("PROTECCIÓN ATMOSFÉRICA, PARARRAYOS PDC Y MALLA DE TIERRAS", 235, 32, height=2.0, layer="TEXTO_NOTAS")
    dxf.add_text("PDC Delta-t >= 45 microseg | Malla Triangulada R <= 5 Ohm | Spark Gap 100kA", 235, 22, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Normas UNE 21186 / NF C 17-102 / IEC 62305 (Nivel I de Protección)", 235, 14, height=1.4, layer="TEXTO_NOTAS")

    # 1. Cabezal Captador PDC en Cúspide
    dxf.add_rect(45, 240, 25, 35, layer="CABEZAL_PDC")
    dxf.add_line(57.5, 275, 57.5, 285, layer="CABEZAL_PDC")
    dxf.add_text("CABEZAL PDC", 47, 265, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Δt ≥ 45 µs", 47, 255, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("Radio = 45m", 47, 245, height=1.3, layer="TEXTO_NOTAS")

    # Mástil Soporte 3 metros
    dxf.add_line(57.5, 240, 57.5, 190, layer="CABEZAL_PDC")
    dxf.add_text("Mástil Inox 3m", 60, 215, height=1.4, layer="TEXTO_NOTAS")

    # Perfil Vivienda / Azotea
    dxf.add_rect(30, 100, 140, 90, layer="MARCO_ROTULO")
    dxf.add_text("VIVIENDA BIOCLIMÁTICA 10x10 m", 40, 150, height=2.0, layer="TEXTO_NOTAS")
    dxf.add_text("Nivel Cubierta (+3.20 m)", 40, 140, height=1.5, layer="TEXTO_NOTAS")

    # 2. Conductor de Bajada Exterior (50 mm² Cu)
    dxf.add_line(57.5, 190, 25, 190, layer="BAJADA_COBRE")
    dxf.add_line(25, 190, 25, 45, layer="BAJADA_COBRE")
    dxf.add_text("Conductor Bajada Cu 50 mm²", 10, 120, height=1.4, layer="TEXTO_NOTAS")

    # Contador de Rayos y Junta de Prueba en Fachada / Arqueta
    dxf.add_rect(15, 60, 20, 25, layer="EQUIPOTENCIAL_DPS")
    dxf.add_text("CONTADOR", 17, 78, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("DE RAYOS", 17, 70, height=1.4, layer="TEXTO_NOTAS")

    # 3. Puesta a Tierra del Pararrayos: Triangulación de 3 Picas
    # Arqueta de Registro
    dxf.add_rect(15, 30, 20, 15, layer="RED_TIERRAS")
    dxf.add_text("Arqueta", 17, 38, height=1.3, layer="TEXTO_NOTAS")

    # Pica 1
    dxf.add_line(25, 30, 25, 10, layer="RED_TIERRAS")
    dxf.add_text("Pica 1 (2m)", 27, 18, height=1.3, layer="TEXTO_NOTAS")

    # Conexión enterrada hacia Pica 2 y 3 (Separación 4 metros)
    dxf.add_line(25, 20, 65, 20, layer="RED_TIERRAS")
    dxf.add_line(65, 20, 65, 10, layer="RED_TIERRAS")
    dxf.add_text("Pica 2 (2m)", 67, 18, height=1.3, layer="TEXTO_NOTAS")

    dxf.add_line(65, 20, 105, 20, layer="RED_TIERRAS")
    dxf.add_line(105, 20, 105, 10, layer="RED_TIERRAS")
    dxf.add_text("Pica 3 (2m)", 107, 18, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("Malla Triangulada R ≤ 5 Ω (Mejorador grafito/bentonita)", 30, 8, height=1.4, layer="TEXTO_NOTAS")

    # 4. Vía de Chispas (Spark Gap) de Equipotencialidad 100 kA
    dxf.add_rect(130, 40, 35, 30, layer="EQUIPOTENCIAL_DPS")
    dxf.add_text("SPARK GAP", 133, 62, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Vía de Chispas", 133, 52, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("100 kA (10/350)", 133, 44, height=1.3, layer="TEXTO_NOTAS")

    # Enlace entre tierra pararrayos y vía de chispas
    dxf.add_line(105, 20, 130, 55, layer="RED_TIERRAS")
    # Enlace entre vía de chispas y barra equipotencial general
    dxf.add_line(165, 55, 190, 55, layer="RED_TIERRAS")

    # Barra Equipotencial Principal de la Vivienda (BEP)
    dxf.add_rect(190, 45, 15, 60, layer="EQUIPOTENCIAL_DPS")
    dxf.add_text("BEP", 192, 95, height=1.8, layer="TEXTO_NOTAS")
    dxf.add_text("Barra Cu", 192, 85, height=1.2, layer="TEXTO_NOTAS")
    dxf.add_text("General", 192, 75, height=1.2, layer="TEXTO_NOTAS")
    dxf.add_text("Tierra", 192, 65, height=1.2, layer="TEXTO_NOTAS")

    # Anillo Perimetral de Tierras Vivienda
    dxf.add_line(197, 45, 197, 20, layer="RED_TIERRAS")
    dxf.add_text("Hacia Anillo de Cimentación", 200, 25, height=1.3, layer="TEXTO_NOTAS")

    # 5. Coordinación de Protectores de Sobretensión (DPS Clase I + II)
    dxf.add_rect(240, 100, 75, 55, layer="EQUIPOTENCIAL_DPS")
    dxf.add_text("TABLERO TGBT - DPS", 243, 145, height=1.8, layer="TEXTO_NOTAS")
    dxf.add_text("DPS Clase I+II Combinado", 243, 133, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("Iimp ≥ 25 kA / polo (10/350µs)", 243, 122, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("Nivel protección Up ≤ 1.5 kV", 243, 112, height=1.3, layer="TEXTO_NOTAS")

    # Enlace desde DPS hacia Barra BEP
    dxf.add_line(240, 115, 205, 75, layer="EQUIPOTENCIAL_DPS")

    # Notas Técnicas
    dxf.add_rect(230, 170, 180, 110, layer="MARCO_ROTULO")
    dxf.add_text("CRITERIOS DE DISEÑO Y NORMAS TÉCNICAS:", 235, 270, height=1.8, layer="TEXTO_NOTAS")
    dxf.add_text("1. Nivel de Protección: Nivel I (Eficacia 98% según IEC 62305).", 235, 258, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("2. Radio de Protección: Rp = 45 metros a h = 5 metros del cabezal.", 235, 246, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("3. Conductor de Bajada: Pletina o cable Cu 50 mm² sin bucles agudos.", 235, 234, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("4. Separación de Seguridad: s ≥ 0.04 · (l / kr) para evitar chispazos.", 235, 222, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("5. Vía de Chispas (Spark Gap): Evita bucles de tierra e interferencias,", 235, 210, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("   pero une galvánicamente las tierras ante una descarga (>100 kA).", 235, 200, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("6. Resistencia de Puesta a Tierra: Obligatorio R ≤ 5 Ω medido en arqueta.", 235, 188, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("7. Monitoreo IoT: Sensor inductivo de pulsos en bajante conectado a HA.", 235, 176, height=1.3, layer="TEXTO_NOTAS")

    dxf.save()
    print(f"DXF pararrayos guardado en: {dxf_path}")

    # 2. GENERACIÓN SVG
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 850" width="100%" height="100%" style="background-color: #0d1522; font-family: monospace, sans-serif;">
  <rect x="20" y="20" width="1160" height="810" fill="none" stroke="#1e293b" stroke-width="2" rx="8" />

  <!-- Cajetin -->
  <rect x="680" y="730" width="480" height="80" fill="#152132" stroke="#3b82f6" stroke-width="2" rx="4" />
  <text x="700" y="755" fill="#60a5fa" font-size="16" font-weight="bold">OPEN-SOURCE-DOMOTICS</text>
  <text x="700" y="775" fill="#f8fafc" font-size="13" font-weight="bold">PROTECCIÓN ATMOSFÉRICA, PARARRAYOS PDC Y MALLA DE TIERRAS</text>
  <text x="700" y="795" fill="#94a3b8" font-size="11">PDC Δt ≥ 45µs | Malla Triangulada R ≤ 5 Ω | Spark Gap 100kA | DPS Clase I+II</text>

  <!-- Cabezal PDC y Mastil -->
  <g transform="translate(180, 50)">
    <!-- Punta Captadora -->
    <polygon points="40,10 35,60 45,60" fill="#facc15" stroke="#f59e0b" stroke-width="2" />
    <!-- Dispositivo de Cebado Ionico -->
    <rect x="20" y="60" width="40" height="60" fill="#1e293b" stroke="#3b82f6" stroke-width="2" rx="4" />
    <circle cx="40" cy="90" r="28" fill="none" stroke="#60a5fa" stroke-width="2" stroke-dasharray="4,2" />
    <text x="-40" y="85" fill="#60a5fa" font-size="12" font-weight="bold">CABEZAL PDC</text>
    <text x="-40" y="105" fill="#f8fafc" font-size="11">Δt ≥ 45 µs</text>
    
    <!-- Mastil Galvanizado -->
    <rect x="36" y="120" width="8" height="140" fill="#94a3b8" />
    <text x="55" y="180" fill="#cbd5e1" font-size="11">Mástil Acero Inox 3m</text>
  </g>

  <!-- Silueta Vivienda Bioclimatica -->
  <g transform="translate(140, 310)">
    <rect x="0" y="0" width="420" height="240" fill="#1e293b" stroke="#64748b" stroke-width="2" rx="4" />
    <text x="30" y="60" fill="#f8fafc" font-size="16" font-weight="bold">VIVIENDA BIOCLIMÁTICA 10 x 10 m</text>
    <text x="30" y="90" fill="#94a3b8" font-size="12">Nivel de Azotea (+3.20 m) con Aerogenerador y Paneles</text>
    <text x="30" y="120" fill="#38bdf8" font-size="12">Radio de Protección Nivel I: Rp = 45 metros</text>
  </g>

  <!-- Conductor de Bajada Cu 50 mm2 -->
  <path d="M 216 310 L 100 310 L 100 600" stroke="#f59e0b" stroke-width="5" fill="none" />
  <text x="15" y="450" fill="#fbbf24" font-size="11" font-weight="bold" transform="rotate(-90 15,450)">Conductor Cu 50 mm²</text>

  <!-- Contador de Rayos -->
  <g transform="translate(70, 480)">
    <rect x="0" y="0" width="60" height="70" fill="#0f172a" stroke="#eab308" stroke-width="2" rx="4" />
    <text x="8" y="25" fill="#facc15" font-size="10" font-weight="bold">CONTADOR</text>
    <text x="8" y="45" fill="#f8fafc" font-size="9">IoT Pulso</text>
    <text x="8" y="60" fill="#22c55e" font-size="9">WiFi ESP32</text>
  </g>

  <!-- Arqueta de Registro y Triangulacion de Picas -->
  <g transform="translate(60, 600)">
    <rect x="0" y="0" width="80" height="60" fill="#1e293b" stroke="#64748b" stroke-width="2" rx="4" />
    <text x="10" y="25" fill="#f8fafc" font-size="10" font-weight="bold">ARQUETA</text>
    <text x="10" y="45" fill="#94a3b8" font-size="9">Junta prueba</text>
  </g>

  <!-- Picas de Tierra en Triangulo -->
  <!-- Pica 1 -->
  <line x1="100" y1="660" x2="100" y2="760" stroke="#f59e0b" stroke-width="6" stroke-linecap="round" />
  <text x="85" y="780" fill="#fbbf24" font-size="11" font-weight="bold">Pica 1 (2m)</text>

  <!-- Pica 2 (distancia 4m) -->
  <line x1="100" y1="700" x2="250" y2="700" stroke="#f59e0b" stroke-width="4" stroke-dasharray="4,2" />
  <line x1="250" y1="660" x2="250" y2="760" stroke="#f59e0b" stroke-width="6" stroke-linecap="round" />
  <text x="235" y="780" fill="#fbbf24" font-size="11" font-weight="bold">Pica 2 (2m)</text>

  <!-- Pica 3 -->
  <line x1="250" y1="700" x2="400" y2="700" stroke="#f59e0b" stroke-width="4" stroke-dasharray="4,2" />
  <line x1="400" y1="660" x2="400" y2="760" stroke="#f59e0b" stroke-width="6" stroke-linecap="round" />
  <text x="385" y="780" fill="#fbbf24" font-size="11" font-weight="bold">Pica 3 (2m)</text>

  <text x="120" y="730" fill="#4ade80" font-size="13" font-weight="bold">Malla Triangulada: Resistencia R ≤ 5 Ω (Mejorador Mineral)</text>

  <!-- Spark Gap (Via de Chispas 100kA) -->
  <g transform="translate(480, 640)">
    <rect x="0" y="0" width="120" height="90" fill="#1e293b" stroke="#ef4444" stroke-width="2.5" rx="6" />
    <text x="12" y="30" fill="#f87171" font-size="13" font-weight="bold">SPARK GAP</text>
    <text x="12" y="55" fill="#f8fafc" font-size="11">Vía de Chispas</text>
    <text x="12" y="75" fill="#facc15" font-size="11" font-weight="bold">100 kA (10/350)</text>
  </g>
  <path d="M 400 700 L 480 700" stroke="#f59e0b" stroke-width="4" fill="none" />
  <path d="M 600 700 L 680 700" stroke="#38bdf8" stroke-width="4" fill="none" />

  <!-- Barra Equipotencial Principal (BEP) -->
  <g transform="translate(680, 610)">
    <rect x="0" y="0" width="70" height="130" fill="#0f172a" stroke="#38bdf8" stroke-width="2.5" rx="4" />
    <text x="18" y="35" fill="#38bdf8" font-size="16" font-weight="bold">BEP</text>
    <text x="10" y="65" fill="#f8fafc" font-size="10">Barra Cu</text>
    <text x="10" y="85" fill="#cbd5e1" font-size="10">Tierras</text>
    <text x="10" y="105" fill="#cbd5e1" font-size="10">General</text>
  </g>

  <!-- Enlace hacia TGBT y DPS -->
  <path d="M 715 610 L 715 480 L 800 480" stroke="#38bdf8" stroke-width="3" fill="none" />

  <!-- Tablero TGBT con DPS Clase I+II -->
  <g transform="translate(800, 390)">
    <rect x="0" y="0" width="340" height="180" fill="#1e293b" stroke="#a855f7" stroke-width="2.5" rx="8" />
    <text x="20" y="35" fill="#c084fc" font-size="15" font-weight="bold">TGBT - PROTECCIÓN DPS CABECERA</text>
    <text x="20" y="65" fill="#f8fafc" font-size="12">Descargador de Sobretensiones Clase I+II</text>
    <text x="20" y="90" fill="#facc15" font-size="12">• Iimp = 25 kA / polo (Onda 10/350 µs)</text>
    <text x="20" y="115" fill="#cbd5e1" font-size="12">• In = 40 kA (Onda 8/20 µs) | Up ≤ 1.5 kV</text>
    <text x="20" y="140" fill="#4ade80" font-size="12">• Contacto seco de telemetría a Home Assistant</text>
    <text x="20" y="160" fill="#94a3b8" font-size="11">Desconexión y aviso inmediato tras descarga</text>
  </g>

  <!-- Cuadro Superior Derecho: Notas Normativas -->
  <g transform="translate(680, 50)">
    <rect x="0" y="0" width="480" height="310" fill="#152132" stroke="#475569" stroke-width="2" rx="6" />
    <text x="20" y="35" fill="#f8fafc" font-size="14" font-weight="bold">ESPECIFICACIONES Y NORMAS TÉCNICAS</text>
    <line x1="15" y1="50" x2="465" y2="50" stroke="#64748b" stroke-width="1.5" />
    
    <text x="20" y="80" fill="#cbd5e1" font-size="11">• Normas de Referencia: UNE 21186, NF C 17-102 e IEC 62305 (Nivel I).</text>
    <text x="20" y="110" fill="#cbd5e1" font-size="11">• Radio de Cobertura: Rp = 45m (Protege vivienda, torre eólica y cochera EV).</text>
    <text x="20" y="140" fill="#cbd5e1" font-size="11">• Conductor de Bajada: Cu 50 mm² sin bucles cerrados ni radios &lt; 20 cm.</text>
    <text x="20" y="170" fill="#cbd5e1" font-size="11">• Vía de Chispas (Spark Gap): Elimina corrosión galvánica y bucles parásitos,</text>
    <text x="20" y="190" fill="#cbd5e1" font-size="11">  pero ecualiza potenciales a 0V instantáneamente durante el impacto.</text>
    <text x="20" y="220" fill="#cbd5e1" font-size="11">• Resistencia Medida: R ≤ 5 Ω obligatoria con telurómetro en arqueta.</text>
    <text x="20" y="250" fill="#cbd5e1" font-size="11">• Coordinación DPS: Tipo 1 en cabecera + Tipo 2 en subcuadros + Tipo 3 en rack.</text>
    <text x="20" y="285" fill="#38bdf8" font-size="11" font-weight="bold">Integración IoT: Conteo de eventos y salud de descargadores en HA</text>
  </g>
</svg>"""

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"SVG pararrayos guardado en: {svg_path}")

if __name__ == "__main__":
    dxf_out = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/08_pararrayos_y_proteccion_descargas/electrico/esquema_pararrayos_tierras.dxf"
    svg_out = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/08_pararrayos_y_proteccion_descargas/electrico/esquema_pararrayos_tierras.svg"
    generar_diagrama_pararrayos(dxf_out, svg_out)
