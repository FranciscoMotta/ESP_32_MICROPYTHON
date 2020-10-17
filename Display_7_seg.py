# Escribe tu código aquí :-)

import time
import machine

segmentoA = machine.Pin(13, machine.Pin.OUT)
segmentoB = machine.Pin(12, machine.Pin.OUT)
segmentoC = machine.Pin(27, machine.Pin.OUT)
segmentoD = machine.Pin(26, machine.Pin.OUT)
segmentoE = machine.Pin(14, machine.Pin.OUT)
segmentoF = machine.Pin(4, machine.Pin.OUT)
segmentoG = machine.Pin(2, machine.Pin.OUT)

boton = machine.Pin(15, machine.Pin.IN)

counter = 0
while True:
    segmentoA.off()
    segmentoF.off()
    segmentoC.off()
    segmentoD.off()
    segmentoE.off()
    segmentoG.on()
    segmentoB.off()

    estado = boton.value()
    if (estado == 1):

        counter = counter + 1

        if (counter == 1):
            print("EL valor del contador: ", counter)
            segmentoA.on()
            segmentoB.off()
            segmentoC.off()
            segmentoD.on()
            segmentoE.on()
            segmentoF.on()
            segmentoG.on()
            time.sleep_ms(1000)
        elif (counter == 2):
            print("EL valor del contador: ", counter)
            segmentoA.off()
            segmentoB.off()
            segmentoC.on()
            segmentoD.off()
            segmentoE.off()
            segmentoF.on()
            segmentoG.off()
            time.sleep_ms(1000)
        elif (counter == 3):
            print("EL valor del contador: ", counter)
            segmentoA.off()
            segmentoB.off()
            segmentoC.off()
            segmentoD.off()
            segmentoE.on()
            segmentoF.on()
            segmentoG.off()
            time.sleep_ms(1000)
        elif (counter == 4):
            print("EL valor del contador: ", counter)
            segmentoA.on()
            segmentoB.off()
            segmentoC.off()
            segmentoD.on()
            segmentoE.on()
            segmentoF.off()
            segmentoG.off()
            time.sleep_ms(1000)
        elif (counter == 5):
            print("EL valor del contador: ", counter)
            segmentoA.off()
            segmentoB.on()
            segmentoC.off()
            segmentoD.off()
            segmentoE.on()
            segmentoF.off()
            segmentoG.off()
            time.sleep_ms(1000)
        elif (counter > 5):
            counter = 0
