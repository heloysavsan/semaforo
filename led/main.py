from machine import Pin
from utime import sleep

led_verde = Pin(15, Pin.OUT)
led_amarelo = Pin(16, Pin.OUT)
led_vermelho = Pin(17, Pin.OUT)

while True:
    led_verde.on()
    led_amarelo.off()
    led_vermelho.off()
    print('led_verde - Deixar ligado por 20 segundos')
    sleep(20)
    led.verde.off()
    sleep(0.5)

    led_amarelo.on()
    print('led_amarelo - Deixar ligado por 10 segundos')
    sleep(10)
    led_amarelo.off()
    sleep(0.5)

    led_vermelho.on()
    print('led_vermelho - Deixar ligado por 7 segundos')
    sleep(7)
    led_vermelho.off()
    sleep(0.5)
