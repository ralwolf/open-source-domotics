#!/usr/bin/env python3
"""
generar_oficina_pdu_3d.py
Genera el modelo paramétrico 3D de la PDU técnica de escritorio para la oficina
con tomas filtradas EMI/RFI y señalizador frontal "ON AIR / EN LLAMADA" en FreeCAD 1.1+ y exporta a STEP AP214.
Dimensiones: 240 x 70 x 45 mm, soporte de fijación a tablero de mesa y difusor LED.
"""

import sys
import os

try:
    import FreeCAD
    import Part
except ImportError:
    print("Error: FreeCAD no está en el path de Python.")
    sys.exit(1)

def crear_pdu_oficina_3d():
    doc = FreeCAD.newDocument("PDU_Escritorio_Oficina_OnAir")

    # 1. Carcasa principal de perfil de aluminio extruido (240 x 70 x 45 mm)
    caja = Part.makeBox(240, 70, 45)
    caja.translate(FreeCAD.Vector(-120, -35, 0))

    cavidad = Part.makeBox(234, 64, 41)
    cavidad.translate(FreeCAD.Vector(-117, -32, 2))
    carcasa = caja.cut(cavidad)

    # 2. Tomas Schuko frontales (3 tomas filtradas EMI)
    tomas = []
    for i in range(3):
        pos_x = -70 + i * 45
        t = Part.makeCylinder(19, 4, FreeCAD.Vector(pos_x, 0, 43), FreeCAD.Vector(0, 0, 1))
        tomas.append(t)

    # 3. Módulo frontal señalizador luminoso "ON AIR" con difusor acrílico (60 x 25 mm)
    on_air_caja = Part.makeBox(60, 25, 4)
    on_air_caja.translate(FreeCAD.Vector(50, -12.5, 43))

    # 4. Mordaza / pinza de sujeción al borde del escritorio (espesor mesa 25-40 mm)
    mordaza_u = Part.makeBox(40, 20, 60)
    mordaza_u.translate(FreeCAD.Vector(-20, -55, -20))
    mordaza_hueco = Part.makeBox(42, 22, 45)
    mordaza_hueco.translate(FreeCAD.Vector(-21, -56, -10))
    pinza = mordaza_u.cut(mordaza_hueco)

    # Pomo de apriete manual
    pomo = Part.makeCylinder(12, 15, FreeCAD.Vector(0, -45, -25), FreeCAD.Vector(0, 0, 1))

    modelo = carcasa.fuse([on_air_caja, pinza, pomo])
    for t in tomas:
        modelo = modelo.cut(t)

    obj = doc.addObject("Part::Feature", "PDU_Escritorio_Oficina")
    obj.Shape = modelo

    if hasattr(obj, "ViewObject") and obj.ViewObject:
        obj.ViewObject.ShapeColor = (0.2, 0.2, 0.22) # Negro mate anodizado
        obj.ViewObject.Transparency = 5

    doc.recompute()

    output_dir = "/home/ral/Documents/GitHub/open-source-domotics/04_telemetria_y_cargas_criticas/04_cargas_oficina/mecanico"
    os.makedirs(output_dir, exist_ok=True)

    fcstd_path = os.path.join(output_dir, "pdu_escritorio_oficina_con_senalizador.FCStd")
    step_path = os.path.join(output_dir, "pdu_escritorio_oficina_con_senalizador.step")

    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)
    print(f"Modelo PDU Oficina FreeCAD generado: {fcstd_path}")
    print(f"Modelo PDU Oficina STEP exportado: {step_path}")

if __name__ == "__main__":
    crear_pdu_oficina_3d()

