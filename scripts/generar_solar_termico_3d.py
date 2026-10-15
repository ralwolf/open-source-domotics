#!/usr/bin/env python3
"""
generar_solar_termico_3d.py
Genera el modelo paramétrico 3D del sistema Solar Térmico y Calefacción por Suelo Radiante
(Captador solar de 30 tubos de vacío heat-pipe y depósito de inercia estratificado de 500L con aislamiento de 50 mm)
en FreeCAD 1.1+ y exporta a STEP AP214.
"""

import sys
import os
import math

try:
    import FreeCAD
    import Part
except ImportError:
    print("Error: FreeCAD no está en el path de Python.")
    sys.exit(1)

def crear_solar_termico_3d():
    doc = FreeCAD.newDocument("Solar_Termico_Acumulador_500L")

    # 1. Depósito de inercia estratificado 500 L (diámetro 750 mm, altura 1750 mm)
    # Cuerpo cilíndrico aislado
    tanque_cuerpo = Part.makeCylinder(375, 1500, FreeCAD.Vector(-800, 0, 100), FreeCAD.Vector(0, 0, 1))
    tapa_sup = Part.makeSphere(375, FreeCAD.Vector(-800, 0, 1600))
    # Recorte para semiesfera superior
    box_corte = Part.makeBox(800, 800, 400)
    box_corte.translate(FreeCAD.Vector(-1200, -400, 1200))
    tapa = tapa_sup.cut(box_corte)

    # Base soporte del acumulador
    soporte_tanque = Part.makeCylinder(360, 100, FreeCAD.Vector(-800, 0, 0), FreeCAD.Vector(0, 0, 1))

    # Tomas hidráulicas (bridas 1" y vainas para sondas PT1000)
    toma_solar_ret = Part.makeCylinder(20, 60, FreeCAD.Vector(-800, 360, 250), FreeCAD.Vector(0, 1, 0))
    toma_solar_imp = Part.makeCylinder(20, 60, FreeCAD.Vector(-800, 360, 750), FreeCAD.Vector(0, 1, 0))
    toma_suelo_imp = Part.makeCylinder(25, 60, FreeCAD.Vector(-800, 360, 1200), FreeCAD.Vector(0, 1, 0))
    toma_suelo_ret = Part.makeCylinder(25, 60, FreeCAD.Vector(-800, 360, 450), FreeCAD.Vector(0, 1, 0))

    tanque_completo = tanque_cuerpo.fuse([tapa, soporte_tanque, toma_solar_ret, toma_solar_imp, toma_suelo_imp, toma_suelo_ret])

    # 2. Vaso de expansión solar (diámetro 280 mm, altura 450 mm, 24 litros)
    vaso_exp = Part.makeCylinder(140, 400, FreeCAD.Vector(-300, 200, 150), FreeCAD.Vector(0, 0, 1))
    vaso_soporte = Part.makeCylinder(30, 150, FreeCAD.Vector(-300, 200, 0), FreeCAD.Vector(0, 0, 1))
    vaso = vaso_exp.fuse(vaso_soporte)

    # 3. Captador solar de tubos de vacío heat-pipe (30 tubos)
    # Cabezal colector superior horizontal (aislado, diámetro 120 mm, largo 2000 mm)
    inclinacion = 45.0
    x_colector = 500.0

    colector_sup = Part.makeBox(2000, 140, 120)
    colector_sup.translate(FreeCAD.Vector(x_colector - 1000, -70, 1400))

    # Tubos de vacío (cilindros de 58 mm diámetro, largo 1800 mm)
    tubos = []
    num_tubos = 15 # Representación simplificada de tubos principales
    for i in range(num_tubos):
        tx = x_colector - 900 + i * 125.0
        tubo = Part.makeCylinder(29, 1800, FreeCAD.Vector(tx, 0, 1400), FreeCAD.Vector(0, 1, 0))
        tubo.rotate(FreeCAD.Vector(tx, 0, 1400), FreeCAD.Vector(1, 0, 0), -inclinacion)
        tubos.append(tubo)

    # Estructura de soporte del captador
    pata_1 = Part.makeBox(40, 40, 1400)
    pata_1.translate(FreeCAD.Vector(x_colector - 980, -60, 0))
    pata_2 = Part.makeBox(40, 40, 1400)
    pata_2.translate(FreeCAD.Vector(x_colector + 940, -60, 0))

    captador_estructura = colector_sup.fuse([pata_1, pata_2] + tubos)

    # Fusión final
    solido_final = tanque_completo.fuse([vaso, captador_estructura])

    obj = doc.addObject("Part::Feature", "Sistema_Solar_Termico_Calefaccion")
    obj.Shape = solido_final

    if hasattr(obj, "ViewObject") and obj.ViewObject:
        obj.ViewObject.ShapeColor = (0.7, 0.72, 0.75) # Acero inoxidable / aluminio
        obj.ViewObject.Transparency = 0

    doc.recompute()

    output_dir = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/02_solar_termico_y_calefaccion/mecanico"
    os.makedirs(output_dir, exist_ok=True)

    fcstd_path = os.path.join(output_dir, "colector_termico_estratificacion_3d.FCStd")
    step_path = os.path.join(output_dir, "colector_termico_estratificacion_3d.step")

    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)

    print(f"Éxito: Modelo 3D guardado en {fcstd_path}")
    print(f"Éxito: Archivo STEP exportado en {step_path}")

if __name__ == "__main__":
    crear_solar_termico_3d()

