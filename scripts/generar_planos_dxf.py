#!/usr/bin/env python3
"""
Generador de Planos 2D en formato DXF estándar (LibreCAD / FreeCAD / Ingetrazzo)
Proyecto: open-source-domotics
"""

import os

class SimpleDXF:
    def __init__(self, filepath):
        self.filepath = filepath
        self.layers = set()
        self.entities = []

    def add_layer(self, name, color=7):
        self.layers.add((name, color))

    def add_line(self, x1, y1, x2, y2, layer="0"):
        self.entities.append(f"0\nLINE\n8\n{layer}\n10\n{x1:.3f}\n20\n{y1:.3f}\n30\n0.0\n11\n{x2:.3f}\n21\n{y2:.3f}\n31\n0.0\n")

    def add_rect(self, x, y, w, h, layer="0"):
        self.add_line(x, y, x + w, y, layer)
        self.add_line(x + w, y, x + w, y + h, layer)
        self.add_line(x + w, y + h, x, y + h, layer)
        self.add_line(x, y + h, x, y, layer)

    def add_circle(self, cx, cy, r, layer="0"):
        self.entities.append(f"0\nCIRCLE\n8\n{layer}\n10\n{cx:.3f}\n20\n{cy:.3f}\n30\n0.0\n40\n{r:.3f}\n")

    def add_text(self, text, x, y, height=250.0, layer="0"):
        self.entities.append(f"0\nTEXT\n8\n{layer}\n10\n{x:.3f}\n20\n{y:.3f}\n30\n0.0\n40\n{height:.3f}\n1\n{text}\n")

    def save(self):
        os.makedirs(os.path.dirname(os.path.abspath(self.filepath)), exist_ok=True)
        with open(self.filepath, "w", encoding="utf-8") as f:
            # HEADER
            f.write("0\nSECTION\n2\nHEADER\n9\n$ACADVER\n1\nAC1009\n0\nENDSEC\n")
            # TABLES
            f.write("0\nSECTION\n2\nTABLES\n0\nTABLE\n2\nLAYER\n70\n" + str(len(self.layers)) + "\n")
            for name, color in self.layers:
                f.write(f"0\nLAYER\n2\n{name}\n70\n0\n62\n{color}\n6\nCONTINUOUS\n")
            f.write("0\nENDTAB\n0\nENDSEC\n")
            # BLOCKS
            f.write("0\nSECTION\n2\nBLOCKS\n0\nENDSEC\n")
            # ENTITIES
            f.write("0\nSECTION\n2\nENTITIES\n")
            for ent in self.entities:
                f.write(ent)
            f.write("0\nENDSEC\n0\nEOF\n")
        print(f"Plano DXF generado: {self.filepath}")

def build_foundation_dxf(filepath):
    dxf = SimpleDXF(filepath)
    # Capas (Colores: 1=Rojo, 2=Amarillo, 3=Verde, 4=Cian, 5=Azul, 6=Magenta, 7=Blanco)
    dxf.add_layer("EJES", color=1)
    dxf.add_layer("CIM_ZAPATAS", color=4)
    dxf.add_layer("CIM_RIOSTRAS", color=3)
    dxf.add_layer("ESTR_COLUMNAS", color=2)
    dxf.add_layer("SALA_IT_LOSA", color=6)
    dxf.add_layer("TEXTO_COTAS", color=7)
    
    grid_x = [0.0, 5000.0, 10000.0]
    grid_y = [0.0, 5000.0, 10000.0]
    ejes_x_labels = ["1", "2", "3"]
    ejes_y_labels = ["A", "B", "C"]
    
    # Ejes longitudinales y transversales con prolongación
    for i, x in enumerate(grid_x):
        dxf.add_line(x, -1200.0, x, 11200.0, layer="EJES")
        dxf.add_circle(x, -1500.0, 250.0, layer="EJES")
        dxf.add_text(ejes_x_labels[i], x - 70.0, -1600.0, height=200.0, layer="TEXTO_COTAS")
        
    for j, y in enumerate(grid_y):
        dxf.add_line(-1200.0, y, 11200.0, y, layer="EJES")
        dxf.add_circle(-1500.0, y, 250.0, layer="EJES")
        dxf.add_text(ejes_y_labels[j], -1600.0, y - 70.0, height=200.0, layer="TEXTO_COTAS")
        
    # Zapatas y Columnas
    for i, x in enumerate(grid_x):
        for j, y in enumerate(grid_y):
            # Zapata aislada 1.30 x 1.30 m
            dxf.add_rect(x - 650.0, y - 650.0, 1300.0, 1300.0, layer="CIM_ZAPATAS")
            # Columna
            is_turb = (x == 10000.0 and y == 10000.0)
            cw = 350.0 if is_turb else 300.0
            dxf.add_rect(x - cw/2, y - cw/2, cw, cw, layer="ESTR_COLUMNAS")
            label = "C-TURB (35x35)" if is_turb else f"C{i+1}{j+1} (30x30)"
            dxf.add_text(label, x - 500.0, y + 700.0, height=120.0, layer="TEXTO_COTAS")
            
    # Vigas Riostras Eje X
    for y in grid_y:
        for k in range(len(grid_x) - 1):
            x1 = grid_x[k] + 650.0
            x2 = grid_x[k+1] - 650.0
            dxf.add_rect(x1, y - 150.0, x2 - x1, 300.0, layer="CIM_RIOSTRAS")
            
    # Vigas Riostras Eje Y
    for x in grid_x:
        for k in range(len(grid_y) - 1):
            y1 = grid_y[k] + 650.0
            y2 = grid_y[k+1] - 650.0
            dxf.add_rect(x - 150.0, y1, 300.0, y2 - y1, layer="CIM_RIOSTRAS")
            
    # Losa Sala Técnica IT y Baterías
    dxf.add_rect(-100.0, -100.0, 3200.0, 2700.0, layer="SALA_IT_LOSA")
    dxf.add_text("LOSA REFORZADA SALA TECNICA IT Y BATERIAS (e=20cm)", 200.0, 1200.0, height=140.0, layer="TEXTO_COTAS")
    
    # Cuadro de datos y rótulo
    dxf.add_rect(6500.0, -2500.0, 4500.0, 1800.0, layer="TEXTO_COTAS")
    dxf.add_text("PROYECTO: open-source-domotics", 6700.0, -1000.0, height=180.0, layer="TEXTO_COTAS")
    dxf.add_text("PLANO: REPLANTEO DE CIMENTACION Y PILARES", 6700.0, -1300.0, height=150.0, layer="TEXTO_COTAS")
    dxf.add_text("ESCALA: 1:50 | COTAS EN MILIMETROS", 6700.0, -1600.0, height=120.0, layer="TEXTO_COTAS")
    dxf.add_text("SOFTWARE: LIBRE (LibreCAD / FreeCAD / DXF R12)", 6700.0, -1900.0, height=120.0, layer="TEXTO_COTAS")
    
    dxf.save()

