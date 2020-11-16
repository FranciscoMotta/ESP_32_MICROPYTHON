
# Escribe tu código aquí :-)

import time
import machine

led = machine.Pin(2, machine.Pin.OUT)
boton = machine.Pin(15, machine.Pin.IN)

while True:
    if(boton.value() == 1):
        led.on()
        time.sleep_ms(100)
        led.off()
        time.sleep_ms(100)
    elif(boton.value() == 0):
        print("LED OFF")


