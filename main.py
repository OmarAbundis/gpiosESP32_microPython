# Programa de prueba de las distintas líneas de entrada de un
# ESP32DevKit, utilizando micropython

from machine import Pin,ADC,PWM
from time import sleep

# Configuración de GPIOs

led = Pin(4,Pin.OUT)
button = Pin(5,Pin.IN)

#Configuración del ADC con una resolución de 10 bits.

pot = ADC(Pin(34))
pot.width(ADC.WIDTH_10BIT)
pot.atten(ADC.ATTN_11DB)

# Configuración del PWM

ledPWM = PWM(Pin(13),50)

while True:
    buttonState = button.value()
    led.value(buttonState)
    
    potValue = pot.read()
    ledPWM.duty(potValue)
    
    sleep(0.1)