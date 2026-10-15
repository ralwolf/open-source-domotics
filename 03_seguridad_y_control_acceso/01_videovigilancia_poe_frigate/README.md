# Cámaras PoE con Detección IA y Almacenamiento por Eventos

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Cámaras IP tipo torreta o bala con certificación IP67 e IK10 antivandálica.
- Cajas estancas de conexiones con prensacables para sellado de conectores RJ45.
- Tubos conduit metálicos para protección física del cableado perimetral.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Alimentación Power over Ethernet (PoE 802.3af/at) estándar a 48V.
- Inyectores o puertos de switch PoE con protección individual contra cortocircuito.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Configuración de Frigate NVR: detección de objetos en flujo substream en RAM; guardado a disco en mainstream solo al confirmar persona, auto o mascota.
- Automatización en Home Assistant: notificaciones instantáneas con snapshot y activación de luces exteriores de disuasión.

---

## 5. Estructura y Entregables de este Directorio
- **`mecanico/`**:
  - [`caja_montaje_camara_poe.FCStd`](mecanico/caja_montaje_camara_poe.FCStd): Modelo 3D FreeCAD de caja estanca IP67 de montaje mural para cámaras torreta/domo PoE con entrada roscada para conduit M20 y alojamiento para conector RJ45.
  - [`caja_montaje_camara_poe.step`](mecanico/caja_montaje_camara_poe.step): Exportación neutra STEP para mecanizado o inyección.
  - [`plano_cobertura_cctv_poe.dxf`](mecanico/plano_cobertura_cctv_poe.dxf): Plano CAD de distribución de 4 cámaras PoE perimetrales (CAM-01 a CAM-04), conos de visión (FOV 108°/89°), distancias DORI (EN 62676-4) y zonas IA.
  - [`plano_cobertura_cctv_poe.svg`](mecanico/plano_cobertura_cctv_poe.svg): Diagrama vectorial en alta resolución del mapa de cobertura y zonas de detección.
- **`control/`**:
  - [`config.yml`](control/config.yml): Configuración de producción para Frigate NVR con aceleración por hardware Google Coral Edge TPU (7ms/frame), servidor WebRTC go2rtc integrado para latencia <200ms, flujo dual (substream 640x360@5fps en RAM para inferencia y mainstream 4K/2K a TrueNAS NFS por eventos), y tópicos MQTT hacia Home Assistant.

