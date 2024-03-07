from machine import Pin, PWM
import time

import notes
from notes import Note

tune = [
        Note('d5', 1/16),
        Note('d5', 1/16),
        Note('a5', 1/16),
        Note('pause', 1/8),
        Note('g#5',1/16),
        Note('pause', 1/4),
        Note('g5',1/16),
        Note('pause', 1/16),
        Note('f5',1/8),
        Note('d5',1/16),
        Note('f5',1/16),
        Note('g5',1/16),
        
        Note('c5',1/16),
        Note('c5',1/16),
        Note('a5', 1/16),
        Note('pause', 1/8),
        Note('g#5',1/16),
        Note('pause', 1/4),
        Note('g5',1/16),
        Note('pause', 1/16),
        Note('f5',1/8),
        Note('d5',1/16),
        Note('f5',1/16),
        Note('g5',1/16),
        
        Note('b4',1/16),
        Note('b4',1/16),
        Note('a5', 1/16),
        Note('pause', 1/8),
        Note('g#5',1/16),
        Note('pause', 1/4),
        Note('g5',1/16),
        Note('pause', 1/16),
        Note('f5',1/8),
        Note('d5',1/16),
        Note('f5',1/16),
        Note('g5',1/16),
        
        Note('a#4',1/16),
        Note('a#4',1/16),
        Note('a5', 1/16),
        Note('pause', 1/8),
        Note('g#5',1/16),
        Note('pause', 1/4),
        Note('g5',1/16),
        Note('pause', 1/16),
        Note('f5',1/8),
        Note('d5',1/16),
        Note('f5',1/16),
        Note('g5',1/16)
        ]

tempo = 60

pwm_pin_4 = PWM(Pin(4))
pwm_pin_4.freq(4000)
pwm_pin_4.duty(0)

for i in tune:
    print('Frequency of ', i.freq(), 'played for ', 1000/tempo*i.dur(), 'ms with duty of ', i.dut())
    
    pwm_pin_4.freq(i.freq())
    pwm_pin_4.duty(i.dut())
    time.sleep_ms(int(100000/tempo*i.dur()))
    
pwm_pin_4.duty(0)
 