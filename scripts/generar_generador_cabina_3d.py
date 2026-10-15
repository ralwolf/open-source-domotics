#!/usr/bin/env python3
"""
generar_generador_cabina_3d.py
Genera el modelo paramétrico 3D de la cabina exterior insonorizada para el motogenerador
de respaldo terciario de gasolina en FreeCAD 1.1+ y exporta a formato neutral STEP AP214.
Dimensiones: 950 x 650 x 700 mm, deflectores acústicos, tubo de escape y silentblocks.
"""

import sys
import os

try:
    import FreeCAD
    import Part
except ImportError:
    print("Error: FreeCAD no está en el path de Python.")
    sys.exit(1)

def crear_cabina_generador_3d():
    doc = FreeCAD.newDocument("Cabina_Insonorizada_Generador_Respaldo")

    # 1. Carcasa exterior insonorizada de chapa galvanizada (950 x 650 x 700 mm)
    cuerpo = Part.makeBox(950, 650, 700)
    cuerpo.translate(FreeCAD.Vector(-475, -325, 0))

    # Cavidad interna
    cavidad = Part.makeBox(920, 620, 670)
    cavidad.translate(FreeCAD.Vector(-460, -310, 15))
    carcasa = cuerpo.cut(cavidad)

    # 2. Tapa superior inclinada para evacuación de agua de lluvia
    tapa = Part.makeBox(960, 660, 25)
    tapa.translate(FreeCAD.Vector(-480, -330, 690))

    # 3. Deflectores acústicos / rejillas tipo laberinto para ventilación sin escape sonoro
    rejilla_in = Part.makeBox(15, 220, 180)
    rejilla_in.translate(FreeCAD.Vector(-476, -110, 250))

    rejilla_out = Part.makeBox(15, 220, 180)
    rejilla_out.translate(FreeCAD.Vector(461, -110, 250))

    # 4. Tubo de escape de gases de combustión con silenciador exterior
    escape_codo = Part.makeCylinder(25, 80, FreeCAD.Vector(300, 325, 500), FreeCAD.Vector(0, 1, 0))
    silenciador = Part.makeCylinder(45, 160, FreeCAD.Vector(300, 405, 500), FreeCAD.Vector(0, 0, 1))

    # 5. Cuatro amortiguadores silentblocks de caucho en la base
    silentblocks = []
    posiciones = [(-400, -250), (-400, 250), (400, -250), (400, 250)]
    for px, py in posiciones:
        sb = Part.makeCylinder(35, 30, FreeCAD.Vector(px, py, -30), FreeCAD.Vector(0, 0, 1))
        silentblocks.append(sb)

    modelo = carcasa.fuse([tapa, escape_codo, silenciador] + silentblocks)
    modelo = modelo.cut(rejilla_in).cut(rejilla_out)

    obj = doc.addObject("Part::Feature", "Cabina_Generador_Respaldo")
    obj.Shape = modelo

    if hasattr(obj, "ViewObject") and obj.ViewObject:
        obj.ViewObject.ShapeColor = (0.28, 0.45, 0.35) # Verde militar / técnico
        obj.ViewObject.Transparency = 10

    doc.recompute()

    output_dir = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/06_generador_gasolina_respaldo/mecanico"
    os.makedirs(output_dir, exist_ok=True)

    fcstd_path = os.path.join(output_dir, "cabina_insonorizada_generador_gasolina.FCStd")
    step_path = os.path.join(output_dir, "cabina_insonorizada_generador_gasolina.step")

    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)
    print(f"Modelo Cabina Generador FreeCAD generado: {fcstd_path}")
    print(f"Modelo Cabina Generador STEP exportado: {step_path}")

if __name__ == "__main__":
    crear_cabina_generador_3d()
