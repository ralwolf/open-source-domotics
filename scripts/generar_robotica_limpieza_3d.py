#!/usr/bin/env python3
"""
generar_robotica_limpieza_3d.py
Genera el modelo paramétrico 3D de la estación base de vaciado y lavado de mopas
para robot aspirador/fregona en FreeCAD 1.1+ y exporta a formato STEP AP214.
Dimensiones: 450 x 400 x 480 mm con rampa de entrada y bahías para tanques de agua y polvo.
"""

import sys
import os

try:
    import FreeCAD
    import Part
except ImportError:
    print("Error: FreeCAD no está en el path de Python.")
    sys.exit(1)

def crear_estacion_robotica_3d():
    doc = FreeCAD.newDocument("Estacion_Base_Robot_Limpieza")

    # 1. Cuerpo principal de la torre de acoplamiento (450 x 400 x 480 mm)
    cuerpo = Part.makeBox(450, 400, 480)
    cuerpo.translate(FreeCAD.Vector(-225, -200, 0))

    # Cavidad inferior para garaje y acoplamiento del robot (360 x 300 x 140 mm)
    garaje = Part.makeBox(360, 300, 140)
    garaje.translate(FreeCAD.Vector(-180, -201, 0))
    estacion = cuerpo.cut(garaje)

    # 2. Rampa de entrada frontal inclinada (360 x 120 x 20 mm)
    rampa = Part.makeBox(360, 120, 15)
    rampa.translate(FreeCAD.Vector(-180, -320, 0))

    # 3. Tapa superior abatible para acceso a tanques de agua limpia y residual
    tapa = Part.makeBox(440, 390, 15)
    tapa.translate(FreeCAD.Vector(-220, -195, 470))

    # 4. Dos tanques superiores interiores visibles mediante hendiduras de inspección
    t1 = Part.makeBox(180, 160, 260)
    t1.translate(FreeCAD.Vector(-200, -10, 200))
    t2 = Part.makeBox(180, 160, 260)
    t2.translate(FreeCAD.Vector(20, -10, 200))

    # 5. Bahía para bolsa de polvo con cono de aspiración ciclónica
    cono = Part.makeCone(60, 20, 120, FreeCAD.Vector(0, 80, 220), FreeCAD.Vector(0, 0, 1))

    modelo = estacion.fuse([rampa, tapa, cono])

    obj = doc.addObject("Part::Feature", "Estacion_Robot_Limpieza")
    obj.Shape = modelo

    if hasattr(obj, "ViewObject") and obj.ViewObject:
        obj.ViewObject.ShapeColor = (0.9, 0.92, 0.95) # Blanco electrodoméstico
        obj.ViewObject.Transparency = 10

    doc.recompute()

    output_dir = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/02_robotica_limpieza/mecanico"
    os.makedirs(output_dir, exist_ok=True)

    fcstd_path = os.path.join(output_dir, "estacion_carga_robot_limpieza.FCStd")
    step_path = os.path.join(output_dir, "estacion_carga_robot_limpieza.step")

    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)
    print(f"Modelo Estación Limpieza FreeCAD generado: {fcstd_path}")
    print(f"Modelo Estación Limpieza STEP exportado: {step_path}")

if __name__ == "__main__":
    crear_estacion_robotica_3d()
