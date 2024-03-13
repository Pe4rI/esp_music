from machine import Pin, PWM
import time

# local
import notes
from notes import Note
from tunes import TEST

# initial values
pwm_pin_4 = PWM(Pin(4))
pwm_pin_4.freq(4000)
pwm_pin_4.duty(0)

# it is necessary to add small intervals of silence,
# so individual notes may be heard
end_cut = 2     # ms

# play
tempo = 120

for i in TEST:
    # print('Frequency of ', i.freq(),
    # 'played for ', 1000/tempo*i.dur(),
    # 'ms with duty of ', i.dut())
    
    pwm_pin_4.freq(i.freq())
    pwm_pin_4.duty(i.dut())
    time.sleep_ms(int(60000/tempo*i.dur() - end_cut))

    # the silent part
    pwm_pin_4.duty(0)
    time.sleep_ms(end_cut))
    
# volume 0
pwm_pin_4.duty(0)
 
