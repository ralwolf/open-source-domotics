# Control de Acceso Biométrico por Huella Dactilar

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Cerradura de embutir motorizada de alta seguridad multipunto o cerradura electromagnética.
- Carcasa metálica exterior con lector de huella dactilar capacitivo antivandálico IP65.
- Cilindro mecánico de llave física de alta seguridad para apertura manual de emergencia.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Fuente de poder de 12V DC con circuito de carga y batería de respaldo de plomo-gel de 7Ah.
- Pulsador de salida interior tipo contacto seco (No Touch / capacitivo).
- Relé de control de apertura conectado por bus seguro Wiegand / RS485 o placa ESP32 con ESPHome.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Registro y auditoría de accesos por usuario con fecha y hora en Home Assistant.
- Apertura remota cifrada y alertas automáticas por intentos de acceso no autorizados.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
