# Almacenamiento de Energía en Baterías para el Hogar (ESS)

## 1. Descripción y Alcance
Este subsistema proporciona respaldo eléctrico ininterrumpido (almacenamiento ESS de 14.3 kWh) y optimización de autoconsumo solar mediante un banco de 16 celdas prismáticas LiFePO4 EVE LF280K conectadas en serie (51.2V nominal, 280Ah). Incorpora placas de compresión mecánica constante calibradas a 300 kgf con muelles Belleville, pletinas de cobre flexibles, BMS inteligente con equilibrado activo de 2A, shunt de alta precisión y fusible de acción ultra-rápida Class T de 200A.

---

## 2. Entregables Mecánicos y Modelado 3D (`mecanico/`)
- [`gabinete_baterias_lifepo4_16s.FCStd`](./mecanico/gabinete_baterias_lifepo4_16s.FCStd): Modelo paramétrico 3D en FreeCAD 1.1+ del banco LiFePO4 16S (14.3 kWh) con celdas prismáticas EVE LF280K, placas de compresión de 8 mm con varillas roscadas M8, aislantes epoxi FR4, barras colectoras de cobre niqueladas y portafusibles Clase T.
- [`gabinete_baterias_lifepo4_16s.step`](./mecanico/gabinete_baterias_lifepo4_16s.step): Exportación universal STEP AP214 para fabricación y montaje en rack.
- [`plano_banco_baterias_lifepo4.dxf`](./mecanico/plano_banco_baterias_lifepo4.dxf): Plano CAD 2D de distribución mecánica, bornes, cableado de potencia y shunt.
- [`plano_banco_baterias_lifepo4.svg`](./mecanico/plano_banco_baterias_lifepo4.svg): Esquema interactivo vectorial del banco de baterías.

---

## 3. Entregables de Control y Automatización (`control/`)
- [`bms_lifepo4_monitor.yaml`](./control/bms_lifepo4_monitor.yaml): Firmware ESPHome para monitorización del Smart BMS JK / Daly con balanceador activo 2A, lecturas de las 16 celdas individuales, $\Delta V$, temperatura NTC y SoC %.
- [`NOTA_DE_DISENO.md`](./NOTA_DE_DISENO.md): Memoria de cálculo de capacidad útil (14.3 kWh al 90% DoD), corrientes máximas (200A) y dimensionamiento de cables 50 mm².
