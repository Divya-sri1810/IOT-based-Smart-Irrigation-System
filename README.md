# Automatic Controlling System of Pump based on Temperature and Moisture Conditions with IoT Monitoring
## 📌 Overview
This project presents an IoT-based Smart Irrigation System designed to automate water supply for agricultural fields based on temperature and soil moisture levels. Using an Arduino UNO, sensors, and Python-based notifications, the system improves irrigation efficiency, conserves water, and allows remote monitoring through Gmail notifications.

## ✨ Features
- 🌱 Automatic irrigation control based on temperature and soil moisture.

- 📊 Real-time monitoring using DHT11 and soil moisture sensors.

- 🔔 Gmail notifications for moisture and motor status using Python.

- 💧 Water conservation through intelligent irrigation scheduling.

- 📱 Remote monitoring capability for farmers using smartphones.

## 🛠 Hardware Requirements
- Arduino UNO (ATmega328)

- Soil Moisture Sensor

- DHT11 Temperature & Humidity Sensor

- Relay Module

- DC Motor Pump

- LCD Display

- Power Supply

## 💻 Software Requirements
- Arduino IDE – For coding and uploading programs to Arduino.

- Python IDLE – For reading sensor data and sending Gmail notifications.

Required Libraries:

-  smtplib (for Gmail notifications)

-  pyserial (for serial communication with Arduino)

## 📐 System Design
1. Sensors collect real-time temperature, humidity, and soil moisture data.

2. Arduino processes the sensor values and controls the pump using a relay module.

3. Python script communicates with Arduino and sends Gmail notifications to farmers.

4. LCD displays live data for on-field monitoring.

## 🔄 Workflow
|Condition |Action|
|----------|------|
|Temp > 34°C & Soil Dry	|Pump ON|
|Temp > 34°C & Soil Wet	|Pump ON|
|Temp < 34°C & Soil Wet	|Pump OFF|
|Temp < 34°C & Soil Dry	|Pump ON|

## 🚜 Applications
- Precision Agriculture: Provides accurate irrigation control for better crop health.

- Water Conservation: Reduces overwatering and prevents wastage.

- Cost Reduction: Minimizes manual labor and water expenses.

## 📄 Conclusion
This IoT-based irrigation system enables sustainable farming, reduces resource waste, and improves crop yield. Farmers can remotely monitor irrigation status, ensuring an automated, cost-effective, and intelligent irrigation solution.

## 📚 References
- "A Smart Irrigation System Using IoT and Fuzzy Logic Controller" – HCT ITT 2018

- "Smart Irrigation System based on ThingSpeak and Arduino" – ICASS 2018

- "Development of a Cloud-based Automatic Irrigation System" – ICMCST 2018

- "Research of Irrigation Control System Based on Fuzzy Neural Network" – Mechatronic Science Conference 2011

- "Automated Water Supply Control System of Graded Constant Pressure" – WRI Global Congress 2010

