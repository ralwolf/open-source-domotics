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
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
