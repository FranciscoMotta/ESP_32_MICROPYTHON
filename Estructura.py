# Escribe tu código aquí :-)

# Importar Librerias

import time  # Importamos la libreria para los delay
import machine  # Importamos la libreria para los GPIO

# Variables

tiempo = 500  # Tiempo en ms

# Vamos a configurar los pines GPIO E/S

# Entrada

boton = machine.Pin(15, machine.Pin.IN)  # Pin 15 puesto como entrada
led = machine.Pin(2, machine.Pin.OUT)  # Pin 2 como salida

"""LED CON BOTON"""

while True:

    if (boton.value() == True):
        led.off()
        print("Boton activo")
        time.sleep_ms(10)
    else:
        led.on()
        time.sleep_ms(100)


