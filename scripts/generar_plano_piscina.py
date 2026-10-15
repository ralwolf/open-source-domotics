#!/usr/bin/env python3
"""
Generador de Plano Hidráulico P&ID y Esquema de Filtración de Piscina
Formatos de salida: DXF (AutoCAD R12) y SVG vectorial
Módulo: 05_confort_y_exteriores/04_mantenimiento_automatizado_piscina/mecanico
"""

import os
import sys

# Asegurar path para importar SimpleDXF
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generar_planos_dxf import SimpleDXF

def generar_plano_piscina(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_ROTULO", color=7)
    dxf.add_layer("TUBERIAS_PVC", color=4)
    dxf.add_layer("EQUIPOS_FILTRACION", color=3)
    dxf.add_layer("VALVULAS_ACCESORIOS", color=1)
    dxf.add_layer("SENSORES_ANALISIS", color=2)
    dxf.add_layer("DOSIFICACION_QUIMICA", color=6)
    dxf.add_layer("TEXTO_NOTAS", color=7)

    # Marco y Cajetín A3 (420 x 297 mm)
    dxf.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf.add_rect(210, 10, 200, 45, layer="MARCO_ROTULO")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", 215, 45, height=4.0, layer="TEXTO_NOTAS")
    dxf.add_text("ESQUEMA P&ID: FILTRACION, QUIMICA Y CLIMATIZACION PISCINA", 215, 36, height=2.0, layer="TEXTO_NOTAS")
    dxf.add_text("Bomba 1CV 11 m3/h | Filtro Arena D500 | Bypass pH/ORP | Climatizacion Solar", 215, 26, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Inyeccion Peristaltica pH-/Cloro | Interbloqueo Flujo | Tuberia PVC D50 PN10", 215, 16, height=1.4, layer="TEXTO_NOTAS")

    # Diagrama de Vasos y Colectores
    # Piscina representada a la izquierda (X=20 a 90, Y=100 a 250)
    dxf.add_rect(20, 100, 75, 160, layer="EQUIPOS_FILTRACION")
    dxf.add_text("VASO PISCINA (8 x 4 x 1.5 m)", 25, 250, height=2.2, layer="TEXTO_NOTAS")
    dxf.add_text("Volumen: 48.000 Litros", 25, 240, height=1.8, layer="TEXTO_NOTAS")
    dxf.add_text("Recirculacion: 4.5 horas", 25, 232, height=1.6, layer="TEXTO_NOTAS")

    # Elementos en el vaso: Skimmers, Sumidero Fondo, Impulsores
    dxf.add_rect(20, 210, 10, 15, layer="VALVULAS_ACCESORIOS")
    dxf.add_text("SK-1", 22, 216, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_rect(20, 160, 10, 15, layer="VALVULAS_ACCESORIOS")
    dxf.add_text("SK-2", 22, 166, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_rect(20, 110, 12, 12, layer="VALVULAS_ACCESORIOS")
    dxf.add_text("Fondo", 21, 114, height=1.4, layer="TEXTO_NOTAS")

    # Líneas de aspiración hacia la Caseta Técnica
    # Colector de aspiración (X=95 a 130)
    dxf.add_line(30, 217, 125, 217, layer="TUBERIAS_PVC")
    dxf.add_line(30, 167, 125, 167, layer="TUBERIAS_PVC")
    dxf.add_line(32, 116, 125, 116, layer="TUBERIAS_PVC")

    dxf.add_line(125, 217, 125, 116, layer="TUBERIAS_PVC")
    dxf.add_text("Colector Aspiracion DN50", 95, 222, height=1.5, layer="TEXTO_NOTAS")

    # Bomba Autoaspirante (X=145, Y=150)
    dxf.add_line(125, 167, 145, 167, layer="TUBERIAS_PVC")
    dxf.add_circle(155, 167, 10, layer="EQUIPOS_FILTRACION")
    dxf.add_rect(165, 160, 15, 14, layer="EQUIPOS_FILTRACION")
    dxf.add_text("BOMBA 1 CV", 146, 182, height=1.8, layer="TEXTO_NOTAS")
    dxf.add_text("0.75 kW - 11 m3/h", 146, 148, height=1.4, layer="TEXTO_NOTAS")

    # Tubería de impulsión de bomba hacia Válvula Selectora y Filtro
    dxf.add_line(180, 167, 210, 167, layer="TUBERIAS_PVC")
    dxf.add_line(210, 167, 210, 200, layer="TUBERIAS_PVC")

    # Válvula de 6 vías y Filtro de Arena (X=210 a 245, Y=190 a 250)
    dxf.add_circle(210, 205, 8, layer="VALVULAS_ACCESORIOS")
    dxf.add_text("6-VIAS", 204, 216, height=1.4, layer="TEXTO_NOTAS")

    dxf.add_circle(235, 205, 16, layer="EQUIPOS_FILTRACION")
    dxf.add_text("FILTRO D500", 222, 225, height=1.8, layer="TEXTO_NOTAS")
    dxf.add_text("Lecho Vidrio Activo", 222, 182, height=1.4, layer="TEXTO_NOTAS")

    # Salida filtrada hacia Bypass de Análisis y Tratamiento
    dxf.add_line(210, 213, 210, 240, layer="TUBERIAS_PVC")
    dxf.add_line(210, 240, 260, 240, layer="TUBERIAS_PVC")

    # Cámara de Bypass para Sondas pH y ORP (Derivación superior X=260 a 320, Y=260)
    dxf.add_line(270, 240, 270, 265, layer="SENSORES_ANALISIS")
    dxf.add_line(270, 265, 320, 265, layer="SENSORES_ANALISIS")
    dxf.add_line(320, 265, 320, 240, layer="SENSORES_ANALISIS")
    dxf.add_rect(280, 258, 30, 14, layer="SENSORES_ANALISIS")
    dxf.add_text("VASO BYPASS ANALISIS", 278, 275, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Sonda pH (BNC)", 282, 268, height=1.3, layer="SENSORES_ANALISIS")
    dxf.add_text("Sonda ORP (BNC)", 282, 261, height=1.3, layer="SENSORES_ANALISIS")

    # Sensor de flujo magnético (Flow Switch) en línea principal
    dxf.add_rect(275, 236, 12, 8, layer="SENSORES_ANALISIS")
    dxf.add_text("FLOW-SW", 273, 230, height=1.4, layer="TEXTO_NOTAS")

    # Collarines de Inyección de Químicos (pH- y Cloro)
    dxf.add_circle(335, 240, 4, layer="DOSIFICACION_QUIMICA")
    dxf.add_text("Inyector pH-", 325, 248, height=1.4, layer="DOSIFICACION_QUIMICA")
    dxf.add_circle(355, 240, 4, layer="DOSIFICACION_QUIMICA")
    dxf.add_text("Inyector Cloro", 345, 248, height=1.4, layer="DOSIFICACION_QUIMICA")

    # Intercambiador de Calor Solar / Climatización (X=330 a 375, Y=160 a 195)
    dxf.add_line(370, 240, 370, 180, layer="TUBERIAS_PVC")
    dxf.add_rect(350, 160, 40, 25, layer="EQUIPOS_FILTRACION")
    dxf.add_text("INTERCAMBIADOR SOLAR", 348, 190, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Titanio 40 kW (Piso Rad)", 348, 152, height=1.3, layer="TEXTO_NOTAS")

    # Retorno hacia boquillas de impulsión de la piscina
    dxf.add_line(370, 160, 370, 90, layer="TUBERIAS_PVC")
    dxf.add_line(370, 90, 85, 90, layer="TUBERIAS_PVC")
    dxf.add_line(85, 90, 85, 115, layer="TUBERIAS_PVC")
    dxf.add_text("Retorno Impulsion 3x Boquillas D50", 160, 83, height=1.6, layer="TEXTO_NOTAS")

    # Bombas Peristálticas y Depósitos de Químicos (Zona Inferior X=260 a 330, Y=105 a 140)
    dxf.add_rect(260, 105, 22, 25, layer="DOSIFICACION_QUIMICA")
    dxf.add_text("Bomba pH-", 261, 134, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("1.5 L/h 24V", 261, 112, height=1.2, layer="TEXTO_NOTAS")

    dxf.add_rect(295, 105, 22, 25, layer="DOSIFICACION_QUIMICA")
    dxf.add_text("Bomba Cloro", 296, 134, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("1.5 L/h 24V", 296, 112, height=1.2, layer="TEXTO_NOTAS")

    # Líneas de inyección flexibles teflón
    dxf.add_line(271, 130, 335, 236, layer="DOSIFICACION_QUIMICA")
    dxf.add_line(306, 130, 355, 236, layer="DOSIFICACION_QUIMICA")

    dxf.save()

    # 2. GENERACIÓN SVG VECTORIAL
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 297" width="100%" height="100%" style="background-color: #171b24; font-family: monospace;">
  <defs>
    <style>
      .marco {{ stroke: #455066; stroke-width: 1.0; fill: none; }}
      .vaso {{ stroke: #00b4d8; stroke-width: 1.8; fill: rgba(0, 180, 216, 0.15); }}
      .tubo-pvc {{ stroke: #48cae4; stroke-width: 1.6; fill: none; }}
      .tubo-retorno {{ stroke: #0077b6; stroke-width: 1.6; fill: none; stroke-dasharray: 4,2; }}
      .equipo {{ stroke: #52b788; stroke-width: 1.4; fill: #1f3328; }}
      .sensor {{ stroke: #ffd166; stroke-width: 1.2; fill: #332d18; }}
      .quimica {{ stroke: #ef476f; stroke-width: 1.2; fill: #381b25; }}
      .txt-title {{ fill: #ffffff; font-size: 4px; font-weight: bold; }}
      .txt-sub {{ fill: #00f0ff; font-size: 2.2px; font-weight: bold; }}
      .txt-body {{ fill: #cad2c5; font-size: 1.6px; }}
      .txt-tag {{ fill: #ffbe0b; font-size: 1.4px; font-weight: bold; }}
      .txt-alert {{ fill: #ff4d6d; font-size: 1.4px; }}
    </style>
  </defs>

  <!-- Marco A3 -->
  <rect x="5" y="5" width="410" height="287" class="marco"/>
  <rect x="210" y="242" width="200" height="45" class="marco"/>
  <text x="215" y="254" class="txt-title">OPEN-SOURCE-DOMOTICS</text>
  <text x="215" y="262" class="txt-sub">ESQUEMA P&amp;ID: FILTRACIÓN, QUÍMICA Y CLIMATIZACIÓN PISCINA</text>
  <text x="215" y="271" class="txt-body">Bomba 1CV 11 m³/h | Filtro Arena D500 | Bypass pH/ORP | Climatización Solar</text>
  <text x="215" y="279" class="txt-body">Inyección Peristáltica pH-/Cloro | Interbloqueo Flujo | Tubería PVC D50 PN10</text>

  <!-- Vaso Piscina -->
  <g id="piscina">
    <rect x="20" y="40" width="75" height="160" class="vaso" rx="3"/>
    <text x="25" y="55" class="txt-sub">VASO PISCINA</text>
    <text x="25" y="65" class="txt-body">8.0 x 4.0 x 1.5 m</text>
    <text x="25" y="73" class="txt-body">Vol: 48.000 L (48 m³)</text>
    <text x="25" y="81" class="txt-body">Recirc: 4.36 h a 11 m³/h</text>

    <!-- Skimmers y Sumidero -->
    <rect x="85" y="60" width="10" height="15" fill="#0077b6" stroke="#48cae4"/>
    <text x="68" y="71" class="txt-tag">SK-1</text>
    <rect x="85" y="110" width="10" height="15" fill="#0077b6" stroke="#48cae4"/>
    <text x="68" y="121" class="txt-tag">SK-2</text>
    <rect x="85" y="160" width="10" height="12" fill="#023e8a" stroke="#48cae4"/>
    <text x="62" y="169" class="txt-tag">Fondo</text>
  </g>

  <!-- Colector Aspiración y Bomba -->
  <g id="filtracion">
    <line x1="95" y1="67" x2="125" y2="67" class="tubo-pvc"/>
    <line x1="95" y1="117" x2="125" y2="117" class="tubo-pvc"/>
    <line x1="95" y1="166" x2="125" y2="166" class="tubo-pvc"/>
    <line x1="125" y1="67" x2="125" y2="166" class="tubo-pvc"/>
    <line x1="125" y1="117" x2="145" y2="117" class="tubo-pvc"/>

    <!-- Bomba -->
    <circle cx="155" cy="117" r="10" class="equipo"/>
    <rect x="165" y="110" width="15" height="14" class="equipo"/>
    <text x="142" y="100" class="txt-sub">BOMBA 1 CV</text>
    <text x="142" y="137" class="txt-body">0.75 kW - 11 m³/h</text>

    <!-- Impulsión a Filtro -->
    <line x1="180" y1="117" x2="210" y2="117" class="tubo-pvc"/>
    <line x1="210" y1="117" x2="210" y2="85" class="tubo-pvc"/>

    <!-- Válvula 6 vías y Filtro -->
    <circle cx="210" cy="78" r="8" fill="#2b2d42" stroke="#ef233c"/>
    <text x="202" y="81" class="txt-alert" font-size="2">6-VÍAS</text>

    <circle cx="240" cy="78" r="18" class="equipo"/>
    <text x="228" y="75" class="txt-sub">FILTRO D500</text>
    <text x="228" y="83" class="txt-body">Vidrio Activo AFM</text>

    <!-- Salida Filtrada -->
    <line x1="210" y1="70" x2="210" y2="50" class="tubo-pvc"/>
    <line x1="210" y1="50" x2="265" y2="50" class="tubo-pvc"/>
  </g>

  <!-- Sistema de Análisis en Bypass y Dosificación -->
  <g id="quimica_analisis">
    <!-- Bypass -->
    <line x1="270" y1="50" x2="270" y2="30" class="sensor"/>
    <line x1="270" y1="30" x2="320" y2="30" class="sensor"/>
    <line x1="320" y1="30" x2="320" y2="50" class="sensor"/>
    <rect x="280" y="22" width="32" height="16" class="sensor" rx="2"/>
    <text x="283" y="30" class="txt-tag">VASO BYPASS</text>
    <text x="283" y="36" class="txt-body">• Sonda pH (BNC)</text>
    <text x="283" y="42" class="txt-body">• Sonda ORP (BNC)</text>

    <!-- Flow Switch -->
    <rect x="275" y="46" width="14" height="8" class="sensor"/>
    <text x="276" y="52" class="txt-tag">FLOW</text>

    <!-- Puntos de inyección -->
    <line x1="265" y1="50" x2="370" y2="50" class="tubo-pvc"/>
    <circle cx="335" cy="50" r="4" class="quimica"/>
    <text x="325" y="60" class="txt-alert">Inyector pH-</text>
    <circle cx="355" cy="50" r="4" class="quimica"/>
    <text x="345" y="68" class="txt-alert">Inyector Cloro</text>

    <!-- Bombas peristálticas -->
    <rect x="260" y="160" width="25" height="28" class="quimica" rx="2"/>
    <text x="262" y="172" class="txt-sub">PERIST. 1</text>
    <text x="262" y="180" class="txt-body">pH- (Ácido)</text>
    <text x="262" y="186" class="txt-body">1.5 L/h 24V</text>

    <rect x="295" y="160" width="25" height="28" class="quimica" rx="2"/>
    <text x="297" y="172" class="txt-sub">PERIST. 2</text>
    <text x="297" y="180" class="txt-body">Cloro / Redox</text>
    <text x="297" y="186" class="txt-body">1.5 L/h 24V</text>

    <!-- Mangueras PTFE inyección -->
    <line x1="272" y1="160" x2="335" y2="54" stroke="#ff4d6d" stroke-width="1.0" stroke-dasharray="2,2"/>
    <line x1="307" y1="160" x2="355" y2="54" stroke="#ffbe0b" stroke-width="1.0" stroke-dasharray="2,2"/>
  </g>

  <!-- Climatización Solar e Impulsión Final -->
  <g id="climatizacion">
    <line x1="370" y1="50" x2="370" y2="105" class="tubo-pvc"/>
    <rect x="350" y="105" width="40" height="28" class="equipo" rx="2"/>
    <text x="353" y="117" class="txt-sub">INTERCAMBIADOR</text>
    <text x="353" y="125" class="txt-body">Titanio 40 kW</text>
    <text x="353" y="131" class="txt-body">Primario Solar Térmico</text>

    <!-- Retorno impulsión hacia la piscina -->
    <line x1="370" y1="133" x2="370" y2="210" class="tubo-retorno"/>
    <line x1="370" y1="210" x2="55" y2="210" class="tubo-retorno"/>
    <line x1="55" y1="210" x2="55" y2="200" class="tubo-retorno"/>
    <circle cx="55" cy="200" r="3" fill="#00f0ff"/>
    <text x="140" y="218" class="txt-sub">RETORNO IMPULSIÓN (3x Boquillas Orientables DN50)</text>
  </g>
</svg>
"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Plano CAD 2D DXF generado en: {dxf_path}")
    print(f"Plano vectorial SVG generado en: {svg_path}")

if __name__ == "__main__":
    dxf_out = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/04_mantenimiento_automatizado_piscina/mecanico/plano_hidraulico_piscina.dxf"
    svg_out = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/04_mantenimiento_automatizado_piscina/mecanico/plano_hidraulico_piscina.svg"
    generar_plano_piscina(dxf_out, svg_out)
