#!/usr/bin/env python3
"""
Generador de Plano CAD 2D: Zonificación de Detección de Incendio EN54, CO y Extinción por Aerosol
Formatos de salida: DXF (AutoCAD R12) y SVG vectorial
Módulo: 03_seguridad_y_control_acceso/07_seguridad_incendio_co_y_aerosoles/mecanico
"""

import os
import sys

# Asegurar path para importar SimpleDXF
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generar_planos_dxf import SimpleDXF

def generar_plano_incendio(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_ROTULO", color=7)
    dxf.add_layer("ESTRUCTURA_MUROS", color=8)
    dxf.add_layer("DETECTOR_HUMO_EN54", color=1)
    dxf.add_layer("DETECTOR_CO", color=2)
    dxf.add_layer("CAPSULA_AEROSOL", color=6)
    dxf.add_layer("SIRENAS_EVACUACION", color=3)
    dxf.add_layer("LAZO_SUPERVISADO", color=4)
    dxf.add_layer("TEXTO_NOTAS", color=7)

    # Marco y Cajetín A3 (420 x 297 mm)
    dxf.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf.add_rect(210, 10, 200, 45, layer="MARCO_ROTULO")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", 215, 45, height=4.0, layer="TEXTO_NOTAS")
    dxf.add_text("PLANTA DE PROTECCION CONTRA INCENDIOS, CO Y EXTINCION POR AEROSOL", 215, 36, height=2.0, layer="TEXTO_NOTAS")
    dxf.add_text("Detectores Ópticos EN54-7 | Sensor CO Electroquímico | Cápsulas Stat-X 60E", 215, 26, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Lazo Supervisado EOL 4.7kΩ | Disparo Seguro por Supercap | Enclavamiento VMC/Gas", 215, 16, height=1.4, layer="TEXTO_NOTAS")

    # Planta de la vivienda 10x10 m (Escala 1:60, factor s=18.0)
    ox, oy = 25.0, 75.0
    s = 18.0

    # Perímetro exterior
    dxf.add_rect(ox, oy, 10.0 * s, 10.0 * s, layer="ESTRUCTURA_MUROS")
    dxf.add_text("VIVIENDA AUTOSUSTENTABLE 10 x 10 m", ox + 5, oy + 10.0*s + 5, height=2.0, layer="TEXTO_NOTAS")

    # Habitaciones y zonas
    # Cuarto Técnico IT Central (X=4.0 a 6.5, Y=4.0 a 6.5)
    cx, cy = ox + 4.0 * s, oy + 4.0 * s
    dxf.add_rect(cx, cy, 2.5 * s, 2.5 * s, layer="ESTRUCTURA_MUROS")
    dxf.add_text("SALA TECNICA IT / ESS", cx + 5, cy + 38, height=1.6, layer="TEXTO_NOTAS")

    # Cocina (X=0 a 4.0, Y=6.0 a 10.0)
    dxf.add_rect(ox, oy + 6.0 * s, 4.0 * s, 4.0 * s, layer="ESTRUCTURA_MUROS")
    dxf.add_text("COCINA", ox + 5, oy + 9.5 * s, height=1.6, layer="TEXTO_NOTAS")

    # Salón / Comedor (X=0 a 6.5, Y=0 a 4.0)
    dxf.add_rect(ox, oy, 6.5 * s, 4.0 * s, layer="ESTRUCTURA_MUROS")
    dxf.add_text("SALON / COMEDOR", ox + 5, oy + 3.5 * s, height=1.6, layer="TEXTO_NOTAS")

    # Dormitorio Principal (X=6.5 a 10.0, Y=0 a 5.0)
    dxf.add_rect(ox + 6.5 * s, oy, 3.5 * s, 5.0 * s, layer="ESTRUCTURA_MUROS")
    dxf.add_text("DORMITORIO 1", ox + 6.7 * s, oy + 4.5 * s, height=1.6, layer="TEXTO_NOTAS")

    # Dormitorio Infantil (X=6.5 a 10.0, Y=5.0 a 10.0)
    dxf.add_rect(ox + 6.5 * s, oy + 5.0 * s, 3.5 * s, 5.0 * s, layer="ESTRUCTURA_MUROS")
    dxf.add_text("DORMITORIO 2", ox + 6.7 * s, oy + 9.5 * s, height=1.6, layer="TEXTO_NOTAS")

    # 1. Detectores Ópticos de Humo EN 54-7 (SD)
    # SD-01 en Salón
    dxf.add_circle(ox + 3.2 * s, oy + 2.0 * s, 4.0, layer="DETECTOR_HUMO_EN54")
    dxf.add_text("SD-01", ox + 3.2 * s - 4, oy + 2.0 * s - 6, height=1.3, layer="DETECTOR_HUMO_EN54")

    # SD-02 en Cocina (Detector Térmico/Óptico combinado)
    dxf.add_circle(ox + 2.0 * s, oy + 8.0 * s, 4.0, layer="DETECTOR_HUMO_EN54")
    dxf.add_text("SD-02 (Term/Opt)", ox + 2.0 * s - 8, oy + 8.0 * s - 6, height=1.3, layer="DETECTOR_HUMO_EN54")

    # SD-03 en Cuarto IT (Doble Detector para coincidencia cruzada)
    dxf.add_circle(cx + 0.8 * s, cy + 1.2 * s, 4.0, layer="DETECTOR_HUMO_EN54")
    dxf.add_text("SD-03 (IT)", cx + 0.8 * s - 5, cy + 1.2 * s - 6, height=1.3, layer="DETECTOR_HUMO_EN54")
    dxf.add_circle(cx + 1.8 * s, cy + 1.2 * s, 4.0, layer="DETECTOR_HUMO_EN54")
    dxf.add_text("SD-04 (ESS)", cx + 1.8 * s - 5, cy + 1.2 * s - 6, height=1.3, layer="DETECTOR_HUMO_EN54")

    # SD-05 en Dormitorio 1
    dxf.add_circle(ox + 8.2 * s, oy + 2.5 * s, 4.0, layer="DETECTOR_HUMO_EN54")
    dxf.add_text("SD-05", ox + 8.2 * s - 4, oy + 2.5 * s - 6, height=1.3, layer="DETECTOR_HUMO_EN54")

    # SD-06 en Dormitorio 2
    dxf.add_circle(ox + 8.2 * s, oy + 7.5 * s, 4.0, layer="DETECTOR_HUMO_EN54")
    dxf.add_text("SD-06", ox + 8.2 * s - 4, oy + 7.5 * s - 6, height=1.3, layer="DETECTOR_HUMO_EN54")

    # 2. Detectores de Monóxido de Carbono (CO)
    # CO-01 en Cocina
    dxf.add_rect(ox + 0.8 * s, oy + 8.5 * s, 6.0, 6.0, layer="DETECTOR_CO")
    dxf.add_text("CO-01", ox + 0.8 * s, oy + 8.5 * s - 4, height=1.3, layer="DETECTOR_CO")

    # CO-02 en Sala Técnica
    dxf.add_rect(cx + 0.4 * s, cy + 2.0 * s, 6.0, 6.0, layer="DETECTOR_CO")
    dxf.add_text("CO-02", cx + 0.4 * s, cy + 2.0 * s - 4, height=1.3, layer="DETECTOR_CO")

    # 3. Cápsulas Extintoras de Aerosol Stat-X (EXT)
    # EXT-01 dentro de Rack IT 19"
    dxf.add_circle(cx + 1.0 * s, cy + 0.6 * s, 5.0, layer="CAPSULA_AEROSOL")
    dxf.add_text("EXT-01 (Rack IT)", cx + 1.0 * s - 8, cy + 0.6 * s + 7, height=1.4, layer="CAPSULA_AEROSOL")

    # EXT-02 dentro de Gabinete Baterías LiFePO4
    dxf.add_circle(cx + 2.0 * s, cy + 0.6 * s, 5.0, layer="CAPSULA_AEROSOL")
    dxf.add_text("EXT-02 (LiFePO4)", cx + 2.0 * s - 8, cy + 0.6 * s + 7, height=1.4, layer="CAPSULA_AEROSOL")

    # Pulsador de Parada / Aborto de Extinción (Pared exterior cuarto IT)
    dxf.add_rect(cx - 3, cy + 15, 6, 8, layer="CAPSULA_AEROSOL")
    dxf.add_text("ABORT EXTING", cx - 18, cy + 26, height=1.3, layer="TEXTO_NOTAS")

    # 4. Matriz de Causa y Efecto (Derecha)
    mx, my = 230.0, 210.0
    dxf.add_text("MATRIZ DE CAUSA Y EFECTO EN CASO DE INCENDIO", mx - 10, my + 50, height=2.0, layer="TEXTO_NOTAS")

    dxf.add_rect(mx - 10, my - 25, 185, 68, layer="MARCO_ROTULO")
    dxf.add_text("1. DETECCION (SD o CO):", mx - 5, my + 35, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("   - Disparo Sirena 110dB interior + Strobe exterior", mx - 5, my + 27, height=1.3, layer="DETECTOR_HUMO_EN54")
    dxf.add_text("   - Notificacion Push Critica a smartphones residentes", mx - 5, my + 20, height=1.3, layer="DETECTOR_HUMO_EN54")

    dxf.add_text("2. AISLAMIENTO Y EVACUACION AUTOMATICA (< 2 seg):", mx - 5, my + 10, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("   - Parada inmediata de VMC y Climatizacion Multi-Split (corte oxigeno)", mx - 5, my + 2, height=1.3, layer="SIRENAS_EVACUACION")
    dxf.add_text("   - Cierre automatico de electrovalvulas de Gas Natural y Biogas", mx - 5, my - 6, height=1.3, layer="SIRENAS_EVACUACION")
    dxf.add_text("   - Apertura 100% de persianas motorizadas (desbloqueo de salidas)", mx - 5, my - 14, height=1.3, layer="SIRENAS_EVACUACION")
    dxf.add_text("   - Encendido 100% luces interiores blanco brillante (ruta de escape)", mx - 5, my - 22, height=1.3, layer="SIRENAS_EVACUACION")

    dxf.add_text("3. EXTINCION POR AEROSOL CONDENSADO (ZONAS IT / ESS):", mx - 5, my - 38, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("   - Coincidencia cruzada confirmada (SD-03 + SD-04)", mx - 5, my - 46, height=1.3, layer="CAPSULA_AEROSOL")
    dxf.add_text("   - Cuenta regresiva sonora de 30 segundos (abortable por pulsador)", mx - 5, my - 54, height=1.3, layer="CAPSULA_AEROSOL")
    dxf.add_text("   - Descarga aerosol K2CO3: extincion quimica en 10 seg sin residuos", mx - 5, my - 62, height=1.3, layer="CAPSULA_AEROSOL")

    dxf.save()

    # 2. GENERACIÓN SVG VECTORIAL
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 297" width="100%" height="100%" style="background-color: #1a1921; font-family: monospace;">
  <defs>
    <style>
      .marco {{ stroke: #454255; stroke-width: 1.0; fill: none; }}
      .muros {{ stroke: #7d7987; stroke-width: 1.6; fill: #24222c; }}
      .muros-it {{ stroke: #ef476f; stroke-width: 1.4; fill: #381b24; }}
      .sd-humo {{ stroke: #e63946; stroke-width: 1.2; fill: #d90429; }}
      .co-sensor {{ stroke: #ffd166; stroke-width: 1.2; fill: #f77f00; }}
      .aerosol {{ stroke: #7209b7; stroke-width: 1.4; fill: #f72585; }}
      .bloque-matriz {{ stroke: #4361ee; stroke-width: 1.2; fill: #1c2541; }}
      .txt-title {{ fill: #ffffff; font-size: 4px; font-weight: bold; }}
      .txt-sub {{ fill: #00f0ff; font-size: 2.2px; font-weight: bold; }}
      .txt-body {{ fill: #cad2c5; font-size: 1.6px; }}
      .txt-fire {{ fill: #ff4d6d; font-size: 1.4px; font-weight: bold; }}
      .txt-tag {{ fill: #ffbe0b; font-size: 1.3px; }}
    </style>
  </defs>

  <!-- Marco A3 -->
  <rect x="5" y="5" width="410" height="287" class="marco"/>
  <rect x="210" y="242" width="200" height="45" class="marco"/>
  <text x="215" y="254" class="txt-title">OPEN-SOURCE-DOMOTICS</text>
  <text x="215" y="262" class="txt-sub">PLANTA DE PROTECCIÓN CONTRA INCENDIOS, CO Y EXTINCIÓN</text>
  <text x="215" y="271" class="txt-body">Detectores Ópticos EN54-7 | Sensor CO Electroquímico | Cápsulas Stat-X 60E</text>
  <text x="215" y="279" class="txt-body">Lazo Supervisado EOL 4.7kΩ | Disparo Seguro por Supercap | Enclavamiento VMC/Gas</text>

  <!-- Vivienda 10x10 m -->
  <g id="planta_incendio">
    <rect x="{ox}" y="{297 - (oy + 10.0*s)}" width="{10.0*s}" height="{10.0*s}" class="muros"/>
    <text x="{ox + 5}" y="{297 - (oy + 10.0*s + 4)}" class="txt-sub">VIVIENDA 10 x 10 m - ZONIFICACIÓN EN54</text>

    <!-- Sala Técnica IT Central -->
    <rect x="{cx}" y="{297 - (cy + 2.5*s)}" width="{2.5*s}" height="{2.5*s}" class="muros-it"/>
    <text x="{cx + 4}" y="{297 - (cy + 2.0*s)}" class="txt-fire">ZONA EXTINCIÓN IT/ESS</text>

    <!-- Detectores de Humo (Rojo) -->
    <circle cx="{ox + 3.2*s}" cy="{297 - (oy + 2.0*s)}" r="4" class="sd-humo"/>
    <text x="{ox + 3.2*s - 6}" y="{297 - (oy + 2.0*s - 7)}" class="txt-fire">SD-01</text>

    <circle cx="{ox + 2.0*s}" cy="{297 - (oy + 8.0*s)}" r="4" class="sd-humo"/>
    <text x="{ox + 2.0*s - 12}" y="{297 - (oy + 8.0*s - 7)}" class="txt-fire">SD-02 (Coc)</text>

    <circle cx="{cx + 0.8*s}" cy="{297 - (cy + 1.2*s)}" r="4" class="sd-humo"/>
    <circle cx="{cx + 1.8*s}" cy="{297 - (cy + 1.2*s)}" r="4" class="sd-humo"/>
    <text x="{cx + 0.5*s}" y="{297 - (cy + 1.2*s - 7)}" class="txt-fire">SD-03/04 (Coincidencia)</text>

    <circle cx="{ox + 8.2*s}" cy="{297 - (oy + 2.5*s)}" r="4" class="sd-humo"/>
    <text x="{ox + 8.2*s - 6}" y="{297 - (oy + 2.5*s - 7)}" class="txt-fire">SD-05</text>

    <circle cx="{ox + 8.2*s}" cy="{297 - (oy + 7.5*s)}" r="4" class="sd-humo"/>
    <text x="{ox + 8.2*s - 6}" y="{297 - (oy + 7.5*s - 7)}" class="txt-fire">SD-06</text>

    <!-- Detectores CO (Amarillo) -->
    <rect x="{ox + 0.8*s}" y="{297 - (oy + 8.5*s)}" width="6" height="6" class="co-sensor" rx="1"/>
    <text x="{ox + 0.8*s - 2}" y="{297 - (oy + 8.5*s - 6)}" class="txt-tag">CO-01</text>

    <rect x="{cx + 0.4*s}" y="{297 - (cy + 2.0*s)}" width="6" height="6" class="co-sensor" rx="1"/>
    <text x="{cx + 0.4*s - 2}" y="{297 - (cy + 2.0*s - 6)}" class="txt-tag">CO-02</text>

    <!-- Cápsulas de Aerosol (Magenta/Morado) -->
    <circle cx="{cx + 1.0*s}" cy="{297 - (cy + 0.6*s)}" r="5" class="aerosol"/>
    <text x="{cx + 0.6*s}" y="{297 - (cy + 0.6*s - 8)}" class="txt-fire">EXT-01 (Rack)</text>

    <circle cx="{cx + 2.0*s}" cy="{297 - (cy + 0.6*s)}" r="5" class="aerosol"/>
    <text x="{cx + 1.6*s}" y="{297 - (cy + 0.6*s - 8)}" class="txt-fire">EXT-02 (Baterías)</text>
  </g>

  <!-- Matriz de Causa y Efecto (Derecha) -->
  <g id="matriz_seguridad">
    <text x="215" y="45" class="txt-sub">PROTOCOLO DE SEGURIDAD Y EVACUACIÓN AUTOMÁTICA</text>

    <rect x="215" y="55" width="190" height="175" class="bloque-matriz" rx="2"/>

    <text x="220" y="70" class="txt-sub">1. DETECCIÓN TEMPRANA (HUMO / CO):</text>
    <text x="225" y="80" class="txt-body">• Lazo cableado supervisado clase B (EOL 4.7 kΩ)</text>
    <text x="225" y="88" class="txt-body">• Sirena interior 110 dB + Strobe exterior intermitente</text>
    <text x="225" y="96" class="txt-body">• Notificación Push Crítica (bypass de modo 'No Molestar')</text>

    <text x="220" y="112" class="txt-sub">2. INTERVENCIONES MECÁNICAS INMEDIATAS (&lt; 2s):</text>
    <text x="225" y="122" class="txt-fire">• Parada total de VMC y Clima (bloqueo aporte oxígeno)</text>
    <text x="225" y="130" class="txt-fire">• Corte inmediato electroválvulas Gas Natural / Biogás</text>
    <text x="225" y="138" class="txt-body">• Apertura 100% de persianas (liberación de vías de escape)</text>
    <text x="225" y="146" class="txt-body">• Iluminación blanca 100% de cortesía en toda la casa</text>

    <text x="220" y="162" class="txt-sub">3. EXTINCIÓN POR AEROSOL (RACK IT / ESS LiFePO4):</text>
    <text x="225" y="172" class="txt-body">• Activación por coincidencia cruzada (2 detectores)</text>
    <text x="225" y="180" class="txt-body">• Cuenta atrás de 30 segundos con avisador zumbador</text>
    <text x="225" y="188" class="txt-body">• Pulsador manual de aborto de extinción en pasillo</text>
    <text x="225" y="196" class="txt-fire">• Disparo por Supercondensador 24V 2A (inmune a corte eléctrico)</text>
    <text x="225" y="204" class="txt-body">• Aerosol de K2CO3: supresión en 10s sin agua ni residuos</text>
  </g>
</svg>
"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Plano CAD 2D DXF generado en: {dxf_path}")
    print(f"Plano vectorial SVG generado en: {svg_path}")

if __name__ == "__main__":
    dxf_out = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/07_seguridad_incendio_co_y_aerosoles/mecanico/plano_seguridad_incendio_aerosoles.dxf"
    svg_out = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/07_seguridad_incendio_co_y_aerosoles/mecanico/plano_seguridad_incendio_aerosoles.svg"
    generar_plano_incendio(dxf_out, svg_out)

