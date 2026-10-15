#!/usr/bin/env python3
"""
generar_solar_pv_3d.py
Genera el modelo paramétrico 3D de la estructura de soporte coplanar/triangular de paneles solares fotovoltaicos
(2 módulos bifaciales de 550W de 2278 x 1134 x 35 mm inclinados a 30° sur) en FreeCAD 1.1+ y exporta a STEP AP214.
Estructura en perfilería de aluminio AL6005-T5, grapas intermedias/finales, anclajes de acero inoxidable A2
y bandeja de microinversores/caja de conexiones.
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

def crear_solar_pv_3d():
    doc = FreeCAD.newDocument("Estructura_Solar_Fotovoltaica_550W")

    inclinacion_deg = 30.0
    rad = math.radians(inclinacion_deg)

    # 1. Vigas base horizontales sobre cubierta (perfil 40x40x2400 mm)
    viga_base_1 = Part.makeBox(40, 2400, 40)
    viga_base_1.translate(FreeCAD.Vector(-600, -1200, 0))

    viga_base_2 = Part.makeBox(40, 2400, 40)
    viga_base_2.translate(FreeCAD.Vector(600, -1200, 0))

    # 2. Triángulos de sustentación inclinados a 30°
    # Pilar trasero vertical (altura = 2300 * sin(30°) = 1150 mm)
    pilar_post_1 = Part.makeBox(40, 40, 1150)
    pilar_post_1.translate(FreeCAD.Vector(-600, 1000, 40))

    pilar_post_2 = Part.makeBox(40, 40, 1150)
    pilar_post_2.translate(FreeCAD.Vector(600, 1000, 40))

    # Tirante diagonal de arriostramiento contra viento
    tirante_1 = Part.makeBox(40, 40, 1300)
    tirante_1.rotate(FreeCAD.Vector(-600, 1000, 40), FreeCAD.Vector(1, 0, 0), -45)
    tirante_2 = Part.makeBox(40, 40, 1300)
    tirante_2.rotate(FreeCAD.Vector(600, 1000, 40), FreeCAD.Vector(1, 0, 0), -45)

    # 3. Carriles de aluminio inclinados a 30° (longitud 2350 mm)
    carril_1 = Part.makeBox(40, 2350, 40)
    carril_1.translate(FreeCAD.Vector(-600, -1000, 40))
    carril_1.rotate(FreeCAD.Vector(-600, -1000, 40), FreeCAD.Vector(1, 0, 0), inclinacion_deg)

    carril_2 = Part.makeBox(40, 2350, 40)
    carril_2.translate(FreeCAD.Vector(600, -1000, 40))
    carril_2.rotate(FreeCAD.Vector(600, -1000, 40), FreeCAD.Vector(1, 0, 0), inclinacion_deg)

    # 4. Dos módulos fotovoltaicos de 550W (2278 x 1134 x 35 mm cada uno)
    # Colocados en orientación vertical (portrait) lado a lado
    # Marco de panel 1
    panel_1 = Part.makeBox(1134, 2278, 35)
    panel_1.translate(FreeCAD.Vector(-1144, -980, 80))
    panel_1.rotate(FreeCAD.Vector(-1144, -980, 80), FreeCAD.Vector(1, 0, 0), inclinacion_deg)

    # Marco de panel 2
    panel_2 = Part.makeBox(1134, 2278, 35)
    panel_2.translate(FreeCAD.Vector(10, -980, 80))
    panel_2.rotate(FreeCAD.Vector(10, -980, 80), FreeCAD.Vector(1, 0, 0), inclinacion_deg)

    # 5. Caja estanca combinadora de strings / microinversor en la parte posterior
    caja_pv = Part.makeBox(280, 140, 240)
    caja_pv.translate(FreeCAD.Vector(-140, 600, 400))

    estructura = viga_base_1.fuse([viga_base_2, pilar_post_1, pilar_post_2, tirante_1, tirante_2, carril_1, carril_2, caja_pv])
    solido_final = estructura.fuse([panel_1, panel_2])

    obj = doc.addObject("Part::Feature", "Estructura_Solar_Fotovoltaica")
    obj.Shape = solido_final

    if hasattr(obj, "ViewObject") and obj.ViewObject:
        obj.ViewObject.ShapeColor = (0.2, 0.25, 0.35) # Azul oscuro / silicio policristalino
        obj.ViewObject.Transparency = 0

    doc.recompute()

    output_dir = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/03_solar_fotovoltaica/mecanico"
    os.makedirs(output_dir, exist_ok=True)

    fcstd_path = os.path.join(output_dir, "estructura_montaje_coplanar_pv.FCStd")
    step_path = os.path.join(output_dir, "estructura_montaje_coplanar_pv.step")

    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)

    print(f"Éxito: Modelo 3D guardado en {fcstd_path}")
    print(f"Éxito: Archivo STEP exportado en {step_path}")

if __name__ == "__main__":
    crear_solar_pv_3d()