def build_architectural_dxf(filepath):
    dxf = SimpleDXF(filepath)
    dxf.add_layer("MUROS_CARGA", color=7)
    dxf.add_layer("TABIQUES", color=3)
    dxf.add_layer("VENTANAS_PUERTAS", color=4)
    dxf.add_layer("LUCERNARIO_CENITAL", color=6)
    dxf.add_layer("DUCTOS_FUERZA", color=2)
    dxf.add_layer("DUCTOS_DATOS", color=1)
    dxf.add_layer("ZONIFICACION", color=5)
    
    # Perímetro exterior de vivienda (10 x 10 m con terrazas)
    dxf.add_rect(0.0, 0.0, 10000.0, 10000.0, layer="MUROS_CARGA")
    
    # Sala Técnica IT (Suroeste)
    dxf.add_rect(200.0, 200.0, 2800.0, 2300.0, layer="TABIQUES")
    dxf.add_text("SALA TECNICA IT / BATERIAS / INVERSOR", 400.0, 1200.0, height=120.0, layer="ZONIFICACION")
    
    # Cocina y Lavandería
    dxf.add_rect(3200.0, 200.0, 3600.0, 4000.0, layer="TABIQUES")
    dxf.add_text("COCINA / COMEDOR BIOCLIMATICO", 3500.0, 2000.0, height=140.0, layer="ZONIFICACION")
    
    # Sala de Estar Central con Doble Altura
    dxf.add_rect(200.0, 4400.0, 6600.0, 5400.0, layer="TABIQUES")
    dxf.add_text("SALA PRINCIPAL / ZONA DE ESTAR", 2000.0, 6500.0, height=160.0, layer="ZONIFICACION")
    
    # Vitrina / Lucernario Astronómico Cenital (Cenit de la sala central)
    dxf.add_rect(2500.0, 5500.0, 3000.0, 2000.0, layer="LUCERNARIO_CENITAL")
    dxf.add_text("LUCERNARIO ASTRONOMICO CENITAL (3.0x2.0m)", 2600.0, 6300.0, height=120.0, layer="LUCERNARIO_CENITAL")
    dxf.add_text("EJE ALINEADO NORTE-SUR CELESTE", 2800.0, 5800.0, height=100.0, layer="LUCERNARIO_CENITAL")
    
    # Patios y Balcones (Zona Este)
    dxf.add_rect(7000.0, 200.0, 2800.0, 9600.0, layer="TABIQUES")
    dxf.add_text("PATIO JARDIN / TERRAZA BIOCLIMATICA", 7200.0, 5000.0, height=140.0, layer="ZONIFICACION")
    
    # Trazado de Ductos Segregados (Trinchera técnica desde Sala IT hacia estancias)
    # Canalización de Potencia (Amarillo)
    dxf.add_line(1500.0, 2500.0, 1500.0, 8000.0, layer="DUCTOS_FUERZA")
    dxf.add_line(1500.0, 8000.0, 6500.0, 8000.0, layer="DUCTOS_FUERZA")
    dxf.add_text("TRINCHERA DUCTO POTENCIA (PVC 1-1/4\")", 1600.0, 4000.0, height=90.0, layer="DUCTOS_FUERZA")
    
    # Canalización de Datos / Telecomunicaciones (Rojo, separada 350 mm)
    dxf.add_line(1850.0, 2500.0, 1850.0, 8350.0, layer="DUCTOS_DATOS")
    dxf.add_line(1850.0, 8350.0, 6500.0, 8350.0, layer="DUCTOS_DATOS")
    dxf.add_text("DUCTO DATOS CAT6A (SEPARACION 350mm)", 1950.0, 4500.0, height=90.0, layer="DUCTOS_DATOS")
    
    dxf.save()

if __name__ == "__main__":
    c_out = "/home/ral/Documents/GitHub/open-source-domotics/00_diseno_arquitectonico_y_estructural/01_mecanica_suelos_y_cimentacion/planos_y_calculos/plano_cimentacion_ejes.dxf"
    a_out = "/home/ral/Documents/GitHub/open-source-domotics/00_diseno_arquitectonico_y_estructural/03_arquitectura_habitaciones_patios_terrazas/planos_2d_dxf/planta_arquitectonica_base.dxf"
    build_foundation_dxf(c_out)
    build_architectural_dxf(a_out)
