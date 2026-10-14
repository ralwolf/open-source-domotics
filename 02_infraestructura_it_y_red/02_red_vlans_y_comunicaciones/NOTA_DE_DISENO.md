# Ficha Técnica y Nota de Cálculo: Red de Comunicaciones y VLANs

## 1. Equipamiento de Red Central (Rack IT)
- **Router / Firewall:** Minipc x86 Intel N100 / Celeron 4x 2.5GbE i226-V corriendo OPNsense o OpenWrt con reglas de filtrado entre VLANs.
- **Switch Principal:** Switch gestionado L2+ de 24 puertos Gigabit RJ45 con PoE+ 802.3at ($370\text{ W}$ de presupuesto PoE total) y 4 puertos SFP+ de 10Gbps para enlace ascendente hacia Proxmox y TrueNAS.
- **Cableado Estructurado:** Bobina Cat6A F/UTP apantallada de cobre 100% (23 AWG) con terminación en patch panel Cat6A con descarga a tierra.

## 2. Parámetros de Calidad de Servicio (QoS) y Seguridad
- Tráfico SIP/VoIP etiquetado con DSCP Expedited Forwarding (EF - valor decimal 46).
- Control de tormentas de difusión (*Broadcast Storm Control*) activado en todas las bocas de acceso.
- Aislamiento estricto de la VLAN 30 (cámaras IP de Frigate) sin puerta de enlace hacia WAN pública.

*Para la memoria de cálculo completa, consulte [`docs/notas_de_diseno/05_infraestructura_it_red_vlans_y_seguridad.md`](../../docs/notas_de_diseno/05_infraestructura_it_red_vlans_y_seguridad.md).*

