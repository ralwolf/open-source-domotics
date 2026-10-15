#!/usr/bin/env python3
"""
Generador de Modelo 3D FreeCAD 1.1+
Proyecto: Satélite de Voz de Sobremesa 100% Local y Privado con ESP32-S3
Módulo: 05_confort_y_exteriores/06_asistente_voz_local_privado/mecanico
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

def generar_satelite_voz_3d(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    fcstd_path = os.path.join(output_dir, "satelite_voz_sobremesa.FCStd")
    step_path = os.path.join(output_dir, "satelite_voz_sobremesa.step")

    doc = FreeCAD.newDocument("SateliteVozSobremesa")

    # Dimensiones de la carcasa troncocónica con inclinación ergonómica
    # Diámetro base: 90 mm, Diámetro superior: 75 mm, Altura: 55 mm
    R_base = 45.0
    R_top = 37.5
    H = 55.0

    # 1. Cuerpo principal troncocónico exterior
    cuerpo_ext = Part.makeCone(R_base, R_top, H, Vector(0, 0, 0), Vector(0, 0, 1))

    # Cavidad interior hueca (espesor de pared 2.5 mm)
    cuerpo_int = Part.makeCone(R_base - 2.5, R_top - 2.5, H - 2.0, Vector(0, 0, 2.5), Vector(0, 0, 1))
    chasis = cuerpo_ext.cut(cuerpo_int)

    # 2. Rejilla acústica superior para altavoz de 40 mm (rejilla perforada circular)
    # Tapa superior
    tapa_sup = Part.makeCylinder(R_top, 3.0, Vector(0, 0, H), Vector(0, 0, 1))
    # Perforaciones acústicas concéntricas
    orificios = []
    # Centro
    orificios.append(Part.makeCylinder(1.5, 6.0, Vector(0, 0, H - 1.0), Vector(0, 0, 1)))
    # Anillo 1 (radio 8 mm, 6 orificios)
    for a in range(0, 360, 60):
        rad = math.radians(a)
        ox, oy = 8.0 * math.cos(rad), 8.0 * math.sin(rad)
        orificios.append(Part.makeCylinder(1.2, 6.0, Vector(ox, oy, H - 1.0), Vector(0, 0, 1)))
    # Anillo 2 (radio 16 mm, 12 orificios)
    for a in range(0, 360, 30):
        rad = math.radians(a)
        ox, oy = 16.0 * math.cos(rad), 16.0 * math.sin(rad)
        orificios.append(Part.makeCylinder(1.2, 6.0, Vector(ox, oy, H - 1.0), Vector(0, 0, 1)))
    # Anillo 3 (radio 24 mm, 18 orificios)
    for a in range(0, 360, 20):
        rad = math.radians(a)
        ox, oy = 24.0 * math.cos(rad), 24.0 * math.sin(rad)
        orificios.append(Part.makeCylinder(1.2, 6.0, Vector(ox, oy, H - 1.0), Vector(0, 0, 1)))

    orificios_comp = Part.makeCompound(orificios)
    tapa_rejilla = tapa_sup.cut(orificios_comp)

    # Botón táctil / Mute físico central superior (diámetro 12 mm en relieve)
    boton_mute = Part.makeCylinder(6.0, 2.0, Vector(0, 0, H + 2.5), Vector(0, 0, 1))

    # 3. Puertos acústicos frontales para micrófonos MEMS I2S duales (separación 45 mm)
    # Angulados a 15° hacia el frente
    mic_izq = Part.makeCylinder(1.5, 10.0, Vector(-22.5, -35.0, 25.0), Vector(0, 1, 0))
    mic_der = Part.makeCylinder(1.5, 10.0, Vector(22.5, -35.0, 25.0), Vector(0, 1, 0))
    chasis = chasis.cut(mic_izq).cut(mic_der)

    # 4. Difusor anular inferior para Anillo de 12 LEDs RGB WS2812B
    # Anillo de policarbonato translúcido (R_ext 46 mm, R_int 42 mm, H=4 mm)
    difusor_ext = Part.makeCylinder(R_base + 0.5, 4.0, Vector(0, 0, 1.0), Vector(0, 0, 1))
    difusor_int = Part.makeCylinder(R_base - 3.5, 4.0, Vector(0, 0, 1.0), Vector(0, 0, 1))
    anillo_difusor = difusor_ext.cut(difusor_int)

    # 5. Pasamuros posterior para conector USB-C (X=0, Y=R_base, Z=6 mm)
    ranura_usbc = Part.makeBox(10.0, 8.0, 4.0, Vector(-5.0, R_base - 5.0, 4.0))
    chasis = chasis.cut(ranura_usbc)

    # 6. Altavoz dinámico interior de 40 mm (3W, 4 Ohm)
    altavoz_cono = Part.makeCone(18.0, 5.0, 14.0, Vector(0, 0, H - 16.0), Vector(0, 0, 1))
    altavoz_iman = Part.makeCylinder(12.0, 8.0, Vector(0, 0, H - 24.0), Vector(0, 0, 1))
    altavoz = altavoz_cono.fuse(altavoz_iman)

    # 7. Placa PCB ESP32-S3 interior (60 x 50 mm a Z=15 mm)
    pcb_esp32 = Part.makeBox(60.0, 50.0, 1.6, Vector(-30.0, -25.0, 15.0))

    # Agregar objetos al documento FreeCAD
    obj_chasis = doc.addObject("Part::Feature", "Carcasa_Satelite_Sobremesa")
    obj_chasis.Shape = chasis
    if hasattr(obj_chasis, "ViewObject") and obj_chasis.ViewObject:
        obj_chasis.ViewObject.ShapeColor = (0.2, 0.22, 0.25)

    obj_tapa = doc.addObject("Part::Feature", "Rejilla_Acustica_Superior")
    obj_tapa.Shape = tapa_rejilla
    if hasattr(obj_tapa, "ViewObject") and obj_tapa.ViewObject:
        obj_tapa.ViewObject.ShapeColor = (0.3, 0.32, 0.35)

    obj_boton = doc.addObject("Part::Feature", "Boton_Mute_Privacidad")
    obj_boton.Shape = boton_mute
    if hasattr(obj_boton, "ViewObject") and obj_boton.ViewObject:
        obj_boton.ViewObject.ShapeColor = (0.85, 0.15, 0.15)

    obj_difusor = doc.addObject("Part::Feature", "Difusor_Anillo_LED_RGB")
    obj_difusor.Shape = anillo_difusor
    if hasattr(obj_difusor, "ViewObject") and obj_difusor.ViewObject:
        obj_difusor.ViewObject.ShapeColor = (0.9, 0.95, 1.0)
        obj_difusor.ViewObject.Transparency = 45

    obj_altavoz = doc.addObject("Part::Feature", "Altavoz_40mm_3W")
    obj_altavoz.Shape = altavoz
    if hasattr(obj_altavoz, "ViewObject") and obj_altavoz.ViewObject:
        obj_altavoz.ViewObject.ShapeColor = (0.1, 0.1, 0.1)

    obj_pcb = doc.addObject("Part::Feature", "PCB_ESP32S3_Audio")
    obj_pcb.Shape = pcb_esp32
    if hasattr(obj_pcb, "ViewObject") and obj_pcb.ViewObject:
        obj_pcb.ViewObject.ShapeColor = (0.1, 0.5, 0.2)

    doc.recompute()
    doc.saveAs(fcstd_path)

    # Exportar modelo de intercambio STEP del ensamble completo
    Part.export([obj_chasis, obj_tapa, obj_boton, obj_difusor, obj_altavoz, obj_pcb], step_path)

    print(f"Modelo FreeCAD guardado en: {fcstd_path}")
    print(f"Modelo STEP exportado en: {step_path}")

if __name__ == "__main__":
    out_dir = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/06_asistente_voz_local_privado/mecanico"
    generar_satelite_voz_3d(out_dir)
