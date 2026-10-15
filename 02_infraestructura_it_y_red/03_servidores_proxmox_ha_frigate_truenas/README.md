# Virtualización y Núcleo de Software (Proxmox, HA, Frigate, TrueNAS)

## 1. Descripción y Alcance
Este subsistema constituye el cerebro computacional y de almacenamiento masivo local de la domótica y seguridad. Todo el ecosistema opera 100% on-premises sin requerir servicios en la nube de terceros, garantizando privacidad absoluta mediante virtualización tipo 1 (bare-metal KVM con Proxmox VE), contenedores LXC de alto rendimiento, aceleración de redes neuronales con Google Coral Edge TPU para Frigate NVR, y almacenamiento ZFS redundante con TrueNAS.

---

## 2. Entregables Mecánicos y Modelado 3D (`mecanico/`)
- [`servidor_rack_1u_computo.FCStd`](./mecanico/servidor_rack_1u_computo.FCStd): Modelo paramétrico 3D nativo en FreeCAD 1.1+ del chasis de servidor 19" 1U (482.6 x 450 x 43.6 mm), chapa SPCC 1.2 mm, orejetas normalizadas EIA-310, 4 bahías hot-swap para discos SSD de 2.5", ranura de expansión PCIe de media altura para acelerador Coral TPU y fuentes redundantes Flex-ATX.
- [`servidor_rack_1u_computo.step`](./mecanico/servidor_rack_1u_computo.step): Archivo STEP AP214 universal para integración en el armario rack del centro de datos.

---

## 3. Entregables de Arquitectura y Topología de Servicios (`control/`)
- [`arquitectura_servidores_servicios.dxf`](./control/arquitectura_servidores_servicios.dxf): Plano CAD 2D de la arquitectura de capas lógicas, asignación de núcleos de CPU, memoria RAM ECC y segmentación de interfaces de red por VLAN.
- [`arquitectura_servidores_servicios.svg`](./control/arquitectura_servidores_servicios.svg): Diagrama vectorial interactivo del ecosistema de software y servicios virtualizados.
- [`docker-compose.yml`](./control/docker-compose.yml): Manifiesto unificado para despliegue de Home Assistant Core, Mosquitto MQTT, Frigate NVR (aceleración Coral Edge TPU), servidor de streaming go2rtc WebRTC y Zigbee2MQTT.
