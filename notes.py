from values import VALUES

class Note:
    """Class for handling musical notes"""

    def __init__(self, value: str, duration: float, duty=512):
        """A constructor of the class
        
        Parameters
        ----------
        value : str
            The name of a note (example: c3, a#4)
        duration : float
            The duration of a note written as a fraction of a single beat.
        """

        self.__freq = VALUES[value]
        self.__dur = duration
        if value == 'pause':
            self.__duty = 0
        else:
            self.__duty = duty

    def freq(self) -> int:
        """Returns note's frequency

        Returns
        -------
        int
            a frequency of the note
        """

        return self.__freq

    def dur(self) -> int:
        """Returns note's duration as a fraction of a beat

        Returns
        -------
        int
            the duration of the note
        """

        return self.__dur

    def dut(self) -> int:
        """Returns note's duty

        Returns
        -------
        int
            the duty of the note
        """

        return self.__duty
