#!/usr/bin/env python3
"""
generar_actuador_valvula_3d.py
Genera el modelo paramétrico 3D del Actuador Motorizado de Corte Rápido para Válvulas de Bola (Agua y Gas)
en FreeCAD 1.1+ y exporta a STEP AP214.
Dimensiones: 100 x 70 x 85 mm, carcasa IP65, motorreductor 12V DC con reductor planetario metálico,
soporte de abrazadera a tubería de 3/4" y 1", horquilla mecánica de arrastre de palanca y anilla de embrague manual.
"""

import sys
import os

try:
    import FreeCAD
    import Part
except ImportError:
    print("Error: FreeCAD no está en el path de Python.")
    sys.exit(1)

def crear_actuador_valvula_3d():
    doc = FreeCAD.newDocument("Actuador_Motorizado_Valvula_Bola")

    # 1. Carcasa principal del actuador (100 x 70 x 60 mm)
    caja_ext = Part.makeBox(100, 70, 60)
    caja_ext.translate(FreeCAD.Vector(-50, -35, 25))

    cavidad_int = Part.makeBox(94, 64, 56)
    cavidad_int.translate(FreeCAD.Vector(-47, -32, 27))
    carcasa = caja_ext.cut(cavidad_int)

    # Tapa superior con botón de test local y LED indicador bicolor
    tapa_sup = Part.makeBox(100, 70, 5)
    tapa_sup.translate(FreeCAD.Vector(-50, -35, 85))
    boton_test = Part.makeCylinder(6, 4, FreeCAD.Vector(-20, 0, 90), FreeCAD.Vector(0, 0, 1))
    led_estado = Part.makeCylinder(3, 3, FreeCAD.Vector(20, 0, 90), FreeCAD.Vector(0, 0, 1))

    # 2. Eje rotativo de salida y horquilla de arrastre de la maneta de la válvula
    eje_salida = Part.makeCylinder(10, 25, FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1))
    brazo_horquilla = Part.makeBox(80, 20, 8)
    brazo_horquilla.translate(FreeCAD.Vector(-15, -10, 8))
    # Perno de arrastre que abraza la maneta de la válvula
    pivote_arrastre = Part.makeCylinder(6, 25, FreeCAD.Vector(55, 0, -17), FreeCAD.Vector(0, 0, 1))

    # 3. Anilla / pomo de desbloqueo manual (embrague) en la parte inferior
    anilla_embrague = Part.makeCylinder(8, 20, FreeCAD.Vector(-30, 0, 5), FreeCAD.Vector(0, 0, -1))
    aro_tirador = Part.makeTorus(10, 3, FreeCAD.Vector(-30, 0, -15), FreeCAD.Vector(1, 0, 0))

    # 4. Soporte metálico y abrazadera ajustable de fijación a la tubería
    soporte_l = Part.makeBox(6, 60, 100)
    soporte_l.translate(FreeCAD.Vector(-56, -30, -15))

    # Abrazadera en U (U-Bolt) para tubos de 3/4" (Ø26.9 mm) a 1" (Ø33.7 mm)
    abrazadera_u = Part.makeCylinder(18, 50, FreeCAD.Vector(-80, -25, -25), FreeCAD.Vector(0, 1, 0))
    abrazadera_hueco = Part.makeCylinder(14, 52, FreeCAD.Vector(-80, -26, -25), FreeCAD.Vector(0, 1, 0))
    u_bolt = abrazadera_u.cut(abrazadera_hueco)

    # Válvula de bola y tubería de referencia (Ø28 mm)
    tubo_ref = Part.makeCylinder(14, 160, FreeCAD.Vector(-80, -80, -25), FreeCAD.Vector(0, 1, 0))
    cuerpo_valvula = Part.makeBox(40, 50, 40)
    cuerpo_valvula.translate(FreeCAD.Vector(-100, -25, -45))
    palanca_valvula = Part.makeBox(120, 16, 4)
    palanca_valvula.translate(FreeCAD.Vector(-95, -8, -5))

    solido_actuador = carcasa.fuse([tapa_sup, boton_test, led_estado, eje_salida, brazo_horquilla, pivote_arrastre, anilla_embrague, aro_tirador, soporte_l, u_bolt])
    solido_completo = solido_actuador.fuse([tubo_ref, cuerpo_valvula, palanca_valvula])

    obj = doc.addObject("Part::Feature", "Actuador_Valvula_Corte_Rapido")
    obj.Shape = solido_completo

    if hasattr(obj, "ViewObject") and obj.ViewObject:
        obj.ViewObject.ShapeColor = (0.85, 0.25, 0.2) # Rojo seguridad industrial
        obj.ViewObject.Transparency = 5

    doc.recompute()

    output_dir = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/03_actuadores_valvulas_gas_agua/mecanico"
    os.makedirs(output_dir, exist_ok=True)

    fcstd_path = os.path.join(output_dir, "actuador_motorizado_valvula_3d.FCStd")
    step_path = os.path.join(output_dir, "actuador_motorizado_valvula_3d.step")

    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)

    print(f"Éxito: Modelo 3D guardado en {fcstd_path}")
    print(f"Éxito: Archivo STEP exportado en {step_path}")

if __name__ == "__main__":
    crear_actuador_valvula_3d()
