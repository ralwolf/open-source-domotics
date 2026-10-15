# Instalaciones Hidráulicas, Sanitarias y Red Dual de Gas (Red de Comisión + Tanque Estacionario LP / Biogás)

Este subsistema comprende la ingeniería civil, mecánica y de fluidos para el abastecimiento, distribución y retorno de agua potable (AF), agua caliente sanitaria (ACS), evacuación de saneamiento y la red dual de gas combustible con alta redundancia, aislamiento y conmutación segura.

---

## 1. Alcance y Especificaciones Técnicas

### 1.1 Red Hidráulica y Sanitaria
- **Materiales de Tuberías:**
  - Tuberías de Polipropileno Copolímero Random (PPR termofusionado PN25) y Polietileno Reticulado (PEX-a) con barrera antioxígeno y aislamiento elastomérico de 13 mm ($\lambda = 0.038\text{ W/m}\cdot\text{K}$).
  - Dimensionado principal: Acometida DN25 (1"), distribución a colectores secundarios DN20 (3/4"), derivaciones terminales DN15 (1/2").
- **Circuito de Recirculación de ACS Solar:**
  - Anillo de retorno continuo con bomba circuladora ECM de 12V DC / 8W con control temporizado y por sensor de presencia/temperatura en baños.
  - Asegura agua a 50 °C en grifos terminales en menos de 3 segundos sin purga de agua fría residual.
- **Evacuación y Separación de Desagües:**
  - Desagüe primario de aguas negras (fecales) en PVC-U sanitario DN110 canalizado directamente a la cámara de biodigestión anaerobia (`01_energia_renovable_y_almacenamiento/03_biodigestor_biogas_generador/`).
  - Desagüe secundario de aguas grises (duchas, lavabos, lavadora) en PVC-U DN50/DN75 con trampa de grasas y decantador hacia el sistema de riego o filtración previa.

### 1.2 Red Dual de Gas y Conmutación Segura
- **Fuentes de Alimentación:**
  - **Línea A (Red de Comisión / Gas Natural):** Suministro canalizado a 20 mbar (baja presión).
  - **Línea B (Tanque Estacionario LP / Biogás Filtrado):** Suministro regulado a 28-37 mbar.
- **Colector de Conmutación y Seguridad:**
  - Colector de acero inoxidable AISI 316L / Cobre rígido Tipo L con válvulas de bola con bloqueo por candado (LOTO).
  - Electroválvulas de seguridad normalmente cerradas (NC) de 12V/24V con rearme manual, certificadas ATEX / EN 161.
  - Válvulas antirretorno (check) con muelle de acero inoxidable para evitar contaminación o reflujo cruzado entre redes de diferente presión.
  - Transductor de presión 4-20mA / I2C y manómetros analógicos glicerina (0-100 mbar / 0-4 bar según etapa).
  - Interbloqueo con sensores de gas metano/GLP y central de alarma de incendio y CO (`03_seguridad_y_control_acceso/07_seguridad_incendio_co_y_aerosoles/`).

---

## 2. Modelos 3D y Planos de Ingeniería

| Componente | Tipo | Enlaces de Descarga / Visualización | Descripción Técnica |
| :--- | :--- | :--- | :--- |
| **Colector de Fluidos y Conmutación** | Modelo CAD 3D | [colector_conmutacion_gas_y_fontaneria.FCStd](planos_fontaneria/colector_conmutacion_gas_y_fontaneria.FCStd)<br>[colector_conmutacion_gas_y_fontaneria.step](planos_fontaneria/colector_conmutacion_gas_y_fontaneria.step) | Ensamble 3D FreeCAD del colector de fluidos: bloque de corte AF/ACS, recirculación y conmutación de gas con electroválvulas. |
| **Esquema P&ID Fontanería AF/ACS/Retorno** | Plano Vectorial 2D | [plano_fontaneria_af_acs_retorno.svg](planos_fontaneria/plano_fontaneria_af_acs_retorno.svg)<br>[plano_fontaneria_af_acs_retorno.dxf](planos_fontaneria/plano_fontaneria_af_acs_retorno.dxf) | Diagrama de flujo hidráulico de agua fría, acumulador solar 300L, retorno forzado de ACS y colectores de distribución. |
| **Esquema P&ID Red Dual de Gas** | Plano Vectorial 2D | [plano_gas_dual_conmutacion.svg](planos_gas_dual/plano_gas_dual_conmutacion.svg)<br>[plano_gas_dual_conmutacion.dxf](planos_gas_dual/plano_gas_dual_conmutacion.dxf) | Diagrama de distribución de gas con doble acometida, válvulas check, reguladores de 1ª/2ª etapa y electroválvulas de corte. |

---

## 3. Scripts de Generación Paramétrica

Los modelos y esquemas fueron generados mediante scripts reproducibles de código abierto:
- `scripts/generar_colector_fluidos_3d.py`: Crea el sólido paramétrico 3D en FreeCAD 1.1+ y exporta en formato neutro STEP AP214.
- `scripts/generar_plano_fontaneria_gas.py`: Genera los planos isométricos y P&ID en DXF R12 y SVG vectorial nativo.

```bash
# Para regenerar modelos 3D y planos:
flatpak-spawn --host flatpak run --command=freecadcmd org.freecad.FreeCAD -c "exec(open('scripts/generar_colector_fluidos_3d.py').read())"
python3 scripts/generar_plano_fontaneria_gas.py
```
