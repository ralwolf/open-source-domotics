#!/usr/bin/env python3
"""
generar_plano_arquitectura_servidores.py
Genera el diagrama de arquitectura y topología de servicios 2D (.dxf y .svg)
para los servidores Proxmox VE, TrueNAS ZFS, Home Assistant, Frigate NVR y Mosquitto MQTT.
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
BASTIDOR_PROXMOX
10
0.0
20
0.0
30
0.0
11
800.0
21
0.0
31
0.0
0
LINE
8
BASTIDOR_PROXMOX
10
800.0
20
0.0
30
0.0
11
800.0
21
500.0
31
0.0
0
LINE
8
BASTIDOR_PROXMOX
10
800.0
20
500.0
30
0.0
11
0.0
21
500.0
31
0.0
0
LINE
8
BASTIDOR_PROXMOX
10
0.0
20
500.0
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
50.0
20
450.0
30
0.0
40
25.0
1
PROXMOX VE HYPERVISOR (BARE-METAL KVM)
0
TEXT
8
TEXTO
10
60.0
20
380.0
30
0.0
40
18.0
1
VM 100: HOME ASSISTANT SUPERVISED (OS NATIVO)
0
TEXT
8
TEXTO
10
60.0
20
320.0
30
0.0
40
18.0
1
LXC 101: FRIGATE NVR (PASSTHROUGH CORAL TPU PCIE)
0
TEXT
8
TEXTO
10
60.0
20
260.0
30
0.0
40
18.0
1
LXC 102: MOSQUITTO MQTT BROKER (TLS VLAN 30/10)
0
TEXT
8
TEXTO
10
60.0
20
200.0
30
0.0
40
18.0
1
LXC 103: GO2RTC WEBRTC STREAMING SERVER
0
TEXT
8
TEXTO
10
60.0
20
140.0
30
0.0
40
18.0
1
VM 200: TRUENAS SCALE ZFS (PASSTHROUGH HBA SAS)
0
TEXT
8
TEXTO
10
60.0
20
80.0
30
0.0
40
18.0
1
LXC 104: LOCAL WHISPER & PIPER TTS (VOZ PRIVADA)
0
ENDSEC
0
EOF
"""

