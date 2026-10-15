#!/usr/bin/env python3
"""
Generador del Modelo 3D Paramétrico del Banco de Baterías LiFePO4 48V 14.3 kWh (16S LF280K)
Herramienta: FreeCAD 1.1+ (headless con freecadcmd)
Formatos de salida: .FCStd y .step
Proyecto: open-source-domotics
"""

import os
import subprocess

FREECAD_SCRIPT = """
import FreeCAD as App
import Part

doc = App.newDocument("Banco_Baterias_LiFePO4_16S")

# Dimensiones estándar celda EVE LF280K (mm):
# Ancho (W): 71.5 mm
# Largo (L): 173.5 mm
# Alto cuerpo (H): 207.0 mm
# Altura con terminales: 215.0 mm
w_celda = 71.5
l_celda = 173.5
h_celda = 207.0
num_celdas = 16
espesor_separador = 1.0 # Lámina epoxi FR4 aislante entre celdas
espesor_placa_compresion = 8.0 # mm aluminio/acero

longitud_total = num_celdas * (w_celda + espesor_separador) + 2 * espesor_placa_compresion

# 1. Base / Bandeja de alojamiento en rack (Bandeja 4U/6U reforzada)
bandeja = Part.makeBox(longitud_total + 40.0, l_celda + 30.0, 15.0)
bandeja.translate(App.Vector(-20.0, -15.0, -15.0))
banco = bandeja

# 2. Modelado de las 16 Celdas Prismáticas
x_offset = espesor_placa_compresion
for i in range(num_celdas):
    # Cuerpo de la celda
    celda = Part.makeBox(w_celda, l_celda, h_celda)
    celda.translate(App.Vector(x_offset, 0, 0))
    banco = banco.fuse(celda)
    
    # Terminal Positivo (Borne de aluminio M6/M8)
    # Alternando polaridad para conexión serie 16S
    y_pos = 35.0 if (i % 2 == 0) else (l_celda - 35.0)
    y_neg = (l_celda - 35.0) if (i % 2 == 0) else 35.0
    
    borne_pos = Part.makeCylinder(8.0, 8.0)
    borne_pos.translate(App.Vector(x_offset + w_celda / 2.0, y_pos, h_celda))
    banco = banco.fuse(borne_pos)
    
    # Terminal Negativo (Borne de cobre)
    borne_neg = Part.makeCylinder(8.0, 8.0)
    borne_neg.translate(App.Vector(x_offset + w_celda / 2.0, y_neg, h_celda))
    banco = banco.fuse(borne_neg)
    
    # Válvula de alivio de presión central (Explosion-Proof Vent)
    vent = Part.makeBox(12.0, 18.0, 3.0)
    vent.translate(App.Vector(x_offset + w_celda / 2.0 - 6.0, l_celda / 2.0 - 9.0, h_celda))
    banco = banco.fuse(vent)
    
    x_offset += w_celda + espesor_separador

# 3. Placas de Compresión Frontal y Trasera (Acero 8 mm)
placa_izq = Part.makeBox(espesor_placa_compresion, l_celda + 10.0, h_celda + 5.0)
placa_izq.translate(App.Vector(0, -5.0, 0))
banco = banco.fuse(placa_izq)

placa_der = Part.makeBox(espesor_placa_compresion, l_celda + 10.0, h_celda + 5.0)
placa_der.translate(App.Vector(x_offset, -5.0, 0))
banco = banco.fuse(placa_der)

# 4. Varillas Roscadas de Compresión M8 (4 varillas exteriores longitudinales)
for y_pos in [10.0, l_celda - 10.0]:
    for z_pos in [20.0, h_celda - 20.0]:
        varilla = Part.makeCylinder(4.0, longitud_total + 60.0)
        varilla.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
        varilla.translate(App.Vector(-30.0, y_pos, z_pos))
        banco = banco.fuse(varilla)

# 5. Smart BMS (Montado sobre placa lateral: 200A con pantalla)
bms_caja = Part.makeBox(60.0, 120.0, 30.0)
bms_caja.translate(App.Vector(longitud_total / 2.0 - 30.0, l_celda + 2.0, h_celda / 2.0 - 60.0))
banco = banco.fuse(bms_caja)

# 6. Fusible Clase T de 300A y Seccionador Principal
fusible_t = Part.makeCylinder(22.0, 65.0)
fusible_t.rotate(App.Vector(0,0,0), App.Vector(1,0,0), 90)
fusible_t.translate(App.Vector(40.0, l_celda + 25.0, h_celda - 40.0))
banco = banco.fuse(fusible_t)

obj = doc.addObject("Part::Feature", "Banco_LiFePO4_16S_280Ah")
obj.Shape = banco
doc.recompute()

out_fcstd = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/04_almacenamiento_baterias_ess/mecanico/gabinete_baterias_lifepo4_16s.FCStd"
out_step = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/04_almacenamiento_baterias_ess/mecanico/gabinete_baterias_lifepo4_16s.step"

doc.saveAs(out_fcstd)
Part.export([obj], out_step)
print("Modelo 3D del Banco LiFePO4 16S generado con éxito:")
print(" - FCStd:", out_fcstd)
print(" - STEP:", out_step)
"""

def main():
    script_tmp = "/home/ral/Documents/GitHub/open-source-domotics/scripts/temp_freecad_lifepo4.py"
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

