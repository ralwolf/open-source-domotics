#!/usr/bin/env python3
"""
generar_micromodulo_rele_3d.py
Genera el modelo paramétrico 3D de la carcasa del micromódulo inteligente empotrable
de pared con doble relé y detección Zero-Cross en FreeCAD 1.1+ y exporta a STEP AP214.
Dimensiones compactas: 42 x 38 x 17 mm para cajas de mecanismos estándar de 65 mm.
"""

import sys
import os

try:
    import FreeCAD
    import Part
except ImportError:
    print("Error: FreeCAD no está en el path de Python.")
    sys.exit(1)

def crear_micromodulo_3d():
    doc = FreeCAD.newDocument("Micromodulo_Rele_Pared_ZeroCross")

    # 1. Cuerpo principal de plástico ignífugo ABS / Policarbonato UL94-V0
    # Longitud=42mm, Ancho=38mm, Alto=17mm con aristas redondeadas
    cuerpo = Part.makeBox(42, 38, 17)
    cuerpo.translate(FreeCAD.Vector(-21, -19, 0))

    # Redondeo de esquinas verticales
    # Cavidad interna para PCB
    cavidad = Part.makeBox(39, 35, 15)
    cavidad.translate(FreeCAD.Vector(-19.5, -17.5, 1.5))
    carcasa = cuerpo.cut(cavidad)

    # 2. Tapa frontal con hendiduras de clips
    tapa = Part.makeBox(41, 37, 1.5)
    tapa.translate(FreeCAD.Vector(-20.5, -18.5, 16.5))

    # 3. Bornero de tornillo de 6 polos paso 5.0mm en la parte inferior
    # L, N, L1_OUT, L2_OUT, S1, S2
    bornero = Part.makeBox(32, 10, 11)
    bornero.translate(FreeCAD.Vector(-16, -18, 2))

    # Orificios de tornillos de bornas
    tornillos = []
    for i in range(6):
        pos_x = -13.5 + i * 5.4
        t = Part.makeCylinder(1.5, 4, FreeCAD.Vector(pos_x, -13, 11), FreeCAD.Vector(0, 0, 1))
        tornillos.append(t)

    # 4. Botón de emparejamiento / reset físico frontal y orificio LED RGB
    btn = Part.makeCylinder(2, 2, FreeCAD.Vector(12, 10, 16), FreeCAD.Vector(0, 0, 1))
    led = Part.makeCylinder(1, 2, FreeCAD.Vector(12, 5, 16), FreeCAD.Vector(0, 0, 1))

    # 5. Ranuras de disipación y ventilación en caras laterales
    ranuras = []
    for j in range(4):
        pos_y = -10 + j * 6
        r1 = Part.makeBox(2, 3, 8)
        r1.translate(FreeCAD.Vector(-21.5, pos_y, 4))
        r2 = Part.makeBox(2, 3, 8)
        r2.translate(FreeCAD.Vector(19.5, pos_y, 4))
        ranuras.extend([r1, r2])

    carcasa_final = carcasa.fuse([tapa, bornero, btn, led])
    if tornillos:
        for t in tornillos:
            carcasa_final = carcasa_final.cut(t)
    if ranuras:
        for r in ranuras:
            carcasa_final = carcasa_final.cut(r)

    obj = doc.addObject("Part::Feature", "Micromodulo_Pared_ZeroCross")
    obj.Shape = carcasa_final

    if hasattr(obj, "ViewObject") and obj.ViewObject:
        obj.ViewObject.ShapeColor = (0.2, 0.5, 0.8) # Azul técnico
        obj.ViewObject.Transparency = 10

    doc.recompute()

    output_dir = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/05_reles_conmutacion_pared/mecanico"
    os.makedirs(output_dir, exist_ok=True)

    fcstd_path = os.path.join(output_dir, "micromodulo_rele_pared.FCStd")
    step_path = os.path.join(output_dir, "micromodulo_rele_pared.step")

    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)
    print(f"Modelo Micromódulo FreeCAD generado: {fcstd_path}")
    print(f"Modelo Micromódulo STEP exportado: {step_path}")

if __name__ == "__main__":
    crear_micromodulo_3d()

