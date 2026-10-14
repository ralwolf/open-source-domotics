# Infraestructura de Red, VLANs y Comunicaciones Seguras

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Patch panel Cat6A modular de 24 puertos en rack.
- Puntos de acceso Wi-Fi montados en techo con anclajes discretos.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Router dedicado multi-puerto (Hardware x86 para OpenWrt / OPNsense / pfSense).
- Switch PoE+ gestionado L2/L3 (802.3at/bt) de 16-24 puertos con presupuesto de potencia >150W.
- Cableado estructurado de cobre puro Cat6A / Cat7 con conectores blindados apantallados.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Configuración de VLAN 10 (Servidores), VLAN 20 (Cámaras PoE sin WAN), VLAN 30 (IoT), VLAN 40 (LAN principal), VLAN 50 (Invitados).
- Reglas estrictas de firewall y túnel VPN WireGuard para acceso remoto sin abrir puertos inseguros.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
