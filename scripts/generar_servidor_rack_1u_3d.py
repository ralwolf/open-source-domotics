#!/usr/bin/env python3
"""
generar_servidor_rack_1u_3d.py
Genera el modelo paramétrico 3D del chasis de servidor 19" 1U para virtualización Proxmox VE
con aceleración Coral TPU y almacenamiento TrueNAS en FreeCAD 1.1+ y exporta a STEP AP214.
Dimensiones: Ancho estándar 482.6 mm (frontal con orejetas), Chasis 437 x 450 x 43.6 mm (1U),
4 bahías hot-swap SAS/SATA para discos SSD de 2.5", fuentes redundantes y disipadores pasivos.
"""

import sys
import os

try:
    import FreeCAD
    import Part
except ImportError:
    print("Error: FreeCAD no está en el path de Python.")
    sys.exit(1)

def crear_servidor_1u_3d():
    doc = FreeCAD.newDocument("Servidor_Rack_1U_Computo")

    # 1. Chasis principal de chapa metálica SPCC 1.2 mm (437 x 450 x 43.6 mm)
    chasis_box = Part.makeBox(437, 450, 43.6)
    chasis_box.translate(FreeCAD.Vector(-218.5, -225, 0))

    cavidad = Part.makeBox(434.6, 447.6, 41.2)
    cavidad.translate(FreeCAD.Vector(-217.3, -223.8, 1.2))
    carcasa = chasis_box.cut(cavidad)

    # 2. Frontal de 19 pulgadas con orejetas de fijación para tuercas enjauladas (482.6 x 15 x 43.6 mm)
    frontal = Part.makeBox(482.6, 8, 43.6)
    frontal.translate(FreeCAD.Vector(-241.3, -233, 0))

    # Taladros ovalados en las orejetas de montaje EIA-310 (2 a cada lado)
    taladros = []
    for x_orejeta in [-233, 233]:
        for z_h in [10, 33.6]:
            t = Part.makeCylinder(4, 12, FreeCAD.Vector(x_orejeta, -235, z_h), FreeCAD.Vector(0, 1, 0))
            taladros.append(t)

    for t in taladros:
        frontal = frontal.cut(t)

    # 3. 4 Bahías Hot-Swap para discos SSD/NVMe de 2.5 pulgadas en el frontal izquierdo
    bahias = []
    for i in range(4):
        bx = -190 + i * 40
        bahia = Part.makeBox(32, 100, 15)
        bahia.translate(FreeCAD.Vector(bx, -230, 14))
        tirador = Part.makeCylinder(3, 8, FreeCAD.Vector(bx + 16, -234, 21.5), FreeCAD.Vector(0, 1, 0))
        bahias.extend([bahia, tirador])

    # 4. Rejilla de ventilación frontal para ventiladores de 40x40 mm (lado derecho)
    rejilla = Part.makeBox(120, 10, 30)
    rejilla.translate(FreeCAD.Vector(40, -230, 7))

    # 5. Módulo posterior de fuentes redundantes (Dual 1U Flex-ATX 80+ Platinum)
    psu1 = Part.makeBox(80, 150, 40)
    psu1.translate(FreeCAD.Vector(130, 70, 2))
    psu2 = Part.makeBox(80, 150, 40)
    psu2.translate(FreeCAD.Vector(40, 70, 2))

    # 6. Tarjeta PCIe / Módulo acelerador Coral Edge TPU y disipadores de CPU
    heatsink1 = Part.makeBox(80, 80, 28)
    heatsink1.translate(FreeCAD.Vector(-100, -50, 5))

    solido_final = carcasa.fuse([frontal, rejilla, psu1, psu2, heatsink1] + bahias)

    obj = doc.addObject("Part::Feature", "Servidor_Rack_1U_Computo")
    obj.Shape = solido_final

    if hasattr(obj, "ViewObject") and obj.ViewObject:
        obj.ViewObject.ShapeColor = (0.2, 0.22, 0.25) # Metal cepillado / negro anodizado
        obj.ViewObject.Transparency = 5

    doc.recompute()

    output_dir = "/home/ral/Documents/GitHub/open-source-domotics/02_infraestructura_it_y_red/03_servidores_proxmox_ha_frigate_truenas/mecanico"
    os.makedirs(output_dir, exist_ok=True)

    fcstd_path = os.path.join(output_dir, "servidor_rack_1u_computo.FCStd")
    step_path = os.path.join(output_dir, "servidor_rack_1u_computo.step")

    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)

    print(f"Éxito: Modelo 3D guardado en {fcstd_path}")
    print(f"Éxito: Archivo STEP exportado en {step_path}")

if __name__ == "__main__":
    crear_servidor_1u_3d()
