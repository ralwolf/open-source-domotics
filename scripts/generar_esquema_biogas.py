#!/usr/bin/env python3
"""
Generador del Esquema P&ID del Biodigestor Séptico, Depuración de Biogás y Generador Dual
Formatos de salida: DXF y SVG vectorial
Proyecto: open-source-domotics
"""

import os
from generar_planos_dxf import SimpleDXF

def generar_esquema_biogas(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_ROTULO", color=7)
    dxf.add_layer("BIODIGESTOR_REACTOR", color=3)
    dxf.add_layer("LINEAS_BIOGAS", color=1)
    dxf.add_layer("FILTROS_Y_EQUIPOS", color=4)
    dxf.add_layer("GENERADOR_ATS", color=2)
    dxf.add_layer("TEXTO_NOTAS", color=7)

    # Marco y Cajetín A3
    dxf.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf.add_rect(230, 10, 180, 42, layer="MARCO_ROTULO")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", 235, 42, height=4.0, layer="TEXTO_NOTAS")
    dxf.add_text("P&ID BIODIGESTOR SÉPTICO, BIOGÁS Y GENERADOR DUAL", 235, 32, height=2.2, layer="TEXTO_NOTAS")
    dxf.add_text("Depuración H2S + Trampa Condensado + Parallamas + Motogenerador 5 kW", 235, 22, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Arranque automático ATS en contingencia o baja carga ESS", 235, 14, height=1.4, layer="TEXTO_NOTAS")

    # 1. Entrada Aguas Negras y Reactor Biodigestor (1500 L)
    dxf.add_rect(15, 160, 40, 40, layer="BIODIGESTOR_REACTOR")
    dxf.add_text("ENTRADA", 18, 190, height=1.8, layer="TEXTO_NOTAS")
    dxf.add_text("Aguas Negras", 18, 180, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("PVC 110 mm", 18, 170, height=1.4, layer="TEXTO_NOTAS")

    dxf.add_line(55, 180, 75, 180, layer="BIODIGESTOR_REACTOR")

    # Tanque Biodigestor
    dxf.add_rect(75, 120, 65, 120, layer="BIODIGESTOR_REACTOR")
    dxf.add_text("BIODIGESTOR", 80, 230, height=2.2, layer="TEXTO_NOTAS")
    dxf.add_text("Anaeróbico 1500 L", 80, 218, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Cámara de Digestión", 80, 180, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("Fondo cónico lodos", 80, 150, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("Purga lodos mineralizados", 80, 130, height=1.3, layer="TEXTO_NOTAS")

    # Salida Efluente Líquido (Biol para jardín)
    dxf.add_line(140, 160, 165, 160, layer="BIODIGESTOR_REACTOR")
    dxf.add_text("Biol Clarificado", 142, 165, height=1.3, layer="TEXTO_NOTAS")

    # Salida Superior de Biogás hacia Trampa de Condensado
    dxf.add_line(107, 240, 107, 260, layer="LINEAS_BIOGAS")
    dxf.add_line(107, 260, 160, 260, layer="LINEAS_BIOGAS")
    dxf.add_text("Biogás Bruto (CH4 65% + CO2 32% + H2S)", 110, 265, height=1.4, layer="TEXTO_NOTAS")

    # 2. Trampa de Condensados (Water Trap con Sifón)
    dxf.add_rect(160, 235, 30, 45, layer="FILTROS_Y_EQUIPOS")
    dxf.add_text("TRAMPA", 163, 270, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Condensados", 163, 260, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("Purga agua", 163, 245, height=1.3, layer="TEXTO_NOTAS")

    dxf.add_line(190, 260, 210, 260, layer="LINEAS_BIOGAS")

    # 3. Columna de Desulfuración (Filtro de Viruta de Hierro Fe2O3)
    dxf.add_rect(210, 220, 35, 65, layer="FILTROS_Y_EQUIPOS")
    dxf.add_text("DESULFURADOR", 212, 275, height=1.6, layer="TEXTO_NOTAS")
    dxf.add_text("Filtro Fe2O3", 212, 265, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("Eliminación H2S", 212, 250, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("< 10 ppm", 212, 235, height=1.3, layer="TEXTO_NOTAS")

    dxf.add_line(245, 260, 265, 260, layer="LINEAS_BIOGAS")

    # 4. Gasómetro / Pulmón Flexible de Almacenamiento (2 m³)
    dxf.add_rect(265, 220, 45, 65, layer="FILTROS_Y_EQUIPOS")
    dxf.add_text("GASÓMETRO", 268, 275, height=1.8, layer="TEXTO_NOTAS")
    dxf.add_text("Pulmón 2000 L", 268, 265, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("Membrana PVC", 268, 250, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("P: 15-25 mbar", 268, 235, height=1.3, layer="TEXTO_NOTAS")

    dxf.add_line(310, 260, 330, 260, layer="LINEAS_BIOGAS")

    # 5. Seguridad: Manómetro + Válvula Alivio + Parallamas ATEX
    dxf.add_rect(330, 235, 30, 45, layer="FILTROS_Y_EQUIPOS")
    dxf.add_text("SEGURIDAD", 333, 272, height=1.5, layer="TEXTO_NOTAS")
    dxf.add_text("Parallamas", 333, 262, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("Alivio 35mbar", 333, 250, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("EV Corte ATEX", 333, 240, height=1.3, layer="TEXTO_NOTAS")

    dxf.add_line(360, 260, 380, 260, layer="LINEAS_BIOGAS")
    dxf.add_line(380, 260, 380, 180, layer="LINEAS_BIOGAS")

    # 6. Motogenerador Dual 5 kW (Biogás / Gasolina)
    dxf.add_rect(330, 110, 75, 70, layer="GENERADOR_ATS")
    dxf.add_text("GENERADOR DUAL 5 kW", 335, 170, height=2.0, layer="TEXTO_NOTAS")
    dxf.add_text("Carburador GLP/Biogás", 335, 158, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("+ Gasolina de Reserva", 335, 146, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("230V 50Hz Monofásico", 335, 134, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("Arranque Eléctrico 12V", 335, 120, height=1.4, layer="TEXTO_NOTAS")

    # Salida AC hacia ATS / Cuadro General
    dxf.add_line(330, 130, 270, 130, layer="GENERADOR_ATS")
    dxf.add_rect(210, 110, 60, 50, layer="GENERADOR_ATS")
    dxf.add_text("TABLERO ATS", 215, 150, height=1.8, layer="TEXTO_NOTAS")
    dxf.add_text("Conmutación Autom.", 215, 140, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("Inversor / Generador", 215, 128, height=1.3, layer="TEXTO_NOTAS")
    dxf.add_text("Enclavamiento Eléc.", 215, 118, height=1.2, layer="TEXTO_NOTAS")

    # 7. Cuadro de Automatización ESP32 (Zona Segura)
    dxf.add_rect(15, 20, 185, 85, layer="FILTROS_Y_EQUIPOS")
    dxf.add_text("CONTROL Y TELEMETRÍA BIOGÁS (ESP32 IoT)", 20, 95, height=2.0, layer="TEXTO_NOTAS")
    dxf.add_text("• Sensor de Presión Piezorresistivo 0-50 mbar (4-20mA)", 20, 83, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("• Sensor de Gas Metano MQ-4 / Catalítico con barrera zener", 20, 73, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("• Contactos secos de arranque / parada de generador (Start/Stop)", 20, 63, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("• Corte automático de válvula ATEX ante fuga o sobrepresión", 20, 53, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("• Telemetría de producción estimada de biometano a Home Assistant", 20, 43, height=1.4, layer="TEXTO_NOTAS")
    dxf.add_text("• Cargador flotante 12V para batería de arranque del motor", 20, 33, height=1.4, layer="TEXTO_NOTAS")

    dxf.save()
    print(f"DXF P&ID biogás guardado en: {dxf_path}")

    # 2. GENERACIÓN SVG
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 850" width="100%" height="100%" style="background-color: #0c141f; font-family: monospace, sans-serif;">
  <rect x="20" y="20" width="1160" height="810" fill="none" stroke="#1e293b" stroke-width="2" rx="8" />

  <!-- Cajetin -->
  <rect x="680" y="730" width="480" height="80" fill="#152132" stroke="#eab308" stroke-width="2" rx="4" />
  <text x="700" y="755" fill="#facc15" font-size="16" font-weight="bold">OPEN-SOURCE-DOMOTICS</text>
  <text x="700" y="775" fill="#f8fafc" font-size="13" font-weight="bold">P&amp;ID BIODIGESTOR SÉPTICO, BIOGÁS Y GENERADOR DUAL</text>
  <text x="700" y="795" fill="#94a3b8" font-size="11">Depuración H2S + Trampa Condensado + Parallamas + Motogenerador 5 kW</text>

  <!-- Entrada Aguas Negras -->
  <g transform="translate(40, 200)">
    <rect x="0" y="0" width="110" height="120" fill="#1e293b" stroke="#64748b" stroke-width="2" rx="6" />
    <text x="12" y="25" fill="#f8fafc" font-size="12" font-weight="bold">ENTRADA AFLUENTE</text>
    <text x="12" y="45" fill="#94a3b8" font-size="11">Aguas Negras</text>
    <text x="12" y="65" fill="#94a3b8" font-size="11">+ Residuos Org.</text>
    <text x="12" y="90" fill="#cbd5e1" font-size="11">PVC 110 mm</text>
  </g>

  <path d="M 150 260 L 210 260" stroke="#64748b" stroke-width="8" fill="none" />

  <!-- Reactor Biodigestor -->
  <g transform="translate(210, 140)">
    <rect x="0" y="0" width="160" height="260" fill="#1e293b" stroke="#10b981" stroke-width="2.5" rx="8" />
    <text x="15" y="30" fill="#34d399" font-size="14" font-weight="bold">BIODIGESTOR</text>
    <text x="15" y="55" fill="#f8fafc" font-size="12">Anaeróbico 1500 L</text>
    <text x="15" y="80" fill="#94a3b8" font-size="11">Cámara de Digestión</text>
    <text x="15" y="100" fill="#94a3b8" font-size="11">Temperatura óptima: 35°C</text>
    
    <path d="M 20 180 L 140 180" stroke="#334155" stroke-width="2" />
    <text x="15" y="210" fill="#cbd5e1" font-size="11">Fondo cónico lodos</text>
    <text x="15" y="235" fill="#22c55e" font-size="10">Salida Biol Fertilizante</text>
  </g>

  <!-- Salida Biogas Superior -->
  <path d="M 290 140 L 290 90 L 410 90" stroke="#eab308" stroke-width="6" fill="none" />
  <text x="300" y="80" fill="#facc15" font-size="11" font-weight="bold">Línea Biogás Bruto (CH4 65%)</text>

  <!-- Trampa de Condensado -->
  <g transform="translate(410, 40)">
    <rect x="0" y="0" width="90" height="110" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="6" />
    <text x="10" y="25" fill="#38bdf8" font-size="11" font-weight="bold">TRAMPA AGUA</text>
    <text x="10" y="45" fill="#f8fafc" font-size="10">Condensados</text>
    <text x="10" y="70" fill="#94a3b8" font-size="10">Sifón U</text>
    <text x="10" y="95" fill="#22c55e" font-size="9">Purga manual</text>
  </g>

  <path d="M 500 90 L 550 90" stroke="#eab308" stroke-width="6" fill="none" />

  <!-- Filtro Desulfurador H2S -->
  <g transform="translate(550, 40)">
    <rect x="0" y="0" width="110" height="110" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="6" />
    <text x="10" y="25" fill="#fbbf24" font-size="11" font-weight="bold">DESULFURADOR</text>
    <text x="10" y="45" fill="#f8fafc" font-size="10">Viruta Fe2O3</text>
    <text x="10" y="70" fill="#94a3b8" font-size="10">Elimina H2S</text>
    <text x="10" y="95" fill="#4ade80" font-size="9">&lt; 10 ppm (anti-ácido)</text>
  </g>

  <path d="M 660 90 L 710 90" stroke="#eab308" stroke-width="6" fill="none" />

  <!-- Gasometro Flexible -->
  <g transform="translate(710, 40)">
    <rect x="0" y="0" width="130" height="110" fill="#1e293b" stroke="#a855f7" stroke-width="2" rx="6" />
    <text x="12" y="25" fill="#c084fc" font-size="12" font-weight="bold">GASÓMETRO</text>
    <text x="12" y="45" fill="#f8fafc" font-size="11">Pulmón 2000 L</text>
    <text x="12" y="70" fill="#94a3b8" font-size="10">Presión: 20 mbar</text>
    <text x="12" y="95" fill="#cbd5e1" font-size="10">Membrana estanca</text>
  </g>

  <path d="M 840 90 L 890 90" stroke="#eab308" stroke-width="6" fill="none" />

  <!-- Valvulas de Seguridad y Parallamas -->
  <g transform="translate(890, 40)">
    <rect x="0" y="0" width="120" height="110" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="6" />
    <text x="10" y="25" fill="#f87171" font-size="11" font-weight="bold">SEGURIDAD</text>
    <text x="10" y="45" fill="#f8fafc" font-size="10">Parallamas Inox</text>
    <text x="10" y="65" fill="#facc15" font-size="10">Alivio: 35 mbar</text>
    <text x="10" y="85" fill="#ef4444" font-size="10">EV Corte ATEX</text>
    <text x="10" y="100" fill="#94a3b8" font-size="9">NC Fail-safe</text>
  </g>

  <path d="M 1010 90 L 1050 90 L 1050 280 L 980 280" stroke="#eab308" stroke-width="6" fill="none" />

  <!-- Motogenerador Dual 5 kW -->
  <g transform="translate(760, 230)">
    <rect x="0" y="0" width="220" height="170" fill="#1e293b" stroke="#f43f5e" stroke-width="2.5" rx="8" />
    <text x="15" y="30" fill="#fb7185" font-size="14" font-weight="bold">GENERADOR DUAL 5 kW</text>
    <text x="15" y="55" fill="#f8fafc" font-size="12">Biogás + Gasolina</text>
    <text x="15" y="75" fill="#94a3b8" font-size="11">Motor 4T OHV 389cc</text>
    <text x="15" y="95" fill="#94a3b8" font-size="11">Carburador bi-combustible</text>
    <text x="15" y="120" fill="#cbd5e1" font-size="11">Salida: 230V~ 50Hz</text>
    <text x="15" y="145" fill="#22c55e" font-size="11">Arranque automático 12V</text>
  </g>

  <!-- Linea AC hacia Tablero ATS -->
  <path d="M 760 315 L 680 315" stroke="#38bdf8" stroke-width="4" fill="none" />

  <!-- Tablero ATS -->
  <g transform="translate(500, 240)">
    <rect x="0" y="0" width="180" height="150" fill="#0f172a" stroke="#38bdf8" stroke-width="2" rx="6" />
    <text x="15" y="30" fill="#38bdf8" font-size="13" font-weight="bold">TABLERO ATS</text>
    <text x="15" y="55" fill="#f8fafc" font-size="11">Transferencia Automática</text>
    <text x="15" y="75" fill="#94a3b8" font-size="10">Inversor Solar &lt;-&gt; Generador</text>
    <text x="15" y="100" fill="#e2e8f0" font-size="10">Enclavamiento Eléc. / Mec.</text>
    <text x="15" y="125" fill="#4ade80" font-size="10">Arranque por contacto seco</text>
  </g>

  <!-- Cuadro Inferior: Logica del Controlador ESP32 -->
  <g transform="translate(40, 480)">
    <rect x="0" y="0" width="600" height="220" fill="#152132" stroke="#10b981" stroke-width="2" rx="6" />
    <text x="25" y="35" fill="#34d399" font-size="15" font-weight="bold">CONTROLADOR INTELIGENTE BIOGÁS &amp; ATS (ESP32 / VLAN 30)</text>
    
    <text x="25" y="70" fill="#cbd5e1" font-size="11">• Transmisor de presión 0-50 mbar con lectura analógica 4-20mA</text>
    <text x="25" y="95" fill="#cbd5e1" font-size="11">• Detector de gas metano MQ-4 calibrado en cámara con aislamiento galvánico</text>
    <text x="25" y="120" fill="#cbd5e1" font-size="11">• Secuencia de arranque: Ignición ON -&gt; Choke motorizado -&gt; Pulso Starter 4s</text>
    <text x="25" y="145" fill="#cbd5e1" font-size="11">• Interbloqueo de seguridad: Corte instantáneo de gas ante llama apagada</text>
    <text x="25" y="170" fill="#cbd5e1" font-size="11">• Algoritmo ESS Low Battery: Arranca grupo si SoC de baterías LiFePO4 &lt; 20%</text>
    <text x="25" y="195" fill="#38bdf8" font-size="11">• Estimación volumétrica de biometano generado y horas de autonomía en HA</text>
  </g>
</svg>"""

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"SVG P&ID biogás guardado en: {svg_path}")

if __name__ == "__main__":
    dxf_out = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/05_biodigestor_biogas_generador/mecanico/esquema_biogas_generador.dxf"
    svg_out = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/05_biodigestor_biogas_generador/mecanico/esquema_biogas_generador.svg"
    generar_esquema_biogas(dxf_out, svg_out)

