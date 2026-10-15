# Sistema Solar Fotovoltaico y Generación Distribuida

## 1. Descripción y Alcance
Este subsistema aborda la generación eléctrica renovable solar mediante módulos fotovoltaicos bifaciales de alta eficiencia (550 Wp monocristalinos), la estructura portante de cubierta inclinada a 30° con orientación sur, y la caja combinadora/protecciones DC con telemetría local autónoma para máxima resiliencia energética.

---

## 2. Entregables Mecánicos y Modelado 3D (`mecanico/`)
- [`estructura_montaje_coplanar_pv.FCStd`](./mecanico/estructura_montaje_coplanar_pv.FCStd): Modelo paramétrico 3D nativo en FreeCAD 1.1+ de la estructura triangular autoportante en perfil de aluminio estructural AL6005-T5, tornillería de acero inoxidable A2, mordazas centrales y finales, arriostramiento contra cargas de viento según CTE DB-SE-AE y dos módulos fotovoltaicos de 550W (2278 x 1134 x 35 mm).
- [`estructura_montaje_coplanar_pv.step`](./mecanico/estructura_montaje_coplanar_pv.step): Archivo de intercambio STEP AP214 para validación estructural en cubiertas y análisis de sombras (heliodon/shading).

---

## 3. Entregables Eléctricos y Electrónica (`electrico/`)
- [`esquema_fotovoltaico_ess.dxf`](./electrico/esquema_fotovoltaico_ess.dxf): Plano CAD unifilar 2D del campo solar, diodos de bloqueo, fusibles gPV de 1000V DC y topología de conexión hacia el inversor híbrido / sistema ESS.
- [`esquema_fotovoltaico_ess.svg`](./electrico/esquema_fotovoltaico_ess.svg): Esquema vectorial interactivo.
- [`combinador_telemetria_pv.kicad_sch`](./electrico/combinador_telemetria_pv.kicad_sch): Esquema electrónico profesional en KiCad 10 con ESP32-S3, sensor de corriente Hall aislado Allegro ACS758 (50A DC), divisor resistivo de alta tensión (hasta 600V DC), descargador de sobretensiones SPD DC Tipo II con contacto auxiliar optoacoplado y sensor térmico SHT31.
- [`combinador_telemetria_pv.kicad_pro`](./electrico/combinador_telemetria_pv.kicad_pro): Proyecto en KiCad 10.
- [`esquema_svg/combinador_telemetria_pv.svg`](./electrico/esquema_svg/combinador_telemetria_pv.svg): Renderizado esquemático vectorial.
- [`BOM.md`](./electrico/BOM.md): Lista completa de materiales y componentes fotovoltaicos y de instrumentación.

---

## 4. Entregables de Control y Firmware (`control/`)
- [`combinador_solar_pv.yaml`](./control/combinador_solar_pv.yaml): Firmware ESPHome para adquisición continua de tensión DC, amperaje y potencia instantánea producida (W), estimación de pérdidas por calentamiento de placas y alarma ante degradación de protectores SPD.
