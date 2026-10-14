# Ficha Técnica y Nota de Cálculo: Bioclimática, Ventilación y Lucernario Celeste

## 1. Especificaciones de la Cúpula Cenital
- **Dimensiones:** $3000\text{ mm} \times 2000\text{ mm}$.
- **Orientación:** Eje longitudinal alineado Norte-Sur astronómico.
- **Acristalamiento:** Doble vidrio de seguridad laminado extraclaro (bajo hierro) $8+8\text{ mm}$ con cámara de $16\text{ mm}$ con Argón ($U_g = 1.1\text{ W/m}^2\text{K}$).
- **Estructura:** Perfilería tubular $80 \times 40 \times 3\text{ mm}$ con rotura de puente térmico y babeta perimetral de estanqueidad de EPDM.

## 2. Automatización y Control
- **Actuadores:** 2 actuadores lineales de $24\text{ V}$ DC, carrera $300\text{ mm}$, empuje $1000\text{ N}$.
- **Driver de Potencia:** Placa de relés de estado sólido / puente H con medición de corriente para detección de atrapamiento.
- **Entradas de Seguridad:**
  - Sensor de lluvia óptico Hydreon RG-11 conectado por contacto seco a módulo ESPHome.
  - Anemómetro de pulsos (cierre forzado si viento $> 35\text{ km/h}$).
- **Modos de Operación en Home Assistant:**
  1. *Astro-Night Mode:* Persiana abierta al $100\%$, luces interiores apagadas o en rojo tenue ($< 2200\text{ K}$, $5\%$).
  2. *Summer Cool Flush:* Apertura al $40\%$ durante la madrugada si $T_{ext} < T_{int} - 2^\circ\text{C}$.
  3. *Storm Lock:* Cierre y bloqueo total inmediato ante primera gota o ráfaga.

*Para la memoria de cálculo completa, consulte [`docs/notas_de_diseno/02_bioclimatica_ventilacion_y_lucernario.md`](../../docs/notas_de_diseno/02_bioclimatica_ventilacion_y_lucernario.md).*
