from player import Player
from buzzer import Buzzer
from tunes import TEST

player = Player(Buzzer(33), TEST, 120)
player.play(a=0)
