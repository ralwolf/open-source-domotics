#!/usr/bin/env python3
"""
Generador de Modelo 3D FreeCAD 1.1+
Proyecto: Mecanismo de Persiana Enrollable con Eje Octogonal de 60 mm y Motor Tubular
Módulo: 03_seguridad_y_control_acceso/04_cortinas_y_persianas_motorizadas/mecanico
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

def generar_persiana_3d(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    fcstd_path = os.path.join(output_dir, "mecanismo_persiana_eje_octogonal.FCStd")
    step_path = os.path.join(output_dir, "mecanismo_persiana_eje_octogonal.step")

    doc = FreeCAD.newDocument("MecanismoPersianaMotorizada")

    # Longitud representativa de ventana: L = 1200 mm
    L = 1200.0
    R_octo = 30.0  # Radio exterior del eje octogonal de 60 mm

    # 1. Eje tubular octogonal de acero galvanizado (D=60 mm, espesor 0.8 mm)
    # Crear prisma regular octogonal
    pts = []
    for i in range(8):
        ang = math.radians(i * 45.0)
        pts.append(Vector(R_octo * math.cos(ang), R_octo * math.sin(ang), 0))
    pts.append(pts[0])
    wire_octo = Part.makePolygon(pts)
    face_octo = Part.Face(wire_octo)
    eje_octogonal = face_octo.extrude(Vector(0, 0, L))

    # Cavidad interior hueca
    pts_int = []
    for i in range(8):
        ang = math.radians(i * 45.0)
        pts_int.append(Vector((R_octo - 1.2) * math.cos(ang), (R_octo - 1.2) * math.sin(ang), -5))
    pts_int.append(pts_int[0])
    wire_int = Part.makePolygon(pts_int)
    face_int = Part.Face(wire_int)
    hueco = face_int.extrude(Vector(0, 0, L + 10))
    eje_octogonal = eje_octogonal.cut(hueco)

    # 2. Motor tubular embutido en el extremo derecho (longitud 520 mm, D=45 mm)
    motor_cuerpo = Part.makeCylinder(22.5, 520, Vector(0, 0, L - 520), Vector(0, 0, 1))
    # Corona adaptadora de arrastre octogonal (Z=L-500)
    corona_arrastre = Part.makeCylinder(28.5, 30, Vector(0, 0, L - 500), Vector(0, 0, 1))
    # Cabeza en estrella del motor con finales de carrera (Z=L a L+25 mm)
    cabeza_motor = Part.makeCylinder(35.0, 25, Vector(0, 0, L), Vector(0, 0, 1))
    motor_total = Part.makeCompound([motor_cuerpo, corona_arrastre, cabeza_motor])

    # 3. Soporte / Placa de testero motor (acero estampado 100 x 100 x 3 mm)
    placa_soporte_der = Part.makeBox(100, 100, 3.0, Vector(-50, -50, L + 25))

    # 4. Contera plástica y rodamiento con espiga en el extremo izquierdo (Z=-30 a Z=0)
    contera = Part.makeCylinder(28.0, 40, Vector(0, 0, -10), Vector(0, 0, 1))
    espiga_eje = Part.makeCylinder(6.0, 30, Vector(0, 0, -40), Vector(0, 0, 1))
    soporte_izq = Part.makeBox(100, 100, 3.0, Vector(-50, -50, -43))
    contera_total = Part.makeCompound([contera, espiga_eje, soporte_izq])

    # 5. Paño de persiana enrollada representativo (cilindro de lamas de aluminio Z=100 a L-100)
    paño_lamas = Part.makeCylinder(65.0, L - 200, Vector(0, 0, 100), Vector(0, 0, 1))
    hueco_paño = Part.makeCylinder(32.0, L - 200, Vector(0, 0, 100), Vector(0, 0, 1))
    paño_lamas = paño_lamas.cut(hueco_paño)

    # Lamas cayendo hacia abajo (representación parcial 4 lamas de 45 mm cada una)
    lamas_descendiendo = Part.makeBox(180, 12, L - 200, Vector(-R_octo - 65, -12, 100))

    # Agregar objetos al documento FreeCAD
    obj_eje = doc.addObject("Part::Feature", "Eje_Octogonal_60mm")
    obj_eje.Shape = eje_octogonal
    if hasattr(obj_eje, "ViewObject") and obj_eje.ViewObject:
        obj_eje.ViewObject.ShapeColor = (0.7, 0.72, 0.75)

    obj_motor = doc.addObject("Part::Feature", "Motor_Tubular_20Nm")
    obj_motor.Shape = motor_total
    if hasattr(obj_motor, "ViewObject") and obj_motor.ViewObject:
        obj_motor.ViewObject.ShapeColor = (0.15, 0.15, 0.18)

    obj_contera = doc.addObject("Part::Feature", "Contera_Rodamiento_Soporte")
    obj_contera.Shape = contera_total
    if hasattr(obj_contera, "ViewObject") and obj_contera.ViewObject:
        obj_contera.ViewObject.ShapeColor = (0.8, 0.8, 0.85)

    obj_lamas = doc.addObject("Part::Feature", "Paño_Lamas_Aluminio")
    obj_lamas.Shape = Part.makeCompound([paño_lamas, lamas_descendiendo])
    if hasattr(obj_lamas, "ViewObject") and obj_lamas.ViewObject:
        obj_lamas.ViewObject.ShapeColor = (0.9, 0.9, 0.92)

    doc.recompute()
    doc.saveAs(fcstd_path)

    # Exportar modelo de intercambio STEP del ensamble completo
    Part.export([obj_eje, obj_motor, obj_contera, obj_lamas], step_path)

    print(f"Modelo FreeCAD guardado en: {fcstd_path}")
    print(f"Modelo STEP exportado en: {step_path}")

if __name__ == "__main__":
    out_dir = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/04_cortinas_y_persianas_motorizadas/mecanico"
    generar_persiana_3d(out_dir)

