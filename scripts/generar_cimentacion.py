#!/usr/bin/env python3
"""
Generador paramétrico de Cimentaciones y Estructura en FreeCAD
Proyecto: open-source-domotics
Genera: cimentacion_zapatas_pilares.FCStd y cimentacion_zapatas_pilares.step
"""

import sys
import os

try:
    import FreeCAD
    import Part
    from FreeCAD import Vector
except ImportError:
    print("Error: Este script debe ser ejecutado bajo el entorno de FreeCADCmd.")
    sys.exit(1)

def build_foundations(output_fcstd, output_step):
    print("Iniciando generación de modelo paramétrico de cimentación y pilares...")
    doc = FreeCAD.newDocument("Cimentacion_open_source_domotics")
    
    # Parámetros dimensionales (en mm)
    ZAPATA_W = 1300.0
    ZAPATA_L = 1300.0
    ZAPATA_H = 450.0
    
    COLUMNA_W = 300.0
    COLUMNA_L = 300.0
    COLUMNA_H = 3000.0
    
    COL_TURB_W = 350.0
    COL_TURB_L = 350.0
    COL_TURB_H = 3500.0
    
    VIGA_W = 300.0
    VIGA_H = 300.0
    
    # Coordenadas de los 9 pilares principales (Ejes 1-3, A-C a 5000 mm)
    grid_x = [0.0, 5000.0, 10000.0]
    grid_y = [0.0, 5000.0, 10000.0]
    
    compound_shapes = []
    
    # 1. Zapatas y Columnas
    for i, x in enumerate(grid_x):
        for j, y in enumerate(grid_y):
            # Zapata aislada
            box_zap = Part.makeBox(
                ZAPATA_W, ZAPATA_L, ZAPATA_H,
                Vector(x - ZAPATA_W/2, y - ZAPATA_L/2, -ZAPATA_H)
            )
            compound_shapes.append(box_zap)
            
            # Columna
            is_turb = (x == 10000.0 and y == 10000.0)
            cw = COL_TURB_W if is_turb else COLUMNA_W
            cl = COL_TURB_L if is_turb else COLUMNA_L
            ch = COL_TURB_H if is_turb else COLUMNA_H
            
            box_col = Part.makeBox(
                cw, cl, ch,
                Vector(x - cw/2, y - cl/2, 0.0)
            )
            compound_shapes.append(box_col)
    
    # 2. Vigas Riostras de Atado (Eje X)
    for y in grid_y:
        for k in range(len(grid_x) - 1):
            x1 = grid_x[k] + ZAPATA_W/2
            x2 = grid_x[k+1] - ZAPATA_W/2
            length = x2 - x1
            if length > 0:
                viga_x = Part.makeBox(
                    length, VIGA_W, VIGA_H,
                    Vector(x1, y - VIGA_W/2, -VIGA_H)
                )
                compound_shapes.append(viga_x)
                
    # 3. Vigas Riostras de Atado (Eje Y)
    for x in grid_x:
        for k in range(len(grid_y) - 1):
            y1 = grid_y[k] + ZAPATA_L/2
            y2 = grid_y[k+1] - ZAPATA_L/2
            length = y2 - y1
            if length > 0:
                viga_y = Part.makeBox(
                    VIGA_W, length, VIGA_H,
                    Vector(x - VIGA_W/2, y1, -VIGA_H)
                )
                compound_shapes.append(viga_y)
                
    # 4. Losa Reforzada de Sala Técnica IT y Banco de Baterías
    # Ubicada entre (0,0) y (3000, 2500) mm
    losa_it = Part.makeBox(
        3200.0, 2700.0, 200.0,
        Vector(-100.0, -100.0, 0.0)
    )
    compound_shapes.append(losa_it)
    
    # 5. Placa de anclaje de la turbina eólica en cabeza de columna maestra
    placa_turb = Part.makeBox(
        400.0, 400.0, 20.0,
        Vector(10000.0 - 200.0, 10000.0 - 200.0, COL_TURB_H)
    )
    compound_shapes.append(placa_turb)
    
    # Fusionar piezas en estructura compuesta
    structure_compound = Part.makeCompound(compound_shapes)
    
    feature = doc.addObject("Part::Feature", "Estructura_Cimentacion_Pilares")
    feature.Shape = structure_compound
    
    # Asegurar que los directorios de destino existen
    os.makedirs(os.path.dirname(os.path.abspath(output_fcstd)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(output_step)), exist_ok=True)
    
    # Recomputar y guardar
    doc.recompute()
    doc.saveAs(output_fcstd)
    print(f"Modelo guardado exitosamente en: {output_fcstd}")
    
    # Exportar formato STEP estandarizado ISO 10303-21
    Part.export([feature], output_step)
    print(f"Exportación STEP completada en: {output_step}")

if __name__ == "__main__":
    fcstd_target = "/home/ral/Documents/GitHub/open-source-domotics/00_diseno_arquitectonico_y_estructural/01_mecanica_suelos_y_cimentacion/planos_y_calculos/cimentacion_zapatas_pilares.FCStd"
    step_target = "/home/ral/Documents/GitHub/open-source-domotics/00_diseno_arquitectonico_y_estructural/01_mecanica_suelos_y_cimentacion/planos_y_calculos/cimentacion_zapatas_pilares.step"
    build_foundations(fcstd_target, step_target)
