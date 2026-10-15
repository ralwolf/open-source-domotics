#!/usr/bin/env python3
"""
generar_tablero_cgmp_3d.py
Genera el modelo paramétrico 3D del Cuadro General de Mando y Protección (CGMP)
de 72 módulos DIN (4 filas x 18 módulos) conforme a norma UNE-EN 61439 en FreeCAD 1.1+ y exporta a STEP AP214.
Dimensiones exteriores: 450 x 750 x 160 mm, con puerta transparente abatible,
4 carriles DIN 35x7.5 mm, embarrados de neutro y tierra, y aparamenta modular.
"""

import sys
import os

try:
    import FreeCAD
    import Part
except ImportError:
    print("Error: FreeCAD no está en el path de Python.")
    sys.exit(1)

def crear_tablero_cgmp_3d():
    doc = FreeCAD.newDocument("Cuadro_General_Mando_Proteccion_72M")

    ancho = 450.0
    altura = 750.0
    profundidad = 160.0
    espesor = 3.0

    # 1. Caja envolvente IP65 / IK08 en policarbonato autoextinguible
    caja_ext = Part.makeBox(ancho, profundidad, altura)
    caja_ext.translate(FreeCAD.Vector(-ancho/2.0, -profundidad/2.0, 0))

    cavidad_int = Part.makeBox(ancho - 2*espesor, profundidad - 2*espesor, altura - 2*espesor)
    cavidad_int.translate(FreeCAD.Vector(-ancho/2.0 + espesor, -profundidad/2.0 + espesor, espesor))

    envolvente = caja_ext.cut(cavidad_int)

    # 2. Marco frontal y puerta transparente ahumada
    marco_frontal = Part.makeBox(ancho + 4, 15, altura + 4)
    marco_frontal.translate(FreeCAD.Vector(-ancho/2.0 - 2, profundidad/2.0 - 5, -2))
    hueco_puerta = Part.makeBox(ancho - 50, 20, altura - 50)
    hueco_puerta.translate(FreeCAD.Vector(-ancho/2.0 + 25, profundidad/2.0 - 8, 25))
    marco = marco_frontal.cut(hueco_puerta)

    puerta = Part.makeBox(ancho - 46, 6, altura - 46)
    puerta.translate(FreeCAD.Vector(-ancho/2.0 + 23, profundidad/2.0 + 2, 23))

    # Cierre de leva / maneta
    cerradura = Part.makeCylinder(14, 12, FreeCAD.Vector(ancho/2.0 - 45, profundidad/2.0 + 4, altura/2.0), FreeCAD.Vector(0, 1, 0))

    # 3. 4 Carriles DIN 35x7.5 mm (longitud 380 mm)
    carriles = []
    modulos_din = []
    separacion_filas = 140.0
    y_carril = -profundidad/2.0 + 45.0

    for i in range(4):
        z_pos = 120.0 + i * separacion_filas
        # Carril DIN metálico
        carril = Part.makeBox(380, 7.5, 35)
        carril.translate(FreeCAD.Vector(-190, y_carril, z_pos))
        carriles.append(carril)

        # Bloques de interruptores automáticos magnetotérmicos y diferenciales (18 módulos de 18 mm = 324 mm)
        bloque_aparamenta = Part.makeBox(324, 60, 85)
        bloque_aparamenta.translate(FreeCAD.Vector(-162, y_carril + 5, z_pos - 25))
        modulos_din.append(bloque_aparamenta)

    # 4. Embarrados de latón para Neutro (N) y Protección de Tierra (PE)
    embarrado_pe = Part.makeBox(360, 15, 12)
    embarrado_pe.translate(FreeCAD.Vector(-180, -profundidad/2.0 + 20, 30))

    embarrado_n = Part.makeBox(360, 15, 12)
    embarrado_n.translate(FreeCAD.Vector(-180, -profundidad/2.0 + 20, altura - 42))

    # 5. Pasamuros cónicos para entrada de acometidas (M40 / M32 / M25)
    conduits = []
    for cx in [-120, -40, 40, 120]:
        c_sup = Part.makeCylinder(18, 20, FreeCAD.Vector(cx, 0, altura - 5), FreeCAD.Vector(0, 0, 1))
        c_inf = Part.makeCylinder(18, 20, FreeCAD.Vector(cx, 0, -15), FreeCAD.Vector(0, 0, 1))
        conduits.extend([c_sup, c_inf])

    chasis = envolvente.fuse([marco, cerradura, embarrado_pe, embarrado_n] + carriles + modulos_din)
    for c in conduits:
        chasis = chasis.fuse(c)

    solido_final = chasis.fuse(puerta)

    obj = doc.addObject("Part::Feature", "Tablero_CGMP_72M")
    obj.Shape = solido_final

    if hasattr(obj, "ViewObject") and obj.ViewObject:
        obj.ViewObject.ShapeColor = (0.85, 0.86, 0.88) # RAL 7035 Gris Claro
        obj.ViewObject.Transparency = 5

    doc.recompute()

    output_dir = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/07_tableros_distribucion_y_protecciones/mecanico"
    os.makedirs(output_dir, exist_ok=True)

    fcstd_path = os.path.join(output_dir, "gabinete_cuadro_general_mando_proteccion.FCStd")
    step_path = os.path.join(output_dir, "gabinete_cuadro_general_mando_proteccion.step")

    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)

    print(f"Éxito: Modelo 3D guardado en {fcstd_path}")
    print(f"Éxito: Archivo STEP exportado en {step_path}")

if __name__ == "__main__":
    crear_tablero_cgmp_3d()
