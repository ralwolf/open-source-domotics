#!/usr/bin/env python3
"""
generar_rack_19u_3d.py
Genera el modelo paramétrico 3D del armario Rack 19" 15U de Telecomunicaciones y Servidores
conforme a estándar EIA-310-D / IEC 60297 en FreeCAD 1.1+ y exporta a STEP AP214.
Dimensiones exteriores: 600 x 600 x 770 mm, con bastidores de 19 pulgadas,
puerta acristalada, extractores superiores termorregulados, PDU, Patch Panel,
switch PoE+, servidores 1U y unidad SAI/UPS 2U.
"""

import sys
import os

try:
    import FreeCAD
    import Part
except ImportError:
    print("Error: FreeCAD no está en el path de Python.")
    sys.exit(1)

def crear_rack_19u_3d():
    doc = FreeCAD.newDocument("Rack_19U_Servidores_UPS")

    # 1. Estructura envolvente del rack (600 x 600 x 770 mm)
    ancho = 600.0
    profundidad = 600.0
    altura = 770.0
    espesor_chapa = 2.0

    caja_ext = Part.makeBox(ancho, profundidad, altura)
    caja_ext.translate(FreeCAD.Vector(-ancho/2.0, -profundidad/2.0, 0))

    cavidad_int = Part.makeBox(ancho - 2*espesor_chapa, profundidad - 2*espesor_chapa, altura - 2*espesor_chapa)
    cavidad_int.translate(FreeCAD.Vector(-ancho/2.0 + espesor_chapa, -profundidad/2.0 + espesor_chapa, espesor_chapa))

    envolvente = caja_ext.cut(cavidad_int)

    # 2. Apertura frontal para puerta acristalada
    hueco_puerta = Part.makeBox(520, 10, 710)
    hueco_puerta.translate(FreeCAD.Vector(-260, -profundidad/2.0 - 5, 30))
    envolvente = envolvente.cut(hueco_puerta)

    # Marco y cristal de puerta frontal
    marco_puerta = Part.makeBox(516, 8, 706)
    marco_puerta.translate(FreeCAD.Vector(-258, -profundidad/2.0 - 2, 32))
    hueco_cristal = Part.makeBox(450, 12, 640)
    hueco_cristal.translate(FreeCAD.Vector(-225, -profundidad/2.0 - 4, 65))
    puerta = marco_puerta.cut(hueco_cristal)

    cristal = Part.makeBox(448, 4, 638)
    cristal.translate(FreeCAD.Vector(-224, -profundidad/2.0, 66))

    # Maneta con cerradura
    maneta = Part.makeCylinder(10, 18, FreeCAD.Vector(230, -profundidad/2.0 - 15, 385), FreeCAD.Vector(0, 1, 0))

    # 3. Cuatro perfiles angulares verticales de montaje 19" (EIA-310)
    perfiles = []
    # Distancia entre centros de perfiles 19": 465 mm
    dist_x = 465.0 / 2.0
    # Profundidad de montaje entre perfiles frontales y traseros: 450 mm
    dist_y = 450.0 / 2.0

    for px in [-dist_x, dist_x]:
        for py in [-dist_y, dist_y]:
            perfil = Part.makeBox(25, 25, 700)
            if px < 0 and py < 0:
                perfil.translate(FreeCAD.Vector(px, py, 35))
            elif px > 0 and py < 0:
                perfil.translate(FreeCAD.Vector(px - 25, py, 35))
            elif px < 0 and py > 0:
                perfil.translate(FreeCAD.Vector(px, py - 25, 35))
            else:
                perfil.translate(FreeCAD.Vector(px - 25, py - 25, 35))
            perfiles.append(perfil)

    # 4. Equipamiento interno 19"
    # Unidad 1-2 (Fondo inferior): UPS Online 2U (ancho 482.6, alto 88, prof 480)
    ups_2u = Part.makeBox(482, 480, 85)
    ups_2u.translate(FreeCAD.Vector(-241, -240, 50))

    # Unidad 4: PDU Horizontal 1U (ancho 482.6, alto 44, prof 60)
    pdu_1u = Part.makeBox(482, 70, 42)
    pdu_1u.translate(FreeCAD.Vector(-241, -240, 180))

    # Unidad 6: Servidor TrueNAS ZFS Storage 2U (ancho 482, alto 85, prof 450)
    nas_2u = Part.makeBox(482, 450, 85)
    nas_2u.translate(FreeCAD.Vector(-241, -240, 270))

    # Unidad 9: Servidor Proxmox VE 1U (ancho 482, alto 42, prof 420)
    proxmox_1u = Part.makeBox(482, 420, 42)
    proxmox_1u.translate(FreeCAD.Vector(-241, -240, 400))

    # Unidad 11: Switch Managed 24P PoE+ 1U (ancho 482, alto 42, prof 280)
    switch_1u = Part.makeBox(482, 280, 42)
    switch_1u.translate(FreeCAD.Vector(-241, -240, 490))

    # Unidad 12: Patch Panel 24P Cat6A 1U (ancho 482, alto 42, prof 100)
    patch_1u = Part.makeBox(482, 100, 42)
    patch_1u.translate(FreeCAD.Vector(-241, -240, 540))

    # Unidad 14: Firewall Appliance OPNsense 1U (ancho 482, alto 42, prof 250)
    fw_1u = Part.makeBox(482, 250, 42)
    fw_1u.translate(FreeCAD.Vector(-241, -240, 630))

    # 5. Extractores de techo dobles (120 mm)
    fan1 = Part.makeCylinder(58, 10, FreeCAD.Vector(-80, 0, 765), FreeCAD.Vector(0, 0, 1))
    fan2 = Part.makeCylinder(58, 10, FreeCAD.Vector(80, 0, 765), FreeCAD.Vector(0, 0, 1))
    techo_fans = Part.makeBox(280, 160, 8)
    techo_fans.translate(FreeCAD.Vector(-140, -80, 762))

    # Fusión y cortes
    solido_chasis = envolvente.fuse([puerta, maneta, techo_fans] + perfiles + [ups_2u, pdu_1u, nas_2u, proxmox_1u, switch_1u, patch_1u, fw_1u])
    solido_chasis = solido_chasis.cut(fan1)
    solido_chasis = solido_chasis.cut(fan2)

    solido_final = solido_chasis.fuse(cristal)

    obj = doc.addObject("Part::Feature", "Rack_19U_Datacenter")
    obj.Shape = solido_final

    if hasattr(obj, "ViewObject") and obj.ViewObject:
        obj.ViewObject.ShapeColor = (0.15, 0.15, 0.16) # RAL 9005 Jet Black
        obj.ViewObject.Transparency = 10

    doc.recompute()

    output_dir = "/home/ral/Documents/GitHub/open-source-domotics/02_infraestructura_it_y_red/01_rack_servidores_y_ups/mecanico"
    os.makedirs(output_dir, exist_ok=True)

    fcstd_path = os.path.join(output_dir, "gabinete_rack_19u_datacenter.FCStd")
    step_path = os.path.join(output_dir, "gabinete_rack_19u_datacenter.step")

    doc.saveAs(fcstd_path)
    Part.export([obj], step_path)

    print(f"Éxito: Modelo 3D guardado en {fcstd_path}")
    print(f"Éxito: Archivo STEP exportado en {step_path}")

if __name__ == "__main__":
    crear_rack_19u_3d()
