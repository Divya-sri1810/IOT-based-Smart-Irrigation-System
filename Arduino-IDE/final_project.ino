#include "DHT.h"
#define DHTPIN 8   
#define DHTTYPE DHT11
#include<LiquidCrystal.h>
LiquidCrystal LCD(A0,A1,A2,A3,A4,A5);
DHT dht(DHTPIN, DHTTYPE);
int sensor_pin=2;
int relay=3;
String str;
void setup() {
  pinMode(sensor_pin,INPUT);
  pinMode(relay,OUTPUT);
  Serial.begin(9600);
  digitalWrite(relay,HIGH);
  // Serial.println(F("DHTxx test!"));
   dht.begin();
   LCD.begin(16,2);
   LCD.clear();
   LCD.setCursor(0,0);
   LCD.print("IRRIGATION");
   LCD.setCursor(0,1);
   LCD.print("SYSTEM");
   delay(2000);
}

void loop() 
{
  
  float h = dht.readHumidity();
  float t = dht.readTemperature();


  if (isnan(h) || isnan(t)) {
    // Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  // Serial.println(F("Humidity: "));
  // Serial.println(h);
  // Serial.println(F("Temperature: "));
  // Serial.println(t);
  int sensor_data=digitalRead(sensor_pin);
  // Serial.println(sensor_data);
  LCD.clear();
   LCD.setCursor(0,0);
   LCD.print("TEMP:");
   LCD.setCursor(5,0);
   LCD.print(t);
   LCD.setCursor(10,0);
   LCD.print("MOI:");
   LCD.setCursor(14,0);
   LCD.print(sensor_data);
  LCD.setCursor(0,1);
   LCD.print("HUMIDITY:");
   LCD.setCursor(10,1);
   LCD.print(h);
   delay(2000);
   str=String(sensor_data)+String("!")+String(t)+String("@")+String(h);
   Serial.println(str);
   if(t>34&&sensor_data==1)
   {
    digitalWrite(relay,LOW);
    delay(5000);
    digitalWrite(relay,HIGH);
   }
   else if(t<=34&&sensor_data==1)
   {
    digitalWrite(relay,LOW);
    delay(5000);
    digitalWrite(relay,HIGH);
   }
   else if(t>34&&sensor_data==0)
   {
    digitalWrite(relay,LOW);
    delay(5000);
    digitalWrite(relay,HIGH);
   }
   else if(t<=34&&sensor_data==0)
   {
    digitalWrite(relay,HIGH);
   }
}
