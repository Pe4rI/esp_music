from machine import Pin, PWM
from oper import clamp

class Buzzer:
    """A class for handling buzzer.
    """

    def __init__(self, pin: Pin):
        """Constructor.

        Args:
            pin (Pin): pin where the buzzer is connected
        """
        self.__pwm = PWM(pin, duty_u16 = 0, freq = 440)
        self.__uint16_max = 65535
        self.__volume = 0
        self.vol(self.__volume)

    def vol(self, volume: int) -> None:
        """Sets the volume (duty cycle).

        Args:
            volume (int): value between 0 and 100
        """
        self.__volume = clamp(volume, 0, 100)
        self.__pwm.duty_u16(int(self.__volume * self.__uint16_max * 0.01))

    def add_vol(self, value: int) -> None:
        """Adds the value to the current volume.

        Args:
            value (int): a value by which volume changes
        """
        self.__volume = clamp(self.__volume + value, 0, 100)
        self.__pwm.duty_u16(int(self.__volume * self.__uint16_max * 0.01))
        
    def get_vol(self) -> int:
        """Returns current volume.

        Returns:
            int: current volume
        """
        return self.__volume
        
    def freq(self, frequency: int) -> None:
        """Sets the frequency.

        Args:
            frequency (int): value between 1 and 30000
        """
        self.__pwm.freq(clamp(frequency, 1, 30000))

    def reset(self):
        self.__pwm.duty_u16(0)
        self.__pwm.freq(440)
