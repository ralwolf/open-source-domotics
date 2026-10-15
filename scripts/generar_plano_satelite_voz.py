#!/usr/bin/env python3
"""
Generador de Plano CAD 2D: Satélite de Voz de Sobremesa ESP32-S3 y Pipeline Local
Formatos de salida: DXF (AutoCAD R12) y SVG vectorial
Módulo: 05_confort_y_exteriores/06_asistente_voz_local_privado/mecanico
"""

import os
import sys

# Asegurar path para importar SimpleDXF
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generar_planos_dxf import SimpleDXF

def generar_plano_satelite_voz(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_ROTULO", color=7)
    dxf.add_layer("CHASIS_CARCASA", color=8)
    dxf.add_layer("REJILLA_ALTAVOZ", color=4)
    dxf.add_layer("MIC_MEMS_I2S", color=1)
    dxf.add_layer("ANILLO_LED_DIFUSOR", color=3)
    dxf.add_layer("COTAS_COTACION", color=2)
    dxf.add_layer("TEXTO_NOTAS", color=7)

    # Marco y Cajetín A3 (420 x 297 mm)
    dxf.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf.add_rect(210, 10, 200, 45, layer="MARCO_ROTULO")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", 215, 45, height=4.0, layer="TEXTO_NOTAS")
    dxf.add_text("SATELITE DE VOZ LOCAL Y PRIVADO (ESP32-S3 + I2S DUPLEX)", 215, 36, height=2.0, layer="TEXTO_NOTAS")
    dxf.add_text("Matriz 2x INMP441 (45mm) | Altavoz 40mm 3W | DAC MAX98357A | 12x WS2812B", 215, 26, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("openWakeWord + Whisper STT + Piper TTS 100% Local en Proxmox VE", 215, 16, height=1.4, layer="TEXTO_NOTAS")

    # Vista 1: Alzado Frontal (Centro X=110, Y=180)
    ax, ay = 110.0, 180.0
    # Base 90 mm, Top 75 mm, Alto 55 mm
    dxf.add_line(ax - 45, ay, ax + 45, ay, layer="CHASIS_CARCASA")
    dxf.add_line(ax - 37.5, ay + 55, ax + 37.5, ay + 55, layer="CHASIS_CARCASA")
    dxf.add_line(ax - 45, ay, ax - 37.5, ay + 55, layer="CHASIS_CARCASA")
    dxf.add_line(ax + 45, ay, ax + 37.5, ay + 55, layer="CHASIS_CARCASA")

    # Difusor LED inferior (H=4 mm)
    dxf.add_rect(ax - 46, ay + 1, 92, 4, layer="ANILLO_LED_DIFUSOR")

    # Micrófonos frontales (Separación 45 mm, Y=ay + 25)
    dxf.add_circle(ax - 22.5, ay + 25, 2.0, layer="MIC_MEMS_I2S")
    dxf.add_circle(ax + 22.5, ay + 25, 2.0, layer="MIC_MEMS_I2S")
    dxf.add_text("MIC-L (INMP441)", ax - 40, ay + 18, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("MIC-R (INMP441)", ax + 10, ay + 18, height=1.4, layer="TEXTO_NOTAS")

    # Botón Mute Privacidad superior
    dxf.add_rect(ax - 6, ay + 55, 12, 3, layer="MIC_MEMS_I2S")
    dxf.add_text("MUTE HARDWARE", ax - 15, ay + 61, height=1.4, layer="TEXTO_NOTAS")

    # Cotas Alzado
    dxf.add_line(ax - 45, ay - 8, ax + 45, ay - 8, layer="COTAS_COTACION")
    dxf.add_text("90.0 mm (Base)", ax - 14, ay - 7, height=1.8, layer="COTAS_COTACION")

    dxf.add_line(ax + 45 + 10, ay, ax + 45 + 10, ay + 55, layer="COTAS_COTACION")
    dxf.add_text("55.0 mm", ax + 45 + 12, ay + 26, height=1.8, layer="COTAS_COTACION")

    dxf.add_text("ALZADO FRONTAL (ESC. 1:1)", ax - 25, ay + 72, height=2.2, layer="TEXTO_NOTAS")

    # Vista 2: Planta Superior (Centro X=110, Y=70)
    px, py = 110.0, 70.0
    dxf.add_circle(px, py, 37.5, layer="CHASIS_CARCASA")
    dxf.add_circle(px, py, 6.0, layer="MIC_MEMS_I2S")  # Botón central
    # Rejilla concéntrica
    dxf.add_circle(px, py, 12.0, layer="REJILLA_ALTAVOZ")
    dxf.add_circle(px, py, 20.0, layer="REJILLA_ALTAVOZ")
    dxf.add_circle(px, py, 28.0, layer="REJILLA_ALTAVOZ")
    dxf.add_text("PLANTA SUPERIOR - REJILLA ACUSTICA", px - 35, py - 43, height=2.0, layer="TEXTO_NOTAS")

    # Vista 3: Arquitectura del Pipeline de Voz Local Privado (Derecha)
    fx, fy = 240.0, 220.0
    dxf.add_text("PIPELINE DE VOZ 100% LOCAL (WYOMING PROTOCOL)", fx - 15, fy + 45, height=2.2, layer="TEXTO_NOTAS")

    # Bloque 1: Satélite ESP32-S3
    dxf.add_rect(fx - 15, fy + 5, 80, 32, layer="CHASIS_CARCASA")
    dxf.add_text("SATELITE ESP32-S3 (Borde)", fx - 10, fy + 30, height=1.8, layer="TEXTO_NOTAS")
    dxf.add_text("• Matriz Micrófonos I2S 16 kHz", fx - 10, fy + 22, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("• openWakeWord local ('Ok Nabu')", fx - 10, fy + 15, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("• Indicador Anillo RGB WS2812B", fx - 10, fy + 8, height=1.4, layer="TEXTO_NOTAS")

    # Conexión Wi-Fi segura VLAN 30
    dxf.add_line(fx + 25, fy + 5, fx + 25, fy - 15, layer="REJILLA_ALTAVOZ")
    dxf.add_text("Audio RAW PCM (VLAN 30 IoT)", fx + 28, fy - 5, height=1.3, layer="COTAS_COTACION")

    # Bloque 2: Servidor Proxmox VE (Whisper + Piper)
    dxf.add_rect(fx - 15, fy - 55, 80, 38, layer="REJILLA_ALTAVOZ")
    dxf.add_text("SERVIDOR PROXMOX VE (Local)", fx - 10, fy - 24, height=1.8, layer="TEXTO_NOTAS")
    dxf.add_text("• Whisper STT (Speech-to-Text)", fx - 10, fy - 32, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("• Home Assistant Intent Engine", fx - 10, fy - 40, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("• Piper TTS (Sintesis de voz ES)", fx - 10, fy - 48, height=1.4, layer="TEXTO_NOTAS")

    # Retorno de audio sintetizado
    dxf.add_line(fx + 65, fy - 35, fx + 65, fy + 20, layer="ANILLO_LED_DIFUSOR")
    dxf.add_line(fx + 65, fy + 20, fx + 55, fy + 20, layer="ANILLO_LED_DIFUSOR")
    dxf.add_text("Audio TTS (FLAC/WAV)", fx + 70, fy - 5, height=1.3, layer="COTAS_COTACION")

    # Bloque 3: Acciones Domóticas Ejecutadas
    dxf.add_rect(fx - 15, fy - 110, 80, 45, layer="ANILLO_LED_DIFUSOR")
    dxf.add_text("CONTROL RESIDENCIAL INTEGRADO", fx - 10, fy - 72, height=1.8, layer="TEXTO_NOTAS")
    dxf.add_text("• Luces Circadianas y Escenas", fx - 10, fy - 80, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("• Climatización Suelo Radiante", fx - 10, fy - 88, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("• Consulta Baterías LiFePO4 y Solar", fx - 10, fy - 96, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("• Apertura Puertas y Bomba Piscina", fx - 10, fy - 104, height=1.4, layer="TEXTO_NOTAS")

    dxf.save()

    # 2. GENERACIÓN SVG VECTORIAL
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 297" width="100%" height="100%" style="background-color: #1a1c23; font-family: monospace;">
  <defs>
    <style>
      .marco {{ stroke: #454d66; stroke-width: 1.0; fill: none; }}
      .chasis {{ stroke: #70798c; stroke-width: 1.5; fill: #2d3142; }}
      .difusor {{ stroke: #48cae4; stroke-width: 1.2; fill: rgba(72, 202, 228, 0.3); }}
      .mic {{ stroke: #f28482; stroke-width: 1.2; fill: #e76f51; }}
      .rejilla {{ stroke: #84a59d; stroke-width: 1.0; fill: none; stroke-dasharray: 2,1; }}
      .bloque {{ stroke: #457b9d; stroke-width: 1.2; fill: #1d3557; }}
      .cable {{ stroke: #e9c46a; stroke-width: 1.2; stroke-dasharray: 3,2; fill: none; }}
      .txt-title {{ fill: #ffffff; font-size: 4px; font-weight: bold; }}
      .txt-sub {{ fill: #00f5d4; font-size: 2.2px; font-weight: bold; }}
      .txt-body {{ fill: #d8e2dc; font-size: 1.6px; }}
      .txt-cota {{ fill: #f4a261; font-size: 1.8px; }}
      .txt-alert {{ fill: #e63946; font-size: 1.5px; font-weight: bold; }}
    </style>
  </defs>

  <!-- Marco A3 -->
  <rect x="5" y="5" width="410" height="287" class="marco"/>
  <rect x="210" y="242" width="200" height="45" class="marco"/>
  <text x="215" y="254" class="txt-title">OPEN-SOURCE-DOMOTICS</text>
  <text x="215" y="262" class="txt-sub">SATÉLITE DE VOZ LOCAL Y PRIVADO (ESP32-S3 + I2S DÚPLEX)</text>
  <text x="215" y="271" class="txt-body">Matriz 2x INMP441 (45mm) | Altavoz 40mm 3W | DAC MAX98357A | 12x WS2812B</text>
  <text x="215" y="279" class="txt-body">openWakeWord + Whisper STT + Piper TTS 100% Local en Proxmox VE</text>

  <!-- Vista Alzado Frontal -->
  <g id="alzado">
    <text x="75" y="45" class="txt-sub">ALZADO FRONTAL (ESC. 1:1)</text>
    
    <!-- Botón Mute -->
    <rect x="{ax - 6}" y="{297 - (ay + 58)}" width="12" height="3" class="mic" rx="1"/>
    <text x="{ax - 18}" y="{297 - (ay + 61)}" class="txt-alert">MUTE PRIVACIDAD</text>

    <!-- Carcasa Troncocónica -->
    <polygon points="{ax - 45},{297 - ay} {ax - 37.5},{297 - (ay + 55)} {ax + 37.5},{297 - (ay + 55)} {ax + 45},{297 - ay}" class="chasis"/>

    <!-- Difusor LED inferior -->
    <rect x="{ax - 46}" y="{297 - (ay + 5)}" width="92" height="4" class="difusor" rx="1"/>

    <!-- Micrófonos I2S -->
    <circle cx="{ax - 22.5}" cy="{297 - (ay + 25)}" r="2.5" class="mic"/>
    <circle cx="{ax + 22.5}" cy="{297 - (ay + 25)}" r="2.5" class="mic"/>
    <text x="{ax - 38}" y="{297 - (ay + 18)}" class="txt-body">MIC-L (I2S)</text>
    <text x="{ax + 8}" y="{297 - (ay + 18)}" class="txt-body">MIC-R (I2S)</text>

    <!-- Cotas -->
    <line x1="{ax - 45}" y1="{297 - (ay - 8)}" x2="{ax + 45}" y2="{297 - (ay - 8)}" stroke="#f4a261" stroke-width="0.8"/>
    <text x="{ax - 15}" y="{297 - (ay - 14)}" class="txt-cota">Ø 90.0 mm</text>
  </g>

  <!-- Vista Planta Superior Rejilla -->
  <g id="planta">
    <text x="65" y="195" class="txt-sub">PLANTA SUPERIOR - REJILLA ACÚSTICA</text>
    <circle cx="{px}" cy="{297 - py}" r="37.5" class="chasis"/>
    <circle cx="{px}" cy="{297 - py}" r="28.0" class="rejilla"/>
    <circle cx="{px}" cy="{297 - py}" r="20.0" class="rejilla"/>
    <circle cx="{px}" cy="{297 - py}" r="12.0" class="rejilla"/>
    <circle cx="{px}" cy="{297 - py}" r="6.0" class="mic"/>
  </g>

  <!-- Diagrama de Arquitectura Wyoming Local (Derecha) -->
  <g id="pipeline">
    <text x="230" y="45" class="txt-sub">ARQUITECTURA DE VOZ 100% LOCAL Y PRIVADA</text>

    <!-- Satélite -->
    <rect x="230" y="60" width="85" height="42" class="bloque" rx="2"/>
    <text x="235" y="73" class="txt-sub">SATÉLITE ESP32-S3 (Borde)</text>
    <text x="235" y="82" class="txt-body">• Captura estéreo I2S 16 kHz</text>
    <text x="235" y="90" class="txt-body">• openWakeWord local ("Ok Nabu")</text>
    <text x="235" y="98" class="txt-body">• Feedback anillo LED WS2812B</text>

    <!-- Conexión Stream -->
    <line x1="272" y1="102" x2="272" y2="125" class="cable"/>
    <text x="277" y="116" class="txt-cota">RAW Audio</text>

    <!-- Servidor Proxmox -->
    <rect x="230" y="125" width="85" height="50" class="bloque" rx="2"/>
    <text x="235" y="138" class="txt-sub">PROXMOX VE (Servidor)</text>
    <text x="235" y="147" class="txt-body">• Whisper STT (Español)</text>
    <text x="235" y="155" class="txt-body">• Home Assistant Intents Engine</text>
    <text x="235" y="163" class="txt-body">• Piper TTS (Síntesis voz local)</text>
    <text x="235" y="171" class="txt-alert">✓ CERO DATOS A LA NUBE</text>

    <!-- Respuesta Altavoz -->
    <line x1="315" y1="150" x2="335" y2="150" class="cable"/>
    <line x1="335" y1="150" x2="335" y2="80" class="cable"/>
    <line x1="335" y1="80" x2="315" y2="80" class="cable"/>
    <text x="340" y="115" class="txt-cota">TTS I2S</text>
  </g>
</svg>
"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Plano CAD 2D DXF generado en: {dxf_path}")
    print(f"Plano vectorial SVG generado en: {svg_path}")

if __name__ == "__main__":
    dxf_out = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/06_asistente_voz_local_privado/mecanico/plano_satelite_voz.dxf"
    svg_out = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/06_asistente_voz_local_privado/mecanico/plano_satelite_voz.svg"
    generar_plano_satelite_voz(dxf_out, svg_out)
