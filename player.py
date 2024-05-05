from machine import Pin, PWM, Timer
import time

# local
import values
from note import Note
from tunes import TEST

class Player:
    def __init__(self, buzzer: Buzzer, tune , tempo: int = 120):
        self.__buzzer = buzzer
        self.__tune = tune
        self.__beat = 60000*4/tempo
        self.__end_cut = 10
        self.__timer = Timer(0)
        self.__iter = 0

    def tempo(self, tempo: int) -> None:
        self.__beat = 60000*4/tempo

    def timer(self, timer: Timer) -> None:
        self.__timer = timer

    def __silence(self, a):
        self.__buzzer.reset()
        self.__iter += 1

        self.__timer.init(period = self.__end_cut,
                   mode = Timer.ONE_SHOT, callback = self.play)


    def play(self, a) -> None:
        if self.__iter < len(self.__tune):
            i = self.__tune[self.__iter]
            self.__buzzer.freq(i.freq())
            self.__buzzer.vol(i.vol())

            self.__timer.init(period = int(self.__beat * i.dur() - self.__end_cut),
                       mode = Timer.ONE_SHOT, callback = self.__silence)

