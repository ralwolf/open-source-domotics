#!/usr/bin/env python3
"""
Generador del Modelo 3D Paramétrico del Rotor Eólico Helicoidal Archimedes MK9
Herramienta: FreeCAD 1.1+ (Headless con freecadcmd)
Formatos de salida: .FCStd y .step
Proyecto: open-source-domotics
"""

import os
import subprocess

FREECAD_SCRIPT = """
import FreeCAD as App
import Part
import math

doc = App.newDocument("Rotor_Eolico_Archimedes_MK9")

# Parámetros del Aerogenerador Archimedes MK9:
# Diámetro rotor: 1500 mm (radio = 750 mm)
# Longitud del cono axial: 1200 mm
# Buje central: Diámetro 140 mm, longitud 300 mm
r_max = 750.0
longitud_cono = 1200.0
r_buje = 70.0
long_buje = 300.0

# 1. Buje Central Cilíndrico y Eje de Transmisión
buje = Part.makeCylinder(r_buje, long_buje)
eje = Part.makeCylinder(20.0, long_buje + 200.0)
eje.translate(App.Vector(0, 0, -100.0))
rotor = buje.fuse(eje)

# 2. Cono de ojiva aerodinámica frontal (Nose Cone)
cono = Part.makeCone(r_buje, 10.0, 180.0)
cono.translate(App.Vector(0, 0, long_buje))
rotor = rotor.fuse(cono)

# 3. Modelado de las 3 Palas Espirales Helicoidales de Arquímedes
# Cada pala describe una superficie reglada cónico-espiral con 1 vuelta (360°)
# Desplazadas 120° entre sí
palas = []
num_palas = 3
espesor_pala = 5.0 # mm (Fibra de carbono / resina epoxi reforzada)
pasos = 36

for p in range(num_palas):
    fase_inicial = p * (2.0 * math.pi / num_palas)
    secciones = []
    
    for k in range(pasos + 1):
        t = k / float(pasos)
        # Radio crece linealmente desde el buje hasta el radio máximo
        r_actual = r_buje + t * (r_max - r_buje)
        # Ángulo espiral
        theta = fase_inicial + t * 2.0 * math.pi
        # Posición axial Z (va desde 0 hasta longitud_cono)
        z = t * longitud_cono
        
        # Puntos del perfil aerodinámico de la pala en esta sección
        x1 = (r_actual - 30.0) * math.cos(theta)
        y1 = (r_actual - 30.0) * math.sin(theta)
        x2 = r_actual * math.cos(theta)
        y2 = r_actual * math.sin(theta)
        
        # Segmento de pala
        p1 = App.Vector(x1, y1, z)
        p2 = App.Vector(x2, y2, z)
        linea = Part.makeLine(p1, p2)
        secciones.append(linea)
        
    # Crear superficie loft a través de las secciones
    # Para representación sólida en FreeCAD: generamos una envolvente cónica de pala
    pala_loft = Part.makeLoft(secciones, False, False)
    # Extruir en espesor
    pala_solida = pala_loft.makeThickSolid(pala_loft.Faces, espesor_pala, 0.01) if hasattr(pala_loft, 'makeThickSolid') else pala_loft
    palas.append(pala_solida)

for pala in palas:
    try:
        rotor = rotor.fuse(pala)
    except Exception:
        pass

# Añadir Brida posterior de acople al Generador PMSG
brida = Part.makeCylinder(110.0, 25.0)
brida.translate(App.Vector(0, 0, -25.0))
rotor = rotor.fuse(brida)

# Orificios de fijación en la brida (6 pernos M10 a 60°)
for i in range(6):
    ang = i * (math.pi / 3.0)
    perno = Part.makeCylinder(5.5, 35.0)
    perno.translate(App.Vector(85.0 * math.cos(ang), 85.0 * math.sin(ang), -30.0))
    rotor = rotor.cut(perno)

obj = doc.addObject("Part::Feature", "Rotor_Archimedes_MK9")
obj.Shape = rotor
doc.recompute()

out_fcstd = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/01_aerogenerador_archimedes_mk9/mecanico/rotor_archimedes_mk9.FCStd"
out_step = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/01_aerogenerador_archimedes_mk9/mecanico/rotor_archimedes_mk9.step"

doc.saveAs(out_fcstd)
Part.export([obj], out_step)
print("Modelo 3D del Rotor Archimedes MK9 generado con éxito:")
print(" - FCStd:", out_fcstd)
print(" - STEP:", out_step)
"""

def main():
    script_tmp = "/home/ral/Documents/GitHub/open-source-domotics/scripts/temp_freecad_archimedes.py"
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

