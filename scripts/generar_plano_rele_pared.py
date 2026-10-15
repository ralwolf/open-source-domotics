#!/usr/bin/env python3
"""
generar_plano_rele_pared.py
Genera los planos CAD 2D en DXF R12 y SVG vectorial de la integración del micromódulo
de pared detrás del mecanismo convencional en caja de empotrar estándar de 65mm.
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

def generar_svg_rele_pared(svg_path):
    svg_content = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 800" width="100%" height="100%" style="background-color: #0d1117; font-family: 'DejaVu Sans', Helvetica, Arial, sans-serif;">
  <defs>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#21262d" stroke-width="1"/>
    </pattern>
  </defs>

  <rect width="1000" height="800" fill="url(#grid)" />

  <!-- Carátula -->
  <rect x="40" y="30" width="920" height="60" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="60" y="65" fill="#f0f6fc" font-size="18" font-weight="bold">DETALLE DE INTEGRACIÓN Y CABLEADO: MICROMÓDULO ZERO-CROSS EN CAJA UNIVERSAL</text>
  <text x="60" y="82" fill="#8b949e" font-size="12">Caja de empotrar Ø65 mm x 50 mm | Doble Relé 10A con Shunt BL0942 | Pulsadores de Pared Existentes S1/S2</text>

  <!-- SECCIÓN TRANSVERSAL MECÁNICA (IZQUIERDA) -->
  <rect x="60" y="120" width="400" height="520" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="80" y="150" fill="#58a6ff" font-size="14" font-weight="bold">SECCIÓN MECÁNICA EN CAJA Ø65 mm</text>

  <!-- Paramento / Muro de yeso o ladrillo -->
  <rect x="80" y="170" width="60" height="440" fill="#21262d" stroke="#484f58" stroke-width="1.5"/>
  <text x="90" y="380" fill="#8b949e" font-size="12" transform="rotate(-90 90,380)">MURO DE LADRILLO / YESO</text>

  <!-- Caja de mecanismos universal Ø65 x 50 mm empotrada -->
  <rect x="140" y="200" width="220" height="380" fill="#0d1117" stroke="#e3b341" stroke-width="3" rx="10"/>
  <text x="155" y="230" fill="#e3b341" font-size="11" font-weight="bold">CAJA EMPOTRAR Ø65 mm (Prof. 50 mm)</text>

  <!-- Fondo de caja: Micromódulo inteligente (42x38x17 mm) -->
  <rect x="155" y="260" width="110" height="280" fill="#1f6feb" stroke="#58a6ff" stroke-width="2" rx="6"/>
  <text x="175" y="390" fill="#ffffff" font-size="12" font-weight="bold" transform="rotate(-90 175,390)">MICROMÓDULO INTELIGENTE</text>
  <text x="200" y="405" fill="#f0f6fc" font-size="9" transform="rotate(-90 200,405)">42 x 38 x 17 mm | UL94-V0</text>

  <!-- Espacio libre para conductores de 2.5 mm² -->
  <rect x="275" y="260" width="30" height="280" fill="none" stroke="#8b949e" stroke-width="1" stroke-dasharray="4,4"/>
  <text x="282" y="410" fill="#8b949e" font-size="9" transform="rotate(-90 282,410)">PASO DE CABLES 2.5 mm²</text>

  <!-- Mecanismo de tecla / pulsador convencional frontal -->
  <rect x="315" y="230" width="40" height="320" fill="#30363d" stroke="#8b949e" stroke-width="2" rx="4"/>
  <text x="330" y="400" fill="#c9d1d9" font-size="10" font-weight="bold" transform="rotate(-90 330,400)">INTERRUPTOR DE PARED</text>

  <!-- Placa embellecedora exterior -->
  <rect x="355" y="190" width="15" height="400" fill="#f0f6fc" stroke="#8b949e" stroke-width="2" rx="2"/>
  <text x="380" y="390" fill="#f0f6fc" font-size="10">Marco Frontal Decorativo</text>

  <!-- ESQUEMA ELÉCTRICO DE CONEXIÓN UNIFILAR (DERECHA) -->
  <rect x="490" y="120" width="470" height="520" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="510" y="150" fill="#58a6ff" font-size="14" font-weight="bold">DIAGRAMA DE CONEXIÓN ELÉCTRICA ZERO-CROSS</text>

  <!-- Bloque Micromódulo Bornero -->
  <rect x="620" y="200" width="220" height="380" fill="#21262d" stroke="#58a6ff" stroke-width="2" rx="8"/>
  <text x="655" y="235" fill="#58a6ff" font-size="13" font-weight="bold">MICROMÓDULO DUAL</text>
  <text x="660" y="255" fill="#8b949e" font-size="10">Zero-Cross + Medidor Shunt</text>

  <!-- Bornas y Etiquetas -->
  <!-- Borna L -->
  <circle cx="620" cy="290" r="8" fill="#d29922"/>
  <text x="635" y="295" fill="#f0f6fc" font-size="11" font-weight="bold">L (Fase 230V)</text>
  <path d="M 520 290 L 620 290" stroke="#d29922" stroke-width="3"/>
  <text x="530" y="280" fill="#d29922" font-size="10">Fase Línea (C10)</text>

  <!-- Borna N -->
  <circle cx="620" cy="340" r="8" fill="#58a6ff"/>
  <text x="635" y="345" fill="#f0f6fc" font-size="11" font-weight="bold">N (Neutro)</text>
  <path d="M 520 340 L 620 340" stroke="#58a6ff" stroke-width="3"/>
  <text x="530" y="330" fill="#58a6ff" font-size="10">Neutro 230V</text>

  <!-- Borna S1 -->
  <circle cx="620" cy="400" r="8" fill="#bc8cff"/>
  <text x="635" y="405" fill="#f0f6fc" font-size="11" font-weight="bold">S1 (Pulsador 1)</text>
  <!-- Interruptor 1 externo -->
  <path d="M 570 400 L 620 400" stroke="#bc8cff" stroke-width="2.5"/>
  <line x1="570" y1="400" x2="540" y2="385" stroke="#bc8cff" stroke-width="2.5"/>
  <circle cx="570" cy="400" r="3" fill="#bc8cff"/>
  <circle cx="540" cy="400" r="3" fill="#bc8cff"/>
  <path d="M 540 400 L 520 400 L 520 290" stroke="#bc8cff" stroke-width="2.5"/>

  <!-- Borna S2 -->
  <circle cx="620" cy="450" r="8" fill="#bc8cff"/>
  <text x="635" y="455" fill="#f0f6fc" font-size="11" font-weight="bold">S2 (Pulsador 2)</text>
  <path d="M 570 450 L 620 450" stroke="#bc8cff" stroke-width="2.5"/>
  <line x1="570" y1="450" x2="540" y2="435" stroke="#bc8cff" stroke-width="2.5"/>
  <circle cx="570" cy="450" r="3" fill="#bc8cff"/>
  <circle cx="540" cy="450" r="3" fill="#bc8cff"/>
  <path d="M 540 450 L 520 450 L 520 290" stroke="#bc8cff" stroke-width="2.5"/>

  <!-- Salida L1 (Carga 1) -->
  <circle cx="840" cy="310" r="8" fill="#f85149"/>
  <text x="735" y="315" fill="#f0f6fc" font-size="11" font-weight="bold">L1_OUT</text>
  <path d="M 840 310 L 920 310" stroke="#f85149" stroke-width="3"/>
  <circle cx="920" cy="310" r="10" fill="none" stroke="#f85149" stroke-width="2"/>
  <text x="915" y="314" fill="#f85149" font-size="10">X1</text>
  <text x="860" y="300" fill="#f85149" font-size="9">Lámpara 1</text>

  <!-- Salida L2 (Carga 2) -->
  <circle cx="840" cy="370" r="8" fill="#f85149"/>
  <text x="735" y="375" fill="#f0f6fc" font-size="11" font-weight="bold">L2_OUT</text>
  <path d="M 840 370 L 920 370" stroke="#f85149" stroke-width="3"/>
  <circle cx="920" cy="370" r="10" fill="none" stroke="#f85149" stroke-width="2"/>
  <text x="915" y="374" fill="#f85149" font-size="10">X2</text>
  <text x="860" y="360" fill="#f85149" font-size="9">Lámpara 2</text>

  <!-- Retorno Neutro Cargas -->
  <path d="M 920 420 L 920 380" stroke="#58a6ff" stroke-width="2"/>
  <path d="M 920 420 L 520 420 L 520 340" stroke="#58a6ff" stroke-width="2"/>

  <!-- Bloque Zero-Cross interior destacado -->
  <rect x="645" y="490" width="170" height="70" fill="#161b22" stroke="#2ea043" stroke-width="1.5" rx="4"/>
  <text x="655" y="515" fill="#2ea043" font-size="10" font-weight="bold">VENTAJA TÉCNICA ZERO-CROSS:</text>
  <text x="655" y="530" fill="#8b949e" font-size="9">Conmutación en V = 0V</text>
  <text x="655" y="545" fill="#8b949e" font-size="9">Elimina corriente de irrupción (inrush)</text>
  <text x="655" y="558" fill="#8b949e" font-size="9">Multiplica x3 vida útil del relé</text>

  <!-- Pie de plano -->
  <rect x="40" y="660" width="920" height="90" fill="#161b22" stroke="#30363d" stroke-width="2" rx="6"/>
  <text x="60" y="685" fill="#f0f6fc" font-size="12" font-weight="bold">ESPECIFICACIONES DE MONTAJE Y SEGURIDAD:</text>
  <text x="60" y="705" fill="#c9d1d9" font-size="11">1. Compatible con cajas universales redondas y cuadradas de 65 mm con profundidad recomendada ≥ 50 mm.</text>
  <text x="60" y="722" fill="#c9d1d9" font-size="11">2. Entradas S1 y S2 admiten pulsadores normalmente abiertos (NO) o interruptores conmutados tradicionales.</text>
  <text x="60" y="739" fill="#c9d1d9" font-size="11">3. Soporta modo desacoplado (Decoupled Mode): el relé mantiene tensión constante para bombillas Zigbee/Matter mientras el pulsador envía eventos MQTT/HA.</text>
</svg>"""

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Plano SVG generado: {svg_path}")

