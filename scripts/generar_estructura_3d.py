#!/usr/bin/env python3
"""
Generador del Modelo 3D Paramétrico de la Estructura Portante (Pilares, Vigas y Losa)
Herramienta: FreeCAD 1.1+ (headless con freecadcmd)
Formatos de salida: .FCStd y .step
Proyecto: open-source-domotics
"""

import os
import subprocess

FREECAD_SCRIPT = """
import FreeCAD as App
import Part

doc = App.newDocument("Estructura_Portante_Vivienda")

# Dimensiones en mm (Vivienda 10m x 10m)
# Altura de entrepiso: 3000 mm (3.0 m)
# Espesor de losa: 200 mm
h_col = 3000.0
espesor_losa = 200.0
h_viga = 400.0
w_viga = 250.0

# Posiciones de los 9 pilares (Ejes A, B, C a Y = 500, 5000, 9500; Ejes 1, 2, 3 a X = 500, 5000, 9500)
coords_pilares = [
    # Eje A
    (500.0, 500.0, False, "P1"),
    (5000.0, 500.0, False, "P2"),
    (9500.0, 500.0, False, "P3"),
    # Eje B
    (500.0, 5000.0, False, "P4"),
    (5000.0, 5000.0, False, "P5"),
    (9500.0, 5000.0, False, "P6"),
    # Eje C
    (500.0, 9500.0, False, "P7"),
    (5000.0, 9500.0, False, "P8"),
    (9500.0, 9500.0, True, "P9_TURB"), # Pilar esquina técnica reforzado
]

estructura = None

# 1. Modelado de los 9 Pilares
for x, y, es_turb, tag in coords_pilares:
    w_p = 350.0 if es_turb else 300.0
    h_p = 350.0 if es_turb else 300.0
    
    col = Part.makeBox(w_p, h_p, h_col)
    col.translate(App.Vector(x - w_p / 2.0, y - h_p / 2.0, 0))
    
    if es_turb:
        # Sobreelevación / Muelle de anclaje para mástil eólico en azotea
        pedestal = Part.makeBox(400.0, 400.0, 800.0)
        pedestal.translate(App.Vector(x - 200.0, y - 200.0, h_col))
        col = col.fuse(pedestal)
        
    if estructura is None:
        estructura = col
    else:
        estructura = estructura.fuse(col)

# 2. Modelado de las Vigas Principales de Amarre (Cinturón perimetral e interior)
# Vigas en X (longitudinales) a lo largo de Ejes A (500), B (5000), C (9500)
for y in [500.0, 5000.0, 9500.0]:
    viga_x = Part.makeBox(9600.0, w_viga, h_viga)
    viga_x.translate(App.Vector(200.0, y - w_viga / 2.0, h_col - h_viga))
    estructura = estructura.fuse(viga_x)

# Vigas en Y (transversales) a lo largo de Ejes 1 (500), 2 (5000), 3 (9500)
for x in [500.0, 5000.0, 9500.0]:
    viga_y = Part.makeBox(w_viga, 9600.0, h_viga)
    viga_y.translate(App.Vector(x - w_viga / 2.0, 200.0, h_col - h_viga))
    estructura = estructura.fuse(viga_y)

# 3. Modelado de la Losa Superior Maciza de Cubierta (10.0m x 10.0m x 0.20m)
losa = Part.makeBox(10000.0, 10000.0, espesor_losa)
losa.translate(App.Vector(0, 0, h_col))

# Hueco Cenital Central para el Lucernario Astronómico (3.0m x 2.0m en centro geométrico)
hueco_cenital = Part.makeBox(3000.0, 2000.0, espesor_losa + 20.0)
hueco_cenital.translate(App.Vector(3500.0, 4000.0, h_col - 10.0))
losa = losa.cut(hueco_cenital)

# Brocal perimetral del hueco cenital (recrecido de apoyo para carpintería RPT)
brocal = Part.makeBox(3200.0, 2200.0, 250.0)
brocal.translate(App.Vector(3400.0, 3900.0, h_col + espesor_losa))
brocal_hueco = Part.makeBox(3000.0, 2000.0, 260.0)
brocal_hueco.translate(App.Vector(3500.0, 4000.0, h_col + espesor_losa - 5.0))
brocal = brocal.cut(brocal_hueco)

losa = losa.fuse(brocal)
estructura = estructura.fuse(losa)

obj = doc.addObject("Part::Feature", "Estructura_Portante_Pilares_Losas")
obj.Shape = estructura

doc.recompute()

out_dir = "/home/ral/Documents/GitHub/open-source-domotics/00_diseno_arquitectonico_y_estructural/02_estructura_pilares_y_losas/planos_y_calculos"
os.makedirs(out_dir, exist_ok=True)
fcstd_path = os.path.join(out_dir, "estructura_portante_vivienda.FCStd")
step_path = os.path.join(out_dir, "estructura_portante_vivienda.step")

doc.saveAs(fcstd_path)
Part.export([obj], step_path)
print(f"Éxito: Archivos guardados:\\n  {fcstd_path}\\n  {step_path}")
"""

def main():
    script_tmp = "/home/ral/Documents/GitHub/open-source-domotics/scripts/_temp_freecad_estructura.py"
    with open(script_tmp, "w", encoding="utf-8") as f:
        f.write(FREECAD_SCRIPT)
    
    cmd = [
        "flatpak-spawn", "--host", "flatpak", "run",
        "--command=freecadcmd", "org.freecad.FreeCAD",
        script_tmp
    ]
    print("Ejecutando FreeCAD headless para modelo 3D estructural...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Salida:", res.stdout)
    if res.stderr:
        print("Avisos:", res.stderr)
        
    if os.path.exists(script_tmp):
        os.remove(script_tmp)
        
    if res.returncode != 0:
        raise RuntimeError(f"Error generando estructura FreeCAD (código {res.returncode})")

if __name__ == "__main__":
    main()
