#!/usr/bin/env python3
"""
Generador de Topología de Red y Arquitectura VLANs (IEC / TIA-568)
Formatos de salida: DXF CAD 2D y SVG Vectorial Interactivo
Proyecto: open-source-domotics
"""

import os
from generar_planos_dxf import SimpleDXF

def generar_topologia_red(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_ROTULO", color=7)
    dxf.add_layer("WAN_INTERNET", color=1)       # Rojo
    dxf.add_layer("VLAN10_GESTION", color=3)      # Verde
    dxf.add_layer("VLAN20_IT_CONFIABLE", color=4) # Cian
    dxf.add_layer("VLAN30_DOMOTICA_IOT", color=2) # Amarillo
    dxf.add_layer("VLAN40_CCTV_SEGURIDAD", color=6) # Magenta
    dxf.add_layer("VLAN50_INVITADOS", color=5)   # Azul
    dxf.add_layer("HARDWARE_NODOS", color=7)
    dxf.add_layer("TEXTO_ROTULOS", color=7)

    # Marco A3 (420 x 297 mm)
    dxf.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf.add_rect(240, 10, 170, 40, layer="MARCO_ROTULO")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", 245, 38, height=4.0, layer="TEXTO_ROTULOS")
    dxf.add_text("TOPOLOGÍA DE RED Y SEGREGACIÓN DE VLANS (802.1Q)", 245, 28, height=2.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Firewall OPNsense | Switch PoE+ | Proxmox VE | Frigate NVR", 245, 18, height=2.0, layer="TEXTO_ROTULOS")

    # WAN Inputs (Fibra FTTH + Starlink/4G Backup)
    dxf.add_rect(20, 240, 70, 25, layer="WAN_INTERNET")
    dxf.add_text("ONT FIBRA (1 Gbps)", 25, 254, height=2.4, layer="TEXTO_ROTULOS")
    dxf.add_text("WAN 1 - PPPoE / DHCP", 25, 246, height=1.8, layer="TEXTO_ROTULOS")

    dxf.add_rect(100, 240, 70, 25, layer="WAN_INTERNET")
    dxf.add_text("BACKUP 4G / STARLINK", 103, 254, height=2.4, layer="TEXTO_ROTULOS")
    dxf.add_text("WAN 2 - Failover Gateway", 103, 246, height=1.8, layer="TEXTO_ROTULOS")

    # Líneas WAN hacia Router
    dxf.add_line(55, 240, 55, 215, layer="WAN_INTERNET")
    dxf.add_line(135, 240, 135, 215, layer="WAN_INTERNET")
    dxf.add_line(55, 215, 95, 215, layer="WAN_INTERNET")
    dxf.add_line(135, 215, 95, 215, layer="WAN_INTERNET")
    dxf.add_line(95, 215, 95, 195, layer="WAN_INTERNET")

    # ROUTER FIREWALL OPNSENSE 4x 2.5GbE
    dxf.add_rect(40, 155, 110, 40, layer="HARDWARE_NODOS")
    dxf.add_text("ROUTER FIREWALL APPLIANCE (OPNsense)", 45, 184, height=2.8, layer="TEXTO_ROTULOS")
    dxf.add_text("CPU 4C/8T 16GB RAM | 4x 2.5GbE Intel i226-V", 45, 175, height=2.0, layer="TEXTO_ROTULOS")
    dxf.add_text("Enrutamiento Inter-VLAN | WireGuard VPN | Suricata IDS", 45, 166, height=1.8, layer="TEXTO_ROTULOS")
    dxf.add_text("Gateway Principal: 192.168.X.1", 45, 159, height=1.8, layer="TEXTO_ROTULOS")

    # Troncal Trunk 802.1Q (LACP 2x 2.5G)
    dxf.add_line(95, 155, 95, 125, layer="HARDWARE_NODOS")
    dxf.add_text("TRUNK 802.1Q (VLAN 10,20,30,40,50) - LACP 5 Gbps", 100, 138, height=2.0, layer="TEXTO_ROTULOS")

    # CORE SWITCH POE+ MANAGED 24 PUERTOS
    dxf.add_rect(20, 85, 380, 40, layer="HARDWARE_NODOS")
    dxf.add_text("SWITCH CORE MANAGED 24-PORT POE+ (IEEE 802.3at/bt 370W)", 30, 114, height=3.2, layer="TEXTO_ROTULOS")
    dxf.add_text("VLAN Tagging por Puerto | IGMP Snooping v3 | Aislamiento de Puertos CCTV | QoS Voz/Vídeo", 30, 103, height=2.0, layer="TEXTO_ROTULOS")
    dxf.add_text("Capacidad de Conmutación: 128 Gbps | Puertos 1-16 PoE+ (30W) | 17-24 GbE No-PoE | 2x SFP+ 10G", 30, 93, height=1.8, layer="TEXTO_ROTULOS")

    # Distribución a las 5 VLANs
    vlans_dxf = [
        {"id": "VLAN 10", "name": "GESTIÓN IT", "ip": "192.168.10.0/24", "x": 30, "color": "VLAN10_GESTION", "equipos": ["Proxmox GUI (:8006)", "Switch Core Admin", "Router Admin (:443)", "UPS NMC SNMP"]},
        {"id": "VLAN 20", "name": "IT Y USUARIOS", "ip": "192.168.20.0/24", "x": 105, "color": "VLAN20_IT_CONFIABLE", "equipos": ["TrueNAS ZFS SMB", "PCs / Laptops", "Home Assistant Core", "Servidor Domótico"]},
        {"id": "VLAN 30", "name": "DOMÓTICA IOT", "ip": "192.168.30.0/24", "x": 180, "color": "VLAN30_DOMOTICA_IOT", "equipos": ["ESP32 Telemetría", "Shelly Pro Relés", "Zigbee2MQTT Coord", "Sin Acceso WAN"]},
        {"id": "VLAN 40", "name": "CCTV SEGURIDAD", "ip": "192.168.40.0/24", "x": 255, "color": "VLAN40_CCTV_SEGURIDAD", "equipos": ["Videoportero SIP", "Cámaras Frigate PoE", "Intercomunicadores", "go2rtc WebRTC"]},
        {"id": "VLAN 50", "name": "INVITADOS (GUEST)", "ip": "192.168.50.0/24", "x": 330, "color": "VLAN50_INVITADOS", "equipos": ["WiFi Clientes Visitas", "Aislamiento Total", "Solo Salida Web", "QoS Limitado 50M"]},
    ]

    for v in vlans_dxf:
        x = v["x"]
        dxf.add_line(x + 30, 85, x + 30, 70, layer=v["color"])
        dxf.add_rect(x, 20, 65, 50, layer=v["color"])
        dxf.add_text(v["id"], x + 5, 62, height=2.4, layer="TEXTO_ROTULOS")
        dxf.add_text(v["name"], x + 5, 55, height=2.0, layer="TEXTO_ROTULOS")
        dxf.add_text(v["ip"], x + 5, 48, height=1.6, layer="TEXTO_ROTULOS")
        y_eq = 40
        for eq in v["equipos"]:
            dxf.add_text(f"- {eq}", x + 5, y_eq, height=1.4, layer="TEXTO_ROTULOS")
            y_eq -= 5.5

    dxf.save()

    # 2. GENERACIÓN SVG VECTORIAL
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" width="100%" height="100%" style="background:#11111b; font-family: 'Segoe UI', system-ui, sans-serif;">
  <defs>
    <style>
      .title {{ fill: #cdd6f4; font-size: 22px; font-weight: bold; }}
      .sub {{ fill: #a6adc8; font-size: 13px; }}
      .lbl {{ fill: #cdd6f4; font-size: 11px; }}
      .lbl-bold {{ fill: #ffffff; font-size: 12px; font-weight: bold; }}
      .lbl-sm {{ fill: #bac2de; font-size: 9.5px; }}
      .wire-wan {{ stroke: #f38ba8; stroke-width: 3; stroke-dasharray: 6 3; fill: none; }}
      .wire-trunk {{ stroke: #cdd6f4; stroke-width: 5; fill: none; }}
      .vlan-card {{ stroke-width: 2; rx: 8; }}
      .node-box {{ fill: #1e1e2e; stroke: #585b70; stroke-width: 2; rx: 6; }}
    </style>
  </defs>

  <!-- Marco -->
  <rect x="15" y="15" width="1170" height="870" fill="none" stroke="#313244" stroke-width="2" rx="10"/>

  <!-- Encabezado -->
  <rect x="40" y="30" width="1120" height="70" fill="#181825" stroke="#45475a" stroke-width="1.5" rx="8"/>
  <text x="60" y="60" class="title">OPEN-SOURCE-DOMOTICS | TOPOLOGÍA DE RED Y SEGREGACIÓN DE VLANS (IEEE 802.1Q)</text>
  <text x="60" y="84" class="sub">Arquitectura Zero-Trust con OPNsense, Switch PoE+, Proxmox VE, Frigate NVR, TrueNAS y Home Assistant</text>

  <!-- Nodos WAN -->
  <rect x="180" y="130" width="220" height="60" class="node-box" stroke="#f38ba8"/>
  <text x="200" y="155" class="lbl-bold" style="fill:#f38ba8;">WAN 1: Fibra Óptica FTTH</text>
  <text x="200" y="175" class="lbl-sm">ONT GPON 1000/1000 Mbps (DHCP)</text>

  <rect x="450" y="130" width="220" height="60" class="node-box" stroke="#fab387"/>
  <text x="470" y="155" class="lbl-bold" style="fill:#fab387;">WAN 2: Starlink / 4G Respaldo</text>
  <text x="470" y="175" class="lbl-sm">Multi-WAN Failover Automático</text>

  <!-- Enlaces a Firewall -->
  <line x1="290" y1="190" x2="290" y2="230" class="wire-wan"/>
  <line x1="560" y1="190" x2="560" y2="230" class="wire-wan"/>
  <line x1="290" y1="230" x2="425" y2="230" class="wire-wan"/>
  <line x1="560" y1="230" x2="425" y2="230" class="wire-wan"/>
  <line x1="425" y1="230" x2="425" y2="260" class="wire-wan"/>

  <!-- ROUTER FIREWALL OPNSENSE -->
  <rect x="250" y="260" width="350" height="90" class="node-box" stroke="#89b4fa" stroke-width="2.5"/>
  <text x="270" y="290" class="lbl-bold" style="fill:#89b4fa; font-size:15px;">FIREWALL APPLIANCE: OPNsense 24.x</text>
  <text x="270" y="310" class="lbl-sm">Intel N100 4-Core / 16GB RAM / 4x 2.5GbE Intel i226-V</text>
  <text x="270" y="328" class="lbl-sm">• Enrutamiento Inter-VLAN • WireGuard VPN • DNS Unbound con DoT</text>
  <text x="270" y="343" class="lbl-sm">• Reglas estrictas: Domótica y CCTV sin salida a Internet (Solo NTP local)</text>

  <!-- Troncal al Switch -->
  <line x1="425" y1="350" x2="425" y2="400" class="wire-trunk"/>
  <rect x="300" y="365" width="250" height="22" fill="#11111b" stroke="#cdd6f4" rx="4"/>
  <text x="315" y="380" class="lbl-bold" style="fill:#cdd6f4; font-size:10px;">LACP BOND 2x 2.5GbE (Trunk 802.1Q)</text>

  <!-- SWITCH CORE POE+ -->
  <rect x="40" y="400" width="1120" height="85" class="node-box" stroke="#a6e3a1" stroke-width="2.5"/>
  <text x="70" y="430" class="lbl-bold" style="fill:#a6e3a1; font-size:16px;">SWITCH GESTIONABLE CORE POE+ 24 PUERTOS GIGABIT + 2x 10G SFP+</text>
  <text x="70" y="450" class="lbl">Presupuesto PoE: 370W (IEEE 802.3af/at) | IGMP Snooping v3 para Multicast de Vídeo CCTV | Port Isolation</text>
  <text x="70" y="470" class="lbl-sm">Puertos 1-8: CCTV PoE (VLAN 40) | 9-14: APs WiFi + Domótica (VLAN 30) | 15-20: Servidores LACP (VLAN 10/20) | 21-24: Puestos IT</text>

  <!-- LÍNEAS DE DERIVACIÓN A CADA VLAN -->
  <!-- VLAN 10 -->
  <line x1="150" y1="485" x2="150" y2="530" stroke="#a6e3a1" stroke-width="3"/>
  <rect x="45" y="530" width="210" height="320" fill="#181825" stroke="#a6e3a1" class="vlan-card"/>
  <text x="60" y="560" class="lbl-bold" style="fill:#a6e3a1; font-size:14px;">VLAN 10: GESTIÓN</text>
  <text x="60" y="580" class="lbl-sm" style="fill:#a6e3a1; font-weight:bold;">Subred: 192.168.10.0/24</text>
  <text x="60" y="605" class="lbl">• OPNsense WebGUI (192.168.10.1)</text>
  <text x="60" y="625" class="lbl">• Switch Core Admin (192.168.10.2)</text>
  <text x="60" y="645" class="lbl">• PDU Inteligente (192.168.10.5)</text>
  <text x="60" y="665" class="lbl">• Proxmox VE Host (192.168.10.10)</text>
  <text x="60" y="685" class="lbl">• Tarjeta Red UPS NMC (192.168.10.15)</text>
  <text x="60" y="715" class="lbl-sm" style="fill:#a6adc8;">Aislamiento total. Solo accesible desde IPs de administradores con llave SSH o VPN.</text>

  <!-- VLAN 20 -->
  <line x1="380" y1="485" x2="380" y2="530" stroke="#89b4fa" stroke-width="3"/>
  <rect x="275" y="530" width="210" height="320" fill="#181825" stroke="#89b4fa" class="vlan-card"/>
  <text x="290" y="560" class="lbl-bold" style="fill:#89b4fa; font-size:14px;">VLAN 20: IT &amp; CONFIABLE</text>
  <text x="290" y="580" class="lbl-sm" style="fill:#89b4fa; font-weight:bold;">Subred: 192.168.20.0/24</text>
  <text x="290" y="605" class="lbl">• Home Assistant Core (.20.10)</text>
  <text x="290" y="625" class="lbl">• TrueNAS ZFS SMB/NFS (.20.20)</text>
  <text x="290" y="645" class="lbl">• Frigate NVR Web App (.20.30)</text>
  <text x="290" y="665" class="lbl">• PCs / Workstations Oficina</text>
  <text x="290" y="685" class="lbl">• Laptops y Celulares Personales</text>
  <text x="290" y="715" class="lbl-sm" style="fill:#a6adc8;">Acceso completo bidireccional hacia domótica mediante reglas seguras de Firewall.</text>

  <!-- VLAN 30 -->
  <line x1="610" y1="485" x2="610" y2="530" stroke="#f9e2af" stroke-width="3"/>
  <rect x="505" y="530" width="210" height="320" fill="#181825" stroke="#f9e2af" class="vlan-card"/>
  <text x="520" y="560" class="lbl-bold" style="fill:#f9e2af; font-size:14px;">VLAN 30: DOMÓTICA IOT</text>
  <text x="520" y="580" class="lbl-sm" style="fill:#f9e2af; font-weight:bold;">Subred: 192.168.30.0/24</text>
  <text x="520" y="605" class="lbl">• ESP32 Telemetría Energía (.30.45)</text>
  <text x="520" y="625" class="lbl">• Shelly Pro Carril DIN (.30.50+)</text>
  <text x="520" y="645" class="lbl">• Zigbee2MQTT PoE Coordinator</text>
  <text x="520" y="665" class="lbl">• Actuadores Válvulas Agua/Gas</text>
  <text x="520" y="685" class="lbl">• Climatización e Inversores</text>
  <text x="520" y="715" class="lbl-sm" style="fill:#f38ba8; font-weight:bold;">BLOQUEO WAN TOTAL.</text>
  <text x="520" y="730" class="lbl-sm" style="fill:#a6adc8;">Solo habla MQTT localmente con el Broker en Proxmox. Sin nube ni telemetría externa.</text>

  <!-- VLAN 40 -->
  <line x1="840" y1="485" x2="840" y2="530" stroke="#f38ba8" stroke-width="3"/>
  <rect x="735" y="530" width="210" height="320" fill="#181825" stroke="#f38ba8" class="vlan-card"/>
  <text x="750" y="560" class="lbl-bold" style="fill:#f38ba8; font-size:14px;">VLAN 40: CCTV Y FÍSICA</text>
  <text x="750" y="580" class="lbl-sm" style="fill:#f38ba8; font-weight:bold;">Subred: 192.168.40.0/24</text>
  <text x="750" y="605" class="lbl">• Videoportero Entrada SIP (.40.5)</text>
  <text x="750" y="625" class="lbl">• Cámaras PoE Frigate (.40.11-18)</text>
  <text x="750" y="645" class="lbl">• Intercomunicador Bebé 940nm</text>
  <text x="750" y="665" class="lbl">• Pantallas de Pared WebRTC</text>
  <text x="750" y="685" class="lbl">• Cerraduras Biométricas PoE</text>
  <text x="750" y="715" class="lbl-sm" style="fill:#f38ba8; font-weight:bold;">AISLAMIENTO DE PUERTOS.</text>
  <text x="750" y="730" class="lbl-sm" style="fill:#a6adc8;">Cámaras no pueden verse entre sí. Solo entregan flujo RTSP a Frigate/go2rtc.</text>

  <!-- VLAN 50 -->
  <line x1="1070" y1="485" x2="1070" y2="530" stroke="#b4befe" stroke-width="3"/>
  <rect x="965" y="530" width="195" height="320" fill="#181825" stroke="#b4befe" class="vlan-card"/>
  <text x="980" y="560" class="lbl-bold" style="fill:#b4befe; font-size:14px;">VLAN 50: INVITADOS</text>
  <text x="980" y="580" class="lbl-sm" style="fill:#b4befe; font-weight:bold;">Subred: 192.168.50.0/24</text>
  <text x="980" y="605" class="lbl">• WiFi SSID "Domotics-Guest"</text>
  <text x="980" y="625" class="lbl">• Client Isolation activado</text>
  <text x="980" y="645" class="lbl">• DNS con filtrado AdGuard</text>
  <text x="980" y="665" class="lbl">• Sin acceso a LANs internas</text>
  <text x="980" y="685" class="lbl">• Limitador de Ancho de Banda</text>
  <text x="980" y="715" class="lbl-sm" style="fill:#a6adc8;">Tráfico confinado exclusivamente a navegación web hacia el exterior.</text>

</svg>
"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Topología de Red generada: DXF={dxf_path}, SVG={svg_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dxf_out = os.path.join(base_dir, "02_infraestructura_it_y_red/02_red_vlans_y_comunicaciones/electrico/topologia_red_vlans.dxf")
    svg_out = os.path.join(base_dir, "02_infraestructura_it_y_red/02_red_vlans_y_comunicaciones/electrico/topologia_red_vlans.svg")
    generar_topologia_red(dxf_out, svg_out)

