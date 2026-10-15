#!/usr/bin/env python3
"""
Generador del Esquema Hidráulico del Colector de Riego Inteligente Multizona
Formatos de salida: DXF y SVG vectorial
Proyecto: open-source-domotics
"""

import os
from generar_planos_dxf import SimpleDXF

def generar_esquema_riego(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_ROTULO", color=7)
    dxf.add_layer("TUBERIA_PRINCIPAL", color=5)
    dxf.add_layer("ELECTROVALVULAS", color=1)
    dxf.add_layer("LINEAS_ZONAS", color=3)
    dxf.add_layer("SENSORES_MEDICION", color=4)
    dxf.add_layer("TEXTO_NOTAS", color=7)

    # Marco y Cajetín A3
    dxf.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf.add_rect(230, 10, 180, 40, layer="MARCO_ROTULO")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", 235, 38, height=4.0, layer="TEXTO_NOTAS")
    dxf.add_text("ESQUEMA HIDRÁULICO - RIEGO AUTOMATIZADO MULTIZONA", 235, 28, height=2.2, layer="TEXTO_NOTAS")
    dxf.add_text("Colector 4 Zonas + Válvula Maestra 24VAC + Caudalímetro + Cisterna Pluvial", 235, 18, height=1.6, layer="TEXTO_NOTAS")

    # Alimentación de Agua desde Cisterna Pluvial / Bomba Presurizadora
    dxf.add_rect(15, 170, 40, 80, layer="TUBERIA_PRINCIPAL")
    dxf.add_text("ALIMENTACIÓN", 18, 235, height=2.0, layer="TEXTO_NOTAS")
    dxf.add_text("Desde Cisterna", 18, 225, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Pluvial / Bomba", 18, 215, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Tubo PE 32 mm", 18, 195, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("Presión: 3.0 bar", 18, 180, height=1.5, layer="TEXTO_NOTAS")

    # Línea principal hacia Filtro
    dxf.add_line(55, 210, 80, 210, layer="TUBERIA_PRINCIPAL")

    # Filtro de Anillas 120 Mesh con Manómetro
    dxf.add_rect(80, 190, 30, 40, layer="TUBERIA_PRINCIPAL")
    dxf.add_text("FILTRO", 85, 220, height=1.8, layer="TEXTO_NOTAS")
    dxf.add_text("Anillas 120#", 82, 208, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("130 micras", 83, 198, height=1.3, layer="TEXTO_NOTAS")

    dxf.add_line(110, 210, 130, 210, layer="TUBERIA_PRINCIPAL")

    # Caudalímetro de Pulsos (1 pulso / litro)
    dxf.add_rect(130, 192, 30, 36, layer="SENSORES_MEDICION")
    dxf.add_text("CAUDALÍMETRO", 132, 220, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("Turbina Hall", 133, 210, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("1 pulso / litro", 132, 200, height=1.3, layer="TEXTO_NOTAS")

    dxf.add_line(160, 210, 180, 210, layer="TUBERIA_PRINCIPAL")

    # Válvula Maestra de Seguridad (Master Valve 24VAC)
    dxf.add_rect(180, 192, 35, 36, layer="ELECTROVALVULAS")
    dxf.add_text("VÁLVULA MAESTRA", 182, 220, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("24V AC Solenoide", 183, 210, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("Normalm. Cerrada", 182, 200, height=1.2, layer="TEXTO_NOTAS")

    dxf.add_line(215, 210, 240, 210, layer="TUBERIA_PRINCIPAL")

    # Colector Manifold de 4 Salidas (Manifold 1" BSP)
    dxf.add_line(240, 260, 240, 110, layer="TUBERIA_PRINCIPAL")
    dxf.add_text("COLECTOR DISTRIBUIDOR 1\" BSP", 220, 270, height=1.8, layer="TEXTO_NOTAS")

    zonas = [
        ("ZONA 1: SETOS Y PERÍMETRO", 250, "Goteo Autocompensante 2.3 L/h", "PE 16mm / Longitud 45m"),
        ("ZONA 2: CÉSPED Y PRADERA", 200, "4x Difusores emergentes 90°-180°", "Caudal total: 18 L/min (2.5 bar)"),
        ("ZONA 3: HUERTO / VEGETALES", 150, "Microdifusión / Goteo integrado", "Sonda Humedad Suelo CH3"),
        ("ZONA 4: MACETAS Y TERRAZA", 100, "Microtubo 4mm con goteros pincho", "Sonda Humedad Suelo CH4"),
    ]

    for nombre, y_pos, desc1, desc2 in zonas:
        # Tubería desde colector hacia electroválvula
        dxf.add_line(240, y_pos, 260, y_pos, layer="TUBERIA_PRINCIPAL")
        
        # Electroválvula de Zona (1" 24VAC con control de caudal manual)
        dxf.add_rect(260, y_pos - 12, 35, 24, layer="ELECTROVALVULAS")
        dxf.add_text("EV 24VAC", 265, y_pos + 4, height=1.5, layer="TEXTO_NOTAS")
        dxf.add_text("1\" Solenoide", 263, y_pos - 4, height=1.3, layer="TEXTO_NOTAS")

        # Tubería hacia sector de riego
        dxf.add_line(295, y_pos, 320, y_pos, layer="LINEAS_ZONAS")
        
        # Bloque de Zona y emisores
        dxf.add_rect(320, y_pos - 16, 90, 32, layer="LINEAS_ZONAS")
        dxf.add_text(nombre, 323, y_pos + 6, height=1.5, layer="TEXTO_NOTAS")
        dxf.add_text(desc1, 323, y_pos - 2, height=1.3, layer="TEXTO_NOTAS")
        dxf.add_text(desc2, 323, y_pos - 9, height=1.2, layer="TEXTO_NOTAS")

    # Esquema de Controladores y Sondas de Humedad en Suelo
    dxf.add_rect(15, 60, 210, 95, layer="SENSORES_MEDICION")
    dxf.add_text("CONTROLADOR ELECTRÓNICO ESP32 RIEGO (VLAN 30 IoT)", 20, 145, height=2.0, layer="TEXTO_NOTAS")
    dxf.add_text("• 5x Triacs BT136-600E con optoacopladores MOC3041 (Zero-Cross)", 20, 133, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("• 4x Sondas capacitivas de humedad de suelo anticorrosión (v2.0)", 20, 123, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("• Algoritmo de Evapotranspiración (Hargreaves / Open-Meteo)", 20, 113, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("• Bloqueo automático si previsión de lluvia > 60% en 12 horas", 20, 103, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("• Interbloqueo por nivel bajo en cisterna pluvial (< 15%)", 20, 93, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("• Detección de fugas: Caudal detectado con todas las EV cerradas", 20, 83, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("• Alimentación: Transformador de aislamiento 230V -> 24V AC 50VA", 20, 73, height=1.4, layer="TEXTO_NOTAS")

    dxf.save()
    print(f"DXF guardado en: {dxf_path}")

    # 2. GENERACIÓN SVG
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 850" width="100%" height="100%" style="background-color: #0b131e; font-family: monospace, sans-serif;">
  <defs>
    <filter id="glow_water" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect x="20" y="20" width="1160" height="810" fill="none" stroke="#1e293b" stroke-width="2" rx="8" />

  <!-- Cajetin -->
  <rect x="680" y="730" width="480" height="80" fill="#152132" stroke="#0284c7" stroke-width="2" rx="4" />
  <text x="700" y="755" fill="#38bdf8" font-size="16" font-weight="bold">OPEN-SOURCE-DOMOTICS</text>
  <text x="700" y="775" fill="#f8fafc" font-size="13" font-weight="bold">ESQUEMA HIDRÁULICO - RIEGO AUTOMATIZADO MULTIZONA</text>
  <text x="700" y="795" fill="#94a3b8" font-size="11">Colector 4 Zonas + Válvula Maestra 24VAC + Caudalímetro + Cisterna Pluvial</text>

  <!-- Alimentacion Cisterna Pluvial -->
  <g transform="translate(50, 180)">
    <rect x="0" y="0" width="130" height="220" fill="#1e293b" stroke="#0284c7" stroke-width="2" rx="6" />
    <text x="15" y="30" fill="#38bdf8" font-size="13" font-weight="bold">SUMINISTRO AGUA</text>
    <text x="15" y="55" fill="#f8fafc" font-size="12">Cisterna Pluvial</text>
    <text x="15" y="75" fill="#94a3b8" font-size="11">10.000 L / Bomba</text>
    <text x="15" y="110" fill="#cbd5e1" font-size="11">Presión: 3.0 bar</text>
    <text x="15" y="130" fill="#cbd5e1" font-size="11">Tubería PE 32 mm</text>
    <text x="15" y="160" fill="#22c55e" font-size="11">Válvula Bypass</text>
    <text x="15" y="180" fill="#94a3b8" font-size="10">a Red de Agua</text>
  </g>

  <!-- Tuberia Principal -->
  <path d="M 180 290 L 250 290" stroke="#0ea5e9" stroke-width="8" fill="none" />

  <!-- Filtro de Anillas 120 Mesh -->
  <g transform="translate(250, 220)">
    <rect x="0" y="0" width="100" height="140" fill="#1e293b" stroke="#eab308" stroke-width="2" rx="6" />
    <text x="12" y="30" fill="#facc15" font-size="12" font-weight="bold">FILTRO ANILLAS</text>
    <text x="12" y="55" fill="#f8fafc" font-size="12">120 Mesh</text>
    <text x="12" y="75" fill="#94a3b8" font-size="11">130 micras</text>
    <text x="12" y="105" fill="#cbd5e1" font-size="10">Manómetro 0-6 bar</text>
    <text x="12" y="125" fill="#22c55e" font-size="10">Purga manual</text>
  </g>

  <path d="M 350 290 L 410 290" stroke="#0ea5e9" stroke-width="8" fill="none" />

  <!-- Caudimetro de Pulsos -->
  <g transform="translate(410, 220)">
    <rect x="0" y="0" width="110" height="140" fill="#1e293b" stroke="#8b5cf6" stroke-width="2" rx="6" />
    <text x="10" y="30" fill="#c084fc" font-size="12" font-weight="bold">CAUDALÍMETRO</text>
    <text x="10" y="55" fill="#f8fafc" font-size="12">Efecto Hall</text>
    <text x="10" y="75" fill="#94a3b8" font-size="11">1 pulso / Litro</text>
    <text x="10" y="105" fill="#cbd5e1" font-size="10">Rango: 2-50 L/min</text>
    <text x="10" y="125" fill="#38bdf8" font-size="10">Detección fugas</text>
  </g>

  <path d="M 520 290 L 580 290" stroke="#0ea5e9" stroke-width="8" fill="none" />

  <!-- Valvula Maestra de Seguridad (Master Valve) -->
  <g transform="translate(580, 220)">
    <rect x="0" y="0" width="120" height="140" fill="#1e293b" stroke="#f43f5e" stroke-width="2" rx="6" />
    <text x="12" y="30" fill="#fb7185" font-size="12" font-weight="bold">VÁLVULA MAESTRA</text>
    <text x="12" y="55" fill="#f8fafc" font-size="12">Solenoide 24V AC</text>
    <text x="12" y="75" fill="#94a3b8" font-size="11">1" BSP (NC)</text>
    <text x="12" y="105" fill="#cbd5e1" font-size="10">Apertura única</text>
    <text x="12" y="125" fill="#ef4444" font-size="10">Corte preventivo</text>
  </g>

  <!-- Tuberia al Colector Manifold -->
  <path d="M 700 290 L 760 290" stroke="#0ea5e9" stroke-width="8" fill="none" />

  <!-- Colector Manifold Vertical -->
  <path d="M 760 120 L 760 560" stroke="#0284c7" stroke-width="12" stroke-linecap="round" fill="none" />
  <text x="740" y="100" fill="#38bdf8" font-size="13" font-weight="bold">COLECTOR MANIFOLD 1"</text>

  <!-- 4 Salidas a Zonas de Riego -->
  <!-- Zona 1: Setos (Y=140) -->
  <path d="M 760 140 L 820 140" stroke="#0ea5e9" stroke-width="6" fill="none" />
  <g transform="translate(820, 105)">
    <rect x="0" y="0" width="75" height="70" fill="#1e293b" stroke="#10b981" stroke-width="1.5" rx="4" />
    <text x="8" y="25" fill="#34d399" font-size="11" font-weight="bold">EV ZONA 1</text>
    <text x="8" y="45" fill="#f8fafc" font-size="10">24V AC 1"</text>
    <text x="8" y="60" fill="#94a3b8" font-size="9">Caudal Reg.</text>
  </g>
  <path d="M 895 140 L 930 140" stroke="#10b981" stroke-width="4" fill="none" />
  <g transform="translate(930, 105)">
    <rect x="0" y="0" width="220" height="70" fill="#0f172a" stroke="#10b981" stroke-width="1.5" rx="4" />
    <text x="12" y="25" fill="#f8fafc" font-size="12" font-weight="bold">ZONA 1: SETOS PERIMETRALES</text>
    <text x="12" y="45" fill="#94a3b8" font-size="10">Goteo autocompensante 2.3 L/h (PE 16mm)</text>
    <text x="12" y="60" fill="#38bdf8" font-size="10">Sonda Humedad Suelo 1 (Raíces 30cm)</text>
  </g>

  <!-- Zona 2: Cesped (Y=280) -->
  <path d="M 760 280 L 820 280" stroke="#0ea5e9" stroke-width="6" fill="none" />
  <g transform="translate(820, 245)">
    <rect x="0" y="0" width="75" height="70" fill="#1e293b" stroke="#10b981" stroke-width="1.5" rx="4" />
    <text x="8" y="25" fill="#34d399" font-size="11" font-weight="bold">EV ZONA 2</text>
    <text x="8" y="45" fill="#f8fafc" font-size="10">24V AC 1"</text>
    <text x="8" y="60" fill="#94a3b8" font-size="9">Caudal Reg.</text>
  </g>
  <path d="M 895 280 L 930 280" stroke="#10b981" stroke-width="4" fill="none" />
  <g transform="translate(930, 245)">
    <rect x="0" y="0" width="220" height="70" fill="#0f172a" stroke="#10b981" stroke-width="1.5" rx="4" />
    <text x="12" y="25" fill="#f8fafc" font-size="12" font-weight="bold">ZONA 2: CÉSPED Y PRADERA</text>
    <text x="12" y="45" fill="#94a3b8" font-size="10">4x Aspersores emergentes (18 L/min total)</text>
    <text x="12" y="60" fill="#38bdf8" font-size="10">Sonda Humedad Suelo 2 (Superficie 10cm)</text>
  </g>

  <!-- Zona 3: Huerto (Y=420) -->
  <path d="M 760 420 L 820 420" stroke="#0ea5e9" stroke-width="6" fill="none" />
  <g transform="translate(820, 385)">
    <rect x="0" y="0" width="75" height="70" fill="#1e293b" stroke="#10b981" stroke-width="1.5" rx="4" />
    <text x="8" y="25" fill="#34d399" font-size="11" font-weight="bold">EV ZONA 3</text>
    <text x="8" y="45" fill="#f8fafc" font-size="10">24V AC 1"</text>
    <text x="8" y="60" fill="#94a3b8" font-size="9">Caudal Reg.</text>
  </g>
  <path d="M 895 420 L 930 420" stroke="#10b981" stroke-width="4" fill="none" />
  <g transform="translate(930, 385)">
    <rect x="0" y="0" width="220" height="70" fill="#0f172a" stroke="#10b981" stroke-width="1.5" rx="4" />
    <text x="12" y="25" fill="#f8fafc" font-size="12" font-weight="bold">ZONA 3: HUERTO Y BANCALES</text>
    <text x="12" y="45" fill="#94a3b8" font-size="10">Microaspersión / Nebulización en bancales</text>
    <text x="12" y="60" fill="#38bdf8" font-size="10">Sonda Humedad Suelo 3 (Sustrato 15cm)</text>
  </g>

  <!-- Zona 4: Macetas Terraza (Y=540) -->
  <path d="M 760 540 L 820 540" stroke="#0ea5e9" stroke-width="6" fill="none" />
  <g transform="translate(820, 505)">
    <rect x="0" y="0" width="75" height="70" fill="#1e293b" stroke="#10b981" stroke-width="1.5" rx="4" />
    <text x="8" y="25" fill="#34d399" font-size="11" font-weight="bold">EV ZONA 4</text>
    <text x="8" y="45" fill="#f8fafc" font-size="10">24V AC 1"</text>
    <text x="8" y="60" fill="#94a3b8" font-size="9">Caudal Reg.</text>
  </g>
  <path d="M 895 540 L 930 540" stroke="#10b981" stroke-width="4" fill="none" />
  <g transform="translate(930, 505)">
    <rect x="0" y="0" width="220" height="70" fill="#0f172a" stroke="#10b981" stroke-width="1.5" rx="4" />
    <text x="12" y="25" fill="#f8fafc" font-size="12" font-weight="bold">ZONA 4: MACETAS Y PATIO</text>
    <text x="12" y="45" fill="#94a3b8" font-size="10">Microtubo 4mm con goteros regulables</text>
    <text x="12" y="60" fill="#38bdf8" font-size="10">Sonda Humedad Suelo 4 (Jardinera central)</text>
  </g>

  <!-- Cuadro Inferior: Logica del Controlador ESP32 -->
  <g transform="translate(50, 480)">
    <rect x="0" y="0" width="650" height="230" fill="#152132" stroke="#10b981" stroke-width="2" rx="6" />
    <text x="25" y="35" fill="#34d399" font-size="15" font-weight="bold">CONTROLADOR INTELIGENTE ESP32 (VLAN 30 IoT - Cero Nube)</text>
    
    <text x="25" y="70" fill="#cbd5e1" font-size="11">• 5x Triacs BT136 con optotriacs MOC3041 (Conmutación en cruce por cero sin chispas ni ruidos)</text>
    <text x="25" y="95" fill="#cbd5e1" font-size="11">• 4x Sondas capacitivas analógicas protegidas contra corrosión galvánica (0-100% calibradas)</text>
    <text x="25" y="120" fill="#cbd5e1" font-size="11">• Integración de radar meteorológico Open-Meteo: Omite riego si probabilidad de lluvia &gt; 60%</text>
    <text x="25" y="145" fill="#cbd5e1" font-size="11">• Interbloqueo cisterna pluvial: Desactiva riego si nivel desciende por debajo del 15%</text>
    <text x="25" y="170" fill="#cbd5e1" font-size="11">• Algoritmo Watchdog anti-fugas: Si el caudalímetro lee flujo con válvulas OFF -&gt; Corte y Alerta HA</text>
    <text x="25" y="195" fill="#38bdf8" font-size="11">• Aislamiento galvánico: Transformador 230V a 24V AC 50VA independiente con fusible 2A</text>
  </g>
</svg>"""

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"SVG guardado en: {svg_path}")

if __name__ == "__main__":
    dxf_out = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/03_riego_automatizado_jardin/mecanico/esquema_hidraulico_riego.dxf"
    svg_out = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/03_riego_automatizado_jardin/mecanico/esquema_hidraulico_riego.svg"
    generar_esquema_riego(dxf_out, svg_out)
