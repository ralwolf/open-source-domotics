#!/usr/bin/env python3
"""
generar_cocina_ups_3d.py
Genera el modelo paramétrico 3D del gabinete protector para el regulador de estado sólido
y mini-UPS LiFePO4 para el refrigerador en FreeCAD 1.1+ y exporta a STEP AP214.
Dimensiones: 280 x 200 x 95 mm, aletas de ventilación, display LCD frontal y tomas C20.
"""

import sys
import os

try:
    import FreeCAD
    import Part
except ImportError:
    print("Error: FreeCAD no está en el path de Python.")
    sys.exit(1)

def crear_gabinete_ups_cocina_3d():
    doc = FreeCAD.newDocument("Gabinete_Mini_UPS_Refrigerador")

    # 1. Carcasa exterior de chapa galvanizada / aluminio (280 x 200 x 95 mm)
    cuerpo = Part.makeBox(280, 200, 95)
    cuerpo.translate(FreeCAD.Vector(-140, -100, 0))

    # Cavidad interna
    cavidad = Part.makeBox(274, 194, 91)
    cavidad.translate(FreeCAD.Vector(-137, -97, 2))
    carcasa = cuerpo.cut(cavidad)

    # 2. Tapa frontal con mirilla de display OLED/LCD y LED de estado
    display = Part.makeBox(70, 30, 4)
    display.translate(FreeCAD.Vector(-35, 40, 93))
    led1 = Part.makeCylinder(2.5, 5, FreeCAD.Vector(-45, 55, 93), FreeCAD.Vector(0, 0, 1))
    led2 = Part.makeCylinder(2.5, 5, FreeCAD.Vector(-45, 40, 93), FreeCAD.Vector(0, 0, 1))

    # 3. Ranuras de ventilación para etapa reguladora de potencia
    ranuras = []
    for i in range(8):
        pos_x = -100 + i * 25
        r = Part.makeBox(15, 3, 50)
        r.translate(FreeCAD.Vector(pos_x, -101, 25))
        ranuras.append(r)

    # 4. Panel lateral: Toma de entrada IEC C20 y toma de salida Schuko protegida
    toma_in = Part.makeBox(32, 24, 6)
    toma_in.translate(FreeCAD.Vector(138, -60, 30))
    toma_out = Part.makeCylinder(20, 6, FreeCAD.Vector(138, 20, 45), FreeCAD.Vector(1, 0, 0))

    # 5. Pestañas de fijación mural
    p1 = Part.makeBox(15, 30, 3)
    p1.translate(FreeCAD.Vector(-155, -15, 0))
    p2 = Part.makeBox(15, 30, 3)
    p2.translate(FreeCAD.Vector(140, -15, 0))

    modelo = carcasa.fuse([p1, p2])
    modelo = modelo.cut(display).cut(led1).cut(led2).cut(toma_in).cut(toma_out)
    for r in ranuras:
        modelo = modelo.cut(r)

    obj = doc.addObject("Part::Feature", "Gabinete_UPS_Refrigerador")
    obj.Shape = modelo

    if hasattr(obj, "ViewObject") and obj.ViewObject:
        obj.ViewObject.ShapeColor = (0.25, 0.28, 0.32) # Gris oscuro técnico
        obj.ViewObject.Transparency = 5

    doc.recompute()

    output_dir = "/home/ral/Documents/GitHub/open-source-domotics/04_telemetria_y_cargas_criticas/02_cargas_cocina/mecanico"
    os.makedirs(output_dir, exist_ok=True)

    fcstd_path = os.path.join(output_dir, "gabinete_mini_ups_refrigerador.FCStd")
    step_path = os.path.join(output_dir, "gabinete_mini_ups_refrigerador.step")

    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)
    print(f"Modelo Mini-UPS Cocina FreeCAD generado: {fcstd_path}")
    print(f"Modelo Mini-UPS Cocina STEP exportado: {step_path}")

if __name__ == "__main__":
    crear_gabinete_ups_cocina_3d()
