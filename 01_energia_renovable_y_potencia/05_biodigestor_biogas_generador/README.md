# Biodigestor Séptico, Purificación de Biogás y Generación Eléctrica

## 1. Descripción y Alcance
Este directorio contiene la documentación, especificaciones, esquemas y archivos de diseño tanto mecánicos como eléctricos para este componente.

---

## 2. Requerimientos de Diseño Mecánico (`mecanico/`)
- Tanque biodigestor anaeróbico modificado para tratamiento de efluentes y lodos orgánicos con cierre hermético.
- Campana o gasómetro de acumulación de baja presión con membrana flexible o sello hidráulico.
- Trampa de condensado y purga de agua en el punto más bajo de la línea de gas.
- Filtro desulfurador de sulfuro de hidrógeno (H2S) con viruta de hierro o carbón activado.
- Columna o trampa de enriquecimiento de metano (separación de CO2).
- Válvula de alivio de presión mecánica calibrada y arrestador de flama (parallamas certificado).

---

## 3. Requerimientos de Diseño Eléctrico y Protecciones (`electrico/`)
- Motogenerador adaptable a biogás (carburador dual gas/nafta con gobernador de velocidad).
- Electroválvula de corte de biogás normalmente cerrada con certificación ATEX.
- Sensor industrial de presión diferencial piezoeléctrico en línea de gas.

---

## 4. Requerimientos de Control y Automatización (`control/`)
- Detectores de gas metano (CH4) instalados en la caseta técnica con interlock de corte físico.
- Monitoreo de presión de gasómetro y producción volumétrica estimada en Home Assistant.

---

## 5. Estructura y Entregables de este Directorio
- **`mecanico/`**:
  - [`biodigestor_biogas_sistema.FCStd`](mecanico/biodigestor_biogas_sistema.FCStd): Modelo 3D FreeCAD del reactor biodigestor cilíndrico-cónico (1500 L), trampa de condensado con purga sifónica, columna desulfuradora Fe2O3, arrestador de flama (parallamas ATEX AISI 316) y motogenerador dual.
  - [`biodigestor_biogas_sistema.step`](mecanico/biodigestor_biogas_sistema.step): Exportación neutra STEP para fabricación y montaje.
  - [`esquema_biogas_generador.dxf`](mecanico/esquema_biogas_generador.dxf): Plano CAD P&ID con entrada de aguas negras/lodos, salida de biol fertilizante, línea de biogás, desulfuración (<10 ppm H2S), pulmón gasómetro (20 mbar), válvula ATEX, generador dual 5 kW y transferencia ATS.
  - [`esquema_biogas_generador.svg`](mecanico/esquema_biogas_generador.svg): Diagrama vectorial del flujo de biogás y generación eléctrica.
- **`electrico/`**:
  - [`controlador_biogas_generador.kicad_pro`](electrico/controlador_biogas_generador.kicad_pro): Proyecto electrónico KiCad 10.
  - [`controlador_biogas_generador.kicad_sch`](electrico/controlador_biogas_generador.kicad_sch): Esquema electrónico KiCad 10 con ESP32, entrada 4-20mA para sensor de presión 0-50 mbar, detector MQ-4 de metano, transformador ZMPT101B de supervisión 230VAC del generador y relés de maniobra (Ignición, Arranque motor, Choke y Válvula ATEX).
  - [`controlador_biogas_generador.svg`](electrico/esquema_svg/controlador_biogas_generador.svg): Esquema renderizado mediante kicad-cli.
  - [`BOM.md`](electrico/BOM.md): Lista detallada de componentes y aparamenta.
- **`control/`**:
  - [`monitoreo_biogas_generador.yaml`](control/monitoreo_biogas_generador.yaml): Firmware ESPHome con telemetría de presión de gasómetro, secuencia automatizada de arranque del motor (Ignición -> Choke -> Starter -> Verificación AC -> ATS), corte de seguridad por fuga de metano y encendido automático de contingencia si el SoC de baterías LiFePO4 cae de 18%.

