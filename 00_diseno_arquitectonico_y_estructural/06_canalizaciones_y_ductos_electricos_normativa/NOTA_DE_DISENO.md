# Ficha Técnica y Nota de Cálculo: Canalizaciones Eléctricas y Redes de Datos

## 1. Tabla de Segregación Física en Obra
| Servicio | Tipo de Conductor | Ducto / Conduit | Distancia a Fuerza | Observaciones |
| :--- | :--- | :--- | :--- | :--- |
| **Fuerza AC 120/230V** | THHN/THWN-2 Cu 10/12/14 AWG | PVC Cédula 40 $\phi 1"$ | $0\text{ cm}$ (Referencia) | Canalización principal de potencia |
| **Red Datos / PoE** | Cat6A F/UTP libre de halógenos | Corrugado doble capa $\phi 25\text{ mm}$ | $\ge 30\text{ cm}$ | Cable apantallado con tierra en patch panel |
| **Buses Sensores / RS-485** | Par trenzado blindado 22 AWG | Corrugado $\phi 20\text{ mm}$ | $\ge 30\text{ cm}$ | Modbus RTU, 1-Wire y contacto seco |
| **Fibra Óptica (Backbone)** | Monomodo 2 hilos OS2 | Tubo liso rígido $\phi 20\text{ mm}$ | $\ge 10\text{ cm}$ | Inmune a EMI pero separada por protección física |

## 2. Puntos Clave de Instalación
- Todos los codos de conduit deben tener un radio de curvatura amplio ($R \ge 6 \times \text{diámetro}$) para no degradar la velocidad de transmisión de Cat6A.
- Registro en cada cambio de dirección mayor a $180^\circ$ acumulados.
- Hilos guía de nylon instalados permanentemente en cada ducto para ampliaciones futuras.

*Para la memoria de cálculo completa, consulte [`docs/notas_de_diseno/03_canalizaciones_normadas_y_redes_fluidos.md`](../../docs/notas_de_diseno/03_canalizaciones_normadas_y_redes_fluidos.md).*

