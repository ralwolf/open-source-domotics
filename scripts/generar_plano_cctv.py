#!/usr/bin/env python3
"""
Generador del Plano de Cobertura de Videovigilancia CCTV PoE y Zonas IA de Frigate
Formatos de salida: DXF y SVG vectorial
Proyecto: open-source-domotics
"""

import os
from generar_planos_dxf import SimpleDXF

def generar_plano_cctv(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_ROTULO", color=7)
    dxf.add_layer("ESTRUCTURA_MUROS", color=8)
    dxf.add_layer("CAMARAS_POE", color=1)
    dxf.add_layer("CONOS_VISION_FOV", color=4)
    dxf.add_layer("ZONAS_DETECCION_IA", color=3)
    dxf.add_layer("TEXTO_NOTAS", color=7)

    # Marco y Cajetín A3
    dxf.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf.add_rect(230, 10, 180, 42, layer="MARCO_ROTULO")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", 235, 42, height=4.0, layer="TEXTO_NOTAS")
    dxf.add_text("PLANO DE COBERTURA CCTV POE Y ZONAS IA (FRIGATE NVR)", 235, 32, height=2.0, layer="TEXTO_NOTAS")
    dxf.add_text("4x Cámaras Torreta 4K/2K PoE | FOV 108° / 89° | Cero Puntos Ciegos", 235, 22, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Aceleración Google Coral TPU | RTSP H.265 en VLAN 40 CCTV Aislada", 235, 14, height=1.4, layer="TEXTO_NOTAS")

    # Origen y Escala
    ox, oy = 30.0, 75.0
    s = 18.0

    # Perímetro de la vivienda 10x10 m
    dxf.add_rect(ox, oy, 10.0 * s, 10.0 * s, layer="ESTRUCTURA_MUROS")
    
    # Cuarto Técnico IT (Centro)
    cx, cy = ox + 4.5 * s, oy + 4.5 * s
    dxf.add_rect(cx, cy, 2.0 * s, 2.0 * s, layer="ESTRUCTURA_MUROS")
    dxf.add_text("RACK IT / SWITCH POE", cx + 2, cy + 18, height=1.5, layer="TEXTO_NOTAS")

    # Patio Central / Lucernario (X=3.5 a 6.5m, Y=4.0 a 6.0m)
    dxf.add_rect(ox + 3.5 * s, oy + 4.0 * s, 3.0 * s, 2.0 * s, layer="ESTRUCTURA_MUROS")
    dxf.add_text("PATIO INTERIOR", ox + 3.8 * s, oy + 4.8 * s, height=1.5, layer="TEXTO_NOTAS")

    # Ubicación de Cámaras PoE y Conos de Visión (FOV)
    # CAM-01: Porche / Entrada Principal (Fachada Sur, X=5.0m, Y=0.0m) mirando hacia afuera (Sur)
    cam1_x, cam1_y = ox + 5.0 * s, oy
    dxf.add_circle(cam1_x, cam1_y, 4.0, layer="CAMARAS_POE")
    dxf.add_text("CAM-01 (Entrada)", cam1_x + 5, cam1_y - 2, height=1.5, layer="TEXTO_NOTAS")
    # Cono de visión 108° hacia abajo (Sur)
    dxf.add_line(cam1_x, cam1_y, cam1_x - 45, cam1_y - 50, layer="CONOS_VISION_FOV")
    dxf.add_line(cam1_x, cam1_y, cam1_x + 45, cam1_y - 50, layer="CONOS_VISION_FOV")
    dxf.add_line(cam1_x - 45, cam1_y - 50, cam1_x + 45, cam1_y - 50, layer="CONOS_VISION_FOV")
    dxf.add_text("Zona Acceso Peatonal (zone_entrada)", cam1_x - 35, cam1_y - 30, height=1.3, layer="ZONAS_DETECCION_IA")

    # CAM-02: Cochera EV / Fachada Oeste (X=0.0m, Y=2.5m) mirando hacia el Norte-Oeste
    cam2_x, cam2_y = ox, oy + 2.5 * s
    dxf.add_circle(cam2_x, cam2_y, 4.0, layer="CAMARAS_POE")
    dxf.add_text("CAM-02 (Cochera EV)", cam2_x - 28, cam2_y + 6, height=1.5, layer="TEXTO_NOTAS")
    # Cono FOV 89°
    dxf.add_line(cam2_x, cam2_y, cam2_x - 20, cam2_y + 60, layer="CONOS_VISION_FOV")
    dxf.add_line(cam2_x, cam2_y, cam2_x - 55, cam2_y + 10, layer="CONOS_VISION_FOV")
    dxf.add_line(cam2_x - 20, cam2_y + 60, cam2_x - 55, cam2_y + 10, layer="CONOS_VISION_FOV")
    dxf.add_text("Zona Vehicular (zone_driveway)", cam2_x - 50, cam2_y + 35, height=1.3, layer="ZONAS_DETECCION_IA")

    # CAM-03: Patio Interior / Lucernario (X=3.5m, Y=6.0m) mirando hacia el Patio
    cam3_x, cam3_y = ox + 3.5 * s, oy + 6.0 * s
    dxf.add_circle(cam3_x, cam3_y, 4.0, layer="CAMARAS_POE")
    dxf.add_text("CAM-03 (Patio)", cam3_x + 5, cam3_y + 4, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_line(cam3_x, cam3_y, cam3_x + 50, cam3_y - 30, layer="CONOS_VISION_FOV")
    dxf.add_line(cam3_x, cam3_y, cam3_x + 10, cam3_y - 35, layer="CONOS_VISION_FOV")
    dxf.add_text("Zona Patio Social (zone_patio)", cam3_x + 8, cam3_y - 18, height=1.2, layer="ZONAS_DETECCION_IA")

    # CAM-04: Fachada Trasera Norte / Caseta Técnica y Biodigestor (X=8.0m, Y=10.0m)
    cam4_x, cam4_y = ox + 8.0 * s, oy + 10.0 * s
    dxf.add_circle(cam4_x, cam4_y, 4.0, layer="CAMARAS_POE")
    dxf.add_text("CAM-04 (Perímetro Técnico)", cam4_x - 50, cam4_y + 10, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_line(cam4_x, cam4_y, cam4_x + 30, cam4_y + 50, layer="CONOS_VISION_FOV")
    dxf.add_line(cam4_x, cam4_y, cam4_x - 50, cam4_y + 40, layer="CONOS_VISION_FOV")
    dxf.add_line(cam4_x + 30, cam4_y + 50, cam4_x - 50, cam4_y + 40, layer="CONOS_VISION_FOV")
    dxf.add_text("Zona Caseta Técnica & Biodigestor", cam4_x - 45, cam4_y + 25, height=1.3, layer="ZONAS_DETECCION_IA")

    # Líneas Cat6A PoE desde Cámaras hasta Switch IT
    dxf.add_line(cam1_x, cam1_y, cx + 18, cy, layer="CAMARAS_POE")
    dxf.add_line(cam2_x, cam2_y, cx, cy + 18, layer="CAMARAS_POE")
    dxf.add_line(cam3_x, cam3_y, cx + 5, cy + 25, layer="CAMARAS_POE")
    dxf.add_line(cam4_x, cam4_y, cx + 25, cy + 25, layer="CAMARAS_POE")

    # Tabla Informativa de Cámaras y Criterios DORI
    tx, ty = 230.0, 75.0
    dxf.add_rect(tx, ty, 180, 165, layer="MARCO_ROTULO")
    dxf.add_text("CUADRO DE CÁMARAS Y CRITERIOS DORI (EN 62676-4)", tx + 5, ty + 155, height=2.0, layer="TEXTO_NOTAS")
    dxf.add_line(tx, ty + 148, tx + 180, ty + 148, layer="MARCO_ROTULO")

    dxf.add_text("Cámara", tx + 5, ty + 140, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("Lente / FOV", tx + 50, ty + 140, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("Resolución", tx + 105, ty + 140, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("Función IA", tx + 145, ty + 140, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_line(tx, ty + 135, tx + 180, ty + 135, layer="MARCO_ROTULO")

    filas = [
        ("CAM-01 Entrada", "2.8mm / 108°", "4K (3840x2160)", "Person / Delivery"),
        ("CAM-02 Cochera", "4.0mm / 89°", "4K (3840x2160)", "Car / License Plate"),
        ("CAM-03 Patio", "2.8mm / 108°", "2K (2560x1440)", "Person / Pet"),
        ("CAM-04 Trasera", "2.8mm / 108°", "2K (2560x1440)", "Perimeter Breach"),
    ]
    cy_c = ty + 125
    for c_id, l_fov, res_c, func_c in filas:
        dxf.add_text(c_id, tx + 5, cy_c, height=1.4, layer="TEXTO_NOTAS")
        dxf.add_text(l_fov, tx + 50, cy_c, height=1.3, layer="TEXTO_NOTAS")
        dxf.add_text(res_c, tx + 105, cy_c, height=1.3, layer="TEXTO_NOTAS")
        dxf.add_text(func_c, tx + 145, cy_c, height=1.3, layer="TEXTO_NOTAS")
        cy_c -= 12

    # Notas Técnicas Frigate NVR y Aceleración Coral
    dxf.add_line(tx, ty + 75, tx + 180, ty + 75, layer="MARCO_ROTULO")
    dxf.add_text("CONFIGURACIÓN FRIGATE NVR + GO2RTC:", tx + 5, ty + 67, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("1. Aceleración Edge TPU: Inferencia en 7-10 ms por frame (Google Coral).", tx + 5, ty + 57, height=1.2, layer="TEXTO_NOTAS")
    dxf.add_text("2. Arquitectura Doble Stream: Detección en substream 640x360@5fps en RAM;", tx + 5, ty + 49, height=1.2, layer="TEXTO_NOTAS")
    dxf.add_text("   Grabación en mainstream 4K/2K a disco TrueNAS solo ante eventos.", tx + 5, ty + 41, height=1.2, layer="TEXTO_NOTAS")
    dxf.add_text("3. Retransmisión WebRTC: go2rtc integrado para latencia < 200 ms.", tx + 5, ty + 33, height=1.2, layer="TEXTO_NOTAS")
    dxf.add_text("4. Red Segregada: Cámaras en VLAN 40 CCTV (Sin acceso a Internet / WAN).", tx + 5, ty + 25, height=1.2, layer="TEXTO_NOTAS")
    dxf.add_text("5. Retención: 7 días continuo en baja + 30 días clips de personas en alta.", tx + 5, ty + 17, height=1.2, layer="TEXTO_NOTAS")

    dxf.save()
    print(f"DXF CCTV guardado en: {dxf_path}")

    # 2. GENERACIÓN SVG
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 850" width="100%" height="100%" style="background-color: #0b111a; font-family: monospace, sans-serif;">
  <rect x="20" y="20" width="1160" height="810" fill="none" stroke="#1e293b" stroke-width="2" rx="8" />

  <!-- Cajetin -->
  <rect x="680" y="730" width="480" height="80" fill="#152132" stroke="#3b82f6" stroke-width="2" rx="4" />
  <text x="700" y="755" fill="#60a5fa" font-size="16" font-weight="bold">OPEN-SOURCE-DOMOTICS</text>
  <text x="700" y="775" fill="#f8fafc" font-size="13" font-weight="bold">PLANO DE COBERTURA CCTV POE Y ZONAS IA (FRIGATE NVR)</text>
  <text x="700" y="795" fill="#94a3b8" font-size="11">4x Cámaras PoE 4K/2K | Coral TPU | go2rtc WebRTC | Cero Puntos Ciegos</text>

  <!-- Vivienda 10m x 10m y Conos de Vision -->
  <g transform="translate(100, 100)">
    <!-- Perímetro Casa -->
    <rect x="0" y="0" width="480" height="480" fill="#111827" stroke="#475569" stroke-width="3" />

    <!-- Sala IT Central -->
    <rect x="190" y="190" width="100" height="100" fill="#1e293b" stroke="#3b82f6" stroke-width="2" />
    <text x="205" y="240" fill="#60a5fa" font-size="11" font-weight="bold">SWITCH POE</text>
    <text x="205" y="255" fill="#cbd5e1" font-size="10">Frigate NVR</text>

    <!-- Patio Central -->
    <rect x="150" y="160" width="180" height="160" fill="none" stroke="#334155" stroke-dasharray="4,4" />
    <text x="195" y="180" fill="#94a3b8" font-size="10">Patio Interior</text>

    <!-- CONOS DE VISION FOV Y CAMARAS -->
    <!-- CAM-01: Entrada Principal Sur -->
    <polygon points="240,480 80,620 400,620" fill="#38bdf8" fill-opacity="0.15" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="5,3" />
    <circle cx="240" cy="480" r="10" fill="#ef4444" stroke="#f87171" stroke-width="2" />
    <text x="255" y="495" fill="#f8fafc" font-size="12" font-weight="bold">CAM-01 (Entrada 4K)</text>
    <text x="160" y="560" fill="#38bdf8" font-size="11" font-weight="bold">ZONA ENTRADA (Person)</text>

    <!-- CAM-02: Cochera EV Oeste -->
    <polygon points="0,120 -150,0 -150,260" fill="#facc15" fill-opacity="0.15" stroke="#facc15" stroke-width="1.5" stroke-dasharray="5,3" />
    <circle cx="0" cy="120" r="10" fill="#ef4444" stroke="#f87171" stroke-width="2" />
    <text x="-140" y="110" fill="#f8fafc" font-size="12" font-weight="bold">CAM-02 (Cochera EV 4K)</text>
    <text x="-130" y="170" fill="#facc15" font-size="11" font-weight="bold">ZONA COCHERA (Car)</text>

    <!-- CAM-03: Patio Interior -->
    <polygon points="150,160 330,160 330,320" fill="#4ade80" fill-opacity="0.15" stroke="#4ade80" stroke-width="1.5" stroke-dasharray="5,3" />
    <circle cx="150" cy="160" r="8" fill="#ef4444" stroke="#f87171" stroke-width="2" />
    <text x="80" y="150" fill="#f8fafc" font-size="11" font-weight="bold">CAM-03 (Patio 2K)</text>

    <!-- CAM-04: Perímetro Trasero Norte -->
    <polygon points="400,0 200,-130 520,-130" fill="#c084fc" fill-opacity="0.15" stroke="#c084fc" stroke-width="1.5" stroke-dasharray="5,3" />
    <circle cx="400" cy="0" r="10" fill="#ef4444" stroke="#f87171" stroke-width="2" />
    <text x="415" y="20" fill="#f8fafc" font-size="12" font-weight="bold">CAM-04 (Trasera 2K)</text>
    <text x="260" y="-60" fill="#c084fc" font-size="11" font-weight="bold">ZONA BIODIGESTOR</text>

    <!-- Cableado PoE Cat6A (Azul) -->
    <line x1="240" y1="480" x2="240" y2="290" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4,2" />
    <line x1="0" y1="120" x2="190" y2="240" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4,2" />
    <line x1="150" y1="160" x2="190" y2="200" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4,2" />
    <line x1="400" y1="0" x2="280" y2="190" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4,2" />
  </g>

  <!-- Tabla Cuadro de Camaras y Especificaciones a la Derecha -->
  <g transform="translate(680, 60)">
    <rect x="0" y="0" width="480" height="640" fill="#152132" stroke="#475569" stroke-width="2" rx="6" />
    <text x="20" y="35" fill="#f8fafc" font-size="14" font-weight="bold">CUADRO DE CÁMARAS Y CRITERIOS DORI</text>
    <line x1="15" y1="50" x2="465" y2="50" stroke="#64748b" stroke-width="1.5" />

    <text x="20" y="75" fill="#94a3b8" font-size="11" font-weight="bold">CÁMARA</text>
    <text x="140" y="75" fill="#94a3b8" font-size="11" font-weight="bold">LENTE / FOV</text>
    <text x="260" y="75" fill="#94a3b8" font-size="11" font-weight="bold">RESOLUCIÓN</text>
    <text x="370" y="75" fill="#94a3b8" font-size="11" font-weight="bold">DETECCIÓN IA</text>
    <line x1="15" y1="85" x2="465" y2="85" stroke="#334155" stroke-width="1" />

    <text x="20" y="115" fill="#38bdf8" font-size="11" font-weight="bold">CAM-01 Entrada</text>
    <text x="140" y="115" fill="#cbd5e1" font-size="11">2.8 mm / 108°</text>
    <text x="260" y="115" fill="#cbd5e1" font-size="11">4K (8 MP)</text>
    <text x="370" y="115" fill="#4ade80" font-size="11">Persona / Paquete</text>

    <text x="20" y="155" fill="#facc15" font-size="11" font-weight="bold">CAM-02 Cochera</text>
    <text x="140" y="155" fill="#cbd5e1" font-size="11">4.0 mm / 89°</text>
    <text x="260" y="155" fill="#cbd5e1" font-size="11">4K (8 MP)</text>
    <text x="370" y="155" fill="#4ade80" font-size="11">Vehículo / Placa</text>

    <text x="20" y="195" fill="#4ade80" font-size="11" font-weight="bold">CAM-03 Patio</text>
    <text x="140" y="195" fill="#cbd5e1" font-size="11">2.8 mm / 108°</text>
    <text x="260" y="195" fill="#cbd5e1" font-size="11">2K (4 MP)</text>
    <text x="370" y="195" fill="#4ade80" font-size="11">Persona / Mascota</text>

    <text x="20" y="235" fill="#c084fc" font-size="11" font-weight="bold">CAM-04 Trasera</text>
    <text x="140" y="235" fill="#cbd5e1" font-size="11">2.8 mm / 108°</text>
    <text x="260" y="235" fill="#cbd5e1" font-size="11">2K (4 MP)</text>
    <text x="370" y="235" fill="#4ade80" font-size="11">Intrusión Perimetral</text>

    <line x1="15" y1="270" x2="465" y2="270" stroke="#64748b" stroke-width="1.5" />

    <text x="20" y="300" fill="#facc15" font-size="12" font-weight="bold">PARÁMETROS FRIGATE NVR Y CORAL TPU:</text>
    <text x="20" y="330" fill="#cbd5e1" font-size="10">• Motor de Inferencia: Google Coral Edge TPU vía PCIe (Inferencia &lt; 8 ms).</text>
    <text x="20" y="355" fill="#cbd5e1" font-size="10">• Flujo de Detección: Substream H.264 640x360@5fps procesado en memoria RAM.</text>
    <text x="20" y="380" fill="#cbd5e1" font-size="10">• Grabación Eventos: Mainstream 4K/2K H.265 guardado a disco TrueNAS vía NFS.</text>
    <text x="20" y="405" fill="#cbd5e1" font-size="10">• Retransmisión WebRTC: Servidor go2rtc integrado para visualización inmediata.</text>
    <text x="20" y="430" fill="#cbd5e1" font-size="10">• Red Segregada: Cámaras aisladas en VLAN 40 CCTV (Sin acceso a Internet).</text>
    <text x="20" y="455" fill="#cbd5e1" font-size="10">• Máscaras de Movimiento: Calles públicas enmascaradas para 0 falsos positivos.</text>
    <text x="20" y="480" fill="#cbd5e1" font-size="10">• Criterios DORI (EN 62676-4): Identificar a 3.8m, Reconocer a 7.6m, Detectar a 38m.</text>
    <text x="20" y="505" fill="#cbd5e1" font-size="10">• Almacenamiento: 7 días continuo en baja + 30 días clips de personas en alta.</text>
    <text x="20" y="535" fill="#38bdf8" font-size="11" font-weight="bold">Zero-Trust: Detección 100% local sin nube de terceros</text>
  </g>
</svg>"""

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"SVG CCTV guardado en: {svg_path}")

if __name__ == "__main__":
    dxf_out = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/01_videovigilancia_poe_frigate/mecanico/plano_cobertura_cctv_poe.dxf"
    svg_out = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/01_videovigilancia_poe_frigate/mecanico/plano_cobertura_cctv_poe.svg"
    generar_plano_cctv(dxf_out, svg_out)

