# Escribe tu código aquí :-)

from machine import ADC, Pin
import time

adc = ADC(Pin(32)) # Usamos el pin análogo 32

adc.atten(ADC.ATTN_11DB)

""" Otras combinaciones de atenuación
    ADC.ATTN_0DB : 1 volt max
    ADC.ATTN_2_5DB : 1.34 volt max
    ADC.ATTN_6DB : 2 volt max
    ADC.ATTN_11DB : 3.6 volt max
"""

while True:

    v = adc.read()
    print("El valor analogo es: ", v)
    time.sleep_ms(500)# Escribe tu código aquí :-)
