# Monitorización y Protección de Cargas en Lavandería

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Bases de enchufe estancas contra humedad (IP44/IP55).
- Soportes antivibratorios bajo lavadora y secadora.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Circuito independiente C20 con cable de 4 mm².
- Protector contra sobretensiones y picos transitorios de grado industrial (SPD Tipo 3) instalado en la toma de lavadora y secadora.
- Sensor de corriente o enchufe inteligente de alta carga (16A continuo).

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Detección de fin de ciclo de lavado y secado enviando aviso sonoro y push al móvil.
- Corte automático de energía si el sensor de inundación inferior detecta fuga de agua en la manguera de llenado.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D, modelos STL/STEP, especificaciones de corte, perfiles, anclajes y tolerancias mecánicas.
- `electrico/`: Diagramas unifilares y multifilares, esquemas de borneros, selección de disyuntores, calibres de cableado y listas de componentes (BOM).
- `control/`: Archivos de configuración (YAML de Home Assistant, configuraciones de ESPHome, tópicos MQTT, plantillas de automatización).
