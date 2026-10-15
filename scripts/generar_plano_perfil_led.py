#!/usr/bin/env python3
"""
Generador de Plano CAD 2D: Perfil de Aluminio Disipador y Montaje de Tira LED Circadiana
Formatos de salida: DXF (AutoCAD R12) y SVG vectorial
Módulo: 05_confort_y_exteriores/01_iluminacion_circadiana_y_exterior/mecanico
"""

import os
import sys

# Asegurar path para importar SimpleDXF
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generar_planos_dxf import SimpleDXF

def generar_plano_perfil_led(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_ROTULO", color=7)
    dxf.add_layer("PERFIL_ALUMINIO", color=8)
    dxf.add_layer("DIFUSOR_OPALINO", color=4)
    dxf.add_layer("TIRA_LED_PCB", color=1)
    dxf.add_layer("COTAS_COTACION", color=2)
    dxf.add_layer("TEXTO_NOTAS", color=7)
    dxf.add_layer("CLIP_MONTAJE", color=3)

    # Marco y Cajetín A3 (420 x 297 mm)
    dxf.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf.add_rect(210, 10, 200, 45, layer="MARCO_ROTULO")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", 215, 45, height=4.0, layer="TEXTO_NOTAS")
    dxf.add_text("DETALLE DE CORTE Y MONTAJE: PERFIL LED CIRCADIANO CCT", 215, 36, height=2.0, layer="TEXTO_NOTAS")
    dxf.add_text("Aluminio Extruido 6063-T5 | Difusor PC Bayer Makrolon Opalino 85% Trans.", 215, 26, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Tira Dual CCT 2200K-6500K 24VDC 19.2W/m | Clip de Inox Oculto", 215, 16, height=1.4, layer="TEXTO_NOTAS")

    # Vista 1: Sección Transversal Escala Ampliada (Escala 4:1)
    # Centro en X=110, Y=170
    cx, cy = 110.0, 170.0
    s4 = 4.0  # factor de escala

    # Dimensiones reales en mm: Ancho Ext 25, Alto Ext 15, Espesor 1.5, Interior 22 x 13.5
    w_ext, h_ext, t = 25.0 * s4, 15.0 * s4, 1.5 * s4
    w_int, h_int = 22.0 * s4, 13.5 * s4

    # Perfil de Aluminio
    dxf.add_rect(cx - w_ext/2, cy - h_ext/2, w_ext, h_ext, layer="PERFIL_ALUMINIO")
    dxf.add_rect(cx - w_int/2, cy - h_ext/2 + t, w_int, h_int, layer="PERFIL_ALUMINIO")

    # Difusor Superior (encaje a presión)
    w_dif = (22.0 + 0.8) * s4
    h_dif = 4.0 * s4
    t_dif = 1.2 * s4
    dxf.add_rect(cx - w_dif/2, cy + h_ext/2 - t, w_dif, h_dif, layer="DIFUSOR_OPALINO")
    dxf.add_rect(cx - (w_dif - 2*t_dif)/2, cy + h_ext/2 - t + t_dif, w_dif - 2*t_dif, h_dif - t_dif, layer="DIFUSOR_OPALINO")

    # Tira LED en el fondo interior
    w_pcb = 10.0 * s4
    h_pcb = 1.0 * s4
    dxf.add_rect(cx - w_pcb/2, cy - h_ext/2 + t, w_pcb, h_pcb, layer="TIRA_LED_PCB")
    # Dos emisores SMD 2835 (Warm White y Cold White)
    dxf.add_rect(cx - 3.5*s4, cy - h_ext/2 + t + h_pcb, 2.8*s4, 1.2*s4, layer="TIRA_LED_PCB")
    dxf.add_rect(cx + 0.7*s4, cy - h_ext/2 + t + h_pcb, 2.8*s4, 1.2*s4, layer="TIRA_LED_PCB")

    # Clip de Montaje Oculto inferior
    dxf.add_rect(cx - (w_ext + 2.5*s4)/2, cy - h_ext/2 - 2.5*s4, w_ext + 2.5*s4, 2.5*s4, layer="CLIP_MONTAJE")
    dxf.add_rect(cx - (w_ext + 2.5*s4)/2, cy - h_ext/2, 1.5*s4, 5.0*s4, layer="CLIP_MONTAJE")
    dxf.add_rect(cx + (w_ext + 2.5*s4)/2 - 1.5*s4, cy - h_ext/2, 1.5*s4, 5.0*s4, layer="CLIP_MONTAJE")

    # Cotas Sección Transversal
    dxf.add_line(cx - w_ext/2, cy - h_ext/2 - 15, cx + w_ext/2, cy - h_ext/2 - 15, layer="COTAS_COTACION")
    dxf.add_text("25.0 mm", cx - 8, cy - h_ext/2 - 14, height=2.0, layer="COTAS_COTACION")

    dxf.add_line(cx + w_ext/2 + 15, cy - h_ext/2, cx + w_ext/2 + 15, cy + h_ext/2, layer="COTAS_COTACION")
    dxf.add_text("15.0 mm", cx + w_ext/2 + 17, cy, height=2.0, layer="COTAS_COTACION")

    dxf.add_text("SECCION TRANSVERSAL (ESC. 4:1)", cx - 35, cy + h_ext/2 + 25, height=2.5, layer="TEXTO_NOTAS")
    dxf.add_text("1. Difusor Policarbonato Opalino Curvo", cx - 45, cy + h_ext/2 + 15, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("2. LEDs SMD 2835 Dual CCT (WW 2200K + CW 6500K)", cx - 45, cy - 2, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("3. Perfil Disipador Aluminio Anodizado", cx - 45, cy - h_ext/2 + 4, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("4. Clip Oculto Acero Inox AISI 304", cx - 45, cy - h_ext/2 - 8, height=1.6, layer="TEXTO_NOTAS")

    # Vista 2: Esquema Unifilar de Cableado y Conexión Dimmer PWM (Derecha)
    px, py = 250.0, 160.0
    dxf.add_text("ESQUEMA DE CONEXION DIMMER PWM 24V", px - 20, py + 85, height=2.5, layer="TEXTO_NOTAS")

    # Fuente Mean Well HLG-240H-24 (24VDC 10A)
    dxf.add_rect(px - 20, py + 40, 50, 30, layer="PERFIL_ALUMINIO")
    dxf.add_text("FUENTE MEAN WELL", px - 18, py + 62, height=1.8, layer="TEXTO_NOTAS")
    dxf.add_text("HLG-240H-24 SELV", px - 18, py + 54, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("In: 230VAC | Out: 24VDC 10A", px - 18, py + 46, height=1.4, layer="TEXTO_NOTAS")

    # Controlador Dimmer ESP32 (4 Canales MOSFET)
    dxf.add_rect(px + 60, py + 30, 65, 45, layer="PERFIL_ALUMINIO")
    dxf.add_text("DIMMER ESP32 CIRCADIANO", px + 63, py + 68, height=1.8, layer="TEXTO_NOTAS")
    dxf.add_text("4x MOSFET AOD4184A", px + 63, py + 60, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("PWM 20 kHz Flicker-Free", px + 63, py + 52, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("Bus I2C (BH1750 + mmWave)", px + 63, py + 44, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("RS485 DMX/Modbus Aislado", px + 63, py + 36, height=1.4, layer="TEXTO_NOTAS")

    # Conexión Fuente a Dimmer
    dxf.add_line(px + 30, py + 55, px + 60, py + 55, layer="TIRA_LED_PCB")
    dxf.add_text("+24V / GND", px + 35, py + 58, height=1.4, layer="COTAS_COTACION")

    # Salidas PWM a las Tiras LED (Zona Interior CCT + Zona Exterior Perimetral)
    dxf.add_rect(px + 60, py - 40, 70, 45, layer="DIFUSOR_OPALINO")
    dxf.add_text("LUMINARIAS Y TIRAS LED", px + 63, py - 2, height=1.8, layer="TEXTO_NOTAS")
    dxf.add_text("CH1: Blanco Calido 2200K (CCT)", px + 63, py - 10, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("CH2: Blanco Frio 6500K (CCT)", px + 63, py - 18, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("CH3: Exterior Porche/Jardin 24V", px + 63, py - 26, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("CH4: Cortesía Fachada Perimetral", px + 63, py - 34, height=1.5, layer="TEXTO_NOTAS")

    # Líneas de control PWM
    dxf.add_line(px + 90, py + 30, px + 90, py + 5, layer="TIRA_LED_PCB")
    dxf.add_text("Salidas PWM 24V", px + 93, py + 18, height=1.4, layer="COTAS_COTACION")

    dxf.save()

    # 2. GENERACIÓN SVG VECTORIAL
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 297" width="100%" height="100%" style="background-color: #1e1e24; font-family: monospace;">
  <defs>
    <style>
      .marco {{ stroke: #555566; stroke-width: 1.0; fill: none; }}
      .perfil {{ stroke: #a0a0b0; stroke-width: 1.5; fill: #2b2b36; }}
      .difusor {{ stroke: #66ccff; stroke-width: 1.2; fill: rgba(102, 204, 255, 0.2); }}
      .pcb {{ stroke: #ffcc00; stroke-width: 1.0; fill: #d4a017; }}
      .clip {{ stroke: #00ff88; stroke-width: 1.2; fill: none; }}
      .cota {{ stroke: #ff7700; stroke-width: 0.8; fill: none; }}
      .txt-title {{ fill: #ffffff; font-size: 4px; font-weight: bold; }}
      .txt-sub {{ fill: #00ddff; font-size: 2.2px; font-weight: bold; }}
      .txt-body {{ fill: #cccccc; font-size: 1.6px; }}
      .txt-cota {{ fill: #ff9933; font-size: 1.8px; }}
      .txt-sec {{ fill: #88ffaa; font-size: 2.5px; font-weight: bold; }}
      .bloque {{ stroke: #4488ee; stroke-width: 1.0; fill: #222b40; }}
      .cable {{ stroke: #ffaa00; stroke-width: 1.2; stroke-dasharray: 2,1; }}
    </style>
  </defs>

  <!-- Marco A3 -->
  <rect x="5" y="5" width="410" height="287" class="marco"/>
  <rect x="210" y="242" width="200" height="45" class="marco"/>
  <text x="215" y="254" class="txt-title">OPEN-SOURCE-DOMOTICS</text>
  <text x="215" y="262" class="txt-sub">DETALLE DE CORTE Y MONTAJE: PERFIL LED CIRCADIANO CCT</text>
  <text x="215" y="271" class="txt-body">Aluminio Extruido 6063-T5 | Difusor PC Makrolon Opalino 85% Trans.</text>
  <text x="215" y="279" class="txt-body">Tira Dual CCT 2200K-6500K 24VDC 19.2W/m | Clip de Inox Oculto</text>

  <!-- Vista Sección Transversal 4:1 -->
  <!-- Invertir Y para SVG (cy = 297 - 170 = 127) -->
  <g id="seccion_perfil">
    <!-- Clip Inox -->
    <rect x="{cx - (w_ext + 2.5*s4)/2}" y="{127 + h_ext/2}" width="{w_ext + 2.5*s4}" height="{2.5*s4}" class="clip"/>
    <rect x="{cx - (w_ext + 2.5*s4)/2}" y="{127 + h_ext/2 - 5*s4}" width="{1.5*s4}" height="{5.0*s4}" class="clip"/>
    <rect x="{cx + (w_ext + 2.5*s4)/2 - 1.5*s4}" y="{127 + h_ext/2 - 5*s4}" width="{1.5*s4}" height="{5.0*s4}" class="clip"/>

    <!-- Perfil Aluminio Exterior e Interior -->
    <rect x="{cx - w_ext/2}" y="{127 - h_ext/2}" width="{w_ext}" height="{h_ext}" class="perfil"/>
    <rect x="{cx - w_int/2}" y="{127 - h_ext/2}" width="{w_int}" height="{h_int}" fill="#1e1e24" stroke="#a0a0b0" stroke-width="1.0"/>

    <!-- PCB y Emisores LED -->
    <rect x="{cx - w_pcb/2}" y="{127 + h_ext/2 - t - h_pcb}" width="{w_pcb}" height="{h_pcb}" class="pcb"/>
    <rect x="{cx - 3.5*s4}" y="{127 + h_ext/2 - t - h_pcb - 1.2*s4}" width="{2.8*s4}" height="{1.2*s4}" fill="#ffaa00"/>
    <rect x="{cx + 0.7*s4}" y="{127 + h_ext/2 - t - h_pcb - 1.2*s4}" width="{2.8*s4}" height="{1.2*s4}" fill="#88ddff"/>

    <!-- Difusor PC Opalino -->
    <rect x="{cx - w_dif/2}" y="{127 - h_ext/2 - h_dif + t}" width="{w_dif}" height="{h_dif}" class="difusor" rx="2"/>

    <!-- Cotas -->
    <line x1="{cx - w_ext/2}" y1="{127 + h_ext/2 + 18}" x2="{cx + w_ext/2}" y2="{127 + h_ext/2 + 18}" class="cota"/>
    <text x="{cx - 10}" y="{127 + h_ext/2 + 23}" class="txt-cota">25.0 mm</text>

    <line x1="{cx + w_ext/2 + 15}" y1="{127 - h_ext/2}" x2="{cx + w_ext/2 + 15}" y2="{127 + h_ext/2}" class="cota"/>
    <text x="{cx + w_ext/2 + 18}" y="{127 + 2}" class="txt-cota">15.0 mm</text>

    <text x="{cx - 45}" y="50" class="txt-sec">SECCIÓN TRANSVERSAL (ESC. 4:1)</text>
    <text x="{cx - 50}" y="65" class="txt-body">1. Difusor Policarbonato Opalino Curvo (85% Difusión)</text>
    <text x="{cx - 50}" y="73" class="txt-body">2. LEDs SMD 2835 Dual CCT (WW 2200K + CW 6500K, CRI &gt; 95)</text>
    <text x="{cx - 50}" y="81" class="txt-body">3. Perfil Disipador Aluminio Anodizado 6063-T5</text>
    <text x="{cx - 50}" y="89" class="txt-body">4. Clip Oculto Acero Inox AISI 304 con Ranura Clic</text>
  </g>

  <!-- Esquema Eléctrico Unifilar (Derecha) -->
  <g id="esquema_conexion">
    <text x="230" y="50" class="txt-sec">ARQUITECTURA DE CONTROL Y ALIMENTACIÓN</text>

    <!-- Fuente Mean Well -->
    <rect x="230" y="70" width="70" height="38" class="bloque"/>
    <text x="235" y="82" class="txt-sub">FUENTE 24VDC</text>
    <text x="235" y="90" class="txt-body">Mean Well HLG-240H-24</text>
    <text x="235" y="98" class="txt-body">230VAC -&gt; 24VDC 10A (SELV)</text>

    <!-- Línea 24V -->
    <line x1="300" y1="89" x2="330" y2="89" class="cable"/>
    <text x="303" y="85" class="txt-cota">24VDC</text>

    <!-- Dimmer ESP32 -->
    <rect x="330" y="65" width="75" height="55" class="bloque"/>
    <text x="335" y="77" class="txt-sub">DIMMER ESP32</text>
    <text x="335" y="85" class="txt-body">4x MOSFET AOD4184A</text>
    <text x="335" y="93" class="txt-body">PWM 20 kHz Flicker-Free</text>
    <text x="335" y="101" class="txt-body">Bus I2C (BH1750 / mmWave)</text>
    <text x="335" y="109" class="txt-body">RS-485 DMX/Modbus Aislado</text>

    <!-- Línea hacia Tiras -->
    <line x1="367" y1="120" x2="367" y2="145" class="cable"/>
    <text x="372" y="135" class="txt-cota">4x PWM 24V</text>

    <!-- Cargas LED -->
    <rect x="250" y="145" width="155" height="55" class="bloque"/>
    <text x="255" y="158" class="txt-sub">CANALES Y CIRCUITOS DE ILUMINACIÓN</text>
    <text x="255" y="167" class="txt-body">• CH1: Blanco Cálido 2200K (Interior Sala/Dormitorios - Ciclo Circadiano)</text>
    <text x="255" y="175" class="txt-body">• CH2: Blanco Frío 6500K (Interior Cocina/Despacho - Ciclo Circadiano)</text>
    <text x="255" y="183" class="txt-body">• CH3: Exterior Jardín y Pérgola (Modulación 24V IP66)</text>
    <text x="255" y="191" class="txt-body">• CH4: Iluminación de Seguridad Perimetral (Cortesía 15% -&gt; Detección 100%)</text>
  </g>
</svg>
"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Plano CAD 2D DXF generado en: {dxf_path}")
    print(f"Plano vectorial SVG generado en: {svg_path}")

if __name__ == "__main__":
    dxf_out = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/01_iluminacion_circadiana_y_exterior/mecanico/plano_corte_perfil_led.dxf"
    svg_out = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/01_iluminacion_circadiana_y_exterior/mecanico/plano_corte_perfil_led.svg"
    generar_plano_perfil_led(dxf_out, svg_out)

