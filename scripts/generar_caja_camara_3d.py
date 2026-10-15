#!/usr/bin/env python3
"""
Generador del Modelo 3D Paramétrico de la Caja de Montaje Estanca para Cámara PoE IP
Herramienta: FreeCAD 1.1+ (headless con freecadcmd)
Formatos de salida: .FCStd y .step
Proyecto: open-source-domotics
"""

import os
import subprocess

FREECAD_SCRIPT = """
import FreeCAD as App
import Part

doc = App.newDocument("Caja_Montaje_Camara_PoE")

# Dimensiones en mm (Caja cilíndrica IP67 para cámara torreta / domo)
r_ext = 65.0      # Radio exterior 65mm -> Diámetro 130mm
h_total = 55.0    # Altura total 55mm
espesor = 3.5

# 1. Cuerpo exterior cilíndrico
cuerpo_ext = Part.makeCylinder(r_ext, h_total)

# 2. Vaciado interior para alojamiento de conector RJ45 hembra estanco
cuerpo_int = Part.makeCylinder(r_ext - espesor, h_total - espesor)
cuerpo_int.translate(App.Vector(0, 0, espesor))
caja = cuerpo_ext.cut(cuerpo_int)

# 3. Brida de fijación mural con 4 orejetas
for ang_deg in [45, 135, 225, 315]:
    import math
    rad = math.radians(ang_deg)
    ox = (r_ext + 10.0) * math.cos(rad)
    oy = (r_ext + 10.0) * math.sin(rad)
    orejeta = Part.makeCylinder(12.0, 8.0)
    orejeta.translate(App.Vector(ox, oy, 0))
    taladro = Part.makeCylinder(3.5, 10.0)
    taladro.translate(App.Vector(ox, oy, -1.0))
    orejeta = orejeta.cut(taladro)
    caja = caja.fuse(orejeta)

# 4. Entrada lateral para tubo conduit roscado M20 (Prensacables IP68)
entrada_m20 = Part.makeCylinder(16.0, 25.0)
entrada_m20.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
entrada_m20.translate(App.Vector(r_ext - 5.0, 0, h_total / 2.0))
caja = caja.fuse(entrada_m20)

orificio_m20 = Part.makeCylinder(10.5, 30.0)
orificio_m20.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
orificio_m20.translate(App.Vector(r_ext - 10.0, 0, h_total / 2.0))
caja = caja.cut(orificio_m20)

# 5. Tapa superior con patrón universal de anclaje de cámara (Domo/Torreta)
tapa = Part.makeCylinder(r_ext + 2.0, 6.0)
tapa.translate(App.Vector(0, 0, h_total))

# Hueco central para paso de cable de la cámara
paso_cable = Part.makeCylinder(15.0, 10.0)
paso_cable.translate(App.Vector(0, 0, h_total - 2.0))
tapa = tapa.cut(paso_cable)

# 4 taladros roscados M4 para fijación de la cámara (Radio 45mm)
for ang_deg in [0, 90, 180, 270]:
    import math
    rad = math.radians(ang_deg)
    tx = 45.0 * math.cos(rad)
    ty = 45.0 * math.sin(rad)
    m4_hole = Part.makeCylinder(2.0, 10.0)
    m4_hole.translate(App.Vector(tx, ty, h_total - 2.0))
    tapa = tapa.cut(m4_hole)

caja = caja.fuse(tapa)

obj = doc.addObject("Part::Feature", "Caja_Montaje_Estanca_Camara_PoE")
obj.Shape = caja

doc.recompute()

out_dir = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/01_videovigilancia_poe_frigate/mecanico"
os.makedirs(out_dir, exist_ok=True)
fcstd_path = os.path.join(out_dir, "caja_montaje_camara_poe.FCStd")
step_path = os.path.join(out_dir, "caja_montaje_camara_poe.step")

doc.saveAs(fcstd_path)
Part.export([obj], step_path)
print(f"Éxito: Archivos guardados:\\n  {fcstd_path}\\n  {step_path}")
"""

def main():
    script_tmp = "/home/ral/Documents/GitHub/open-source-domotics/scripts/_temp_freecad_caja_camara.py"
    with open(script_tmp, "w", encoding="utf-8") as f:
        f.write(FREECAD_SCRIPT)
    
    cmd = [
        "flatpak-spawn", "--host", "flatpak", "run",
        "--command=freecadcmd", "org.freecad.FreeCAD",
        script_tmp
    ]
    print("Ejecutando FreeCAD headless para caja de cámara PoE...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Salida:", res.stdout)
    if res.stderr:
        print("Avisos:", res.stderr)
        
    if os.path.exists(script_tmp):
        os.remove(script_tmp)
        
    if res.returncode != 0:
        raise RuntimeError(f"Error generando caja cámara FreeCAD (código {res.returncode})")

if __name__ == "__main__":
    main()

