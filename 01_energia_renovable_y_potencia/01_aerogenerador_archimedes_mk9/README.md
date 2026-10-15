# Aerogenerador Helicoidal Archimedes Adaptable Wind Turbine MK9

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Rotor helicoidal tipo tornillo de Arquímedes MK9 (diámetro y paso optimizado para bajas velocidades de viento).
- Eje central con rodamientos sellados de baja fricción y brida de montaje mecanizada.
- Mástil o torre arriostrada con soporte antivibratorio y amortiguadores de torsión.
- Carenado o cono aerodinámico de protección contra intemperie.

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Generador síncrono de imanes permanentes (PMSG) trifásico AC.
- Puente rectificador de onda completa de diodos Schottky de baja pérdida.
- Controlador de carga MPPT eólico con entrada para freno electrónico (Dump Load).
- Banco de resistencias de frenado de disipación de calor para sobrevelocidad.
- Interruptor seccionador manual de corte y cableado apantallado hacia el banco de baterías.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Sensor óptico o inductivo de RPM de rotor.
- Medición de voltaje y corriente DC/AC integrada a Home Assistant (ESPHome / Modbus RS485).
- Automatización de parada segura por ráfagas superiores a velocidad crítica (>60 km/h).

---

## 5. Estructura de este Directorio
- `mecanico/`:
  - [`rotor_archimedes_mk9.FCStd`](./mecanico/rotor_archimedes_mk9.FCStd): Modelo paramétrico 3D en FreeCAD 1.1+ del rotor helicoidal de Arquímedes ($\varnothing 1.50\text{ m}$, longitud $1.20\text{ m}$, ojiva frontal aerodinámica y brida de 6 pernos M10).
  - [`rotor_archimedes_mk9.step`](./mecanico/rotor_archimedes_mk9.step): Exportación universal STEP AP214 del conjunto de rotor y eje.
- `electrico/`:
  - [`esquema_potencia_eolico.dxf`](./electrico/esquema_potencia_eolico.dxf): Plano CAD 2D del esquema unifilar de rectificación, MPPT y contactor de seguridad.
  - [`esquema_potencia_eolico.svg`](./electrico/esquema_potencia_eolico.svg): Diagrama vectorial interactivo de potencia con generador PMSG 48V, rectificador Schottky, controlador MPPT y disipador dump-load de 1.5 kW.
- `control/`:
  - [`controlador_freno_eolico.yaml`](./control/controlador_freno_eolico.yaml): Firmware ESPHome para tacómetro RPM de rotor, anemómetro de mástil, sensor INA226 y disparo autónomo del freno de emergencia por cortocircuito ante ráfagas > 18 m/s.
- [`NOTA_DE_DISENO.md`](./NOTA_DE_DISENO.md): Memoria de cálculo aerodinámico, empuje de viento ($1020\text{ N}$) y momento de vuelco en columna C-TURB.
