#!/usr/bin/env python3
"""
Generador de Modelo 3D FreeCAD 1.1+
Proyecto: Caseta Técnica, Filtro de Arena, Colectores y Dosificadores de Piscina
Módulo: 05_confort_y_exteriores/04_mantenimiento_automatizado_piscina/mecanico
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

def generar_piscina_3d(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    fcstd_path = os.path.join(output_dir, "caseta_tecnica_piscina_filtro.FCStd")
    step_path = os.path.join(output_dir, "caseta_tecnica_piscina_filtro.step")

    doc = FreeCAD.newDocument("CasetaTecnicaPiscina")

    # 1. Base / Solera de la caseta técnica (1200 x 900 x 50 mm)
    base_losa = Part.makeBox(1200, 900, 50, Vector(0, 0, 0))

    # 2. Filtro de lecho de arena/vidrio laminado en poliéster (D=500mm, H=750mm)
    # Ubicado en X=350, Y=450
    cx_filtro, cy_filtro = 350.0, 450.0
    filtro_cuerpo = Part.makeCylinder(250, 500, Vector(cx_filtro, cy_filtro, 100), Vector(0, 0, 1))
    filtro_cupula = Part.makeSphere(250, Vector(cx_filtro, cy_filtro, 600))
    # Recortar mitad inferior de la esfera
    recorte_inf = Part.makeBox(600, 600, 300, Vector(cx_filtro - 300, cy_filtro - 300, 300))
    filtro_tapa = filtro_cupula.cut(recorte_inf)
    filtro_peana = Part.makeCylinder(180, 50, Vector(cx_filtro, cy_filtro, 50), Vector(0, 0, 1))
    filtro_total = Part.makeCompound([filtro_peana, filtro_cuerpo, filtro_tapa])

    # Válvula selectora lateral de 6 vías (X=130, Y=450, Z=450)
    valvula_6v = Part.makeCylinder(75, 120, Vector(cx_filtro - 220, cy_filtro, 450), Vector(1, 0, 0))
    palanca = Part.makeBox(20, 140, 20, Vector(cx_filtro - 220, cy_filtro - 70, 570))
    valvula_total = valvula_6v.fuse(palanca)

    # 3. Bomba de recirculación autoaspirante (0.75 kW / 1 CV)
    # Ubicada en X=850, Y=450
    cx_bomba, cy_bomba = 850.0, 450.0
    motor_bomba = Part.makeCylinder(80, 240, Vector(cx_bomba, cy_bomba, 140), Vector(1, 0, 0))
    carcasa_turbina = Part.makeCylinder(110, 100, Vector(cx_bomba - 100, cy_bomba, 140), Vector(1, 0, 0))
    prefiltro_cesta = Part.makeCylinder(75, 180, Vector(cx_bomba - 200, cy_bomba, 100), Vector(0, 0, 1))
    peana_bomba = Part.makeBox(380, 180, 50, Vector(cx_bomba - 240, cy_bomba - 90, 50))
    bomba_total = Part.makeCompound([peana_bomba, prefiltro_cesta, carcasa_turbina, motor_bomba])

    # 4. Tuberías de PVC Presión D=50mm
    tubo1 = Part.makeCylinder(25, 300, Vector(cx_filtro - 150, cy_filtro, 450), Vector(1, 0, 0))
    tubo2 = Part.makeCylinder(25, 200, Vector(cx_bomba - 100, cy_bomba, 140), Vector(0, 0, 1))
    tubo3 = Part.makeCylinder(25, 350, Vector(cx_bomba - 100, cy_bomba, 340), Vector(-1, 0, 0))
    tuberias = Part.makeCompound([tubo1, tubo2, tubo3])

    # 5. Cámara de análisis en By-pass transparente para electrodos de pH y ORP
    # Ubicada en X=600, Y=750, Z=400
    camara_bypass = Part.makeCylinder(40, 150, Vector(600, 750, 300), Vector(0, 0, 1))
    sonda_ph = Part.makeCylinder(8, 120, Vector(585, 750, 380), Vector(0, 0, 1))
    sonda_orp = Part.makeCylinder(8, 120, Vector(615, 750, 380), Vector(0, 0, 1))
    bypass_analisis = Part.makeCompound([camara_bypass, sonda_ph, sonda_orp])

    # 6. Bombas dosificadoras peristálticas (2x montadas en pared de caseta X=1050)
    # Peristáltica 1: pH- (X=1050, Y=700, Z=450)
    dosi_ph = Part.makeBox(90, 110, 140, Vector(1050, 650, 400))
    rotor_ph = Part.makeCylinder(30, 25, Vector(1050, 705, 470), Vector(-1, 0, 0))
    # Peristáltica 2: Cloro (X=1050, Y=250, Z=450)
    dosi_cl = Part.makeBox(90, 110, 140, Vector(1050, 200, 400))
    rotor_cl = Part.makeCylinder(30, 25, Vector(1050, 255, 470), Vector(-1, 0, 0))
    dosificadoras = Part.makeCompound([dosi_ph, rotor_ph, dosi_cl, rotor_cl])

    # 7. Cuadro Eléctrico e Inmunidad IP65 (X=200, Y=150, Z=400)
    cuadro = Part.makeBox(120, 250, 300, Vector(150, 50, 400))

    # Agregar objetos al documento FreeCAD
    obj_base = doc.addObject("Part::Feature", "Solera_Hormigon")
    obj_base.Shape = base_losa
    if hasattr(obj_base, "ViewObject") and obj_base.ViewObject:
        obj_base.ViewObject.ShapeColor = (0.7, 0.7, 0.7)

    obj_filtro = doc.addObject("Part::Feature", "Filtro_Arena_D500")
    obj_filtro.Shape = filtro_total
    if hasattr(obj_filtro, "ViewObject") and obj_filtro.ViewObject:
        obj_filtro.ViewObject.ShapeColor = (0.1, 0.5, 0.8)

    obj_valv = doc.addObject("Part::Feature", "Valvula_Selectora_6V")
    obj_valv.Shape = valvula_total
    if hasattr(obj_valv, "ViewObject") and obj_valv.ViewObject:
        obj_valv.ViewObject.ShapeColor = (0.2, 0.2, 0.2)

    obj_bomba = doc.addObject("Part::Feature", "Bomba_Autoaspirante_1CV")
    obj_bomba.Shape = bomba_total
    if hasattr(obj_bomba, "ViewObject") and obj_bomba.ViewObject:
        obj_bomba.ViewObject.ShapeColor = (0.15, 0.65, 0.3)

    obj_tubos = doc.addObject("Part::Feature", "Tuberias_PVC_D50")
    obj_tubos.Shape = tuberias
    if hasattr(obj_tubos, "ViewObject") and obj_tubos.ViewObject:
        obj_tubos.ViewObject.ShapeColor = (0.3, 0.3, 0.35)

    obj_bypass = doc.addObject("Part::Feature", "Bypass_Sondas_pH_ORP")
    obj_bypass.Shape = bypass_analisis
    if hasattr(obj_bypass, "ViewObject") and obj_bypass.ViewObject:
        obj_bypass.ViewObject.ShapeColor = (0.8, 0.9, 1.0)
        obj_bypass.ViewObject.Transparency = 50

    obj_dosi = doc.addObject("Part::Feature", "Bombas_Peristalticas_Dosificadoras")
    obj_dosi.Shape = dosificadoras
    if hasattr(obj_dosi, "ViewObject") and obj_dosi.ViewObject:
        obj_dosi.ViewObject.ShapeColor = (0.9, 0.4, 0.1)

    obj_cuadro = doc.addObject("Part::Feature", "Cuadro_Control_IP65")
    obj_cuadro.Shape = cuadro
    if hasattr(obj_cuadro, "ViewObject") and obj_cuadro.ViewObject:
        obj_cuadro.ViewObject.ShapeColor = (0.85, 0.85, 0.85)

    doc.recompute()
    doc.saveAs(fcstd_path)

    # Exportar modelo de intercambio STEP del ensamble completo
    Part.export([obj_base, obj_filtro, obj_valv, obj_bomba, obj_tubos, obj_bypass, obj_dosi, obj_cuadro], step_path)

    print(f"Modelo FreeCAD guardado en: {fcstd_path}")
    print(f"Modelo STEP exportado en: {step_path}")

if __name__ == "__main__":
    out_dir = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/04_mantenimiento_automatizado_piscina/mecanico"
    generar_piscina_3d(out_dir)
