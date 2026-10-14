# Ventilación Mecánica Controlada (VMC) de Doble Flujo con Recuperador de Calor

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Unidad de ventilación mecánica con intercambiador entálpico de flujos cruzados suspendida en falso techo técnico con silenciadores acústicos en impulsión y retorno.
- Red de conductos termoplásticos semirrígidos antibacterianos y antiestáticos hacia cada estancia.
- Bypass automático de verano (Free-Cooling) para refrescamiento nocturno pasivo.
- Filtros de aire de alta eficiencia F7 (polen/partículas) y filtro HEPA en la admisión de aire exterior.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Ventiladores centrífugos con motores de conmutación electrónica EC de velocidad variable y muy bajo consumo (< 35W continuo).
- Servomotor de 24V para accionamiento de la compuerta de bypass de verano.
- Alimentación exclusiva C10 protegida con magnetotérmico.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Sensores ambientales de calidad de aire interior (CO2, PM2.5, humedad y compuestos orgánicos volátiles TVOC) en recámaras y sala.
- Lógica en Home Assistant: modulación del caudal de renovación en 3 velocidades según la concentración de CO2 interior (evitando ambientes viciados sin perder calor ni frío).
- Modo Free-Cooling: si la temperatura exterior nocturna en verano es inferior a la interior, la VMC conmuta a bypass para refrescar la casa sin encender el aire acondicionado.

---

## 5. Estructura de este Directorio
- `mecanico/`: Planos CAD 2D/3D (FreeCAD / Open CAD Studio), modelos STL/STEP, tolerancias y anclajes.
- `electrico/`: Diagramas unifilares y esquemas de conexionado (QElectroTech / KiCad), protecciones y lista de materiales (BOM).
- `control/`: Configuraciones YAML de Home Assistant, firmware (ESPHome / Arduino CLI), integraciones locales.
