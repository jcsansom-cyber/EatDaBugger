import serial

try:
    arduino = serial.Serial("COM7", timeout=1)
except:
    print("Check Port")

def controller():
    ret=str(arduino.readine())
    return ret
