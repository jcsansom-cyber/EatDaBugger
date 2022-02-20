import serial

try:
    arduino = serial.Serial("7", timeout=1)
except:
    print("Check Port")

def controller():
    ret=arduino.readine()
    return ret
