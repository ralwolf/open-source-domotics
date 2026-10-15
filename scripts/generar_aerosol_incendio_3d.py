#!/usr/bin/env python3
"""
Generador de Modelo 3D FreeCAD 1.1+
Proyecto: Cápsula Extintora de Aerosol Condensado (Stat-X/FirePro) y Detector Óptico EN54
Módulo: 03_seguridad_y_control_acceso/07_seguridad_incendio_co_y_aerosoles/mecanico
"""

import sys
import os
import math

try:
    import FreeCAD
    import Part
    from FreeCAD import Base, Vector
except ImportError:
    print("Error: Este script debe ser ejecutado bajo el entorno FreeCAD (freecadcmd).")
    sys.exit(1)

def generar_aerosol_incendio_3d(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    fcstd_path = os.path.join(output_dir, "capsula_extincion_aerosol_soporte.FCStd")
    step_path = os.path.join(output_dir, "capsula_extincion_aerosol_soporte.step")

    doc = FreeCAD.newDocument("ExtincionAerosolIncendio")

    # 1. Cápsula generadora de aerosol condensado (D=75 mm, H=160 mm)
    # Acero inoxidable AISI 304 pulido
    R_cap = 37.5
    H_cap = 160.0

    cuerpo_cil = Part.makeCylinder(R_cap, H_cap - 20.0, Vector(0, 0, 20.0), Vector(0, 0, 1))
    tapa_sup = Part.makeSphere(R_cap, Vector(0, 0, H_cap))
    # Recortar mitad inferior
    recorte = Part.makeBox(100, 100, 50, Vector(-50, -50, H_cap - 50))
    tapa_cupula = tapa_sup.cut(recorte)

    # Conector de disparo eléctrico superior hermético (M12 2-pin)
    conector_disp = Part.makeCylinder(6.0, 15.0, Vector(0, 0, H_cap + 10.0), Vector(0, 0, 1))

    # Boquilla inferior de descarga radial 360° con ranuras
    boquilla_base = Part.makeCylinder(R_cap - 5.0, 20.0, Vector(0, 0, 0), Vector(0, 0, 1))
    ranuras = []
    for i in range(8):
        ang = math.radians(i * 45.0)
        rx, ry = (R_cap - 2.0) * math.cos(ang), (R_cap - 2.0) * math.sin(ang)
        ranura = Part.makeBox(8.0, 4.0, 12.0, Vector(rx - 4.0, ry - 2.0, 4.0))
        ranuras.append(ranura)
    ranuras_comp = Part.makeCompound(ranuras)
    boquilla_ranurada = boquilla_base.cut(ranuras_comp)

    capsula_aerosol = Part.makeCompound([cuerpo_cil, tapa_cupula, conector_disp, boquilla_ranurada])

    # 2. Soporte de fijación a rack / pared con aislamiento térmico (Abrazadera de acero 2 mm)
    abra_base = Part.makeBox(120.0, 15.0, 3.0, Vector(-60.0, -R_cap - 18.0, 80.0))
    abra_cil_ext = Part.makeCylinder(R_cap + 4.0, 30.0, Vector(0, 0, 65.0), Vector(0, 0, 1))
    abra_cil_int = Part.makeCylinder(R_cap, 35.0, Vector(0, 0, 62.0), Vector(0, 0, 1))
    abrazadera_anillo = abra_cil_ext.cut(abra_cil_int)
    # Recorte mitad trasera de la abrazadera para formar abrazadera en U
    corte_u = Part.makeBox(120.0, R_cap + 10.0, 40.0, Vector(-60.0, 0, 60.0))
    abrazadera_u = abrazadera_anillo.cut(corte_u)
    soporte_montaje = abra_base.fuse(abrazadera_u)

    # 3. Detector óptico de humo EN54 (ubicado al lado a X=140, Y=0, Z=100)
    # Diámetro 100 mm, altura 45 mm
    det_base = Part.makeCylinder(50.0, 15.0, Vector(140.0, 0, 130.0), Vector(0, 0, 1))
    det_cono = Part.makeCone(50.0, 40.0, 25.0, Vector(140.0, 0, 105.0), Vector(0, 0, 1))
    det_camara = Part.makeCylinder(35.0, 10.0, Vector(140.0, 0, 95.0), Vector(0, 0, 1))
    det_led = Part.makeCylinder(2.5, 3.0, Vector(140.0, 38.0, 108.0), Vector(0, 1, 0))
    detector_humo = Part.makeCompound([det_base, det_cono, det_camara, det_led])

    # Agregar objetos al documento FreeCAD
    obj_capsula = doc.addObject("Part::Feature", "Capsula_Aerosol_StatX")
    obj_capsula.Shape = capsula_aerosol
    if hasattr(obj_capsula, "ViewObject") and obj_capsula.ViewObject:
        obj_capsula.ViewObject.ShapeColor = (0.85, 0.2, 0.2)

    obj_soporte = doc.addObject("Part::Feature", "Soporte_Abrazadera_Rack")
    obj_soporte.Shape = soporte_montaje
    if hasattr(obj_soporte, "ViewObject") and obj_soporte.ViewObject:
        obj_soporte.ViewObject.ShapeColor = (0.4, 0.42, 0.45)

    obj_detector = doc.addObject("Part::Feature", "Detector_Humo_EN54")
    obj_detector.Shape = detector_humo
    if hasattr(obj_detector, "ViewObject") and obj_detector.ViewObject:
        obj_detector.ViewObject.ShapeColor = (0.95, 0.95, 0.95)

    doc.recompute()
    doc.saveAs(fcstd_path)

    # Exportar modelo de intercambio STEP
    Part.export([obj_capsula, obj_soporte, obj_detector], step_path)

    print(f"Modelo FreeCAD guardado en: {fcstd_path}")
    print(f"Modelo STEP exportado en: {step_path}")

if __name__ == "__main__":
    out_dir = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/07_seguridad_incendio_co_y_aerosoles/mecanico"
    generar_aerosol_incendio_3d(out_dir)
