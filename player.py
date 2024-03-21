from machine import Pin, PWM
import time

# local
import notes
from notes import Note
from tunes import TEST

# initial values
player_pin = PWM(Pin(33))
player_pin.freq(4000)
player_pin.duty(0)

# it is necessary to add small intervals of silence,
# so individual notes may be heard
end_cut = 10     # ms

# play
tempo = 120

# calculates lenght of a single beat in miliseconds
beat = 60000*4/tempo

for i in TEST:
    # print('Frequency of ', i.freq(),
    # 'played for ', 1000/tempo*i.dur(),
    # 'ms with duty of ', i.dut())
    
    player_pin.freq(i.freq())
    player_pin.duty(i.dut())
    time.sleep_ms(int(beat*i.dur() - end_cut))

    # the silent part
    player_pin.duty(0)
    time.sleep_ms(end_cut)
    
# volume 0
player_pin.duty(0)
 
