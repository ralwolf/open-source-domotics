#!/usr/bin/env python3
"""
Generador de Modelo 3D FreeCAD 1.1+
Proyecto: Perfil de Aluminio Disipador Arquitectónico para Iluminación LED Circadiana
Módulo: 05_confort_y_exteriores/01_iluminacion_circadiana_y_exterior/mecanico
"""

import sys
import os

try:
    import FreeCAD
    import Part
    from FreeCAD import Base, Vector
except ImportError:
    print("Error: Este script debe ser ejecutado bajo el entorno FreeCAD (freecadcmd).")
    sys.exit(1)

def generar_perfil_led(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    fcstd_path = os.path.join(output_dir, "perfil_aluminio_disipador_led.FCStd")
    step_path = os.path.join(output_dir, "perfil_aluminio_disipador_led.step")

    doc = FreeCAD.newDocument("PerfilAluminioCircadiano")

    # Dimensiones del perfil (Longitud representativa de 300 mm para el ensamble BIM/CAD)
    # Sección exterior: 25 mm ancho x 15 mm alto x 300 mm largo
    L = 300.0
    W_ext = 25.0
    H_ext = 15.0
    T_wall = 1.5

    # 1. Cuerpo principal del perfil disipador de aluminio 6063-T5
    cuerpo_ext = Part.makeBox(W_ext, L, H_ext, Vector(-W_ext/2.0, 0, 0))
    # Cavidad interior para tiras LED CCT / RGBW (ancho interior 22 mm, profundidad 13.5 mm)
    cuerpo_int = Part.makeBox(W_ext - 2*T_wall, L, H_ext - T_wall, Vector(-(W_ext - 2*T_wall)/2.0, 0, T_wall))
    perfil_aluminio = cuerpo_ext.cut(cuerpo_int)

    # Aletas de disipación térmica laterales en el exterior
    for lado in [-1, 1]:
        aleta1 = Part.makeBox(1.2, L, 2.0, Vector(lado * (W_ext/2.0 - 0.6) if lado < 0 else W_ext/2.0 - 0.6, 0, 4.0))
        aleta2 = Part.makeBox(1.2, L, 2.0, Vector(lado * (W_ext/2.0 - 0.6) if lado < 0 else W_ext/2.0 - 0.6, 0, 8.0))
        # Pestaña para anclaje a clips
        ranura_clip = Part.makeBox(1.0, L, 1.5, Vector(-W_ext/2.0 if lado < 0 else W_ext/2.0 - 1.0, 0, 2.0))
        perfil_aluminio = perfil_aluminio.cut(ranura_clip)

    # 2. Difusor Opalino Curvo de Policarbonato (PC Bayer Makrolon con protección UV)
    # Encaja a presión en la parte superior del perfil
    W_dif = W_ext - 2*T_wall + 0.8
    H_dif = 4.0
    T_dif = 1.2
    difusor_ext = Part.makeBox(W_dif, L, H_dif, Vector(-W_dif/2.0, 0, H_ext - 1.0))
    difusor_int = Part.makeBox(W_dif - 2*T_dif, L, H_dif, Vector(-(W_dif - 2*T_dif)/2.0, 0, H_ext - 1.0 + T_dif))
    difusor_pc = difusor_ext.cut(difusor_int)

    # 3. Tira PCB LED CCT Dual (Warm White 2200K + Cold White 6500K) en el fondo
    W_pcb = 10.0
    T_pcb = 0.8
    tira_pcb = Part.makeBox(W_pcb, L, T_pcb, Vector(-W_pcb/2.0, 0, T_wall))

    # Módulos LED SMD 2835 representativos distribuidos cada 12.5 mm (80 LEDs en 300 mm)
    leds = []
    for i in range(0, int(L), 15):
        led_ww = Part.makeBox(2.8, 3.5, 0.7, Vector(-3.5, i + 3.0, T_wall + T_pcb))
        led_cw = Part.makeBox(2.8, 3.5, 0.7, Vector(0.7, i + 3.0, T_wall + T_pcb))
        leds.append(led_ww)
        leds.append(led_cw)

    leds_compound = Part.makeCompound(leds)

    # 4. Grapa / Clip de Fijación Oculta de Acero Inoxidable (2 unidades a L=50 mm y L=250 mm)
    clips = []
    for y_pos in [50.0, 250.0]:
        clip_base = Part.makeBox(W_ext + 2.5, 15.0, 1.2, Vector(-(W_ext + 2.5)/2.0, y_pos, -1.2))
        clip_ala_izq = Part.makeBox(1.2, 15.0, 6.0, Vector(-(W_ext + 2.5)/2.0, y_pos, 0))
        clip_ala_der = Part.makeBox(1.2, 15.0, 6.0, Vector((W_ext + 2.5)/2.0 - 1.2, y_pos, 0))
        clip_agujero = Part.makeCylinder(2.0, 4.0, Vector(0, y_pos + 7.5, -2.0), Vector(0, 0, 1))
        clip = clip_base.fuse([clip_ala_izq, clip_ala_der]).cut(clip_agujero)
        clips.append(clip)
    clips_compound = Part.makeCompound(clips)

    # 5. Agregar objetos al documento FreeCAD
    obj_perfil = doc.addObject("Part::Feature", "Perfil_Aluminio_Disipador")
    obj_perfil.Shape = perfil_aluminio
    if hasattr(obj_perfil, "ViewObject") and obj_perfil.ViewObject:
        obj_perfil.ViewObject.ShapeColor = (0.75, 0.75, 0.78)

    obj_difusor = doc.addObject("Part::Feature", "Difusor_Opalino_PC")
    obj_difusor.Shape = difusor_pc
    if hasattr(obj_difusor, "ViewObject") and obj_difusor.ViewObject:
        obj_difusor.ViewObject.ShapeColor = (0.95, 0.95, 0.98)
        obj_difusor.ViewObject.Transparency = 40

    obj_pcb = doc.addObject("Part::Feature", "Tira_PCB_LED_CCT")
    obj_pcb.Shape = tira_pcb
    if hasattr(obj_pcb, "ViewObject") and obj_pcb.ViewObject:
        obj_pcb.ViewObject.ShapeColor = (0.9, 0.9, 0.9)

    obj_leds = doc.addObject("Part::Feature", "LEDs_SMD2835_CCT")
    obj_leds.Shape = leds_compound
    if hasattr(obj_leds, "ViewObject") and obj_leds.ViewObject:
        obj_leds.ViewObject.ShapeColor = (1.0, 0.9, 0.3)

    obj_clips = doc.addObject("Part::Feature", "Clips_Montaje_Inox")
    obj_clips.Shape = clips_compound
    if hasattr(obj_clips, "ViewObject") and obj_clips.ViewObject:
        obj_clips.ViewObject.ShapeColor = (0.5, 0.5, 0.55)

    doc.recompute()
    doc.saveAs(fcstd_path)

    # Exportar modelo de intercambio STEP del ensamble completo
    ensamble_completo = Part.makeCompound([perfil_aluminio, difusor_pc, tira_pcb, leds_compound, clips_compound])
    Part.export([obj_perfil, obj_difusor, obj_pcb, obj_leds, obj_clips], step_path)

    print(f"Modelo FreeCAD guardado en: {fcstd_path}")
    print(f"Modelo STEP exportado en: {step_path}")

if __name__ == "__main__":
    out_dir = "/home/ral/Documents/GitHub/open-source-domotics/05_confort_y_exteriores/01_iluminacion_circadiana_y_exterior/mecanico"
    generar_perfil_led(out_dir)
