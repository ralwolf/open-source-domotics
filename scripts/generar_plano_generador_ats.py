#!/usr/bin/env python3
"""
generar_plano_generador_ats.py
Genera los planos CAD 2D en DXF R12 y SVG vectorial de la instalación del motogenerador
de respaldo terciario a gasolina, tablero de conmutación ATS y cargador de flotación.
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

def generar_svg_generador_ats(svg_path):
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
  <text x="70" y="65" fill="#f0f6fc" font-size="18" font-weight="bold">GENERADOR A GASOLINA DE RESPALDO TERCIARIO, TABLERO ATS Y LÓGICA DE ARRANQUE</text>
  <text x="70" y="82" fill="#8b949e" font-size="12">Grupo Electrógeno 6.5 kVA Insonorizado | Conmutación ATS Enclavada | Contacto Seco SoC &lt; 18% | Cargador Flotación 12V</text>

  <!-- PATIO TÉCNICO EXTERIOR (IZQUIERDA) -->
  <rect x="60" y="120" width="480" height="580" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="80" y="150" fill="#58a6ff" font-size="14" font-weight="bold">PATIO EXTERIOR VENTILADO - CABINA INSONORIZADA</text>

  <!-- Muro de Fachada / Aislamiento -->
  <rect x="480" y="180" width="40" height="500" fill="#21262d" stroke="#484f58" stroke-width="1.5"/>
  <text x="495" y="440" fill="#8b949e" font-size="12" font-weight="bold" transform="rotate(-90 495,440)">MURO EXTERIOR</text>

  <!-- Cabina Insonorizada 950 x 650 mm -->
  <rect x="110" y="240" width="320" height="240" fill="#21262d" stroke="#2ea043" stroke-width="3" rx="8"/>
  <text x="130" y="275" fill="#2ea043" font-size="14" font-weight="bold">CABINA GRUPO ELECTRÓGENO</text>
  <text x="130" y="295" fill="#8b949e" font-size="11">Motor 4T 389cc / 6.5 kVA / 230V 50Hz</text>

  <!-- Silenciador de Escape y Expulsión de Gases -->
  <circle cx="380" cy="200" r="25" fill="#da3633" stroke="#f85149" stroke-width="2"/>
  <path d="M 380 240 L 380 200" stroke="#f85149" stroke-width="6"/>
  <text x="320" y="170" fill="#f85149" font-size="11" font-weight="bold">ESCAPE GASES (Orientado al exterior)</text>

  <!-- Batería de Arranque 12V y Cargador de Flotación -->
  <rect x="130" y="340" width="70" height="50" fill="#161b22" stroke="#e3b341" stroke-width="2" rx="3"/>
  <text x="135" y="370" fill="#e3b341" font-size="10" font-weight="bold">BAT 12V</text>

  <!-- Tanque de Combustible 25L con Boya de Nivel -->
  <rect x="230" y="340" width="170" height="90" fill="#161b22" stroke="#58a6ff" stroke-width="2" rx="4"/>
  <text x="250" y="380" fill="#58a6ff" font-size="12" font-weight="bold">DEPÓSITO 25L</text>
  <text x="250" y="400" fill="#8b949e" font-size="10">Sensor Nivel Analógico</text>

  <!-- ESQUEMA ELÉCTRICO UNIFILAR ATS (DERECHA) -->
  <rect x="560" y="120" width="490" height="580" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="580" y="150" fill="#58a6ff" font-size="14" font-weight="bold">TABLERO ATS Y CONMUTACIÓN RED / INVERSOR / GRUPO</text>

  <!-- Fuente A: Inversor Solar ESS / Red (Prioridad 1) -->
  <rect x="580" y="200" width="190" height="55" fill="#21262d" stroke="#58a6ff" stroke-width="2" rx="4"/>
  <text x="595" y="225" fill="#58a6ff" font-size="12" font-weight="bold">FUENTE A: INVERSOR ESS</text>
  <text x="595" y="245" fill="#8b949e" font-size="10">Solar FV + Batería LiFePO4</text>

  <!-- Fuente B: Generador Respaldo (Prioridad 2) -->
  <rect x="820" y="200" width="200" height="55" fill="#21262d" stroke="#2ea043" stroke-width="2" rx="4"/>
  <text x="835" y="225" fill="#2ea043" font-size="12" font-weight="bold">FUENTE B: GENERADOR</text>
  <text x="835" y="245" fill="#8b949e" font-size="10">Respaldo Terciario 6.5 kVA</text>

  <!-- Mecanismo de Conmutación ATS con Enclavamiento Mecánico/Eléctrico -->
  <rect x="680" y="300" width="240" height="90" fill="#161b22" stroke="#d29922" stroke-width="3" rx="6"/>
  <text x="710" y="335" fill="#d29922" font-size="13" font-weight="bold">CONMUTADOR ATS 63A</text>
  <text x="700" y="355" fill="#f0f6fc" font-size="11">Enclavamiento Mecánico</text>
  <text x="700" y="375" fill="#8b949e" font-size="10">Imposible conexión simultánea</text>

  <!-- Salida hacia Cuadro General TGBT -->
  <path d="M 800 390 L 800 450" stroke="#f0f6fc" stroke-width="4"/>
  <rect x="710" y="450" width="180" height="45" fill="#21262d" stroke="#f0f6fc" stroke-width="2" rx="4"/>
  <text x="725" y="478" fill="#f0f6fc" font-size="12" font-weight="bold">TGBT (Cargas Esenciales)</text>

  <!-- Controlador ESP32-C3 ATS y Arranque por Contacto Seco -->
  <rect x="620" y="520" width="370" height="150" fill="#21262d" stroke="#58a6ff" stroke-width="2" rx="6"/>
  <text x="640" y="550" fill="#58a6ff" font-size="13" font-weight="bold">CONTROLADOR ATS Y ARRANQUE (ESP32-C3)</text>
  <text x="640" y="575" fill="#f0f6fc" font-size="11">■ Entrada Contacto Seco: Disparo por SoC &lt; 18% en LiFePO4</text>
  <text x="640" y="600" fill="#f0f6fc" font-size="11">■ Secuencia: 3 intentos de arranque (5s estárter, 10s reposo)</text>
  <text x="640" y="625" fill="#f0f6fc" font-size="11">■ Calentamiento: Conmutación ATS tras 45s de régimen nominal</text>
  <text x="640" y="650" fill="#8b949e" font-size="10">Test automático de lubricación mensual (10 min en vacío)</text>

  <!-- Pie de plano -->
  <rect x="50" y="720" width="1000" height="100" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="70" y="745" fill="#f0f6fc" font-size="12" font-weight="bold">PARÁMETROS OPERATIVOS DE RESPALDO Y PROTECCIÓN:</text>
  <text x="70" y="765" fill="#2ea043" font-size="11">■ Enclavamiento de Seguridad: El conmutador ATS dispone de bloqueo mecánico físico mediante barra basculante que impide el cruce entre la red/inversor y el generador.</text>
  <text x="70" y="785" fill="#e3b341" font-size="11">■ Mantenimiento de Batería de Arranque: Cargador por flotación permanente conectado a la barra esencial que mantiene la batería de 12V a 13.6V para arranque garantizado.</text>
  <text x="70" y="805" fill="#f85149" font-size="11">■ Sensor de Nivel y Parada Segura: Si el nivel de gasolina desciende del 10%, el sistema conmuta la carga y apaga el motor antes de descebar el circuito de carburación.</text>
</svg>"""

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Plano SVG generado: {svg_path}")

