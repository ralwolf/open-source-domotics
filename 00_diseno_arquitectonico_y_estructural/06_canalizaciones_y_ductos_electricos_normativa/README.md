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

## 4. Contenido del Directorio
- `trazado_canalizaciones/`: Planos de tendido de tuberías por techos, pisos y muros, ubicación de cajas de registro, cuadros secundarios y pasamuros cortafuegos.
- `normativas_y_calculos/`: Tablas de cálculo de sección de tuberías conduit según número y calibre de cables, y tabla de compatibilidad electromagnética.
