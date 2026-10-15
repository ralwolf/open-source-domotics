# Automatización, Filtrado y Mantenimiento Químico de Piscina

Este subsistema implementa el control integral de la piscina residencial: bombeo y filtración con vidrio activo AFM, medición analítica aislada galvánicamente de pH y potencial de óxido-reducción (ORP/Redox), inyección química peristáltica proporcional e interbloqueo estricto de seguridad contra funcionamiento en seco y sobrequímica.

---

## 1. Arquitectura Hidráulica y de Control Químico

```
                           [ COLECTOR DE ASPIRACIÓN DN50 ]
                                  |            |
                             Skimmers (2x)   Sumidero
                                  \            /
                                   \          /
                                    v        v
                           +-------------------------+
                           |  BOMBA 1 CV (0.75 kW)   |
                           |  11 m³/h con Prefiltro  |
                           +------------+------------+
                                        | Impulsión PVC DN50
                                        v
                           +-------------------------+
                           |  VÁLVULA SELECTORA 6V   |
                           +------------+------------+
                                        |
                                        v
                           +-------------------------+
                           |   FILTRO ARENA D500     |
                           |   (Lecho Vidrio Activo) |
                           +------------+------------+
                                        |
             +--------------------------+--------------------------+
             | Salida Filtrada                                     |
             v                                                     v
    +-----------------+                                  +-------------------+
    | BYPASS ANÁLISIS |                                  | LÍNEA PRINCIPAL   |
    | - Sonda pH BNC  |                                  | - Flow-Switch M12 |
    | - Sonda ORP BNC |                                  | - Sonda Temp DS18 |
    +--------+--------+                                  +---------+---------+
             | Retorno Bypass                                      |
             +--------------------------+--------------------------+
                                        |
                                        v
                           +-------------------------+
                           | PUNTOS DE INYECCIÓN     |
                           | 1. Reductor pH- (Ácido) | <--- Peristáltica 1 (24V)
                           | 2. Cloro / Desinfect.   | <--- Peristáltica 2 (24V)
                           +------------+------------+
                                        |
                                        v
                           +-------------------------+
                           | INTERCAMBIADOR SOLAR    | <--- Primario Solar Térmico
                           | Titanio 40 kW           |
                           +------------+------------+
                                        |
                                        v
                         [ 3x BOQUILLAS DE IMPULSIÓN ]
```

### Reglas de Seguridad e Interbloqueo Físico
1. **Interbloqueo Químico por Flow-Switch:** Las bombas peristálticas de dosificación química están condicionadas física y lógicamente al sensor de flujo. Si el flujo se detiene ($Q = 0$), las dosificadoras se cortan de inmediato ($< 100\text{ ms}$) para impedir acumulaciones gaseosas peligrosas de cloro en la tubería.
2. **Protección contra Marcha en Seco:** Si tras 90 segundos de arrancar la bomba no se detecta señal de agua en el flow switch, la bomba se detiene automáticamente y se bloquea emitiendo alarma crítica.
3. **Optimización Solar Fotovoltaica:** La recirculación de 4.5 horas se programa automáticamente para coincidir con la curva de excedente solar fotovoltaico reportada por el inversor ESS en la VLAN 30 IoT.

---

## 2. Entregables y Modelos del Subsistema

### 2.1 Diseño Mecánico y Caseta Técnica 3D (`mecanico/`)
- **Modelo CAD FreeCAD 1.1+**: [caseta_tecnica_piscina_filtro.FCStd](mecanico/caseta_tecnica_piscina_filtro.FCStd)
- **Modelo de Intercambio STEP**: [caseta_tecnica_piscina_filtro.step](mecanico/caseta_tecnica_piscina_filtro.step)
- **Script Generador 3D**: [generar_piscina_3d.py](../../scripts/generar_piscina_3d.py)
- **Plano P&ID 2D CAD (DXF)**: [plano_hidraulico_piscina.dxf](mecanico/plano_hidraulico_piscina.dxf)
- **Plano Vectorial SVG**: [plano_hidraulico_piscina.svg](mecanico/plano_hidraulico_piscina.svg)
- **Script Generador P&ID**: [generar_plano_piscina.py](../../scripts/generar_plano_piscina.py)
- **Especificaciones**:
  - Caseta técnica en arqueta enterrada ventilada ($1.20 \times 0.90\text{ m}$).
  - Filtro laminado de poliéster $\varnothing 500\text{ mm}$ con válvula selectora de 6 posiciones.
  - Bomba autoaspirante $0.75\text{ kW}$ ($1\text{ CV}$, $11\text{ m}^3\text{/h}$) con prefiltro desmontable.
  - Vaso de bypass en acrílico transparente para electrodos de pH y ORP.
  - Dos bombas dosificadoras peristálticas compactas de $1.5\text{ L/h}$ a $24\text{VDC}$.

### 2.2 Diseño Eléctrico y Esquemático KiCad 10 (`electrico/`)
- **Proyecto KiCad 10**: [controlador_quimica_piscina.kicad_pro](electrico/controlador_quimica_piscina.kicad_pro)
- **Esquema Electrónico**: [controlador_quimica_piscina.kicad_sch](electrico/controlador_quimica_piscina.kicad_sch)
- **Vectorial SVG**: [controlador_quimica_piscina.svg](electrico/esquema_svg/controlador_quimica_piscina.svg)
- **Lista de Materiales y Costes (BOM)**: [BOM.md](electrico/BOM.md)
- **Script Generador KiCad**: [generar_kicad_piscina.py](../../scripts/generar_kicad_piscina.py)
- **Topología Aislada Galvánicamente**:
  - Convertidor DC-DC aislado B0505S ($1\text{ kV}$ aislamiento galvánico) para alimentar la etapa analógica.
  - Amplificadores operacionales de electroteca LMC6001 con corriente de polarización ultrabaja ($I_b < 25\text{ fA}$) para electrodos de vidrio con impedancias de gigaohmios.
  - Convertidor analógico-digital ADS1115 de 16 bits conectado por bus I2C.
  - Driver de potencia MOSFET AOD4184A con diodos flyback 1N5408 para conmutación de bombas peristálticas.
  - Relé Omron de 16A para maniobra segura de la bobina del contactor de la bomba principal de 230VAC.

### 2.3 Firmware y Automatización ESPHome (`control/`)
- **Firmware ESPHome**: [control_piscina_automatizada.yaml](control/control_piscina_automatizada.yaml)
- **Lógica Integrada**:
  - Curva de calibración Nernst de 2 puntos para electrodo de pH.
  - Medición directa de potencial Redox en milivoltios (rango $0\text{ a }1000\text{ mV}$).
  - Sonda digital DS18B20 para compensación de temperatura del agua.
  - Sensor de nivel en skimmer con accionamiento de electroválvula de llenado automático.
  - Regulación proporcional con descansos de mezcla de 15 minutos para evitar sobredosificación química.
  - Exposición de servicios seguros en Home Assistant para forzar ciclos de filtrado o choque químico.