SVG_CONTENT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 700" width="100%" height="100%">
  <rect width="1000" height="700" fill="#0b0f19"/>

  <!-- Encabezado -->
  <text x="500" y="45" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">ARQUITECTURA DE VIRTUALIZACIÓN Y SERVICIOS LOCALES ZERO-TRUST</text>
  <text x="500" y="70" fill="#94a3b8" font-family="sans-serif" font-size="13" text-anchor="middle">Proxmox VE + TrueNAS SCALE + Home Assistant Core + Frigate NVR Coral TPU</text>

  <!-- Chasis Bare Metal Proxmox VE -->
  <rect x="50" y="100" width="900" height="550" rx="10" fill="#1e293b" stroke="#e11d48" stroke-width="3"/>
  <rect x="50" y="100" width="900" height="45" rx="10" fill="#e11d48"/>
  <text x="70" y="130" fill="#ffffff" font-family="sans-serif" font-size="16" font-weight="bold">HYPERVISOR HOST: Proxmox VE 8.x (Linux Debian 12 Kernel ZFS)</text>

  <!-- Nodos Virtuales / Máquinas y Contenedores -->
  <!-- 1. Home Assistant VM -->
  <rect x="80" y="170" width="260" height="135" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="2"/>
  <text x="100" y="200" fill="#38bdf8" font-family="sans-serif" font-size="14" font-weight="bold">VM 100: Home Assistant</text>
  <text x="100" y="225" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Core + Supervisor (HAOS)</text>
  <text x="100" y="245" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Zigbee2MQTT (Sonoff P Dongle)</text>
  <text x="100" y="265" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Energy Dashboard &amp; InfluxDB</text>
  <text x="100" y="285" fill="#10b981" font-family="sans-serif" font-size="11">IP: 10.0.10.10 (VLAN 10)</text>

  <!-- 2. Frigate NVR LXC -->
  <rect x="370" y="170" width="260" height="135" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
  <text x="390" y="200" fill="#34d399" font-family="sans-serif" font-size="14" font-weight="bold">LXC 101: Frigate NVR</text>
  <text x="390" y="225" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Detección Objetos 100 fps</text>
  <text x="390" y="245" fill="#fbbf24" font-family="sans-serif" font-size="11">• Passthrough Coral Dual Edge TPU</text>
  <text x="390" y="265" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Ingesta RTSP 8 Cámaras PoE</text>
  <text x="390" y="285" fill="#10b981" font-family="sans-serif" font-size="11">IP: 10.0.40.10 (VLAN 40)</text>

  <!-- 3. Mosquitto MQTT & WebRTC -->
  <rect x="660" y="170" width="260" height="135" rx="6" fill="#0f172a" stroke="#8b5cf6" stroke-width="2"/>
  <text x="680" y="200" fill="#a78bfa" font-family="sans-serif" font-size="14" font-weight="bold">LXC 102: Broker &amp; Streaming</text>
  <text x="680" y="225" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Mosquitto MQTT (TLS 8883)</text>
  <text x="680" y="245" fill="#cbd5e1" font-family="sans-serif" font-size="11">• go2rtc Servidor WebRTC ultrabajo lat</text>
  <text x="680" y="265" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Autenticación ACL estricta</text>
  <text x="680" y="285" fill="#10b981" font-family="sans-serif" font-size="11">IP: 10.0.10.15 (VLAN 10)</text>

  <!-- 4. TrueNAS SCALE ZFS Storage -->
  <rect x="80" y="330" width="410" height="140" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
  <text x="100" y="360" fill="#fbbf24" font-family="sans-serif" font-size="14" font-weight="bold">VM 200: TrueNAS SCALE (Almacenamiento ZFS)</text>
  <text x="100" y="385" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Pool ZFS RAID-Z2 con 4x Discos Enterprise (Passthrough HBA SAS IT-Mode)</text>
  <text x="100" y="405" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Grabación continua NVR CCTV (Dataset con compresión LZ4)</text>
  <text x="100" y="425" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Snapshots automáticos inmutables horarias / diarias (Anti-Ransomware)</text>
  <text x="100" y="445" fill="#10b981" font-family="sans-serif" font-size="11">IP: 10.0.10.20 (VLAN 10)</text>

  <!-- 5. Asistente Local de Voz Privado (Whisper + Piper) -->
  <rect x="510" y="330" width="410" height="140" rx="6" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
  <text x="530" y="360" fill="#f472b6" font-family="sans-serif" font-size="14" font-weight="bold">LXC 104: Inteligencia y Voz Local (Privacidad 100%)</text>
  <text x="530" y="385" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Faster-Whisper STT (Transcripción de voz en GPU/CPU en &lt;200ms)</text>
  <text x="530" y="405" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Piper TTS (Sintetizador neuronal en español neutro de alta fidelidad)</text>
  <text x="530" y="425" fill="#cbd5e1" font-family="sans-serif" font-size="11">• openWakeWord (Detección local precisa de palabra de activación)</text>
  <text x="530" y="445" fill="#10b981" font-family="sans-serif" font-size="11">IP: 10.0.10.30 (VLAN 10)</text>

  <!-- Barra de hardware subyacente y redundancia -->
  <rect x="80" y="500" width="840" height="120" rx="6" fill="#030712" stroke="#64748b" stroke-width="1.5"/>
  <text x="100" y="530" fill="#f8fafc" font-family="sans-serif" font-size="13" font-weight="bold">CAPA FÍSICA Y HARDWARE (CHASIS RACK 19" 1U CON DUAL PSU):</text>
  <text x="100" y="555" fill="#94a3b8" font-family="sans-serif" font-size="11">Procesador AMD Ryzen / EPYC Embedded | 64GB DDR4 ECC RAM | 2x M.2 NVMe ZFS Mirror (Boot/VMs) | Dual 10GbE SFP+ LACP</text>
  <text x="100" y="575" fill="#94a3b8" font-family="sans-serif" font-size="11">Doble fuente redundante 80+ Platinum conectada a circuitos independientes (Línea SAI 1 / Línea SAI 2)</text>
  <text x="100" y="595" fill="#38ef7d" font-family="sans-serif" font-size="11">Supervisión constante de salud SMART, temperatura de cores y apagado limpio coordinado vía demonio NUT</text>
</svg>
"""

def generar_planos_servidores():
    base_dir = "/home/ral/Documents/GitHub/open-source-domotics/02_infraestructura_it_y_red/03_servidores_proxmox_ha_frigate_truenas/control"
    dxf_path = os.path.join(base_dir, "arquitectura_servidores_servicios.dxf")
    svg_path = os.path.join(base_dir, "arquitectura_servidores_servicios.svg")

    with open(dxf_path, "w", encoding="utf-8") as f:
        f.write(DXF_CONTENT)
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(SVG_CONTENT)

    print(f"Plano DXF guardado en: {dxf_path}")
    print(f"Plano SVG guardado en: {svg_path}")

if __name__ == "__main__":
    generar_planos_servidores()