def generar_plano_generador_ats_dxf(dxf_path):
    dxf = SimpleDXF(dxf_path)
    # Patio exterior (4000 x 3000 mm)
    dxf.add_rect(0, 0, 4000, 3000, layer="PATIO_TECNICO", color=7)

    # Cabina generador (950 x 650 mm)
    dxf.add_rect(500, 500, 950, 650, layer="CABINA_GENERADOR", color=3) # Verde
    dxf.add_text("CABINA INSONORIZADA GENERADOR 6.5 kVA", 500, 1300, height=80, layer="TEXTOS", color=3)

    # Escape gases
    dxf.add_circle(1300, 400, 60, layer="ESCAPE_GASES", color=1) # Rojo
    dxf.add_text("ESCAPE CON SILENCIADOR Y PARALLAMAS", 1000, 250, height=60, layer="TEXTOS", color=1)

    # Tablero ATS en Sala IT (1000 x 400 mm)
    dxf.add_rect(2500, 1000, 1000, 400, layer="TABLERO_ATS", color=2) # Amarillo
    dxf.add_text("TABLERO CONMUTACION ATS 63A", 2500, 1500, height=80, layer="TEXTOS", color=2)

    # Línea de potencia (3x6 mm2)
    dxf.add_line(1450, 800, 2500, 1200, layer="CABLE_POTENCIA", color=5)

    dxf.save()

if __name__ == "__main__":
    out_dir = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/06_generador_gasolina_respaldo/mecanico"
    os.makedirs(out_dir, exist_ok=True)
    dxf_file = os.path.join(out_dir, "plano_generador_respaldo_ats.dxf")
    svg_file = os.path.join(out_dir, "plano_generador_respaldo_ats.svg")

    generar_plano_generador_ats_dxf(dxf_file)
    generar_svg_generador_ats(svg_file)

