#!/usr/bin/env python3
"""
generar_multisplit_interfaz_3d.py
Genera el modelo paramétrico 3D de la pasarela IoT de interfaz CN105 / Midea UART
para splits y el conjunto de bancada antivibratoria exterior en FreeCAD 1.1+ y exporta a STEP AP214.
"""

import sys
import os

try:
    import FreeCAD
    import Part
except ImportError:
    print("Error: FreeCAD no está en el path de Python.")
    sys.exit(1)

def crear_multisplit_3d():
    doc = FreeCAD.newDocument("Pasarela_MultiSplit_IoT_Bancada")

    # 1. Carcasa ultra-compacta para la pasarela IoT interna (60 x 40 x 16 mm)
    caja = Part.makeBox(60, 40, 16)
    caja.translate(FreeCAD.Vector(-30, -20, 0))

    cavidad = Part.makeBox(56, 36, 14)
    cavidad.translate(FreeCAD.Vector(-28, -18, 2))
    carcasa_iot = caja.cut(cavidad)

    # Tapa con clips
    tapa = Part.makeBox(58, 38, 1.5)
    tapa.translate(FreeCAD.Vector(-29, -19, 15))

    # Abertura para conector JST-PA de 5 pines (cable CN105)
    hueco_cable = Part.makeBox(12, 6, 8)
    hueco_cable.translate(FreeCAD.Vector(-6, -21, 4))
    carcasa_iot = carcasa_iot.cut(hueco_cable)

    # Ventana para sensor SHT31 (ranuras en la tapa)
    r1 = Part.makeBox(8, 2, 3)
    r1.translate(FreeCAD.Vector(-4, 5, 14.5))
    r2 = Part.makeBox(8, 2, 3)
    r2.translate(FreeCAD.Vector(-4, 10, 14.5))
    tapa = tapa.cut(r1).cut(r2)

    pasarela_completa = carcasa_iot.fuse(tapa)

    # 2. Bancada antivibratoria de unidad exterior (Soporte en escuadra con silentblocks de caucho)
    # Perfil en L de acero galvanizado (450 mm largo, 400 mm alto)
    brazo_h = Part.makeBox(450, 50, 4)
    brazo_h.translate(FreeCAD.Vector(50, -25, 0))

    brazo_v = Part.makeBox(4, 50, 400)
    brazo_v.translate(FreeCAD.Vector(50, -25, 0))

    tirante = Part.makeBox(300, 4, 300)
    tirante.translate(FreeCAD.Vector(50, -2, 0))

    # Dos amortiguadores cónicos de caucho EPDM (Silentblocks Ø40 x 30 mm con espárrago M8)
    s1 = Part.makeCylinder(20, 30, FreeCAD.Vector(150, 0, 4), FreeCAD.Vector(0, 0, 1))
    s1_esparrago = Part.makeCylinder(4, 25, FreeCAD.Vector(150, 0, 34), FreeCAD.Vector(0, 0, 1))

    s2 = Part.makeCylinder(20, 30, FreeCAD.Vector(400, 0, 4), FreeCAD.Vector(0, 0, 1))
    s2_esparrago = Part.makeCylinder(4, 25, FreeCAD.Vector(400, 0, 34), FreeCAD.Vector(0, 0, 1))

    bancada = brazo_h.fuse([brazo_v, s1, s1_esparrago, s2, s2_esparrago])

    # Unir todo el conjunto
    modelo_total = pasarela_completa.fuse(bancada)

    obj = doc.addObject("Part::Feature", "Pasarela_Split_IoT_y_Bancada")
    obj.Shape = modelo_total

    if hasattr(obj, "ViewObject") and obj.ViewObject:
        obj.ViewObject.ShapeColor = (0.7, 0.75, 0.8) # Acabado industrial
        obj.ViewObject.Transparency = 10

    doc.recompute()

    output_dir = "/home/ral/Documents/GitHub/open-source-domotics/04_telemetria_y_cargas_criticas/05_climatizacion_multisplit/mecanico"
    os.makedirs(output_dir, exist_ok=True)

    fcstd_path = os.path.join(output_dir, "pasarela_split_iot_y_bancada.FCStd")
    step_path = os.path.join(output_dir, "pasarela_split_iot_y_bancada.step")

    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)
    print(f"Modelo MultiSplit FreeCAD generado: {fcstd_path}")
    print(f"Modelo MultiSplit STEP exportado: {step_path}")

if __name__ == "__main__":
    crear_multisplit_3d()

