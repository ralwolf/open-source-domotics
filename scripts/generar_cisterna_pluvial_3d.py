#!/usr/bin/env python3
"""
generar_cisterna_pluvial_3d.py
Genera el modelo paramétrico 3D de la Cisterna Pluvial Enterrada de 10.000 L y el Skid de Filtración y Desinfección UV-C
en FreeCAD 1.1+ y exporta a STEP AP214.
Dimensiones cisterna: Ø2400 x 2600 mm con registro DN600, filtro vórtex,
skid de presurización, 3 etapas de cartuchos filtrantes (20µm, carbón, 1µm) y esterilizador UV-C de acero inoxidable.
"""

import sys
import os

try:
    import FreeCAD
    import Part
except ImportError:
    print("Error: FreeCAD no está en el path de Python.")
    sys.exit(1)

def crear_cisterna_pluvial_3d():
    doc = FreeCAD.newDocument("Cisterna_Pluvial_Skid_10000L")

    # 1. Cisterna enterrada cilíndrica de 10.000 Litros (Ø2400 x 2600 mm)
    tanque_ext = Part.makeCylinder(1200, 2600, FreeCAD.Vector(-1500, 0, 0), FreeCAD.Vector(0, 0, 1))
    tanque_int = Part.makeCylinder(1150, 2500, FreeCAD.Vector(-1500, 0, 50), FreeCAD.Vector(0, 0, 1))
    cisterna = tanque_ext.cut(tanque_int)

    # Cuello y registro de inspección DN600 con tapa
    cuello = Part.makeCylinder(300, 400, FreeCAD.Vector(-1500, 0, 2600), FreeCAD.Vector(0, 0, 1))
    tapa_registro = Part.makeCylinder(340, 40, FreeCAD.Vector(-1500, 0, 3000), FreeCAD.Vector(0, 0, 1))

    # Filtro vórtex de entrada pluvial DN110
    tubo_entrada = Part.makeCylinder(55, 300, FreeCAD.Vector(-1500, -1300, 2400), FreeCAD.Vector(0, 1, 0))
    tubo_rebosadero = Part.makeCylinder(55, 300, FreeCAD.Vector(-1500, 1100, 2350), FreeCAD.Vector(0, 1, 0))

    conjunto_cisterna = cisterna.fuse([cuello, tapa_registro, tubo_entrada, tubo_rebosadero])

    # 2. Skid de potabilización y presurización (Bancada sobre sala técnica contigua)
    # Bancada de acero inoxidable (800 x 400 x 40 mm)
    bancada = Part.makeBox(800, 400, 40)
    bancada.translate(FreeCAD.Vector(400, -200, 0))

    # Bomba centrífuga multietapa vertical / presurizador (diámetro 180, altura 550)
    bomba = Part.makeCylinder(90, 550, FreeCAD.Vector(500, 0, 40), FreeCAD.Vector(0, 0, 1))
    motor_bomba = Part.makeBox(140, 140, 200)
    motor_bomba.translate(FreeCAD.Vector(430, -70, 350))
    bomba_completa = bomba.fuse(motor_bomba)

    # Tren de 3 filtros de cartucho Big Blue 10" (Ø180 mm, altura 350 mm cada uno)
    filtros = []
    for i in range(3):
        fx = 720 + i * 160
        f_vaso = Part.makeCylinder(70, 350, FreeCAD.Vector(fx, 0, 150), FreeCAD.Vector(0, 0, 1))
        f_cabezal = Part.makeBox(120, 120, 60)
        f_cabezal.translate(FreeCAD.Vector(fx - 60, -60, 500))
        filtros.append(f_vaso.fuse(f_cabezal))

    # Cámara de desinfección UV-C en acero inoxidable AISI 304 (diámetro 90, largo 950 mm horizontal)
    uvc_cilindro = Part.makeCylinder(45, 950, FreeCAD.Vector(420, 0, 650), FreeCAD.Vector(1, 0, 0))
    uvc_brida1 = Part.makeCylinder(20, 80, FreeCAD.Vector(480, 0, 650), FreeCAD.Vector(0, 0, 1))
    uvc_brida2 = Part.makeCylinder(20, 80, FreeCAD.Vector(1300, 0, 650), FreeCAD.Vector(0, 0, 1))
    camara_uvc = uvc_cilindro.fuse([uvc_brida1, uvc_brida2])

    # Cuadro eléctrico y balastro electrónico UV (250 x 200 x 120 mm)
    cuadro_control = Part.makeBox(250, 120, 300)
    cuadro_control.translate(FreeCAD.Vector(800, -180, 40))

    skid_potabilizacion = bancada.fuse([bomba_completa, camara_uvc, cuadro_control] + filtros)

    # Fusión total
    solido_final = conjunto_cisterna.fuse(skid_potabilizacion)

    obj = doc.addObject("Part::Feature", "Cisterna_Pluvial_y_Skid_Potabilizacion")
    obj.Shape = solido_final

    if hasattr(obj, "ViewObject") and obj.ViewObject:
        obj.ViewObject.ShapeColor = (0.3, 0.45, 0.6) # Azul polietileno técnico
        obj.ViewObject.Transparency = 10

    doc.recompute()

    output_dir = "/home/ral/Documents/GitHub/open-source-domotics/00_diseno_arquitectonico_y_estructural/07_captacion_pluvial_cisterna_y_potabilizacion/mecanico"
    os.makedirs(output_dir, exist_ok=True)

    fcstd_path = os.path.join(output_dir, "cisterna_y_skid_potabilizacion_3d.FCStd")
    step_path = os.path.join(output_dir, "cisterna_y_skid_potabilizacion_3d.step")

    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)

    print(f"Éxito: Modelo 3D guardado en {fcstd_path}")
    print(f"Éxito: Archivo STEP exportado en {step_path}")

if __name__ == "__main__":
    crear_cisterna_pluvial_3d()
