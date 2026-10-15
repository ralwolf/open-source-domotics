#!/usr/bin/env python3
"""
generar_vmc_recuperador_3d.py
Genera el modelo paramétrico 3D de la unidad de Ventilación Mecánica Controlada (VMC)
de doble flujo con intercambiador de calor entálpico, compuerta de bypass para free-cooling
y toberas de conexión aeráulicas DN160 en FreeCAD 1.1+ y exporta a formato neutral STEP AP214.
"""

import sys
import os

try:
    import FreeCAD
    import Part
except ImportError:
    print("Error: FreeCAD no está en el path de Python.")
    sys.exit(1)

def crear_unidad_vmc():
    doc = FreeCAD.newDocument("Unidad_VMC_Recuperador_Entalpico")

    # 1. Carcasa principal de chapa galvanizada con aislamiento termoacústico
    # Dimensiones: Largo=720mm, Ancho=620mm, Alto=280mm
    cuerpo = Part.makeBox(720, 620, 280)
    cuerpo.translate(FreeCAD.Vector(-360, -310, 0))

    # Tapa y rebajes para inspección frontal
    tapa = Part.makeBox(700, 600, 20)
    tapa.translate(FreeCAD.Vector(-350, -300, 270))

    # 2. Intercambiador entálpico hexagonal de flujo contracorriente (núcleo central)
    nucleo = Part.makeBox(320, 320, 240)
    nucleo.rotate(FreeCAD.Vector(0, 0, 120), FreeCAD.Vector(0, 0, 1), 45)
    nucleo.translate(FreeCAD.Vector(0, 0, 20))

    # 3. Cuatro toberas aeráulicas DN160 (diámetro exterior 160mm, pared 2mm, longitud 70mm)
    # T1: Admisión de aire exterior (Izquierda - Trasera)
    t1 = Part.makeCylinder(80, 70, FreeCAD.Vector(-360, 160, 140), FreeCAD.Vector(-1, 0, 0))
    t1_hueco = Part.makeCylinder(77, 80, FreeCAD.Vector(-360, 160, 140), FreeCAD.Vector(-1, 0, 0))
    tobera1 = t1.cut(t1_hueco)

    # T2: Extracción de aire viciado húmedo (Izquierda - Delantera)
    t2 = Part.makeCylinder(80, 70, FreeCAD.Vector(-360, -160, 140), FreeCAD.Vector(-1, 0, 0))
    t2_hueco = Part.makeCylinder(77, 80, FreeCAD.Vector(-360, -160, 140), FreeCAD.Vector(-1, 0, 0))
    tobera2 = t2.cut(t2_hueco)

    # T3: Impulsión de aire nuevo a estancias secas (Derecha - Trasera)
    t3 = Part.makeCylinder(80, 70, FreeCAD.Vector(360, 160, 140), FreeCAD.Vector(1, 0, 0))
    t3_hueco = Part.makeCylinder(77, 80, FreeCAD.Vector(360, 160, 140), FreeCAD.Vector(1, 0, 0))
    tobera3 = t3.cut(t3_hueco)

    # T4: Expulsión de aire viciado al exterior (Derecha - Delantera)
    t4 = Part.makeCylinder(80, 70, FreeCAD.Vector(360, -160, 140), FreeCAD.Vector(1, 0, 0))
    t4_hueco = Part.makeCylinder(77, 80, FreeCAD.Vector(360, -160, 140), FreeCAD.Vector(1, 0, 0))
    tobera4 = t4.cut(t4_hueco)

    # 4. Compuerta motorizada de bypass (Free-Cooling) 24V y actuador Belimo
    servomotor = Part.makeBox(60, 90, 80)
    servomotor.translate(FreeCAD.Vector(-340, 240, 180))

    eje_damper = Part.makeCylinder(6, 40, FreeCAD.Vector(-310, 285, 260), FreeCAD.Vector(0, 0, 1))

    # 5. Bandeja de condensados y racor de drenaje DN20 con sifón de bola
    drenaje = Part.makeCylinder(12, 50, FreeCAD.Vector(250, -250, 0), FreeCAD.Vector(0, 0, -1))
    drenaje_h = Part.makeCylinder(9, 60, FreeCAD.Vector(250, -250, 5), FreeCAD.Vector(0, 0, -1))
    drenaje_tubo = drenaje.cut(drenaje_h)

    # 6. Soportes antivibratorios y pletinas de fijación al techo
    p1 = Part.makeBox(40, 70, 8)
    p1.translate(FreeCAD.Vector(-380, 250, 272))
    p2 = Part.makeBox(40, 70, 8)
    p2.translate(FreeCAD.Vector(-380, -320, 272))
    p3 = Part.makeBox(40, 70, 8)
    p3.translate(FreeCAD.Vector(340, 250, 272))
    p4 = Part.makeBox(40, 70, 8)
    p4.translate(FreeCAD.Vector(340, -320, 272))

    # Combinación de sólidos
    unidad = cuerpo.fuse([tapa, tobera1, tobera2, tobera3, tobera4, servomotor, eje_damper, drenaje_tubo, p1, p2, p3, p4])

    obj = doc.addObject("Part::Feature", "Unidad_VMC_DobleFlujo")
    obj.Shape = unidad

    if hasattr(obj, "ViewObject") and obj.ViewObject:
        obj.ViewObject.ShapeColor = (0.85, 0.88, 0.90) # Gris metálico
        obj.ViewObject.Transparency = 15

    doc.recompute()

    output_dir = "/home/ral/Documents/GitHub/open-source-domotics/04_telemetria_y_cargas_criticas/06_climatizacion_vmc_recuperador_calor/mecanico"
    os.makedirs(output_dir, exist_ok=True)

    fcstd_path = os.path.join(output_dir, "unidad_vmc_recuperador_entalpico.FCStd")
    step_path = os.path.join(output_dir, "unidad_vmc_recuperador_entalpico.step")

    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)
    print(f"Modelo VMC FreeCAD generado: {fcstd_path}")
    print(f"Modelo VMC STEP exportado: {step_path}")

if __name__ == "__main__":
    crear_unidad_vmc()

