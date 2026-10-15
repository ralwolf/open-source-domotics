#!/usr/bin/env python3
"""
Generador de Alzado y Distribución Mecánica de Rack IT de 19" (15U / EIA-310-D)
Formatos de salida: DXF (AutoCAD/LibreCAD) y SVG Vectorial
Proyecto: open-source-domotics
"""

import os
from generar_planos_dxf import SimpleDXF

def generar_rack_19u(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF (Escala 1:1 en milímetros)
    # Estándar EIA-310: Ancho 19" (482.6 mm), 1U = 1.75" (44.45 mm)
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_RACK", color=7)
    dxf.add_layer("GUIAS_19_PULGADAS", color=3)
    dxf.add_layer("EQUIPOS_RED", color=4)
    dxf.add_layer("SERVIDORES_COMPUTO", color=1)
    dxf.add_layer("ALMACENAMIENTO_ZFS", color=6)
    dxf.add_layer("ENERGIA_UPS_PDU", color=2)
    dxf.add_layer("TEXTO_COTAS", color=7)

    u_height = 44.45
    rack_width = 482.6
    total_u = 15
    rack_total_height = total_u * u_height

    # Gabinete exterior (600 mm ancho x 800 mm alto exterior)
    ext_w = 600.0
    ext_h = rack_total_height + 120.0
    dxf.add_rect(0, 0, ext_w, ext_h, layer="MARCO_RACK")
    dxf.add_rect(15, 15, ext_w - 30, ext_h - 30, layer="MARCO_RACK")

    # Postes de fijación EIA-310 (separación 465 mm entre centros)
    x_rack = (ext_w - rack_width) / 2 # 58.7 mm
    y_rack_base = 60.0

    # Guías verticales izquierda y derecha
    dxf.add_rect(x_rack - 15, y_rack_base, 15, rack_total_height, layer="GUIAS_19_PULGADAS")
    dxf.add_rect(x_rack + rack_width, y_rack_base, 15, rack_total_height, layer="GUIAS_19_PULGADAS")

    # Unidades de Rack (15U de abajo hacia arriba)
    rack_units = [
        {"u_start": 1, "u_size": 2, "name": "UPS ONLINE DOBLE CONVERSIÓN 2000VA (2U)", "layer": "ENERGIA_UPS_PDU"},
        {"u_start": 3, "u_size": 1, "name": "PDU GESTIONABLE 8 TOMAS IEC CON MONITOR (.10.5) (1U)", "layer": "ENERGIA_UPS_PDU"},
        {"u_start": 4, "u_size": 2, "name": "TRUENAS ZFS STORAGE 8x 3.5\" HOT-SWAP (2U)", "layer": "ALMACENAMIENTO_ZFS"},
        {"u_start": 6, "u_size": 2, "name": "SERVIDOR PROXMOX VE 12C/24T 64GB ECC (HA + FRIGATE) (2U)", "layer": "SERVIDORES_COMPUTO"},
        {"u_start": 8, "u_size": 1, "name": "BANDEJA CON VENTILACIÓN TÉRMICA (1U)", "layer": "MARCO_RACK"},
        {"u_start": 9, "u_size": 1, "name": "ROUTER FIREWALL OPNSENSE 4x 2.5GbE (1U)", "layer": "EQUIPOS_RED"},
        {"u_start": 10, "u_size": 1, "name": "SWITCH CORE 24-PORT POE+ GESTIONABLE (1U)", "layer": "EQUIPOS_RED"},
        {"u_start": 11, "u_size": 1, "name": "PASACABLES CON CEPILLO ANTIPOLVO (1U)", "layer": "MARCO_RACK"},
        {"u_start": 12, "u_size": 1, "name": "PATCH PANEL CAT6A BLINDADO 24 PUERTOS (1U)", "layer": "EQUIPOS_RED"},
        {"u_start": 13, "u_size": 1, "name": "COORDINADOR ZIGBEE PoE + GATEWAY MODBUS (1U)", "layer": "EQUIPOS_RED"},
        {"u_start": 14, "u_size": 2, "name": "UNIDAD DE VENTILACIÓN SUPERIOR TERMOSTATIZADA (2U)", "layer": "MARCO_RACK"},
    ]

    for item in rack_units:
        y_bot = y_rack_base + (item["u_start"] - 1) * u_height
        h = item["u_size"] * u_height
        dxf.add_rect(x_rack, y_bot, rack_width, h, layer=item["layer"])
        # Tornillos de oreja en postes
        for u in range(item["u_size"]):
            yu = y_bot + u * u_height
            dxf.add_circle(x_rack - 7.5, yu + 6.35, 2.5, layer="GUIAS_19_PULGADAS")
            dxf.add_circle(x_rack - 7.5, yu + 38.1, 2.5, layer="GUIAS_19_PULGADAS")
            dxf.add_circle(x_rack + rack_width + 7.5, yu + 6.35, 2.5, layer="GUIAS_19_PULGADAS")
            dxf.add_circle(x_rack + rack_width + 7.5, yu + 38.1, 2.5, layer="GUIAS_19_PULGADAS")
            # Marcador de U
            u_num = item["u_start"] + u
            dxf.add_text(f"U{u_num}", x_rack - 35, yu + 15, height=10.0, layer="TEXTO_COTAS")

        # Texto del equipo centrado
        dxf.add_text(item["name"], x_rack + 20, y_bot + h/2 - 4.0, height=8.0, layer="TEXTO_COTAS")

    # Cuadro de rotulación
    dxf.add_rect(ext_w + 30, 60, 220, 200, layer="MARCO_RACK")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", ext_w + 40, 230, height=12.0, layer="TEXTO_COTAS")
    dxf.add_text("ALZADO FRONTAL RACK 19\" (15U)", ext_w + 40, 205, height=9.0, layer="TEXTO_COTAS")
    dxf.add_text("Norma: EIA-310-D / IEC 60297", ext_w + 40, 180, height=7.0, layer="TEXTO_COTAS")
    dxf.add_text("Ubicación: Sala Técnica IT Central", ext_w + 40, 160, height=6.0, layer="TEXTO_COTAS")
    dxf.add_text("Profundidad: 800 mm", ext_w + 40, 140, height=6.0, layer="TEXTO_COTAS")
    dxf.add_text("Respaldo: UPS Online + NUT Server", ext_w + 40, 120, height=6.0, layer="TEXTO_COTAS")

    dxf.save()

    # 2. GENERACIÓN SVG
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 950" width="100%" height="100%" style="background:#11111b; font-family:sans-serif;">
  <defs>
    <style>
      .rack-frame {{ fill: #181825; stroke: #45475a; stroke-width: 3; rx: 8; }}
      .rack-rail {{ fill: #313244; stroke: #585b70; stroke-width: 1.5; }}
      .dev-net {{ fill: #1e1e2e; stroke: #89b4fa; stroke-width: 2; rx: 4; }}
      .dev-srv {{ fill: #1e1e2e; stroke: #f38ba8; stroke-width: 2; rx: 4; }}
      .dev-nas {{ fill: #1e1e2e; stroke: #cba6f7; stroke-width: 2; rx: 4; }}
      .dev-pwr {{ fill: #1e1e2e; stroke: #fab387; stroke-width: 2; rx: 4; }}
      .dev-fan {{ fill: #1e1e2e; stroke: #a6e3a1; stroke-width: 2; rx: 4; }}
      .u-text {{ fill: #6c7086; font-size: 11px; font-weight: bold; }}
      .dev-text {{ fill: #cdd6f4; font-size: 12px; font-weight: bold; }}
      .dev-sub {{ fill: #a6adc8; font-size: 9.5px; }}
      .led-green {{ fill: #a6e3a1; }}
      .led-blue {{ fill: #89b4fa; }}
      .led-amber {{ fill: #fab387; }}
    </style>
  </defs>

  <!-- Título -->
  <text x="50" y="45" style="fill:#cdd6f4; font-size:22px; font-weight:bold;">SALA TÉCNICA IT | ALZADO Y DISTRIBUCIÓN EN RACK DE 19" (15U)</text>
  <text x="50" y="70" style="fill:#89b4fa; font-size:13px;">EIA-310-D / IEC 60297 | Cableado Estructurado Cat6A | Alimentación Redundante UPS Online</text>

  <!-- Marco Exterior Gabinete 19" -->
  <rect x="50" y="100" width="560" height="800" class="rack-frame"/>
  <rect x="70" y="120" width="520" height="760" fill="#11111b" stroke="#313244"/>

  <!-- Guías EIA-310 -->
  <rect x="90" y="130" width="25" height="740" class="rack-rail"/>
  <rect x="545" y="130" width="25" height="740" class="rack-rail"/>

  <!-- Unidades (15U, de U15 arriba a U1 abajo) -->
  <!-- U14-15: Ventilación -->
  <rect x="118" y="140" width="424" height="85" class="dev-fan"/>
  <text x="140" y="175" class="dev-text" style="fill:#a6e3a1;">UNIDAD EXTRACTORA DUAL TERMOSTATIZADA (2U)</text>
  <text x="140" y="195" class="dev-sub">2x Ventiladores 120mm PWM silenciosos con sonda NTC de temperatura</text>

  <!-- U13: Coordinador Domótico -->
  <rect x="118" y="230" width="424" height="40" class="dev-net"/>
  <text x="140" y="255" class="dev-text">COORDINADOR ZIGBEE 3.0 PoE + GATEWAY MODBUS RTU/TCP (1U)</text>

  <!-- U12: Patch Panel -->
  <rect x="118" y="275" width="424" height="40" class="dev-net"/>
  <text x="140" y="300" class="dev-text">PATCH PANEL 24 PUERTOS CAT6A BLINDADO FTP/STP (1U)</text>

  <!-- U11: Cepillo Pasacables -->
  <rect x="118" y="320" width="424" height="40" fill="#181825" stroke="#45475a" rx="4"/>
  <text x="140" y="345" class="dev-sub" style="fill:#6c7086;">PASACABLES CON CEPILLO ANTIPOLVO Y GESTOR TRASERO DE PARCHES (1U)</text>

  <!-- U10: Switch Core PoE+ -->
  <rect x="118" y="365" width="424" height="40" class="dev-net" stroke-width="2.5"/>
  <text x="140" y="390" class="dev-text" style="fill:#89b4fa;">SWITCH GESTIONABLE CORE 24P POE+ (370W) + 2x SFP+ 10G (1U)</text>

  <!-- U9: Router OPNsense -->
  <rect x="118" y="410" width="424" height="40" class="dev-net" stroke-width="2.5"/>
  <text x="140" y="435" class="dev-text" style="fill:#89b4fa;">ROUTER FIREWALL APPLIANCE OPNSENSE 4x 2.5GbE INTEL i226-V (1U)</text>

  <!-- U8: Bandeja de Ventilación -->
  <rect x="118" y="455" width="424" height="40" fill="#181825" stroke="#45475a" rx="4"/>
  <text x="140" y="480" class="dev-sub" style="fill:#6c7086;">BANDEJA PASANTE VENTILADA DE SEPARACIÓN TÉRMICA (1U)</text>

  <!-- U6-7: Servidor Proxmox VE -->
  <rect x="118" y="500" width="424" height="85" class="dev-srv" stroke-width="2.5"/>
  <text x="140" y="535" class="dev-text" style="fill:#f38ba8;">SERVIDOR PROXMOX VE 2U (CEREBRO COMPUTACIONAL)</text>
  <text x="140" y="555" class="dev-sub">AMD Ryzen 9 / 64GB ECC RAM / 2x 1TB NVMe ZFS Mirror</text>
  <text x="140" y="572" class="dev-sub">• VM Home Assistant OS • LXC Frigate (Coral Edge TPU) • LXC Mosquitto</text>

  <!-- U4-5: Servidor TrueNAS Storage -->
  <rect x="118" y="590" width="424" height="85" class="dev-nas" stroke-width="2.5"/>
  <text x="140" y="625" class="dev-text" style="fill:#cba6f7;">SERVIDOR ALMACENAMIENTO TRUENAS SCALE 2U</text>
  <text x="140" y="645" class="dev-sub">8x Bahías 3.5" Hot-Swap SAS/SATA en RAID-Z2 (ZFS Pool Seguro)</text>
  <text x="140" y="662" class="dev-sub">Grabaciones Frigate NVR, Backups automáticos de Proxmox y Nextcloud</text>

  <!-- U3: PDU Gestionable -->
  <rect x="118" y="680" width="424" height="40" class="dev-pwr"/>
  <text x="140" y="705" class="dev-text" style="fill:#fab387;">PDU GESTIONABLE 8 TOMAS IEC C13 CON MEDICIÓN INDIVIDUAL (1U)</text>

  <!-- U1-2: UPS Online Doble Conversión -->
  <rect x="118" y="725" width="424" height="85" class="dev-pwr" stroke-width="2.5"/>
  <text x="140" y="760" class="dev-text" style="fill:#fab387;">UPS ONLINE DE DOBLE CONVERSIÓN 2000VA / 1800W (2U)</text>
  <text x="140" y="780" class="dev-sub">0 ms tiempo de transferencia | Baterías internas 48V | Tarjeta de Red SNMP</text>
  <text x="140" y="798" class="dev-sub">Protocolo NUT Server: Apagado limpio y ordenado ante fallas prolongadas</text>

  <!-- Panel de Información Lateral -->
  <rect x="640" y="100" width="320" height="420" fill="#181825" stroke="#45475a" rx="8"/>
  <text x="660" y="135" style="fill:#cdd6f4; font-size:16px; font-weight:bold;">PARÁMETROS DEL RACK</text>
  <text x="660" y="165" class="dev-sub" style="font-size:11px;">• Altura Útil: 15U (667 mm)</text>
  <text x="660" y="185" class="dev-sub" style="font-size:11px;">• Ancho Estándar: 19 pulgadas (482.6 mm)</text>
  <text x="660" y="205" class="dev-sub" style="font-size:11px;">• Profundidad: 800 mm (Cables de alimentación y parcheo)</text>
  <text x="660" y="225" class="dev-sub" style="font-size:11px;">• Consumo Medio Estimado: 280 W continuo</text>
  <text x="660" y="245" class="dev-sub" style="font-size:11px;">• Autonomía UPS 2000VA: ~55 minutos al 20% de carga</text>
  <text x="660" y="265" class="dev-sub" style="font-size:11px;">• Climatización: Desacoplado con entrada de aire inferior</text>
  <text x="660" y="295" style="fill:#a6e3a1; font-size:14px; font-weight:bold;">INTEGRACIÓN CON HOME ASSISTANT</text>
  <text x="660" y="325" class="dev-sub" style="font-size:10.5px;">1. Telemetría de UPS vía NUT (Voltaje, Batería %, Carga W)</text>
  <text x="660" y="345" class="dev-sub" style="font-size:10.5px;">2. Estado de puertos PoE del Switch vía SNMP</text>
  <text x="660" y="365" class="dev-sub" style="font-size:10.5px;">3. Monitorización de discos TrueNAS (Smart status y Zpool)</text>
  <text x="660" y="385" class="dev-sub" style="font-size:10.5px;">4. Alerta de intrusión por tamper en puerta de rack</text>
</svg>
"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Alzado de Rack 19U generado: DXF={dxf_path}, SVG={svg_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dxf_target = os.path.join(base_dir, "02_infraestructura_it_y_red/01_rack_servidores_y_ups/mecanico/elevacion_rack_19u.dxf")
    svg_target = os.path.join(base_dir, "02_infraestructura_it_y_red/01_rack_servidores_y_ups/mecanico/elevacion_rack_19u.svg")
    generar_rack_19u(dxf_target, svg_target)

