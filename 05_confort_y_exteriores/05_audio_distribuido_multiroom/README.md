# Sistema de Audio Distribuido Multiroom de Alta Fidelidad

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Altavoces pasivos empotrados en falso techo con rejillas magnéticas extraplanas y tratamiento antihumedad en cocina y baños.
- Altavoces de intemperie con soporte direccionable y certificación IP65 en terraza y zona de piscina.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Amplificadores digitales multicanal Clase D (eficiencia > 90%) centralizados en el rack o streamers zonales compactos.
- Cableado de audio de cobre libre de oxígeno (OFC) de 2x1.5 mm² apantallado en canalizaciones independientes.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Plataforma de audio de código abierto Music Assistant ejecutada en Home Assistant:
- - Compatibilidad nativa con Snapcast, AirPlay 2, Spotify Connect y DLNA/UPnP.
- - Agrupación de zonas en tiempo real (modo fiesta: música idéntica sincronizada en toda la casa, o listas independientes por habitación).
- - Integración con avisos por voz y campanadas de videoportero con atenuación automática de la música (*audio ducking*).

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D (FreeCAD / Open CAD Studio), modelos STL/STEP, tolerancias y anclajes.
- `electrico/`: Diagramas unifilares y esquemas de conexionado (QElectroTech / KiCad), protecciones y lista de materiales (BOM).
- `control/`: Configuraciones YAML de Home Assistant, firmware (ESPHome / Arduino CLI), integraciones locales.
