#!/usr/bin/env python3
"""
Generador paramétrico de Vitrina / Lucernario Astronómico Cenital en FreeCAD
Proyecto: open-source-domotics
Genera: lucernario_astronomico_cenital.FCStd y lucernario_astronomico_cenital.step
"""

import sys
import os

try:
    import FreeCAD
    import Part
    from FreeCAD import Vector
except ImportError:
    print("Error: Ejecutar bajo FreeCADCmd.")
    sys.exit(1)

def build_skylight(output_fcstd, output_step):
    print("Generando modelo 3D del Lucernario Astronómico Cenital...")
    doc = FreeCAD.newDocument("Lucernario_Astronomico_Cenital")
    
    # Dimensiones generales (en mm)
    LARGO = 3000.0
    ANCHO = 2000.0
    PERFIL_H = 80.0
    PERFIL_W = 40.0
    VIDRIO_THICK = 24.0 # 8 mm ext + 8 mm int + 16 mm cámara/intercalario
    
    parts = []
    
    # 1. Bastidor Perimetral Exterior Fijo (Acero rectangular 80x40x3)
    # Larguero inferior Y=0
    l1 = Part.makeBox(LARGO, PERFIL_W, PERFIL_H, Vector(0, 0, 0))
    # Larguero superior Y=ANCHO-PERFIL_W
    l2 = Part.makeBox(LARGO, PERFIL_W, PERFIL_H, Vector(0, ANCHO - PERFIL_W, 0))
    # Travesaño izquierdo X=0
    t1 = Part.makeBox(PERFIL_W, ANCHO - 2*PERFIL_W, PERFIL_H, Vector(0, PERFIL_W, 0))
    # Travesaño derecho X=LARGO-PERFIL_W
    t2 = Part.makeBox(PERFIL_W, ANCHO - 2*PERFIL_W, PERFIL_H, Vector(LARGO - PERFIL_W, PERFIL_W, 0))
    # Travesaño intermedio de refuerzo X=LARGO/2
    t_mid = Part.makeBox(PERFIL_W, ANCHO - 2*PERFIL_W, PERFIL_H, Vector(LARGO/2 - PERFIL_W/2, PERFIL_W, 0))
    
    frame_steel = Part.makeCompound([l1, l2, t1, t2, t_mid])
    parts.append(frame_steel)
    
    # 2. Marco de Aluminio con Rotura de Puente Térmico (RPT) abatible
    MARCO_ALU_W = 50.0
    MARCO_ALU_H = 60.0
    al1 = Part.makeBox(LARGO - 20, MARCO_ALU_W, MARCO_ALU_H, Vector(10, 10, PERFIL_H))
    al2 = Part.makeBox(LARGO - 20, MARCO_ALU_W, MARCO_ALU_H, Vector(10, ANCHO - 10 - MARCO_ALU_W, PERFIL_H))
    at1 = Part.makeBox(MARCO_ALU_W, ANCHO - 20 - 2*MARCO_ALU_W, MARCO_ALU_H, Vector(10, 10 + MARCO_ALU_W, PERFIL_H))
    at2 = Part.makeBox(MARCO_ALU_W, ANCHO - 20 - 2*MARCO_ALU_W, MARCO_ALU_H, Vector(LARGO - 10 - MARCO_ALU_W, 10 + MARCO_ALU_W, PERFIL_H))
    
    frame_alu = Part.makeCompound([al1, al2, at1, at2])
    parts.append(frame_alu)
    
    # 3. Paquete de Acristalamiento Doble Low-Iron (Vidrio Extraclaro)
    # Panel Izquierdo
    v_w = (LARGO - 20 - 2*MARCO_ALU_W - PERFIL_W) / 2
    v_l = ANCHO - 20 - 2*MARCO_ALU_W
    vidrio_izq = Part.makeBox(v_w, v_l, VIDRIO_THICK, Vector(10 + MARCO_ALU_W, 10 + MARCO_ALU_W, PERFIL_H + MARCO_ALU_H - VIDRIO_THICK))
    vidrio_der = Part.makeBox(v_w, v_l, VIDRIO_THICK, Vector(10 + MARCO_ALU_W + v_w + PERFIL_W, 10 + MARCO_ALU_W, PERFIL_H + MARCO_ALU_H - VIDRIO_THICK))
    
    glazing = Part.makeCompound([vidrio_izq, vidrio_der])
    parts.append(glazing)
    
    # 4. Actuadores Lineales Electromecánicos 24V (Cuerpo cilíndrico y vástago)
    # Actuador lado izquierdo
    act1_body = Part.makeCylinder(25.0, 350.0, Vector(500.0, 100.0, -150.0), Vector(0.0, 0.3, 0.95))
    # Actuador lado derecho
    act2_body = Part.makeCylinder(25.0, 350.0, Vector(2500.0, 100.0, -150.0), Vector(0.0, 0.3, 0.95))
    actuators = Part.makeCompound([act1_body, act2_body])
    parts.append(actuators)
    
    # 5. Cofre de Persiana Térmica Exterior Enrollable
    cofre = Part.makeBox(LARGO, 180.0, 180.0, Vector(0, ANCHO - 50.0, PERFIL_H + MARCO_ALU_H))
    parts.append(cofre)
    
    skylight_compound = Part.makeCompound(parts)
    
    feat = doc.addObject("Part::Feature", "Vitrina_Lucernario_Astronomico")
    feat.Shape = skylight_compound
    
    os.makedirs(os.path.dirname(os.path.abspath(output_fcstd)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(output_step)), exist_ok=True)
    
    doc.recompute()
    doc.saveAs(output_fcstd)
    Part.export([feat], output_step)
    print(f"Lucernario guardado en: {output_fcstd} y {output_step}")

if __name__ == "__main__":
    fcstd_out = "/home/ral/Documents/GitHub/open-source-domotics/00_diseno_arquitectonico_y_estructural/04_bioclimatica_ventilacion_lucernario_celeste/mecanico/lucernario_astronomico_cenital.FCStd"
    step_out = "/home/ral/Documents/GitHub/open-source-domotics/00_diseno_arquitectonico_y_estructural/04_bioclimatica_ventilacion_lucernario_celeste/mecanico/lucernario_astronomico_cenital.step"
    build_skylight(fcstd_out, step_out)
