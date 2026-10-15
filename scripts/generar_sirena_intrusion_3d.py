#!/usr/bin/env python3
"""
Generador de Modelo 3D FreeCAD 1.1+
Proyecto: Sirena Exterior de Alta Seguridad 120dB y Columna de Barrera Infrarroja
Módulo: 03_seguridad_y_control_acceso/08_intrusion_perimetral_sensores_y_sirena/mecanico
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

def generar_sirena_intrusion_3d(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    fcstd_path = os.path.join(output_dir, "sirena_exterior_y_barrera_infrarroja.FCStd")
    step_path = os.path.join(output_dir, "sirena_exterior_y_barrera_infrarroja.step")

    doc = FreeCAD.newDocument("SirenaYBarreraPerimetral")

    # 1. Carcasa de Sirena Exterior Autolimentada IP65 / IK08
    # Dimensiones: Ancho 200 mm, Alto 280 mm, Profundidad 85 mm
    W_sir = 200.0
    H_sir = 280.0
    D_sir = 85.0

    # Base posterior en policarbonato blanco
    base_sir = Part.makeBox(W_sir, D_sir - 15.0, H_sir, Vector(-W_sir/2.0, 0, 0))
    # Tapa frontal abombada
    tapa_sir = Part.makeBox(W_sir - 4.0, 15.0, H_sir - 4.0, Vector(-(W_sir - 4.0)/2.0, D_sir - 15.0, 2.0))

    # Difusor de Flash Estroboscópico de policarbonato rojo superior (ancho 160 mm, alto 60 mm)
    strobe_red = Part.makeBox(160.0, 8.0, 60.0, Vector(-80.0, D_sir - 2.0, H_sir - 75.0))

    # Rejilla acústica inferior para transductor de compresión piezoeléctrico de 120 dB
    rejillas = []
    for z_pos in range(40, 140, 15):
        rej = Part.makeBox(140.0, 5.0, 6.0, Vector(-70.0, D_sir - 2.0, z_pos))
        rejillas.append(rej)
    rejillas_comp = Part.makeCompound(rejillas)
    tapa_sir = tapa_sir.cut(rejillas_comp)

    sirena_ensamble = Part.makeCompound([base_sir, tapa_sir])

    # 2. Reja interior de acero antiespuma y antitaladro (chapa zincada de 1.5 mm)
    reja_acero = Part.makeBox(W_sir - 20.0, 2.0, H_sir - 30.0, Vector(-(W_sir - 20.0)/2.0, D_sir - 20.0, 15.0))

    # 3. Columna de Barrera Infrarroja Activa (AIR) Perimetral (X=220 mm)
    # Perfil elíptico / cilíndrico de aluminio anodizado negro (D=70 mm, H=450 mm)
    col_x = 220.0
    columna_al = Part.makeCylinder(35.0, 450.0, Vector(col_x, 30.0, 0), Vector(0, 0, 1))
    # Ventana frontal de policarbonato con filtro IR oscuro (ancho 40 mm, alto 430 mm)
    visor_ir = Part.makeBox(40.0, 10.0, 430.0, Vector(col_x - 20.0, 30.0 + 30.0, 10.0))
    # Tapa superior e inferior de la columna
    tapa_col_inf = Part.makeCylinder(42.0, 15.0, Vector(col_x, 30.0, 0), Vector(0, 0, 1))
    tapa_col_sup = Part.makeCylinder(42.0, 15.0, Vector(col_x, 30.0, 450.0), Vector(0, 0, 1))
    barrera_air = Part.makeCompound([columna_al, visor_ir, tapa_col_inf, tapa_col_sup])

    # 4. Sensor Acústico de Rotura de Cristal (X=-200 mm, Y=30 mm, Z=100 mm)
    # Carcasa compacta 80 x 50 x 25 mm
    sensor_vidrio = Part.makeBox(80.0, 25.0, 50.0, Vector(-240.0, 20.0, 100.0))
    micro_piezo = Part.makeCylinder(8.0, 4.0, Vector(-200.0, 45.0, 125.0), Vector(0, 1, 0))
    sensor_rotura = sensor_vidrio.fuse(micro_piezo)

    # Agregar objetos al documento FreeCAD
    obj_sirena = doc.addObject("Part::Feature", "Sirena_Exterior_120dB")
    obj_sirena.Shape = sirena_ensamble
    if hasattr(obj_sirena, "ViewObject") and obj_sirena.ViewObject:
        obj_sirena.ViewObject.ShapeColor = (0.9, 0.9, 0.92)

    obj_strobe = doc.addObject("Part::Feature", "Difusor_Flash_Strobe_Rojo")
    obj_strobe.Shape = strobe_red
    if hasattr(obj_strobe, "ViewObject") and obj_strobe.ViewObject:
        obj_strobe.ViewObject.ShapeColor = (0.95, 0.1, 0.1)
        obj_strobe.ViewObject.Transparency = 30

    obj_blindaje = doc.addObject("Part::Feature", "Blindaje_Acero_Antiespuma")
    obj_blindaje.Shape = reja_acero
    if hasattr(obj_blindaje, "ViewObject") and obj_blindaje.ViewObject:
        obj_blindaje.ViewObject.ShapeColor = (0.6, 0.62, 0.65)

    obj_air = doc.addObject("Part::Feature", "Barrera_Infrarroja_AIR")
    obj_air.Shape = barrera_air
    if hasattr(obj_air, "ViewObject") and obj_air.ViewObject:
        obj_air.ViewObject.ShapeColor = (0.15, 0.15, 0.18)

    obj_rotura = doc.addObject("Part::Feature", "Sensor_Rotura_Cristal")
    obj_rotura.Shape = sensor_rotura
    if hasattr(obj_rotura, "ViewObject") and obj_rotura.ViewObject:
        obj_rotura.ViewObject.ShapeColor = (0.85, 0.85, 0.85)

    doc.recompute()
    doc.saveAs(fcstd_path)

    # Exportar modelo de intercambio STEP
    Part.export([obj_sirena, obj_strobe, obj_blindaje, obj_air, obj_rotura], step_path)

    print(f"Modelo FreeCAD guardado en: {fcstd_path}")
    print(f"Modelo STEP exportado en: {step_path}")

if __name__ == "__main__":
    out_dir = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/08_intrusion_perimetral_sensores_y_sirena/mecanico"
    generar_sirena_intrusion_3d(out_dir)

