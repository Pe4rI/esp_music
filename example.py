import music
from tunes import TEST

player = music.Player(music.Buzzer(33), TEST, 120)
player.play(a=0)
