# ESP Music
A crappy code allowing you to play melody though buzzer.
It is primarily meant for ESP32-WROOM-32E, but should work on other microcontrollers as well, but may require some modifications.

## Todo
- [ ] Use universal duty cycle
- [ ] Make class for handling buzzer
- [ ] Rewrite `note.py` so that it uses buzzer and volume from 0 to 100
- [X] Fix two consecutive notes sounding as one (small delay)
