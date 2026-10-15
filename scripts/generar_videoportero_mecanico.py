#!/usr/bin/env python3
"""
Generador del Modelo 3D de la Carcasa Antivandálica para Videoportero Exterior
Herramienta FOSS: FreeCAD 1.1+ (ejecutado en modo headless con freecadcmd)
Formatos de salida: .FCStd (paramétrico nativo) y .step (interoperable universal)
Proyecto: open-source-domotics
"""

import os
import subprocess

FREECAD_SCRIPT = """
import FreeCAD as App
import Part
import os

doc = App.newDocument("Videoportero_Exterior_IP65")

# Dimensiones en mm (85 mm ancho x 175 mm alto x 36 mm profundidad)
ancho = 85.0
alto = 175.0
prof = 36.0
espesor = 3.5

# 1. Cuerpo principal de la carcasa (Box exterior)
cuerpo = Part.makeBox(ancho, alto, prof)

# Chaflán o fileteado de esquinas exteriores
cuerpo = cuerpo.makeChamfer(4.0, cuerpo.Edges)

# 2. Vaciado interior para alojamiento de PCB y altavoz
hueco = Part.makeBox(ancho - 2*espesor, alto - 2*espesor, prof - espesor)
hueco.translate(App.Vector(espesor, espesor, espesor))
carcasa = cuerpo.cut(hueco)

# 3. Visera superior inclinada antilluvia
visera = Part.makeBox(ancho + 6.0, 20.0, 8.0)
visera.translate(App.Vector(-3.0, alto - 15.0, prof - 2.0))
carcasa = carcasa.fuse(visera)

# 4. Mecanizado frontal: Hueco para Lente de Cámara Gran Angular (M12)
# Diámetro 22 mm en la zona superior (Y = 135 mm)
lente_cut = Part.makeCylinder(11.0, 20.0)
lente_cut.translate(App.Vector(ancho / 2.0, 135.0, prof - 10.0))
carcasa = carcasa.cut(lente_cut)

# Orificio para Sensor LDR y LED Infrarrojo nocturno
ir_cut = Part.makeCylinder(3.0, 20.0)
ir_cut.translate(App.Vector(ancho / 2.0 + 20.0, 135.0, prof - 10.0))
carcasa = carcasa.cut(ir_cut)

# 5. Mecanizado frontal: Hueco para Botón Piezoeléctrico Antivandálico (19 mm)
# Situado en Y = 45 mm
boton_cut = Part.makeCylinder(9.5, 20.0)
boton_cut.translate(App.Vector(ancho / 2.0, 45.0, prof - 10.0))
carcasa = carcasa.cut(boton_cut)

# 6. Rejilla acústica de Altavoz (Microperforaciones para salida de audio)
# Situada en Y = 85 mm
for i in range(-2, 3):
    for j in range(-2, 3):
        slot = Part.makeCylinder(1.2, 20.0)
        slot.translate(App.Vector(ancho / 2.0 + i * 5.0, 85.0 + j * 5.0, prof - 10.0))
        carcasa = carcasa.cut(slot)

# 7. Orificio para Micrófono MEMS I2S (2 mm con guía cónica)
mic_cut = Part.makeCylinder(1.0, 20.0)
mic_cut.translate(App.Vector(ancho / 2.0 - 22.0, 45.0, prof - 10.0))
carcasa = carcasa.cut(mic_cut)

# 8. Pasacables estanco posterior RJ45 / PoE
cable_cut = Part.makeCylinder(10.0, 20.0)
cable_cut.translate(App.Vector(ancho / 2.0, alto / 2.0, -5.0))
carcasa = carcasa.cut(cable_cut)

# Guardar en Documento
obj = doc.addObject("Part::Feature", "Carcasa_Videoportero")
obj.Shape = carcasa
doc.recompute()

out_fcstd = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/06_intercomunicacion_videoportero_y_multizona/mecanico/videoportero_carcasa.FCStd"
out_step = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/06_intercomunicacion_videoportero_y_multizona/mecanico/videoportero_carcasa.step"

doc.saveAs(out_fcstd)
Part.export([obj], out_step)
print("Modelo 3D de Videoportero generado con éxito:")
print(" - FCStd:", out_fcstd)
print(" - STEP:", out_step)
"""

def main():
    script_tmp = "/home/ral/Documents/GitHub/open-source-domotics/scripts/temp_freecad_doorbell.py"
    with open(script_tmp, "w", encoding="utf-8") as f:
        f.write(FREECAD_SCRIPT)

    cmd = [
        "flatpak-spawn", "--host", "flatpak", "run", "--command=freecadcmd",
        "org.freecad.FreeCAD", script_tmp
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(res.stdout)
    finally:
        if os.path.exists(script_tmp):
            os.remove(script_tmp)

if __name__ == "__main__":
    main()
