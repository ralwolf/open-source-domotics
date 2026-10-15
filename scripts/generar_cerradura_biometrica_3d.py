#!/usr/bin/env python3
"""
Generador del Modelo 3D Paramétrico del Panel de Acceso Biométrico y Teclado RFID
Herramienta: FreeCAD 1.1+ (headless con freecadcmd)
Formatos de salida: .FCStd y .step
Proyecto: open-source-domotics
"""

import os
import subprocess

FREECAD_SCRIPT = """
import FreeCAD as App
import Part

doc = App.newDocument("Panel_Acceso_Biometrico_IP65")

# Dimensiones en mm (Panel mural estrecho de entrada: 70 x 160 x 25 mm)
w_panel = 70.0
h_panel = 160.0
d_panel = 25.0
espesor = 3.0

# 1. Carcasa principal de aleación de aluminio / polímero reforzado
cuerpo = Part.makeBox(w_panel, d_panel, h_panel)

# 2. Alojamiento circular para sensor de huella dactilar capacitivo R503 (Diam 21mm)
hueco_huella = Part.makeCylinder(11.0, 10.0)
hueco_huella.rotate(App.Vector(0,0,0), App.Vector(1,0,0), -90)
hueco_huella.translate(App.Vector(w_panel / 2.0, d_panel - 5.0, 125.0))

anillo_led_huella = Part.makeCylinder(13.5, 4.0)
anillo_led_huella.rotate(App.Vector(0,0,0), App.Vector(1,0,0), -90)
anillo_led_huella.translate(App.Vector(w_panel / 2.0, d_panel - 2.0, 125.0))

cuerpo = cuerpo.cut(hueco_huella).fuse(anillo_led_huella)

# 3. Ventana para pantalla OLED 0.96" o matriz de estado
pantalla = Part.makeBox(38.0, 4.0, 22.0)
pantalla.translate(App.Vector((w_panel - 38.0) / 2.0, d_panel - 2.0, 85.0))
cuerpo = cuerpo.cut(pantalla)

# 4. Teclado capacitivo numérico / Lector RFID (Zona táctil)
zona_rfid = Part.makeCylinder(18.0, 2.0)
zona_rfid.rotate(App.Vector(0,0,0), App.Vector(1,0,0), -90)
zona_rfid.translate(App.Vector(w_panel / 2.0, d_panel - 1.0, 50.0))
cuerpo = cuerpo.fuse(zona_rfid)

# 5. Pulsador de llamada / Timbre en parte inferior
pulsador_timbre = Part.makeCylinder(9.0, 4.0)
pulsador_timbre.rotate(App.Vector(0,0,0), App.Vector(1,0,0), -90)
pulsador_timbre.translate(App.Vector(w_panel / 2.0, d_panel - 2.0, 22.0))
cuerpo = cuerpo.fuse(pulsador_timbre)

# 6. Placa posterior de anclaje mural con orificio para cableado y tamper switch
placa_post = Part.makeBox(w_panel - 4.0, 3.0, h_panel - 4.0)
placa_post.translate(App.Vector(2.0, -3.0, 2.0))
orificio_cable = Part.makeCylinder(10.0, 10.0)
orificio_cable.rotate(App.Vector(0,0,0), App.Vector(1,0,0), -90)
orificio_cable.translate(App.Vector(w_panel / 2.0, -5.0, 80.0))
placa_post = placa_post.cut(orificio_cable)

panel_completo = cuerpo.fuse(placa_post)

obj = doc.addObject("Part::Feature", "Panel_Control_Acceso_Biometrico")
obj.Shape = panel_completo

doc.recompute()

out_dir = "/home/ral/Documents/GitHub/open-source-domotics/03_seguridad_y_control_acceso/02_cerraduras_biometricas/mecanico"
os.makedirs(out_dir, exist_ok=True)
fcstd_path = os.path.join(out_dir, "panel_acceso_biometrico.FCStd")
step_path = os.path.join(out_dir, "panel_acceso_biometrico.step")

doc.saveAs(fcstd_path)
Part.export([obj], step_path)
print(f"Éxito: Archivos guardados:\\n  {fcstd_path}\\n  {step_path}")
"""

def main():
    script_tmp = "/home/ral/Documents/GitHub/open-source-domotics/scripts/_temp_freecad_cerradura.py"
    with open(script_tmp, "w", encoding="utf-8") as f:
        f.write(FREECAD_SCRIPT)
    
    cmd = [
        "flatpak-spawn", "--host", "flatpak", "run",
        "--command=freecadcmd", "org.freecad.FreeCAD",
        script_tmp
    ]
    print("Ejecutando FreeCAD headless para panel biométrico...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Salida:", res.stdout)
    if res.stderr:
        print("Avisos:", res.stderr)
        
    if os.path.exists(script_tmp):
        os.remove(script_tmp)
        
    if res.returncode != 0:
        raise RuntimeError(f"Error generando panel biométrico FreeCAD (código {res.returncode})")

if __name__ == "__main__":
    main()
