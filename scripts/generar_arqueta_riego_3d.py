#!/usr/bin/env python3
"""
generar_arqueta_riego_3d.py
Genera el modelo paramétrico 3D de la Arqueta Enterrada de Riego Automatizado
con colector manifold de 4 zonas, electroválvula maestra, filtro de anillas y caudalímetro
en FreeCAD 1.1+ y exporta a STEP AP214.
Dimensiones arqueta: Base 640 x 500 mm, Tapa 500 x 350 mm, Altura 300 mm,
polietileno negro de alta densidad y tapa verde con perno antivandálico.
"""

import sys
import os

try:
    import FreeCAD
    import Part
except ImportError:
    print("Error: FreeCAD no está en el path de Python.")
    sys.exit(1)

def crear_arqueta_riego_3d():
    doc = FreeCAD.newDocument("Arqueta_Riego_4_Zonas")

    # 1. Cuerpo cónico/troncopiramidal de la arqueta enterrada
    # Pirámide truncada exterior (640x500 en base, 500x350 en cima, h=300)
    # Modelado con caja exterior recortada o composición
    caja_ext = Part.makeBox(520, 370, 300)
    caja_ext.translate(FreeCAD.Vector(-260, -185, 0))

    cavidad_int = Part.makeBox(500, 350, 290)
    cavidad_int.translate(FreeCAD.Vector(-250, -175, 10))
    cuerpo_arqueta = caja_ext.cut(cavidad_int)

    # Tapa superior verde (516 x 366 x 20 mm)
    tapa = Part.makeBox(516, 366, 20)
    tapa.translate(FreeCAD.Vector(-258, -183, 295))

    # Perno / cerradura de tapa
    perno = Part.makeCylinder(10, 15, FreeCAD.Vector(0, 0, 305), FreeCAD.Vector(0, 0, 1))

    # Recortes laterales para paso de tuberías (Ø40 mm = 1" 1/4)
    # Entrada de agua
    tubo_in = Part.makeCylinder(22, 60, FreeCAD.Vector(-270, 0, 80), FreeCAD.Vector(1, 0, 0))
    # 4 salidas de zona
    salidas = []
    for i in range(4):
        sy = -120 + i * 80
        s = Part.makeCylinder(18, 60, FreeCAD.Vector(240, sy, 80), FreeCAD.Vector(1, 0, 0))
        salidas.append(s)

    cuerpo = cuerpo_arqueta.cut(tubo_in)
    for s in salidas:
        cuerpo = cuerpo.cut(s)

    # 2. Colector hidráulico interior de 1"
    # Tubería de entrada con válvula manual de bola y filtro
    filtro_anillas = Part.makeCylinder(35, 120, FreeCAD.Vector(-180, 0, 80), FreeCAD.Vector(0, 0, 1))
    valvula_maestra = Part.makeBox(60, 60, 110)
    valvula_maestra.translate(FreeCAD.Vector(-100, -30, 40))
    solenoide_m = Part.makeCylinder(16, 45, FreeCAD.Vector(-70, 0, 150), FreeCAD.Vector(0, 0, 1))

    # Caudalímetro de pulsos
    caudalimetro = Part.makeCylinder(28, 80, FreeCAD.Vector(-20, -15, 80), FreeCAD.Vector(0, 1, 0))

    # Colector manifold principal (tubo horizontal de distribución)
    manifold = Part.makeCylinder(20, 260, FreeCAD.Vector(80, -130, 80), FreeCAD.Vector(0, 1, 0))

    # 4 electroválvulas de zona 24VAC (Hunter/Rain Bird 1")
    valvulas_zona = []
    for i in range(4):
        vy = -120 + i * 80
        cuerpo_v = Part.makeBox(60, 50, 90)
        cuerpo_v.translate(FreeCAD.Vector(140, vy - 25, 40))
        solenoide = Part.makeCylinder(14, 40, FreeCAD.Vector(170, vy, 130), FreeCAD.Vector(0, 0, 1))
        valvulas_zona.extend([cuerpo_v, solenoide])

    interior_hidraulico = filtro_anillas.fuse([valvula_maestra, solenoide_m, caudalimetro, manifold] + valvulas_zona)

    solido_final = cuerpo.fuse([tapa, perno, interior_hidraulico])

    obj = doc.addObject("Part::Feature", "Arqueta_Riego_4_Zonas")
    obj.Shape = solido_final

    if hasattr(obj, "ViewObject") and obj.ViewObject:
        obj.ViewObject.ShapeColor = (0.2, 0.45, 0.2) # Verde técnico de jardinería
        obj.ViewObject.Transparency = 10

    doc.recompute()

    output_dir = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/03_riego_automatizado_jardin/mecanico"
    os.makedirs(output_dir, exist_ok=True)

    fcstd_path = os.path.join(output_dir, "arqueta_riego_electrovalvulas_3d.FCStd")
    step_path = os.path.join(output_dir, "arqueta_riego_electrovalvulas_3d.step")

    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)

    print(f"Éxito: Modelo 3D guardado en {fcstd_path}")
    print(f"Éxito: Archivo STEP exportado en {step_path}")

if __name__ == "__main__":
    crear_arqueta_riego_3d()

