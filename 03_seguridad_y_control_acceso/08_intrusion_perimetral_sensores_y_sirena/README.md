# Sistema de Intrusión Perimetral, Sensores Magnéticos, Rotura de Cristal y Sirena

Este subsistema implementa la protección perimetral activa y pasiva del inmueble conforme a la norma de seguridad EN 50131 Grado 2/3: anillo exterior de barreras infrarrojas activas (AIR), contactos magnéticos reed ocultos en carpinterías exteriores, detectores acústicos piezoeléctricos de rotura de cristal y sirena exterior autoalimentada de $120\text{ dB}$ con flash estroboscópico y protección antidesprendimiento.

---

## 1. Arquitectura de Zonas DEOL y Modos de Armado

```
+-------------------------------------------------------------------------------+
|                       PERÍMETRO Y ACCESOS EXTERIORES                          |
|  +--------------------+  +--------------------+  +-------------------------+  |
|  | 4x Barreras AIR    |  | Contactos Reed     |  | Sensores Rotura Vidrio  |  |
|  | Haz Cuádruple 60m  |  | Puertas y Ventanas |  | Impacto + Audio 5 kHz   |  |
|  +---------+----------+  +---------+----------+  +------------+------------+  |
+------------|-----------------------|--------------------------|---------------+
             \                       |                          /
              \                      |                         /
               v                     v                        v
+-------------------------------------------------------------------------------+
|                     CENTRAL DE ALARMA AUTÓNOMA (ESP32)                        |
|                     Supervisión de Doble Fin de Línea (DEOL 2x 2.2kΩ)         |
|                                                                               |
|  +-------------------------------------+   +-------------------------------+  |
|  | Driver MOSFET AOD4184A + Fusible PTC|-->| Sirena Exterior 120 dB IP65   |  |
|  +-------------------------------------+   +-------------------------------+  |
|  +-------------------------------------+   +-------------------------------+  |
|  | Driver MOSFET Estroboscópico Rojo   |-->| Flash LED Señalización Visual |  |
|  +-------------------------------------+   +-------------------------------+  |
|  +-------------------------------------+   +-------------------------------+  |
|  | Batería Respaldo 12V 2.2Ah Plomo-Gel|-->| Monitorización ADC Tensión    |  |
|  +-------------------------------------+   +-------------------------------+  |
+------------------------------------+------------------------------------------+
                                     | Wi-Fi VLAN 30 IoT (Sin Salida WAN)
                                     v
                  +--------------------------------------+
                  | Home Assistant (Integración Alarmo)  |
                  | - Armado Total (Fuera de Casa)       |
                  | - Armado Noche (Perimetral Seguro)   |
                  | - Desarmado                          |
                  +--------------------------------------+
```

### Principio de Supervisión DEOL (Doble Fin de Línea)
Mediante dos resistencias de $2.2\text{ k}\Omega$ en el sensor (una en paralelo con el contacto de alarma y otra en serie con el contacto de tamper), la central mide la resistencia total del bucle:
- **Reposo (Normal):** $R = 2.2\text{ k}\Omega$ (Tensión ADC $\approx 1.65\text{V}$).
- **Alarma (Apertura):** $R = 4.4\text{ k}\Omega$ (Tensión ADC $\approx 2.20\text{V}$).
- **Sabotaje / Corte de Cable:** $R = \infty$ (Tensión ADC $> 2.95\text{V}$).
- **Sabotaje / Cortocircuito:** $R = 0\ \Omega$ (Tensión ADC $< 0.35\text{V}$).

---

## 2. Entregables y Modelos del Subsistema

### 2.1 Diseño Mecánico y Sirena Exterior 3D (`mecanico/`)
- **Modelo CAD FreeCAD 1.1+**: [sirena_exterior_y_barrera_infrarroja.FCStd](mecanico/sirena_exterior_y_barrera_infrarroja.FCStd)
- **Modelo de Intercambio STEP**: [sirena_exterior_y_barrera_infrarroja.step](mecanico/sirena_exterior_y_barrera_infrarroja.step)
- **Script Generador 3D**: [generar_sirena_intrusion_3d.py](../../scripts/generar_sirena_intrusion_3d.py)
- **Plano 2D CAD (DXF)**: [plano_seguridad_perimetral_intrusion.dxf](mecanico/plano_seguridad_perimetral_intrusion.dxf)
- **Plano Vectorial SVG**: [plano_seguridad_perimetral_intrusion.svg](mecanico/plano_seguridad_perimetral_intrusion.svg)
- **Script Generador Plano 2D**: [generar_plano_intrusion.py](../../scripts/generar_plano_intrusion.py)
- **Especificaciones**:
  - Envolvente de sirena exterior en policarbonato anti-UV ($200 \times 280 \times 85\text{ mm}$, IP65/IK08) con doble blindaje interno de acero zincado antiespuma y antitaladro.
  - Columna de barrera infrarroja activa (AIR) de aluminio anodizado ($450\text{ mm}$) con haz cuádruple sincronizado de $60\text{ m}$ de alcance.
  - Detector acústico de rotura de cristal con doble sensor (infrasónico de impacto + piezoeléctrico de alta frecuencia $4\text{ - }6\text{ kHz}$).
  - Plano general de implantación perimetral en parcela de $20 \times 20\text{ m}$.

### 2.2 Diseño Eléctrico y Esquemático KiCad 10 (`electrico/`)
- **Proyecto KiCad 10**: [central_alarma_intrusion_perimetral.kicad_pro](electrico/central_alarma_intrusion_perimetral.kicad_pro)
- **Esquema Electrónico**: [central_alarma_intrusion_perimetral.kicad_sch](electrico/central_alarma_intrusion_perimetral.kicad_sch)
- **Vectorial SVG**: [central_alarma_intrusion_perimetral.svg](electrico/esquema_svg/central_alarma_intrusion_perimetral.svg)
- **Lista de Materiales y Costes (BOM)**: [BOM.md](electrico/BOM.md)
- **Script Generador KiCad**: [generar_kicad_intrusion.py](../../scripts/generar_kicad_intrusion.py)
- **Topología Electrónica**:
  - 4 zonas balanceadas con medición analógica continua y supresión de transitorios ESD por diodos TVS bidireccionales SMBJ15CA.
  - Driver de potencia para sirena exterior de $120\text{ dB}$ ($12\text{VDC}$, $2\text{A}$) con MOSFET AOD4184A y protección por fusible rearmable Polyswitch PTC de $2.5\text{A}$.
  - Driver independiente para flash estroboscópico de LEDs de alta luminosidad.
  - Regulador reductor MP1584 de $12\text{V}$ a $3.3\text{V}$ y circuito de respaldo con batería local de $12\text{V}$.

### 2.3 Firmware y Automatización ESPHome (`control/`)
- **Firmware ESPHome**: [central_intrusion_alarma.yaml](control/central_intrusion_alarma.yaml)
- **Lógica Integrada**:
  - Algoritmo de discriminación de estados DEOL en tiempo real con filtrado digital anti-ruido de 50 ms.
  - Temporizador de desconexión acústica automática a los 180 segundos conforme a normativas de contaminación acústica.
  - Integración nativa con la plataforma `Alarmo` de Home Assistant:
    - **Armado Fuera de Casa (Total):** Activa todas las zonas exteriores e interiores y videovigilancia Frigate.
    - **Armado Noche (Perimetral):** Vigila el vallado exterior AIR, accesos y lucernario cenital permitiendo la libre circulación nocturna interior.
  - Disuasión activa: ráfagas estroboscópicas e intermitencia de iluminación perimetral en caso de salto de alarma.
