# Rack de Servidores Central y Sistema UPS

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Armario rack de 19 pulgadas (9U a 15U) para pared o suelo con puerta de cristal templado y cerradura.
- Bandejas fijas ventiladas, organizadores de cables horizontales y panel ciego para ventilación.
- Unidad de ventilación superior termorregulada.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- PDU (Power Distribution Unit) montable en rack de 8 tomas protegidas.
- UPS Online de doble conversión de 1500VA - 2000VA con salida de onda senoidal pura y factor de potencia 0.9+.
- Tarjeta de gestión de red SNMP o enlace USB para protocolo NUT.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Configuración de Network UPS Tools (NUT) para Home Assistant y TrueNAS.
- Monitoreo continuo de carga en W, voltaje de entrada/salida y porcentaje de batería restante.

---

## 5. Estructura de este Directorio
- `mecanico/`:
  - [`elevacion_rack_19u.dxf`](./mecanico/elevacion_rack_19u.dxf): Plano CAD 2D normalizado EIA-310-D del alzado frontal del Rack de 19" (15U).
  - [`elevacion_rack_19u.svg`](./mecanico/elevacion_rack_19u.svg): Vista vectorial interactiva de la distribución física de unidades (UPS, PDU, TrueNAS, Proxmox, Switch PoE+, OPNsense, Patch Panel y extractores).
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`:
  - [`upsmon.conf`](./control/upsmon.conf): Configuración del cliente NUT para monitorización y apagado escalonado limpio ante cortes de energía prolongados.
