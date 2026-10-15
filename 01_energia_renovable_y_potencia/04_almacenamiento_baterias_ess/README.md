# Almacenamiento de Energía en Baterías para el Hogar (ESS)

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Gabinete metálico o rack de baterías ventilado con aislamiento ignífugo y bandejas de retención.
- Espaciadores de compresión para celdas prismáticas LiFePO4.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Banco de celdas LiFePO4 (48V nominal, 16S) con barras colectoras de cobre estañado (busbars).
- BMS inteligente (Battery Management System) de 150A-200A con balanceador activo.
- Desconectador manual de corte en carga de trabajo pesado (Heavy-duty DC Disconnect switch).
- Fusible general clase T o ANL de 200A en borne positivo principal.
- Cableado de potencia de alta flexibilidad (35 mm² o 50 mm²).

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Comunicación digital BMS mediante puerto CAN / RS485 hacia inversor y pasarela Home Assistant.
- Monitoreo continuo de SoC (%), SoH, voltajes individuales por celda y sensores de temperatura térmicos.

---

## 5. Estructura de este Directorio
- `mecanico/`:
  - [`gabinete_baterias_lifepo4_16s.FCStd`](./mecanico/gabinete_baterias_lifepo4_16s.FCStd): Modelo paramétrico 3D en FreeCAD 1.1+ del banco LiFePO4 16S (14.3 kWh) con celdas prismáticas EVE LF280K, placas de compresión de 8 mm con varillas M8 (300 kgf), barras colectoras y fusible Clase T.
  - [`gabinete_baterias_lifepo4_16s.step`](./mecanico/gabinete_baterias_lifepo4_16s.step): Exportación universal STEP AP214 para fabricación y montaje en rack.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`:
  - [`bms_lifepo4_monitor.yaml`](./control/bms_lifepo4_monitor.yaml): Firmware ESPHome para monitorización del Smart BMS JK / Daly con balanceador activo 2A, lecturas de las 16 celdas individuales, $\Delta V$, temperatura NTC y SoC %.
- [`NOTA_DE_DISENO.md`](./NOTA_DE_DISENO.md): Memoria de cálculo de capacidad útil (14.3 kWh al 90% DoD), corrientes máximas (200A) y dimensionamiento de cables 50 mm².
