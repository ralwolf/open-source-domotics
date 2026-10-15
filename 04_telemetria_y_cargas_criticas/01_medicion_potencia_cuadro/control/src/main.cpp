/**
 * @file main.cpp
 * @brief Gateway ESP32 de Telemetría Energética, Modbus RTU y Desconexión de Emergencia
 * @project open-source-domotics
 * @license MIT / CERN-OHL-P
 */

#include <Arduino.h>
#include <WiFi.h>
#include <PubSubClient.h>
#include <ModbusMaster.h>
#include <PZEM004Tv30.h>
#include <U8g2lib.h>
#include <Wire.h>
#include <ArduinoJson.h>

// Definición de Pines de Hardware
#define PIN_RS485_RX      16
#define PIN_RS485_TX      17
#define PIN_RS485_DIR     23
#define PIN_PZEM_RX       18
#define PIN_PZEM_TX       19
#define PIN_RELAY_SHED    25
#define PIN_RELAY_SAFETY  26
#define PIN_I2C_SDA       21
#define PIN_I2C_SCL       22

// Configuración de Umbrales de Seguridad
#define MAX_POWER_TOTAL_WATTS 11500.0f // Límite de potencia contratada (11.5 kW)
#define OVERVOLTAGE_LIMIT     253.0f   // +10% sobre 230V
#define UNDERVOLTAGE_LIMIT    207.0f   // -10% sobre 230V

// Objetos de Comunicación y Periféricos
ModbusMaster sdm630;
PZEM004Tv30 pzem(Serial1, PIN_PZEM_RX, PIN_PZEM_TX);
U8G2_SSD1306_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, U8X8_PIN_NONE, PIN_I2C_SCL, PIN_I2C_SDA);
WiFiClient espClient;
PubSubClient mqttClient(espClient);

// Estructura de Telemetría
struct EnergyMetrics {
    float voltageGrid = 0.0f;
    float currentGrid = 0.0f;
    float activePowerGrid = 0.0f;
    float frequency = 0.0f;
    float powerFactor = 0.0f;
    float energyTotalKWh = 0.0f;
    float pzemVoltage = 0.0f;
    float pzemCurrent = 0.0f;
    float pzemPower = 0.0f;
    float pzemEnergy = 0.0f;
    bool loadSheddingActive = false;
    bool safetyCutoffActive = false;
} metrics;

// Control de Dirección del Transceptor RS-485
void preTransmission() {
    digitalWrite(PIN_RS485_DIR, HIGH);
}

void postTransmission() {
    digitalWrite(PIN_RS485_DIR, LOW);
}

// Lectura de Registros Modbus en Formato IEEE-754 (Float32)
float readModbusFloat(uint16_t regAddress) {
    uint8_t result = sdm630.readInputRegisters(regAddress, 2);
    if (result == sdm630.ku8MBSuccess) {
        uint16_t reg0 = sdm630.getResponseBuffer(0);
        uint16_t reg1 = sdm630.getResponseBuffer(1);
        uint32_t combined = ((uint32_t)reg0 << 16) | reg1;
        float value;
        memcpy(&value, &combined, sizeof(value));
        return value;
    }
    return -1.0f;
}

void updateDisplay() {
    u8g2.clearBuffer();
    u8g2.setFont(u8g2_font_6x10_tf);
    u8g2.drawStr(0, 10, "DOMOTICS ENERGY GW");
    
    char line1[32], line2[32], line3[32], line4[32];
    snprintf(line1, sizeof(line1), "V: %.1fV  I: %.2fA", metrics.voltageGrid, metrics.currentGrid);
    snprintf(line2, sizeof(line2), "Pot: %.0f W", metrics.activePowerGrid);
    snprintf(line3, sizeof(line3), "PZEM: %.0f W (%.1fA)", metrics.pzemPower, metrics.pzemCurrent);
    snprintf(line4, sizeof(line4), "Shed: %s | F: %.1fHz", 
             metrics.loadSheddingActive ? "OFF" : "ON", metrics.frequency);
    
    u8g2.drawStr(0, 24, line1);
    u8g2.drawStr(0, 38, line2);
    u8g2.drawStr(0, 50, line3);
    u8g2.drawStr(0, 62, line4);
    u8g2.sendBuffer();
}

void publishTelemetryMQTT() {
    StaticJsonDocument<512> doc;
    doc["grid_voltage"] = metrics.voltageGrid;
    doc["grid_current"] = metrics.currentGrid;
    doc["grid_power_w"] = metrics.activePowerGrid;
    doc["grid_frequency"] = metrics.frequency;
    doc["grid_pf"] = metrics.powerFactor;
    doc["grid_energy_kwh"] = metrics.energyTotalKWh;
    doc["sub_kitchen_power_w"] = metrics.pzemPower;
    doc["sub_kitchen_energy_kwh"] = metrics.pzemEnergy;
    doc["load_shedding"] = metrics.loadSheddingActive;
    doc["safety_cutoff"] = metrics.safetyCutoffActive;

    char buffer[512];
    serializeJson(doc, buffer);
    mqttClient.publish("domotics/power/gateway", buffer, true);
}

