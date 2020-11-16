# Escribe tu código aquí :-)
# Código de control de manejo de un servo

import time
import machine

boton = machine.Pin(15, machine.Pin.IN)
servo = machine.Pin(25, machine.Pin.OUT)
led = machine.Pin(2, machine.Pin.OUT)

state = boton.value()

while True:

    if (state == 1):
        servo.on()
        time.sleep_us(900)
        servo.off()
        time.sleep_ms(20)
        led.on()
        print("El servo a 0 grados")
    elif(state == 0):
        servo.on()
        time.sleep_us(1900)
        servo.off()
        time.sleep_ms(20)
        led.off()
        print("El servo a 90 grados")
