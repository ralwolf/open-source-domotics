#!/usr/bin/env python3
"""
generar_arquitectura_vivienda_3d.py
Genera el modelo paramétrico 3D arquitectónico de la vivienda bioclimática completa (10.0 x 10.0 m)
con patio central interior (3.0 x 2.0 m), muros de cerramiento con aislamiento,
particiones interiores (Dormitorio Principal, Dormitorio Infantil, Sala/Comedor, Cocina, Cuarto Técnico IT)
y huecos de ventanas/puertas en FreeCAD 1.1+ y exporta a STEP AP214.
"""

import sys
import os

try:
    import FreeCAD
    import Part
except ImportError:
    print("Error: FreeCAD no está en el path de Python.")
    sys.exit(1)

def crear_arquitectura_vivienda_3d():
    doc = FreeCAD.newDocument("Arquitectura_Vivienda_Bioclimatica_10x10")

    ancho = 10000.0
    largo = 10000.0
    altura_muro = 3000.0
    espesor_ext = 300.0
    espesor_int = 150.0

    # 1. Losa de cimentación / solera base (10.2 x 10.2 m x 0.2 m)
    solera = Part.makeBox(ancho + 200, largo + 200, 200)
    solera.translate(FreeCAD.Vector(-100, -100, 0))

    # 2. Muros exteriores perimetrales
    caja_ext = Part.makeBox(ancho, largo, altura_muro)
    caja_ext.translate(FreeCAD.Vector(0, 0, 200))

    cavidad_ext = Part.makeBox(ancho - 2*espesor_ext, largo - 2*espesor_ext, altura_muro + 10)
    cavidad_ext.translate(FreeCAD.Vector(espesor_ext, espesor_ext, 195))

    envolvente = caja_ext.cut(cavidad_ext)

    # 3. Patio interior central (3.0 x 2.0 m en coordenadas X: 3500..6500, Y: 4000..6000)
    muro_patio_ext = Part.makeBox(3000 + 2*espesor_int, 2000 + 2*espesor_int, altura_muro)
    muro_patio_ext.translate(FreeCAD.Vector(3500 - espesor_int, 4000 - espesor_int, 200))

    hueco_patio = Part.makeBox(3000, 2000, altura_muro + 20)
    hueco_patio.translate(FreeCAD.Vector(3500, 4000, 190))
    patio_muros = muro_patio_ext.cut(hueco_patio)

    # 4. Tabiques divisorios interiores
    # Pared dormitorio principal (Y = 6000, X de 300 a 3500)
    muro_dorm1 = Part.makeBox(3200, espesor_int, altura_muro)
    muro_dorm1.translate(FreeCAD.Vector(espesor_ext, 6000, 200))

    # Pared dormitorio infantil (Y = 6000, X de 6500 a 9700)
    muro_dorm2 = Part.makeBox(3200, espesor_int, altura_muro)
    muro_dorm2.translate(FreeCAD.Vector(6500, 6000, 200))

    # Pared Cuarto Técnico IT central (X = 6500, Y de 1500 a 4000)
    muro_it = Part.makeBox(espesor_int, 2500, altura_muro)
    muro_it.translate(FreeCAD.Vector(6500, 1500, 200))

    # Pared divisoria Cocina / Entrada (X = 3500, Y de 300 a 4000)
    muro_cocina = Part.makeBox(espesor_int, 3700, altura_muro)
    muro_cocina.translate(FreeCAD.Vector(3500, espesor_ext, 200))

    # 5. Huecos de puertas y ventanas
    # Puerta principal de acceso (ancho 1000, alto 2200 en X=5000, Y=0)
    p_principal = Part.makeBox(1000, espesor_ext + 20, 2200)
    p_principal.translate(FreeCAD.Vector(4500, -10, 200))

    # Ventanal salón sur (ancho 2500, alto 2200 en X=7000, Y=0)
    v_salon = Part.makeBox(2500, espesor_ext + 20, 2200)
    v_salon.translate(FreeCAD.Vector(7000, -10, 200))

    # Ventana cocina este (ancho 1500, alto 1200 en X=0, Y=2000, antepecho 1000)
    v_cocina = Part.makeBox(espesor_ext + 20, 1500, 1200)
    v_cocina.translate(FreeCAD.Vector(-10, 2000, 1200))

    # Ventanas dormitorios norte (ancho 1400, alto 1400 en Y=10000)
    v_dorm1 = Part.makeBox(1400, espesor_ext + 20, 1400)
    v_dorm1.translate(FreeCAD.Vector(1500, largo - espesor_ext - 10, 1000))

    v_dorm2 = Part.makeBox(1400, espesor_ext + 20, 1400)
    v_dorm2.translate(FreeCAD.Vector(7500, largo - espesor_ext - 10, 1000))

    # Losa de cubierta plana transitable con hueco cenital para el lucernario
    losa_techo = Part.makeBox(ancho, largo, 200)
    losa_techo.translate(FreeCAD.Vector(0, 0, altura_muro + 200))
    hueco_lucernario = Part.makeBox(3000, 2000, 250)
    hueco_lucernario.translate(FreeCAD.Vector(3500, 4000, altura_muro + 180))
    cubierta = losa_techo.cut(hueco_lucernario)

    # Fusión y cortes
    muros = envolvente.fuse([patio_muros, muro_dorm1, muro_dorm2, muro_it, muro_cocina])
    muros = muros.cut(p_principal)
    muros = muros.cut(v_salon)
    muros = muros.cut(v_cocina)
    muros = muros.cut(v_dorm1)
    muros = muros.cut(v_dorm2)

    solido_vivienda = solera.fuse([muros, cubierta])

    obj = doc.addObject("Part::Feature", "Arquitectura_Vivienda_Bioclimatica")
    obj.Shape = solido_vivienda

    if hasattr(obj, "ViewObject") and obj.ViewObject:
        obj.ViewObject.ShapeColor = (0.9, 0.88, 0.85) # Blanco piedra / mortero de cal
        obj.ViewObject.Transparency = 15

    doc.recompute()

    output_dir = "/home/ral/Documents/GitHub/open-source-domotics/00_diseno_arquitectonico_y_estructural/03_arquitectura_habitaciones_patios_terrazas/mecanico"
    os.makedirs(output_dir, exist_ok=True)

    fcstd_path = os.path.join(output_dir, "modelo_arquitectonico_vivienda_3d.FCStd")
    step_path = os.path.join(output_dir, "modelo_arquitectonico_vivienda_3d.step")

    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)

    print(f"Éxito: Modelo 3D guardado en {fcstd_path}")
    print(f"Éxito: Archivo STEP exportado en {step_path}")

if __name__ == "__main__":
    crear_arquitectura_vivienda_3d()
