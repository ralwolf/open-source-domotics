# Canalizaciones, Ductos Eléctricos y Trazados Segregados

## 1. Descripción y Alcance
Este subsistema define los recorridos físicos de los servicios de la vivienda (baja tensión, comunicaciones de datos, domótica, fontanería, climatización y gas), garantizando el cumplimiento estricto de la normativa de compatibilidad electromagnética (EMC, UNE-EN 50174) e instalaciones interiores (ITC-BT-21 del REBT y CTE DB-HS).

---

## 2. Entregables Mecánicos y Modelado 3D (`mecanico/`)
- [`patinillo_instalaciones_conduits.FCStd`](./mecanico/patinillo_instalaciones_conduits.FCStd): Modelo paramétrico 3D nativo en FreeCAD 1.1+ del patinillo técnico vertical central (1200 x 400 x 3200 mm), muros y puerta de registro cortafuegos EI-60, bandejas Rejiband perforadas separadas >300 mm (Potencia BT vs. Telecomunicaciones Cat6A/Fibra), bajante insonorizada DN110, tuberías PE-Xa con coquilla elastomérica, conducto de gas ventilado y sellados pasantes intumescentes.
- [`patinillo_instalaciones_conduits.step`](./mecanico/patinillo_instalaciones_conduits.step): Archivo neutro STEP AP214 para análisis de interferencias (clash detection BIM).

---

## 3. Planos 2D de Canalizaciones (`trazado_canalizaciones/`)
- [`plano_canalizaciones_segregadas.dxf`](./trazado_canalizaciones/plano_canalizaciones_segregadas.dxf): Plano CAD 2D de planta con la segregación cromática de canalizaciones en suelos técnicos y techos registrables.
- [`plano_canalizaciones_segregadas.svg`](./trazado_canalizaciones/plano_canalizaciones_segregadas.svg): Vista vectorial interactiva del trazado de tubos corrugados y bandejas.

---

## 4. Memorias y Normativa (`normativas_y_calculos/`)
- [`NOTA_DE_DISENO.md`](./NOTA_DE_DISENO.md): Justificación técnica de distancias mínimas de aislamiento galvánico contra interferencias inducidas, radios mínimos de curvatura para cableado Cat6A/fibra óptica y cálculo de sección útil de tubos (ocupación máxima del 40%).
