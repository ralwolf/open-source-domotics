# Virtualización y Núcleo de Software (Proxmox, HA, Frigate, TrueNAS)

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Chasis de servidor en rack (1U/2U) o Mini PC / servidor torre con bahías para discos intercambiables.
- Disipadores pasivos/activos de cobre y ventiladores PWM silenciosos.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Fuente de alimentación certificada 80 Plus Gold/Platinum con PFC activo.
- Acelerador de IA Google Coral TPU (interfaz USB o M.2 PCIe).
- Adaptador/Coordinador Zigbee 3.0 / Matter USB de alta ganancia con cable de extensión apantallado.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Proxmox VE como hipervisor base con clustering y snapshots automáticos.
- VM Home Assistant OS con passthrough del coordinador Zigbee y broker Mosquitto.
- LXC/VM Frigate NVR con aceleración Coral TPU y streams RTSP directos.
- VM TrueNAS CORE/SCALE con pool ZFS en espejo para almacenamiento de grabaciones y backups.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
