# Escribe tu código aquí :-)

# CREACIÓN DE MÓDULOS

import machine
import time

"""
Vamos a crear una función que nos va a permitir hacer parpadear
cualquier led que deseeamos conectado a un pin de nuestra preferencia
esto debe ser lo más general posible para facilitar su practicidad
"""


def parpadeo(tiempo_pardadeo, numero_de_parpadeos, pin):

    led = machine.Pin(pin, machine.Pin.OUT)

    for x in range(numero_de_parpadeos):
        led.on()
        time.sleep_ms(tiempo_pardadeo)
        led.off()
        time.sleep_ms(tiempo_pardadeo)

return ('LISTO!')
