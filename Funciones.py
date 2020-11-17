# Escribe tu código aquí :-)

# Apartado para las funciones

import machine
import time

led = machine.Pin(2, machine.Pin.OUT)

def saludo():
    print("HOLA MUNDO!")

# FUNCION CON VALORES ARBITRARIOS

def destellos(*arb):
    suma = 0

    for i in arb:
        suma += i

    print("EL LED VA A PRENDER: ", suma, " VECES")

    for x in range(suma):
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)

