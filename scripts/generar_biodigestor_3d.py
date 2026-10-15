#!/usr/bin/env python3
"""
Generador del Modelo 3D Paramétrico del Biodigestor y Sistema de Biogás
Herramienta: FreeCAD 1.1+ (headless con freecadcmd)
Formatos de salida: .FCStd y .step
Proyecto: open-source-domotics
"""

import os
import subprocess

FREECAD_SCRIPT = """
import FreeCAD as App
import Part

doc = App.newDocument("Biodigestor_Biogas_Generador")

# Dimensiones generales en mm
# 1. Reactor Biodigestor Anaeróbico Cilíndrico con Fondo Cónico
r_reactor = 600.0  # Radio 600mm -> Diametro 1.20m
h_cilindro = 1400.0
h_cono = 400.0

# Cilindro principal
cilindro = Part.makeCylinder(r_reactor, h_cilindro)
# Cono inferior para lodos
cono = Part.makeCone(r_reactor, 100.0, h_cono)
cono.translate(App.Vector(0, 0, -h_cono))
reactor = cilindro.fuse(cono)

# Tapa hermética superior con brida de registro
tapa = Part.makeCylinder(r_reactor + 50.0, 40.0)
tapa.translate(App.Vector(0, 0, h_cilindro))
reactor = reactor.fuse(tapa)

# Tubería de entrada de aguas negras / lodos orgánicos (PVC 110 mm)
tubo_in = Part.makeCylinder(55.0, 700.0)
tubo_in.rotate(App.Vector(0,0,0), App.Vector(1,0,0), 45)
tubo_in.translate(App.Vector(-r_reactor + 100.0, 0, h_cilindro - 200.0))
reactor = reactor.fuse(tubo_in)

# Tubería de salida de biol / efluente clarificado
tubo_out = Part.makeCylinder(55.0, 600.0)
tubo_out.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
tubo_out.translate(App.Vector(r_reactor - 100.0, 0, h_cilindro - 350.0))
reactor = reactor.fuse(tubo_out)

# Cúpula / Domo de salida de Biogás
domo_gas = Part.makeSphere(200.0)
domo_gas.translate(App.Vector(0, 0, h_cilindro + 40.0))
reactor = reactor.fuse(domo_gas)

# Tubería de salida de biogás (1" INOX / PE-AL-PE)
tubo_gas = Part.makeCylinder(16.0, 350.0)
tubo_gas.translate(App.Vector(0, 0, h_cilindro + 200.0))
reactor = reactor.fuse(tubo_gas)

# 2. Trampa de Condensado y Purga de Agua
trampa_w = Part.makeCylinder(60.0, 220.0)
trampa_w.translate(App.Vector(500.0, 0, h_cilindro))
reactor = reactor.fuse(trampa_w)

# 3. Columna de Desulfuración de H2S (Filtro de Viruta de Hierro Fe2O3)
filtro_h2s = Part.makeCylinder(120.0, 650.0)
filtro_h2s.translate(App.Vector(850.0, 0, h_cilindro - 200.0))
reactor = reactor.fuse(filtro_h2s)

# Bridas del filtro
brida_inf = Part.makeCylinder(150.0, 30.0)
brida_inf.translate(App.Vector(850.0, 0, h_cilindro - 200.0))
brida_sup = Part.makeCylinder(150.0, 30.0)
brida_sup.translate(App.Vector(850.0, 0, h_cilindro + 420.0))
reactor = reactor.fuse(brida_inf).fuse(brida_sup)

# 4. Arrestador de Flama (Parallamas ATEX de Malla Inox AISI 316)
parallamas = Part.makeCylinder(45.0, 90.0)
parallamas.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
parallamas.translate(App.Vector(1050.0, 0, h_cilindro + 200.0))
reactor = reactor.fuse(parallamas)

# 5. Generador Dual (Motogenerador 5 kW a Biogás / Gasolina)
cárter_gen = Part.makeBox(650.0, 480.0, 420.0)
cárter_gen.translate(App.Vector(1250.0, -240.0, 100.0))
alternador = Part.makeCylinder(160.0, 300.0)
alternador.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)
alternador.translate(App.Vector(1250.0 + 350.0, 0, 310.0))
reactor = reactor.fuse(cárter_gen).fuse(alternador)

# Cuadro ATS de Transferencia y Control en pared
cuadro_ats = Part.makeBox(300.0, 180.0, 400.0)
cuadro_ats.translate(App.Vector(1400.0, -90.0, 700.0))
reactor = reactor.fuse(cuadro_ats)

obj = doc.addObject("Part::Feature", "Sistema_Biodigestor_Biogas_Generador")
obj.Shape = reactor

doc.recompute()

out_dir = "/home/ral/Documents/GitHub/open-source-domotics/01_energia_renovable_y_potencia/05_biodigestor_biogas_generador/mecanico"
os.makedirs(out_dir, exist_ok=True)
fcstd_path = os.path.join(out_dir, "biodigestor_biogas_sistema.FCStd")
step_path = os.path.join(out_dir, "biodigestor_biogas_sistema.step")

doc.saveAs(fcstd_path)
Part.export([obj], step_path)
print(f"Éxito: Archivos guardados:\\n  {fcstd_path}\\n  {step_path}")
"""

def main():
    script_tmp = "/home/ral/Documents/GitHub/open-source-domotics/scripts/_temp_freecad_biodigestor.py"
    with open(script_tmp, "w", encoding="utf-8") as f:
        f.write(FREECAD_SCRIPT)
    
    cmd = [
        "flatpak-spawn", "--host", "flatpak", "run",
        "--command=freecadcmd", "org.freecad.FreeCAD",
        script_tmp
    ]
    print("Ejecutando FreeCAD headless para modelo 3D del Biodigestor y Biogás...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Salida:", res.stdout)
    if res.stderr:
        print("Avisos:", res.stderr)
        
    if os.path.exists(script_tmp):
        os.remove(script_tmp)
        
    if res.returncode != 0:
        raise RuntimeError(f"Error generando biodigestor FreeCAD (código {res.returncode})")

if __name__ == "__main__":
    main()
