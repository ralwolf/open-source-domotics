# NDT-04: Balance de Cargas Eléctricas, Matriz Renovable y Almacenamiento ESS

## 1. Matriz de Balance de Cargas de la Vivienda

Para garantizar autonomía energética total (*Off-Grid*) con opción a respaldo de red (*Grid-Tied con Zero Export*), las cargas se clasifican en dos barras colectoras: **Cargas Críticas/Esenciales (Barra A)** y **Cargas Generales/Deslastrables (Barra B)**.

### 1.1 Tabla de Consumos Diarios Estimados
| Subsistema / Carga | Tensión (V) | Pot. Nom. (W) | $\cos \phi$ | Horas/Día | Energía (Wh/Día) | Barra |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Rack IT (Proxmox, TrueNAS, HA, PoE, Router)** | 120/230 AC | 220 | 0.95 | 24.0 | 5,280 | A (Crítica) |
| **Refrigerador + Congelador Inverter** | 120/230 AC | 140 | 0.85 | 8.0 (ciclo) | 1,120 | A (Crítica) |
| **Seguridad, Válvulas Gas/Agua e Intercom** | 24 DC / 120 | 45 | 0.90 | 24.0 | 1,080 | A (Crítica) |
| **Iluminación Esencial LED Circadiana** | 24 DC / 120 | 120 | 0.95 | 6.0 | 720 | A (Crítica) |
| **Bomba Presurizadora Agua Sanitaria** | 120/230 AC | 650 | 0.80 | 1.0 | 650 | A (Crítica) |
| **Ventilación Mecánica VMC con Recuperador** | 120/230 AC | 55 | 0.90 | 24.0 | 1,320 | A (Crítica) |
| *Subtotal Barra Crítica (Esencial)* | - | - | - | - | **10,170 Wh/d** | **Barra A** |
| **Placa de Inducción + Horno Eléctrico** | 230 AC | 3,200 | 0.98 | 1.5 | 4,800 | B (General) |
| **Lavadora y Secadora Bomba de Calor** | 230 AC | 1,400 | 0.92 | 1.5 | 2,100 | B (General) |
| **Climatización Multi-Split Inverter (A/C)** | 230 AC | 1,800 | 0.95 | 4.0 | 7,200 | B (General) |
| **Depuración y Química de Piscina** | 230 AC | 750 | 0.85 | 3.0 | 2,250 | B (General) |
| *Subtotal Barra General* | - | - | - | - | **16,350 Wh/d** | **Barra B** |
| **TOTAL CONSUMO DIARIO MEDIO ($E_{total}$)** | - | - | - | - | **26,520 Wh/d** | **A + B** |

---

## 2. Dimensionamiento del Banco de Almacenamiento LiFePO4 (ESS)

El banco opera a **$51.2\text{ V}$ nominal (16S)** para minimizar corrientes de descarga y pérdidas por efecto Joule ($P_{loss} = I^2 R$).

### 2.1 Ecuación de Capacidad Requerida
$$C_{Ah} = \frac{E_{critica} \cdot N_{autonomia}}{DoD \cdot \eta_{inversor} \cdot V_{nominal}}$$

- **Autonomía deseada sin sol ni viento ($N_{autonomia}$):** $2.0\text{ días}$ para la barra crítica ($20,340\text{ Wh}$).
- **Profundidad de descarga ($DoD$):** $0.80$ ($80\%$, garantizando $> 6,000$ ciclos al $80\%$ de salud).
- **Eficiencia del inversor/cargador ($\eta_{inversor}$):** $0.93$.
- **Tensión de banco ($V_{nominal}$):** $51.2\text{ V}$.

$$C_{Ah} = \frac{20340\text{ Wh}}{0.80 \cdot 0.93 \cdot 51.2\text{ V}} \approx 534\text{ Ah}$$

### 2.2 Configuración del Banco Físico
- **Módulos:** 6 módulos rackeables de $5.12\text{ kWh}$ cada uno ($48\text{V} / 100\text{Ah}$) en paralelo.
- **Capacidad Total Instalada:** **$30.72\text{ kWh}$ ($600\text{ Ah}$ a $51.2\text{ V}$)**.
- **BMS (Battery Management System):** Comunicación nativa mediante bus CAN / RS-485 con protocolo Pylontech hacia el inversor híbrido y Home Assistant.

---

## 3. Dimensionamiento del Campo Solar Fotovoltaico

### 3.1 Potencia Pico Requerida ($P_{pico}$)
$$P_{pico} = \frac{E_{total}}{HSP \cdot PR}$$

- **Horas de Sol Pico anuales medias ($HSP$):** $4.8\text{ h/día}$.
- **Performance Ratio ($PR$):** $0.78$ (pérdidas térmicas en celdas, polvo, caídas en cableado DC y rendimiento MPPT).
- **Consumo total a cubrir:** $26,520\text{ Wh/día}$.

$$P_{pico} = \frac{26520}{4.8 \cdot 0.78} = 7,083\text{ Wp} \approx 7.1\text{ kWp}$$

### 3.2 Selección y Arreglo de Paneles
- **Módulos:** 16 paneles monocristalinos bifaciales de $550\text{ Wp}$ (Tecnología N-Type TOPCon).
- **Potencia Pico Total:** **$8.80\text{ kWp}$** (proporciona un sobredimensionamiento del $24\%$ para compensar días nublados de invierno).
- **Arreglo Eléctrico:** 2 strings independientes de 8 paneles en serie:
  - Tensión de circuito abierto ($V_{oc}$ a $-10^\circ\text{C}$): $8 \times 50.2\text{ V} \times 1.10 = 441.7\text{ V}$ (dentro del rango MPPT $150 - 500\text{ V}$ DC del inversor).
  - Corriente de cortocircuito ($I_{sc}$): $14.2\text{ A}$ por string.

---

## 4. Integración del Aerogenerador Archimedes MK9

- **Curva de Producción:**
  - Velocidad de arranque (*Cut-in*): $1.5\text{ m/s}$.
  - Potencia nominal: $1,500\text{ W}$ a $12\text{ m/s}$.
  - Generación nocturna estimada (viento medio $5.5\text{ m/s}$): $\approx 350\text{ W}$ continuos $\implies 3.5 - 4.5\text{ kWh/noche}$, complementando la descarga nocturna de las baterías.
- **Controlador de Carga Híbrido Eólico:**
  - Rectificador trifásico síncrono con MPPT eólico de seguimiento de par.
  - Resistencia de frenado electrónico (*Dump Load*) de $2.0\text{ kW}$ con derivación PWM de excedentes hacia termoacumulador de agua caliente sanitaria.

---

## 5. Medición Granular y Telemetría en Tableros

```mermaid
graph LR
    RED["Red / Inversor"] --> TI_MAIN["Transformador de Corriente (CT 100A/50mA)"]
    TI_MAIN --> ATM90["Medidor ATM90E32 / Eastron SDM630 (Modbus RTU)"]
    ATM90 --> RS485["Bus RS-485 Blindado"]
    RS485 --> ESP["ESP32 Gateway (ESPHome)"]
    ESP -->|Ethernet/MQTT| HA["Home Assistant (Energía Dashboard)"]
```

- Transformadores de corriente toroidales de núcleo partido (*Split-Core CTs*) en cada circuito derivado de $15\text{A}$ y $20\text{A}$ (PZEM-004T v3 / CircuitSetup 6-channel expander).
- Muestreo a $1\text{ Hz}$ de: Tensión eficaz ($V_{rms}$), Corriente ($I_{rms}$), Potencia Activa ($W$), Factor de Potencia ($PF$) y Frecuencia ($Hz$).
