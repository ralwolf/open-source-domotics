# Canalizaciones, Ductos Eléctricos y Cableado Estructurado bajo Normas Técnicas

## 1. Alcance Técnico
Diseño y trazado de los sistemas de conducción de cableado (conduit, bandejas portacables y registros) bajo estrictas normas internacionales y locales (NEC / NFPA 70, REBT, NOM-001-SEDE, TIA-568/569).

## 2. Segregación y Separación de Señales (Anti-Interferencias)
- **Separación Obligatoria de Tuberías:**
  - **Canalización A (Corrientes Fuertes / Potencia):** Circuitos de 230V / 110V AC para fuerza, electrodomésticos, motores e inversores. Tubería conduit metálica galvanizada (EMT/RMC) o PVC pesado antillama.
  - **Canalización B (Corrientes Débiles / Telecomunicaciones / Control):** Cables de datos UTP/FTP Cat6A/Cat7, alimentación PoE a 48V, buses domóticos RS485/Modbus, cableado de altavoces y sensores de alarma.
- **Distancia de Separación Normativa:**
  - Mínimo 20 cm a 30 cm de separación en recorridos paralelos.
  - Cruces perpendiculares a 90° para anular acoplamientos inductivos y ruido electromagnético.

## 3. Criterios de Capacidad, Registros y Trazado
- **Factor de Ocupación de Ductos:** Máximo 40% de la sección transversal ocupada por conductores para permitir disipación térmica y futuras ampliaciones (norma NEC).
- **Cajas de Registro y Paso:**
  - Instalación de cajas de derivación accesibles cada 15 metros de tirada recta o tras un máximo de 3 curvas de 90° (270° totales).
  - Radios de curvatura mínimos para cables UTP y fibra óptica (mínimo 4 a 8 veces el diámetro exterior del cable para evitar atenuación).
- **Identificación y Código de Colores:**
  - Marcaje unificado en borneros y conductores en ambos extremos con etiquetas termoencogibles numeradas según plano unifilar.

## 4. Contenido y Entregables del Directorio
- **`trazado_canalizaciones/`**:
  - [`plano_canalizaciones_segregadas.dxf`](trazado_canalizaciones/plano_canalizaciones_segregadas.dxf): Plano CAD 2D completo de la vivienda ($10 \times 10\text{ m}$) con segregación física de rutas de Fuerza AC 230V (PVC Cédula 40 1" / EMT), Red de Datos UTP Cat6A / PoE ($\ge 30\text{ cm}$ en corrugado LSZH 25mm), Bus de Sensores / Modbus RS-485 apantallado (20mm), cruces perpendiculares a 90° y ubicación de cajas de registro normalizadas CR-01 a CR-06.
  - [`plano_canalizaciones_segregadas.svg`](trazado_canalizaciones/plano_canalizaciones_segregadas.svg): Render vectorial con código de colores normalizado y tabla de compatibilidad electromagnética.
- **`NOTA_DE_DISENO.md`**: Ficha técnica y criterios de ocupación máxima (<40%), radio de curvatura ($R \ge 6 \times D$) y tendido según ANSI/TIA-569-E y REBT ITC-BT-21.
- **`normativas_y_calculos/`**: Criterios de compatibilidad electromagnética (EMC) y cálculo de atenuación en Cat6A.

