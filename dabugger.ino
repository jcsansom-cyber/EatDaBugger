// This example use I2C.
//import processing.serial.*; // imports library for serial communication
//import java.awt.Robot; // imports library for key press or release simulation
//import java.awt.event.KeyEvent; // imports library for reading the data from the serial port
//import java.io.IOException;

#include "LIS3DHTR.h"
#include <Wire.h>
LIS3DHTR<TwoWire> LIS; //IIC
#define WIRE Wire

void setup(){
//{try 
//{
//robot = new Robot();
//}
//catch (Exception e) {
//e.printStackTrace();
//exit();
//}
//Wire.begin();
  Serial.begin(9600);
  while (!Serial)
  {
  };
  LIS.begin(WIRE, LIS3DHTR_ADDRESS_UPDATED); //IIC init
  delay(100);
  LIS.setOutputDataRate(LIS3DHTR_DATARATE_50HZ);

}
void loop()
{
  if (!LIS)
  {
    Serial.println("LIS3DHTR didn't connect.");
    while (1)
      ;
    return;
  }
  //3 axis
//   Serial.print("x:"); Serial.print(LIS.getAccelerationX()); Serial.print("  ");
//   Serial.print("y:"); Serial.print(LIS.getAccelerationY()); Serial.print("  ");
//   Serial.print("z:"); Serial.println(LIS.getAccelerationZ());

   if (LIS.getAccelerationX() > .1){
//      robot.keyPress(KeyEvent.VK_UP);
      Serial.print("1");
   
    }
   if(LIS.getAccelerationX() < -.1){
//      robot.keyPress(KeyEvent.VK_DOWN);
      Serial.print("2");
   }
   if(LIS.getAccelerationY() > .1){
//      robot.keyPress(KeyEvent.VK_UP);
      Serial.print("3");
   
    }
   if(LIS.getAccelerationY() < -.1){
//      robot.keyPress(KeyEvent.VK_DOWN);
      Serial.print("4");
   }
   else{
//   robot.keyRelease(KeyEvent.VK_UP);
//   robot.keyRelease(KeyEvent.VK_DOWN);
    }
}
