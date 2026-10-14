# Índice de Notas de Diseño y Memorias de Ingeniería (open-source-domotics)

Este directorio reúne las **Notas de Diseño Técnico (NDT)** y memorias de cálculo para cada subsistema del proyecto, permitiendo la transición directa de especificaciones conceptuales a modelos de fabricación y planos en software libre (*FreeCAD, LibreCAD, QElectroTech, KiCad, Arduino CLI*).

---

## 📑 Índice de Notas de Diseño por Dominio Técnico

| Código | Documento de Diseño | Dominio Técnico | Herramientas FOSS Asociadas | Estado |
| :--- | :--- | :--- | :--- | :--- |
| **NDT-01** | [01_geotecnia_cimentacion_y_estructuras.md](01_geotecnia_cimentacion_y_estructuras.md) | Geotecnia, Zapatas, Pilares y Sobrecargas en Cubierta | *LibreCAD, FreeCAD (FEM Module)* | **Vigente** |
| **NDT-02** | [02_bioclimatica_ventilacion_y_lucernario.md](02_bioclimatica_ventilacion_y_lucernario.md) | Bioclimática, Ventilación Pasiva y Cúpula Astronómica | *FreeCAD, Blender, SunCalc* | **Vigente** |
| **NDT-03** | [03_canalizaciones_normadas_y_redes_fluidos.md](03_canalizaciones_normadas_y_redes_fluidos.md) | Red de Gas Dual, Hidráulica y Segregación Eléctrica | *QElectroTech, LibreCAD* | **Vigente** |
| **NDT-04** | [04_balance_cargas_y_dimensionamiento_energetico.md](04_balance_cargas_y_dimensionamiento_energetico.md) | Matriz Energética, Baterías LiFePO4, Solar y Eólica | *KiCad, QElectroTech, Python Scipy* | **Vigente** |
| **NDT-05** | [05_infraestructura_it_red_vlans_y_seguridad.md](05_infraestructura_it_red_vlans_y_seguridad.md) | Topología Red, VLANs, Cámaras PoE e Intercom SIP | *Draw.io/Dia, Proxmox VE, Asterisk* | **Vigente** |

---

## 🛠️ Estándar Metodológico para cada Nota de Diseño

Cada documento sigue el siguiente estándar de ingeniería:
1. **Objetivo y Criterios Base:** Parámetros de partida, normativas técnicas aplicables y factores de seguridad ($FS$).
2. **Formulación Matemática y Memorias de Cálculo:** Ecuaciones gobernantes, balance de masas/energía y hojas de dimensionamiento.
3. **Especificación de Materiales y Tolerancias:** Fichas de componentes, aleaciones, calibres, presiones y tensiones nominales.
4. **Guía de Modelado FOSS:** Flujo de diseño para representar la solución en las herramientas de software libre seleccionadas.
5. **Puntos de Integración e Interfaces:** Cruce con otros módulos (ej. anclajes mecánicos con red eléctrica, sensores con buses de datos).
