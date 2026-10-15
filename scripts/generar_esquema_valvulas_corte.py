#!/usr/bin/env python3
"""
Generador del Esquema de Corte de Emergencia de Válvulas de Gas y Agua
Formatos de salida: DXF y SVG vectorial
Proyecto: open-source-domotics
"""

import os
from generar_planos_dxf import SimpleDXF

def generar_esquema_valvulas_corte(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_ROTULO", color=7)
    dxf.add_layer("TUBERIA_AGUA", color=5)       # Azul
    dxf.add_layer("TUBERIA_GAS", color=2)        # Amarillo
    dxf.add_layer("VALVULAS_ACTUADORES", color=1) # Rojo
    dxf.add_layer("SENSORES_FUGAS", color=4)     # Cian
    dxf.add_layer("CONTROL_ELECTRONICO", color=6) # Magenta
    dxf.add_layer("TEXTO_ROTULOS", color=7)

    dxf.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf.add_rect(240, 10, 170, 40, layer="MARCO_ROTULO")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", 245, 38, height=4.0, layer="TEXTO_ROTULOS")
    dxf.add_text("SISTEMA DE CORTE DE EMERGENCIA: VÁLVULAS DE GAS Y AGUA", 245, 28, height=2.2, layer="TEXTO_ROTULOS")
    dxf.add_text("Detección de Fugas -> Disparo Autónomo <1s -> Respaldo Batería", 245, 18, height=1.8, layer="TEXTO_ROTULOS")

    # LÍNEA 1: ACOMETIDA DE AGUA POTABLE (Azul)
    dxf.add_line(30, 220, 390, 220, layer="TUBERIA_AGUA")
    dxf.add_text("ACOMETIDA GENERAL AGUA RED / CISTERNA", 35, 228, height=2.2, layer="TEXTO_ROTULOS")

    # Contador / Manómetro
    dxf.add_circle(90, 220, 8, layer="VALVULAS_ACTUADORES")
    dxf.add_text("CONTADOR IMPULSOS", 75, 235, height=1.6, layer="TEXTO_ROTULOS")

    # Filtro de Sedimentos 50 micras
    dxf.add_rect(130, 210, 25, 20, layer="VALVULAS_ACTUADORES")
    dxf.add_text("FILTRO 50u", 132, 218, height=1.5, layer="TEXTO_ROTULOS")

    # Válvula de Corte Motorizada DN25 (1") con Condensador de Retorno
    dxf.add_rect(180, 205, 40, 30, layer="VALVULAS_ACTUADORES")
    dxf.add_text("ELECTROVÁLVULA AGUA", 182, 226, height=1.8, layer="TEXTO_ROTULOS")
    dxf.add_text("Biestable 12V DC (DN25)", 182, 218, height=1.5, layer="TEXTO_ROTULOS")
    dxf.add_text("Retorno Automático < 3s", 182, 210, height=1.3, layer="TEXTO_ROTULOS")

    # Sensores de Fuga de Agua (Cocina, Baños, Lavandería)
    dxf.add_rect(280, 205, 30, 30, layer="SENSORES_FUGAS")
    dxf.add_text("SENSOR AGUA", 282, 224, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Cable Conductivo", 282, 215, height=1.3, layer="TEXTO_ROTULOS")

    dxf.add_text("DISTRIBUCIÓN AGUA VIVIENDA", 330, 228, height=2.0, layer="TEXTO_ROTULOS")

    # LÍNEA 2: ACOMETIDA DE GAS DUAL (Amarillo)
    dxf.add_line(30, 120, 390, 120, layer="TUBERIA_GAS")
    dxf.add_text("ACOMETIDA GAS DUAL (RED / BIOGÁS / GLP)", 35, 128, height=2.2, layer="TEXTO_ROTULOS")

    # Regulador de Presión de Gas
    dxf.add_rect(80, 110, 25, 20, layer="VALVULAS_ACTUADORES")
    dxf.add_text("REGULADOR 20mbar", 72, 135, height=1.6, layer="TEXTO_ROTULOS")

    # Electroválvula de Rearme Manual de Gas (Disparo Rápido <1s)
    dxf.add_rect(180, 105, 40, 30, layer="VALVULAS_ACTUADORES")
    dxf.add_text("VÁLVULA GAS 12V", 182, 126, height=1.8, layer="TEXTO_ROTULOS")
    dxf.add_text("Rearme Manual Seguro", 182, 118, height=1.5, layer="TEXTO_ROTULOS")
    dxf.add_text("Corte Instantáneo < 1s", 182, 110, height=1.3, layer="TEXTO_ROTULOS")

    # Sensor Detector de Gas Metano / GLP
    dxf.add_rect(280, 105, 30, 30, layer="SENSORES_FUGAS")
    dxf.add_text("SENSOR GAS", 283, 124, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("MQ-4 / Óptico", 283, 115, height=1.3, layer="TEXTO_ROTULOS")

    dxf.add_text("HACIA COCINA / CALDERA / HORNO", 310, 128, height=2.0, layer="TEXTO_ROTULOS")

    # CONTROLADOR ELECTRÓNICO CENTRAL DE SEGURIDAD (Abajo)
    dxf.add_rect(140, 25, 120, 50, layer="CONTROL_ELECTRONICO")
    dxf.add_text("CONTROLADOR DE SEGURIDAD ESP32", 145, 62, height=2.2, layer="TEXTO_ROTULOS")
    dxf.add_text("- Batería Li-Ion 18650 de Respaldo Integrada", 145, 52, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("- Alarma Sonora Sirena 85 dB in situ", 145, 44, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("- Disparo Autónomo sin dependencia de WiFi", 145, 36, height=1.6, layer="TEXTO_ROTULOS")

    # Enlaces de control a válvulas
    dxf.add_line(200, 75, 200, 105, layer="CONTROL_ELECTRONICO")
    dxf.add_line(200, 135, 200, 205, layer="CONTROL_ELECTRONICO")

    dxf.save()

    # 2. GENERACIÓN SVG
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 700" width="100%" height="100%" style="background:#11111b; font-family:sans-serif;">
  <defs>
    <style>
      .title {{ fill: #cdd6f4; font-size: 20px; font-weight: bold; }}
      .sub {{ fill: #89b4fa; font-size: 13px; }}
      .box {{ fill: #1e1e2e; stroke: #45475a; stroke-width: 2; rx: 6; }}
      .lbl {{ fill: #cdd6f4; font-size: 11px; }}
      .lbl-bold {{ fill: #ffffff; font-size: 12px; font-weight: bold; }}
      .lbl-sm {{ fill: #a6adc8; font-size: 9.5px; }}
      .pipe-water {{ stroke: #89b4fa; stroke-width: 5; fill: none; }}
      .pipe-gas {{ stroke: #f9e2af; stroke-width: 5; fill: none; }}
      .wire-ctrl {{ stroke: #f38ba8; stroke-width: 2; stroke-dasharray: 4; fill: none; }}
    </style>
  </defs>

  <!-- Marco -->
  <rect x="20" y="20" width="1060" height="660" fill="none" stroke="#313244" stroke-width="2" rx="10"/>

  <!-- Encabezado -->
  <text x="50" y="55" class="title">SISTEMA AUTÓNOMO DE CORTE DE EMERGENCIA PARA FUGAS DE GAS Y AGUA</text>
  <text x="50" y="80" class="sub">Válvula Motorizada DN25 (Agua) | Válvula Disparo Rápido &lt;1s (Gas) | Sensores Conductivos y Catalíticos | Batería Respaldo</text>

  <!-- LÍNEA DE AGUA POTABLE -->
  <text x="60" y="140" class="lbl-bold" style="fill:#89b4fa; font-size:14px;">1. ACOMETIDA GENERAL DE AGUA POTABLE</text>
  <line x1="60" y1="180" x2="1000" y2="180" class="pipe-water"/>

  <!-- Contador y Filtro -->
  <rect x="180" y="150" width="100" height="60" class="box" stroke="#89b4fa"/>
  <text x="195" y="175" class="lbl-bold">CONTADOR +</text>
  <text x="190" y="195" class="lbl-sm">Filtro Sedimentos</text>

  <!-- Válvula de Corte Motorizada Agua -->
  <rect x="420" y="140" width="160" height="80" class="box" stroke="#f38ba8" stroke-width="2.5"/>
  <text x="435" y="170" class="lbl-bold" style="fill:#f38ba8;">VÁLVULA CORTE AGUA</text>
  <text x="435" y="190" class="lbl-sm">Motorizada Biestable DN25 1"</text>
  <text x="435" y="205" class="lbl-sm">Cierre seguro por retorno</text>

  <!-- Sensor Inundación -->
  <rect x="740" y="150" width="130" height="60" class="box" stroke="#a6e3a1"/>
  <text x="755" y="175" class="lbl-bold" style="fill:#a6e3a1;">SENSOR AGUA</text>
  <text x="750" y="195" class="lbl-sm">Cable Conductivo Cocina</text>

  <text x="1010" y="185" class="lbl-bold" style="fill:#89b4fa;">VIVIENDA</text>

  <!-- LÍNEA DE GAS -->
  <text x="60" y="290" class="lbl-bold" style="fill:#f9e2af; font-size:14px;">2. ACOMETIDA DE GAS DUAL (METANO / BIOGÁS / GLP)</text>
  <line x1="60" y1="330" x2="1000" y2="330" class="pipe-gas"/>

  <!-- Regulador Gas -->
  <rect x="180" y="300" width="100" height="60" class="box" stroke="#f9e2af"/>
  <text x="190" y="325" class="lbl-bold">REGULADOR</text>
  <text x="195" y="345" class="lbl-sm">Gas 20 mbar</text>

  <!-- Válvula de Corte Gas -->
  <rect x="420" y="290" width="160" height="80" class="box" stroke="#f38ba8" stroke-width="2.5"/>
  <text x="440" y="320" class="lbl-bold" style="fill:#f38ba8;">VÁLVULA CORTE GAS</text>
  <text x="435" y="340" class="lbl-sm">Rearme Manual 12V DC</text>
  <text x="435" y="355" class="lbl-sm" style="fill:#f38ba8; font-weight:bold;">Disparo Instantáneo &lt; 1s</text>

  <!-- Sensor Gas -->
  <rect x="740" y="300" width="130" height="60" class="box" stroke="#fab387"/>
  <text x="755" y="325" class="lbl-bold" style="fill:#fab387;">DETECTOR GAS</text>
  <text x="750" y="345" class="lbl-sm">Sensor Óptico / MQ-4</text>

  <text x="1010" y="335" class="lbl-bold" style="fill:#f9e2af;">CONSUMOS</text>

  <!-- 3. CONTROLADOR CENTRAL ESP32 (Abajo) -->
  <rect x="360" y="470" width="380" height="150" class="box" stroke="#a6e3a1" stroke-width="2.5"/>
  <text x="390" y="505" class="lbl-bold" style="fill:#a6e3a1; font-size:16px;">CONTROLADOR DE SEGURIDAD ESP32</text>
  <text x="390" y="530" class="lbl">• Batería de Respaldo Li-Ion 18650 (Cierre garantizado aún sin luz)</text>
  <text x="390" y="550" class="lbl">• Sirena piezoeléctrica local de 85 dB en cocina y cuarto técnico</text>
  <text x="390" y="570" class="lbl">• Disparo de relé por interrupción física directa en menos de 100 ms</text>
  <text x="390" y="590" class="lbl">• Notificación crítica inmediata a celulares mediante Home Assistant</text>

  <!-- Cables de Señal hacia Válvulas -->
  <line x1="500" y1="470" x2="500" y2="370" class="wire-ctrl"/>
  <line x1="500" y1="290" x2="500" y2="220" class="wire-ctrl"/>

  <!-- Cables de Sensores -->
  <line x1="740" y1="520" x2="805" y2="520" class="wire-ctrl"/>
  <line x1="805" y1="520" x2="805" y2="360" class="wire-ctrl"/>
  <line x1="805" y1="300" x2="805" y2="210" class="wire-ctrl"/>

</svg>
"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Esquema de corte de válvulas generado: DXF={dxf_path}, SVG={svg_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dxf_target = os.path.join(base_dir, "03_seguridad_y_control_acceso/03_actuadores_valvulas_gas_agua/mecanico/esquema_corte_valvulas_gas_agua.dxf")
    svg_target = os.path.join(base_dir, "03_seguridad_y_control_acceso/03_actuadores_valvulas_gas_agua/mecanico/esquema_corte_valvulas_gas_agua.svg")
    generar_esquema_valvulas_corte(dxf_target, svg_target)
