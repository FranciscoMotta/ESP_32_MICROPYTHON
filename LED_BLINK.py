
# Escribe tu código aquí :-)

import time
import machine

led = machine.Pin(2, machine.Pin.OUT)

while True:
    led.on()
    time.sleep_ms(500)
    led.off()
    time.sleep_ms(500)


