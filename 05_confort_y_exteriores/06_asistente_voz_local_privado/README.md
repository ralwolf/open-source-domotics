# Asistente de Voz 100% Local, Privado y Seguro (Sin Nube)

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Carcasas empotradas en pared o módulos de techo impresos en 3D con difusores acústicos para satélites de voz.
- Bases de sobremesa compactas con ángulo de inclinación para captación frontal de voz.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Nodos satélite basados en microcontroladores ESP32-S3 (ESP32-S3-BOX o placas Atom Echo) con matriz de micrófonos duales I2S con cancelación de eco y altavoz de confirmación.
- Alimentación estándar PoE o USB-C a 5V DC.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Arquitectura de procesamiento de lenguaje natural completamente local en Home Assistant (Year of the Voice):
- - Motor de reconocimiento de voz (STT): Whisper ejecutándose en el servidor Proxmox VE sin enviar audio a internet.
- - Motor de síntesis de voz (TTS): Piper local para respuestas de voz realistas en español.
- - Activación por palabra clave local (Wake Word: ej. "Casa", "Jarvis") mediante openWakeWord.
- - Control por voz natural de iluminación, climatización, cortinas, puertas y consulta del estado de energía/baterías con privacidad absoluta.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D (FreeCAD / Open CAD Studio), modelos STL/STEP, tolerancias y anclajes.
- `electrico/`: Diagramas unifilares y esquemas de conexionado (QElectroTech / KiCad), protecciones y lista de materiales (BOM).
- `control/`: Configuraciones YAML de Home Assistant, firmware (ESPHome / Arduino CLI), integraciones locales.
