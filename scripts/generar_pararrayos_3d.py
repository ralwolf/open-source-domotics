#!/usr/bin/env python3
"""
Generador del Modelo 3D Paramétrico del Sistema de Pararrayos PDC y Mástil
Herramienta: FreeCAD 1.1+ (headless con freecadcmd)
Formatos de salida: .FCStd y .step
Proyecto: open-source-domotics
"""

import os
import subprocess

FREECAD_SCRIPT = """
import FreeCAD as App
import Part

doc = App.newDocument("Pararrayos_PDC_Proteccion_Descargas")

# 1. Cabezal de Pararrayos con Dispositivo de Cebado (PDC / ESE)
# Punta central captadora (Cobre cromado / Acero Inox AISI 316)
punta = Part.makeCone(6.0, 1.0, 180.0)
punta.translate(App.Vector(0, 0, 300.0))

# Cuerpo ionizador / Generador de impulsos de alta tensión (Campana PDC)
cuerpo_pdc = Part.makeCylinder(45.0, 160.0)
cuerpo_pdc.translate(App.Vector(0, 0, 140.0))

# Aro equipotencial deflector de descargas
aro_deflector = Part.makeTorus(65.0, 10.0)
aro_deflector.translate(App.Vector(0, 0, 200.0))

cabezal = punta.fuse(cuerpo_pdc).fuse(aro_deflector)

# Base cónica adaptadora hacia el mástil
base_cabezal = Part.makeCone(30.0, 45.0, 140.0)
cabezal = cabezal.fuse(base_cabezal)

# 2. Mástil Soporte de Acero Galvanizado (Tubo 2" exterior, longitud 3000 mm)
mastil = Part.makeCylinder(30.0, 3000.0)
mastil.translate(App.Vector(0, 0, -3000.0))
pararrayos = cabezal.fuse(mastil)

# Abrazaderas de sujeción mural o anclaje a torre
abrazadera_1 = Part.makeBox(120.0, 30.0, 50.0)
abrazadera_1.translate(App.Vector(-60.0, -15.0, -1000.0))
abrazadera_2 = Part.makeBox(120.0, 30.0, 50.0)
abrazadera_2.translate(App.Vector(-60.0, -15.0, -2500.0))
pararrayos = pararrayos.fuse(abrazadera_1).fuse(abrazadera_2)

# 3. Conductor de Bajada Exterior (Cable 50 mm² Cu fijado con aisladores)
conductor_bajada = Part.makeCylinder(5.0, 3200.0)
conductor_bajada.translate(App.Vector(45.0, 0, -3000.0))
pararrayos = pararrayos.fuse(conductor_bajada)

# 4. Arqueta de Registro y Junta de Control de Puesta a Tierra (Nivel de Suelo)
arqueta = Part.makeBox(250.0, 250.0, 200.0)
arqueta.translate(App.Vector(-125.0, -125.0, -3200.0))
tapa_arqueta = Part.makeBox(270.0, 270.0, 25.0)
tapa_arqueta.translate(App.Vector(-135.0, -135.0, -3025.0))
pararrayos = pararrayos.fuse(arqueta).fuse(tapa_arqueta)

# Pica de tierra de cobre vertical en el fondo de arqueta
pica_tierra = Part.makeCylinder(8.0, 800.0)
pica_tierra.translate(App.Vector(0, 0, -4000.0))
pararrayos = pararrayos.fuse(pica_tierra)

obj = doc.addObject("Part::Feature", "Sistema_Pararrayos_PDC_Mastil")
obj.Shape = pararrayos

doc.recompute()

out_dir = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/08_pararrayos_y_proteccion_descargas/mecanico"
os.makedirs(out_dir, exist_ok=True)
fcstd_path = os.path.join(out_dir, "pararrayos_pdc_mastil.FCStd")
step_path = os.path.join(out_dir, "pararrayos_pdc_mastil.step")

doc.saveAs(fcstd_path)
Part.export([obj], step_path)
print(f"Éxito: Archivos guardados:\\n  {fcstd_path}\\n  {step_path}")
"""

def main():
    script_tmp = "/home/ral/Documents/GitHub/open-source-domotics/scripts/_temp_freecad_pararrayos.py"
    with open(script_tmp, "w", encoding="utf-8") as f:
        f.write(FREECAD_SCRIPT)
    
    cmd = [
        "flatpak-spawn", "--host", "flatpak", "run",
        "--command=freecadcmd", "org.freecad.FreeCAD",
        script_tmp
    ]
    print("Ejecutando FreeCAD headless para modelo 3D del Pararrayos PDC...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Salida:", res.stdout)
    if res.stderr:
        print("Avisos:", res.stderr)
        
    if os.path.exists(script_tmp):
        os.remove(script_tmp)
        
    if res.returncode != 0:
        raise RuntimeError(f"Error generando pararrayos FreeCAD (código {res.returncode})")

if __name__ == "__main__":
    main()
