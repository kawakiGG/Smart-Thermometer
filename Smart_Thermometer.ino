int limit= 100;
#include <Wire.h>
#include <Adafruit_MLX90614.h>
Adafruit_MLX90614 mlx = Adafruit_MLX90614();
void setup() {
  Serial.begin(9600); 
  pinMode(13,OUTPUT);
  pinMode(12,OUTPUT);
  mlx.begin();  
}
void loop() {
  Serial.print(""); Serial.print(mlx.readObjectTempF()); Serial.println("");
 int current_temp = (mlx.readObjectTempF());
 if (current_temp>= limit){
  digitalWrite(13,HIGH);
  delay(1000);
  digitalWrite(13,LOW);
  }else if(current_temp>=92){
  digitalWrite(12,HIGH);
  delay(1000);
  digitalWrite(12,LOW);
    }
 delay(4000);

}
