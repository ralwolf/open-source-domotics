#!/usr/bin/env python3
"""
generar_plano_robotica.py
Genera los planos CAD 2D en DXF R12 y SVG vectorial de la integración de la estación base
de robótica de limpieza (aspirado y trapeado con Valetudo) y mapa de navegación LiDAR.
"""

import os

class SimpleDXF:
    def __init__(self, filename):
        self.filename = filename
        self.entities = []

    def add_line(self, x1, y1, x2, y2, layer="0", color=7):
        self.entities.append(f"0\nLINE\n8\n{layer}\n62\n{color}\n10\n{x1:.3f}\n20\n{y1:.3f}\n30\n0.0\n11\n{x2:.3f}\n21\n{y2:.3f}\n31\n0.0")

    def add_circle(self, cx, cy, radius, layer="0", color=7):
        self.entities.append(f"0\nCIRCLE\n8\n{layer}\n62\n{color}\n10\n{cx:.3f}\n20\n{cy:.3f}\n30\n0.0\n40\n{radius:.3f}")

    def add_rect(self, x, y, w, h, layer="0", color=7):
        self.add_line(x, y, x + w, y, layer, color)
        self.add_line(x + w, y, x + w, y + h, layer, color)
        self.add_line(x + w, y + h, x, y + h, layer, color)
        self.add_line(x, y + h, x, y, layer, color)

    def add_text(self, text, x, y, height=150, layer="0", color=7):
        self.entities.append(f"0\nTEXT\n8\n{layer}\n62\n{color}\n10\n{x:.3f}\n20\n{y:.3f}\n30\n0.0\n40\n{height:.3f}\n1\n{text}")

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write("0\nSECTION\n2\nHEADER\n0\nENDSEC\n")
            f.write("0\nSECTION\n2\nENTITIES\n")
            for e in self.entities:
                f.write(e + "\n")
            f.write("0\nENDSEC\n0\nEOF\n")
        print(f"Plano DXF generado: {self.filename}")