def generar_plano_rele_dxf(dxf_path):
    dxf = SimpleDXF(dxf_path)
    # Caja de empotrar de 65x50 mm en milímetros
    dxf.add_rect(0, 0, 50, 65, layer="CAJA_EMPOTRAR", color=2) # Amarillo
    # Micromódulo (17x38 mm en sección transversal)
    dxf.add_rect(5, 13, 17, 38, layer="MICROMODULO", color=4) # Cyan
    dxf.add_text("MICROMODULO DUAL ZERO-CROSS", 7, 30, height=2, layer="TEXTOS", color=4)

    # Mecanismo interruptor frontal (15x50 mm)
    dxf.add_rect(30, 7, 15, 50, layer="INTERRUPTOR_MECANISMO", color=7)
    dxf.add_text("MECANISMO TECLA", 32, 30, height=2, layer="TEXTOS", color=7)

    # Placa exterior decorativa
    dxf.add_rect(47, 0, 5, 80, layer="MARCO_DECORATIVO", color=1)

    dxf.save()

if __name__ == "__main__":
    out_dir = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/05_reles_conmutacion_pared/mecanico"
    os.makedirs(out_dir, exist_ok=True)
    dxf_file = os.path.join(out_dir, "plano_instalacion_micromodulo_pared.dxf")
    svg_file = os.path.join(out_dir, "plano_instalacion_micromodulo_pared.svg")

    generar_plano_rele_dxf(dxf_file)
    generar_svg_rele_pared(svg_file)

