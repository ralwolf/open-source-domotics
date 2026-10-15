# Sistema de Riego Inteligente y Automatizado de Jardín

## 1. Descripción y Alcance
Este subsistema gestiona el riego de precisión para las áreas verdes, jardineras y huerto doméstico. Utiliza datos agrometeorológicos locales combinados con balance hídrico (evapotranspiración $ET_0$), sensores capacitivos de humedad en suelo y caudalímetro de pulsos en línea para detección inmediata de fugas o roturas de tuberías.

---

## 2. Entregables Mecánicos y Modelado 3D (`mecanico/`)
- [`arqueta_riego_electrovalvulas_3d.FCStd`](./mecanico/arqueta_riego_electrovalvulas_3d.FCStd): Modelo paramétrico 3D nativo en FreeCAD 1.1+ de la arqueta enterrada estanca en polietileno de alta resistencia (Base 640 x 500 mm, Tapa 500 x 350 mm, Altura 300 mm), tapa verde texturizada con perno de seguridad, tubería de alimentación de 1", filtro de anillas de 120 mesh, electroválvula maestra de seguridad, caudalímetro digital de turbina y colector manifold de polipropileno con 4 electroválvulas solenoides de 24VAC (Hunter PGV / Rain Bird 100-DV).
- [`arqueta_riego_electrovalvulas_3d.step`](./mecanico/arqueta_riego_electrovalvulas_3d.step): Archivo STEP AP214 universal para replanteo topográfico y de zanjas en exteriores.
- [`esquema_hidraulico_riego.dxf`](./mecanico/esquema_hidraulico_riego.dxf): Plano CAD P&ID 2D con la sectorización hidráulica (Césped aspersión, Huerto goteo, Setos perimetrales y Macetas).
- [`esquema_hidraulico_riego.svg`](./mecanico/esquema_hidraulico_riego.svg): Esquema hidráulico interactivo vectorial.

---

## 3. Entregables Eléctricos y Electrónica (`electrico/`)
- [`controlador_riego_jardin.kicad_sch`](./electrico/controlador_riego_jardin.kicad_sch): Esquema electrónico profesional en KiCad 10 con ESP32-S3, 5x etapas de potencia con Triacs BT136 y optoacopladores de cruce por cero MOC3041 para activación silenciosa y sin arcos de solenoides a 24VAC, entrada de pulsos de caudalímetro y puerto RS485 para sondas de humedad de suelo Modbus.
- [`controlador_riego_jardin.kicad_pro`](./electrico/controlador_riego_jardin.kicad_pro): Proyecto en KiCad 10.
- [`esquema_svg/controlador_riego_jardin.svg`](./electrico/esquema_svg/controlador_riego_jardin.svg): Renderizado esquemático vectorial.
- [`BOM.md`](./electrico/BOM.md): Lista completa de materiales y componentes electrónicos.

---

## 4. Entregables de Control y Firmware (`control/`)
- [`riego_inteligente_jardin.yaml`](./control/riego_inteligente_jardin.yaml): Firmware para ESPHome con componente nativo `sprinkler` secuencial, enclavamiento por caudal (corte automático si se detecta flujo sin orden de riego activa, indicando rotura de tubería) y ajuste dinámico según predicción meteorológica local.
