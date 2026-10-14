# NDT-01: Geotecnia, Cimentaciones, Pilares y Sobrecargas en Cubierta

## 1. Criterios Base y Parámetros Geotécnicos

El diseño estructural garantiza la estabilidad global ante cargas gravitatorias estáticas, sobrecargas técnicas concentradas (banco de baterías, termosifones de inercia) y solicitaciones dinámicas severas (empuje aerodinámico y momentos de vuelco por el aerogenerador Archimedes MK9 en cubierta, ráfagas de viento y sismo).

### 1.1 Parámetros Geotécnicos de Referencia (Terreno Tipo II / Intermedio)
- **Profundidad de desplante ($D_f$):** $1.50\text{ m}$ respecto al nivel de terreno natural (NTN).
- **Número de golpes SPT ($N_{60}$):** $N \ge 22$ (estrato resistente de arenas limo-arcillosas compactas).
- **Ángulo de fricción interna ($\phi$):** $28^\circ$.
- **Cohesión efectiva ($c'$):** $12\text{ kPa}$ ($0.12\text{ kg/cm}^2$).
- **Peso unitario del suelo ($\gamma$):** $18.5\text{ kN/m}^3$.
- **Nivel Freático ($NF$):** Considerado a $-2.20\text{ m}$ en época de lluvias máximas (prevención de subpresión).

### 1.2 Capacidad de Carga Admisible (Ecuación de Terzaghi para Falla General)
$$q_{ult} = c \cdot N_c \cdot s_c + \gamma \cdot D_f \cdot N_q \cdot s_q + 0.5 \cdot \gamma \cdot B \cdot N_\gamma \cdot s_\gamma$$

Para $\phi = 28^\circ$, factores de capacidad: $N_c = 25.8$, $N_q = 14.7$, $N_\gamma = 11.2$.
Con factor de seguridad $FS = 3.0$:
$$\sigma_{adm} = \frac{q_{ult}}{FS} \approx 180\text{ kPa} \quad (1.83\text{ kg/cm}^2)$$

---

## 2. Espectro de Cargas y Sobrecargas Especiales

### 2.1 Cargas Concentradas en Cubierta (Azotea Técnica)
1. **Aerogenerador Archimedes MK9 + Mástil:**
   - Masa estática total: $105\text{ kg}$ ($45\text{ kg}$ turbina + $60\text{ kg}$ mástil y contravientos).
   - Altura de fijación sobre losa: $h = 3.50\text{ m}$.
   - Velocidad de viento de diseño: $v = 120\text{ km/h}$ ($33.3\text{ m/s}$, ráfaga de tormenta).
   - Diámetro del rotor: $D = 1.50\text{ m}$ (Área barrida $A = 1.77\text{ m}^2$).
   - Coeficiente de empuje axial ($C_T$ con freno de estacionamiento accionado): $C_T \approx 0.85$.
   - **Empuje lateral de viento sobre la turbina ($F_{empuje}$):**
     $$F_T = \frac{1}{2} \cdot \rho_{aire} \cdot A \cdot v^2 \cdot C_T = \frac{1}{2} \cdot 1.225 \cdot 1.77 \cdot (33.3)^2 \cdot 0.85 \approx 1020\text{ N} \quad (\approx 104\text{ kgf})$$
   - **Momento flector en la base del pilar maestro:**
     $$M_{vuelco} = F_T \cdot h = 1020\text{ N} \cdot 3.50\text{ m} = 3570\text{ N}\cdot\text{m} \quad (364\text{ kgf}\cdot\text{m})$$
2. **Bancada Solar Fotovoltaica (16 Paneles monocristalinos 550W):**
   - Peso propio: $16 \times 28\text{ kg} = 448\text{ kg}$.
   - Estructura de aluminio anodizado y lastres/anclajes: $280\text{ kg}$.
   - Carga distribuida media: $\approx 22\text{ kg/m}^2$.
   - Coeficiente de presión neta por succión de viento: $C_p = -1.2$ (diseño de anclajes químicos a tracción: $F_{arranque} \ge 180\text{ kgf}$ por anclaje).
3. **Termosifón Solar e Interacumulador de Inercia:**
   - Depósito de inercia solar primario: $300\text{ L}$ de agua + $75\text{ kg}$ estructura = $375\text{ kg}$ concentrado en $1.2\text{ m}^2$.
4. **Cúpula / Vitrina Cenital Astronómica (Observatorio Estelar):**
   - Bastidor de perfiles estructurales de acero al carbono 80x40x3mm + marcos de aluminio RPT: $160\text{ kg}$.
   - Vidrio doble laminado templado ($8\text{ mm} + \text{PVB} + 8\text{ mm}$, $3.0\text{ m} \times 2.0\text{ m}$): $\approx 240\text{ kg}$.
   - Peso total sobre losa perimetral de vitrina: $400\text{ kg}$.

### 2.2 Zona Técnica en Planta Baja (Cuarto IT y Sala Eléctrica)
- Banco de Baterías LiFePO4 ($30\text{ kWh}$, 6 módulos rack 48V): $320\text{ kg}$ sobre $0.8\text{ m}^2$ ($400\text{ kg/m}^2$).
- Generador gasolina insonorizado de emergencia: $115\text{ kg}$ con depósito lleno.
- **Solución constructiva:** Losa maciza de cimentación de espesor $e = 20\text{ cm}$ con doble mallazo $\phi 10\text{ mm}$ cada $15\text{ cm}$ ($f'_c = 250\text{ kg/cm}^2$) desacoplada acústicamente mediante juntas de neopreno de alta densidad para evitar transmisión de vibraciones mecánicas al resto de la vivienda.

---

## 3. Dimensionamiento Estructural

### 3.1 Zapatas Aisladas y Vigas de Atado (Riostras)
- **Zapatas Centrales (Columnas con soporte de cubierta técnica):**
  - Carga axial de servicio total ($P_{serv}$): $280\text{ kN}$ ($28.5\text{ toneladas}$).
  - Área requerida: $A = \frac{P_{serv}}{\sigma_{adm}} = \frac{280}{180} = 1.55\text{ m}^2 \implies B \times L = 1.30\text{ m} \times 1.30\text{ m}$.
  - Canto mínimo de zapata ($h_z$): $45\text{ cm}$ (para verificar punzonamiento sin armadura transversal de corte).
  - Armadura inferior en ambas direcciones: Parrilla de varillas $\phi 12\text{ mm}$ cada $15\text{ cm}$ ($B400S$ o Grado 60).
- **Vigas Riostras de Atado (Antisísmicas):**
  - Sección: $30\text{ cm} \times 30\text{ cm}$.
  - Armadura longitudinal: 4 varillas $\phi 12\text{ mm}$ (2 superiores, 2 inferiores).
  - Estribos: $\phi 8\text{ mm}$ cerrados con ganchos sísmicos a $135^\circ$, cada $10\text{ cm}$ en zonas de confinamiento y cada $20\text{ cm}$ en zona central.

### 3.2 Columnas Principales
- **Sección:** $30\text{ cm} \times 30\text{ cm}$ en hormigón armado $f'_c \ge 250\text{ kg/cm}^2$.
- **Columna Maestra de Anclaje del Mástil Eólico:**
  - Sobredimensionada a $35\text{ cm} \times 35\text{ cm}$.
  - Refuerzo longitudinal: 8 varillas $\phi 16\text{ mm}$ continuas desde zapata hasta azotea para resistir el momento de flexotorsión $M_{vuelco} = 3570\text{ N}\cdot\text{m}$.
  - Placa de anclaje en cabeza de columna: Chapa de acero estructural S275JR de $400\text{ mm} \times 400\text{ mm} \times 20\text{ mm}$, soldada con 8 pernos de anclaje roscados embebidos $M20$ (acero Grado 8.8) con profundidad de embebido $L_e \ge 450\text{ mm}$.

---

## 4. Guía de Modelado FOSS

```mermaid
flowchart LR
    A["Estudio SPT (Datos CSV)"] --> B["LibreCAD (Ejes y Zapatas 2D)"]
    B --> C["FreeCAD (BIM / Arch Workbench)"]
    C --> D["FreeCAD FEM (Malla CalculiX)"]
    D --> E["Validación Tensiones Von Mises y Desplazamientos"]
```

1. **LibreCAD (Planta de Cimentaciones):**
   - Capa `CIM_ZAPATAS`: polígonos cerrados de zapatas $1.30 \times 1.30\text{ m}$ y $1.10 \times 1.10\text{ m}$.
   - Capa `CIM_RIOSTRAS`: ejes y líneas dobles de vigas de atado $0.30\text{ m}$.
   - Capa `CIM_LOSA_IT`: contorno de la losa de sala técnica $2.40 \times 3.00\text{ m}$.
   - Exportación directa en formato `.DXF` estandarizado R12/2000.
2. **FreeCAD (BIM & FEM):**
   - Importación de `.dxf` en *BIM / Arch Workbench*.
   - Extrusión de columnas y losas con material predefinido: `Concrete f'c=25 MPa, E=25 GPa, Poisson=0.2`.
   - Inserción de la placa de anclaje de turbina eólica en *Part Design*.
   - Módulo *FEM*: Aplicación de fuerza tangencial $F_T = 1020\text{ N}$ y torsión en la base del mástil. Simulación con solver CalculiX para verificar que la deformación máxima en punta de columna sea inferior a $H/500 = 7\text{ mm}$.
