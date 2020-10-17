# Escribe tu código aquí :-)

import time
import machine

led = machine.Pin(2, machine.Pin.OUT)
boton = machine.Pin(15, machine.Pin.IN)
counter = 0
x = 0
while True:

    state = boton.value()
    time.sleep_ms(10)
    led.off()

    if (state == 1):
        counter += 1
        print("El valor de cuenta es: ", counter)

        if (counter == 1):
            led.on()
            time.sleep_ms(1000)
            led.off()
        elif(counter == 2):
            for x in range(3):
                led.on()
                time.sleep_ms(1000)
                led.off()
                time.sleep_ms(500)
        elif(counter == 3):
            for x in range(3):
                led.on()
                time.sleep_ms(100)
                led.off()
                time.sleep_ms(100)
        else:
            led.off()
            time.sleep_ms(100)
            counter = 0
