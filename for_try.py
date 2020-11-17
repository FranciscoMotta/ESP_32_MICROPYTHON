# Escribe tu código aquí :-)

import machine
import time
import math

led = machine.Pin(12, machine.Pin.OUT)

modpar = 0

while True:
    for i in range(0, 10):
        print("La cuenta es: ", i)
        time.sleep_ms(500)

        if (modpar == 0):
            led.on()
        else:
            led.off()
        # Buscamos optener un número par, por tal motivo
        # sacamos el módulo entre el contador y 2
        # es decir, divimos entre 2, de ser par, el residuo
        # es CERO, daro que se usa en la condicional
        modpar = math.fmod(i,2)
