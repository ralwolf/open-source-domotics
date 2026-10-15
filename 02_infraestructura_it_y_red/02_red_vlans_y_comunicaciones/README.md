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
- `mecanico/`:
  - [`patch_panel_24p_1u.FCStd`](./mecanico/patch_panel_24p_1u.FCStd): Modelo CAD 3D paramétrico nativo en FreeCAD 1.1+ del patch panel modular de 24 puertos Keystone 1U (EIA-310-D) con bandeja de retención trasera de cableado y perno M5 de tierra.
  - [`patch_panel_24p_1u.step`](./mecanico/patch_panel_24p_1u.step): Exportación universal STEP AP214 para montaje e interoperabilidad en el rack de 15U.
  - [`plano_patch_panel_red_1u.dxf`](./mecanico/plano_patch_panel_red_1u.dxf): Plano CAD 2D de alzado frontal, planta y detalle de colisas de anclaje según norma DIN 41494.
  - [`plano_patch_panel_red_1u.svg`](./mecanico/plano_patch_panel_red_1u.svg): Vista vectorial técnica interactiva con asignación de puertos, codificación de color por VLAN y criterios de curvatura y EMC.
- `electrico/`:
  - [`topologia_red_vlans.dxf`](./electrico/topologia_red_vlans.dxf): Plano CAD 2D normalizado de la arquitectura de red y enlaces LACP/Trunk 802.1Q.
  - [`topologia_red_vlans.svg`](./electrico/topologia_red_vlans.svg): Diagrama vectorial interactivo de las 5 VLANs segregadas con direcciones IP, puertos y políticas Zero-Trust.
- `control/`:
  - [`opnsense_vlans_firewall.json`](./control/opnsense_vlans_firewall.json): Archivo de configuración estructurado para OPNsense con interfaces LACP, subredes DHCP y reglas de aislamiento para IoT y CCTV.
- [`NOTA_DE_DISENO.md`](./NOTA_DE_DISENO.md): Memoria de cálculo y criterios normados de segmentación de tráfico y ciberseguridad.
