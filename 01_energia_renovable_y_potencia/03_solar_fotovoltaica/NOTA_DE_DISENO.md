# Ficha Técnica y Nota de Cálculo: Generación Solar Fotovoltaica

## 1. Arreglo de Paneles y Strings
- **Potencia Pico Total:** $8.80\text{ kWp}$ ($16 \times 550\text{ Wp}$).
- **Tipo de Panel:** Monocristalino N-Type TOPCon bifacial, eficiencia del módulo $21.5\%$.
- **Configuración:** 2 strings de 8 módulos cada uno conectados a 2 seguidores MPPT independientes.
- **Tensiones y Corrientes:**
  - $V_{mp} = 8 \times 42.1\text{ V} = 336.8\text{ V}$.
  - $V_{oc} = 8 \times 50.2\text{ V} = 401.6\text{ V}$ ($441.7\text{ V}$ corregido por temperatura fría extrema a $-10^\circ\text{C}$).
  - $I_{mp} = 13.06\text{ A}$ / $I_{sc} = 14.20\text{ A}$.

## 2. Inversor Híbrido y Protecciones DC
- Inversor cargador híbrido de $10\text{ kW}$ monofásico/bifásico con acoplamiento DC directo a banco de baterías de $48\text{V}$.
- Caja combinadora DC con fusibles gPV de $1000\text{ V} / 20\text{ A}$, descargador de sobretensiones transitorias SPD Clase II ($1000\text{ V}$ DC, $I_n = 20\text{ kA}$, $I_{max} = 40\text{ kA}$) y seccionador de corte en carga rotativo de $1000\text{ V} / 32\text{ A}$.

*Para la memoria de cálculo completa, consulte [`docs/notas_de_diseno/04_balance_cargas_y_dimensionamiento_energetico.md`](../../docs/notas_de_diseno/04_balance_cargas_y_dimensionamiento_energetico.md).*

