VALUES = {
        'pause': 200,
        'c0':   16,
        'c#0':  17,
        'd0':   18,
        'd#0':  19,
        'e0':   20,
        'f0':   22,
        'f#0':  23,
        'g0':   25,
        'g#0':  26,
        'a0':   27,
        'a#0':  29,
        'b0':   31,
        'c1':   33,
        'c#1':  35,
        'd1':   37,
        'd#1':  39,
        'e1':   41,
        'f1':   44,
        'f#1':  46,
        'g1':   49,
        'g#1':  52,
        'a1':   55,
        'a#1':  58,
        'b1':   62,
        'c2':   66,
        'c#2':  69,
        'd2':   73,
        'd#2':  78,
        'e2':   83,
        'f2':   87,
        'f#2':  93,
        'g2':   98,
        'g#2':  104,
        'a2':   110,
        'a#2':  117,
        'b2':   124,
        'c3':   131,
        'c#3':  139,
        'd3':   147,
        'd#3':  156,
        'e3':   165,
        'f3':   175,
        'f#3':  185,
        'g3':   196,
        'g#3':  208,
        'a3':   220,
        'a#3':  233,
        'b3':   247,
        'c4':   262,
        'c#4':  277,
        'd4':   294,
        'd#4':  311,
        'e4':   330,
        'f4':   350,
        'f#4':  370,
        'g4':   392,
        'g#4':  415,
        'a4':   440,
        'a#4':  466,
        'b4':   494,
        'c5':   523,
        'c#5':  554,
        'd5':   587,
        'd#5':  622,
        'e5':   659,
        'f5':   699,
        'f#5':  740,
        'g5':   784,
        'g#5':  831,
        'a5':   880,
        'a#5':  932,
        'b5':   988,
        'c6':   1046,
        'c#6':  1109,
        'd6':   1175,
        'd#6':  1245,
        'e6':   1319,
        'f6':   1397,
        'f#6':  1480,
        'g6':   1568,
        'g#6':  1661,
        'a6':   1760,
        'a#6':  1865,
        'b6':   1976,
        'c7':   2093,
        'c#7':  2217,
        'd7':   2349,
        'd#7':  2489,
        'e7':   2637,
        'f7':   2794,
        'f#7':  2960,
        'g7':   3136,
        'g#7':  3322,
        'a7':   3520,
        'a#7':  3729,
        'b7':   3951,
        'c8':   4186,
        'c#8':  4435,
        'd8':   4699,
        'd#8':  4978,
        'e8':   5274,
        'f8':   5588,
        'f#8':  5920,
        'g8':   6272,
        'g#8':  6645,
        'a8':   7040,
        'a#8':  7459,
        'b8':   7902
        }

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


