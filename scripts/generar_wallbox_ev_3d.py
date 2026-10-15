#!/usr/bin/env python3
"""
Generador del Modelo 3D Paramétrico del Cargador de Vehículo Eléctrico (Wallbox Inteligente)
Compatible con conector Tipo 2 (Mennekes / IEC 62196-2) 32A 7.4 kW / 22 kW
Herramienta: FreeCAD 1.1+ (headless con freecadcmd)
Formatos de salida: .FCStd y .step
Proyecto: open-source-domotics
"""

import os
import subprocess

FREECAD_SCRIPT = """
import FreeCAD as App
import Part

doc = App.newDocument("Cargador_EV_Wallbox_Inteligente")

# Dimensiones generales del gabinete Wallbox (mm):
# Ancho (X): 220 mm
# Altura (Z): 330 mm
# Profundidad (Y): 130 mm
w_box = 220.0
h_box = 330.0
d_box = 130.0
espesor_pared = 4.0

# 1. Carcasa principal (Gabinete IP54 / IK10)
cuerpo_exterior = Part.makeBox(w_box, d_box, h_box)
# Chaflanes ergonómicos en esquinas verticales
cuerpo = cuerpo_exterior

# 2. Pestañas de montaje mural posterior (4 orejetas con orificio M6)
orejeta_izq = Part.makeBox(25.0, 10.0, h_box + 30.0)
orejeta_izq.translate(App.Vector(-25.0, 0, -15.0))
orejeta_der = Part.makeBox(25.0, 10.0, h_box + 30.0)
orejeta_der.translate(App.Vector(w_box, 0, -15.0))
cuerpo = cuerpo.fuse(orejeta_izq).fuse(orejeta_der)

# 3. Alojamiento frontal del Receptáculo Tipo 2 (Mennekes IEC 62196)
# Cilindro inclinado o frontal para inserción del conector
r_socket = 35.0  # Radio exterior del barril
h_socket = 40.0
socket_base = Part.makeCylinder(r_socket, h_socket)
socket_base.rotate(App.Vector(0,0,0), App.Vector(1,0,0), -90)
socket_base.translate(App.Vector(w_box / 2.0, d_box, 130.0))
cuerpo = cuerpo.fuse(socket_base)

# Hueco del conector Tipo 2
socket_interior = Part.makeCylinder(30.0, h_socket + 5.0)
socket_interior.rotate(App.Vector(0,0,0), App.Vector(1,0,0), -90)
socket_interior.translate(App.Vector(w_box / 2.0, d_box - 5.0, 130.0))
cuerpo = cuerpo.cut(socket_interior)

# Pines de contacto Type 2 dentro del receptáculo (L1, N, PE, CP, PP)
pin_pe = Part.makeCylinder(3.5, 25.0)
pin_pe.rotate(App.Vector(0,0,0), App.Vector(1,0,0), -90)
pin_pe.translate(App.Vector(w_box / 2.0, d_box, 130.0))
cuerpo = cuerpo.fuse(pin_pe)

for angle_deg in [30, 90, 150, 210, 270, 330]:
    import math
    rad = math.radians(angle_deg)
    px = (w_box / 2.0) + 16.0 * math.cos(rad)
    pz = 130.0 + 16.0 * math.sin(rad)
    pin = Part.makeCylinder(2.5, 20.0)
    pin.rotate(App.Vector(0,0,0), App.Vector(1,0,0), -90)
    pin.translate(App.Vector(px, d_box, pz))
    cuerpo = cuerpo.fuse(pin)

# 4. Aro difusor LED RGB de Estado (anillo alrededor del zócalo)
aro_led = Part.makeCylinder(42.0, 4.0)
aro_led.rotate(App.Vector(0,0,0), App.Vector(1,0,0), -90)
aro_led.translate(App.Vector(w_box / 2.0, d_box + h_socket - 2.0, 130.0))
aro_corte = Part.makeCylinder(38.0, 6.0)
aro_corte.rotate(App.Vector(0,0,0), App.Vector(1,0,0), -90)
aro_corte.translate(App.Vector(w_box / 2.0, d_box + h_socket - 3.0, 130.0))
aro_anillo = aro_led.cut(aro_corte)
cuerpo = cuerpo.fuse(aro_anillo)

# 5. Ventana para Pantalla OLED 1.3" / 0.96" y Lector RFID
oled_bezel = Part.makeBox(60.0, 6.0, 35.0)
oled_bezel.translate(App.Vector((w_box - 60.0)/2.0, d_box - 2.0, 240.0))
cuerpo = cuerpo.fuse(oled_bezel)

rfid_icon = Part.makeCylinder(18.0, 3.0)
rfid_icon.rotate(App.Vector(0,0,0), App.Vector(1,0,0), -90)
rfid_icon.translate(App.Vector(w_box / 2.0, d_box + 1.0, 200.0))
cuerpo = cuerpo.fuse(rfid_icon)

# 6. Pulsador de Parada de Emergencia (Seta de seguridad en lateral derecho)
paro_cuello = Part.makeCylinder(12.0, 15.0)
paro_cuello.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
paro_cuello.translate(App.Vector(w_box, d_box / 2.0, 270.0))

paro_seta = Part.makeCylinder(20.0, 15.0)
paro_seta.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
paro_seta.translate(App.Vector(w_box + 15.0, d_box / 2.0, 270.0))
cuerpo = cuerpo.fuse(paro_cuello).fuse(paro_seta)

# 7. Soporte inferior para enrollar cable de carga (Saddle / Hook)
gancho_base = Part.makeBox(120.0, 60.0, 25.0)
gancho_base.translate(App.Vector((w_box - 120.0)/2.0, d_box - 10.0, 25.0))
gancho_tope = Part.makeBox(120.0, 15.0, 45.0)
gancho_tope.translate(App.Vector((w_box - 120.0)/2.0, d_box + 50.0, 25.0))
cuerpo = cuerpo.fuse(gancho_base).fuse(gancho_tope)

# 8. Prensacables inferiores (M32 Potencia AC, M16 Datos Ethernet/RS485)
prensacable_pot = Part.makeCylinder(19.0, 25.0)
prensacable_pot.translate(App.Vector(w_box * 0.3, d_box / 2.0, -25.0))

prensacable_datos = Part.makeCylinder(11.0, 20.0)
prensacable_datos.translate(App.Vector(w_box * 0.7, d_box / 2.0, -20.0))
cuerpo = cuerpo.fuse(prensacable_pot).fuse(prensacable_datos)

# Añadir objeto final al documento
obj = doc.addObject("Part::Feature", "Wallbox_EV_32A_Inteligente")
obj.Shape = cuerpo

doc.recompute()

# Rutas de exportación
out_dir = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/09_cargador_vehiculo_electrico_ev/mecanico"
os.makedirs(out_dir, exist_ok=True)
fcstd_path = os.path.join(out_dir, "cargador_ev_wallbox.FCStd")
step_path = os.path.join(out_dir, "cargador_ev_wallbox.step")

doc.saveAs(fcstd_path)
Part.export([obj], step_path)
print(f"Éxito: Archivos guardados:\\n  {fcstd_path}\\n  {step_path}")
"""

def main():
    script_tmp = "/home/ral/Documents/GitHub/open-source-domotics/scripts/_temp_freecad_wallbox.py"
    with open(script_tmp, "w", encoding="utf-8") as f:
        f.write(FREECAD_SCRIPT)
    
    cmd = [
        "flatpak-spawn", "--host", "flatpak", "run",
        "--command=freecadcmd", "org.freecad.FreeCAD",
        script_tmp
    ]
    print(f"Ejecutando FreeCAD headless para modelo 3D del Wallbox EV...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Salida:", res.stdout)
    if res.stderr:
        print("Errores/Avisos:", res.stderr)
        
    if os.path.exists(script_tmp):
        os.remove(script_tmp)
        
    if res.returncode != 0:
        raise RuntimeError(f"Error generando modelo FreeCAD (código {res.returncode})")

if __name__ == "__main__":
    main()
