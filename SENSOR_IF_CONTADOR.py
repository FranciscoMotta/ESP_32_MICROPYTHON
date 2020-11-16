# Escribe tu código aquí :-)
# Sensor de objetos con contador

import machine
import time

contador = 0

sensor = machine.Pin(15, machine.Pin.IN)
led = machine.Pin(2, machine.Pin.OUT)

while True:

    if(sensor.value() == 0):
        led.on()
        time.sleep_ms(50)
        if (contador == 30):
            print("ALERTA! MUCHAS PERSONAS")
            contador = 0
        else:
            contador = contador + 1
        print("Numero de interferencias:", contador)
    elif(sensor.value() == 1):
        led.off()

