#!/usr/bin/env python3
"""
Generador del Esquema Eléctrico y de Control del Cargador EV Wallbox Inteligente (IEC 61851)
Formatos de salida: DXF y SVG vectorial
Proyecto: open-source-domotics
"""

import os
from generar_planos_dxf import SimpleDXF

def generar_diagrama_ev_wallbox(dxf_path, svg_path):
    os.makedirs(os.path.dirname(os.path.abspath(dxf_path)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(svg_path)), exist_ok=True)

    # 1. GENERACIÓN DXF
    dxf = SimpleDXF(dxf_path)
    dxf.add_layer("MARCO_ROTULO", color=7)
    dxf.add_layer("LINEAS_POTENCIA_AC", color=1)
    dxf.add_layer("LINEAS_NEUTRO", color=5)
    dxf.add_layer("LINEAS_TIERRA_PE", color=3)
    dxf.add_layer("SEÑALES_CONTROL_PILOT", color=2)
    dxf.add_layer("MODULOS_PROTECCION", color=4)
    dxf.add_layer("TEXTO_ROTULOS", color=7)

    # Marco y Cajetín A3
    dxf.add_rect(0, 0, 420, 297, layer="MARCO_ROTULO")
    dxf.add_rect(5, 5, 410, 287, layer="MARCO_ROTULO")
    dxf.add_rect(230, 10, 180, 40, layer="MARCO_ROTULO")
    dxf.add_text("OPEN-SOURCE-DOMOTICS", 235, 38, height=4.0, layer="TEXTO_ROTULOS")
    dxf.add_text("ESQUEMA ELÉCTRICO Y DE CONTROL - EV WALLBOX 32A (7.4 kW)", 235, 28, height=2.2, layer="TEXTO_ROTULOS")
    dxf.add_text("IEC 61851-1 / SAE J1772 + Modbus RS485 + Balanceo Solar Dinámico", 235, 18, height=1.7, layer="TEXTO_ROTULOS")

    # 1. Entrada de Red / Acometida desde Cuadro General (TGBT)
    dxf.add_rect(15, 180, 35, 80, layer="MODULOS_PROTECCION")
    dxf.add_text("ALIMENTACIÓN", 17, 245, height=2.0, layer="TEXTO_ROTULOS")
    dxf.add_text("230V~ 50Hz", 17, 235, height=1.8, layer="TEXTO_ROTULOS")
    dxf.add_text("3x10 mm² Cu", 17, 220, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Tubo rígido M32", 17, 200, height=1.5, layer="TEXTO_ROTULOS")

    # Líneas de Potencia hacia Protecciones
    # L1 (Fase)
    dxf.add_line(50, 240, 75, 240, layer="LINEAS_POTENCIA_AC")
    dxf.add_text("L1 (Fase)", 52, 242, height=1.4, layer="TEXTO_ROTULOS")
    # N (Neutro)
    dxf.add_line(50, 210, 75, 210, layer="LINEAS_NEUTRO")
    dxf.add_text("N (Neutro)", 52, 212, height=1.4, layer="TEXTO_ROTULOS")
    # PE (Tierra)
    dxf.add_line(50, 190, 345, 190, layer="LINEAS_TIERRA_PE")
    dxf.add_text("PE (Tierra de Protección 10 mm²)", 120, 192, height=1.4, layer="TEXTO_ROTULOS")

    # 2. Bloque de Protecciones (MCB 40A + RCD Tipo B / 6mA DC)
    dxf.add_rect(75, 180, 50, 80, layer="MODULOS_PROTECCION")
    dxf.add_text("DISYUNTOR MCB", 78, 250, height=1.8, layer="TEXTO_ROTULOS")
    dxf.add_text("2P C40A 10kA", 78, 240, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("DIFERENCIAL RCD", 78, 220, height=1.8, layer="TEXTO_ROTULOS")
    dxf.add_text("Tipo B / 30mA AC", 78, 210, height=1.5, layer="TEXTO_ROTULOS")
    dxf.add_text("+ 6mA DC (IEC 62955)", 78, 200, height=1.4, layer="TEXTO_ROTULOS")

    # Continuación de potencia hacia Medidor
    dxf.add_line(125, 240, 145, 240, layer="LINEAS_POTENCIA_AC")
    dxf.add_line(125, 210, 145, 210, layer="LINEAS_NEUTRO")

    # 3. Medidor de Energía Bidireccional Modbus RS-485
    dxf.add_rect(145, 195, 45, 65, layer="MODULOS_PROTECCION")
    dxf.add_text("MEDIDOR ENERGÍA", 148, 250, height=1.8, layer="TEXTO_ROTULOS")
    dxf.add_text("DIN Modbus RS-485", 148, 240, height=1.5, layer="TEXTO_ROTULOS")
    dxf.add_text("V, I, P, Q, FP, kWh", 148, 225, height=1.4, layer="TEXTO_ROTULOS")
    dxf.add_text("Clase 1.0 (MID)", 148, 205, height=1.4, layer="TEXTO_ROTULOS")

    # Conexión hacia Contactor
    dxf.add_line(190, 240, 210, 240, layer="LINEAS_POTENCIA_AC")
    dxf.add_line(190, 210, 210, 210, layer="LINEAS_NEUTRO")

    # 4. Contactor de Potencia 2P 40A con Contacto Auxiliar
    dxf.add_rect(210, 195, 45, 65, layer="MODULOS_PROTECCION")
    dxf.add_text("CONTACTOR 2P", 213, 250, height=1.8, layer="TEXTO_ROTULOS")
    dxf.add_text("40A AC-1 / 230V", 213, 240, height=1.5, layer="TEXTO_ROTULOS")
    dxf.add_text("Bobina A1-A2 230V", 213, 225, height=1.4, layer="TEXTO_ROTULOS")
    dxf.add_text("Aux 1NO (Feedback)", 213, 205, height=1.4, layer="TEXTO_ROTULOS")

    # Salida Contactor hacia Conector Tipo 2
    dxf.add_line(255, 240, 345, 240, layer="LINEAS_POTENCIA_AC")
    dxf.add_line(255, 210, 345, 210, layer="LINEAS_NEUTRO")

    # 5. Conector Hembra Tipo 2 (Mennekes IEC 62196-2)
    dxf.add_rect(345, 120, 60, 145, layer="MODULOS_PROTECCION")
    dxf.add_text("BASE TIPO 2", 348, 255, height=2.2, layer="TEXTO_ROTULOS")
    dxf.add_text("IEC 62196-2", 348, 245, height=1.8, layer="TEXTO_ROTULOS")
    dxf.add_text("Pin L1 (Fase 32A)", 348, 235, height=1.5, layer="TEXTO_ROTULOS")
    dxf.add_text("Pin N (Neutro 32A)", 348, 215, height=1.5, layer="TEXTO_ROTULOS")
    dxf.add_text("Pin PE (Tierra)", 348, 195, height=1.5, layer="TEXTO_ROTULOS")
    dxf.add_text("Pin CP (Control Pilot)", 348, 165, height=1.5, layer="TEXTO_ROTULOS")
    dxf.add_text("Pin PP (Proximity)", 348, 145, height=1.5, layer="TEXTO_ROTULOS")
    dxf.add_text("Actuador Bloqueo 12V", 348, 130, height=1.4, layer="TEXTO_ROTULOS")

    # 6. Controlador Electrónico ESP32 EVSE (Cerebro Inteligente)
    dxf.add_rect(75, 60, 180, 105, layer="MODULOS_PROTECCION")
    dxf.add_text("PLACA DE CONTROL INTELIGENTE (ESP32-WROOM-32 / EVSE)", 80, 155, height=2.2, layer="TEXTO_ROTULOS")
    
    # Submódulos del Controlador
    dxf.add_rect(82, 115, 45, 30, layer="MODULOS_PROTECCION")
    dxf.add_text("CIRCUITO CP", 85, 138, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("1 kHz PWM ±12V", 85, 128, height=1.4, layer="TEXTO_ROTULOS")
    dxf.add_text("ADC Detección Estado", 85, 120, height=1.2, layer="TEXTO_ROTULOS")

    dxf.add_rect(132, 115, 38, 30, layer="MODULOS_PROTECCION")
    dxf.add_text("CIRCUITO PP", 135, 138, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Divisor Resistivo", 135, 128, height=1.4, layer="TEXTO_ROTULOS")
    dxf.add_text("Detección Cable", 135, 120, height=1.2, layer="TEXTO_ROTULOS")

    dxf.add_rect(175, 115, 38, 30, layer="MODULOS_PROTECCION")
    dxf.add_text("DRIVER RELÉ", 178, 138, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Control Bobina 230V", 178, 128, height=1.4, layer="TEXTO_ROTULOS")
    dxf.add_text("+ Feedback Auxiliar", 178, 120, height=1.2, layer="TEXTO_ROTULOS")

    dxf.add_rect(218, 115, 32, 30, layer="MODULOS_PROTECCION")
    dxf.add_text("BLOQUEO", 221, 138, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Puente H 12V", 221, 128, height=1.4, layer="TEXTO_ROTULOS")
    dxf.add_text("Solenoide", 221, 120, height=1.2, layer="TEXTO_ROTULOS")

    # Módulo RS485 Modbus y ESP32 Core
    dxf.add_rect(82, 70, 70, 35, layer="MODULOS_PROTECCION")
    dxf.add_text("INTERFAZ MODBUS RS-485", 85, 95, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Aislada galvánicamente (ISO3082)", 85, 87, height=1.3, layer="TEXTO_ROTULOS")
    dxf.add_text("Lectura Medidor local + Panel Solar", 85, 78, height=1.3, layer="TEXTO_ROTULOS")

    dxf.add_rect(160, 70, 90, 35, layer="MODULOS_PROTECCION")
    dxf.add_text("ESP32 SOC + FIRMWARE ESPHOME", 163, 95, height=1.6, layer="TEXTO_ROTULOS")
    dxf.add_text("Algoritmo Solar Excess Tracker (6A - 32A)", 163, 87, height=1.3, layer="TEXTO_ROTULOS")
    dxf.add_text("OLED SSD1306 + RFID RC522 + Anillo RGB", 163, 78, height=1.3, layer="TEXTO_ROTULOS")

    # Líneas de Señal y Control
    # CP desde circuito hasta conector
    dxf.add_line(127, 130, 345, 165, layer="SEÑALES_CONTROL_PILOT")
    dxf.add_text("Línea CP (Control Pilot IEC 61851-1)", 190, 168, height=1.4, layer="TEXTO_ROTULOS")

    # PP desde circuito hasta conector
    dxf.add_line(170, 130, 345, 145, layer="SEÑALES_CONTROL_PILOT")
    dxf.add_text("Línea PP (Proximity Pilot)", 240, 148, height=1.4, layer="TEXTO_ROTULOS")

    # Bus Modbus RS485 desde controlador hasta Medidor
    dxf.add_line(117, 105, 117, 175, layer="SEÑALES_CONTROL_PILOT")
    dxf.add_line(117, 175, 150, 175, layer="SEÑALES_CONTROL_PILOT")
    dxf.add_line(150, 175, 150, 195, layer="SEÑALES_CONTROL_PILOT")
    dxf.add_text("Bus RS-485 A/B (Modbus RTU)", 120, 177, height=1.3, layer="TEXTO_ROTULOS")

    # Control de Bobina Contactor
    dxf.add_line(195, 145, 195, 185, layer="SEÑALES_CONTROL_PILOT")
    dxf.add_line(195, 185, 220, 185, layer="SEÑALES_CONTROL_PILOT")
    dxf.add_line(220, 185, 220, 195, layer="SEÑALES_CONTROL_PILOT")
    dxf.add_text("Disparo Bobina 230V", 198, 187, height=1.3, layer="TEXTO_ROTULOS")

    # Seta de Parada de Emergencia
    dxf.add_rect(270, 170, 35, 20, layer="MODULOS_PROTECCION")
    dxf.add_text("PARADA EMERGENCIA", 272, 183, height=1.3, layer="TEXTO_ROTULOS")
    dxf.add_text("Corte Físico Bobina", 272, 174, height=1.2, layer="TEXTO_ROTULOS")

    # Tabla de Estados IEC 61851
    dxf.add_rect(15, 15, 205, 38, layer="MARCO_ROTULO")
    dxf.add_text("ESTADOS DE CARGA NORMA IEC 61851-1:", 20, 45, height=1.8, layer="TEXTO_ROTULOS")
    dxf.add_text("• Estado A (12V): En espera (Vehículo Desconectado)", 20, 38, height=1.4, layer="TEXTO_ROTULOS")
    dxf.add_text("• Estado B (9V): Vehículo Conectado (Sin Carga)", 20, 32, height=1.4, layer="TEXTO_ROTULOS")
    dxf.add_text("• Estado C (6V): Carga Activa Normal (Contactor ON)", 20, 26, height=1.4, layer="TEXTO_ROTULOS")
    dxf.add_text("• Estado D (3V): Carga con Ventilación Requerida", 20, 20, height=1.4, layer="TEXTO_ROTULOS")

    dxf.save()
    print(f"DXF guardado en: {dxf_path}")

    # 2. GENERACIÓN SVG
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 850" width="100%" height="100%" style="background-color: #121820; font-family: monospace, sans-serif;">
  <defs>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Marco Exterior y Cajetin -->
  <rect x="20" y="20" width="1160" height="810" fill="none" stroke="#2a3b4c" stroke-width="3" rx="8" />
  <rect x="30" y="30" width="1140" height="790" fill="none" stroke="#1f2d3d" stroke-width="1.5" />
  
  <rect x="680" y="730" width="480" height="80" fill="#182230" stroke="#3b82f6" stroke-width="2" rx="4" />
  <text x="700" y="755" fill="#60a5fa" font-size="16" font-weight="bold">OPEN-SOURCE-DOMOTICS</text>
  <text x="700" y="775" fill="#f8fafc" font-size="13" font-weight="bold">ESQUEMA ELÉCTRICO Y CONTROL - EV WALLBOX 32A (7.4 kW)</text>
  <text x="700" y="795" fill="#94a3b8" font-size="11">IEC 61851-1 / SAE J1772 + Modbus RS485 + Balanceo Solar Dinámico</text>

  <!-- Alimentacion Acometida -->
  <g transform="translate(50, 120)">
    <rect x="0" y="0" width="120" height="260" fill="#1e293b" stroke="#0ea5e9" stroke-width="2" rx="6" />
    <text x="15" y="30" fill="#38bdf8" font-size="14" font-weight="bold">ACOMETIDA</text>
    <text x="15" y="55" fill="#f8fafc" font-size="13">230V~ 50Hz</text>
    <text x="15" y="80" fill="#94a3b8" font-size="11">TGBT / Cuadro</text>
    <text x="15" y="100" fill="#94a3b8" font-size="11">Cochera</text>
    <text x="15" y="140" fill="#e2e8f0" font-size="11">Conductores:</text>
    <text x="15" y="160" fill="#fb923c" font-size="11">• L1: 10 mm²</text>
    <text x="15" y="180" fill="#38bdf8" font-size="11">• N: 10 mm²</text>
    <text x="15" y="200" fill="#4ade80" font-size="11">• PE: 10 mm²</text>
    <text x="15" y="235" fill="#cbd5e1" font-size="10">Tubo M32 IK10</text>
  </g>

  <!-- Lineas de Potencia AC -->
  <!-- Fase L1 -->
  <path d="M 170 170 L 230 170" stroke="#fb923c" stroke-width="4" fill="none" />
  <text x="180" y="160" fill="#fb923c" font-size="11" font-weight="bold">L1</text>
  <!-- Neutro N -->
  <path d="M 170 250 L 230 250" stroke="#38bdf8" stroke-width="4" fill="none" />
  <text x="180" y="240" fill="#38bdf8" font-size="11" font-weight="bold">N</text>
  <!-- PE -->
  <path d="M 170 330 L 980 330" stroke="#4ade80" stroke-width="3" stroke-dasharray="6,4" fill="none" />
  <text x="500" y="320" fill="#4ade80" font-size="12" font-weight="bold">PE (Tierra de Protección Continua 10 mm²)</text>

  <!-- Protecciones: MCB 40A + RCD Tipo B 6mA DC -->
  <g transform="translate(230, 120)">
    <rect x="0" y="0" width="140" height="260" fill="#1e293b" stroke="#eab308" stroke-width="2" rx="6" />
    <text x="15" y="30" fill="#facc15" font-size="13" font-weight="bold">PROTECCIÓN</text>
    <text x="15" y="55" fill="#f8fafc" font-size="12">MCB 2P C40A</text>
    <text x="15" y="75" fill="#94a3b8" font-size="11">Poder corte 10kA</text>
    
    <line x1="10" y1="95" x2="130" y2="95" stroke="#334155" stroke-width="1.5" />
    
    <text x="15" y="125" fill="#f8fafc" font-size="12">RCD Tipo B</text>
    <text x="15" y="145" fill="#94a3b8" font-size="11">IΔn = 30 mA AC</text>
    <text x="15" y="165" fill="#ef4444" font-size="11" font-weight="bold">+ 6 mA DC (RDC-DD)</text>
    <text x="15" y="185" fill="#94a3b8" font-size="10">Norma IEC 62955</text>
    <text x="15" y="235" fill="#22c55e" font-size="10">Test Mensual</text>
  </g>

  <!-- Lineas Protecciones a Medidor -->
  <path d="M 370 170 L 430 170" stroke="#fb923c" stroke-width="4" fill="none" />
  <path d="M 370 250 L 430 250" stroke="#38bdf8" stroke-width="4" fill="none" />

  <!-- Medidor de Energia Modbus -->
  <g transform="translate(430, 120)">
    <rect x="0" y="0" width="140" height="260" fill="#1e293b" stroke="#8b5cf6" stroke-width="2" rx="6" />
    <text x="15" y="30" fill="#a78bfa" font-size="13" font-weight="bold">MEDIDOR ENERGÍA</text>
    <text x="15" y="55" fill="#f8fafc" font-size="12">Modbus RS-485</text>
    <text x="15" y="75" fill="#94a3b8" font-size="11">Clase 1.0 (MID)</text>
    <text x="15" y="115" fill="#cbd5e1" font-size="11">Medición:</text>
    <text x="15" y="135" fill="#94a3b8" font-size="10">• Voltaje (V)</text>
    <text x="15" y="155" fill="#94a3b8" font-size="10">• Corriente (A)</text>
    <text x="15" y="175" fill="#94a3b8" font-size="10">• Potencia (kW)</text>
    <text x="15" y="195" fill="#94a3b8" font-size="10">• Factor de Pot.</text>
    <text x="15" y="215" fill="#94a3b8" font-size="10">• Energía (kWh)</text>
  </g>

  <!-- Lineas Medidor a Contactor -->
  <path d="M 570 170 L 630 170" stroke="#fb923c" stroke-width="4" fill="none" />
  <path d="M 570 250 L 630 250" stroke="#38bdf8" stroke-width="4" fill="none" />

  <!-- Contactor de Potencia 40A 2P -->
  <g transform="translate(630, 120)">
    <rect x="0" y="0" width="140" height="260" fill="#1e293b" stroke="#f43f5e" stroke-width="2" rx="6" />
    <text x="15" y="30" fill="#fb7185" font-size="13" font-weight="bold">CONTACTOR 2P</text>
    <text x="15" y="55" fill="#f8fafc" font-size="12">40A AC-1 / 230V</text>
    <text x="15" y="75" fill="#94a3b8" font-size="11">Bobina: 230VAC</text>
    <text x="15" y="115" fill="#f8fafc" font-size="11">Contacto Auxiliar:</text>
    <text x="15" y="135" fill="#94a3b8" font-size="10">1NO Feedback</text>
    <text x="15" y="155" fill="#38bdf8" font-size="10">Supervisión Soldadura</text>
    <circle cx="70" cy="205" r="22" fill="#334155" stroke="#fb7185" stroke-width="2" />
    <text x="58" y="210" fill="#f8fafc" font-size="12" font-weight="bold">A1-A2</text>
  </g>

  <!-- Lineas Contactor a Base Tipo 2 -->
  <path d="M 770 170 L 980 170" stroke="#fb923c" stroke-width="4" fill="none" />
  <path d="M 770 250 L 980 250" stroke="#38bdf8" stroke-width="4" fill="none" />

  <!-- Base Tipo 2 (Mennekes) -->
  <g transform="translate(980, 100)">
    <rect x="0" y="0" width="160" height="340" fill="#1e293b" stroke="#3b82f6" stroke-width="2.5" rx="8" />
    <text x="15" y="35" fill="#60a5fa" font-size="15" font-weight="bold">BASE TIPO 2</text>
    <text x="15" y="55" fill="#94a3b8" font-size="12">IEC 62196-2</text>
    
    <circle cx="40" cy="70" r="12" fill="#fb923c" />
    <text x="60" y="75" fill="#f8fafc" font-size="12">L1 (Fase)</text>
    
    <circle cx="40" cy="150" r="12" fill="#38bdf8" />
    <text x="60" y="155" fill="#f8fafc" font-size="12">N (Neutro)</text>
    
    <circle cx="40" cy="230" r="12" fill="#4ade80" />
    <text x="60" y="235" fill="#f8fafc" font-size="12">PE (Tierra)</text>
    
    <circle cx="40" cy="275" r="9" fill="#eab308" />
    <text x="60" y="280" fill="#f8fafc" font-size="12">CP (Pilot)</text>
    
    <circle cx="40" cy="310" r="9" fill="#c084fc" />
    <text x="60" y="315" fill="#f8fafc" font-size="12">PP (Proximity)</text>
  </g>

  <!-- Controlador Inteligente ESP32 EVSE -->
  <g transform="translate(200, 430)">
    <rect x="0" y="0" width="750" height="280" fill="#0f172a" stroke="#10b981" stroke-width="2.5" rx="8" />
    <text x="25" y="35" fill="#34d399" font-size="16" font-weight="bold">CONTROLADOR INTELIGENTE DE CARGA EV (ESP32-WROOM-32 / EVSE)</text>
    
    <!-- Sub-bloque CP -->
    <rect x="25" y="60" width="160" height="120" fill="#1e293b" stroke="#eab308" stroke-width="1.5" rx="4" />
    <text x="35" y="85" fill="#facc15" font-size="13" font-weight="bold">CIRCUITO CP (PILOT)</text>
    <text x="35" y="105" fill="#94a3b8" font-size="11">PWM 1 kHz ±12V</text>
    <text x="35" y="125" fill="#f8fafc" font-size="11">ADC Detección Voltaje:</text>
    <text x="35" y="145" fill="#e2e8f0" font-size="10">12V / 9V / 6V / 3V</text>
    <text x="35" y="165" fill="#cbd5e1" font-size="10">Duty = Amp / 0.6</text>

    <!-- Sub-bloque PP -->
    <rect x="205" y="60" width="160" height="120" fill="#1e293b" stroke="#c084fc" stroke-width="1.5" rx="4" />
    <text x="215" y="85" fill="#d8b4fe" font-size="13" font-weight="bold">CIRCUITO PP (CABLE)</text>
    <text x="215" y="105" fill="#94a3b8" font-size="11">Divisor Resistivo</text>
    <text x="215" y="125" fill="#f8fafc" font-size="11">Resistencia Cable:</text>
    <text x="215" y="145" fill="#e2e8f0" font-size="10">• 1500 Ω = 13A</text>
    <text x="215" y="165" fill="#e2e8f0" font-size="10">• 680 Ω = 20A | 220 Ω = 32A</text>

    <!-- Sub-bloque Control Rele Bobina -->
    <rect x="385" y="60" width="160" height="120" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5" rx="4" />
    <text x="395" y="85" fill="#fb7185" font-size="13" font-weight="bold">DRIVER CONTACTOR</text>
    <text x="395" y="105" fill="#94a3b8" font-size="11">Relé de Control 230V</text>
    <text x="395" y="125" fill="#f8fafc" font-size="11">Interbloqueo Físico</text>
    <text x="395" y="145" fill="#94a3b8" font-size="10">Entrada Feedback Aux</text>
    <text x="395" y="165" fill="#ef4444" font-size="10">Corte &lt; 20 ms ante falla</text>

    <!-- Sub-bloque Bloqueo de Conector -->
    <rect x="565" y="60" width="160" height="120" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="4" />
    <text x="575" y="85" fill="#38bdf8" font-size="13" font-weight="bold">BLOQUEO ENCHUFE</text>
    <text x="575" y="105" fill="#94a3b8" font-size="11">Puente H 12V 1.5A</text>
    <text x="575" y="125" fill="#f8fafc" font-size="11">Motor / Solenoide</text>
    <text x="575" y="145" fill="#94a3b8" font-size="10">Retención antirrobo</text>
    <text x="575" y="165" fill="#22c55e" font-size="10">Desbloqueo manual</text>

    <!-- Fila Inferior: Logica Solar y Perifericos -->
    <rect x="25" y="200" width="340" height="65" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.5" rx="4" />
    <text x="35" y="225" fill="#38bdf8" font-size="12" font-weight="bold">MODBUS RS-485 AISLADO (ISO3082)</text>
    <text x="35" y="245" fill="#94a3b8" font-size="11">Enlace hacia Medidor de Entrada + Inversor Híbrido</text>

    <rect x="385" y="200" width="340" height="65" fill="#1e293b" stroke="#10b981" stroke-width="1.5" rx="4" />
    <text x="395" y="225" fill="#34d399" font-size="12" font-weight="bold">MODOS INTELIGENTES (ESPHOME / HA)</text>
    <text x="395" y="245" fill="#94a3b8" font-size="11">1) Solar Puro (0 Red) | 2) Eco Solar | 3) Boost Rápido 32A</text>
  </g>

  <!-- Cableado de Señales desde ESP32 a Elementos Externos -->
  <!-- CP Pilot hacia Conector Tipo 2 -->
  <path d="M 185 490 L 1020 490 L 1020 375" stroke="#eab308" stroke-width="2.5" fill="none" stroke-dasharray="5,3" />
  <!-- PP Pilot hacia Conector Tipo 2 -->
  <path d="M 365 520 L 1040 520 L 1040 410" stroke="#c084fc" stroke-width="2.5" fill="none" stroke-dasharray="5,3" />
  <!-- Disparo Contactor Bobina -->
  <path d="M 665 490 L 700 490 L 700 380" stroke="#f43f5e" stroke-width="2.5" fill="none" />
  <!-- Bus Modbus hacia Medidor -->
  <path d="M 365 650 L 500 650 L 500 380" stroke="#0ea5e9" stroke-width="2" fill="none" stroke-dasharray="4,4" />

  <!-- Tabla Informativa de Estados IEC 61851-1 -->
  <g transform="translate(50, 430)">
    <rect x="0" y="0" width="130" height="280" fill="#182230" stroke="#334155" stroke-width="1.5" rx="6" />
    <text x="10" y="25" fill="#f8fafc" font-size="11" font-weight="bold">ESTADOS IEC:</text>
    <text x="10" y="55" fill="#94a3b8" font-size="10">Estado A (+12V):</text>
    <text x="10" y="70" fill="#e2e8f0" font-size="10">Vehículo no disp.</text>
    
    <text x="10" y="105" fill="#94a3b8" font-size="10">Estado B (+9V):</text>
    <text x="10" y="120" fill="#e2e8f0" font-size="10">Conectado / Stop</text>
    
    <text x="10" y="155" fill="#22c55e" font-size="10">Estado C (+6V):</text>
    <text x="10" y="170" fill="#4ade80" font-size="10">Carga Activa OK</text>
    
    <text x="10" y="205" fill="#facc15" font-size="10">Estado D (+3V):</text>
    <text x="10" y="220" fill="#fde047" font-size="10">Req. Ventilación</text>
    
    <text x="10" y="250" fill="#ef4444" font-size="10">Estado E/F (0V/-12V):</text>
    <text x="10" y="265" fill="#f87171" font-size="10">Falla / Bloqueo</text>
  </g>
</svg>"""

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"SVG guardado en: {svg_path}")

if __name__ == "__main__":
    dxf_out = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/09_cargador_vehiculo_electrico_ev/electrico/esquema_ev_wallbox.dxf"
    svg_out = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/09_cargador_vehiculo_electrico_ev/electrico/esquema_ev_wallbox.svg"
    generar_diagrama_ev_wallbox(dxf_out, svg_out)

