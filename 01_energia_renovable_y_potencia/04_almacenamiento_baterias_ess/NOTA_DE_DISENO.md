# Ficha Técnica y Nota de Cálculo: Banco de Baterías LiFePO4 ESS

## 1. Especificaciones del Banco ESS
- **Capacidad Total:** $30.72\text{ kWh}$ nominal ($600\text{ Ah}$ a $51.2\text{ V}$).
- **Composición:** 6 módulos rack 19" de $48\text{V} / 100\text{Ah}$ en paralelo (celdas prismáticas LiFePO4 Grado A, $3.2\text{V} / 100\text{Ah}$, 16S1P por módulo).
- **Corriente de Carga Recomendada:** $0.5C = 50\text{ A}$ por módulo ($300\text{ A}$ total del banco).
- **Corriente de Descarga Máxima Continua:** $100\text{ A}$ por módulo ($600\text{ A}$ pico / $30.7\text{ kW}$).
- **Ciclos de Vida:** $\ge 6,000$ ciclos al $80\%$ DoD y $25^\circ\text{C}$.

## 2. Protecciones y Desconexión
- Desconectador seccionador fusible tipo NH00 de $250\text{ A}$ gG por cada ramal de 3 módulos.
- Sensor térmico de sobrecalentamiento en bornes con desconexión automática por contactor biestable si $T_{celda} > 50^\circ\text{C}$.
- Sistema de extinción automática local por aerosol de sales de potasio en el interior del gabinete de baterías.

*Para la memoria de cálculo completa, consulte [`docs/notas_de_diseno/04_balance_cargas_y_dimensionamiento_energetico.md`](../../docs/notas_de_diseno/04_balance_cargas_y_dimensionamiento_energetico.md).*

