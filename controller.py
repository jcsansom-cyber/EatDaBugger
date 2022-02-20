import serial

try:
    arduino = serial.Serial("7", timeout=1)
except:
    print("Check Port")


ret=arduino.readine()
