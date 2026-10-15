#!/usr/bin/env python3
"""
generar_medidor_potencia_din_3d.py
Genera el modelo paramétrico 3D de la envolvente modular de 4 módulos DIN (4M)
para el Medidor de Potencia y Telemetría Eléctrica IoT (norma DIN 43880) en FreeCAD 1.1+ y exporta a STEP AP214.
Dimensiones: 72 x 90 x 65 mm, pestaña de enclavamiento a carril DIN TS-35,
pantalla OLED 0.96", puerto RJ45 frontal, pulsadores de navegación y borneros enchufables dobles.
"""

import sys
import os

try:
    import FreeCAD
    import Part
except ImportError:
    print("Error: FreeCAD no está en el path de Python.")
    sys.exit(1)

def crear_medidor_din_3d():
    doc = FreeCAD.newDocument("Medidor_Potencia_DIN_4M")

    ancho = 72.0
    altura = 90.0
    profundidad = 65.0
    espesor = 2.0

    # 1. Cuerpo principal modular según perfil DIN 43880
    # Base inferior ancha (72 x 90 x 45 mm)
    caja_base = Part.makeBox(ancho, altura, 45)
    caja_base.translate(FreeCAD.Vector(-ancho/2.0, -altura/2.0, 0))

    # Nariz o frontal elevado estándar (ancho 72, alto 45, profundidad 20)
    caja_nariz = Part.makeBox(ancho, 45, 20)
    caja_nariz.translate(FreeCAD.Vector(-ancho/2.0, -22.5, 45))

    caja_solida = caja_base.fuse(caja_nariz)

    # Vaciado interior para electrónica
    cavidad_base = Part.makeBox(ancho - 2*espesor, altura - 2*espesor, 43)
    cavidad_base.translate(FreeCAD.Vector(-ancho/2.0 + espesor, -altura/2.0 + espesor, 2))

    cavidad_nariz = Part.makeBox(ancho - 2*espesor, 41, 20)
    cavidad_nariz.translate(FreeCAD.Vector(-ancho/2.0 + espesor, -20.5, 43))

    cavidad = cavidad_base.fuse(cavidad_nariz)
    carcasa = caja_solida.cut(cavidad)

    # 2. Canal posterior de anclaje a carril DIN TS-35 (35 mm x 8 mm de profundidad)
    canal_din = Part.makeBox(ancho + 4, 35.5, 8.5)
    canal_din.translate(FreeCAD.Vector(-ancho/2.0 - 2, -17.75, 0))
    carcasa = carcasa.cut(canal_din)

    # Pestaña móvil de plástico elástico para clip DIN
    pestaña_din = Part.makeBox(18, 25, 4)
    pestaña_din.translate(FreeCAD.Vector(-9, -altura/2.0 + 5, 2))

    # 3. Ventana para pantalla OLED frontal (28 x 16 mm)
    ventana_oled = Part.makeBox(28, 16, 6)
    ventana_oled.translate(FreeCAD.Vector(-14, 2, 63))
    cristal_oled = Part.makeBox(26, 14, 2)
    cristal_oled.translate(FreeCAD.Vector(-13, 3, 64))

    # 4. Puerto RJ45 frontal para bus Modbus RS485 (16 x 14 mm)
    puerto_rj45 = Part.makeBox(16, 14, 6)
    puerto_rj45.translate(FreeCAD.Vector(-24, -16, 63))

    # 5. Tres pulsadores de membrana / navegación táctil (Ø5 mm)
    pulsadores = []
    for i in range(3):
        px = 10 + i * 8
        p = Part.makeCylinder(2.5, 4, FreeCAD.Vector(px, -10, 64), FreeCAD.Vector(0, 0, 1))
        pulsadores.append(p)

    # 6. Borneros enchufables superiores e inferiores (paso 5.08 mm, 6 polos cada uno)
    # Calado bornero superior
    hueco_bornero_sup = Part.makeBox(62, 14, 18)
    hueco_bornero_sup.translate(FreeCAD.Vector(-31, 30, 26))

    # Calado bornero inferior
    hueco_bornero_inf = Part.makeBox(62, 14, 18)
    hueco_bornero_inf.translate(FreeCAD.Vector(-31, -44, 26))

    carcasa = carcasa.cut(ventana_oled)
    carcasa = carcasa.cut(puerto_rj45)
    carcasa = carcasa.cut(hueco_bornero_sup)
    carcasa = carcasa.cut(hueco_bornero_inf)

    modelo = carcasa.fuse([pestaña_din, cristal_oled] + pulsadores)

    obj = doc.addObject("Part::Feature", "Medidor_Potencia_DIN_4M")
    obj.Shape = modelo

    if hasattr(obj, "ViewObject") and obj.ViewObject:
        obj.ViewObject.ShapeColor = (0.85, 0.86, 0.87) # Gris claro RAL 7035
        obj.ViewObject.Transparency = 5

    doc.recompute()

    output_dir = "/home/ral/Documents/GitHub/open-source-domotics/04_telemetria_y_cargas_criticas/01_medicion_potencia_cuadro/mecanico"
    os.makedirs(output_dir, exist_ok=True)

    fcstd_path = os.path.join(output_dir, "gabinete_din_medidor_potencia.FCStd")
    step_path = os.path.join(output_dir, "gabinete_din_medidor_potencia.step")

    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)

    print(f"Éxito: Modelo 3D guardado en {fcstd_path}")
    print(f"Éxito: Archivo STEP exportado en {step_path}")

if __name__ == "__main__":
    crear_medidor_din_3d()

