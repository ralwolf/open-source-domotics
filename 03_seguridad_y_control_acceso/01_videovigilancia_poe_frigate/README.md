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

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
