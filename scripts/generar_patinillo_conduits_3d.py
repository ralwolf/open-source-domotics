#!/usr/bin/env python3
"""
generar_patinillo_conduits_3d.py
Genera el modelo paramétrico 3D del Patinillo Técnico Vertical de Instalaciones Segregadas
conforme a ITC-BT-21, CTE DB-HS y UNE-EN 50174 en FreeCAD 1.1+ y exporta a STEP AP214.
Dimensiones patinillo: 1200 x 400 x 3200 mm, bandejas Rejiband segregadas para Potencia BT y Telecomunicaciones Cat6A,
bajante pluvial/sanitaria insonorizada DN110, PE-Xa fontanería 1" con coquilla y sellados cortafuegos EI-60.
"""

import sys
import os

try:
    import FreeCAD
    import Part
except ImportError:
    print("Error: FreeCAD no está en el path de Python.")
    sys.exit(1)

def crear_patinillo_conduits_3d():
    doc = FreeCAD.newDocument("Patinillo_Instalaciones_Segregadas")

    ancho = 1200.0
    profundidad = 400.0
    altura = 3200.0
    espesor_muro = 100.0

    # 1. Envolvente del patinillo en fábrica de ladrillo / cartón-yeso cortafuegos EI-60
    caja_ext = Part.makeBox(ancho, profundidad, altura)
    caja_ext.translate(FreeCAD.Vector(-ancho/2.0, -profundidad/2.0, 0))

    cavidad_int = Part.makeBox(ancho - 2*espesor_muro, profundidad - 2*espesor_muro, altura + 10)
    cavidad_int.translate(FreeCAD.Vector(-ancho/2.0 + espesor_muro, -profundidad/2.0 + espesor_muro, -5))
    patinillo_muros = caja_ext.cut(cavidad_int)

    # Puerta de registro metálica EI-60 frontal (600 x 1800 mm en cota Z: 600..2400)
    hueco_puerta = Part.makeBox(600, espesor_muro + 20, 1800)
    hueco_puerta.translate(FreeCAD.Vector(-300, -profundidad/2.0 - 10, 600))
    patinillo = patinillo_muros.cut(hueco_puerta)

    puerta_registro = Part.makeBox(590, 15, 1790)
    puerta_registro.translate(FreeCAD.Vector(-295, -profundidad/2.0 + 10, 605))

    # 2. Bandeja portacables de rejilla (Rejiband) para Potencia Eléctrica BT (200 x 60 x 3200 mm)
    # Lado izquierdo del patinillo (X = -350 mm)
    bandeja_potencia = Part.makeBox(200, 60, altura)
    bandeja_potencia.translate(FreeCAD.Vector(-450, 20, 0))

    # Conductores de potencia en el interior (3 cables de 16 mm² y mangueras corrugadas)
    cables_potencia = []
    for cx in [-410, -380, -350, -320, -290]:
        c = Part.makeCylinder(9, altura, FreeCAD.Vector(cx, 50, 0), FreeCAD.Vector(0, 0, 1))
        cables_potencia.append(c)

    # 3. Bandeja portacables para Telecomunicaciones y Fibra Óptica (150 x 60 x 3200 mm)
    # Lado derecho, manteniendo separación normativa >300 mm respecto a potencia (X = +100 mm)
    bandeja_datos = Part.makeBox(150, 60, altura)
    bandeja_datos.translate(FreeCAD.Vector(50, 20, 0))

    # Mazo de cables Cat6A apantallados U/FTP y tubo verde de fibra óptica
    cables_datos = []
    for dx in [80, 105, 130, 155, 180]:
        cd = Part.makeCylinder(5, altura, FreeCAD.Vector(dx, 50, 0), FreeCAD.Vector(0, 0, 1))
        cables_datos.append(cd)

    # 4. Bajante pluvial / sanitaria insonorizada (DN110 = Ø110 mm, espesor 4 mm)
    bajante = Part.makeCylinder(55, altura, FreeCAD.Vector(350, 50, 0), FreeCAD.Vector(0, 0, 1))

    # 5. Columna de fontanería PE-Xa 1" con coquilla aislante elastomérica (Ø60 mm exterior)
    tubo_agua = Part.makeCylinder(30, altura, FreeCAD.Vector(350, -60, 0), FreeCAD.Vector(0, 0, 1))

    # 6. Columna de gas en tubo de cobre rígido con vaina ventilada (Ø35 mm)
    tubo_gas = Part.makeCylinder(18, altura, FreeCAD.Vector(-400, -60, 0), FreeCAD.Vector(0, 0, 1))

    # 7. Forjados pasantes de hormigón superior e inferior con collarines intumescentes cortafuegos
    losa_inf = Part.makeBox(ancho + 200, profundidad + 200, 250)
    losa_inf.translate(FreeCAD.Vector(-ancho/2.0 - 100, -profundidad/2.0 - 100, -250))
    losa_inf = losa_inf.cut(Part.makeBox(ancho - 200, profundidad - 200, 300).translate(FreeCAD.Vector(-ancho/2.0 + 100, -profundidad/2.0 + 100, -280)))

    losa_sup = Part.makeBox(ancho + 200, profundidad + 200, 250)
    losa_sup.translate(FreeCAD.Vector(-ancho/2.0 - 100, -profundidad/2.0 - 100, altura))
    losa_sup = losa_sup.cut(Part.makeBox(ancho - 200, profundidad - 200, 300).translate(FreeCAD.Vector(-ancho/2.0 + 100, -profundidad/2.0 + 100, altura - 20)))

    elementos_internos = [bandeja_potencia, bandeja_datos, bajante, tubo_agua, tubo_gas, losa_inf, losa_sup] + cables_potencia + cables_datos
    solido_final = patinillo.fuse([puerta_registro] + elementos_internos)

    obj = doc.addObject("Part::Feature", "Patinillo_Instalaciones_Segregadas")
    obj.Shape = solido_final

    if hasattr(obj, "ViewObject") and obj.ViewObject:
        obj.ViewObject.ShapeColor = (0.75, 0.77, 0.8) # Chapa galvanizada / hormigón
        obj.ViewObject.Transparency = 10

    doc.recompute()

    output_dir = "/home/ral/Documents/GitHub/open-source-domotics/00_diseno_arquitectonico_y_estructural/06_canalizaciones_y_ductos_electricos_normativa/mecanico"
    os.makedirs(output_dir, exist_ok=True)

    fcstd_path = os.path.join(output_dir, "patinillo_instalaciones_conduits.FCStd")
    step_path = os.path.join(output_dir, "patinillo_instalaciones_conduits.step")

    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)

    print(f"Éxito: Modelo 3D guardado en {fcstd_path}")
    print(f"Éxito: Archivo STEP exportado en {step_path}")

if __name__ == "__main__":
    crear_patinillo_conduits_3d()

