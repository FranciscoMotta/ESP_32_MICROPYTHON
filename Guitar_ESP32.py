# Escribe tu código aquí :-)

import machine
import time
cuerda_Uno = TouchPad(Pin(13))

while True:

    Valor_cuerda = cuerda_Uno.read()
    print(Valor_cuerda)
    sleep(0.5)
