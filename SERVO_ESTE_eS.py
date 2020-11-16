# Escribe tu código aquí :-)
# Control de un servo con un boton

import time
import machine

led = machine.Pin(2, machine.Pin.OUT)
servo = machine.Pin(33, machine.Pin.OUT)
boton = machine.Pin(15, machine.Pin.IN)

while True:

    if(boton.value() == 1):
        led.on()
        servo.on()
        time.sleep_us(500)
        servo.off()
        time.sleep_ms(20)
        print("Led:", boton.value(), "servo a 0")
    elif (boton.value() == 0):
        led.off()
        servo.on()
        time.sleep_us(2000)
        servo.off()
        time.sleep_ms(20)
        print("Led:", boton.value(), "servo a 9  0")
