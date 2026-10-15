#!/usr/bin/env python3
"""
Generador de Modelo 3D FreeCAD 1.1+
Proyecto: Colector de Distribución Hidráulica (AF/ACS/Retorno) y Manifold de Gas Dual
Módulo: 00_diseno_arquitectonico_y_estructural/05_instalaciones_hidraulicas_y_gas/planos_fontaneria
"""

import sys
import os

try:
    import FreeCAD
    import Part
    from FreeCAD import Base, Vector
except ImportError:
    print("Error: Este script debe ser ejecutado bajo el entorno FreeCAD (freecadcmd).")
    sys.exit(1)

def generar_colector_fluidos_3d(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    fcstd_path = os.path.join(output_dir, "colector_conmutacion_gas_y_fontaneria.FCStd")
    step_path = os.path.join(output_dir, "colector_conmutacion_gas_y_fontaneria.step")

    doc = FreeCAD.newDocument("ColectoresFluidosYGas")

    # 1. Manifold Hidráulico de Agua Fría (AF) en Latón Niquelado (1" x 4 vías de 1/2")
    # Ubicado a Z=300 mm
    L_man = 320.0
    barril_af = Part.makeCylinder(16.0, L_man, Vector(0, 0, 300.0), Vector(1, 0, 0))
    hueco_af = Part.makeCylinder(13.0, L_man + 10.0, Vector(-5.0, 0, 300.0), Vector(1, 0, 0))
    manifold_af = barril_af.cut(hueco_af)

    derivaciones_af = []
    for x_pos in [60.0, 130.0, 200.0, 270.0]:
        valv = Part.makeCylinder(10.0, 45.0, Vector(x_pos, 0, 300.0), Vector(0, 0, -1))
        mando = Part.makeBox(25.0, 10.0, 8.0, Vector(x_pos - 12.5, -5.0, 275.0))
        derivaciones_af.append(valv)
        derivaciones_af.append(mando)
    deriv_af_comp = Part.makeCompound(derivaciones_af)

    # 2. Manifold Hidráulico de Agua Caliente Sanitaria (ACS) en Latón (1" x 4 vías de 1/2")
    # Ubicado a Z=450 mm
    barril_acs = Part.makeCylinder(16.0, L_man, Vector(0, 0, 450.0), Vector(1, 0, 0))
    hueco_acs = Part.makeCylinder(13.0, L_man + 10.0, Vector(-5.0, 0, 450.0), Vector(1, 0, 0))
    manifold_acs = barril_acs.cut(hueco_acs)

    derivaciones_acs = []
    for x_pos in [60.0, 130.0, 200.0, 270.0]:
        valv = Part.makeCylinder(10.0, 45.0, Vector(x_pos, 0, 450.0), Vector(0, 0, -1))
        mando = Part.makeBox(25.0, 10.0, 8.0, Vector(x_pos - 12.5, -5.0, 425.0))
        derivaciones_acs.append(valv)
        derivaciones_acs.append(mando)
    deriv_acs_comp = Part.makeCompound(derivaciones_acs)

    # 3. Bomba de Recirculación de Retorno ACS (Rotor húmedo 24V, X=-80, Y=0, Z=450)
    cuerpo_bomba = Part.makeCylinder(35.0, 70.0, Vector(-80.0, 0, 415.0), Vector(0, 0, 1))
    motor_bomba = Part.makeCylinder(28.0, 80.0, Vector(-80.0, 0, 450.0), Vector(0, 1, 0))
    bomba_recirc = cuerpo_bomba.fuse(motor_bomba)

    # 4. Colector de Conmutación de Gas Dual (Cobre rígido 3/4" y Válvulas Solenoides)
    # Ubicado en plano Y=120 mm, Z=200 mm
    tubo_gas_red = Part.makeCylinder(10.0, 180.0, Vector(30.0, 120.0, 100.0), Vector(0, 0, 1))
    tubo_gas_glp = Part.makeCylinder(10.0, 180.0, Vector(180.0, 120.0, 100.0), Vector(0, 0, 1))
    tubo_colector_gas = Part.makeCylinder(12.0, 240.0, Vector(0, 120.0, 280.0), Vector(1, 0, 0))

    # Electroválvulas Solenoides de Gas NC de rearme manual (2x)
    solenoide_red = Part.makeBox(35.0, 45.0, 50.0, Vector(12.5, 97.5, 180.0))
    bobina_red = Part.makeCylinder(15.0, 30.0, Vector(30.0, 120.0, 230.0), Vector(0, 0, 1))
    valv_gas_red = solenoide_red.fuse(bobina_red)

    solenoide_glp = Part.makeBox(35.0, 45.0, 50.0, Vector(162.5, 97.5, 180.0))
    bobina_glp = Part.makeCylinder(15.0, 30.0, Vector(180.0, 120.0, 230.0), Vector(0, 0, 1))
    valv_gas_glp = solenoide_glp.fuse(bobina_glp)

    # Manómetros de glicerina para control de presión (0-60 mbar)
    mano_red = Part.makeCylinder(22.0, 15.0, Vector(30.0, 150.0, 260.0), Vector(0, 1, 0))
    mano_glp = Part.makeCylinder(22.0, 15.0, Vector(180.0, 150.0, 260.0), Vector(0, 1, 0))
    manometros = mano_red.fuse(mano_glp)

    gas_tuberia = Part.makeCompound([tubo_gas_red, tubo_gas_glp, tubo_colector_gas])
    gas_valvulas = Part.makeCompound([valv_gas_red, valv_gas_glp])

    # 5. Bastidor / Placa de montaje en pared (chapa galvanizada 500 x 600 mm)
    placa_bastidor = Part.makeBox(480.0, 3.0, 500.0, Vector(-100.0, -15.0, 80.0))

    # Agregar objetos al documento FreeCAD
    obj_af = doc.addObject("Part::Feature", "Manifold_Agua_Fria_Latón")
    obj_af.Shape = Part.makeCompound([manifold_af, deriv_af_comp])
    if hasattr(obj_af, "ViewObject") and obj_af.ViewObject:
        obj_af.ViewObject.ShapeColor = (0.2, 0.5, 0.8)

    obj_acs = doc.addObject("Part::Feature", "Manifold_ACS_Laton")
    obj_acs.Shape = Part.makeCompound([manifold_acs, deriv_acs_comp])
    if hasattr(obj_acs, "ViewObject") and obj_acs.ViewObject:
        obj_acs.ViewObject.ShapeColor = (0.85, 0.3, 0.2)

    obj_bomba = doc.addObject("Part::Feature", "Bomba_Recirculacion_ACS")
    obj_bomba.Shape = bomba_recirc
    if hasattr(obj_bomba, "ViewObject") and obj_bomba.ViewObject:
        obj_bomba.ViewObject.ShapeColor = (0.15, 0.65, 0.3)

    obj_gas_tub = doc.addObject("Part::Feature", "Red_Gas_Cobre_Tipo_L")
    obj_gas_tub.Shape = gas_tuberia
    if hasattr(obj_gas_tub, "ViewObject") and obj_gas_tub.ViewObject:
        obj_gas_tub.ViewObject.ShapeColor = (0.8, 0.5, 0.2)

    obj_gas_valv = doc.addObject("Part::Feature", "Electrovalvulas_Gas_NC")
    obj_gas_valv.Shape = gas_valvulas
    if hasattr(obj_gas_valv, "ViewObject") and obj_gas_valv.ViewObject:
        obj_gas_valv.ViewObject.ShapeColor = (0.85, 0.75, 0.1)

    obj_manos = doc.addObject("Part::Feature", "Manometros_Presion_Gas")
    obj_manos.Shape = manometros
    if hasattr(obj_manos, "ViewObject") and obj_manos.ViewObject:
        obj_manos.ViewObject.ShapeColor = (0.9, 0.9, 0.9)

    obj_bast = doc.addObject("Part::Feature", "Bastidor_Montaje_Pared")
    obj_bast.Shape = placa_bastidor
    if hasattr(obj_bast, "ViewObject") and obj_bast.ViewObject:
        obj_bast.ViewObject.ShapeColor = (0.7, 0.7, 0.72)

    doc.recompute()
    doc.saveAs(fcstd_path)

    # Exportar modelo de intercambio STEP
    Part.export([obj_af, obj_acs, obj_bomba, obj_gas_tub, obj_gas_valv, obj_manos, obj_bast], step_path)

    print(f"Modelo FreeCAD guardado en: {fcstd_path}")
    print(f"Modelo STEP exportado en: {step_path}")

if __name__ == "__main__":
    out_dir = "/home/ral/Documents/GitHub/open-source-domotics/00_diseno_arquitectonico_y_estructural/05_instalaciones_hidraulicas_y_gas/planos_fontaneria"
    generar_colector_fluidos_3d(out_dir)

