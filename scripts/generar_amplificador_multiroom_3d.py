#!/usr/bin/env python3
"""
generar_amplificador_multiroom_3d.py
Genera el modelo paramétrico 3D de la carcasa del amplificador digital estéreo
Clase D para audio multiroom distribuido en FreeCAD 1.1+ y exporta a formato STEP AP214.
Dimensiones: 110 x 85 x 32 mm, aletas de disipación, bornas banana y conector RJ45.
"""

import sys
import os

try:
    import FreeCAD
    import Part
except ImportError:
    print("Error: FreeCAD no está en el path de Python.")
    sys.exit(1)

def crear_amplificador_3d():
    doc = FreeCAD.newDocument("Amplificador_Audio_Multiroom")

    # 1. Carcasa de extrusión de aluminio anodizado (110 x 85 x 32 mm)
    cuerpo = Part.makeBox(110, 85, 32)
    cuerpo.translate(FreeCAD.Vector(-55, -42.5, 0))

    # Cavidad interna
    cavidad = Part.makeBox(104, 79, 28)
    cavidad.translate(FreeCAD.Vector(-52, -39.5, 2))
    carcasa = cuerpo.cut(cavidad)

    # 2. Aletas laterales de disipación pasiva
    aletas = []
    for i in range(6):
        pos_z = 5 + i * 4.5
        a1 = Part.makeBox(110, 3, 2)
        a1.translate(FreeCAD.Vector(-55, 42.5, pos_z))
        a2 = Part.makeBox(110, 3, 2)
        a2.translate(FreeCAD.Vector(-55, -45.5, pos_z))
        aletas.extend([a1, a2])

    # 3. Panel frontal: Potenciómetro / botón giratorio y LED de estado
    dial = Part.makeCylinder(10, 12, FreeCAD.Vector(55, 0, 16), FreeCAD.Vector(1, 0, 0))
    led1 = Part.makeCylinder(1.5, 3, FreeCAD.Vector(55, -20, 16), FreeCAD.Vector(1, 0, 0))
    led2 = Part.makeCylinder(1.5, 3, FreeCAD.Vector(55, 20, 16), FreeCAD.Vector(1, 0, 0))

    # 4. Panel trasero: 4x bornas banana para altavoces (L+, L-, R+, R-), jack DC 24V y puerto RJ45
    bornas = []
    colores_bornas = [-25, -12, 12, 25]
    for b_y in colores_bornas:
        b = Part.makeCylinder(4, 15, FreeCAD.Vector(-55, b_y, 14), FreeCAD.Vector(-1, 0, 0))
        bornas.append(b)

    jack_dc = Part.makeCylinder(5, 10, FreeCAD.Vector(-55, -32, 20), FreeCAD.Vector(-1, 0, 0))
    puerto_eth = Part.makeBox(14, 16, 12)
    puerto_eth.translate(FreeCAD.Vector(-60, 20, 10))

    # 5. Pestañas de fijación para rack o pared
    p1 = Part.makeBox(8, 15, 3)
    p1.translate(FreeCAD.Vector(-59, -7.5, 0))
    p2 = Part.makeBox(8, 15, 3)
    p2.translate(FreeCAD.Vector(51, -7.5, 0))

    modelo = carcasa.fuse(aletas + [dial, led1, led2, jack_dc, p1, p2] + bornas)
    modelo = modelo.cut(puerto_eth)

    obj = doc.addObject("Part::Feature", "Amplificador_HiFi_Multiroom")
    obj.Shape = modelo

    if hasattr(obj, "ViewObject") and obj.ViewObject:
        obj.ViewObject.ShapeColor = (0.15, 0.15, 0.18) # Negro anodizado
        obj.ViewObject.Transparency = 5

    doc.recompute()

    output_dir = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/05_audio_distribuido_multiroom/mecanico"
    os.makedirs(output_dir, exist_ok=True)

    fcstd_path = os.path.join(output_dir, "amplificador_streamer_multiroom.FCStd")
    step_path = os.path.join(output_dir, "amplificador_streamer_multiroom.step")

    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)
    print(f"Modelo Amplificador FreeCAD generado: {fcstd_path}")
    print(f"Modelo Amplificador STEP exportado: {step_path}")

if __name__ == "__main__":
    crear_amplificador_3d()