void evaluateSafetyRules() {
    // 1. Regla de Load-Shedding por sobrecarga (> 11.5 kW)
    if (metrics.activePowerGrid > MAX_POWER_TOTAL_WATTS && !metrics.loadSheddingActive) {
        metrics.loadSheddingActive = true;
        digitalWrite(PIN_RELAY_SHED, LOW); // Abre contactor de cargas prescindibles
        Serial.println("[ALERTA] Sobrecarga detectada. Desconectando cargas secundarias.");
    } else if (metrics.activePowerGrid < (MAX_POWER_TOTAL_WATTS * 0.80f) && metrics.loadSheddingActive) {
        // Histéresis del 20% antes de reenganchar cargas
        metrics.loadSheddingActive = false;
        digitalWrite(PIN_RELAY_SHED, HIGH); // Cierra contactor
        Serial.println("[INFO] Potencia normalizada. Cargas secundarias reenganchadas.");
    }

    // 2. Regla de sobretensión / subtensión severa de red
    if ((metrics.voltageGrid > OVERVOLTAGE_LIMIT || (metrics.voltageGrid > 50.0f && metrics.voltageGrid < UNDERVOLTAGE_LIMIT))) {
        metrics.safetyCutoffActive = true;
        digitalWrite(PIN_RELAY_SAFETY, HIGH); // Dispara corte o alarma
        Serial.println("[CRITICO] Anomalía de tensión fuera de rango IEC. Disparando protección.");
    } else {
        metrics.safetyCutoffActive = false;
        digitalWrite(PIN_RELAY_SAFETY, LOW);
    }
}

void setup() {
    Serial.begin(115200);
    Serial.println("\n--- Iniciando Gateway ESP32 Open-Source-Domotics ---");

    // Configuración de Pines
    pinMode(PIN_RS485_DIR, OUTPUT);
    digitalWrite(PIN_RS485_DIR, LOW);
    pinMode(PIN_RELAY_SHED, OUTPUT);
    digitalWrite(PIN_RELAY_SHED, HIGH); // NC activo por defecto
    pinMode(PIN_RELAY_SAFETY, OUTPUT);
    digitalWrite(PIN_RELAY_SAFETY, LOW);

    // Inicialización de Pantalla I2C
    Wire.begin(PIN_I2C_SDA, PIN_I2C_SCL);
    u8g2.begin();
    u8g2.clearBuffer();
    u8g2.setFont(u8g2_font_6x10_tf);
    u8g2.drawStr(0, 20, "Iniciando Sensores...");
    u8g2.sendBuffer();

    // Inicialización Modbus UART2
    Serial2.begin(9600, SERIAL_8N1, PIN_RS485_RX, PIN_RS485_TX);
    sdm630.begin(1, Serial2);
    sdm630.preTransmission(preTransmission);
    sdm630.postTransmission(postTransmission);

    Serial.println("Periféricos y buses configurados correctamente.");
}

void loop() {
    static unsigned long lastSampleTime = 0;
    static unsigned long lastDisplayTime = 0;

    unsigned long currentMillis = millis();

    // Muestreo cada 1000 ms (1 Hz)
    if (currentMillis - lastSampleTime >= 1000) {
        lastSampleTime = currentMillis;

        // Lecturas SDM630 Modbus
        float v = readModbusFloat(0x0000); // Voltaje
        float i = readModbusFloat(0x0006); // Corriente
        float p = readModbusFloat(0x0034); // Potencia Activa Total
        float f = readModbusFloat(0x0046); // Frecuencia
        float pf = readModbusFloat(0x001E); // Factor de Potencia
        float e = readModbusFloat(0x0156); // Energía Total kWh

        if (v > 0.0f) metrics.voltageGrid = v;
        if (i >= 0.0f) metrics.currentGrid = i;
        if (p >= 0.0f) metrics.activePowerGrid = p;
        if (f > 0.0f) metrics.frequency = f;
        if (pf >= 0.0f) metrics.powerFactor = pf;
        if (e >= 0.0f) metrics.energyTotalKWh = e;

        // Lecturas PZEM-004T v3
        metrics.pzemVoltage = pzem.voltage();
        metrics.pzemCurrent = pzem.current();
        metrics.pzemPower = pzem.power();
        metrics.pzemEnergy = pzem.energy();

        // Evaluación de protecciones
        evaluateSafetyRules();

        // Publicación MQTT si está conectado
        if (WiFi.status() == WL_CONNECTED && mqttClient.connected()) {
            publishTelemetryMQTT();
        }
    }

    // Actualización de pantalla cada 500 ms
    if (currentMillis - lastDisplayTime >= 500) {
        lastDisplayTime = currentMillis;
        updateDisplay();
    }
}