def generar_svg_robotica(svg_path):
    svg_content = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 850" width="100%" height="100%" style="background-color: #0d1117; font-family: 'DejaVu Sans', Helvetica, Arial, sans-serif;">
  <defs>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#21262d" stroke-width="1"/>
    </pattern>
  </defs>

  <rect width="1100" height="850" fill="url(#grid)" />

  <!-- Carátula -->
  <rect x="50" y="30" width="1000" height="60" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="70" y="65" fill="#f0f6fc" font-size="18" font-weight="bold">INTEGRACIÓN DE ROBÓTICA DE LIMPIEZA: ESTACIÓN BASE, TELEMETRÍA Y MAPA LIDAR</text>
  <text x="70" y="82" fill="#8b949e" font-size="12">Firmware 100% Libre Valetudo | MQTT Local | Vaciado Ciclónico y Lavado de Mopas | Zonas de Exclusión Virtuales</text>

  <!-- MAPA DE NAVEGACIÓN LIDAR Y ZONIFICACIÓN (IZQUIERDA) -->
  <rect x="60" y="120" width="500" height="580" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="80" y="150" fill="#58a6ff" font-size="14" font-weight="bold">MAPA DE NAVEGACIÓN Y TRAYECTORIAS LIDAR</text>

  <!-- Perímetro vivienda 10x10 m -->
  <rect x="90" y="180" width="440" height="440" fill="none" stroke="#8b949e" stroke-width="3"/>

  <!-- Estancias delimitadas -->
  <rect x="90" y="180" width="220" height="200" fill="none" stroke="#30363d" stroke-width="1.5"/>
  <text x="105" y="210" fill="#c9d1d9" font-size="11">Dormitorio Principal</text>

  <rect x="310" y="180" width="220" height="240" fill="none" stroke="#30363d" stroke-width="1.5"/>
  <text x="325" y="210" fill="#c9d1d9" font-size="11">Salón - Comedor</text>

  <rect x="350" y="420" width="180" height="200" fill="none" stroke="#30363d" stroke-width="1.5"/>
  <text x="365" y="450" fill="#c9d1d9" font-size="11">Cocina</text>

  <!-- Estación Base Ubicada en Cocina / Galería -->
  <rect x="470" y="550" width="50" height="45" fill="#1f6feb" stroke="#58a6ff" stroke-width="2" rx="4"/>
  <text x="475" y="575" fill="#ffffff" font-size="8" font-weight="bold">BASE DOCK</text>

  <!-- Robot Aspirador desacoplándose -->
  <circle cx="430" cy="570" r="16" fill="#238636" stroke="#2ea043" stroke-width="2"/>
  <circle cx="430" cy="570" r="5" fill="#d29922"/> <!-- Torreta LiDAR -->
  <text x="415" y="600" fill="#2ea043" font-size="9" font-weight="bold">ROBOT</text>

  <!-- Trayectoria de Limpieza LiDAR en S (Verde) -->
  <path d="M 430 570 L 400 500 L 400 250 L 350 250 L 350 380 L 450 380 L 450 220 L 500 220" fill="none" stroke="#2ea043" stroke-width="2" stroke-dasharray="4,3"/>

  <!-- Zona de Exclusión Virtual (No-Go Zone) en Rojo -->
  <rect x="150" y="260" width="90" height="70" fill="rgba(248, 81, 73, 0.2)" stroke="#f85149" stroke-width="2" stroke-dasharray="4,2"/>
  <text x="160" y="300" fill="#f85149" font-size="10" font-weight="bold">NO-GO ZONE</text>
  <text x="160" y="315" fill="#f85149" font-size="8">Alfombra / Cables</text>

  <!-- ESQUEMA DE TELEMETRÍA Y ARQUITECTURA VALETUDO (DERECHA) -->
  <rect x="580" y="120" width="470" height="580" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="600" y="150" fill="#58a6ff" font-size="14" font-weight="bold">ARQUITECTURA VALETUDO 100% LOCAL SIN NUBE</text>

  <!-- Bloque Robot con Firmware Valetudo -->
  <rect x="620" y="190" width="390" height="90" fill="#21262d" stroke="#2ea043" stroke-width="2" rx="6"/>
  <text x="640" y="220" fill="#2ea043" font-size="13" font-weight="bold">ROBOT CON FIRMWARE LIBRE VALETUDO</text>
  <text x="640" y="245" fill="#f0f6fc" font-size="11">■ Cero dependencia de servidores cloud chinos/externos</text>
  <text x="640" y="265" fill="#f0f6fc" font-size="11">■ Comunicación directa Wi-Fi VLAN 30 IoT hacia Mosquitto MQTT</text>

  <!-- Servidor Local Home Assistant -->
  <rect x="620" y="310" width="390" height="110" fill="#21262d" stroke="#58a6ff" stroke-width="2" rx="6"/>
  <text x="640" y="340" fill="#58a6ff" font-size="13" font-weight="bold">HOME ASSISTANT (INTEGRACIÓN VALETUDO)</text>
  <text x="640" y="365" fill="#f0f6fc" font-size="11">■ Tarjeta de mapa interactivo con selección de estancias</text>
  <text x="640" y="390" fill="#f0f6fc" font-size="11">■ Estado de consumibles: Filtro HEPA, cepillo central, cepillos laterales</text>

  <!-- Telemetría de la Estación Base (ESP32-C3 + BL0942) -->
  <rect x="620" y="445" width="390" height="130" fill="#21262d" stroke="#e3b341" stroke-width="2" rx="6"/>
  <text x="640" y="475" fill="#e3b341" font-size="13" font-weight="bold">MONITOREO DE LA ESTACIÓN BASE (ESP32-C3)</text>
  <text x="640" y="500" fill="#f0f6fc" font-size="11">■ Medición Potencia: Distingue carga (&lt;30W) vs secado térmico (500W)</text>
  <text x="640" y="525" fill="#f0f6fc" font-size="11">■ Sensor Nivel de Agua: Aviso cuando el depósito de agua limpia &lt; 20%</text>
  <text x="640" y="550" fill="#f0f6fc" font-size="11">■ Protección Térmica: Corte de relé si la temperatura de secado &gt; 65°C</text>

  <!-- Pie de plano -->
  <rect x="50" y="720" width="1000" height="100" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="70" y="745" fill="#f0f6fc" font-size="12" font-weight="bold">AUTOMATIZACIONES DE LIMPIEZA AUTÓNOMA:</text>
  <text x="70" y="765" fill="#2ea043" font-size="11">■ Limpieza por Ausencia Total: Al bloquearse las cerraduras biométricas exteriores y activarse la alarma perimetral en modo "Ausente", el robot arranca el ciclo de aspirado completo.</text>
  <text x="70" y="785" fill="#388bfd" font-size="11">■ Retorno Silencioso: Si cualquier miembro de la familia regresa a casa antes de finalizar, el robot cancela la tarea y regresa de inmediato al dock para no entorpecer.</text>
  <text x="70" y="805" fill="#e3b341" font-size="11">■ Secado Térmico de Mopas: Tras finalizar el trapeado, la base activa flujo de aire caliente a 45°C durante 2 horas para evitar malos olores y proliferación bacteriana.</text>
</svg>"""

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Plano SVG generado: {svg_path}")

def generar_plano_robotica_dxf(dxf_path):
    dxf = SimpleDXF(dxf_path)
    # Perímetro vivienda (10000 x 10000 mm)
    dxf.add_rect(0, 0, 10000, 10000, layer="PERIMETRO_CASA", color=7)

    # Estación base (450 x 400 mm)
    dxf.add_rect(7500, 1200, 450, 400, layer="ESTACION_DOCK", color=4) # Cyan
    dxf.add_text("ESTACION BASE ROBOT LIMPIEZA VALETUDO", 7000, 1700, height=100, layer="TEXTOS", color=4)

    # Robot en base (Ø350 mm)
    dxf.add_circle(7725, 1400, 175, layer="ROBOT_ASPIRADOR", color=3) # Verde
    dxf.add_circle(7725, 1400, 40, layer="LIDAR_TORRETA", color=1)

    # Zonas de exclusión virtual
    dxf.add_rect(2000, 3000, 1500, 1200, layer="ZONAS_EXCLUSION_NO_GO", color=1) # Rojo
    dxf.add_text("ZONA NO-GO VIRTUAL (CABLES/ALFOMBRA)", 2000, 4400, height=80, layer="TEXTOS", color=1)

    dxf.save()

if __name__ == "__main__":
    out_dir = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/02_robotica_limpieza/mecanico"
    os.makedirs(out_dir, exist_ok=True)
    dxf_file = os.path.join(out_dir, "plano_estacion_robotica_limpieza.dxf")
    svg_file = os.path.join(out_dir, "plano_estacion_robotica_limpieza.svg")

    generar_plano_robotica_dxf(dxf_file)
    generar_svg_robotica(svg_file)

