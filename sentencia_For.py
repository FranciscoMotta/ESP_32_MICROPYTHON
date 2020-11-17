# Escribe tu código aquí :-)
# Cógido de control para la sentencia FOR

import machine
import time

led = machine.Pin(12, machine.Pin.OUT)

while True:
    led.on()
