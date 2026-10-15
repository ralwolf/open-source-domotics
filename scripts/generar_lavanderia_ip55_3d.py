#!/usr/bin/env python3
"""
generar_lavanderia_ip55_3d.py
Genera el modelo paramétrico 3D de la base de enchufe estanca IP55 con tapa abatible
y soporte de base antivibratoria para lavadora/secadora en FreeCAD 1.1+ y exporta a STEP AP214.
Dimensiones: 160 x 120 x 85 mm, juntas estancas de silicona y prensaestopas PG16.
"""

import sys
import os

try:
    import FreeCAD
    import Part
except ImportError:
    print("Error: FreeCAD no está en el path de Python.")
    sys.exit(1)

def crear_enchufe_lavanderia_3d():
    doc = FreeCAD.newDocument("Enchufe_Estanco_Lavanderia_IP55")

    # 1. Caja estanca de superficie IP55 en ABS / Policarbonato (160 x 120 x 85 mm)
    caja = Part.makeBox(160, 120, 85)
    caja.translate(FreeCAD.Vector(-80, -60, 0))

    cavidad = Part.makeBox(152, 112, 79)
    cavidad.translate(FreeCAD.Vector(-76, -56, 3))
    carcasa = caja.cut(cavidad)

    # 2. Tapa frontal abatible con dos compuertas con muelle para tomas Schuko
    tapa = Part.makeBox(158, 118, 5)
    tapa.translate(FreeCAD.Vector(-79, -59, 83))

    compuerta1 = Part.makeBox(55, 55, 8)
    compuerta1.translate(FreeCAD.Vector(-65, -27.5, 86))

    compuerta2 = Part.makeBox(55, 55, 8)
    compuerta2.translate(FreeCAD.Vector(10, -27.5, 86))

    # 3. Dos prensaestopas estancos PG16 en la parte inferior para entrada de cables
    prensa1 = Part.makeCylinder(11, 20, FreeCAD.Vector(-35, -60, 42.5), FreeCAD.Vector(0, -1, 0))
    prensa2 = Part.makeCylinder(11, 20, FreeCAD.Vector(35, -60, 42.5), FreeCAD.Vector(0, -1, 0))

    # 4. Base antivibratoria / silentblock de caucho vulcanizado (Soporte lavadora)
    base_anti = Part.makeCylinder(40, 25, FreeCAD.Vector(0, 0, -25), FreeCAD.Vector(0, 0, 1))

    modelo = carcasa.fuse([tapa, compuerta1, compuerta2, prensa1, prensa2, base_anti])

    obj = doc.addObject("Part::Feature", "Enchufe_Lavanderia_IP55")
    obj.Shape = modelo

    if hasattr(obj, "ViewObject") and obj.ViewObject:
        obj.ViewObject.ShapeColor = (0.35, 0.45, 0.55) # Gris azulado estanco
        obj.ViewObject.Transparency = 10

    doc.recompute()

    output_dir = "/home/ral/Documents/GitHub/open-source-domotics/04_telemetria_y_cargas_criticas/03_cargas_lavanderia/mecanico"
    os.makedirs(output_dir, exist_ok=True)

    fcstd_path = os.path.join(output_dir, "enchufe_estanco_lavanderia_antivibracion.FCStd")
    step_path = os.path.join(output_dir, "enchufe_estanco_lavanderia_antivibracion.step")

    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)
    print(f"Modelo Enchufe Lavandería FreeCAD generado: {fcstd_path}")
    print(f"Modelo Enchufe Lavandería STEP exportado: {step_path}")

if __name__ == "__main__":
    crear_enchufe_lavanderia_3d()

