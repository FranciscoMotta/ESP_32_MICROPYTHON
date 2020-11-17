# Escribe tu código aquí :-)

from machine import ADC, Pin
import time

segmentoA = machine.Pin(13, machine.Pin.OUT)
segmentoB = machine.Pin(12, machine.Pin.OUT)
segmentoC = machine.Pin(14, machine.Pin.OUT)
segmentoD = machine.Pin(27, machine.Pin.OUT)
segmentoE = machine.Pin(26, machine.Pin.OUT)
segmentoF = machine.Pin(25, machine.Pin.OUT)
segmentoG = machine.Pin(23, machine.Pin.OUT)

adc = ADC(Pin(32)) # Usamos el pin análogo 32

adc.atten(ADC.ATTN_11DB)

""" Otras combinaciones de atenuación
    ADC.ATTN_0DB : 1 volt max
    ADC.ATTN_2_5DB : 1.34 volt max
    ADC.ATTN_6DB : 2 volt max
    ADC.ATTN_11DB : 3.6 volt max
"""

def number_Displayer(numero):

    if numero == 0:
        segmentoA.off()
        segmentoF.off()
        segmentoC.off()
        segmentoD.off()
        segmentoE.off()
        segmentoG.on()
        segmentoB.off()
    elif numero == 1:
        segmentoA.on()
        segmentoB.off()
        segmentoC.off()
        segmentoD.on()
        segmentoE.on()
        segmentoF.on()
        segmentoG.on()
    elif numero == 2:
        segmentoA.off()
        segmentoB.off()
        segmentoC.on()
        segmentoD.off()
        segmentoE.off()
        segmentoF.on()
        segmentoG.off()
    elif numero == 3:
        segmentoA.off()
        segmentoB.off()
        segmentoC.off()
        segmentoD.off()
        segmentoE.on()
        segmentoF.on()
        segmentoG.off()
    elif numero == 4:
        segmentoA.on()
        segmentoB.off()
        segmentoC.off()
        segmentoD.on()
        segmentoE.on()
        segmentoF.off()
        segmentoG.off()
    elif numero == 5:
        segmentoA.off()
        segmentoB.on()
        segmentoC.off()
        segmentoD.off()
        segmentoE.on()
        segmentoF.off()
        segmentoG.off()

while True:

    v = adc.read()
    if v < 600:
        number_Displayer(0)
    elif v < 1200:
        number_Displayer(1)
    elif v < 1800:
        number_Displayer(2)
    elif v < 2400:
        number_Displayer(3)
    elif v < 3000:
        number_Displayer(4)
    elif v < 4000:
        number_Displayer(5)

    print("El valor analogo es: ", v)
    time.sleep_ms(500)# Escribe tu código aquí :-)
