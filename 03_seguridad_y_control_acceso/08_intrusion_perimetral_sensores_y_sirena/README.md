# Sistema de Intrusión Perimetral, Sensores Magnéticos, Rotura de Cristal y Sirena

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Sensores magnéticos de contacto reed ultrafinos ocultos en el perfil de puertas y ventanas exteriores.
- Carcasa de sirena exterior de alta resistencia con protección antidesprendimiento y grado IP65.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Lazo cableado de seguridad o sensores inalámbricos Zigbee 3.0 de ultra bajo consumo en todos los accesos perimetrales.
- Detectores acústicos piezoeléctricos calibrados para la frecuencia de rotura de cristales en salón, terraza y en la vitrina astronómica del techo.
- Sirena estroboscópica exterior cableada de 115 dB con luz destellante y batería interna de respaldo de plomo-gel/Li-ion.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Panel de control de alarma de intrusión virtual en Home Assistant (Alarmo):
- - Modo Fuera de Casa (Armado Total): activa todos los sensores de puerta, ventana, rotura de cristal y cámaras Frigate.
- - Modo Noche (Armado Perimetral): vigila accesos exteriores y ventanales mientras los habitantes duermen, permitiendo libre movimiento interior sin falsos disparos.
- - Disparo de iluminación disuasiva exterior en rojo/blanco intermitente ante intento de intrusión.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D (FreeCAD / Open CAD Studio), modelos STL/STEP, tolerancias y anclajes.
- `electrico/`: Diagramas unifilares y esquemas de conexionado (QElectroTech / KiCad), protecciones y lista de materiales (BOM).
- `control/`: Configuraciones YAML de Home Assistant, firmware (ESPHome / Arduino CLI), integraciones locales.
