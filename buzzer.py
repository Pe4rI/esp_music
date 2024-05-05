from machine import Pin,PWM

class Buzzer:
    def __init__(self, pin: Pin):
        this.__pwm = PWM(pin)