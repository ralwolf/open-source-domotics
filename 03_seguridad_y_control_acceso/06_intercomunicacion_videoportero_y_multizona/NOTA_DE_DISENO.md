# Ficha Técnica y Nota de Cálculo: Intercomunicación, Portero y Monitores de Habitación

## 1. Nodos de Intercomunicación
- **Videoportero Exterior:** Protocolo SIP estándar RFC 3261, PoE 802.3af, cámara $2\text{K}$ con visión IR de $940\text{ nm}$, relé integrado para apertura de portón y contacto magnético para sensor de estado de puerta abierta.
- **Pantallas Interiores (5 Ubicaciones):**
  1. Vestíbulo / Entrada Principal (Pared, 10").
  2. Cocina (Pared / Empotrada, 7").
  3. Sala de Estar / Salón (Pared, 10").
  4. Dormitorio Principal (Sobremesa o cabecero, 7").
  5. Despacho / Oficina (Sobremesa, 7").
- **Monitores Sensibles (Bebé y Mascotas):**
  - Sensor de imagen con LEDs infrarrojos de longitud de onda $940\text{ nm}$ (totalmente invisibles al ojo humano y animal).
  - Algoritmo de clasificación de eventos de sonido en tiempo real: notificación push y activación de audio bidireccional en pantallas prioritarias ante llanto infantil ($> 75\text{ dB}$, patrón armónico característico).

## 2. Pila de Software y Flujo de Audio/Video
- **PBX:** Asterisk 20 LTS o FreePBX sobre contenedor Proxmox.
- **Códecs de Audio:** Opus (banda ancha adaptativa para máxima inteligibilidad) y G.711 A-law (compatibilidad universal).
- **Códec de Video:** H.264 Baseline Profile empaquetado vía WebRTC a través de `go2rtc` para latencia $< 80\text{ ms}$.

*Para la memoria de cálculo completa, consulte [`docs/notas_de_diseno/05_infraestructura_it_red_vlans_y_seguridad.md`](../../docs/notas_de_diseno/05_infraestructura_it_red_vlans_y_seguridad.md).*
